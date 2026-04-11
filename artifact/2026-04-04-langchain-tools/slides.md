---
layout: center
highlighter: shiki
css: unocss
colorSchema: dark
transition: fade-out
title: LangChain Tools 完全指南
exportFilename: langchain-tools-guide
lineNumbers: false
drawings:
  persist: false
mdc: true
clicks: 0
preload: false
glowSeed: 150
routerMode: hash
fonts:
  sans: 'DM Sans'
  mono: 'Fira Code'
---

<div flex flex-col items-center>
  <div text-7xl font-bold mb-6>
    LangChain Tools
  </div>
  <div text-2xl class="text-white/60" mb-10>
    完全指南 — 从基础到高级
  </div>
  <div flex items-center gap-3 mt-4>
    <div i-logos:python text-3xl />
    <div i-logos:langchain-icon text-3xl />
  </div>
</div>

---
layout: section
glowSeed: 200
---

# 什么是 Tools?

---
class: py-10
clicks: 3
glowSeed: 250
---

## Tools: Agent 的能力扩展

<div flex items-center gap-10 translate-y-8>
  <div
    v-click="1"
    flex-1 transition duration-500 ease-in-out
    :class="$clicks < 1 ? 'opacity-0 translate-y-10' : 'opacity-100 translate-y-0'"
  >
    <div border="2 solid violet-800/50" rounded-lg>
      <div flex items-center bg="violet-800/30" px-3 py-2 text-violet-300>
        <div i-carbon:fetch-data text-sm mr-1 />
        <div text-xs><em>实时数据</em></div>
      </div>
      <div bg="violet-800/10" px-4 py-3 text-sm>
        获取 API 数据、搜索网页、查询数据库
      </div>
    </div>
  </div>
  <div
    v-click="2"
    flex-1 transition duration-500 ease-in-out
    :class="$clicks < 2 ? 'opacity-0 translate-y-10' : 'opacity-100 translate-y-0'"
  >
    <div border="2 solid blue-800/50" rounded-lg>
      <div flex items-center bg="blue-800/30" px-3 py-2 text-blue-300>
        <div i-carbon:code text-sm mr-1 />
        <div text-xs><em>执行代码</em></div>
      </div>
      <div bg="blue-800/10" px-4 py-3 text-sm>
        运行 Python、Shell 脚本、计算任务
      </div>
    </div>
  </div>
  <div
    v-click="3"
    flex-1 transition duration-500 ease-in-out
    :class="$clicks < 3 ? 'opacity-0 translate-y-10' : 'opacity-100 translate-y-0'"
  >
    <div border="2 solid green-800/50" rounded-lg>
      <div flex items-center bg="green-800/30" px-3 py-2 text-green-300>
        <div i-carbon:action text-sm mr-1 />
        <div text-xs><em>与世界交互</em></div>
      </div>
      <div bg="green-800/10" px-4 py-3 text-sm>
        发送邮件、操作文件、调用外部服务
      </div>
    </div>
  </div>
</div>

<div v-click="3" mt-20 text-sm class="text-white/50">
  Tool 是带有明确定义输入输出的可调用函数，传递给 Chat Model，由模型决定何时调用
</div>

---
class: py-10
clicks: 2
glowSeed: 300
---

## 工作原理

