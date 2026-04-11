---
layout: center
highlighter: shiki
css: unocss
colorSchema: dark
transition: fade-out
title: LangChain 短期记忆完全指南
exportFilename: langchain-short-term-memory
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
    Short-term Memory
  </div>
  <div text-2xl class="text-white/60" mb-10>
    LangChain 短期记忆完全指南
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

# 什么是短期记忆?

---
class: py-10
clicks: 3
glowSeed: 250
---

## 记忆系统概述

<div flex items-center gap-8 translate-y-8>
  <div
    v-click="1"
    flex-1 transition duration-500 ease-in-out
    :class="$clicks < 1 ? 'opacity-0 translate-y-10' : 'opacity-100 translate-y-0'"
  >
    <div border="2 solid violet-800/50" rounded-lg>
      <div flex items-center bg="violet-800/30" px-3 py-2 text-violet-300>
        <div i-carbon:memory text-sm mr-1 />
        <div text-xs><em>什么是记忆</em></div>
      </div>
      <div bg="violet-800/10" px-4 py-3 text-sm>
        记住先前交互信息的系统，对 AI Agent 至关重要
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
        <div i-carbon:chat text-sm mr-1 />
        <div text-xs><em>短期记忆</em></div>
      </div>
      <div bg="blue-800/10" px-4 py-3 text-sm>
        记住单个线程/对话中的先前交互
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
        <div i-carbon:group text-sm mr-1 />
        <div text-xs><em>线程与对话</em></div>
      </div>
      <div bg="green-800/10" px-4 py-3 text-sm>
        线程(thread) 在会话(session) 中组织多次交互
      </div>
    </div>
  </div>
</div>

<div v-click="3" mt-20 text-sm class="text-white/50" text-center>
  会话历史 (Conversation History) 是短期记忆最常见的形式
</div>

---
class: py-10
glowSeed: 300
---

## 长对话的挑战

<div grid grid-cols-2 gap-8>
  <div>
    <div grid grid-cols-2 gap-3>
      <div border="2 solid rose-800/50" rounded-lg>
        <div flex items-center bg="rose-800/30" px-3 py-2 text-rose-300>
          <div i-carbon:overflow-menu text-sm mr-1 />
          <div text-xs><em>上下文溢出</em></div>
        </div>
        <div bg="rose-800/10" px-3 py-2 text-xs>
          完整历史超出 LLM 上下文窗口
        </div>
      </div>
      <div border="2 solid amber-800/50" rounded-lg>
        <div flex items-center bg="amber-800/30" px-3 py-2 text-amber-300>
          <div i-carbon:warning text-sm mr-1 />
          <div text-xs><em>性能下降</em></div>
        </div>
        <div bg="amber-800/10" px-3 py-2 text-xs>
          被陈旧内容"分心"，响应质量降低
        </div>
      </div>
      <div border="2 solid orange-800/50" rounded-lg>
        <div flex items-center bg="orange-800/30" px-3 py-2 text-orange-300>
          <div i-carbon:timer text-sm mr-1 />
          <div text-xs><em>响应变慢</em></div>
        </div>
        <div bg="orange-800/10" px-3 py-2 text-xs>
          长上下文导致处理延迟增加
        </div>
      </div>
      <div border="2 solid red-800/50" rounded-lg>
        <div flex items-center bg="red-800/30" px-3 py-2 text-red-300>
          <div i-carbon:money text-sm mr-1 />
          <div text-xs><em>成本上升</em></div>
        </div>
        <div bg="red-800/10" px-3 py-2 text-xs>
          更多 token = 更高的 API 费用
        </div>
      </div>
    </div>
  </div>
  <div>
    <div text-sm class="text-white/50" mb-3>消息随时间增长的典型模式：</div>
    <div text-xs class="text-white/30" mb-1>System → Human → AI → Human → AI → ...</div>
    <div text-sm mt-4>
      由于上下文窗口<span text-rose-300 font-bold>有限</span>，需要使用技术来
      <span text-green-300 font-bold>移除</span>或<span text-cyan-300 font-bold>"遗忘"</span>
      陈旧信息
    </div>
  </div>
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

## 使用 Checkpointer 添加记忆

<div grid grid-cols-2 gap-8>
  <div>
    <div text-sm class="text-white/50" mb-3>开发环境 — InMemorySaver</div>
```python
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

agent = create_agent(
    "openai:gpt-5",
    [get_user_info],
    checkpointer=InMemorySaver(),  # 短期记忆
)

# 通过 thread_id 隔离不同对话
agent.invoke(
    {"messages": [{"role": "user",
                   "content": "Hi! My name is Bob."}]},
    {"configurable": {"thread_id": "1"}},
)
```
  </div>
  <div>
    <div text-sm class="text-white/50" mb-3>生产环境 — PostgresSaver</div>
