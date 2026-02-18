#!/usr/bin/env python3
"""
PPT 生成器主入口

将 Markdown 文件转换为酷炫的霓虹风格 HTML 演示文稿

用法:
    python3 md_to_ppt.py input.md output.html
    python3 md_to_ppt.py input.md output.html --theme neon
    python3 md_to_ppt.py --help
"""

import argparse
import sys
import os

# 添加 scripts 目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from parser.slide_parser import SlideParser
from templates import get_template
from themes import get_theme
from utils.helpers import read_file, write_file, get_file_basename, is_valid_md_file


def parse_arguments():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(
        description='将 Markdown 文件转换为酷炫的霓虹风格 HTML 演示文稿',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
示例:
  %(prog)s input.md output.html          # 基本转换
  %(prog)s slides.md slides.html         # 指定输入输出
  %(prog)s input.md output.html --theme neon  # 指定主题

支持的幻灯片类型:
  cover       封面页
  toc         目录页
  chapter     章节页
  content     标准内容页
  two-column  双栏页
  code        代码页
  data        数据表格页
  timeline    时间轴页
  grid        网格卡片页 (2x2 或 3x3)
  quote       金句页
  end         结束页

详细文档:
  references/md-format.md      Markdown 格式规范
  references/content-rules.md  内容转换规则
        '''
    )

    parser.add_argument(
        'input',
        help='输入的 Markdown 文件路径'
    )

    parser.add_argument(
        'output',
        help='输出的 HTML 文件路径'
    )

    parser.add_argument(
        '-t', '--theme',
        default='neon',
        choices=['neon'],
        help='选择主题 (默认: neon)'
    )

    parser.add_argument(
        '--auto-infer',
        action='store_true',
        help='自动推断未标记类型的幻灯片'
    )

    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='显示详细输出'
    )

    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 1.0.0'
    )

    return parser.parse_args()


def convert_md_to_html(input_path: str, output_path: str, theme_name: str = 'neon',
                       auto_infer: bool = False, verbose: bool = False) -> bool:
    """
    将 Markdown 文件转换为 HTML 演示文稿

    Args:
        input_path: 输入的 Markdown 文件路径
        output_path: 输出的 HTML 文件路径
        theme_name: 主题名称
        auto_infer: 是否自动推断类型
        verbose: 是否显示详细输出

    Returns:
        bool: 转换是否成功
    """
    try:
        # 验证输入文件
        if not is_valid_md_file(input_path):
            print(f"错误: '{input_path}' 不是有效的 Markdown 文件")
            return False

        if verbose:
            print(f"读取文件: {input_path}")

        # 读取 Markdown 内容
        md_content = read_file(input_path)

        # 解析幻灯片
        if verbose:
            print("解析幻灯片...")

        parser = SlideParser()
        slides = parser.parse(md_content, auto_infer=auto_infer)

        if not slides:
            print("警告: 未找到任何幻灯片内容")
            return False

        if verbose:
            print(f"找到 {len(slides)} 张幻灯片")

        # 获取主题
        theme = get_theme(theme_name)

        # 渲染幻灯片
        if verbose:
            print("渲染幻灯片...")

        slides_html = []
        for i, slide in enumerate(slides):
            template = get_template(slide.slide_type)
            slide_html = template.render(
                {'content': slide.content, 'meta': slide.meta},
                theme
            )
            slides_html.append(slide_html)

            if verbose:
                print(f"  [{i+1}/{len(slides)}] 类型: {slide.slide_type}")

        # 生成完整 HTML
        all_slides_html = '\n'.join(slides_html)
        title = get_file_basename(input_path)
        final_html = theme.render_html(all_slides_html, title)

        # 写入输出文件
        if verbose:
            print(f"写入文件: {output_path}")

        write_file(output_path, final_html)

        print(f"✓ 成功生成: {output_path}")
        print(f"  幻灯片数量: {len(slides)}")
        print(f"  主题: {theme_name}")

        return True

    except FileNotFoundError as e:
        print(f"错误: 文件不存在 - {e}")
        return False
    except PermissionError as e:
        print(f"错误: 权限不足 - {e}")
        return False
    except Exception as e:
        print(f"错误: {e}")
        if verbose:
            import traceback
            traceback.print_exc()
        return False


def main():
    """主函数"""
    args = parse_arguments()

    success = convert_md_to_html(
        input_path=args.input,
        output_path=args.output,
        theme_name=args.theme,
        auto_infer=args.auto_infer,
        verbose=args.verbose
    )

    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