<div flex items-center justify-center gap-6 mt-8>
  <div
    v-click="1"
    transition duration-500 ease-in-out
    :class="$clicks < 1 ? 'opacity-0 scale-95' : 'opacity-100 scale-100'"
  >
    <div text-center>
      <div flex items-center justify-center mb-3>
        <div i-carbon:user text-5xl text-violet-400 />
      </div>
      <div text-sm font-bold>用户输入</div>
    </div>
  </div>
  <div v-click="1" text-2xl class="text-white/30" transition duration-500>→</div>
  <div
    v-click="1"
    transition duration-500 ease-in-out
    :class="$clicks < 1 ? 'opacity-0 scale-95' : 'opacity-100 scale-100'"
  >
    <div text-center>
      <div flex items-center justify-center mb-3>
        <div i-carbon:machine-learning-model text-5xl text-blue-400 />
      </div>
      <div text-sm font-bold>LLM 决策</div>
    </div>
  </div>
  <div v-click="1" text-2xl class="text-white/30" transition duration-500>→</div>
  <div
    v-click="1"
    transition duration-500 ease-in-out
    :class="$clicks < 1 ? 'opacity-0 scale-95' : 'opacity-100 scale-100'"
  >
    <div text-center>
      <div flex items-center justify-center mb-3>
        <div i-carbon:tool-kit text-5xl text-green-400 />
      </div>
      <div text-sm font-bold>Tool 执行</div>
    </div>
  </div>
  <div v-click="1" text-2xl class="text-white/30" transition duration-500>→</div>
  <div
    v-click="1"
    transition duration-500 ease-in-out
    :class="$clicks < 1 ? 'opacity-0 scale-95' : 'opacity-100 scale-100'"
  >
    <div text-center>
      <div flex items-center justify-center mb-3>
        <div i-carbon:chat text-5xl text-amber-400 />
      </div>
      <div text-sm font-bold>返回结果</div>
    </div>
  </div>
</div>

<div v-click="2" mt-10 text-sm class="text-white/50" text-center>
  模型根据对话上下文决定是否调用工具、调用哪个工具、传入什么参数
</div>

---
layout: section
glowSeed: 350
---

# 基础用法

---
class: py-8
glowSeed: 400
---

## 使用 @tool 装饰器创建工具

<div grid grid-cols-2 gap-6>
  <div>
    <div text-sm class="text-white/50" mb-4>函数的 <span text-amber-300>docstring</span> 成为工具描述</div>
    <div text-sm class="text-white/50" mb-2><span text-amber-300>类型提示</span> 是必需的，定义输入 schema</div>
```python
from langchain.tools import tool

@tool
def search_database(
    query: str,
    limit: int = 10
) -> str:
    """Search the customer database
    for records matching the query.

    Args:
        query: Search terms
        limit: Max results to return
    """
    return f"Found {limit} results"
```
  </div>
  <div>
    <div border="2 solid cyan-800/50" rounded-lg mt-6>
      <div flex items-center bg="cyan-800/30" px-3 py-2 text-cyan-300>
        <div i-carbon:information text-sm mr-1 />
        <div text-xs><em>关键要点</em></div>
      </div>
      <div bg="cyan-800/10" px-4 py-3 text-sm>
        <div mb-3>
          <span text-cyan-300 font-bold>docstring</span> — 帮助模型理解何时使用该工具
        </div>
        <div mb-3>
          <span text-cyan-300 font-bold>类型提示</span> — 自动生成 JSON Schema
        </div>
        <div>
          <span text-cyan-300 font-bold>返回值</span> — str / dict / Command
        </div>
      </div>
    </div>
  </div>
</div>

---
class: py-8
glowSeed: 450
---

## 自定义 Tool 属性

<div grid grid-cols-2 gap-8>
  <div>
    <div text-sm class="text-white/50" mb-3>自定义工具名称</div>
```python
@tool("web_search")  # 自定义名称
def search(query: str) -> str:
    """Search the web."""
    return f"Results for: {query}"

print(search.name)  # "web_search"
```
    <div text-sm class="text-white/50" mt-4>自定义工具描述</div>
```python
@tool(
    "calculator",
    description=(
      "Performs arithmetic. "
      "Use for math problems."
    )
)
def calc(expr: str) -> str:
    """Evaluate math expressions."""
    return str(eval(expr))
```
  </div>
  <div>
    <div border="2 solid purple-800/50" rounded-lg mt-2>
      <div flex items-center bg="purple-800/30" px-3 py-2 text-purple-300>
        <div i-carbon:settings-adjust text-sm mr-1 />
        <div text-xs><em>何时自定义</em></div>
      </div>
      <div bg="purple-800/10" px-4 py-3 text-sm>
        <div mb-2>函数名不够描述性 → <span text-purple-300>自定义 name</span></div>
        <div mb-2>需要更精确的模型引导 → <span text-purple-300>自定义 description</span></div>
        <div>默认 docstring 已经足够 → <span class="text-white/50">无需自定义</span></div>
      </div>
    </div>
    <div border="2 solid amber-800/50" rounded-lg mt-4>
      <div flex items-center bg="amber-800/30" px-3 py-2 text-amber-300>
        <div i-carbon:warning text-sm mr-1 />
        <div text-xs><em>保留参数名</em></div>
      </div>
      <div bg="amber-800/10" px-4 py-3 text-sm>
        <div><span text-amber-300 font-bold>config</span> — RunnableConfig</div>
        <div><span text-amber-300 font-bold>runtime</span> — ToolRuntime</div>
        <div mt-1 class="text-white/50">这两个名称不能作为工具参数</div>
      </div>
    </div>
  </div>
