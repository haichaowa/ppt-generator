"""
幻灯片解析器 - 解析 Markdown 为幻灯片数据结构
"""
import re
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any


@dataclass
class Slide:
    """幻灯片数据结构"""
    slide_type: str
    content: str
    meta: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        """初始化后处理"""
        if not self.meta:
            self.meta = {}


class SlideParser:
    """解析 Markdown 文件为幻灯片列表"""

    # 幻灯片类型标记正则 (支持带连字符的类型名，如 two-column)
    SLIDE_TYPE_PATTERN = re.compile(
        r'<!--\s*\.slide:\s*type=([\w-]+)\s*-->',
        re.IGNORECASE
    )

    def __init__(self):
        self.type_inferer = None  # 延迟导入避免循环依赖

    def parse(self, md_content: str, auto_infer: bool = False) -> List[Slide]:
        """
        解析 Markdown 内容为幻灯片列表

        Args:
            md_content: Markdown 内容
            auto_infer: 是否自动推断未标记类型的幻灯片

        Returns:
            List[Slide]: 幻灯片列表
        """
        slides = []

        # 按 <!-- .slide: type=xxx --> 分割
        parts = self._split_by_slide_marker(md_content)

        for part in parts:
            part = part.strip()
            if not part:
                continue

            # 解析类型
            slide_type, content = self._parse_slide_type(part)

            # 如果没有明确标记，尝试自动推断
            if slide_type is None and auto_infer:
                if self.type_inferer is None:
                    from .type_infer import TypeInferer
                    self.type_inferer = TypeInferer()
                slide_type = self.type_inferer.infer(content)

            # 默认类型为 content
            if slide_type is None:
                slide_type = 'content'

            # 解析元数据
            meta = self._parse_meta(content, slide_type)

            slides.append(Slide(
                slide_type=slide_type,
                content=content,
                meta=meta
            ))

        return slides

    def _split_by_slide_marker(self, content: str) -> List[str]:
        """按幻灯片标记分割内容"""
        # 查找所有幻灯片标记位置
        markers = list(self.SLIDE_TYPE_PATTERN.finditer(content))

        if not markers:
            # 没有标记，整个内容作为一个幻灯片
            return [content] if content.strip() else []

        parts = []

        # 处理第一个标记之前的内容
        if markers[0].start() > 0:
            before = content[:markers[0].start()].strip()
            if before:
                parts.append(before)

        # 处理各标记之间的内容
        for i, marker in enumerate(markers):
            start = marker.start()
            if i + 1 < len(markers):
                end = markers[i + 1].start()
            else:
                end = len(content)

            part = content[start:end].strip()
            if part:
                parts.append(part)

        return parts

    def _parse_slide_type(self, content: str) -> tuple:
        """
        解析幻灯片类型

        Returns:
            tuple: (slide_type, content_without_marker)
        """
        match = self.SLIDE_TYPE_PATTERN.match(content)

        if match:
            slide_type = match.group(1).lower()
            # 移除标记行
            remaining = content[match.end():].strip()
            return slide_type, remaining

        return None, content

    def _parse_meta(self, content: str, slide_type: str) -> Dict[str, Any]:
        """
        解析幻灯片元数据

        Args:
            content: 幻灯片内容
            slide_type: 幻灯片类型

        Returns:
            Dict: 元数据字典
        """
        meta = {}

        if slide_type == 'cover':
            meta.update(self._parse_cover_meta(content))
        elif slide_type == 'chapter':
            meta.update(self._parse_chapter_meta(content))
        elif slide_type == 'two-column':
            meta.update(self._parse_two_column_meta(content))
        elif slide_type == 'timeline':
            meta.update(self._parse_timeline_meta(content))
        elif slide_type == 'grid':
            meta.update(self._parse_grid_meta(content))
        elif slide_type == 'data':
            meta.update(self._parse_data_meta(content))
        elif slide_type == 'end':
            meta.update(self._parse_end_meta(content))

        return meta

    def _parse_cover_meta(self, content: str) -> Dict[str, Any]:
        """解析封面页元数据"""
        meta = {}

        lines = content.split('\n')

        # 查找标题
        for i, line in enumerate(lines):
            line = line.strip()
            if line.startswith('# ') and not line.startswith('## '):
                meta['title'] = line[2:].strip()
            elif line.startswith('## '):
                meta['subtitle'] = line[3:].strip()
            elif '|' in line and not line.startswith('-'):
                # 底部元数据行：作者 | 日期
                parts = [p.strip() for p in line.split('|')]
                if len(parts) >= 1:
                    meta['author'] = parts[0]
                if len(parts) >= 2:
                    meta['date'] = parts[1]

        return meta

    def _parse_chapter_meta(self, content: str) -> Dict[str, Any]:
        """解析章节页元数据"""
        meta = {}

        lines = content.split('\n')

        for line in lines:
            line = line.strip()
            if line.startswith('# ') and not line.startswith('## '):
                # 提取数字
                text = line[2:].strip()
                if text.isdigit():
                    meta['number'] = text
                else:
                    # 可能是 "01" 格式
                    match = re.match(r'^(\d+)', text)
                    if match:
                        meta['number'] = match.group(1)
            elif line.startswith('## '):
                meta['title'] = line[3:].strip()

        return meta

    def _parse_two_column_meta(self, content: str) -> Dict[str, Any]:
        """解析双栏页元数据"""
        meta = {'left': {}, 'right': {}}

        # 按 --- 分割
        parts = content.split('\n---\n')

        if len(parts) >= 2:
            # 解析左侧
            meta['left'] = self._parse_column_content(parts[0])
            # 解析右侧
            meta['right'] = self._parse_column_content(parts[1])

            # 提取顶部标题
            if parts[0]:
                lines = parts[0].strip().split('\n')
                for line in lines:
                    line = line.strip()
                    if line.startswith('## '):
                        meta['title'] = line[3:].strip()
                        break

        return meta

    def _parse_column_content(self, content: str) -> Dict[str, Any]:
        """解析单栏内容"""
        result = {'title': '', 'content': '', 'items': []}

        lines = content.strip().split('\n')
        content_lines = []
        in_items = False

        for line in lines:
            line = line.strip()

            if line.startswith('### '):
                result['title'] = line[4:].strip()
            elif line.startswith('- '):
                in_items = True
                result['items'].append(line[2:].strip())
            elif line and not line.startswith('#') and not line.startswith('---'):
                content_lines.append(line)

        result['content'] = ' '.join(content_lines)

        return result

    def _parse_timeline_meta(self, content: str) -> Dict[str, Any]:
        """解析时间轴页元数据"""
        meta = {'items': []}

        lines = content.split('\n')
        current_item = None

        for line in lines:
            line = line.strip()

            if line.startswith('## '):
                meta['title'] = line[3:].strip()
            elif line.startswith('### '):
                # 新的时间节点
                if current_item:
                    meta['items'].append(current_item)

                # 解析 "### 2020.01 项目启动" 格式
                text = line[4:].strip()
                match = re.match(r'^([\d\.\/\-\u4e00-\u9fa5年月]+)\s+(.+)$', text)
                if match:
                    current_item = {
                        'date': match.group(1).strip(),
                        'title': match.group(2).strip(),
                        'desc': ''
                    }
                else:
                    current_item = {
                        'date': '',
                        'title': text,
                        'desc': ''
                    }
            elif line and current_item and not line.startswith('#'):
                # 描述文字
                if current_item['desc']:
                    current_item['desc'] += ' ' + line
                else:
                    current_item['desc'] = line

        # 添加最后一个项目
        if current_item:
            meta['items'].append(current_item)

        return meta

    def _parse_grid_meta(self, content: str) -> Dict[str, Any]:
        """解析网格页元数据"""
        meta = {'cards': []}

        lines = content.split('\n')
        current_card = None

        for line in lines:
            line = line.strip()

            if line.startswith('## '):
                meta['title'] = line[3:].strip()
            elif line.startswith('### '):
                # 新的卡片
                if current_card:
                    meta['cards'].append(current_card)

                current_card = {
                    'title': line[4:].strip(),
                    'icon': '',
                    'color': 'cyan',
                    'desc': ''
                }
            elif line.startswith('- ') and current_card:
                # 解析属性：- icon: ◉
                prop_line = line[2:].strip()
                if ':' in prop_line:
                    key, value = prop_line.split(':', 1)
                    key = key.strip().lower()
                    value = value.strip()

                    if key == 'icon':
                        current_card['icon'] = value
                    elif key == 'color':
                        current_card['color'] = value
                    elif key == 'desc':
                        current_card['desc'] = value

        # 添加最后一个卡片
        if current_card:
            meta['cards'].append(current_card)

        return meta

    def _parse_data_meta(self, content: str) -> Dict[str, Any]:
        """解析数据页元数据"""
        meta = {'headers': [], 'rows': []}

        lines = content.split('\n')

        for line in lines:
            line = line.strip()

            if line.startswith('## '):
                meta['title'] = line[3:].strip()
            elif line.startswith('|') and '|' in line[1:]:
                # 表格行
                cells = [cell.strip() for cell in line.split('|')]
                # 移除首尾空元素
                cells = [c for c in cells if c or cells.index(c) not in [0, len(cells)-1]]
                cells = [c for c in cells if c]  # 只保留非空

                # 判断是否是分隔行
                if all(set(c.strip()) <= {'-', ':'} for c in cells if c.strip()):
                    continue  # 跳过分隔行

                if not meta['headers']:
                    meta['headers'] = cells
                else:
                    meta['rows'].append(cells)

        return meta

    def _parse_end_meta(self, content: str) -> Dict[str, Any]:
        """解析结束页元数据"""
        meta = {}

        lines = content.split('\n')

        for line in lines:
            line = line.strip()
            if line.startswith('# ') and not line.startswith('## '):
                meta['title'] = line[2:].strip()
            elif line.startswith('## '):
                meta['subtitle'] = line[3:].strip()
            elif '|' in line and not line.startswith('-'):
                parts = [p.strip() for p in line.split('|')]
                if len(parts) >= 1:
                    meta['author'] = parts[0]
                if len(parts) >= 2:
                    meta['contact'] = parts[1]

        return meta

    def parse_file(self, filepath: str, auto_infer: bool = False) -> List[Slide]:
        """
        解析 Markdown 文件

        Args:
            filepath: Markdown 文件路径
            auto_infer: 是否自动推断类型

        Returns:
            List[Slide]: 幻灯片列表
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        return self.parse(content, auto_infer)
