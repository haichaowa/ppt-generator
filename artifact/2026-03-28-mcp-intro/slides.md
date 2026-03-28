---
layout: center
highlighter: shiki
css: unocss
colorSchema: dark
transition: fade-out
title: 'Model Context Protocol: AI 连接世界的标准化接口'
exportFilename: mcp-introduction
lineNumbers: false
drawings:
  persist: false
mdc: true
clicks: 0
preload: false
glowSeed: 233
routerMode: hash
fonts:
  sans: 'DM Sans'
  mono: 'Fira Code'
---

<div flex flex-col items-center gap-4>

<div class="text-lg text-white/30">
  Model Context Protocol
</div>
<div class="text-3xl">
  MCP：AI 连接世界的标准化接口
</div>
<div class="text-white/50 mt-2">
  20 分钟带你理解 MCP 的设计、开发与生态
</div>

</div>

<!--
开场：欢迎来到本次关于 MCP 的技术分享。MCP 是一个正在快速发展的开放标准，它让 AI 应用能够连接到外部世界。今天我们用 20 分钟来全面了解它。
-->

---
layout: section
glowSeed: 200
---

# 01

什么是 MCP

<!--
第一章：认识 MCP，了解它是什么、解决什么问题
-->

---
class: py-10
glowSeed: 250
---

## MCP 是什么？

<span>Model Context Protocol — AI 应用的 USB-C 接口</span>

<div mt-8 />

<div grid grid-cols-2 gap-4>

<div border="2 solid blue-800/50" rounded-lg overflow-hidden bg="blue-900/10" backdrop-blur-sm>
  <div flex items-center bg="blue-800/30" px-3 py-2 text-blue-300>
    <div i-carbon:plug text-sm mr-2 />
    <div font-semibold>标准化连接</div>
  </div>
  <div bg="blue-900/5" px-4 py-3>
    <div text-sm>开放标准，连接 AI 应用与外部系统</div>
    <div text-xs opacity-70 mt-2>数据源、工具、工作流，一次构建随处集成</div>
  </div>
</div>

<div border="2 solid violet-800/50" rounded-lg overflow-hidden bg="violet-900/10" backdrop-blur-sm>
  <div flex items-center bg="violet-800/30" px-3 py-2 text-violet-300>
    <div i-carbon:connect text-sm mr-2 />
    <div font-semibold>类比 USB-C</div>
  </div>
  <div bg="violet-900/5" px-4 py-3>
    <div text-sm>正如 USB-C 统一了设备连接</div>
    <div text-xs opacity-70 mt-2>MCP 统一了 AI 与外部系统的交互方式</div>
  </div>
</div>

<div border="2 solid green-800/50" rounded-lg overflow-hidden bg="green-900/10" backdrop-blur-sm>
  <div flex items-center bg="green-800/30" px-3 py-2 text-green-300>
    <div i-carbon:data-base text-sm mr-2 />
    <div font-semibold>连接数据</div>
  </div>
  <div bg="green-900/5" px-4 py-3>
    <div text-sm>本地文件、数据库、API 响应</div>
    <div text-xs opacity-70 mt-2>让 AI 获取关键上下文信息</div>
  </div>
</div>

<div border="2 solid amber-800/50" rounded-lg overflow-hidden bg="amber-900/10" backdrop-blur-sm>
  <div flex items-center bg="amber-800/30" px-3 py-2 text-amber-300>
    <div i-carbon:task-tools text-sm mr-2 />
    <div font-semibold>连接工具</div>
  </div>
  <div bg="amber-900/5" px-4 py-3>
    <div text-sm>搜索引擎、计算器、文件操作</div>
    <div text-xs opacity-70 mt-2>让 AI 能够执行实际操作</div>
  </div>
</div>

</div>

<!--
MCP 就像 AI 应用的 USB-C 接口。它是一个开放标准，让 AI 应用能够以统一的方式连接到外部系统——无论是数据源、工具还是工作流。
-->

---
class: py-10
glowSeed: 280
clicks: 4
---

## MCP 能做什么？

<span>四个真实场景</span>

<div mt-6 />

<div grid grid-cols-2 gap-3>

<v-clicks>

<div border="2 solid violet-800/50" rounded-lg overflow-hidden bg="violet-900/10" backdrop-blur-sm>
  <div flex items-center bg="violet-800/30" px-3 py-2 text-violet-300>
    <div i-carbon:calendar text-sm mr-1 />
    <div font-semibold>个性化 AI 助手</div>
  </div>
  <div bg="violet-900/5" px-4 py-3>
    <div text-sm>访问 Google Calendar 和 Notion</div>
    <div text-xs opacity-70>成为更懂你的私人助手</div>
  </div>
</div>