</div>

---
layout: section
glowSeed: 500
---

# 访问上下文

---
class: py-10
clicks: 6
glowSeed: 550
---

## ToolRuntime 组件概览

<div grid grid-cols-3 gap-4 pt-6>
<v-clicks>

  <div border="2 solid violet-800/50" rounded-lg>
    <div flex items-center bg="violet-800/30" px-3 py-2 text-violet-300>
      <div i-carbon:data-base text-sm mr-1 />
      <div text-xs><em>State</em></div>
    </div>
    <div bg="violet-800/10" px-3 py-2 text-xs>
      短期记忆 — 消息历史、自定义字段
    </div>
  </div>

  <div border="2 solid blue-800/50" rounded-lg>
    <div flex items-center bg="blue-800/30" px-3 py-2 text-blue-300>
      <div i-carbon:user-avatar text-sm mr-1 />
      <div text-xs><em>Context</em></div>
    </div>
    <div bg="blue-800/10" px-3 py-2 text-xs>
      不可变配置 — 用户 ID、会话信息
    </div>
  </div>

  <div border="2 solid green-800/50" rounded-lg>
    <div flex items-center bg="green-800/30" px-3 py-2 text-green-300>
      <div i-carbon:save text-sm mr-1 />
      <div text-xs><em>Store</em></div>
    </div>
    <div bg="green-800/10" px-3 py-2 text-xs>
      长期记忆 — 跨会话持久数据
    </div>
  </div>

  <div border="2 solid cyan-800/50" rounded-lg>
    <div flex items-center bg="cyan-800/30" px-3 py-2 text-cyan-300>
      <div i-carbon:stream text-sm mr-1 />
      <div text-xs><em>Stream Writer</em></div>
    </div>
    <div bg="cyan-800/10" px-3 py-2 text-xs>
      实时更新 — 执行中发送进度
    </div>
  </div>

  <div border="2 solid amber-800/50" rounded-lg>
    <div flex items-center bg="amber-800/30" px-3 py-2 text-amber-300>
      <div i-carbon:settings text-sm mr-1 />
      <div text-xs><em>Config</em></div>
    </div>
    <div bg="amber-800/10" px-3 py-2 text-xs>
      RunnableConfig — 回调、标签
    </div>
  </div>

  <div border="2 solid rose-800/50" rounded-lg>
    <div flex items-center bg="rose-800/30" px-3 py-2 text-rose-300>
      <div i-carbon:identification text-sm mr-1 />
      <div text-xs><em>Tool Call ID</em></div>
    </div>
    <div bg="rose-800/10" px-3 py-2 text-xs>
      唯一标识 — 日志关联
    </div>
  </div>

</v-clicks>
</div>

---
class: py-8
glowSeed: 600
---

## 短期记忆 (State) 与 Context

<div grid grid-cols-2 gap-8>
  <div>
    <div text-violet-300 font-bold mb-2>State — 可变数据</div>
```python
from langchain.tools import tool, ToolRuntime
from langchain.messages import HumanMessage

@tool
def get_last_user_message(
    runtime: ToolRuntime,
) -> str:
    """Get the most recent user msg."""
    messages = runtime.state["messages"]
    for msg in reversed(messages):
        if isinstance(msg, HumanMessage):
            return msg.content
    return "No user messages found"
```
```python
# 使用 Command 更新状态
from langgraph.types import Command

@tool
def set_user_name(new_name: str) -> Command:
    """Set the user's name."""
    return Command(update={"user_name": new_name})
```
  </div>
  <div>
    <div text-blue-300 font-bold mb-2>Context — 不可变配置</div>
