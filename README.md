# PPT Generator

基于 [Slidev](https://sli.dev/) 的演示文稿生成器，使用 Markdown + Vue 3 + UnoCSS 编写幻灯片，支持 Glow 发光主题、代码高亮、动画效果。

## 快速开始

### 环境要求

- Node.js >= 18
- pnpm（`npm install -g pnpm`）

### 安装依赖

```bash
# 在项目根目录安装共享依赖
pnpm install
```

### 运行一个 PPT

```bash
# 进入某个演示文稿目录
    cd artifact/2026-03-28-airi-intro

# 启动开发服务器（自动打开浏览器）
pnpm run dev
```

启动后浏览器会自动打开 `http://localhost:3030`，修改 `slides.md` 保存后页面自动热更新。

### 导出 PDF

```bash
cd artifact/2026-03-28-airi-intro
pnpm run export
```

导出的 PDF 文件会生成在当前目录下。

### 构建为静态站点

```bash
cd artifact/2026-03-28-airi-intro
pnpm run build
```

构建产物输出到 `dist/` 目录，可直接部署到任意静态托管服务。

## 项目结构

```
ppt-generator/
├── artifact/                    # 生成的演示文稿（每个子目录是一个独立的 Slidev 项目）
│   ├── 2026-03-28-airi-intro/
│   │   ├── slides.md            # 幻灯片内容（主文件）
│   │   ├── package.json         # 项目配置（dev/build/export 脚本）
│   │   ├── uno.config.ts        # UnoCSS 配置
│   │   ├── style.css            # 自定义样式
│   │   ├── global-bottom.vue    # Glow 主题背景组件
│   │   ├── public/              # 图片、视频等静态资源
│   │   └── setup/               # Shiki 代码高亮等配置
│   └── ...
├── ppt-skills/slidev-ppt-generator/   # PPT 生成器 Skill 定义
│   ├── SKILL.md                 # 核心生成逻辑和规范
│   └── references/              # 内容规则、布局模板、示例
├── package.json                 # Monorepo 根配置
└── pnpm-workspace.yaml
```

## 可用的演示文稿

| 目录 | 主题 |
|------|------|
| `artifact/2026-03-28-airi-intro` | Airi 项目介绍 |
| `artifact/2026-03-28-mcp-intro` | MCP 协议介绍 |
| `artifact/2026-04-01-react-tic-tac-toe` | React 井字棋教程 |
| `artifact/2026-04-04-langchain-tools` | LangChain Tools 讲解 |
| `artifact/2026-04-05-langchain-short-term-memory` | LangChain 短期记忆机制 |
| `artifact/k8s-presentation` | Kubernetes 演讲 |

## 技术栈

- [Slidev](https://sli.dev/) — Markdown 驱动的演示文稿框架
- [UnoCSS](https://unocss.dev/) — 原子化 CSS 引擎
- [Vue 3](https://vuejs.org/) — 组件和动画
- [Shiki](https://shiki.style/) — 代码语法高亮
