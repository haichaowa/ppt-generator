# Slidev 布局模式指南

为每种 Slidev 内置布局提供完整的 Markdown 模板。

---

## Headmatter 完整配置（全局）

第一张幻灯片的 frontmatter 同时作为全局配置（headmatter）：

```yaml
---
layout: center
highlighter: shiki
css: unocss
colorSchema: dark
transition: fade-out
title: 演示标题
exportFilename: 导出文件名
lineNumbers: false
drawings:
  persist: false
mdc: true
---
```

### 常用 headmatter 选项

| 选项 | 说明 | 示例 |
|------|------|------|
| `theme` | 主题名 | `default`, `seriph` |
| `title` | 演示文稿标题 | `我的演讲` |
| `highlighter` | 代码高亮器 | `shiki` |
| `css` | CSS 框架 | `unocss` |
| `colorSchema` | 颜色模式 | `dark`, `light`, `auto` |
| `transition` | 默认过渡动画 | `fade-out` |
| `lineNumbers` | 显示行号 | `true`/`false` |
| `drawings.persist` | 保存绘图 | `true`/`false` |
| `mdc` | 启用 MDC 语法 | `true` |
| `fonts` | 自定义字体 | `sans: 'DM Sans'` |
| `aspectRatio` | 画面比例 | `16/9` |
| `canvasWidth` | 画布宽度 | `980` |
| `download` | PDF下载按钮 | `true`/`false` |
| `exportFilename` | 导出文件名 | `my-slides` |

### Per-Slide Frontmatter 选项

| 选项 | 说明 | 示例 |
|------|------|------|
| `layout` | 布局类型 | `center`, `two-cols` |
| `transition` | 本页过渡 | `slide-left` |
| `background` | 背景图片 | `/bg.jpg` |
| `class` | CSS 类 | `text-white text-center` |
| `clicks` | 点击次数 | `5` |
| `zoom` | 缩放比例 | `0.8` |
| `disabled` | 隐藏本页 | `true` |
| `hideInToc` | 从目录隐藏 | `true` |
| `src` | 导入外部文件 | `./intro.md` |
| `glow` | Glow分布(glow主题) | `left`, `right`, `full` |
| `glowOpacity` | Glow透明度 | `0.4` |
| `glowHue` | Glow色调偏移 | `30` |
| `glowSeed` | Glow随机种子 | `my-seed` |

---

## 布局模板

### center — 居中（封面页）

```markdown
---
layout: center
---

# 演讲标题

<div class="abs-br m-6 text-sm opacity-50">
  演讲者 · 日期
</div>
```

### section — 章节分隔

```markdown
---
layout: section
---

# 01

章节名称
```

### default — 标准内容（默认）

```markdown
---
---

## 观点标题

- 论据一
- 论据二
- 论据三

<!-- 演讲者备注 -->
```

### two-cols — 双栏对比

```markdown
---
layout: two-cols
---

## 方案 A

- 优点一
- 优点二

::right::

## 方案 B

- 优点一
- 优点二
```

### two-cols-header — 带标题双栏

```markdown
---
layout: two-cols-header
---

## 对比标题

::left::

### 左侧
内容

::right::

### 右侧
内容
```

### image-left — 左图右文

```markdown
---
layout: image-left
image: /photo.jpg
---

## 标题

说明文字
```

### image-right — 左文右图

```markdown
---
layout: image-right
image: /photo.jpg
---

## 标题

说明文字
```

### image — 全屏图片

```markdown
---
layout: image
image: /photo.jpg
backgroundSize: cover
class: text-white
---
```

### quote — 引用

```markdown
---
layout: quote
---

> 名言内容

— 作者
```

### fact — 数据展示

```markdown
---
layout: fact
---

## 93%

关键数据说明
```

### statement — 核心陈述

```markdown
---
layout: statement
---

## 核心结论

一句话总结
```

### intro — 介绍页

```markdown
---
layout: intro
---

# 演讲标题

演讲副标题或描述

<div class="abs-br m-6">
  演讲者信息
</div>
```

### end — 结束页

```markdown
---
layout: end
---

感谢观看！

联系方式或二维码
```

---

## 常用组件速查

### Link — 页面链接
```html
<Link to="3">跳转到第3页</Link>
<Link to="intro">跳转到别名页</Link>
```

### Toc — 目录
```html
<Toc />
<Toc maxDepth="2" />
```

### VClick — 点击动画
```html
<v-click>
  <div>点击后出现</div>
</v-click>

<v-clicks depth="2">
- 项目一
  - 子项目
- 项目二
</v-clicks>
```

### Arrow — 箭头
```html
<Arrow x1="100" y1="100" x2="400" y2="200" color="green" />
<Arrow v-bind="arrow1" />
```

### Transform — 缩放
```html
<Transform :scale="0.8">
  <div>缩小到80%</div>
</Transform>
```

### Mermaid — 图表
````markdown
```mermaid
graph LR
  A[开始] --> B[过程] --> C[结束]
```
````

### LaTeX — 数学公式
```markdown
行内公式: $E = mc^2$

块级公式:
$$
\frac{a}{b} = c
$$
```