```python
from dataclasses import dataclass

@dataclass
class UserContext:
    user_id: str

@tool
def get_account_info(
    runtime: ToolRuntime[UserContext],
) -> str:
    """Get current user's account."""
    user_id = runtime.context.user_id
    # 查询用户信息...
    return f"Account for {user_id}"

# 创建 Agent 时传入 context
agent = create_agent(
    model,
    tools=[get_account_info],
    context_schema=UserContext,
)
```
  </div>
</div>

---
class: py-8
glowSeed: 650
---

## 长期记忆 (Store) 与 Stream Writer

<div grid grid-cols-2 gap-8>
  <div>
    <div text-green-300 font-bold mb-2>Store — 跨会话持久存储</div>
```python
from langgraph.store.memory import InMemoryStore

@tool
def save_user_info(
    user_id: str,
    info: dict,
    runtime: ToolRuntime,
) -> str:
    """Save user info persistently."""
    store = runtime.store
    store.put(("users",), user_id, info)
    return "Saved!"

@tool
def get_user_info(
    user_id: str,
    runtime: ToolRuntime,
) -> str:
    """Look up saved user info."""
    store = runtime.store
    result = store.get(("users",), user_id)
    return str(result.value) if result else "Unknown"
```
  </div>
  <div>
    <div text-cyan-300 font-bold mb-2>Stream Writer — 实时更新</div>
```python
@tool
def get_weather(
    city: str,
    runtime: ToolRuntime,
) -> str:
    """Get weather for a city."""
    writer = runtime.stream_writer

    # 执行中发送进度更新
    writer(f"Looking up data for {city}")
    writer(f"Acquired data for {city}")

    return f"It's sunny in {city}!"
```
    <div border="2 solid cyan-800/50" rounded-lg mt-3>
      <div bg="cyan-800/10" px-3 py-2 text-xs>
        Store 使用 <span text-cyan-300>namespace/key</span> 模式组织数据，支持跨会话持久化
      </div>
    </div>
  </div>
</div>

---
layout: section
glowSeed: 700
---

# ToolNode 与工作流

---
class: py-8
glowSeed: 750
---

## ToolNode: LangGraph 工作流集成

<div grid grid-cols-2 gap-8>
  <div>
    <div text-sm class="text-white/50" mb-3>预构建节点，自动处理工具执行</div>
```python
from langchain.tools import tool
from langgraph.prebuilt import ToolNode
from langgraph.graph import StateGraph, MessagesState

@tool
def search(query: str) -> str:
    """Search for information."""
    return f"Results for: {query}"

@tool
def calculator(expr: str) -> str:
    """Evaluate math expression."""
    return str(eval(expr))

tool_node = ToolNode([search, calculator])

# 在图中使用
builder = StateGraph(MessagesState)
builder.add_node("tools", tool_node)
```
  </div>
  <div>
    <div border="2 solid violet-800/50" rounded-lg mb-4>
      <div flex items-center bg="violet-800/30" px-3 py-2 text-violet-300>
        <div i-carbon:checkmark-outline text-sm mr-1 />
        <div text-xs><em>自动处理</em></div>
      </div>
      <div bg="violet-800/10" px-4 py-3 text-sm>
        <div mb-2>并行工具调用执行</div>
        <div mb-2>错误捕获与处理</div>
        <div mb-2>状态注入 (ToolRuntime)</div>
        <div>消息格式转换</div>
      </div>
    </div>
    <div border="2 solid amber-800/50" rounded-lg>
      <div flex items-center bg="amber-800/30" px-3 py-2 text-amber-300>
        <div i-carbon:flow text-sm mr-1 />
        <div text-xs><em>路由: tools_condition</em></div>
      </div>
      <div bg="amber-800/10" px-4 py-3 text-sm>
        基于 LLM 是否发起工具调用进行条件路由
      </div>
    </div>
  </div>
