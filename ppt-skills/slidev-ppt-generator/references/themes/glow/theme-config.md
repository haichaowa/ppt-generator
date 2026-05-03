# Glow 主题配置

## 主题 ID: glow

动态发光多边形背景 + 毛玻璃卡片 + 深色基调，为 Slidev 演示文稿提供科技感十足的视觉效果。

## 必需文件

| 文件 | 路径 | 说明 |
|------|------|------|
| global-bottom.vue | `assets/themes/glow/global-bottom.vue` | 动态发光背景组件（必须，提供 glow 效果） |
| uno.config.ts | `assets/themes/glow/uno.config.ts` | UnoCSS 配置（presetWebFonts + bunny provider） |
| style.css | `assets/themes/glow/style.css` | 深色背景样式、过渡动画、balance 动画 |

## 全局 Headmatter 约束

```yaml
colorSchema: dark          # 必须：深色背景配合发光效果
css: unocss                # 必须：启用 UnoCSS
highlighter: shiki         # 推荐：Shiki 代码高亮
```

## Per-Slide Frontmatter 选项

| 选项 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `glow` | string | — | 发光位置：`full` / `top` / `bottom` / `left` / `right` / `center` / `top-left` / `top-right` / `bottom-left` / `bottom-right` / `topmost` |
| `glowOpacity` | number | `0.4` | 透明度 (0-1) |
| `glowHue` | number | `0` | 色调偏移（度数） |
| `glowSeed` | string \| number | — | 随机种子，每页不同获得变化效果 |

## 设计模式

### 毛玻璃卡片（Glassmorphism）
使用 `backdrop-blur` + 半透明背景 + 彩色边框：
```html
<div border="2 solid violet-800/50" rounded-lg bg="violet-900/10" backdrop-blur-sm>
```

### 渐变边框卡片
```html
<div border="2 solid {color}-800/50" rounded-lg>
  <div flex items-center bg="{color}-800/30" px-3 py-2 text-{color}-300>
    <div i-carbon:xxx text-sm mr-1 />
    <div text-xs><em>标题</em></div>
  </div>
  <div bg="{color}-800/10" px-4 py-3>描述</div>
</div>
```

## 配色方案

| 色系 | 可用颜色 | 适用场景 |
|------|---------|---------|
| 主色系 | `violet` / `purple` / `fuchsia` | 主概念、核心特性 |
| 辅助色 | `blue` / `cyan` / `sky` | 次要概念、技术细节 |
| 强调色 | `green` / `indigo` / `amber` | 结果、对比、高亮 |
| 暖色系 | `orange` / `rose` / `red` | 警告、旧方案、问题 |
| 冷色系 | `teal` / `emerald` / `lime` | 成功、新方案、解决方案 |

## 已知约束

1. **必须使用 `colorSchema: dark`** — 浅色背景无法展现发光效果
2. **Web Fonts 必须使用 `provider: 'bunny'`** — 国内网络无法访问 Google Fonts
3. **`/` 在裸属性中会导致编译错误** — 必须用 `class="text-white/50"` 形式
4. **`glowSeed` 建议每页不同** — 建议递增（如 150, 200, 250, ...）以获得视觉变化

## Balance 动画

Glow 主题提供额外的 CSS 动画：
- `animate-balance-shake` — 摇晃动画
- `animate-balance-move-left` — 左移动画
- `animate-balance-move-right` — 右移动画
