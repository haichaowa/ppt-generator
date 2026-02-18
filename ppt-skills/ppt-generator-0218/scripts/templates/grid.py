"""
网格页模板
"""
from .base import BaseTemplate
from typing import Dict, Any


class GridTemplate(BaseTemplate):
    """网格页模板"""

    # 颜色映射
    COLOR_MAP = {
        'cyan': '#00f5ff',
        'purple': '#bf00ff',
        'pink': '#ff006e',
        'orange': '#ff9500',
        'green': '#00ff88',
        'blue': '#0066ff',
        'red': '#ff0055',
        'yellow': '#ffcc00',
    }

    def render(self, slide_data: Dict[str, Any], theme: Any) -> str:
        """
        渲染网格页

        结构：
        - 标题
        - 网格卡片（2x2 或 3x3）
        """
        meta = slide_data.get('meta', {})
        content = slide_data.get('content', '')

        # 从 meta 获取解析好的数据
        title = meta.get('title', '')
        cards = meta.get('cards', [])

        # 如果没有，从 content 解析
        if not title:
            for line in content.split('\n'):
                line = line.strip()
                if line.startswith('## '):
                    title = self.parse_markdown_inline(line[3:].strip())
                    break

        if not cards:
            cards = self._parse_cards(content)

        # 确定网格布局
        grid_class = 'grid-2x2' if len(cards) == 4 else 'grid-3x3'

        html = f'''        <section class="slide grid" data-type="grid">
            <div class="slide-content">
                <div class="grid-container">
                    {self._render_title(title)}
                    <div class="grid-cards {grid_class}">
                        {self._render_cards(cards)}
                    </div>
                </div>
            </div>
        </section>'''

        return html

    def _parse_cards(self, content: str) -> list:
        """解析网格卡片"""
        cards = []
        current_card = None

        for line in content.split('\n'):
            line = line.strip()

            if line.startswith('## '):
                continue  # 跳过标题

            if line.startswith('### '):
                # 保存上一个卡片
                if current_card:
                    cards.append(current_card)

                current_card = {
                    'title': self.parse_markdown_inline(line[4:].strip()),
                    'icon': '',
                    'color': 'cyan',
                    'desc': ''
                }
            elif line.startswith('- ') and current_card:
                # 解析属性
                prop_line = line[2:].strip()
                if ':' in prop_line:
                    key, value = prop_line.split(':', 1)
                    key = key.strip().lower()
                    value = value.strip()

                    if key == 'icon':
                        current_card['icon'] = value
                    elif key == 'color':
                        current_card['color'] = value
                    elif key == 'desc':
                        current_card['desc'] = value

        # 添加最后一个卡片
        if current_card:
            cards.append(current_card)

        return cards

    def _render_title(self, title: str) -> str:
        """渲染标题"""
        if not title:
            return ''
        return f'''                    <h2 class="grid-title">
                        {title}
                    </h2>'''

    def _render_cards(self, cards: list) -> str:
        """渲染网格卡片"""
        if not cards:
            return ''

        card_htmls = []
        for card in cards:
            title = card.get('title', '')
            icon = card.get('icon', '◉')
            color_name = card.get('color', 'cyan')
            desc = card.get('desc', '')

            # 获取实际颜色值
            color = self.COLOR_MAP.get(color_name, '#00f5ff')

            card_html = f'''                        <div class="grid-card glass-card" style="--card-color: {color}">
                            <div class="card-icon" style="color: {color}; text-shadow: 0 0 20px {color}">
                                {self.escape_html(icon)}
                            </div>
                            <div class="card-title">{title}</div>
                            {f'<div class="card-desc">{self.parse_markdown_inline(desc)}</div>' if desc else ''}
                        </div>'''
            card_htmls.append(card_html)

        return '\n'.join(card_htmls)
