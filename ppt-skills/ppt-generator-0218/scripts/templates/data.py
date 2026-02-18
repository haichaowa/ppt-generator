"""
数据页模板
"""
from .base import BaseTemplate
from typing import Dict, Any
import re


class DataTemplate(BaseTemplate):
    """数据页模板"""

    def render(self, slide_data: Dict[str, Any], theme: Any) -> str:
        """
        渲染数据页

        结构：
        - 标题
        - 数据表格
        """
        meta = slide_data.get('meta', {})
        content = slide_data.get('content', '')

        # 从 meta 获取解析好的数据
        title = meta.get('title', '')
        headers = meta.get('headers', [])
        rows = meta.get('rows', [])

        # 如果没有，从 content 解析
        if not title:
            for line in content.split('\n'):
                line = line.strip()
                if line.startswith('## '):
                    title = self.parse_markdown_inline(line[3:].strip())
                    break

        if not headers or not rows:
            headers, rows = self._parse_table(content)

        # 获取主题颜色
        primary_color = self.get_css_var(theme, 'primary', '#00f5ff')
        table_bg = self.get_css_var(theme, 'table_bg', 'rgba(0, 245, 255, 0.05)')

        html = f'''        <section class="slide data" data-type="data">
            <div class="slide-content">
                <div class="data-container">
                    {self._render_title(title, primary_color)}
                    {self._render_table(headers, rows, table_bg)}
                </div>
            </div>
        </section>'''

        return html

    def _parse_table(self, content: str) -> tuple:
        """解析 Markdown 表格"""
        headers = []
        rows = []

        for line in content.split('\n'):
            line = line.strip()

            if line.startswith('|') and '|' in line[1:]:
                # 解析表格行
                cells = [c.strip() for c in line.split('|')]
                # 移除首尾空元素
                cells = [c for c in cells if c]

                # 判断是否是分隔行
                if all(set(c) <= {'-', ':', ' '} for c in cells if c):
                    continue  # 跳过分隔行

                if not headers:
                    headers = cells
                else:
                    rows.append(cells)

        return headers, rows

    def _render_title(self, title: str, color: str) -> str:
        """渲染标题"""
        if not title:
            return ''
        return f'''                    <h2 class="data-title neon-text" style="--neon-color: {color}">
                        {title}
                    </h2>'''

    def _render_table(self, headers: list, rows: list, bg_color: str) -> str:
        """渲染数据表格"""
        if not headers and not rows:
            return ''

        # 渲染表头
        header_htmls = []
        for header in headers:
            header_htmls.append(f'                            <th class="data-header">{self.parse_markdown_inline(header)}</th>')
        header_html = '\n'.join(header_htmls)

        # 渲染数据行
        row_htmls = []
        for row in rows:
            cell_htmls = []
            for cell in row:
                cell_htmls.append(f'                                <td class="data-cell">{self.parse_markdown_inline(cell)}</td>')
            cell_html = '\n'.join(cell_htmls)
            row_htmls.append(f'''                        <tr class="data-row">
{cell_html}
                        </tr>''')

        rows_html = '\n'.join(row_htmls)

        return f'''                    <div class="data-table-wrapper glass-card" style="background: {bg_color}">
                        <table class="data-table">
                            <thead>
                                <tr class="data-header-row">
{header_html}
                                </tr>
                            </thead>
                            <tbody>
{rows_html}
                            </tbody>
                        </table>
                    </div>'''
