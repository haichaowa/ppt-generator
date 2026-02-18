"""
双栏页模板
"""
from .base import BaseTemplate
from typing import Dict, Any


class TwoColumnTemplate(BaseTemplate):
    """双栏页模板"""

    def render(self, slide_data: Dict[str, Any], theme: Any) -> str:
        """
        渲染双栏页

        结构：
        - 顶部标题
        - 左栏：标题 + 描述 + 列表
        - 右栏：标题 + 描述 + 列表
        """
        content = slide_data.get('content', '')

        # 解析内容
        title = ''
        left_content = {}
        right_content = {}

        # 按 --- 分割
        parts = content.split('\n---\n')

        if len(parts) >= 2:
            # 解析顶部标题
            lines = parts[0].strip().split('\n')
            for line in lines:
                line = line.strip()
                if line.startswith('## '):
                    title = self.parse_markdown_inline(line[3:].strip())
                    break

            # 解析左栏
            left_content = self._parse_column(parts[0])

            # 解析右栏
            right_content = self._parse_column(parts[1])
        else:
            # 如果没有分隔符，尝试解析整个内容
            left_content = self._parse_column(content)

        # 获取主题颜色
        primary_color = self.get_css_var(theme, 'primary', '#00f5ff')
        secondary_color = self.get_css_var(theme, 'secondary', '#bf00ff')

        html = f'''        <section class="slide two-column" data-type="two-column">
            <div class="slide-content">
                <div class="two-column-container">
                    {self._render_title(title, primary_color)}
                    <div class="columns-wrapper">
                        {self._render_column(left_content, 'left', primary_color)}
                        {self._render_column(right_content, 'right', secondary_color)}
                    </div>
                </div>
            </div>
        </section>'''

        return html

    def _parse_column(self, content: str) -> dict:
        """解析单栏内容"""
        result = {
            'title': '',
            'description': '',
            'items': []
        }

        desc_lines = []

        for line in content.split('\n'):
            line = line.strip()

            if line.startswith('### '):
                result['title'] = self.parse_markdown_inline(line[4:].strip())
            elif line.startswith('- '):
                result['items'].append(self.parse_markdown_inline(line[2:].strip()))
            elif line and not line.startswith('#') and not line.startswith('---'):
                desc_lines.append(self.parse_markdown_inline(line))

        result['description'] = ' '.join(desc_lines)

        return result

    def _render_title(self, title: str, color: str) -> str:
        """渲染顶部标题"""
        if not title:
            return ''
        return f'''                    <h2 class="two-column-title neon-text" style="--neon-color: {color}">
                        {title}
                    </h2>'''

    def _render_column(self, column: dict, position: str, color: str) -> str:
        """渲染单栏"""
        if not column:
            return ''

        title_html = ''
        if column.get('title'):
            title_html = f'''                        <h3 class="column-title" style="color: {color}">
                            {column['title']}
                        </h3>'''

        desc_html = ''
        if column.get('description'):
            desc_html = f'''                        <p class="column-description">
                            {column['description']}
                        </p>'''

        items_html = ''
        if column.get('items'):
            item_htmls = []
            for item in column['items']:
                item_htmls.append(f'                            <li class="column-item">{item}</li>')
            items_html = f'''                        <ul class="column-list">
{chr(10).join(item_htmls)}
                        </ul>'''

        return f'''                    <div class="column column-{position} glass-card">
                        {title_html}
                        {desc_html}
                        {items_html}
                    </div>'''
