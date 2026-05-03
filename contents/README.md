# contents/ 目录说明

本目录是 PPT 生成器的内容管道，遵循 `ori → generate → artifact` 三阶段工作流。

## 目录结构

```
contents/
├── ori/                  # 原始材料（用户提供的源文件）
│   └── {topic-slug}/     # 每个主题一个目录
│       ├── README.md     # 主题元数据（标题、来源、日期、备注）
│       ├── main.md       # 主要原始内容
│       └── assets/       # 可选：图片、PDF 等附件
├── generate/             # 结构化中间产物
│   └── {topic-slug}/     # 与 ori/ 同名
│       ├── metadata.json # 生成参数（时长、受众、主题、section 列表）
│       ├── outline.md    # 幻灯片结构大纲（每页标题、布局、要点）
│       └── content.md    # 完整内容（注释标记 slide 元数据）
└── README.md             # 本文件
```

## 命名规范

- **topic-slug**：小写英文，连字符分隔，如 `claude-code-best-practices`、`k8s-intro`
- 与 `artifact/` 命名对应但不含日期前缀（日期在 artifact 层加）
- ori/ 和 generate/ 下的 topic-slug 必须一致

## 支持的输入格式

- Markdown 文件（`.md`）— 主要格式
- 纯文本文件（`.txt`）
- URL — 通过 MCP 工具获取并转为 markdown
- 直接粘贴的内容

## 工作流

1. **ori/**：用户提供的原始材料，作为内容源头
2. **generate/**：经过结构化处理的中间产物，可直接喂给 SKILL 生成 Slidev 项目
3. **artifact/**：最终生成的 Slidev 演示文稿（在项目根目录）

## generate/ 中间格式说明

### metadata.json
机器可读的生成参数，包含主题、受众、时长、目标页数、选择的主题等。

### outline.md
幻灯片结构大纲，列出每一页的序号、标题、布局类型、核心要点。

### content.md
完整的结构化内容，使用注释标记 slide 元数据：
```markdown
<!-- slide: cover | layout: center | glowSeed: 150 -->
# 标题
内容...
```
