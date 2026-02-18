"""
封面页模板
"""
from .base import BaseTemplate
from typing import Dict, Any


class CoverTemplate(BaseTemplate):
    """封面页模板"""

    def render(self, slide_data: Dict[str, Any], theme: Any) -> str:
        """
        渲染封面页

        结构：
        - 主标题（大字）
        - 副标题（中字）
        - 底部元数据（作者 | 日期）
        """
        meta = slide_data.get('meta', {})
        content = slide_data.get('content', '')

        # 解析内容
        title = meta.get('title', '')
        subtitle = meta.get('subtitle', '')
        author = meta.get('author', '')
        date = meta.get('date', '')

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
                    if len(parts) >= 2 and not date:
                        date = parts[1]

        # 获取主题颜色
        primary_color = self.get_css_var(theme, 'primary', '#00f5ff')
        secondary_color = self.get_css_var(theme, 'secondary', '#bf00ff')

        html = f'''        <section class="slide cover" data-type="cover">
            <div class="slide-content">
                <div class="cover-container">
                    {self._render_title(title, primary_color)}
                    {self._render_subtitle(subtitle, secondary_color)}
                    {self._render_meta(author, date)}
                </div>
            </div>
        </section>'''

        return html

    def _render_title(self, title: str, color: str) -> str:
        """渲染主标题"""
        if not title:
            return ''
        return f'''                    <h1 class="cover-title neon-text" style="--neon-color: {color}">
                        {title}
                    </h1>'''

    def _render_subtitle(self, subtitle: str, color: str) -> str:
        """渲染副标题"""
        if not subtitle:
            return ''
        return f'''                    <h2 class="cover-subtitle">
                        {subtitle}
                    </h2>'''

    def _render_meta(self, author: str, date: str) -> str:
        """渲染底部元数据"""
        if not author and not date:
            return ''

        meta_parts = []
        if author:
            meta_parts.append(f'<span class="meta-author">{self.escape_html(author)}</span>')
        if date:
            meta_parts.append(f'<span class="meta-date">{self.escape_html(date)}</span>')

        meta_html = ' <span class="meta-separator">|</span> '.join(meta_parts)

        return f'''                    <div class="cover-meta">
                        {meta_html}
                    </div>'''
