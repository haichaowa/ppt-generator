"""
霓虹主题 - 酷炫简洁的霓虹风格
"""
from .base import BaseTheme, ThemeColors
from typing import Dict, Any
import random

# 霓虹颜色池
NEON_COLORS = [
    ('#00f5ff', '#00d4e6'),  # 青色系
    ('#bf00ff', '#9900cc'),  # 紫色系
    ('#ff006e', '#cc0058'),  # 粉色系
    ('#00ff88', '#00cc6e'),  # 绿色系
    ('#ff9500', '#cc7700'),  # 橙色系
]


class NeonTheme(BaseTheme):
    """霓虹主题"""

    def __init__(self):
        super().__init__()

        self.name = 'neon'

        # 随机选择封面霓虹颜色
        colors = random.choice(NEON_COLORS)
        self.neon_primary = colors[0]
        self.neon_secondary = colors[1]

        # 颜色配置
        self.colors = ThemeColors(
            primary='#00f5ff',      # 青色霓虹
            secondary='#bf00ff',    # 紫色霓虹
            background='#0a0a1a',   # 深色背景
            text='#ffffff',         # 白色文字
            accent='#ff006e',       # 粉色强调
        )

        # CSS 变量
        self.css_vars = {
            'code_bg': 'rgba(0, 245, 255, 0.05)',
            'table_bg': 'rgba(0, 245, 255, 0.05)',
            'glass_bg': 'rgba(255, 255, 255, 0.05)',
            'glass_border': 'rgba(255, 255, 255, 0.1)',
        }

        # 字体
        self.fonts = {
            'primary': '"PingFang SC", "Microsoft YaHei", sans-serif',
            'code': '"Fira Code", "Monaco", "Consolas", monospace',
        }

    def get_css(self) -> str:
        """获取霓虹主题 CSS"""
        return f'''
    /* CSS Variables */
    :root {{
        --primary-color: {self.colors.primary};
        --secondary-color: {self.colors.secondary};
        --background-color: {self.colors.background};
        --text-color: {self.colors.text};
        --accent-color: {self.colors.accent};
        --code-bg: {self.css_vars['code_bg']};
        --table-bg: {self.css_vars['table_bg']};
        --glass-bg: {self.css_vars['glass_bg']};
        --glass-border: {self.css_vars['glass_border']};
    }}

    /* Reset & Base */
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }}

    body {{
        font-family: {self.fonts['primary']};
        background: var(--background-color);
        color: var(--text-color);
        overflow: hidden;
        min-height: 100vh;
    }}

    /* Animated Background */
    .background {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        overflow: hidden;
    }}

    .orb {{
        position: absolute;
        border-radius: 50%;
        filter: blur(80px);
        opacity: 0.5;
        animation: glitch-float 20s infinite ease-in-out;
    }}

    .orb-1 {{
        width: 600px;
        height: 600px;
        background: var(--primary-color);
        top: -200px;
        left: -200px;
        animation-delay: 0s;
    }}

    .orb-2 {{
        width: 500px;
        height: 500px;
        background: var(--secondary-color);
        bottom: -150px;
        right: -150px;
        animation-delay: -5s;
    }}

    .orb-3 {{
        width: 400px;
        height: 400px;
        background: var(--accent-color);
        top: 50%;
        left: 50%;
        animation-delay: -10s;
    }}

    @keyframes float {{
        0%, 100% {{ transform: translate(0, 0) scale(1); }}
        25% {{ transform: translate(50px, -50px) scale(1.1); }}
        50% {{ transform: translate(-30px, 30px) scale(0.9); }}
        75% {{ transform: translate(-50px, -30px) scale(1.05); }}
    }}

    /* ====== CYBERPUNK GLITCH EFFECTS ====== */

    /* Scanlines Overlay */
    .scanlines {{
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: repeating-linear-gradient(
            0deg,
            transparent,
            transparent 2px,
            rgba(0, 0, 0, 0.1) 2px,
            rgba(0, 0, 0, 0.1) 4px
        );
        pointer-events: none;
        z-index: 9999;
        animation: scanline-flicker 0.1s infinite;
    }}

    @keyframes scanline-flicker {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0.98; }}
    }}

    /* Glitch Overlay */
    .glitch-overlay {{
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: transparent;
        pointer-events: none;
        z-index: 9998;
        animation: glitch-overlay 5s infinite;
    }}

    @keyframes glitch-overlay {{
        0%, 90%, 100% {{ opacity: 0; transform: translateX(0); }}
        92% {{ opacity: 0.5; transform: translateX(-10px); background: rgba(255, 0, 255, 0.03); }}
        94% {{ opacity: 0.3; transform: translateX(10px); background: rgba(0, 255, 255, 0.03); }}
        96% {{ opacity: 0; transform: translateX(0); }}
    }}

    /* RGB Split Orbs */
    .orb-glitch {{
        animation: glitch-float 15s infinite;
        filter: blur(80px) drop-shadow(0 0 30px currentColor);
    }}

    @keyframes glitch-float {{
        0%, 100% {{ transform: translate(0, 0) scale(1); }}
        5% {{ transform: translate(-5px, 0) scale(1.02); }}
        10% {{ transform: translate(5px, 0) scale(0.98); }}
        15% {{ transform: translate(0, -5px) scale(1.01); }}
        20% {{ transform: translate(-3px, 3px) scale(0.99); }}
        25% {{ transform: translate(3px, -3px) scale(1); }}
        30% {{ transform: translate(0, 5px) scale(1.02); }}
        35% {{ transform: translate(-5px, -5px) scale(0.98); }}
        40% {{ transform: translate(5px, 5px) scale(1); }}
        50% {{ transform: translate(0, 0) scale(1); }}
        60% {{ transform: translate(-2px, 2px) scale(1.01); }}
        70% {{ transform: translate(2px, -2px) scale(0.99); }}
        80% {{ transform: translate(-3px, 0) scale(1); }}
        90% {{ transform: translate(3px, 0) scale(1); }}
    }}

    /* ====== TEXT EFFECTS ====== */

    /* Neon Flicker */
    .neon-flicker {{
        animation: neon-flicker-anim 3s infinite;
    }}

    @keyframes neon-flicker-anim {{
        0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% {{
            text-shadow:
                0 0 10px var(--neon-color, var(--primary-color)),
                0 0 20px var(--neon-color, var(--primary-color)),
                0 0 40px var(--neon-color, var(--primary-color)),
                0 0 80px var(--neon-color, var(--primary-color));
            opacity: 1;
        }}
        20%, 24%, 55% {{
            text-shadow: none;
            opacity: 0.8;
        }}
    }}

    /* Rainbow Flow Text */
    .rainbow-text {{
        background: linear-gradient(
            90deg,
            #ff0000, #ff7f00, #ffff00, #00ff00,
            #0000ff, #4b0082, #8f00ff, #ff0000
        );
        background-size: 400% 100%;
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: rainbow-flow 8s linear infinite;
    }}

    @keyframes rainbow-flow {{
        0% {{ background-position: 0% 50%; }}
        100% {{ background-position: 400% 50%; }}
    }}

    /* Glitch Text */
    .glitch-text {{
        position: relative;
        animation: glitch-skew 1s infinite linear alternate-reverse;
    }}

    .glitch-text::before,
    .glitch-text::after {{
        content: attr(data-text);
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
    }}

    .glitch-text::before {{
        left: 2px;
        text-shadow: -2px 0 #ff00ff;
        clip-path: polygon(0 0, 100% 0, 100% 35%, 0 35%);
        animation: glitch-top 1s infinite linear alternate-reverse;
    }}

    .glitch-text::after {{
        left: -2px;
        text-shadow: -2px 0 #00ffff;
        clip-path: polygon(0 65%, 100% 65%, 100% 100%, 0 100%);
        animation: glitch-bottom 1.5s infinite linear alternate-reverse;
    }}

    @keyframes glitch-skew {{
        0% {{ transform: skewX(0deg); }}
        10% {{ transform: skewX(-1deg); }}
        20% {{ transform: skewX(1deg); }}
        30% {{ transform: skewX(0deg); }}
        100% {{ transform: skewX(0deg); }}
    }}

    @keyframes glitch-top {{
        0%, 100% {{ transform: translateX(0); }}
        20% {{ transform: translateX(-3px); }}
        40% {{ transform: translateX(3px); }}
        60% {{ transform: translateX(-1px); }}
        80% {{ transform: translateX(1px); }}
    }}

    @keyframes glitch-bottom {{
        0%, 100% {{ transform: translateX(0); }}
        20% {{ transform: translateX(3px); }}
        40% {{ transform: translateX(-3px); }}
        60% {{ transform: translateX(1px); }}
        80% {{ transform: translateX(-1px); }}
    }}

    /* Typewriter Effect */
    .typewriter {{
        overflow: hidden;
        border-right: 3px solid var(--primary-color);
        white-space: nowrap;
        animation:
            typing 3.5s steps(40, end),
            blink-caret 0.75s step-end infinite;
    }}

    @keyframes typing {{
        from {{ width: 0; }}
        to {{ width: 100%; }}
    }}

    @keyframes blink-caret {{
        from, to {{ border-color: transparent; }}
        50% {{ border-color: var(--primary-color); }}
    }}

    /* Slide Container */
    .slides-container {{
        width: 100vw;
        height: 100vh;
        overflow: hidden;
        position: relative;
    }}

    .slide {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        opacity: 0;
        transform: translateX(100%);
        transition: none;
        pointer-events: none;
    }}

    .slide.active {{
        opacity: 1;
        transform: translateX(0);
        pointer-events: auto;
        animation: glitch-enter 0.6s forwards;
    }}

    .slide.prev {{
        transform: translateX(-100%);
        animation: glitch-exit 0.4s forwards;
    }}

    /* Glitch Slide Transitions */
    @keyframes glitch-enter {{
        0% {{
            opacity: 0;
            transform: translateX(100%) skewX(0deg);
            filter: hue-rotate(90deg);
        }}
        20% {{
            opacity: 1;
            transform: translateX(-10%) skewX(-5deg);
            filter: hue-rotate(0deg) brightness(2);
        }}
        40% {{
            transform: translateX(5%) skewX(3deg);
            filter: hue-rotate(180deg);
        }}
        60% {{
            transform: translateX(-3%) skewX(-2deg);
            filter: hue-rotate(90deg);
        }}
        80% {{
            transform: translateX(2%) skewX(1deg);
        }}
        100% {{
            opacity: 1;
            transform: translateX(0) skewX(0deg);
            filter: none;
        }}
    }}

    @keyframes glitch-exit {{
        0% {{
            opacity: 1;
            transform: translateX(0) skewX(0deg);
        }}
        20% {{
            opacity: 0.8;
            transform: translateX(5%) skewX(3deg);
            filter: brightness(2) hue-rotate(90deg);
        }}
        40% {{
            transform: translateX(-5%) skewX(-5deg);
            filter: hue-rotate(180deg);
        }}
        100% {{
            opacity: 0;
            transform: translateX(-100%) skewX(0deg);
            filter: none;
        }}
    }}

    .slide-content {{
        width: 90%;
        max-width: 1200px;
        padding: 40px;
    }}

    /* Neon Text Effect */
    .neon-text {{
        color: var(--neon-color, var(--primary-color));
        text-shadow:
            0 0 10px var(--neon-color, var(--primary-color)),
            0 0 20px var(--neon-color, var(--primary-color)),
            0 0 40px var(--neon-color, var(--primary-color)),
            0 0 80px var(--neon-color, var(--primary-color));
        animation: pulse 2s infinite;
    }}

    @keyframes pulse {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0.8; }}
    }}

    /* Metal Neon Text - 金属荧光文字 - 带随机颜色和老旧霓虹灯闪烁 */
    .metal-neon-text {{
        --neon-glow-color: #00f5ff; /* 将被动态替换 */
        background: linear-gradient(
            135deg,
            #b8b8b8 0%,
            #ffffff 20%,
            #e0e0e0 40%,
            #ffffff 60%,
            #c8c8c8 80%,
            #ffffff 100%
        );
        background-size: 300% 300%;
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        animation:
            metal-shine 4s ease-in-out infinite,
            neon-old-flicker 8s linear infinite;
    }}

    @keyframes metal-shine {{
        0%, 100% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
    }}

    /* 老旧霓虹灯闪烁 - 不规律、随机感 */
    /* 模拟真实霓虹灯的不稳定供电效果 */
    @keyframes neon-old-flicker {{
        /* 大部分时间正常发光 */
        0%, 8%, 12%, 18%, 22%, 25%, 53%, 57%, 100% {{
            filter: drop-shadow(0 0 10px var(--neon-glow-color))
                    drop-shadow(0 0 20px var(--neon-glow-color))
                    drop-shadow(0 0 40px var(--neon-glow-color));
            opacity: 1;
        }}
        /* 快速连续闪烁 */
        9%, 11% {{
            filter: drop-shadow(0 0 3px var(--neon-glow-color));
            opacity: 0.7;
        }}
        19%, 21% {{
            filter: drop-shadow(0 0 5px var(--neon-glow-color));
            opacity: 0.85;
        }}
        /* 随机的短暂变暗 */
        54%, 56% {{
            filter: drop-shadow(0 0 4px var(--neon-glow-color));
            opacity: 0.75;
        }}
    }}

    /* ====== INTERACTIVE EFFECTS ====== */

    /* Hover Glow */
    .interactive-element,
    .toc-item,
    .grid-card,
    .nav-hint {{
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}

    .interactive-element:hover,
    .toc-item:hover,
    .grid-card:hover {{
        box-shadow:
            0 0 20px var(--primary-color),
            0 0 40px var(--primary-color),
            inset 0 0 20px rgba(0, 245, 255, 0.1);
        transform: scale(1.02);
    }}

    /* Click Ripple */
    .ripple {{
        position: absolute;
        border-radius: 50%;
        background: radial-gradient(circle, var(--primary-color) 0%, transparent 70%);
        transform: scale(0);
        pointer-events: none;
        animation: ripple-anim 0.6s ease-out forwards;
    }}

    @keyframes ripple-anim {{
        from {{ transform: scale(0); opacity: 1; }}
        to {{ transform: scale(4); opacity: 0; }}
    }}

    /* Progress Bar Glow Animation */
    .progress-bar {{
        position: fixed;
        top: 0;
        left: 0;
        height: 3px;
        background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
        z-index: 1000;
        transition: width 0.3s ease;
        animation: progress-glow 2s ease-in-out infinite;
        box-shadow: 0 0 10px var(--primary-color), 0 0 20px var(--secondary-color);
    }}

    @keyframes progress-glow {{
        0%, 100% {{
            box-shadow: 0 0 10px var(--primary-color), 0 0 20px var(--secondary-color);
        }}
        50% {{
            box-shadow: 0 0 20px var(--primary-color), 0 0 40px var(--secondary-color), 0 0 60px var(--accent-color);
        }}
    }}

    /* Slide Counter Pulse */
    .slide-counter {{
        animation: counter-pulse 2s ease-in-out infinite;
    }}

    @keyframes counter-pulse {{
        0%, 100% {{
            text-shadow: 0 0 5px var(--primary-color);
        }}
        50% {{
            text-shadow: 0 0 15px var(--primary-color), 0 0 25px var(--secondary-color);
        }}
    }}

    /* Nav Hints Hover */
    .nav-hint {{
        position: relative;
        overflow: hidden;
    }}

    .nav-hint:hover {{
        transform: scale(1.2);
        box-shadow: 0 0 20px var(--primary-color);
        border-color: var(--primary-color);
    }}

    /* Mouse Trail Canvas */
    #mouseTrail {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 9998;
    }}

    /* Glass Card */
    .glass-card {{
        background: var(--glass-bg);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid var(--glass-border);
        border-radius: 20px;
        padding: 30px;
    }}

    /* Cover Page */
    .cover .slide-content {{
        text-align: center;
    }}

    .cover-container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 20px;
    }}

    .cover-title {{
        font-size: 4.5rem;
        font-weight: 700;
        margin-bottom: 10px;
        letter-spacing: 0.05em;
    }}

    .cover-subtitle {{
        font-size: 2.2rem;
        color: #ffffff;
        font-weight: 400;
    }}

    .cover-meta {{
        margin-top: 30px;
        font-size: 1rem;
        color: rgba(255, 255, 255, 0.7);
    }}

    .meta-separator {{
        margin: 0 15px;
    }}

    /* TOC Page */
    .toc-container {{
        text-align: center;
    }}

    .toc-title {{
        font-size: 2.8rem;
        margin-bottom: 40px;
    }}

    .toc-items {{
        display: flex;
        flex-direction: column;
        gap: 20px;
        max-width: 600px;
        margin: 0 auto;
    }}

    .toc-item {{
        display: flex;
        align-items: center;
        gap: 20px;
        padding: 15px 30px;
        background: var(--glass-bg);
        border-radius: 10px;
        border: 1px solid var(--glass-border);
        transition: all 0.3s ease;
    }}

    .toc-item:hover {{
        background: rgba(0, 245, 255, 0.1);
        border-color: var(--primary-color);
    }}

    .toc-number {{
        font-size: 1.7rem;
        font-weight: 700;
        color: var(--primary-color);
        min-width: 50px;
    }}

    .toc-text {{
        font-size: 1.5rem;
        flex: 1;
        text-align: left;
    }}

    /* Chapter Page */
    .chapter-container {{
        text-align: center;
    }}

    .chapter-number {{
        font-size: 11rem;
        font-weight: 900;
        line-height: 1;
        margin-bottom: 20px;
    }}

    .chapter-title {{
        font-size: 3.5rem;
        font-weight: 600;
        letter-spacing: 0.1em;
    }}

    /* Content Page */
    .content-container {{
        max-width: 900px;
        margin: 0 auto;
    }}

    .content-title {{
        font-size: 2.8rem;
        margin-bottom: 30px;
        text-align: center;
    }}

    .content-description {{
        font-size: 1.4rem;
        line-height: 1.8;
        margin-bottom: 30px;
        text-align: center;
        color: rgba(255, 255, 255, 0.9);
    }}

    .content-list {{
        list-style: none;
        padding: 0;
    }}

    .content-item {{
        font-size: 1.5rem;
        padding: 15px 0;
        padding-left: 30px;
        position: relative;
        border-bottom: 1px solid var(--glass-border);
    }}

    .content-item:last-child {{
        border-bottom: none;
    }}

    .content-item::before {{
        content: '▹';
        position: absolute;
        left: 0;
        color: var(--primary-color);
    }}

    /* Two Column Page */
    .two-column-container {{
        width: 100%;
    }}

    .two-column-title {{
        font-size: 2.3rem;
        margin-bottom: 30px;
        text-align: center;
    }}

    .columns-wrapper {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 30px;
    }}

    .column {{
        padding: 30px;
    }}

    .column-title {{
        font-size: 1.7rem;
        margin-bottom: 15px;
    }}

    .column-description {{
        font-size: 1rem;
        margin-bottom: 20px;
        color: rgba(255, 255, 255, 0.8);
    }}

    .column-list {{
        list-style: none;
        padding: 0;
    }}

    .column-item {{
        font-size: 1.2rem;
        padding: 10px 0;
        padding-left: 20px;
        position: relative;
    }}

    .column-item::before {{
        content: '•';
        position: absolute;
        left: 0;
        color: var(--primary-color);
    }}

    /* Code Page */
    .code-container {{
        max-width: 1000px;
        margin: 0 auto;
    }}

    .code-title {{
        font-size: 2rem;
        margin-bottom: 20px;
        text-align: center;
    }}

    .code-block {{
        background: rgba(0, 0, 0, 0.5);
        border-radius: 15px;
        overflow: hidden;
        margin-bottom: 20px;
    }}

    .code-header {{
        background: rgba(255, 255, 255, 0.05);
        padding: 10px 20px;
        border-bottom: 1px solid var(--glass-border);
    }}

    .code-language {{
        font-size: 0.9rem;
        color: var(--primary-color);
        font-weight: 500;
    }}

    .code-content {{
        padding: 20px;
        overflow-x: auto;
    }}

    .code-content code {{
        font-family: {self.fonts['code']};
        font-size: 0.95rem;
        line-height: 1.6;
        color: #e0e0e0;
    }}

    .code-content .keyword {{
        color: var(--secondary-color);
    }}

    .code-content .string {{
        color: #00ff88;
    }}

    .code-content .comment {{
        color: #888;
        font-style: italic;
    }}

    .code-description {{
        font-size: 1rem;
        text-align: center;
        color: rgba(255, 255, 255, 0.8);
    }}

    /* Data Page */
    .data-container {{
        max-width: 900px;
        margin: 0 auto;
    }}

    .data-title {{
        font-size: 2rem;
        margin-bottom: 30px;
        text-align: center;
    }}

    .data-table-wrapper {{
        overflow-x: auto;
        padding: 20px;
    }}

    .data-table {{
        width: 100%;
        border-collapse: collapse;
    }}

    .data-header-row {{
        border-bottom: 2px solid var(--primary-color);
    }}

    .data-header {{
        padding: 15px 20px;
        text-align: left;
        font-size: 1.1rem;
        font-weight: 600;
        color: var(--primary-color);
    }}

    .data-row {{
        border-bottom: 1px solid var(--glass-border);
        transition: all 0.3s ease;
    }}

    .data-row:hover {{
        background: rgba(0, 245, 255, 0.05);
    }}

    .data-cell {{
        padding: 15px 20px;
        font-size: 1rem;
    }}

    /* Timeline Page */
    .timeline-container {{
        max-width: 800px;
        margin: 0 auto;
    }}

    .timeline-title {{
        font-size: 2rem;
        margin-bottom: 40px;
        text-align: center;
    }}

    .timeline-items {{
        position: relative;
        padding-left: 40px;
    }}

    .timeline-items::before {{
        content: '';
        position: absolute;
        left: 15px;
        top: 0;
        bottom: 0;
        width: 2px;
        background: linear-gradient(to bottom, var(--primary-color), var(--secondary-color));
    }}

    .timeline-item {{
        position: relative;
        margin-bottom: 30px;
    }}

    .timeline-dot {{
        position: absolute;
        left: -40px;
        top: 20px;
        width: 12px;
        height: 12px;
        border-radius: 50%;
    }}

    .timeline-content {{
        padding: 20px;
    }}

    .timeline-date {{
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 5px;
    }}

    .timeline-item-title {{
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 10px;
    }}

    .timeline-desc {{
        font-size: 1rem;
        color: rgba(255, 255, 255, 0.8);
    }}

    /* Grid Page */
    .grid-container {{
        width: 100%;
        text-align: center;
    }}

    .grid-title {{
        font-size: 2rem;
        margin-bottom: 40px;
    }}

    .grid-cards {{
        display: grid;
        gap: 25px;
        max-width: 1000px;
        margin: 0 auto;
    }}

    .grid-2x2 {{
        grid-template-columns: repeat(2, 1fr);
    }}

    .grid-3x3 {{
        grid-template-columns: repeat(3, 1fr);
    }}

    .grid-card {{
        padding: 30px 20px;
        text-align: center;
        transition: all 0.3s ease;
        border: 1px solid var(--card-color, var(--primary-color));
    }}

    .grid-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }}

    .card-icon {{
        font-size: 3rem;
        margin-bottom: 15px;
    }}

    .card-title {{
        font-size: 1.4rem;
        font-weight: 600;
        margin-bottom: 10px;
    }}

    .card-desc {{
        font-size: 1rem;
        color: rgba(255, 255, 255, 0.7);
    }}

    /* Quote Page */
    .quote-container {{
        max-width: 800px;
        margin: 0 auto;
        text-align: center;
    }}

    .quote-title {{
        font-size: 1.5rem;
        margin-bottom: 30px;
        color: rgba(255, 255, 255, 0.7);
    }}

    .quote-text {{
        padding: 40px;
        border-left: 4px solid var(--primary-color);
        margin-bottom: 30px;
        text-align: left;
    }}

    .quote-content {{
        font-size: 2rem;
        line-height: 1.6;
        font-style: italic;
    }}

    .quote-author {{
        font-size: 1.2rem;
        font-style: italic;
    }}

    /* End Page */
    .end .slide-content {{
        text-align: center;
    }}

    .end-container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 20px;
    }}

    .end-title {{
        font-size: 4.5rem;
        font-weight: 700;
    }}

    .end-subtitle {{
        font-size: 2.2rem;
        font-weight: 400;
    }}

    .end-meta {{
        margin-top: 30px;
        font-size: 1rem;
        color: rgba(255, 255, 255, 0.7);
    }}

    /* Image Page */
    .image-container {{
        max-width: 1000px;
        margin: 0 auto;
        text-align: center;
    }}

    .image-title {{
        font-size: 2rem;
        margin-bottom: 30px;
    }}

    .image-wrapper {{
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 20px;
    }}

    .slide-image {{
        max-width: 100%;
        max-height: 60vh;
        border-radius: 10px;
        box-shadow: 0 0 20px rgba(0, 245, 255, 0.3);
    }}

    .image-caption {{
        font-size: 1rem;
        color: rgba(255, 255, 255, 0.7);
        font-style: italic;
    }}

    .image-placeholder {{
        padding: 60px;
        color: rgba(255, 255, 255, 0.5);
        font-size: 1.2rem;
    }}

    /* Navigation Hints */
    .nav-hints {{
        position: fixed;
        bottom: 20px;
        right: 20px;
        display: flex;
        gap: 10px;
        z-index: 100;
    }}

    .nav-hint {{
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: var(--glass-bg);
        border: 1px solid var(--glass-border);
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        color: var(--text-color);
    }}

    /* Slide Counter */
    .slide-counter {{
        position: fixed;
        bottom: 20px;
        left: 20px;
        font-size: 0.9rem;
        color: rgba(255, 255, 255, 0.6);
        z-index: 100;
    }}

    /* Responsive */
    @media (max-width: 768px) {{
        .cover-title,
        .end-title {{
            font-size: 2.5rem;
        }}

        .cover-subtitle,
        .end-subtitle {{
            font-size: 1.5rem;
        }}

        .chapter-number {{
            font-size: 6rem;
        }}

        .chapter-title {{
            font-size: 2rem;
        }}

        .columns-wrapper {{
            grid-template-columns: 1fr;
        }}

        .grid-3x3 {{
            grid-template-columns: repeat(2, 1fr);
        }}

        .quote-content {{
            font-size: 1.4rem;
        }}
    }}

    @media (max-width: 480px) {{
        .grid-2x2,
        .grid-3x3 {{
            grid-template-columns: 1fr;
        }}
    }}
'''

    def get_html_template(self) -> str:
        """获取 HTML 模板"""
        return '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
{css}
    </style>