</div>

---
class: py-8
glowSeed: 800
---

## 路由与完整工作流

```python{1-3|5-8|10-12|all}{maxHeight:'300px'}
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph import StateGraph, MessagesState, START, END

# 构建图
builder = StateGraph(MessagesState)
builder.add_node("llm", call_llm)
builder.add_node("tools", ToolNode(tools))

# 添加边
builder.add_edge(START, "llm")
builder.add_conditional_edges("llm", tools_condition)  # → "tools" 或 END
builder.add_edge("tools", "llm")  # 工具结果返回 LLM

graph = builder.compile()
```

<div grid grid-cols-4 gap-4 mt-4>
  <div text-center>
    <div i-carbon:user text-3xl text-violet-400 mx-auto mb-1 />
    <div text-xs>START</div>
  </div>
  <div text-center>
    <div i-carbon:machine-learning-model text-3xl text-blue-400 mx-auto mb-1 />
    <div text-xs>LLM</div>
    <div text-xs class="text-white/40">需要工具?</div>
  </div>
  <div text-center>
    <div i-carbon:tool-kit text-3xl text-green-400 mx-auto mb-1 />
    <div text-xs>ToolNode</div>
  </div>
  <div text-center>
    <div i-carbon:checkmark text-3xl text-amber-400 mx-auto mb-1 />
    <div text-xs>END</div>
  </div>
</div>

---
layout: section
glowSeed: 850
---

# 返回值与错误处理

---
class: py-8
clicks: 3
glowSeed: 900
---

## Tool 返回值

<div grid grid-cols-3 gap-6>
  <div
    v-click="1"
    transition duration-500 ease-in-out
    :class="$clicks < 1 ? 'opacity-0 translate-y-10' : 'opacity-100 translate-y-0'"
  >
    <div border="2 solid violet-800/50" rounded-lg h-full>
      <div flex items-center bg="violet-800/30" px-3 py-2 text-violet-300>
        <div i-carbon:text-link text-sm mr-1 />
        <div text-xs><em>返回字符串</em></div>
      </div>
      <div bg="violet-800/10" px-3 py-3 text-xs>
        <div mb-2>人类可读的文本结果</div>
```python
@tool
def get_weather(city: str) -> str:
    """Get weather."""
    return f"Sunny in {city}"
```
        <div mt-2 class="text-white/50">→ ToolMessage</div>
      </div>
    </div>
  </div>
  <div
    v-click="2"
    transition duration-500 ease-in-out
    :class="$clicks < 2 ? 'opacity-0 translate-y-10' : 'opacity-100 translate-y-0'"
  >
    <div border="2 solid blue-800/50" rounded-lg h-full>
      <div flex items-center bg="blue-800/30" px-3 py-2 text-blue-300>
        <div i-carbon:data-structured text-sm mr-1 />
        <div text-xs><em>返回对象</em></div>
      </div>
      <div bg="blue-800/10" px-3 py-3 text-xs>
        <div mb-2>结构化数据供模型推理</div>
```python
@tool
def get_weather_data(
    city: str,
) -> dict:
    """Get structured data."""
    return {
      "city": city,
      "temp_c": 22,
      "conditions": "sunny"
    }
```
      </div>
    </div>
  </div>
  <div
    v-click="3"
    transition duration-500 ease-in-out
    :class="$clicks < 3 ? 'opacity-0 translate-y-10' : 'opacity-100 translate-y-0'"
  >
    <div border="2 solid green-800/50" rounded-lg h-full>
      <div flex items-center bg="green-800/30" px-3 py-2 text-green-300>
        <div i-carbon:flow text-sm mr-1 />
        <div text-xs><em>返回 Command</em></div>
      </div>
      <div bg="green-800/10" px-3 py-3 text-xs>
        <div mb-2>更新 Agent 状态</div>
```python
@tool
def set_language(
    lang: str,
    runtime: ToolRuntime,
) -> Command:
    """Set language pref."""
    return Command(update={
      "lang": lang,
      "messages": [
        ToolMessage(
          content=f"Set: {lang}",
          tool_call_id=
            runtime.tool_call_id
        )
      ]
    })
```
      </div>
    </div>
  </div>
