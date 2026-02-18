# Themes module
from .base import BaseTheme
from .neon import NeonTheme

__all__ = ['BaseTheme', 'NeonTheme']

# 主题注册表
THEME_MAP = {
    'neon': NeonTheme,
}


def get_theme(theme_name: str = 'neon') -> BaseTheme:
    """获取主题实例"""
    theme_class = THEME_MAP.get(theme_name, NeonTheme)
    return theme_class()
