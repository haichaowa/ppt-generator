"""
霓虹主题 - 酷炫简洁的霓虹风格
"""
from .base import BaseTheme, ThemeColors
from typing import Dict, Any


class NeonTheme(BaseTheme):
    """霓虹主题"""

    def __init__(self):
        super().__init__()

        self.name = 'neon'

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
        animation: float 20s infinite ease-in-out;
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
        transform: translate(-50%, -50%);
        animation-delay: -10s;
    }}

    @keyframes float {{
        0%, 100% {{ transform: translate(0, 0) scale(1); }}
        25% {{ transform: translate(50px, -50px) scale(1.1); }}
        50% {{ transform: translate(-30px, 30px) scale(0.9); }}
        75% {{ transform: translate(-50px, -30px) scale(1.05); }}
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
        transition: all 0.6s cubic-bezier(0.4, 0, 0.2, 1);
        pointer-events: none;
    }}

    .slide.active {{
        opacity: 1;
        transform: translateX(0);
        pointer-events: auto;
    }}

    .slide.prev {{
        transform: translateX(-100%);
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
        font-size: 4rem;
        font-weight: 700;
        margin-bottom: 10px;
    }}

    .cover-subtitle {{
        font-size: 2rem;
        color: var(--secondary-color);
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
        font-size: 2.5rem;
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
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--primary-color);
        min-width: 50px;
    }}

    .toc-text {{
        font-size: 1.3rem;
        flex: 1;
        text-align: left;
    }}

    /* Chapter Page */
    .chapter-container {{
        text-align: center;
    }}

    .chapter-number {{
        font-size: 10rem;
        font-weight: 900;
        line-height: 1;
        margin-bottom: 20px;
    }}

    .chapter-title {{
        font-size: 3rem;
        font-weight: 400;
    }}

    /* Content Page */
    .content-container {{
        max-width: 900px;
        margin: 0 auto;
    }}

    .content-title {{
        font-size: 2.5rem;
        margin-bottom: 30px;
        text-align: center;
    }}

    .content-description {{
        font-size: 1.2rem;
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
        font-size: 1.3rem;
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
        font-size: 2rem;
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
        font-size: 1.5rem;
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
        font-size: 1rem;
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
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 10px;
    }}

    .card-desc {{
        font-size: 0.9rem;
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
        font-size: 1.8rem;
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
        font-size: 4rem;
        font-weight: 700;
    }}

    .end-subtitle {{
        font-size: 2rem;
        font-weight: 400;
    }}

    .end-meta {{
        margin-top: 30px;
        font-size: 1rem;
        color: rgba(255, 255, 255, 0.7);
    }}

    /* Progress Bar */
    .progress-bar {{
        position: fixed;
        top: 0;
        left: 0;
        height: 3px;
        background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
        z-index: 1000;
        transition: width 0.3s ease;
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
        transition: all 0.3s ease;
        color: var(--text-color);
    }}

    .nav-hint:hover {{
        background: rgba(0, 245, 255, 0.2);
        border-color: var(--primary-color);
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

        // Initialize
        showSlide(0);
    </script>
</body>
</html>'''
