"""
内容页模板
"""
from .base import BaseTemplate
from typing import Dict, Any


class ContentTemplate(BaseTemplate):
    """标准内容页模板"""

    def render(self, slide_data: Dict[str, Any], theme: Any) -> str:
        """
        渲染内容页

        结构：
        - 标题
        - 描述段落（可选）
        - 列表项
        """
        content = slide_data.get('content', '')

        # 解析内容
        title = ''
        description = ''
        items = []
        desc_lines = []

        for line in content.split('\n'):
            line = line.strip()
            if line.startswith('## '):
                title = self.parse_markdown_inline(line[3:].strip())
            elif line.startswith('- '):
                items.append(self.parse_markdown_inline(line[2:].strip()))
            elif line and not line.startswith('#'):
                desc_lines.append(self.parse_markdown_inline(line))

        description = ' '.join(desc_lines)

        # 获取主题颜色
        primary_color = self.get_css_var(theme, 'primary', '#00f5ff')

        html = f'''        <section class="slide content" data-type="content">
            <div class="slide-content">
                <div class="content-container glass-card">
                    {self._render_title(title, primary_color)}
                    {self._render_description(description)}
                    {self._render_items(items)}
                </div>
            </div>
        </section>'''

        return html

    def _render_title(self, title: str, color: str) -> str:
        """渲染标题"""
        if not title:
            return ''
        return f'''                    <h2 class="content-title neon-text" style="--neon-color: {color}">
                        {title}
                    </h2>'''

    def _render_description(self, description: str) -> str:
        """渲染描述段落"""
        if not description:
            return ''
        return f'''                    <p class="content-description">
                        {description}
                    </p>'''

    def _render_items(self, items: list) -> str:
        """渲染列表项"""
        if not items:
            return ''

        item_htmls = []
        for item in items:
            item_htmls.append(f'                        <li class="content-item">{item}</li>')

        items_html = '\n'.join(item_htmls)

        return f'''                    <ul class="content-list">
{items_html}
                    </ul>'''
