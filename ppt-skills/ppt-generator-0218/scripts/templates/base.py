"""
模板基类 - 定义所有模板的接口
"""
from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseTemplate(ABC):
    """模板基类"""

    @abstractmethod
    def render(self, slide_data: Dict[str, Any], theme: Any) -> str:
        """
        渲染幻灯片为 HTML

        Args:
            slide_data: 幻灯片数据（包含 content, meta 等）
            theme: 主题配置对象

        Returns:
            str: 渲染后的 HTML 字符串
        """
        pass

    def escape_html(self, text: str) -> str:
        """转义 HTML 特殊字符"""
        if not text:
            return ''
        return (
            text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;')
            .replace("'", '&#39;')
        )

    def parse_markdown_inline(self, text: str) -> str:
        """解析行内 Markdown 语法"""
        if not text:
            return ''

        # 转义 HTML
        text = self.escape_html(text)

        # 代码：`code`
        import re
        text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)

        # 粗体：**text**
        text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)

        # 斜体：*text*
        text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)

        return text

    def parse_list_items(self, content: str) -> list:
        """解析列表项"""
        items = []
        for line in content.split('\n'):
            line = line.strip()
            if line.startswith('- '):
                items.append(self.parse_markdown_inline(line[2:]))
        return items

    def get_css_var(self, theme: Any, var_name: str, default: str = '') -> str:
        """获取主题 CSS 变量"""
        if hasattr(theme, 'colors') and hasattr(theme.colors, var_name):
            return getattr(theme.colors, var_name)
        if hasattr(theme, 'css_vars') and var_name in theme.css_vars:
            return theme.css_vars[var_name]
        return default