<div border="2 solid blue-800/50" rounded-lg overflow-hidden bg="blue-900/10" backdrop-blur-sm>
  <div flex items-center bg="blue-800/30" px-3 py-2 text-blue-300>
    <div i-carbon:code text-sm mr-1 />
    <div font-semibold>设计稿生成应用</div>
  </div>
  <div bg="blue-900/5" px-4 py-3>
    <div text-sm>Claude Code + Figma 设计</div>
    <div text-xs opacity-70>从设计稿直接生成 Web 应用</div>
  </div>
</div>

<div border="2 solid green-800/50" rounded-lg overflow-hidden bg="green-900/10" backdrop-blur-sm>
  <div flex items-center bg="green-800/30" px-3 py-2 text-green-300>
    <div i-carbon:analytics text-sm mr-1 />
    <div font-semibold>企业数据分析</div>
  </div>
  <div bg="green-900/5" px-4 py-3>
    <div text-sm>连接多个数据库</div>
    <div text-xs opacity-70>通过聊天即可分析数据</div>
  </div>
</div>

<div border="2 solid amber-800/50" rounded-lg overflow-hidden bg="amber-900/10" backdrop-blur-sm>
  <div flex items-center bg="amber-800/30" px-3 py-2 text-amber-300>
    <div i-carbon:3d-cursor text-sm mr-1 />
    <div font-semibold>3D 设计与打印</div>
  </div>
  <div bg="amber-900/5" px-4 py-3>
    <div text-sm>AI 在 Blender 上创建 3D 设计</div>
    <div text-xs opacity-70>并直接使用 3D 打印机输出</div>
  </div>
</div>

</v-clicks>

</div>

<!--
MCP 能实现很多有趣的场景。比如 AI 助手可以访问你的日历和笔记、从设计稿生成代码、连接企业数据库进行分析，甚至操作 Blender 创建 3D 设计。
-->

---
class: py-10
glowSeed: 300
---

## 为什么 MCP 很重要？

<div mt-8 />

<div grid grid-cols-3 gap-6>
  <div text-center>
    <div flex items-center justify-center mb-4>
      <div i-carbon:code text-5xl text-blue-400 />
    </div>
    <div font-bold mb-1>开发者</div>
    <div text-sm opacity-70>减少开发时间和复杂性</div>
    <div text-xs opacity-50 mt-2>标准化接口，避免重复集成</div>
  </div>
  <div text-center>
    <div flex items-center justify-center mb-4>
      <div i-carbon:bot text-5xl text-violet-400 />
    </div>
    <div font-bold mb-1>AI 应用</div>
    <div text-sm opacity-70>增强功能，改善用户体验</div>
    <div text-xs opacity-50 mt-2>访问数据源、工具和生态</div>
  </div>
  <div text-center>
    <div flex items-center justify-center mb-4>
      <div i-carbon:user text-5xl text-green-400 />
    </div>
    <div font-bold mb-1>最终用户</div>
    <div text-sm opacity-70>更强大的 AI 应用</div>
    <div text-xs opacity-50 mt-2>AI 能访问数据并代为执行任务</div>
  </div>
</div>

<!--
MCP 对不同角色都有价值。开发者减少了集成成本，AI 应用获得了更强的能力，最终用户得到了更智能的工具。
-->

---
class: py-10
glowSeed: 320
---

## 广泛的生态支持

<span>一次构建，随处集成</span>

<div mt-8 />

<div grid grid-cols-4 gap-5>
  <div text-center>
    <div flex items-center justify-center mb-3>
      <div i-simple-icons:anthropic text-4xl />
    </div>
    <div text-sm font-bold>Claude</div>
  </div>
  <div text-center>
    <div flex items-center justify-center mb-3>
      <div i-simple-icons:openai text-4xl />
    </div>
    <div text-sm font-bold>ChatGPT</div>
  </div>
  <div text-center>
    <div flex items-center justify-center mb-3>
      <div i-simple-icons:visualstudiocode text-4xl />
    </div>
    <div text-sm font-bold>VS Code</div>
  </div>
  <div text-center>
    <div flex items-center justify-center mb-3>
      <div i-simple-icons:cursor text-4xl />
    </div>
    <div text-sm font-bold>Cursor</div>
  </div>
  <div text-center>
    <div flex items-center justify-center mb-3>
      <div i-simple-icons:github text-4xl />
    </div>
    <div text-sm font-bold>GitHub</div>
  </div>
  <div text-center>
    <div flex items-center justify-center mb-3>
      <div i-simple-icons:google text-4xl />
    </div>
    <div text-sm font-bold>Google Drive</div>
  </div>
  <div text-center>
    <div flex items-center justify-center mb-3>
      <div i-simple-icons:slack text-4xl />
    </div>
    <div text-sm font-bold>Slack</div>
  </div>
  <div text-center>
    <div flex items-center justify-center mb-3>
      <div i-carbon:tools text-4xl />
    </div>
    <div text-sm font-bold>数百个工具...</div>
  </div>