</div>

---
class: py-8
glowSeed: 950
---

## 错误处理

<div grid grid-cols-2 gap-8>
  <div>
```python{1-2|4-5|7-11|13-14}{maxHeight:'280px'}
# 捕获所有错误，返回消息给 LLM
ToolNode(tools, handle_tool_errors=True)

# 自定义错误消息
ToolNode(tools,
  handle_tool_errors="Something went wrong")

# 自定义处理器
def handle_error(e: ValueError) -> str:
    return f"Invalid input: {e}"

ToolNode(tools, handle_tool_errors=handle_error)

# 仅捕获特定异常
ToolNode(tools,
  handle_tool_errors=(ValueError, TypeError))
```
  </div>
  <div>
    <div border="2 solid rose-800/50" rounded-lg mb-4>
      <div flex items-center bg="rose-800/30" px-3 py-2 text-rose-300>
        <div i-carbon:warning text-sm mr-1 />
        <div text-xs><em>错误处理策略</em></div>
      </div>
      <div bg="rose-800/10" px-4 py-3 text-sm>
        <div mb-3>
          <span text-rose-300 font-bold>True</span> — 捕获所有错误，LLM 自动重试
        </div>
        <div mb-3>
          <span text-rose-300 font-bold>字符串</span> — 自定义错误消息返回给模型
        </div>
        <div mb-3>
          <span text-rose-300 font-bold>函数</span> — 自定义错误处理逻辑
        </div>
        <div>
          <span text-rose-300 font-bold>元组</span> — 仅捕获特定异常类型
        </div>
      </div>
    </div>
  </div>
</div>

---
layout: section
glowSeed: 1000
---

# 预构建工具生态

---
class: py-10
clicks: 4
glowSeed: 1050
---

## 开箱即用的工具

<div grid grid-cols-2 gap-4 mt-6>
<v-clicks>

  <div border="2 solid blue-800/50" rounded-lg>
    <div flex items-center bg="blue-800/30" px-3 py-2 text-blue-300>
      <div i-carbon:search text-sm mr-1 />
      <div text-xs><em>Web Search</em></div>
    </div>
    <div bg="blue-800/10" px-4 py-3 text-sm>
      Tavily, Google, Bing 搜索集成
    </div>
  </div>

  <div border="2 solid green-800/50" rounded-lg>
    <div flex items-center bg="green-800/30" px-3 py-2 text-green-300>
      <div i-carbon:code text-sm mr-1 />
      <div text-xs><em>Code Interpreter</em></div>
    </div>
    <div bg="green-800/10" px-4 py-3 text-sm>
      Python REPL、Shell 执行环境
    </div>
  </div>

  <div border="2 solid violet-800/50" rounded-lg>
    <div flex items-center bg="violet-800/30" px-3 py-2 text-violet-300>
      <div i-carbon:data-base text-sm mr-1 />
      <div text-xs><em>Database Access</em></div>
    </div>
    <div bg="violet-800/10" px-4 py-3 text-sm>
      SQL Database、向量数据库查询
    </div>
  </div>

  <div border="2 solid amber-800/50" rounded-lg>
    <div flex items-center bg="amber-800/30" px-3 py-2 text-amber-300>
      <div i-carbon:api text-sm mr-1 />
      <div text-xs><em>API 工具包</em></div>
    </div>
    <div bg="amber-800/10" px-4 py-3 text-sm>
      GitHub, Slack, Jira, Gmail 等
    </div>
  </div>

</v-clicks>
</div>

<div v-click="4" mt-6 text-sm class="text-white/50" text-center>
  完整列表见 <span text-cyan-300>LangChain Tools & Toolkits 集成页面</span>
</div>

---
layout: quote
glowSeed: 1100
---

> Tools are how agents interact with the world — start simple, add complexity as needed.

---
layout: end
glowSeed: 1150
---

# Thank You!

<div mt-4 text-sm class="text-white/50">
  LangChain Tools 完全指南
</div>
