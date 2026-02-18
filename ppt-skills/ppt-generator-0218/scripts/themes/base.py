"""
主题基类 - 定义所有主题的接口
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class ThemeColors:
    """主题颜色配置"""
    primary: str = '#00f5ff'
    secondary: str = '#bf00ff'
    background: str = '#0a0a1a'
    text: str = '#ffffff'
    accent: str = '#ff006e'


class BaseTheme(ABC):
    """主题基类"""

    def __init__(self):
        self.name = 'base'
        self.colors = ThemeColors()
        self.css_vars = {}
        self.fonts = {}

    @abstractmethod
    def get_css(self) -> str:
        """
        获取主题 CSS 样式

        Returns:
            str: CSS 样式字符串
        """
        pass

    @abstractmethod
    def get_html_template(self) -> str:
        """
        获取 HTML 模板

        Returns:
            str: HTML 模板字符串
        """
        pass

    def get_css_variables(self) -> str:
        """生成 CSS 变量"""
        css_vars = []

        # 颜色变量
        css_vars.append(f'--primary-color: {self.colors.primary};')
        css_vars.append(f'--secondary-color: {self.colors.secondary};')
        css_vars.append(f'--background-color: {self.colors.background};')
        css_vars.append(f'--text-color: {self.colors.text};')
        css_vars.append(f'--accent-color: {self.colors.accent};')

        # 自定义变量
        for key, value in self.css_vars.items():
            css_vars.append(f'--{key}: {value};')

        return '\n    '.join(css_vars)

    def render_html(self, slides_html: str, title: str = 'PPT') -> str:
        """
        渲染完整的 HTML

        Args:
            slides_html: 所有幻灯片的 HTML
            title: 文档标题

        Returns:
            str: 完整的 HTML 字符串
        """
        template = self.get_html_template()

        return template.format(
            title=self._escape_html(title),
            css=self.get_css(),
            slides=slides_html
        )

    def _escape_html(self, text: str) -> str:
        """转义 HTML"""
        return (
            text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;')
            .replace("'", '&#39;')
        )
