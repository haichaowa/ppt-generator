"""
类型推断器 - 根据内容特征自动推断幻灯片类型
"""
import re
from typing import Optional


class TypeInferer:
    """自动推断幻灯片类型"""

    # 类型推断规则
    RULES = [
        # (类型, 检测函数, 优先级)
        ('cover', '_check_cover', 10),
        ('end', '_check_end', 10),
        ('toc', '_check_toc', 8),
        ('chapter', '_check_chapter', 8),
        ('two-column', '_check_two_column', 7),
        ('code', '_check_code', 7),
        ('data', '_check_data', 7),
        ('timeline', '_check_timeline', 6),
        ('grid', '_check_grid', 6),
        ('quote', '_check_quote', 5),
        ('content', '_check_content', 1),
    ]

    def __init__(self):
        pass

    def infer(self, content: str) -> str:
        """
        根据内容特征推断幻灯片类型

        Args:
            content: 幻灯片内容

        Returns:
            str: 推断的类型
        """
        # 按优先级排序规则
        sorted_rules = sorted(self.RULES, key=lambda x: x[2], reverse=True)

        for slide_type, check_method, _ in sorted_rules:
            check_func = getattr(self, check_method)
            if check_func(content):
                return slide_type

        return 'content'

    def _check_cover(self, content: str) -> bool:
        """检测是否为封面页"""
        lines = [l.strip() for l in content.split('\n') if l.strip()]

        # 特征：只有标题和少量元数据
        has_h1 = any(l.startswith('# ') and not l.startswith('## ') for l in lines)
        has_h2 = any(l.startswith('## ') for l in lines)
        has_meta = any('|' in l and not l.startswith('|') for l in lines)
        line_count = len(lines)

        # 封面通常：有 H1，行数少（3-5行），可能有 H2 和元数据
        return has_h1 and line_count <= 6 and (has_h2 or has_meta)

    def _check_end(self, content: str) -> bool:
        """检测是否为结束页"""
        content_lower = content.lower()

        # 特征：包含感谢、关注等关键词
        end_keywords = [
            '感谢', '谢谢', 'thanks', 'thank you',
            '关注', '点赞', '订阅', 'follow', 'subscribe',
            '联系', 'contact', '二维码'
        ]

        has_end_keyword = any(kw in content_lower for kw in end_keywords)
        has_h1 = '# ' in content and not content.strip().startswith('##')
        line_count = len([l for l in content.split('\n') if l.strip()])

        return has_end_keyword and has_h1 and line_count <= 6

    def _check_toc(self, content: str) -> bool:
        """检测是否为目录页"""
        lines = [l.strip() for l in content.split('\n') if l.strip()]

        # 特征：多个带编号的 H2 标题
        h2_lines = [l for l in lines if l.startswith('## ')]

        if len(h2_lines) >= 3:
            # 检查是否有编号模式
            numbered_count = 0
            for line in h2_lines:
                text = line[3:].strip()
                # 检查编号：01, 1., 一、等
                if re.match(r'^(\d+[\.\s、]|[\d一二三四五六七八九十]+[、\s])', text):
                    numbered_count += 1

            # 如果超过一半的 H2 有编号，很可能是目录
            return numbered_count >= len(h2_lines) * 0.5

        # 或者标题包含"目录"、"内容"等关键词
        content_lower = content.lower()
        toc_keywords = ['目录', '内容', '大纲', 'outline', 'contents', 'agenda']
        has_toc_keyword = any(kw in content_lower for kw in toc_keywords)

        return has_toc_keyword and len(h2_lines) >= 3

    def _check_chapter(self, content: str) -> bool:
        """检测是否为章节页"""
        lines = [l.strip() for l in content.split('\n') if l.strip()]

        # 特征：H1 只有数字，H2 是章节名
        has_h1 = False
        h1_is_number = False
        has_h2 = False

        for line in lines:
            if line.startswith('# ') and not line.startswith('## '):
                has_h1 = True
                text = line[2:].strip()
                # 检查是否只有数字
                h1_is_number = text.isdigit() or re.match(r'^[0]+$', text)
            elif line.startswith('## '):
                has_h2 = True

        # 章节页通常只有 2-4 行
        line_count = len(lines)

        return has_h1 and h1_is_number and has_h2 and line_count <= 4

    def _check_two_column(self, content: str) -> bool:
        """检测是否为双栏页"""
        # 特征：包含 --- 分隔符
        has_separator = '\n---\n' in content or '\n--- ' in content

        if has_separator:
            parts = content.split('\n---\n')
            if len(parts) >= 2:
                # 检查两侧是否有 H3 标题
                has_h3_left = '### ' in parts[0]
                has_h3_right = '### ' in parts[1] if len(parts) > 1 else False

                return has_h3_left or has_h3_right

        return False

    def _check_code(self, content: str) -> bool:
        """检测是否为代码页"""
        # 特征：包含围栏代码块
        code_block_pattern = r'```\w*\n'
        has_code_block = bool(re.search(code_block_pattern, content))

        return has_code_block

    def _check_data(self, content: str) -> bool:
        """检测是否为数据页"""
        lines = [l.strip() for l in content.split('\n') if l.strip()]

        # 特征：包含 Markdown 表格
        table_lines = [l for l in lines if l.startswith('|') and l.endswith('|')]

        # 至少有表头和一行数据
        if len(table_lines) >= 2:
            # 检查是否有分隔行
            has_separator = any(
                all(c in '-|: ' for c in line)
                for line in table_lines
            )
            return has_separator

        return False

    def _check_timeline(self, content: str) -> bool:
        """检测是否为时间轴页"""
        lines = [l.strip() for l in content.split('\n') if l.strip()]

        # 特征：多个 H3 标题，包含日期格式
        h3_lines = [l for l in lines if l.startswith('### ')]

        if len(h3_lines) >= 2:
            date_count = 0
            date_patterns = [
                r'\d{4}[.\-\/年]\d{1,2}',  # 2020.01, 2020-01, 2020年1月
                r'\d{1,2}[.\-\/月]\d{4}',  # 01.2020
            ]

            for line in h3_lines:
                text = line[4:].strip()
                for pattern in date_patterns:
                    if re.search(pattern, text):
                        date_count += 1
                        break

            # 如果超过一半的 H3 包含日期
            return date_count >= len(h3_lines) * 0.5

        return False

    def _check_grid(self, content: str) -> bool:
        """检测是否为网格页"""
        lines = [l.strip() for l in content.split('\n') if l.strip()]

        # 特征：4 或 9 个 H3 标题，每个包含 icon/color/desc 属性
        h3_count = sum(1 for l in lines if l.startswith('### '))

        # 只支持 4 或 9 个卡片
        if h3_count not in [4, 9]:
            return False

        # 检查是否有属性列表
        property_count = 0
        for line in lines:
            if line.startswith('- '):
                prop_line = line[2:].strip()
                if ':' in prop_line:
                    key = prop_line.split(':')[0].strip().lower()
                    if key in ['icon', 'color', 'desc']:
                        property_count += 1

        # 每个卡片应该有 3 个属性
        expected_properties = h3_count * 3

        return property_count >= expected_properties * 0.8

    def _check_quote(self, content: str) -> bool:
        """检测是否为金句页"""
        # 特征：包含引用块 >
        has_quote = False
        for line in content.split('\n'):
            line = line.strip()
            if line.startswith('> ') and not line.startswith('>> '):
                has_quote = True
                break

        return has_quote

    def _check_content(self, content: str) -> bool:
        """默认内容页"""
        # 其他所有情况都归为 content
        return True
