"""
工具函数模块
"""
import os
from datetime import datetime
from typing import Optional


def read_file(filepath: str, encoding: str = 'utf-8') -> str:
    """
    读取文件内容

    Args:
        filepath: 文件路径
        encoding: 编码格式

    Returns:
        str: 文件内容
    """
    with open(filepath, 'r', encoding=encoding) as f:
        return f.read()


def write_file(filepath: str, content: str, encoding: str = 'utf-8') -> None:
    """
    写入文件内容

    Args:
        filepath: 文件路径
        content: 文件内容
        encoding: 编码格式
    """
    # 确保目录存在
    ensure_dir(os.path.dirname(filepath))

    with open(filepath, 'w', encoding=encoding) as f:
        f.write(content)


def ensure_dir(dirpath: Optional[str]) -> None:
    """
    确保目录存在，不存在则创建

    Args:
        dirpath: 目录路径
    """
    if dirpath and not os.path.exists(dirpath):
        os.makedirs(dirpath, exist_ok=True)


def get_timestamp(fmt: str = '%Y%m%d_%H%M%S') -> str:
    """
    获取当前时间戳字符串

    Args:
        fmt: 时间格式

    Returns:
        str: 格式化的时间戳
    """
    return datetime.now().strftime(fmt)


def get_file_basename(filepath: str) -> str:
    """
    获取文件基础名称（不含扩展名）

    Args:
        filepath: 文件路径

    Returns:
        str: 文件基础名称
    """
    basename = os.path.basename(filepath)
    return os.path.splitext(basename)[0]


def is_valid_md_file(filepath: str) -> bool:
    """
    检查是否是有效的 Markdown 文件

    Args:
        filepath: 文件路径

    Returns:
        bool: 是否有效
    """
    if not os.path.exists(filepath):
        return False

    ext = os.path.splitext(filepath)[1].lower()
    return ext in ['.md', '.markdown']
