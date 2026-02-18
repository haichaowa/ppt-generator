# Templates module
from .base import BaseTemplate
from .cover import CoverTemplate
from .toc import TocTemplate
from .chapter import ChapterTemplate
from .content import ContentTemplate
from .two_column import TwoColumnTemplate
from .code import CodeTemplate
from .data import DataTemplate
from .timeline import TimelineTemplate
from .grid import GridTemplate
from .quote import QuoteTemplate
from .end import EndTemplate

__all__ = [
    'BaseTemplate',
    'CoverTemplate',
    'TocTemplate',
    'ChapterTemplate',
    'ContentTemplate',
    'TwoColumnTemplate',
    'CodeTemplate',
    'DataTemplate',
    'TimelineTemplate',
    'GridTemplate',
    'QuoteTemplate',
    'EndTemplate',
]

# 模板注册表
TEMPLATE_MAP = {
    'cover': CoverTemplate,
    'toc': TocTemplate,
    'chapter': ChapterTemplate,
    'content': ContentTemplate,
    'two-column': TwoColumnTemplate,
    'code': CodeTemplate,
    'data': DataTemplate,
    'timeline': TimelineTemplate,
    'grid': GridTemplate,
    'quote': QuoteTemplate,
    'end': EndTemplate,
}


def get_template(slide_type: str) -> BaseTemplate:
    """获取指定类型的模板实例"""
    template_class = TEMPLATE_MAP.get(slide_type, ContentTemplate)
    return template_class()