```python
from langgraph.checkpoint.postgres import PostgresSaver

DB_URI = (
  "postgresql://postgres:postgres"
  "@localhost:5442/postgres?sslmode=disable"
)

with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
    checkpointer.setup()  # 自动建表
    agent = create_agent(
        "openai:gpt-5",
        [get_user_info],
        checkpointer=checkpointer,
    )
```
  </div>
</div>

---
class: py-8
glowSeed: 450
---

## 自定义代理记忆

<div grid grid-cols-2 gap-8>
  <div>
    <div text-sm class="text-white/50" mb-3>扩展 AgentState 添加自定义字段</div>
```python
from langchain.agents import create_agent, AgentState
from langgraph.checkpoint.memory import InMemorySaver

class CustomAgentState(AgentState):
    user_id: str
    preferences: dict

agent = create_agent(
    "openai:gpt-5",
    [get_user_info],
    state_schema=CustomAgentState,
    checkpointer=InMemorySaver(),
)
```
  </div>
  <div>
    <div text-sm class="text-white/50" mb-3>传入自定义状态</div>
```python
result = agent.invoke(
    {
        "messages": [
            {"role": "user", "content": "Hello"}
        ],
        "user_id": "user_123",
        "preferences": {"theme": "dark"},
    },
    {"configurable": {"thread_id": "1"}},
)
```
    <div border="2 solid cyan-800/50" rounded-lg mt-3>
      <div bg="cyan-800/10" px-3 py-2 text-xs>
        自定义字段随 state 一起持久化到 checkpointer
      </div>
    </div>
  </div>
</div>

---
layout: section
glowSeed: 500
---

# 常见模式

---
class: py-10
clicks: 4
glowSeed: 550
---

## 四种常见模式

<div grid grid-cols-2 gap-4 mt-6>
<v-clicks>

  <div border="2 solid violet-800/50" rounded-lg>
    <div flex items-center bg="violet-800/30" px-3 py-2 text-violet-300>
      <div i-carbon:scissors-cut text-sm mr-1 />
      <div text-xs><em>修剪消息</em></div>
    </div>
    <div bg="violet-800/10" px-4 py-3 text-sm>
      移除早期消息，保留最近 N 条
    </div>
  </div>

  <div border="2 solid blue-800/50" rounded-lg>
    <div flex items-center bg="blue-800/30" px-3 py-2 text-blue-300>
      <div i-carbon:trash-can text-sm mr-1 />
      <div text-xs><em>删除消息</em></div>
    </div>
    <div bg="blue-800/10" px-4 py-3 text-sm>
      从状态中永久删除特定消息
    </div>
  </div>

  <div border="2 solid green-800/50" rounded-lg>
    <div flex items-center bg="green-800/30" px-3 py-2 text-green-300>
      <div i-carbon:document-tasks text-sm mr-1 />
      <div text-xs><em>总结消息</em></div>
    </div>
    <div bg="green-800/10" px-4 py-3 text-sm>
      用摘要替换早期消息，保留关键信息
    </div>
  </div>

  <div border="2 solid amber-800/50" rounded-lg>
    <div flex items-center bg="amber-800/30" px-3 py-2 text-amber-300>
      <div i-carbon:settings-adjust text-sm mr-1 />
      <div text-xs><em>自定义策略</em></div>
    </div>
    <div bg="amber-800/10" px-4 py-3 text-sm>
      消息过滤、条件截断等灵活策略
    </div>
  </div>

</v-clicks>
</div>

---
class: py-8
glowSeed: 600
---

## 修剪消息 — @before_model

<div grid grid-cols-2 gap-8>
  <div>
