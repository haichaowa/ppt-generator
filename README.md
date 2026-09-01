# PPT Generator

基于 [Slidev](https://sli.dev/) 的演示文稿生成器工作区。核心是 `ppt-skills/slidev-ppt-generator/` 中的生成器 Skill（工作流 + 布局模式 + 踩坑记录），配合 pnpm workspace 管理。

> 2026-09 起重构中：旧演示文稿和素材已清理（可在 git 历史中找回），保留 Skill 知识资产作为新项目的起点。

## 项目结构

```
ppt-generator/
├── ppt-skills/slidev-ppt-generator/   # 生成器 Skill
│   ├── SKILL.md                       # 6 步工作流 + 视觉设计模式 + 常见错误
│   ├── references/                    # 内容规则、Glow 布局模式、布局/组件参考
│   └── assets/                        # default 模板 + Glow 主题文件
├── contents/                          # 内容管道（生成时按需创建）
│   ├── ori/                           # 原始材料 → 结构化 → artifact/
│   └── generate/
├── artifact/                          # 生成的演示文稿（生成时按需创建）
├── package.json                       # Monorepo 根配置（共享依赖）
└── pnpm-workspace.yaml
```

## 使用

```bash
pnpm install                          # 安装共享依赖

# 生成新演示：按 ppt-skills/slidev-ppt-generator/SKILL.md 的工作流执行，
# 产物放在 artifact/{YYYY-MM-DD}-{topic}/

cd artifact/{topic} && pnpm run dev   # 启动开发服务器
cd artifact/{topic} && pnpm run build # 构建静态站点 → dist/
cd artifact/{topic} && pnpm run export # 导出 PDF
```

## 技术栈

- [Slidev](https://sli.dev/) — Markdown 驱动的演示文稿框架
- [UnoCSS](https://unocss.dev/) — 原子化 CSS 引擎
- [Vue 3](https://vuejs.org/) — 组件和动画
- [Shiki](https://shiki.style/) — 代码语法高亮