</div>

<!--
MCP 得到了广泛支持。AI 客户端如 Claude、ChatGPT，开发工具如 VS Code、Cursor，以及 GitHub、Slack 等数百个工具都已支持 MCP。
-->

---
layout: section
glowSeed: 400
---

# 02

核心概念

<!--
第二章：深入 MCP 的三大核心概念——工具、资源和提示词
-->

---
class: py-10
glowSeed: 420
clicks: 3
glow: right
---

## MCP 三大核心原语

<span>服务器暴露的三个核心能力</span>

<div mt-6 />

<div flex items-center gap-8 translate-y-20>
  <div
    v-click="1"
    flex-1 transition duration-500 ease-in-out
    :class="$clicks < 1 ? 'opacity-0 translate-y-10' : 'opacity-100 translate-y-0'"
  >
    <div border="2 solid blue-800/50" rounded-lg>
      <div flex items-center bg="blue-800/30" px-3 py-2 text-blue-300>
        <div i-carbon:task-tools text-sm mr-1 />
        <div text-xs><em>工具 Tools</em></div>
      </div>
      <div bg="blue-800/10" px-4 py-3>
        <div text-sm>可执行函数</div>
        <div text-xs opacity-70 mt-1>文件操作、API 调用、数据库查询</div>
      </div>
    </div>
  </div>

  <div
    v-click="2"
    flex-1 transition duration-500 ease-in-out
    :class="$clicks < 2 ? 'opacity-0 translate-y-10' : 'opacity-100 translate-y-0'"
  >
    <div border="2 solid green-800/50" rounded-lg>
      <div flex items-center bg="green-800/30" px-3 py-2 text-green-300>
        <div i-carbon:data-base text-sm mr-1 />
        <div text-xs><em>资源 Resources</em></div>
      </div>
      <div bg="green-800/10" px-4 py-3>
        <div text-sm>数据源</div>
        <div text-xs opacity-70 mt-1>文件内容、数据库记录、日志</div>
      </div>
    </div>
  </div>

  <div
    v-click="3"
    flex-1 transition duration-500 ease-in-out
    :class="$clicks < 3 ? 'opacity-0 translate-y-10' : 'opacity-100 translate-y-0'"
  >
    <div border="2 solid violet-800/50" rounded-lg>
      <div flex items-center bg="violet-800/30" px-3 py-2 text-violet-300>
        <div i-carbon:text-creation text-sm mr-1 />
        <div text-xs><em>提示词 Prompts</em></div>
      </div>
      <div bg="violet-800/10" px-4 py-3>
        <div text-sm>可复用模板</div>
        <div text-xs opacity-70 mt-1>交互模板、工作流引导</div>
      </div>
    </div>
  </div>
</div>

<!--
MCP 定义了三个核心原语。工具是 AI 可以调用的函数，资源是提供上下文的数据源，提示词是可复用的交互模板。
-->

---
class: py-10
glowSeed: 440
---

## 工具 (Tools)

<span>AI 可调用的可执行函数</span>

<div mt-4 />

```javascript {1-8|10-16|all}{maxHeight:'350px'}
// 工具定义
{
  name: "calculate_sum",        // 唯一标识符
  description: "将两个数字相加", // 人类可读描述
  inputSchema: {                // 参数的 JSON Schema
    type: "object",
    properties: {
      a: { type: "number" },
      b: { type: "number" }
    },
    required: ["a", "b"]
  },
  annotations: {                // 行为提示（可选）
    readOnlyHint: true,         // 只读操作
    openWorldHint: false        // 不与外部交互
  }
}
```

<div mt-2 text-xs opacity-50>
工具通过 tools/list 发现，通过 tools/call 调用
</div>

<!--
工具是 MCP 中最重要的原语。每个工具有名字、描述、参数定义，以及可选的行为注释，帮助 AI 理解何时以及如何使用这个工具。
-->

---
class: py-10
glowSeed: 460
---

## 资源 (Resources)

<span>向客户端提供上下文信息的数据源</span>

<div mt-4 />

<div grid grid-cols-2 gap-6>
  <div>
    <div text-sm font-bold mb-3 text-green-300>资源类型</div>
    <div flex flex-col gap-2>
      <div flex items-center gap-2>
        <div i-carbon:document text-green-400 />
        <span text-sm>文件内容</span>
      </div>
      <div flex items-center gap-2>
        <div i-carbon:data-base text-green-400 />
        <span text-sm>数据库记录</span>
      </div>
      <div flex items-center gap-2>
        <div i-carbon:api text-green-400 />
        <span text-sm>API 响应</span>
      </div>
      <div flex items-center gap-2>
        <div i-carbon:screen text-green-400 />
        <span text-sm>截图和图像</span>
      </div>
      <div flex items-center gap-2>
        <div i-carbon:logs text-green-400 />
        <span text-sm>日志文件</span>
      </div>
    </div>
  </div>
  <div>
    <div text-sm font-bold mb-3 text-green-300>URI 格式示例</div>

