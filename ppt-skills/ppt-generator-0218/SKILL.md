---
name: ppt-generator
description: 从Markdown内容生成酷炫简洁的霓虹风格HTML演示文稿，专为B站视频设计。使用HTML注释标识幻灯片类型，支持11种页面类型。适用于用户请求创建演示文稿、幻灯片或PPT时。
---

# PPT生成器

从简单的Markdown输入生成具有霓虹美学的视觉冲击力HTML演示文稿，专为B站视频优化。

## 适用场景

- B站技术视频PPT
- 产品介绍演示
- 技术分享/教程
- 项目汇报

## 工作流程

1. **收集内容**: 如果未提供，向用户询问演示文稿的核心内容
2. **内容结构化**: 按照 `references/content-rules.md` 规则组织内容
3. **生成Markdown**: 将内容转换为符合规范的Markdown格式
4. **HTML转换**: 运行Python脚本生成最终HTML文件
5. **验证输出**: 确保生成的文件正常工作

## 幻灯片类型速查

| 类型 | 用途 | 标识语法 |
|-----|-----|---------|
| `cover` | 封面页 | `<!-- .slide: type=cover -->` |
| `toc` | 目录页 | `<!-- .slide: type=toc -->` |
| `chapter` | 章节页 | `<!-- .slide: type=chapter -->` |
| `content` | 标准内容 | `<!-- .slide: type=content -->` |
| `two-column` | 双栏对比 | `<!-- .slide: type=two-column -->` |
| `code` | 代码演示 | `<!-- .slide: type=code -->` |
| `data` | 数据表格 | `<!-- .slide: type=data -->` |
| `timeline` | 时间轴 | `<!-- .slide: type=timeline -->` |
| `grid` | 网格卡片(2x2/3x3) | `<!-- .slide: type=grid -->` |
| `quote` | 金句展示 | `<!-- .slide: type=quote -->` |
| `end` | 结束页 | `<!-- .slide: type=end -->` |

## Markdown格式规范

详细格式请参考 `references/md-format.md`。

### 1. 封面页 (cover)

```markdown
<!-- .slide: type=cover -->

# 视频主标题

## 副标题或Slogan

作者 | 2025.02.18
```

### 2. 目录页 (toc)

```markdown
<!-- .slide: type=toc -->

# 本期内容

## 01 背景介绍
## 02 核心概念
## 03 实战演示
## 04 总结回顾
```

### 3. 章节页 (chapter)

```markdown
<!-- .slide: type=chapter -->

# 01

## 章节名称
```

### 4. 内容页 (content)

```markdown
<!-- .slide: type=content -->

## 标题

描述文字段落。

- 要点一
- 要点二
- 要点三
```

### 5. 双栏页 (two-column)

```markdown
<!-- .slide: type=two-column -->

## 对比标题

### 左侧标题

左侧内容描述

- 左侧要点

---

### 右侧标题

右侧内容描述

- 右侧要点
```

### 6. 代码页 (code)

```markdown
<!-- .slide: type=code -->

## 代码标题

```python
def hello():
    print("Hello, World!")
```

### 代码说明
```

### 7. 数据页 (data)

```markdown
<!-- .slide: type=data -->

## 数据展示

| 项目 | 数值 | 增长 |
|-----|-----|-----|
| 用户 | 100万 | +25% |
| 收入 | 500万 | +40% |
```

### 8. 时间轴页 (timeline)

```markdown
<!-- .slide: type=timeline -->

## 发展历程

### 2020.01 项目启动
首次发布原型版本

### 2021.06 正式上线
用户突破10万

### 2022.12 规模化
用户突破100万
```

### 9. 网格页 (grid)

**仅支持 2x2（4卡片）或 3x3（9卡片）**

```markdown
<!-- .slide: type=grid -->

## 核心功能

### 功能一
- icon: ◉
- color: cyan
- desc: 功能描述

### 功能二
- icon: ◈
- color: purple
- desc: 功能描述

### 功能三
- icon: ◆
- color: pink
- desc: 功能描述

### 功能四
- icon: ▣
- color: orange
- desc: 功能描述
```

**约束**: 卡片数量必须是 4 或 9，每个卡片必须包含 `icon`、`color`、`desc`

### 10. 金句页 (quote)

```markdown
<!-- .slide: type=quote -->

## 引用金句

> 设计不仅仅是外观。设计是它如何工作。

### — 史蒂夫·乔布斯
```

### 11. 结束页 (end)

```markdown
<!-- .slide: type=end -->

# 感谢观看

## 点赞关注不迷路

作者 | 联系方式
```

## 内容转换规则

将原始文本转换为PPT Markdown时，遵循以下规则（详见 `references/content-rules.md`）：

### 核心原则

1. **一页一观点**: 每张幻灯片只传达一个核心观点
2. **金字塔原则**: 结论先行，以上统下
3. **少即是多**: 每页不超过50字，要点3-5条

### 页面数量建议

| 视频时长 | 推荐页数 |
|---------|---------|
| 3-5分钟 | 6-10页 |
| 5-10分钟 | 10-15页 |
| 10-20分钟 | 15-25页 |

### 类型匹配规则

| 内容特征 | 推荐类型 |
|---------|---------|
| 标题 + 简介 | cover |
| 并列项目 | toc / grid |
| 编号标题 | chapter |
| 观点 + 论据 | content |
| 对比内容 | two-column |
| 代码片段 | code |
| 数据表格 | data |
| 时间节点 | timeline |
| 名人名言 | quote |
| 致谢 | end |

### B站视频特殊规则

- 结束页必须有引导关注
- 适当使用金句页增加传播性
- 封面停留2-3秒，内容页30-60秒

## 命令使用

```bash
# 基本用法
python3 scripts/md_to_ppt.py input.md output.html

# 指定主题
python3 scripts/md_to_ppt.py input.md output.html --theme neon

# 查看帮助
python3 scripts/md_to_ppt.py --help
```

## 主题系统

当前支持霓虹(neon)主题，后续可扩展：

- 霓虹发光效果
- 毛玻璃容器
- 动态背景
- 键盘/触摸导航

## 输出特性

生成的HTML包含：

- **动态背景**: 带模糊效果的动态色球动画
- **霓虹效果**: 带发光阴影的脉冲文本
- **毛玻璃**: 带背景模糊的磨砂玻璃容器
- **响应式**: 适配桌面、平板、手机
- **导航**: 方向键、空格键、触摸滑动
- **进度条**: 顶部动画进度指示器

## 使用示例

当用户请求: "帮我生成一个关于Python异步编程的演示文稿"

**步骤1**: 收集关键信息
- 目标受众：有Python基础的开发者
- 视频时长：约10分钟
- 核心内容：asyncio基础、协程、实际应用

**步骤2**: 规划结构（约15页）
- 封面 → 目录 → 章节(3-4个) → 结束

**步骤3**: 生成Markdown（按照格式规范）

**步骤4**: 运行转换脚本

**步骤5**: 验证输出文件

---

详细格式规范请参考 `references/md-format.md`
内容转换规则请参考 `references/content-rules.md`
