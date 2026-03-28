# Model Context Protocol (MCP) 完整文档

## 目录
1. [入门指南](#入门指南)
2. [核心概念](#核心概念)
3. [架构设计](#架构设计)
4. [开发指南](#开发指南)
5. [示例和最佳实践](#示例和最佳实践)

---

## 入门指南

### 什么是 Model Context Protocol (MCP)?

MCP (Model Context Protocol) 是一个开源标准，用于将AI应用程序连接到外部系统。通过MCP，AI应用程序（如Claude或ChatGPT）可以连接到：
- 数据源（如本地文件、数据库）
- 工具（如搜索引擎、计算器）
- 工作流程（如专业提示词）

这使AI能够访问关键信息并执行任务。

#### MCP的作用

MCP就像AI应用程序的USB-C端口。正如USB-C提供了连接电子设备的标准化方式，MCP提供了将AI应用程序连接到外部系统的标准化方式。

#### MCP能够实现什么

1. **AI助手可以访问你的Google Calendar和Notion**，作为更个性化的AI助手
2. **Claude Code可以使用Figma设计生成完整的Web应用**
3. **企业聊天机器人可以连接组织内的多个数据库**，使用户能够通过聊天分析数据
4. **AI模型可以在Blender上创建3D设计并使用3D打印机打印出来**

#### 为什么MCP很重要

根据你在生态系统中的位置，MCP具有不同的优势：

- **开发者**：MCP减少了构建或集成AI应用程序或代理时的开发时间和复杂性
- **AI应用程序或代理**：MCP提供了对数据源、工具和应用程序生态系统的访问，从而增强功能并改善最终用户体验
- **最终用户**：MCP产生了更强大的AI应用程序或代理，可以访问你的数据并在必要时代表你采取行动

#### 广泛的生态系统支持

MCP是一个开放协议，在各种客户端和服务器中得到支持。AI助手如Claude和ChatGPT，开发工具如Visual Studio Code、Cursor、MCPJam等都支持MCP——使得一次构建即可随处集成。

---

## 核心概念

### MCP的三大核心原语

MCP定义了三个核心原语，服务器可以暴露这些原语：

#### 1. 工具 (Tools)

工具是可执行函数，AI应用程序可以调用它们来执行操作。

**特点：**
- 可执行的操作（如文件操作、API调用、数据库查询）
- 通过`tools/list`发现
- 通过`tools/call`调用

**工具结构：**
```javascript
{
  name: string;          // 工具的唯一标识符
  description?: string;  // 人类可读的描述
  inputSchema: {         // 工具参数的JSON Schema
    type: "object",
    properties: { ... }  // 工具特定参数
  },
  annotations?: {        // 工具行为的可选提示
    title?: string;      // 工具的人类可读标题
    readOnlyHint?: boolean;    // 如果为true，工具不会修改其环境
    destructiveHint?: boolean; // 如果为true，工具可能执行破坏性更新
    idempotentHint?: boolean;  // 如果为true，使用相同参数重复调用没有额外效果
    openWorldHint?: boolean;   // 如果为true，工具与外部实体交互
  }
}
```

**工具示例：**
```javascript
{
  name: "calculate_sum",
  description: "将两个数字相加",
  inputSchema: {
    type: "object",
    properties: {
      a: { type: "number" },
      b: { type: "number" }
    },
    required: ["a", "b"]
  }
}
```

#### 2. 资源 (Resources)

资源是向客户端提供上下文信息的数据源。

**资源类型：**
- 文件内容
- 数据库记录
- API响应
- 实时系统数据
- 截图和图像
- 日志文件

**资源结构：**
```javascript
{
  uri: string;           // 资源的唯一标识符
  name: string;          // 人类可读的名称
  description?: string;  // 可选描述
  mimeType?: string;     // 可选MIME类型
  size?: number;         // 可选大小（字节）
}
```

**资源URI格式：**
```
[protocol]://[host]/[path]
```

示例：
- `file:///home/user/documents/report.pdf`
- `postgres://database/customers/schema`
- `screen://localhost/display1`

#### 3. 提示词 (Prompts)

提示词是可重用的模板，帮助构建与语言模型的交互。

**提示词结构：**
```javascript
{
  name: string;              // 提示词的唯一标识符
  description?: string;      // 人类可读的描述
  arguments?: [              // 可选参数列表
    {
      name: string;          // 参数标识符
      description?: string;  // 参数描述
      required?: boolean;    // 参数是否必需
    }
  ]
}
```

**提示词功能：**
- 接受动态参数
- 包含资源的上下文
- 链接多个交互
- 指导特定工作流
- 作为UI元素显示（如斜杠命令）

### 客户端原语

MCP还定义了客户端可以暴露的原语：

1. **采样 (Sampling)**：允许服务器从客户端的AI应用程序请求语言模型完成
2. **引导 (Elicitation)**：允许服务器向用户请求额外信息
3. **日志记录 (Logging)**：使服务器能够向客户端发送日志消息

---

## 架构设计

### 参与者

MCP遵循客户端-服务器架构，其中：

1. **MCP主机 (MCP Host)**：协调和管理一个或多个MCP客户端的AI应用程序
2. **MCP客户端 (MCP Client)**：维护与MCP服务器的连接并从MCP服务器获取上下文供主机使用的组件
3. **MCP服务器 (MCP Server)**：向MCP客户端提供上下文的程序

**示例：**
- Visual Studio Code作为MCP主机
- 当VS Code连接到Sentry MCP服务器时，VS Code运行时实例化一个MCP客户端对象来维护连接
- 当VS Code连接到本地文件系统服务器时，它实例化另一个MCP客户端对象

### 层次结构

MCP由两个层次组成：

#### 1. 数据层

定义基于JSON-RPC的客户端-服务器通信协议，包括：
- 生命周期管理
- 核心原语（工具、资源、提示词、通知）

**数据层功能：**
- **生命周期管理**：处理连接初始化、能力协商和连接终止
- **服务器功能**：提供核心功能，包括AI操作的工具、上下文数据的资源和交互模板的提示词
- **客户端功能**：使服务器能够请求从主机LLM采样、引导用户输入和向客户端记录消息
- **实用功能**：支持实时更新通知和长时间运行操作的进度跟踪等附加功能

#### 2. 传输层

定义启用客户端和服务器之间数据交换的通信机制和通道，包括：
- 传输特定的连接建立
- 消息框架
- 授权

**支持的传输机制：**

1. **Stdio传输**
   - 使用标准输入/输出流进行同一机器上本地进程之间的直接进程通信
   - 提供最佳性能，无网络开销

2. **Streamable HTTP传输**
   - 使用HTTP POST进行客户端到服务器的消息传递
   - 可选的服务器发送事件以支持流式传输
   - 支持标准HTTP身份验证方法，包括不记名令牌、API密钥和自定义标头
   - MCP推荐使用OAuth获取身份验证令牌

### 连接生命周期

#### 1. 初始化

1. 客户端发送带有协议版本和能力的`initialize`请求
2. 服务器以其协议版本和能力响应
3. 客户端发送`initialized`通知作为确认
4. 正常消息交换开始

#### 2. 消息交换

初始化后，支持以下模式：
- **请求-响应**：客户端或服务器发送请求，另一方响应
- **通知**：任一方发送单向消息

#### 3. 终止

任一方都可以终止连接：
- 通过`close()`进行干净关闭
- 传输断开连接
- 错误条件

### 消息类型

MCP有以下主要消息类型：

1. **请求**：期望来自另一方的响应
```javascript
interface Request {
  method: string;
  params?: { ... };
}
```

2. **结果**：请求的成功响应
```javascript
interface Result {
  [key: string]: unknown;
}
```

3. **错误**：指示请求失败
```javascript
interface Error {
  code: number;
  message: string;
  data?: unknown;
}
```

4. **通知**：不期望响应的单向消息
```javascript
interface Notification {
  method: string;
  params?: { ... };
}
```

### 错误处理

MCP定义了这些标准错误代码：

```javascript
enum ErrorCode {
  // 标准JSON-RPC错误代码
  ParseError = -32700,
  InvalidRequest = -32600,
  MethodNotFound = -32601,
  InvalidParams = -32602,
  InternalError = -32603,
}
```

SDK和应用程序可以在-32000以上定义自己的错误代码。

**错误传播途径：**
- 对请求的错误响应
- 传输上的错误事件
- 协议级错误处理程序

---

## 开发指南

### 构建MCP服务器

#### 基本服务器实现

```javascript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server({
  name: "example-server",
  version: "1.0.0"
}, {
  capabilities: {
    resources: {}
  }
});

// 处理请求
server.setRequestHandler(ListResourcesRequestSchema, async () => {
  return {
    resources: [
      {
        uri: "example://resource",
        name: "示例资源"
      }
    ]
  };
});

// 连接传输
const transport = new StdioServerTransport();
await server.connect(transport);
```

#### 实现资源支持

```javascript
const server = new Server({
  name: "example-server",
  version: "1.0.0"
}, {
  capabilities: {
    resources: {}
  }
});

// 列出可用资源
server.setRequestHandler(ListResourcesRequestSchema, async () => {
  return {
    resources: [
      {
        uri: "file:///logs/app.log",
        name: "应用程序日志",
        mimeType: "text/plain"
      }
    ]
  };
});

// 读取资源内容
server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
  const uri = request.params.uri;

  if (uri === "file:///logs/app.log") {
    const logContents = await readLogFile();
    return {
      contents: [
        {
          uri,
          mimeType: "text/plain",
          text: logContents
        }
      ]
    };
  }

  throw new Error("未找到资源");
});
```

#### 实现工具支持

```javascript
const server = new Server({
  name: "example-server",
  version: "1.0.0"
}, {
  capabilities: {
    tools: {}
  }
});

// 定义可用工具
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [{
      name: "calculate_sum",
      description: "将两个数字相加",
      inputSchema: {
        type: "object",
        properties: {
          a: { type: "number" },
          b: { type: "number" }
        },
        required: ["a", "b"]
      }
    }]
  };
});

// 处理工具执行
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "calculate_sum") {
    const { a, b } = request.params.arguments;
    return {
      content: [
        {
          type: "text",
          text: String(a + b)
        }
      ]
    };
  }
  throw new Error("未找到工具");
});
```

#### 实现提示词支持

```javascript
import { Server } from "@modelcontextprotocol/sdk/server";
import {
  ListPromptsRequestSchema,
  GetPromptRequestSchema
} from "@modelcontextprotocol/sdk/types";

const PROMPTS = {
  "git-commit": {
    name: "git-commit",
    description: "生成Git提交消息",
    arguments: [
      {
        name: "changes",
        description: "Git diff或更改描述",
        required: true
      }
    ]
  },
  "explain-code": {
    name: "explain-code",
    description: "解释代码如何工作",
    arguments: [
      {
        name: "code",
        description: "要解释的代码",
        required: true
      },
      {
        name: "language",
        description: "编程语言",
        required: false
      }
    ]
  }
};

const server = new Server({
  name: "example-prompts-server",
  version: "1.0.0"
}, {
  capabilities: {
    prompts: {}
  }
});

// 列出可用提示词
server.setRequestHandler(ListPromptsRequestSchema, async () => {
  return {
    prompts: Object.values(PROMPTS)
  };
});

// 获取特定提示词
server.setRequestHandler(GetPromptRequestSchema, async (request) => {
  const prompt = PROMPTS[request.params.name];
  if (!prompt) {
    throw new Error(`未找到提示词：${request.params.name}`);
  }

  if (request.params.name === "git-commit") {
    return {
      messages: [
        {
          role: "user",
          content: {
            type: "text",
            text: `为这些更改生成简洁但描述性的提交消息：\n\n${request.params.arguments?.changes}`
          }
        }
      ]
    };
  }

  if (request.params.name === "explain-code") {
    const language = request.params.arguments?.language || "未知";
    return {
      messages: [
        {
          role: "user",
          content: {
            type: "text",
            text: `解释这个${language}代码是如何工作的：\n\n${request.params.arguments?.code}`
          }
        }
      ]
    };
  }

  throw new Error("未找到提示词实现");
});
```

### 工具类型示例

#### 系统操作工具

```javascript
{
  name: "execute_command",
  description: "运行shell命令",
  inputSchema: {
    type: "object",
    properties: {
      command: { type: "string" },
      args: { type: "array", items: { type: "string" } }
    }
  }
}
```

#### API集成工具

```javascript
{
  name: "github_create_issue",
  description: "创建GitHub问题",
  inputSchema: {
    type: "object",
    properties: {
      title: { type: "string" },
      body: { type: "string" },
      labels: { type: "array", items: { type: "string" } }
    }
  }
}
```

#### 数据处理工具

```javascript
{
  name: "analyze_csv",
  description: "分析CSV文件",
  inputSchema: {
    type: "object",
    properties: {
      filepath: { type: "string" },
      operations: {
        type: "array",
        items: {
          enum: ["sum", "average", "count"]
        }
      }
    }
  }
}
```

### 工具注释示例

```javascript
// 只读搜索工具
{
  name: "web_search",
  description: "在网络上搜索信息",
  inputSchema: {
    type: "object",
    properties: {
      query: { type: "string" }
    },
    required: ["query"]
  },
  annotations: {
    title: "网络搜索",
    readOnlyHint: true,
    openWorldHint: true
  }
}

// 破坏性文件删除工具
{
  name: "delete_file",
  description: "从文件系统中删除文件",
  inputSchema: {
    type: "object",
    properties: {
      path: { type: "string" }
    },
    required: ["path"]
  },
  annotations: {
    title: "删除文件",
    readOnlyHint: false,
    destructiveHint: true,
    idempotentHint: true,
    openWorldHint: false
  }
}

// 非破坏性数据库记录创建工具
{
  name: "create_record",
  description: "在数据库中创建新记录",
  inputSchema: {
    type: "object",
    properties: {
      table: { type: "string" },
      data: { type: "object" }
    },
    required: ["table", "data"]
  },
  annotations: {
    title: "创建数据库记录",
    readOnlyHint: false,
    destructiveHint: false,
    idempotentHint: false,
    openWorldHint: false
  }
}
```

---

## 示例和最佳实践

### 传输选择

#### 本地通信
- 使用stdio传输进行本地进程通信
- 对同一机器通信效率高
- 简单的进程管理

#### 远程通信
- 对需要HTTP兼容性的场景使用Streamable HTTP
- 考虑安全影响，包括身份验证和授权

### 消息处理

#### 请求处理
1. 彻底验证输入
2. 使用类型安全的模式
3. 优雅地处理错误
4. 实现超时

#### 进度报告
1. 对长操作使用进度令牌
2. 增量报告进度
3. 在已知时包含总进度

#### 错误管理
1. 使用适当的错误代码
2. 包含有帮助的错误消息
3. 在错误时清理资源

### 安全考虑

#### 传输安全
- 对远程连接使用TLS
- 验证连接来源
- 在需要时实现身份验证

#### 消息验证
- 验证所有传入消息
- 清理输入
- 检查消息大小限制
- 验证JSON-RPC格式

#### 资源保护
- 实现访问控制
- 验证资源路径
- 监控资源使用
- 对请求进行速率限制

#### 错误处理
- 不要泄露敏感信息
- 记录安全相关错误
- 实现适当的清理
- 处理DoS场景

### 资源实现最佳实践

1. 使用清晰、描述性的资源名称和URI
2. 包含有帮助的描述以指导LLM理解
3. 在已知时设置适当的MIME类型
4. 为动态内容实现资源模板
5. 对频繁更改的资源使用订阅
6. 优雅地处理错误并提供清晰的错误消息
7. 考虑对大型资源列表进行分页
8. 在适当时缓存资源内容
9. 在处理前验证URI
10. 记录自定义URI方案

### 工具实现最佳实践

1. 提供清晰、描述性的名称和描述
2. 为参数使用详细的JSON Schema定义
3. 在工具描述中包含示例以演示模型应如何使用它们
4. 实现适当的错误处理和验证
5. 对长操作使用进度报告
6. 保持工具操作专注和原子化
7. 记录预期的返回值结构
8. 实现适当的超时
9. 对资源密集型操作考虑速率限制
10. 记录工具使用以进行调试和监控

### 提示词实现最佳实践

1. 使用清晰、描述性的提示词名称
2. 为提示词和参数提供详细描述
3. 验证所有必需参数
4. 优雅地处理缺失参数
5. 考虑提示词模板的版本控制
6. 在适当时缓存动态内容
7. 实现错误处理
8. 记录预期的参数格式
9. 考虑提示词的可组合性
10. 使用各种输入测试提示词

### 调试和监控

#### 日志记录
- 记录协议事件
- 跟踪消息流
- 监控性能
- 记录错误

#### 诊断
- 实现健康检查
- 监控连接状态
- 跟踪资源使用
- 性能分析

#### 测试
- 测试不同的传输
- 验证错误处理
- 检查边缘情况
- 负载测试服务器

### 工具错误处理示例

```javascript
try {
  // 工具操作
  const result = performOperation();
  return {
    content: [
      {
        type: "text",
        text: `操作成功：${result}`
      }
    ]
  };
} catch (error) {
  return {
    isError: true,
    content: [
      {
        type: "text",
        text: `错误：${error.message}`
      }
    ]
  };
}
```

### UI集成

提示词可以在客户端UI中显示为：
- 斜杠命令
- 快速操作
- 上下文菜单项
- 命令面板条目
- 引导工作流
- 交互式表单

### 动态更新

服务器可以通知客户端有关更改：

1. 服务器能力：`prompts.listChanged`
2. 通知：`notifications/prompts/list_changed`
3. 客户端重新获取提示词列表

### 资源更新机制

MCP通过两种机制支持资源的实时更新：

#### 列表更改
服务器可以通过`notifications/resources/list_changed`通知客户端其可用资源列表何时更改。

#### 内容更改
客户端可以订阅特定资源的更新：
1. 客户端发送带有资源URI的`resources/subscribe`
2. 服务器在资源更改时发送`notifications/resources/updated`
3. 客户端可以使用`resources/read`获取最新内容
4. 客户端可以使用`resources/unsubscribe`取消订阅

---

## MCP生态系统

### 支持的客户端
- Claude
- ChatGPT
- Visual Studio Code
- Cursor
- MCPJam
- 以及更多

### 预构建的服务器
- GitHub
- Google Drive
- Slack
- 数百个其他工具

### 开发资源
- MCP规范：概述客户端和服务器实现要求的规范
- MCP SDK：不同编程语言的SDK
- MCP开发工具：开发MCP服务器和客户端的工具，包括MCP Inspector
- MCP参考服务器实现：MCP服务器的参考实现

---

## 总结

Model Context Protocol (MCP) 是一个强大的开放标准，通过标准化的方式连接AI应用程序与外部系统。它提供了：

1. **三大核心原语**：工具、资源和提示词
2. **灵活的架构**：支持多种传输机制
3. **丰富的生态系统**：广泛的客户端和服务器支持
4. **开发友好**：提供多种语言SDK和开发工具
5. **安全可靠**：内置安全考虑和最佳实践

通过MCP，开发者可以构建一次，随处集成，为AI应用程序提供强大的上下文和操作能力。