```text
file:///home/user/report.pdf
postgres://db/customers/schema
screen://localhost/display1
```

  </div>
</div>

<!--
资源是提供上下文的数据源。它们通过 URI 标识，可以是文件、数据库记录、API 响应等各种形式。资源是只读的，用来给 AI 提供信息。
-->

---
class: py-10
glowSeed: 480
---

## 提示词 (Prompts)

<span>可重用的交互模板</span>

<div mt-4 />

```javascript {1-12|14-24|all}
// 提示词定义
{
  name: "git-commit",
  description: "生成 Git 提交消息",
  arguments: [
    {
      name: "changes",
      description: "Git diff 或更改描述",
      required: true
    }
  ]
}

// 提示词实现 - 返回消息模板
{
  messages: [{
    role: "user",
    content: {
      type: "text",
      text: `为这些更改生成提交消息：\n\n${arguments.changes}`
    }
  }]
}
```

<div mt-2 text-xs opacity-50>
提示词可接受动态参数，在 UI 中显示为斜杠命令或快捷操作
</div>

<!--
提示词是可重用的交互模板。它们可以接受动态参数，指导特定工作流，在客户端 UI 中可以显示为斜杠命令。
-->

---
class: py-10
glowSeed: 490
---

## 工具注释 (Annotations)

<span>帮助 AI 理解工具的行为特征</span>

<div mt-6 />

<div grid grid-cols-2 gap-4>

<div border="2 solid blue-800/50" rounded-lg overflow-hidden bg="blue-900/10">
  <div flex items-center bg="blue-800/30" px-3 py-2 text-blue-300>
    <div i-carbon:view text-sm mr-2 />
    <div font-semibold>readOnlyHint</div>
  </div>
  <div bg="blue-900/5" px-4 py-3>
    <div text-sm>工具是否只读取数据</div>
    <div text-xs opacity-70>不修改环境，安全调用</div>
  </div>
</div>

<div border="2 solid red-800/50" rounded-lg overflow-hidden bg="red-900/10">
  <div flex items-center bg="red-800/30" px-3 py-2 text-red-300>
    <div i-carbon:warning text-sm mr-2 />
    <div font-semibold>destructiveHint</div>
  </div>
  <div bg="red-900/5" px-4 py-3>
    <div text-sm>工具是否可能破坏数据</div>
    <div text-xs opacity-70>如删除文件、覆盖数据</div>
  </div>
</div>

<div border="2 solid green-800/50" rounded-lg overflow-hidden bg="green-900/10">
  <div flex items-center bg="green-800/30" px-3 py-2 text-green-300>
    <div i-carbon:repeat text-sm mr-2 />
    <div font-semibold>idempotentHint</div>
  </div>
  <div bg="green-900/5" px-4 py-3>
    <div text-sm>重复调用是否有额外效果</div>
    <div text-xs opacity-70>相同参数调用多次结果一致</div>
  </div>
</div>

<div border="2 solid amber-800/50" rounded-lg overflow-hidden bg="amber-900/10">
  <div flex items-center bg="amber-800/30" px-3 py-2 text-amber-300>
    <div i-carbon:earth text-sm mr-2 />
    <div font-semibold>openWorldHint</div>
  </div>
  <div bg="amber-900/5" px-4 py-3>
    <div text-sm>工具是否与外部实体交互</div>
    <div text-xs opacity-70>如网络搜索、API 调用</div>
  </div>
</div>

</div>

<!--
工具注释帮助 AI 理解工具的行为特征：是否只读、是否破坏性、是否幂等、是否与外部交互。这能让 AI 更安全地选择和使用工具。
-->

---
layout: section
glowSeed: 550
---

# 03

架构设计

<!--
第三章：了解 MCP 的架构设计，包括客户端-服务器模型和传输层
-->

---
class: py-10
glowSeed: 560
---

## 客户端-服务器架构

<span>MCP 遵循经典的 CS 架构</span>

<div mt-8 />

