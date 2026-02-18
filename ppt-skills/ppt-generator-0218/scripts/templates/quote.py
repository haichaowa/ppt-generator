"""
金句页模板
"""
from .base import BaseTemplate
from typing import Dict, Any


class QuoteTemplate(BaseTemplate):
    """金句页模板"""

    def render(self, slide_data: Dict[str, Any], theme: Any) -> str:
        """
        渲染金句页

        结构：
        - 标题（可选）
        - 引用内容
        - 作者
        """
        content = slide_data.get('content', '')

        # 解析内容
        title = ''
        quote = ''
        author = ''

        for line in content.split('\n'):
            line = line.strip()

            if line.startswith('## '):
                title = self.parse_markdown_inline(line[3:].strip())
            elif line.startswith('> '):
                # 引用内容
                quote_text = line[2:].strip()
                if quote:
                    quote += '<br>' + self.parse_markdown_inline(quote_text)
                else:
                    quote = self.parse_markdown_inline(quote_text)
            elif line.startswith('### ') and quote:
                # 在引用之后的 H3 是作者
                author_text = line[4:].strip()
                # 去除可能的破折号前缀
                if author_text.startswith('—') or author_text.startswith('-'):
                    author_text = author_text[1:].strip()
                author = self.parse_markdown_inline(author_text)

        # 获取主题颜色
        primary_color = self.get_css_var(theme, 'primary', '#00f5ff')
        secondary_color = self.get_css_var(theme, 'secondary', '#bf00ff')

        html = f'''        <section class="slide quote" data-type="quote">
            <div class="slide-content">
                <div class="quote-container">
                    {self._render_title(title)}
                    {self._render_quote(quote, primary_color)}
                    {self._render_author(author, secondary_color)}
                </div>
            </div>
        </section>'''

        return html

    def _render_title(self, title: str) -> str:
        """渲染标题"""
        if not title:
            return ''
        return f'''                    <h2 class="quote-title">
                        {title}
                    </h2>'''

    def _render_quote(self, quote: str, color: str) -> str:
        """渲染引用内容"""
        if not quote:
            return ''

        return f'''                    <blockquote class="quote-text glass-card" style="border-left-color: {color}">
                        <p class="quote-content neon-text" style="--neon-color: {color}">
                            "{quote}"
                        </p>
                    </blockquote>'''

    def _render_author(self, author: str, color: str) -> str:
        """渲染作者"""
        if not author:
            return ''

        return f'''                    <div class="quote-author" style="color: {color}">
                        — {author}
                    </div>'''
