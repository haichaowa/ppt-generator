"""
时间轴页模板
"""
from .base import BaseTemplate
from typing import Dict, Any


class TimelineTemplate(BaseTemplate):
    """时间轴页模板"""

    def render(self, slide_data: Dict[str, Any], theme: Any) -> str:
        """
        渲染时间轴页

        结构：
        - 标题
        - 时间节点列表（日期 + 标题 + 描述）
        """
        meta = slide_data.get('meta', {})
        content = slide_data.get('content', '')

        # 从 meta 获取解析好的数据
        title = meta.get('title', '')
        items = meta.get('items', [])

        # 如果没有，从 content 解析
        if not title:
            for line in content.split('\n'):
                line = line.strip()
                if line.startswith('## '):
                    title = self.parse_markdown_inline(line[3:].strip())
                    break

        if not items:
            items = self._parse_timeline(content)

        # 获取主题颜色
        primary_color = self.get_css_var(theme, 'primary', '#00f5ff')
        secondary_color = self.get_css_var(theme, 'secondary', '#bf00ff')

        html = f'''        <section class="slide timeline" data-type="timeline">
            <div class="slide-content">
                <div class="timeline-container">
                    {self._render_title(title, primary_color)}
                    <div class="timeline-items">
                        {self._render_items(items, primary_color, secondary_color)}
                    </div>
                </div>
            </div>
        </section>'''

        return html

    def _parse_timeline(self, content: str) -> list:
        """解析时间轴内容"""
        items = []
        current_item = None

        import re

        for line in content.split('\n'):
            line = line.strip()

            if line.startswith('## '):
                continue  # 跳过标题

            if line.startswith('### '):
                # 保存上一个项目
                if current_item:
                    items.append(current_item)

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
            items.append(current_item)

        return items

    def _render_title(self, title: str, color: str) -> str:
        """渲染标题"""
        if not title:
            return ''
        return f'''                    <h2 class="timeline-title neon-text" style="--neon-color: {color}">
                        {title}
                    </h2>'''

    def _render_items(self, items: list, primary_color: str, secondary_color: str) -> str:
        """渲染时间轴项目"""
        if not items:
            return ''

        item_htmls = []
        for i, item in enumerate(items):
            date = item.get('date', '')
            title = self.parse_markdown_inline(item.get('title', ''))
            desc = self.parse_markdown_inline(item.get('desc', ''))

            # 交替使用颜色
            color = primary_color if i % 2 == 0 else secondary_color

            item_html = f'''                        <div class="timeline-item">
                            <div class="timeline-dot" style="background: {color}; box-shadow: 0 0 10px {color}"></div>
                            <div class="timeline-content glass-card">
                                <div class="timeline-date" style="color: {color}">{self.escape_html(date)}</div>
                                <div class="timeline-item-title">{title}</div>
                                {f'<div class="timeline-desc">{desc}</div>' if desc else ''}
                            </div>
                        </div>'''
            item_htmls.append(item_html)

        return '\n'.join(item_htmls)