<div grid grid-cols-3 gap-6>
  <div text-center>
    <div flex items-center justify-center mb-4>
      <div i-carbon:application text-6xl text-blue-400 />
    </div>
    <div font-bold mb-1 text-blue-300>MCP Host</div>
    <div text-sm opacity-70>AI 应用程序</div>
    <div text-xs opacity-50 mt-2>协调和管理 MCP 客户端</div>
    <div text-xs opacity-50>如 VS Code、Claude</div>
  </div>
  <div text-center>
    <div flex items-center justify-center mb-4>
      <div i-carbon:connector text-6xl text-violet-400 />
    </div>
    <div font-bold mb-1 text-violet-300>MCP Client</div>
    <div text-sm opacity-70>连接维护者</div>
    <div text-xs opacity-50 mt-2>维护与 MCP 服务器的连接</div>
    <div text-xs opacity-50>从服务器获取上下文</div>
  </div>
  <div text-center>
    <div flex items-center justify-center mb-4>
      <div i-carbon:server text-6xl text-green-400 />
    </div>
    <div font-bold mb-1 text-green-300>MCP Server</div>
    <div text-sm opacity-70>能力提供者</div>
    <div text-xs opacity-50 mt-2>提供工具、资源、提示词</div>
    <div text-xs opacity-50>暴露核心原语给客户端</div>
  </div>
</div>

<!--
MCP 采用客户端-服务器架构。Host 是 AI 应用（比如 VS Code），它创建 Client 来连接不同的 Server，每个 Server 提供不同的能力。
-->

---
class: py-10
glowSeed: 580
clicks: 2
---

## 传输层：两种通信方式

<span>根据场景选择合适的传输机制</span>

<div mt-8 />

<div grid grid-cols-2 gap-8>
  <div
    v-click="1"
    transition duration-500 ease-in-out
    :class="$clicks < 1 ? 'opacity-0' : 'opacity-100'"
    class="border-2 border-blue-500/30 rounded-lg p-5 bg-blue-500/10"
  >
    <div text-xl font-bold mb-3 text-blue-300>Stdio 传输</div>
    <div text-sm mb-3>同一机器上的本地进程通信</div>
    <div flex flex-col gap-2 text-xs>
      <div flex items-center gap-2>
        <div i-carbon:checkmark text-green-400 />
        <span>最佳性能，无网络开销</span>
      </div>
      <div flex items-center gap-2>
        <div i-carbon:checkmark text-green-400 />
        <span>标准输入/输出流</span>
      </div>
      <div flex items-center gap-2>
        <div i-carbon:checkmark text-green-400 />
        <span>适合本地工具集成</span>
      </div>
    </div>
  </div>
  <div
    v-click="2"
    transition duration-500 ease-in-out
    :class="$clicks < 2 ? 'opacity-0' : 'opacity-100'"
    class="border-2 border-violet-500/30 rounded-lg p-5 bg-violet-500/10"
  >
    <div text-xl font-bold mb-3 text-violet-300>Streamable HTTP</div>
    <div text-sm mb-3>远程通信，支持流式传输</div>
    <div flex flex-col gap-2 text-xs>
      <div flex items-center gap-2>
        <div i-carbon:checkmark text-green-400 />
        <span>HTTP POST + SSE 流式</span>
      </div>
      <div flex items-center gap-2>
        <div i-carbon:checkmark text-green-400 />
        <span>支持 OAuth 等认证方式</span>
      </div>
      <div flex items-center gap-2>
        <div i-carbon:checkmark text-green-400 />
        <span>适合远程服务和云集成</span>
      </div>
    </div>
  </div>
</div>

<!--
MCP 支持两种传输方式。Stdio 适合本地进程通信，性能最好；Streamable HTTP 适合远程通信，支持流式和认证。
-->

---
class: py-10
glowSeed: 590
clicks: 3
---

## 连接生命周期

<span>从初始化到终止的完整流程</span>

<div mt-8 />

<div flex items-center gap-4>

<v-clicks>

<div
  rounded-lg
  border="2 solid blue-900" bg="blue-900/20"
  backdrop-blur
  flex-1
  transition duration-500 ease-in-out
>
  <div px-5 py-10 flex items-center justify-center>
    <div i-solar:hand-shake-bold-duotone size-16 />
  </div>
  <div bg="blue-900/30" w-full px-4 py-2 flex items-center justify-center text-center>
    <span>初始化</span>
  </div>
</div>

<div
  rounded-lg
  border="2 solid violet-800" bg="violet-800/20"
  backdrop-blur
  flex-1
  transition duration-500 ease-in-out
>
  <div px-5 py-10 flex items-center justify-center>
    <div i-solar:chat-round-dots-bold-duotone size-16 />
  </div>
  <div bg="violet-800/30" w-full px-4 py-2 flex items-center justify-center text-center>
    <span>消息交换</span>
  </div>
</div>

<div
  rounded-lg
  border="2 solid green-800" bg="green-800/20"
  backdrop-blur
  flex-1
  transition duration-500 ease-in-out
>
  <div px-5 py-10 flex items-center justify-center>
    <div i-solar:close-circle-bold-duotone size-16 />
  </div>
  <div bg="green-800/30" w-full px-4 py-2 flex items-center justify-center text-center>
    <span>终止</span>
  </div>
</div>

</v-clicks>

</div>

