"""
章节页模板
"""
from .base import BaseTemplate
from typing import Dict, Any
import re


class ChapterTemplate(BaseTemplate):
    """章节页模板"""

    def render(self, slide_data: Dict[str, Any], theme: Any) -> str:
        """
        渲染章节页

        结构：
        - 大号数字
        - 章节名称
        """
        meta = slide_data.get('meta', {})
        content = slide_data.get('content', '')

        # 解析内容
        number = meta.get('number', '')
        title = meta.get('title', '')

        # 如果没有从 meta 中解析到，尝试从 content 解析
        if not number or not title:
            for line in content.split('\n'):
                line = line.strip()
                if line.startswith('# ') and not line.startswith('## '):
                    text = line[2:].strip()
                    # 提取数字
                    match = re.match(r'^(\d+)', text)
                    if match:
                        number = match.group(1)
                elif line.startswith('## '):
                    title = self.parse_markdown_inline(line[3:].strip())

        # 获取主题颜色
        primary_color = self.get_css_var(theme, 'primary', '#00f5ff')
        secondary_color = self.get_css_var(theme, 'secondary', '#bf00ff')

        html = f'''        <section class="slide chapter" data-type="chapter">
            <div class="slide-content">
                <div class="chapter-container">
                    <div class="chapter-number neon-text" style="--neon-color: {primary_color}">
                        {self.escape_html(number)}
                    </div>
                    <h2 class="chapter-title" style="color: {secondary_color}">
                        {title}
                    </h2>
                </div>
            </div>
        </section>'''

        return html
