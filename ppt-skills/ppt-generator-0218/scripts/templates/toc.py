"""
目录页模板
"""
from .base import BaseTemplate
from typing import Dict, Any
import re


class TocTemplate(BaseTemplate):
    """目录页模板"""

    def render(self, slide_data: Dict[str, Any], theme: Any) -> str:
        """
        渲染目录页

        结构：
        - 标题（本期内容）
        - 编号列表项
        """
        meta = slide_data.get('meta', {})
        content = slide_data.get('content', '')

        # 解析标题
        title = '本期内容'
        for line in content.split('\n'):
            line = line.strip()
            if line.startswith('# ') and not line.startswith('## '):
                title = self.parse_markdown_inline(line[2:].strip())
                break

        # 解析目录项
        items = self._parse_items(content)

        # 获取主题颜色
        primary_color = self.get_css_var(theme, 'primary', '#00f5ff')

        html = f'''        <section class="slide toc" data-type="toc">
            <div class="slide-content">
                <div class="toc-container">
                    <h2 class="toc-title neon-text" style="--neon-color: {primary_color}">
                        {title}
                    </h2>
                    <div class="toc-items">
                        {self._render_items(items)}
                    </div>
                </div>
            </div>
        </section>'''

        return html

    def _parse_items(self, content: str) -> list:
        """解析目录项"""
        items = []

        for line in content.split('\n'):
            line = line.strip()
            if line.startswith('## '):
                text = line[3:].strip()

                # 尝试分离编号和内容
                match = re.match(r'^(\d+[\.\s、]*)\s*(.+)$', text)
                if match:
                    number = match.group(1).strip()
                    item_text = match.group(2).strip()
                    items.append({
                        'number': number,
                        'text': item_text
                    })
                else:
                    items.append({
                        'number': '',
                        'text': text
                    })

        return items

    def _render_items(self, items: list) -> str:
        """渲染目录项"""
        if not items:
            return ''

        item_htmls = []
        for i, item in enumerate(items):
            number = item.get('number', str(i + 1).zfill(2))
            text = self.parse_markdown_inline(item.get('text', ''))

            item_html = f'''                        <div class="toc-item">
                            <span class="toc-number">{self.escape_html(number)}</span>
                            <span class="toc-text">{text}</span>
                        </div>'''
            item_htmls.append(item_html)

        return '\n'.join(item_htmls)