<div mt-6 text-xs opacity-50>
初始化：客户端发送协议版本和能力 → 服务器响应 → 确认后开始通信
</div>

<!--
MCP 的连接分为三个阶段：初始化时交换协议版本和能力，然后进入消息交换阶段（支持请求-响应和通知两种模式），最后任一方都可以终止连接。
-->

---
layout: section
glowSeed: 650
---

# 04

开发指南

<!--
第四章：动手实践，看看如何构建一个 MCP 服务器
-->

---
class: py-10
glowSeed: 660
---

## 构建 MCP 服务器

<span>从零开始实现一个服务器</span>

<div mt-4 />

```javascript {1-5|7-17|19-22|all}{maxHeight:'350px'}
// 1. 创建服务器实例
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server({
  name: "example-server",
  version: "1.0.0"
}, {
  capabilities: {
    resources: {},
    tools: {},
    prompts: {}
  }
});

// 2. 连接传输层
const transport = new StdioServerTransport();
await server.connect(transport);
```

<!--
创建一个 MCP 服务器非常简单。首先创建 Server 实例并声明能力，然后连接传输层。这里展示了使用 Stdio 传输的最基本结构。
-->

---
class: py-10
glowSeed: 670
---

## 实现资源支持

<span>让 AI 能读取你的数据</span>

<div mt-4 />

```javascript {1-10|12-22|all}{maxHeight:'350px'}
// 列出可用资源
server.setRequestHandler(ListResourcesRequestSchema, async () => {
  return {
    resources: [{
      uri: "file:///logs/app.log",
      name: "应用程序日志",
      mimeType: "text/plain"
    }]
  };
});

// 读取资源内容
server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
  const uri = request.params.uri;
  if (uri === "file:///logs/app.log") {
    const logContents = await readLogFile();
    return { contents: [{ uri, mimeType: "text/plain", text: logContents }] };
  }
  throw new Error("未找到资源");
});
```

<!--
实现资源支持需要两个处理器：一个列出可用资源，一个根据 URI 读取具体内容。这样就完成了资源的发现和获取。
-->

---
class: py-10
glowSeed: 680
---

## 实现工具支持

<span>让 AI 能执行操作</span>

<div mt-4 />

```javascript {1-14|16-26|all}{maxHeight:'350px'}
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
    return { content: [{ type: "text", text: String(a + b) }] };
  }
  throw new Error("未找到工具");
});
```

<!--
工具实现也是两个处理器：ListTools 声明工具及其参数，CallTool 处理实际的执行逻辑。可以看到 MCP 的设计模式非常一致。
-->

---
class: py-10
glowSeed: 685
---

## 实现提示词支持

<span>创建可复用的交互模板</span>

<div mt-4 />

```javascript {1-15|17-27|all}{maxHeight:'350px'}
// 定义提示词
const PROMPTS = {
  "git-commit": {
    name: "git-commit",
    description: "生成 Git 提交消息",
    arguments: [{
      name: "changes",
      description: "Git diff 或更改描述",
      required: true
    }]
  }
};

// 获取提示词模板
server.setRequestHandler(GetPromptRequestSchema, async (request) => {
  if (request.params.name === "git-commit") {
    return {
      messages: [{
        role: "user",
        content: {
          type: "text",
          text: `为这些更改生成提交消息：\n\n${request.params.arguments?.changes}`
        }
      }]
    };
  }
});
```

<!--
提示词的实现也遵循相同的模式。定义提示词的名称、描述和参数，然后根据参数动态生成消息模板。
-->

---
layout: section
glowSeed: 720
---

# 05

最佳实践

<!--
第五章：开发 MCP 时需要注意的最佳实践，特别是安全方面
-->

---
class: py-10
glowSeed: 730
clicks: 4
---

## 安全考虑

<span>MCP 的安全需要在多个层面保障</span>

<div mt-6 />

<div grid grid-cols-2 gap-3>

<v-clicks>

<div border="2 solid red-800/50" rounded-lg overflow-hidden bg="red-900/10" backdrop-blur-sm>
  <div flex items-center bg="red-800/30" px-3 py-2 text-red-300>
    <div i-carbon:security text-sm mr-2 />
    <div font-semibold>传输安全</div>
  </div>
  <div bg="red-900/5" px-4 py-3>
    <div text-sm>远程连接使用 TLS</div>
    <div text-xs opacity-70>验证连接来源，实现身份验证</div>
  </div>
</div>

<div border="2 solid amber-800/50" rounded-lg overflow-hidden bg="amber-900/10" backdrop-blur-sm>
  <div flex items-center bg="amber-800/30" px-3 py-2 text-amber-300>
    <div i-carbon:validate text-sm mr-2 />
    <div font-semibold>消息验证</div>
  </div>
  <div bg="amber-900/5" px-4 py-3>
    <div text-sm>验证所有传入消息</div>
    <div text-xs opacity-70>清理输入，检查大小限制</div>
  </div>
