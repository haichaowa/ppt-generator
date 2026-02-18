"""
结束页模板
"""
from .base import BaseTemplate
from typing import Dict, Any


class EndTemplate(BaseTemplate):
    """结束页模板"""

    def render(self, slide_data: Dict[str, Any], theme: Any) -> str:
        """
        渲染结束页

        结构：
        - 主标题（感谢观看）
        - 副标题（引导关注）
        - 底部元数据（作者 | 联系方式）
        """
        meta = slide_data.get('meta', {})
        content = slide_data.get('content', '')

        # 解析内容
        title = meta.get('title', '')
        subtitle = meta.get('subtitle', '')
        author = meta.get('author', '')
        contact = meta.get('contact', '')

        # 如果没有从 meta 中解析到，尝试从 content 解析
        if not title or not subtitle:
            for line in content.split('\n'):
                line = line.strip()
                if line.startswith('# ') and not line.startswith('## '):
                    title = self.parse_markdown_inline(line[2:].strip())
                elif line.startswith('## '):
                    subtitle = self.parse_markdown_inline(line[3:].strip())
                elif '|' in line and not line.startswith('-') and not line.startswith('|'):
                    parts = [p.strip() for p in line.split('|')]
                    if len(parts) >= 1 and not author:
                        author = parts[0]
                    if len(parts) >= 2 and not contact:
                        contact = parts[1]

        # 获取主题颜色
        primary_color = self.get_css_var(theme, 'primary', '#00f5ff')
        secondary_color = self.get_css_var(theme, 'secondary', '#bf00ff')

        html = f'''        <section class="slide end" data-type="end">
            <div class="slide-content">
                <div class="end-container">
                    {self._render_title(title, primary_color)}
                    {self._render_subtitle(subtitle, secondary_color)}
                    {self._render_meta(author, contact)}
                </div>
            </div>
        </section>'''

        return html

    def _render_title(self, title: str, color: str) -> str:
        """渲染主标题"""
        if not title:
            title = '感谢观看'
        return f'''                    <h1 class="end-title neon-text" style="--neon-color: {color}">
                        {title}
                    </h1>'''

    def _render_subtitle(self, subtitle: str, color: str) -> str:
        """渲染副标题"""
        if not subtitle:
            subtitle = '点赞关注不迷路'
        return f'''                    <h2 class="end-subtitle" style="color: {color}">
                        {subtitle}
                    </h2>'''

    def _render_meta(self, author: str, contact: str) -> str:
        """渲染底部元数据"""
        if not author and not contact:
            return ''

        meta_parts = []
        if author:
            meta_parts.append(f'<span class="meta-author">{self.escape_html(author)}</span>')
        if contact:
            meta_parts.append(f'<span class="meta-contact">{self.escape_html(contact)}</span>')

        meta_html = ' <span class="meta-separator">|</span> '.join(meta_parts)

        return f'''                    <div class="end-meta">
                        {meta_html}
                    </div>'''
