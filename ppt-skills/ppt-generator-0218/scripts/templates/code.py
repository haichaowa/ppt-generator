"""
代码页模板
"""
from .base import BaseTemplate
from typing import Dict, Any
import re


class CodeTemplate(BaseTemplate):
    """代码页模板"""

    def render(self, slide_data: Dict[str, Any], theme: Any) -> str:
        """
        渲染代码页

        结构：
        - 标题
        - 代码块（带语法高亮）
        - 代码说明
        """
        content = slide_data.get('content', '')

        # 解析内容
        title = ''
        code = ''
        language = ''
        description = ''

        # 解析代码块
        code_match = re.search(r'```(\w*)\n(.*?)```', content, re.DOTALL)
        if code_match:
            language = code_match.group(1) or 'plaintext'
            code = code_match.group(2).strip()

        # 解析标题和说明
        for line in content.split('\n'):
            line = line.strip()
            if line.startswith('## '):
                title = self.parse_markdown_inline(line[3:].strip())
            elif line.startswith('### ') and not code_match or (code_match and content.find(line) > code_match.end()):
                # 在代码块之后的 H3 是说明
                if code_match and content.find(line) > code_match.end():
                    description = self.parse_markdown_inline(line[4:].strip())
                elif not code_match:
                    description = self.parse_markdown_inline(line[4:].strip())

        # 获取主题颜色
        primary_color = self.get_css_var(theme, 'primary', '#00f5ff')
        code_bg = self.get_css_var(theme, 'code_bg', '#0a0a1a')

        html = f'''        <section class="slide code" data-type="code">
            <div class="slide-content">
                <div class="code-container">
                    {self._render_title(title, primary_color)}
                    {self._render_code(code, language, code_bg)}
                    {self._render_description(description)}
                </div>
            </div>
        </section>'''

        return html

    def _render_title(self, title: str, color: str) -> str:
        """渲染标题"""
        if not title:
            return ''
        return f'''                    <h2 class="code-title neon-text" style="--neon-color: {color}">
                        {title}
                    </h2>'''

    def _render_code(self, code: str, language: str, bg_color: str) -> str:
        """渲染代码块"""
        if not code:
            return ''

        # 转义 HTML
        code_escaped = self.escape_html(code)

        # 简单的语法高亮（可选）
        code_highlighted = self._highlight_code(code_escaped, language)

        return f'''                    <div class="code-block glass-card" style="background: {bg_color}">
                        <div class="code-header">
                            <span class="code-language">{self.escape_html(language)}</span>
                        </div>
                        <pre class="code-content"><code class="language-{self.escape_html(language)}">{code_highlighted}</code></pre>
                    </div>'''

    def _render_description(self, description: str) -> str:
        """渲染代码说明"""
        if not description:
            return ''
        return f'''                    <p class="code-description">
                        {description}
                    </p>'''

    def _highlight_code(self, code: str, language: str) -> str:
        """
        语法高亮

        注意：简单的正则高亮容易出现边界情况问题。
        如需更精确的高亮，建议：
        1. 使用 Pygments 库
        2. 或在前端使用 Prism.js / highlight.js

        当前实现：仅高亮关键字，避免字符串匹配破坏已添加的 span
        """
        # 先处理注释（注释中的关键字不应被高亮）
        # 使用占位符保护注释内容
        comments = []
        def save_comment(match):
            comments.append(match.group(1))
            return f'___COMMENT_{len(comments)-1}___'

        if language in ['python', 'py']:
            code = re.sub(r'(#.*)$', save_comment, code, flags=re.MULTILINE)
        elif language in ['javascript', 'js', 'typescript', 'ts']:
            code = re.sub(r'(//.*)$', save_comment, code, flags=re.MULTILINE)

        # 高亮关键字
        if language in ['python', 'py']:
            keywords = ['def', 'class', 'import', 'from', 'as', 'return', 'if', 'else',
                       'elif', 'for', 'while', 'try', 'except', 'finally', 'with',
                       'async', 'await', 'yield', 'lambda', 'pass', 'break', 'continue',
                       'True', 'False', 'None', 'and', 'or', 'not', 'in', 'is']
            keyword_pattern = r'\b(' + '|'.join(keywords) + r')\b'
            code = re.sub(keyword_pattern, r'<span class="keyword">\1</span>', code)

        elif language in ['javascript', 'js', 'typescript', 'ts']:
            keywords = ['function', 'const', 'let', 'var', 'return', 'if', 'else',
                       'for', 'while', 'class', 'import', 'export', 'from', 'async',
                       'await', 'try', 'catch', 'finally', 'new', 'this', 'true', 'false']
            keyword_pattern = r'\b(' + '|'.join(keywords) + r')\b'
            code = re.sub(keyword_pattern, r'<span class="keyword">\1</span>', code)

        # 恢复注释（带高亮）
        for i, comment in enumerate(comments):
            code = code.replace(f'___COMMENT_{i}___', f'<span class="comment">{comment}</span>')

        return code