```python{1-4|6-12|14-18|all}{maxHeight:'320px'}
from langchain.messages import RemoveMessage
from langgraph.graph.message import REMOVE_ALL_MESSAGES
from langchain.agents import create_agent, AgentState
from langchain.agents.middleware import before_model

@before_model
def trim_messages(state, runtime):
    """Keep only the last few messages."""
    messages = state["messages"]
    if len(messages) <= 3:
        return None  # 无需修剪
    first_msg = messages[0]
    recent = messages[-3:] if len(messages) % 2 == 0 \
        else messages[-4:]
    return {
        "messages": [
            RemoveMessage(id=REMOVE_ALL_MESSAGES),
            *recent
        ]
    }

agent = create_agent(
    model, tools=tools,
    middleware=[trim_messages],
    checkpointer=InMemorySaver(),
)
```
  </div>
  <div>
    <div border="2 solid violet-800/50" rounded-lg mb-4>
      <div flex items-center bg="violet-800/30" px-3 py-2 text-violet-300>
        <div i-carbon:flow text-sm mr-1 />
        <div text-xs><em>工作流程</em></div>
      </div>
      <div bg="violet-800/10" px-4 py-3 text-sm>
        <div mb-2>1. <span text-violet-300>用户发送消息</span></div>
        <div mb-2>2. <span text-violet-300>@before_model</span> 检查消息数量</div>
        <div mb-2>3. 超过阈值 → 移除早期消息</div>
        <div>4. LLM 只看到<span text-green-300>最近的消息</span></div>
      </div>
    </div>
    <div border="2 solid cyan-800/50" rounded-lg>
      <div flex items-center bg="cyan-800/30" px-3 py-2 text-cyan-300>
        <div i-carbon:information text-sm mr-1 />
        <div text-xs><em>关键 API</em></div>
      </div>
      <div bg="cyan-800/10" px-4 py-3 text-sm>
        <div mb-2><span text-cyan-300 font-bold>RemoveMessage</span> — 删除指定 ID 的消息</div>
        <div><span text-cyan-300 font-bold>REMOVE_ALL_MESSAGES</span> — 清除全部再重建</div>
      </div>
    </div>
  </div>
</div>

---
class: py-8
glowSeed: 650
---

## 删除消息 — RemoveMessage

<div grid grid-cols-2 gap-8>
  <div>
    <div text-blue-300 font-bold mb-2>删除特定消息</div>
```python
from langchain.messages import RemoveMessage

def delete_messages(state):
    messages = state["messages"]
    if len(messages) > 2:
        # 删除最早的 2 条消息
        return {
            "messages": [
                RemoveMessage(id=m.id)
                for m in messages[:2]
            ]
        }
```
    <div text-green-300 font-bold mb-2 mt-4>删除全部消息</div>
```python
from langgraph.graph.message import REMOVE_ALL_MESSAGES

def clear_all(state):
    return {
        "messages": [
            RemoveMessage(id=REMOVE_ALL_MESSAGES)
        ]
    }
```
  </div>
  <div>
    <div border="2 solid blue-800/50" rounded-lg mb-4>
      <div flex items-center bg="blue-800/30" px-3 py-2 text-blue-300>
        <div i-carbon:warning-alt text-sm mr-1 />
        <div text-xs><em>注意事项</em></div>
      </div>
      <div bg="blue-800/10" px-4 py-3 text-sm>
        <div mb-2>删除后确保消息历史<span text-amber-300>有效</span>：</div>
        <div mb-2 text-xs>• 某些提供商要求以 <span text-amber-300>user</span> 消息开头</div>
        <div mb-2 text-xs>• <span text-amber-300>assistant</span> 的工具调用后必须有对应的 <span text-amber-300>tool</span> 结果</div>
        <div text-xs>• 需要状态键使用 <span text-cyan-300>add_messages</span> reducer</div>
      </div>
    </div>
    <div border="2 solid green-800/50" rounded-lg>
      <div flex items-center bg="green-800/30" px-3 py-2 text-green-300>
        <div i-carbon:code text-sm mr-1 />
        <div text-xs><em>搭配 @after_model</em></div>
      </div>
      <div bg="green-800/10" px-4 py-3 text-xs>
        可在模型响应后自动删除旧消息，保持历史精简
      </div>
    </div>
  </div>
</div>

---
class: py-8
glowSeed: 700
---

## 总结消息 — SummarizationMiddleware

<div grid grid-cols-2 gap-8>
  <div>
```python{1-3|5-10|all}{maxHeight:'280px'}
from langchain.agents.middleware import (
    SummarizationMiddleware
)
from langgraph.checkpoint.memory import InMemorySaver

agent = create_agent(
    model="openai:gpt-4o",
    tools=[],
    middleware=[
        SummarizationMiddleware(
            model="openai:gpt-4o-mini",
            max_tokens_before_summary=4000,
            messages_to_keep=20,
        )
    ],
    checkpointer=InMemorySaver(),
)
```
    <div text-xs class="text-white/40" mt-2>用摘要替换早期消息，避免丢失关键信息</div>
  </div>
  <div>
    <div border="2 solid green-800/50" rounded-lg mb-4>
      <div flex items-center bg="green-800/30" px-3 py-2 text-green-300>
        <div i-carbon:flow text-sm mr-1 />
        <div text-xs><em>工作原理</em></div>
      </div>
      <div bg="green-800/10" px-4 py-3 text-sm>
        <div mb-2>1. 监控消息的 <span text-green-300>token 总量</span></div>
        <div mb-2>2. 超过 <span text-amber-300>max_tokens</span> 阈值时触发</div>
        <div mb-2>3. LLM 生成<span text-cyan-300>摘要</span>替换早期消息</div>
        <div>4. 保留最近 <span text-violet-300>messages_to_keep</span> 条</div>
      </div>
    </div>
    <div border="2 solid amber-800/50" rounded-lg>
      <div flex items-center bg="amber-800/30" px-3 py-2 text-amber-300>
        <div i-carbon:compare text-sm mr-1 />
        <div text-xs><em>vs 修剪/删除</em></div>
      </div>
      <div bg="amber-800/10" px-4 py-3 text-sm>
        修剪和删除会<span text-rose-300>丢失信息</span>，总结则用摘要<span text-green-300>保留关键内容</span>
      </div>
    </div>
  </div>
