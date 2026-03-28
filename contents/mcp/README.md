# Model Context Protocol (MCP) 文档索引

本文档目录包含 MCP (Model Context Protocol) 的完整中文翻译和整理内容。

## 文档结构

### 📚 [完整文档](./MCP-完整文档.md)
包含所有 MCP 相关内容的完整版本，适合全面了解 MCP。

### 📖 分主题文档

| 文档 | 描述 |
|------|------|
| [01-入门指南](./01-入门指南.md) | MCP 是什么、能做什么、为什么重要 |
| [02-核心概念](./02-核心概念.md) | 工具、资源、提示词三大核心原语 |
| [03-架构设计](./03-架构设计.md) | 参与者、层次结构、连接生命周期、消息类型 |
| [04-开发指南](./04-开发指南.md) | 构建 MCP 服务器的完整指南和代码示例 |
| [05-最佳实践](./05-最佳实践.md) | 传输选择、安全考虑、实现建议 |

## 快速导航

### 核心概念
- **工具 (Tools)**: 可执行函数，AI 可以调用
- **资源 (Resources)**: 数据源，提供上下文信息
- **提示词 (Prompts)**: 可重用的模板，指导交互

### 架构组件
- **MCP 主机**: 协调 AI 应用程序的组件
- **MCP 客户端**: 维护与服务器连接的组件
- **MCP 服务器**: 提供上下文的程序

### 传输层
- **Stdio**: 本地进程通信
- **HTTP**: 远程通信，支持 SSE

## 资源链接

- 官方文档: https://modelcontextprotocol.io/docs
- GitHub: https://github.com/modelcontextprotocol
- SDK 文档: https://github.com/modelcontextprotocol/servers

---

*更新时间: 2026-03-28*