</head>
<body>
    <!-- Glitch Overlay -->
    <div class="glitch-overlay"></div>

    <!-- Scanlines -->
    <div class="scanlines"></div>

    <!-- Mouse Trail Canvas -->
    <canvas id="mouseTrail"></canvas>

    <!-- Animated Background -->
    <div class="background">
        <div class="orb orb-1"></div>
        <div class="orb orb-2"></div>
        <div class="orb orb-3"></div>
    </div>

    <!-- Progress Bar -->
    <div class="progress-bar" id="progressBar"></div>

    <!-- Slides Container -->
    <div class="slides-container" id="slidesContainer">
{slides}
    </div>

    <!-- Navigation Hints -->
    <div class="nav-hints">
        <div class="nav-hint" onclick="prevSlide()">←</div>
        <div class="nav-hint" onclick="nextSlide()">→</div>
    </div>

    <!-- Slide Counter -->
    <div class="slide-counter" id="slideCounter">1 / 1</div>

    <script>
        // Slide Navigation
        let currentSlide = 0;
        const slides = document.querySelectorAll('.slide');
        const totalSlides = slides.length;

        function showSlide(index) {{
            if (index < 0) index = 0;
            if (index >= totalSlides) index = totalSlides - 1;

            slides.forEach((slide, i) => {{
                slide.classList.remove('active', 'prev');
                if (i < index) {{
                    slide.classList.add('prev');
                }} else if (i === index) {{
                    slide.classList.add('active');
                }}
            }});

            currentSlide = index;
            updateProgress();
            updateCounter();
        }}

        function nextSlide() {{
            if (currentSlide < totalSlides - 1) {{
                showSlide(currentSlide + 1);
            }}
        }}

        function prevSlide() {{
            if (currentSlide > 0) {{
                showSlide(currentSlide - 1);
            }}
        }}

        function updateProgress() {{
            const progress = ((currentSlide + 1) / totalSlides) * 100;
            document.getElementById('progressBar').style.width = progress + '%';
        }}

        function updateCounter() {{
            document.getElementById('slideCounter').textContent =
                `${{currentSlide + 1}} / ${{totalSlides}}`;
        }}

        // Keyboard Navigation
        document.addEventListener('keydown', (e) => {{
            if (e.key === 'ArrowRight' || e.key === ' ') {{
                e.preventDefault();
                nextSlide();
            }} else if (e.key === 'ArrowLeft') {{
                e.preventDefault();
                prevSlide();
            }} else if (e.key === 'Home') {{
                showSlide(0);
            }} else if (e.key === 'End') {{
                showSlide(totalSlides - 1);
            }}
        }});

        // Touch Navigation
        let touchStartX = 0;
        let touchEndX = 0;

        document.addEventListener('touchstart', (e) => {{
            touchStartX = e.changedTouches[0].screenX;
        }});

        document.addEventListener('touchend', (e) => {{
            touchEndX = e.changedTouches[0].screenX;
            handleSwipe();
        }});

        function handleSwipe() {{
            const swipeThreshold = 50;
            const diff = touchStartX - touchEndX;

            if (Math.abs(diff) > swipeThreshold) {{
                if (diff > 0) {{
                    nextSlide();
                }} else {{
                    prevSlide();
                }}
            }}
        }}

        // ====== CYBERPUNK EFFECTS ======

        // Mouse Trail Effect
        (function initMouseTrail() {{
            const canvas = document.getElementById('mouseTrail');
            const ctx = canvas.getContext('2d');
            let particles = [];

            function resizeCanvas() {{
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
            }}
            resizeCanvas();
            window.addEventListener('resize', resizeCanvas);

            document.addEventListener('mousemove', (e) => {{
                // Add multiple particles for a more vibrant trail
                for (let i = 0; i < 2; i++) {{
                    particles.push({{
                        x: e.clientX + (Math.random() - 0.5) * 10,
                        y: e.clientY + (Math.random() - 0.5) * 10,
                        life: 1,
                        color: `hsl(${{Math.random() * 360}}, 100%, 50%)`,
                        size: Math.random() * 3 + 2
                    }});
                }}
                // Limit particles to prevent performance issues
                if (particles.length > 100) {{
                    particles = particles.slice(-100);
                }}
            }});

            function animateTrail() {{
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                particles = particles.filter(p => p.life > 0);
                particles.forEach(p => {{
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, p.size * p.life, 0, Math.PI * 2);
                    ctx.fillStyle = p.color;
                    ctx.globalAlpha = p.life;
                    ctx.fill();
                    p.life -= 0.02;
                }});
                ctx.globalAlpha = 1;
                requestAnimationFrame(animateTrail);
            }}
            animateTrail();
        }})();

        // Parallax Effect for Orbs
        document.addEventListener('mousemove', (e) => {{
            const x = (e.clientX / window.innerWidth - 0.5) * 20;
            const y = (e.clientY / window.innerHeight - 0.5) * 20;

            document.querySelectorAll('.orb').forEach((orb, i) => {{
                const depth = (i + 1) * 0.5;
                const baseTransform = orb.classList.contains('orb-3')
                    ? 'translate(-50%, -50%)'
                    : '';
                orb.style.transform = `${{baseTransform}} translate(${{x * depth}}px, ${{y * depth}}px)`;
            }});
        }});

        // Click Ripple Effect
        document.addEventListener('click', (e) => {{
            const ripple = document.createElement('div');
            ripple.className = 'ripple';
            ripple.style.left = e.clientX + 'px';
            ripple.style.top = e.clientY + 'px';
            ripple.style.width = '20px';
            ripple.style.height = '20px';
            ripple.style.marginLeft = '-10px';
            ripple.style.marginTop = '-10px';
            document.body.appendChild(ripple);

            ripple.addEventListener('animationend', () => {{
                ripple.remove();
            }});
        }});

        // Initialize
        showSlide(0);
    </script>
</body>
</html>'''