</div>

---
layout: section
glowSeed: 750
---

# 访问记忆与中间件

---
class: py-8
glowSeed: 800
---

## 在工具中读写短期记忆

<div grid grid-cols-2 gap-8>
  <div>
    <div text-violet-300 font-bold mb-2>读取记忆</div>
```python
from langchain.tools import tool, ToolRuntime
from langchain.agents import create_agent, AgentState

class CustomState(AgentState):
    user_id: str

@tool
def get_user_info(runtime: ToolRuntime) -> str:
    """Look up user info."""
    user_id = runtime.state["user_id"]
    return "John Smith" if user_id == "user_123" \
        else "Unknown"
```
  </div>
  <div>
    <div text-green-300 font-bold mb-2>写入记忆</div>
```python
from langgraph.types import Command
from langchain.messages import ToolMessage

@tool
def update_user_info(
    runtime: ToolRuntime,
) -> Command:
    """Look up and update user info."""
    name = "John Smith"
    return Command(update={
        "user_name": name,
        "messages": [
            ToolMessage(
                "Updated!",
                tool_call_id=runtime.tool_call_id,
            )
        ]
    })
```
  </div>
</div>

---
class: py-8
glowSeed: 850
---

## 动态提示 — @dynamic_prompt

```python{1-5|7-10|all}{maxHeight:'280px'}
from langchain.agents.middleware import dynamic_prompt, ModelRequest

@dynamic_prompt
def dynamic_system_prompt(request: ModelRequest) -> str:
    user_name = request.runtime.context["user_name"]
    return f"You are a helpful assistant. Address the user as {user_name}."

agent = create_agent(
    model="openai:gpt-5-nano",
    tools=[get_weather],
    middleware=[dynamic_system_prompt],
    context_schema=CustomContext,
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What is the weather?"}]},
    context=CustomContext(user_name="John Smith"),
)
# AI 回复: "Hi John Smith, the weather in SF is always sunny!"
```

<div text-sm class="text-white/40" mt-2>
  基于状态/上下文动态生成 system prompt，实现个性化对话
</div>

---
class: py-8
glowSeed: 900
---

## 中间件模式

<div grid grid-cols-2 gap-8>
  <div>
    <div text-violet-300 font-bold mb-2>@before_model</div>
```python{maxHeight:'200px'}
from langchain.agents.middleware import before_model

@before_model
def trim_messages(state, runtime):
    """模型调用前处理消息"""
    messages = state["messages"]
    if len(messages) <= 3:
        return None
    return {
        "messages": [
            RemoveMessage(id=REMOVE_ALL_MESSAGES),
            *messages[-3:]
        ]
    }
```
  </div>
  <div>
    <div text-cyan-300 font-bold mb-2>@after_model</div>
```python{maxHeight:'200px'}
from langchain.agents.middleware import after_model

@after_model
def validate_response(state, runtime):
    """模型调用后处理消息"""
    STOP_WORDS = ["password", "secret"]
    last_msg = state["messages"][-1]
    if any(w in last_msg.content for w in STOP_WORDS):
        return {
            "messages": [
                RemoveMessage(id=last_msg.id)
            ]
        }
    return None
```
  </div>
</div>

<div grid grid-cols-2 gap-8 mt-4>
  <div border="2 solid violet-800/50" rounded-lg>
    <div bg="violet-800/10" px-3 py-2 text-xs>
      在 LLM 调用前<span text-violet-300>修剪/过滤</span>消息，控制上下文窗口
    </div>
  </div>
  <div border="2 solid cyan-800/50" rounded-lg>
    <div bg="cyan-800/10" px-3 py-2 text-xs>
      在 LLM 响应后<span text-cyan-300>过滤/验证</span>，如移除敏感词
    </div>
  </div>
</div>

---
layout: quote
glowSeed: 950
---

> 短期记忆让 Agent 记住对话，中间件让它永不遗忘。

---
layout: end
glowSeed: 1000
---

# Thank You!

<div mt-4 text-sm class="text-white/50">
  LangChain 短期记忆完全指南
</div>
