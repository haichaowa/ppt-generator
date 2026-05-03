# Slidev 布局参考

Slidev 内置布局和 Headmatter 配置的完整参考，适用于所有主题。

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

---

## 内置布局模板

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

### iframe — 嵌入网页

```markdown
---
layout: iframe
url: https://example.com
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

## 过渡动画选项

| 值 | 效果 |
|-----|------|
| `fade` | 淡入淡出 |
| `fade-out` | 淡出（推荐） |
| `slide-left` | 从右滑入 |
| `slide-right` | 从左滑入 |
| `slide-up` | 从下滑入 |
| `slide-down` | 从上滑入 |
| `zoom` | 缩放 |

---

## 内容-布局映射表

| 原始内容特征 | 推荐布局 | Frontmatter 配置 |
|-------------|---------|-----------------|
| 演讲标题 + 副标题 | `center` | `layout: center` |
| 章节分隔/编号切换 | `section` | `layout: section` |
| 观点 + 3-5 论据 | `default` | （默认布局） |
| 对比/优缺点分析 | `two-cols` | `layout: two-cols` + `::right::` |
| 带标题的对比 | `two-cols-header` | `layout: two-cols-header` + `::left::`+`::right::` |
| 图片+文字说明 | `image-left/right` | `layout: image-left` + `image: 路径` |
| 全屏图片 | `image` | `layout: image` + `image: 路径` |
| 嵌入网页演示 | `iframe` | `layout: iframe` + `url: 网址` |
| 名言金句 | `quote` | `layout: quote` |
| 关键数据展示（单个） | `fact` | `layout: fact` |
| 核心结论陈述 | `center` 或 `statement` | `layout: statement` |
| 演讲者介绍 | `intro` | `layout: intro` |
| 结束致谢 | `end` | `layout: end` |