</div>

<div border="2 solid blue-800/50" rounded-lg overflow-hidden bg="blue-900/10" backdrop-blur-sm>
  <div flex items-center bg="blue-800/30" px-3 py-2 text-blue-300>
    <div i-carbon:locked text-sm mr-2 />
    <div font-semibold>资源保护</div>
  </div>
  <div bg="blue-900/5" px-4 py-3>
    <div text-sm>实现访问控制</div>
    <div text-xs opacity-70>验证路径，速率限制</div>
  </div>
</div>

<div border="2 solid green-800/50" rounded-lg overflow-hidden bg="green-900/10" backdrop-blur-sm>
  <div flex items-center bg="green-800/30" px-3 py-2 text-green-300>
    <div i-carbon:debug text-sm mr-2 />
    <div font-semibold>错误处理</div>
  </div>
  <div bg="green-900/5" px-4 py-3>
    <div text-sm>不泄露敏感信息</div>
    <div text-xs opacity-70>记录安全错误，适当清理</div>
  </div>
</div>

</v-clicks>

</div>

<!--
安全是 MCP 开发中的重中之重。从传输层的加密，到消息的验证，再到资源的保护和错误处理，每个层面都需要考虑。
-->

---
class: py-10
glowSeed: 740
---

## 开发最佳实践

<span>构建高质量 MCP 服务器的关键</span>

<div mt-6 />

<div grid grid-cols-3 gap-4>
  <div border="2 solid violet-800/50" rounded-lg bg="violet-900/10" px-4 py-3>
    <div font-bold mb-2 text-violet-300 text-sm>工具设计</div>
    <div text-xs leading-5>
      提供清晰的名称和描述<br/>
      详细的 JSON Schema 定义<br/>
      操作保持原子化和聚焦<br/>
      实现适当的超时处理
    </div>
  </div>
  <div border="2 solid blue-800/50" rounded-lg bg="blue-900/10" px-4 py-3>
    <div font-bold mb-2 text-blue-300 text-sm>消息处理</div>
    <div text-xs leading-5>
      彻底验证输入参数<br/>
      使用类型安全的模式<br/>
      对长操作报告进度<br/>
      实现优雅的错误处理
    </div>
  </div>
  <div border="2 solid green-800/50" rounded-lg bg="green-900/10" px-4 py-3>
    <div font-bold mb-2 text-green-300 text-sm>调试监控</div>
    <div text-xs leading-5>
      记录协议事件和消息流<br/>
      实现健康检查端点<br/>
      监控连接状态和性能<br/>
      测试不同的传输方式
    </div>
  </div>
</div>

<!--
开发高质量 MCP 服务器的关键点：工具设计要清晰原子，消息处理要安全可靠，调试监控要全面覆盖。
-->

---
class: py-10
glowSeed: 750
---

## MCP 生态系统

<span>丰富的客户端、服务器和开发工具</span>

<div mt-6 />

<div grid grid-cols-3 gap-4>
  <div border="2 solid blue-800/50" rounded-lg overflow-hidden bg="blue-900/10">
    <div flex items-center bg="blue-800/30" px-3 py-2 text-blue-300>
      <div i-carbon:application text-sm mr-2 />
      <div font-semibold>AI 客户端</div>
    </div>
    <div bg="blue-900/5" px-4 py-3>
      <div text-sm>Claude / ChatGPT</div>
      <div text-xs opacity-70 mt-1>VS Code / Cursor</div>
      <div text-xs opacity-50 mt-1>MCPJam / 更多...</div>
    </div>
  </div>

  <div border="2 solid green-800/50" rounded-lg overflow-hidden bg="green-900/10">
    <div flex items-center bg="green-800/30" px-3 py-2 text-green-300>
      <div i-carbon:plug text-sm mr-2 />
      <div font-semibold>预构建服务器</div>
    </div>
    <div bg="green-900/5" px-4 py-3>
      <div text-sm>GitHub / Google Drive</div>
      <div text-xs opacity-70 mt-1>Slack / 数据库</div>
      <div text-xs opacity-50 mt-1>数百个其他工具</div>
    </div>
  </div>

  <div border="2 solid violet-800/50" rounded-lg overflow-hidden bg="violet-900/10">
    <div flex items-center bg="violet-800/30" px-3 py-2 text-violet-300>
      <div i-carbon:tool-kit text-sm mr-2 />
      <div font-semibold>开发资源</div>
    </div>
    <div bg="violet-900/5" px-4 py-3>
      <div text-sm>MCP 规范文档</div>
      <div text-xs opacity-70 mt-1>多语言 SDK</div>
      <div text-xs opacity-50 mt-1>MCP Inspector 调试工具</div>
    </div>
  </div>
</div>

<!--
MCP 拥有丰富的生态系统。AI 客户端已经广泛支持，预构建的服务器覆盖了主流工具，还有完善的开发工具链。
-->

---
class: py-10
glowSeed: 760
---

## 工具错误处理

<span>优雅地处理错误，提升健壮性</span>

<div mt-4 />

```javascript {1-9|11-19|all}
try {
  // 工具操作
  const result = performOperation();
  return {
    content: [{
      type: "text",
      text: `操作成功：${result}`
    }]
  };
} catch (error) {
  return {
    isError: true,
    content: [{
      type: "text",
      text: `错误：${error.message}`
    }]
  };
}
```

<div mt-4 text-xs opacity-50>
标准错误代码：ParseError(-32700) / InvalidRequest(-32600) / MethodNotFound(-32601) / InvalidParams(-32602)
</div>

<!--
工具的错误处理非常重要。通过 isError 标记错误响应，提供清晰的错误消息，同时遵循标准的 JSON-RPC 错误代码。
-->

---
class: py-10
glowSeed: 770
---

## 资源更新机制

<span>支持实时的数据推送</span>

<div mt-6 />

<div grid grid-cols-2 gap-6>
  <div>
    <div text-sm font-bold mb-3 text-green-300>列表变更</div>
    <div text-sm opacity-80>服务器通过通知告知客户端资源列表变化</div>

```javascript
// 服务器发送通知
notifications/resources/list_changed
```

  </div>
  <div>
    <div text-sm font-bold mb-3 text-blue-300>内容订阅</div>
    <div text-sm opacity-80>客户端订阅特定资源的实时更新</div>

```javascript
// 订阅流程
1. resources/subscribe (uri)
2. notifications/resources/updated
3. resources/read (获取最新)
4. resources/unsubscribe (取消)
```

  </div>
</div>

<!--
MCP 支持两种资源更新机制：列表变更通知和内容订阅。这使得客户端可以实时获取最新的数据。
-->

---
class: flex justify-center items-center gap-20 px-40 text-xl
glowSeed: 800
---

<div
  absolute text-5xl
  :class="$clicks < 1 ? 'text-white' : 'translate-y--18 scale-40 text-white/30'"
  transition duration-500 ease-in-out
>
  <span>MCP 的未来？</span>
</div>

<div flex flex-col items-center>
  <v-clicks>
    <div mt-4>
      <h1 flex items-center text="5xl!">
        <span>一次构建，随处集成</span>
      </h1>
    </div>
  </v-clicks>
</div>

<!--
过渡页：MCP 的未来是什么？答案就是"一次构建，随处集成"。
-->

---
class: py-10
glowSeed: 820
---

## 总结

<span>MCP 核心要点回顾</span>

<div mt-6 />

<div grid grid-cols-3 gap-4>

<div border="2 solid blue-800/50" rounded-lg bg="blue-900/10" px-4 py-3>
  <div font-bold mb-2 text-blue-300 text-sm>三大原语</div>
  <div text-xs leading-5>
    工具 — 可执行函数<br/>
    资源 — 上下文数据<br/>
    提示词 — 交互模板
  </div>
</div>

<div border="2 solid green-800/50" rounded-lg bg="green-900/10" px-4 py-3>
  <div font-bold mb-2 text-green-300 text-sm>灵活架构</div>
  <div text-xs leading-5>
    Stdio 本地通信<br/>
    HTTP 远程通信<br/>
    客户端-服务器模型
  </div>
</div>

<div border="2 solid violet-800/50" rounded-lg bg="violet-900/10" px-4 py-3>
  <div font-bold mb-2 text-violet-300 text-sm>丰富生态</div>
  <div text-xs leading-5>
    多语言 SDK<br/>
    预构建服务器<br/>
    广泛客户端支持
  </div>
</div>

</div>

<div mt-6 />

<div border="2 solid amber-800/50" rounded-lg bg="amber-900/10" px-4 py-3>
  <div font-bold mb-2 text-amber-300 text-sm>开发友好</div>
  <div text-xs leading-5>
    统一的设计模式（List + Handle） · 完善的安全考虑 · MCP Inspector 调试工具 · 热重载开发体验
  </div>
</div>

<!--
最后来总结一下。MCP 提供了三大核心原语，灵活的双传输架构，丰富的生态系统，以及对开发者友好的工具链。
-->

---
layout: end
glowSeed: 900
---

感谢聆听

<div class="text-sm opacity-50 mt-4">
  Model Context Protocol — AI 连接世界的标准化接口
</div>

<div class="text-sm opacity-30 mt-4">
  Powered by Slidev + Glow Theme
</div>

<!--
感谢大家的聆听！MCP 正在改变 AI 应用与外部世界交互的方式，希望大家今天对 MCP 有了全面的理解。
-->
