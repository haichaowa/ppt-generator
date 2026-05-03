---
layout: center
highlighter: shiki
css: unocss
colorSchema: dark
transition: fade-out
title: Claude Code 最佳实践
exportFilename: claude-code-best-practices
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
  <div text-6xl font-bold mb-6>
    Claude Code 最佳实践
  </div>
  <div text-xl class="text-white/60" mb-10>
    从配置环境到并行扩展的完整指南
  </div>
  <div flex items-center gap-3 text-lg class="text-white/40">
    <div i-simple-icons:anthropic />
    <span>Anthropic 官方推荐模式</span>
  </div>
</div>

---
layout: quote
glowSeed: 200
---

> Claude Code 是一个代理式编码环境。与等待回答问题的聊天机器人不同，Claude Code 可以读取你的文件、运行命令、进行更改，并在你观看、重定向或完全离开的情况下自主解决问题。

---
layout: fact
glowSeed: 250
---

## Context Window

最重要的资源

---
class: py-10
glowSeed: 300
glow: left
---

<div flex items-center gap-3 mb-6>
  <div i-carbon:warning-alt text-3xl text-amber-400 />
  <div text-3xl font-bold>核心约束：Context Window</div>
</div>

<div class="text-white/60" mb-8>
  大多数最佳实践都基于一个约束 — Context Window 填充速度很快
</div>

<div grid grid-cols-2 gap-5>
  <div border="2 solid red-800/50" rounded-lg>
    <div flex items-center bg="red-800/30" px-3 py-2 text-red-300>
      <div i-carbon:close-filled text-sm mr-1 />
      <div text-xs><em>Context 充满时</em></div>
    </div>
    <div bg="red-800/10" px-4 py-3 text-sm>
      <div class="text-white/80">LLM 性能下降</div>
      <div class="text-white/80">开始遗忘早期指令</div>
      <div class="text-white/80">犯更多错误</div>
    </div>
  </div>
  <div border="2 solid green-800/50" rounded-lg>
    <div flex items-center bg="green-800/30" px-3 py-2 text-green-300>
      <div i-carbon:checkmark-filled text-sm mr-1 />
      <div text-xs><em>管理好 Context</em></div>
    </div>
    <div bg="green-800/10" px-4 py-3 text-sm>
      <div class="text-white/80">持续保持高性能</div>
      <div class="text-white/80">准确遵循指令</div>
      <div class="text-white/80">更少的错误和修正</div>
    </div>
  </div>
</div>

<div mt-6 text-center>
  <div border="2 solid violet-800/50" rounded-lg bg="violet-800/10" px-4 py-3 inline-block>
    <span class="text-white/90">Context Window 是</span>
    <strong text-violet-300 text-lg>最重要的资源</strong>
  </div>
</div>

---
layout: section
glowSeed: 400
---

# 01
给 Claude 一种验证其工作的方式

---
class: py-10
clicks: 3
glowSeed: 500
glow: right
---

<div text-3xl font-bold mb-2>验证策略</div>
<div class="text-white/50" mb-8>包括测试、屏幕截图或预期输出 — 这是你能做的最高杠杆的事情</div>

<div grid grid-cols-3 gap-5>
  <div
    v-click="1"
    border="2 solid blue-800/50" rounded-lg
    transition duration-500 ease-in-out
    :class="$clicks < 1 ? 'opacity-0 translate-y-10' : 'opacity-100 translate-y-0'"
  >
    <div flex items-center bg="blue-800/30" px-3 py-2 text-blue-300>
      <div i-carbon:test-tool text-sm mr-1 />
      <div text-xs><em>提供验证标准</em></div>
    </div>
    <div bg="blue-800/10" px-4 py-3 text-sm>
      <div class="text-white/70" mb-2>编写测试用例</div>
      <div class="text-white/50 text-xs">"实现后运行测试验证"</div>
    </div>
  </div>
  <div
    v-click="2"
    border="2 solid green-800/50" rounded-lg
    transition duration-500 ease-in-out
    :class="$clicks < 2 ? 'opacity-0 translate-y-10' : 'opacity-100 translate-y-0'"
  >
    <div flex items-center bg="green-800/30" px-3 py-2 text-green-300>
      <div i-carbon:screen text-sm mr-1 />
      <div text-xs><em>视觉验证</em></div>
    </div>
    <div bg="green-800/10" px-4 py-3 text-sm>
      <div class="text-white/70" mb-2>截图对比</div>
      <div class="text-white/50 text-xs">"截图并与原始设计比较"</div>
    </div>
  </div>
  <div
    v-click="3"
    border="2 solid amber-800/50" rounded-lg
    transition duration-500 ease-in-out
    :class="$clicks < 3 ? 'opacity-0 translate-y-10' : 'opacity-100 translate-y-0'"
  >
    <div flex items-center bg="amber-800/30" px-3 py-2 text-amber-300>
      <div i-carbon:debug text-sm mr-1 />
      <div text-xs><em>解决根本原因</em></div>
    </div>
    <div bg="amber-800/10" px-4 py-3 text-sm>
      <div class="text-white/70" mb-2>修复而非抑制</div>
      <div class="text-white/50 text-xs">"粘贴错误，修复根因"</div>
    </div>
  </div>
</div>

<div
  v-click="3"
  mt-6 text-center
  class="text-white/40 text-sm"
  transition duration-500 ease-in-out
  :class="$clicks < 3 ? 'opacity-0' : 'opacity-100'"
>
  投资使你的验证非常可靠 — 测试套件、linter 或检查输出的 Bash 命令
</div>

---
class: py-10
glowSeed: 520
---

<div text-2xl font-bold mb-6>验证策略对比表</div>

<div mt-4 />

| 策略 | 之前 | 之后 |
|------|------|------|
| **提供验证标准** | "实现一个验证电子邮件地址的函数" | "编写 validateEmail 函数，含测试用例，实现后运行测试" |
| **视觉验证 UI** | "让仪表板看起来更好" | "[粘贴截图] 实现此设计，截图对比差异并修复" |
| **解决根本原因** | "构建失败" | "构建失败，错误如下。修复并验证，解决根因" |

<div mt-6 text-sm class="text-white/40">
  UI 更改可使用 Chrome 中的 Claude 扩展验证 — 在浏览器中打开新标签页测试
</div>

---
layout: section
glowSeed: 600
---

# 02
先探索，再规划，最后编码

---
class: py-8
clicks: 4
glowSeed: 700
glow: bottom
---

<div text-3xl font-bold mb-2>四阶段工作流</div>
<div class="text-white/50" mb-6>将研究和规划与实现分开，避免解决错误的问题</div>

<div flex items-center gap-4>
<v-clicks>

<div
  rounded-lg
  border="2 solid violet-800" bg="violet-800/20"
  backdrop-blur
  flex-1 h-full
  transition duration-500 ease-in-out
>
  <div px-5 py-8 flex items-center justify-center>
    <div i-carbon:search text-4xl text-violet-400 />
  </div>
  <div bg="violet-800/30" w-full px-4 py-2 flex items-center justify-center text-center>
    <span text-sm>探索</span>
  </div>
  <div px-3 py-2 text-xs class="text-white/60" text-center>Plan Mode 读取文件</div>
</div>

<div
  rounded-lg
  border="2 solid blue-800" bg="blue-800/20"
  backdrop-blur
  flex-1 h-full
  transition duration-500 ease-in-out
>
  <div px-5 py-8 flex items-center justify-center>
    <div i-carbon:plan text-4xl text-blue-400 />
  </div>
  <div bg="blue-800/30" w-full px-4 py-2 flex items-center justify-center text-center>
    <span text-sm>规划</span>
  </div>
  <div px-3 py-2 text-xs class="text-white/60" text-center>详细实现计划</div>
</div>

<div
  rounded-lg
  border="2 solid green-800" bg="green-800/20"
  backdrop-blur
  flex-1 h-full
  transition duration-500 ease-in-out
>
  <div px-5 py-8 flex items-center justify-center>
    <div i-carbon:code text-4xl text-green-400 />
  </div>
  <div bg="green-800/30" w-full px-4 py-2 flex items-center justify-center text-center>
    <span text-sm>实现</span>
  </div>
  <div px-3 py-2 text-xs class="text-white/60" text-center>Normal Mode 编码</div>
</div>

<div
  rounded-lg
  border="2 solid amber-800" bg="amber-800/20"
  backdrop-blur
  flex-1 h-full
  transition duration-500 ease-in-out
>
  <div px-5 py-8 flex items-center justify-center>
    <div i-carbon:submit text-4xl text-amber-400 />
  </div>
  <div bg="amber-800/30" w-full px-4 py-2 flex items-center justify-center text-center>
    <span text-sm>提交</span>
  </div>
  <div px-3 py-2 text-xs class="text-white/60" text-center>描述性提交 PR</div>
</div>

</v-clicks>
</div>

<div mt-4 text-center text-xs class="text-white/30">
  如果你能用一句话描述 diff，跳过计划
</div>

---
class: py-10
glowSeed: 710
---

<div text-2xl font-bold mb-4>Plan Mode 示例流程</div>

<div grid grid-cols-2 gap-6 mt-6>
  <div>
    <div text-sm font-bold text-violet-300 mb-2>探索阶段</div>

```text
read /src/auth and understand how we handle
sessions and login. also look at how we
manage environment variables for secrets.
```

  </div>
  <div>
    <div text-sm font-bold text-blue-300 mb-2>规划阶段</div>

```text
I want to add Google OAuth. What files need
to change? What's the session flow?
Create a plan.
```

  </div>
</div>

<div mt-4 text-sm class="text-white/40">
  按 Ctrl+G 在文本编辑器中打开计划进行直接编辑，然后 Claude 继续
</div>

---
class: flex justify-center items-center gap-20 px-40 text-xl
glowSeed: 730
---

<div
  absolute text-5xl
  :class="$clicks < 1 ? 'text-white' : 'translate-y--18 scale-40 text-white/30'"
  transition duration-500 ease-in-out
>
  <span>什么时候应该跳过规划？</span>
</div>

<div flex flex-col items-center>
  <v-clicks>
    <div mt-4>
      <h1 flex items-center text="5xl!">
        <span>能用一句话描述 diff 时</span>
      </h1>
    </div>
  </v-clicks>
</div>

---
layout: section
glowSeed: 800
---

# 03
在提示中提供具体的上下文

---
class: py-10
clicks: 4
glowSeed: 900
glow: right
---

<div text-3xl font-bold mb-2>精确指令策略</div>
<div class="text-white/50" mb-6>你的指令越精确，你需要的更正就越少</div>

<div grid grid-cols-2 gap-4>
<v-clicks>

<div border="2 solid cyan-800/50" rounded-lg bg="cyan-800/10">
  <div flex items-center bg="cyan-800/30" px-3 py-2 text-cyan-300>
    <div i-carbon:target text-sm mr-1 />
    <div text-xs><em>限定任务范围</em></div>
  </div>
  <div bg="cyan-800/10" px-4 py-3 text-sm class="text-white/70">
    指定哪个文件、什么场景和测试偏好
  </div>
</div>

<div border="2 solid purple-800/50" rounded-lg bg="purple-800/10">
  <div flex items-center bg="purple-800/30" px-3 py-2 text-purple-300>
    <div i-carbon:link text-sm mr-1 />
    <div text-xs><em>指向来源</em></div>
  </div>
  <div bg="purple-800/10" px-4 py-3 text-sm class="text-white/70">
    引导 Claude 到可以回答问题的来源
  </div>
</div>

<div border="2 solid emerald-800/50" rounded-lg bg="emerald-800/10">
  <div flex items-center bg="emerald-800/30" px-3 py-2 text-emerald-300>
    <div i-carbon:reference text-sm mr-1 />
    <div text-xs><em>参考现有模式</em></div>
  </div>
  <div bg="emerald-800/10" px-4 py-3 text-sm class="text-white/70">
    指向代码库中已有的模式并遵循
  </div>
</div>

<div border="2 solid rose-800/50" rounded-lg bg="rose-800/10">
  <div flex items-center bg="rose-800/30" px-3 py-2 text-rose-300>
    <div i-carbon:stethoscope text-sm mr-1 />
    <div text-xs><em>描述症状</em></div>
  </div>
  <div bg="rose-800/10" px-4 py-3 text-sm class="text-white/70">
    提供症状、位置和"修复"的样子
  </div>
</div>

</v-clicks>
</div>

---
class: py-10
clicks: 5
glowSeed: 950
---

<div text-3xl font-bold mb-2>提供丰富的内容</div>
<div class="text-white/50" mb-6>使用多种方式向 Claude 提供数据</div>

<div grid grid-cols-3 gap-4 mt-4>
<v-clicks>

<div text-center>
  <div flex items-center justify-center mb-3>
    <div i-carbon:document text-4xl text-blue-400 />
  </div>
  <div font-bold text-sm mb-1>@ 引用文件</div>
  <div text-xs class="text-white/50">直接读取文件内容</div>
</div>

<div text-center>
  <div flex items-center justify-center mb-3>
    <div i-carbon:image text-4xl text-green-400 />
  </div>
  <div font-bold text-sm mb-1>粘贴图像</div>
  <div text-xs class="text-white/50">复制/粘贴或拖放</div>
</div>

<div text-center>
  <div flex items-center justify-center mb-3>
    <div i-carbon:link text-4xl text-purple-400 />
  </div>
  <div font-bold text-sm mb-1>提供 URL</div>
  <div text-xs class="text-white/50">文档和 API 参考</div>
</div>

<div text-center>
  <div flex items-center justify-center mb-3>
    <div i-carbon:terminal text-4xl text-amber-400 />
  </div>
  <div font-bold text-sm mb-1>管道数据</div>
  <div text-xs class="text-white/50">cat error.log | claude</div>
</div>

<div text-center>
  <div flex items-center justify-center mb-3>
    <div i-carbon:cloud-download text-4xl text-cyan-400 />
  </div>
  <div font-bold text-sm mb-1>让 Claude 自己获取</div>
  <div text-xs class="text-white/50">Bash、MCP 工具读取</div>
</div>

<div text-center>
  <div flex items-center justify-center mb-3>
    <div i-carbon:idea text-4xl text-rose-400 />
  </div>
  <div font-bold text-sm mb-1>模糊提示</div>
  <div text-xs class="text-white/50">探索时有用</div>
</div>

</v-clicks>
</div>

---
layout: section
glowSeed: 1000
---

# 04
配置你的环境

---
class: py-10
clicks: 2
glowSeed: 1100
glow: right
---

<div flex items-center gap-3 mb-2>
  <div i-carbon:document text-3xl text-violet-400 />
  <div text-3xl font-bold>编写有效的 CLAUDE.md</div>
</div>

<div class="text-white/50" mb-6>运行 /init 生成基础文件，然后随时间精化</div>

<div grid grid-cols-2 gap-6>
  <div
    v-click="1"
    border="2 solid green-800/50" rounded-lg
    transition duration-500 ease-in-out
    :class="$clicks < 1 ? 'opacity-0' : 'opacity-100'"
  >
    <div flex items-center bg="green-800/30" px-3 py-2 text-green-300>
      <div i-carbon:checkmark text-sm mr-1 />
      <div text-xs><em>应该包含</em></div>
    </div>
    <div bg="green-800/10" px-4 py-3 text-sm class="text-white/70">
      <div>Claude 无法猜测的 Bash 命令</div>
      <div>与默认值不同的代码风格规则</div>
      <div>测试指令和首选测试运行器</div>
      <div>存储库礼仪（分支、PR 约定）</div>
      <div>项目特定的架构决策</div>
    </div>
  </div>
  <div
    v-click="2"
    border="2 solid red-800/50" rounded-lg
    transition duration-500 ease-in-out
    :class="$clicks < 2 ? 'opacity-0' : 'opacity-100'"
  >
    <div flex items-center bg="red-800/30" px-3 py-2 text-red-300>
      <div i-carbon:close text-sm mr-1 />
      <div text-xs><em>应该排除</em></div>
    </div>
    <div bg="red-800/10" px-4 py-3 text-sm class="text-white/70">
      <div>读取代码就能弄清楚的东西</div>
      <div>标准语言约定</div>
      <div>详细的 API 文档</div>
      <div>经常变化的信息</div>
      <div>自明的实践</div>
    </div>
  </div>
</div>

---
class: py-8
glowSeed: 1150
---

<div text-2xl font-bold mb-4>CLAUDE.md 示例</div>

```markdown
# Code style
- Use ES modules (import/export) syntax, not CommonJS (require)
- Destructure imports when possible (eg. import { foo } from 'bar')

# Workflow
- Be sure to typecheck when you're done making changes
- Prefer running single tests, and not the whole test suite
```

<div mt-4 text-sm class="text-white/40">
  支持多位置：主文件夹 ~/.claude/CLAUDE.md、项目根目录、子目录、支持 @path/to/import 导入
</div>

---
class: py-10
glowSeed: 1180
---

<div text-2xl font-bold mb-4>CLAUDE.md 位置与作用域</div>

<div mt-6 ml-8>

<div flex gap-4 mb-5>
  <div flex flex-col items-center>
    <div w-3 h-3 rounded-full bg-violet-500 mt-1.5 />
    <div w-0.5 flex-1 bg="violet-800/30" mt-1 />
  </div>
  <div flex-1 pb-2>
    <div text-sm font-bold text-violet-300>~/.claude/CLAUDE.md</div>
    <div text-xs mt-1 class="text-white/50">适用于所有 Claude 会话</div>
  </div>
</div>

<div flex gap-4 mb-5>
  <div flex flex-col items-center>
    <div w-3 h-3 rounded-full bg-blue-500 mt-1.5 />
    <div w-0.5 flex-1 bg="blue-800/30" mt-1 />
  </div>
  <div flex-1 pb-2>
    <div text-sm font-bold text-blue-300>./CLAUDE.md</div>
    <div text-xs mt-1 class="text-white/50">检入 git 与团队共享</div>
  </div>
</div>

<div flex gap-4 mb-5>
  <div flex flex-col items-center>
    <div w-3 h-3 rounded-full bg-green-500 mt-1.5 />
    <div w-0.5 flex-1 bg="green-800/30" mt-1 />
  </div>
  <div flex-1 pb-2>
    <div text-sm font-bold text-green-300>./CLAUDE.local.md</div>
    <div text-xs mt-1 class="text-white/50">个人项目笔记，加入 .gitignore</div>
  </div>
</div>

<div flex gap-4 mb-5>
  <div flex flex-col items-center>
    <div w-3 h-3 rounded-full bg-amber-500 mt-1.5 />
    <div w-0.5 flex-1 bg="amber-800/30" mt-1 />
  </div>
  <div flex-1 pb-2>
    <div text-sm font-bold text-amber-300>子目录 CLAUDE.md</div>
    <div text-xs mt-1 class="text-white/50">处理该目录文件时按需加载</div>
  </div>
</div>

<div flex gap-4>
  <div flex flex-col items-center>
    <div w-3 h-3 rounded-full bg-rose-500 mt-1.5 />
  </div>
  <div flex-1>
    <div text-sm font-bold text-rose-300>支持 @ 导入</div>
    <div text-xs mt-1 class="text-white/50">@README.md、@docs/git-instructions.md</div>
  </div>
</div>

</div>

---
class: py-10
glowSeed: 1200
---

<div text-3xl font-bold mb-6>权限配置三方式</div>

<div grid grid-cols-3 gap-6 mt-4>

<div border="2 solid violet-800/50" rounded-lg bg="violet-800/10">
  <div flex items-center bg="violet-800/30" px-3 py-2 text-violet-300>
    <div i-carbon:flash text-sm mr-1 />
    <div text-xs><em>Auto Mode</em></div>
  </div>
  <div bg="violet-800/10" px-4 py-3 text-sm class="text-white/60">
    分类器模型审查命令，仅阻止有风险操作
  </div>
</div>

<div border="2 solid blue-800/50" rounded-lg bg="blue-800/10">
  <div flex items-center bg="blue-800/30" px-3 py-2 text-blue-300>
    <div i-carbon:list text-sm mr-1 />
    <div text-xs><em>允许列表</em></div>
  </div>
  <div bg="blue-800/10" px-4 py-3 text-sm class="text-white/60">
    允许可安全执行的特定工具，如 npm run lint
  </div>
</div>

<div border="2 solid green-800/50" rounded-lg bg="green-800/10">
  <div flex items-center bg="green-800/30" px-3 py-2 text-green-300>
    <div i-carbon:security text-sm mr-1 />
    <div text-xs><em>沙箱</em></div>
  </div>
  <div bg="green-800/10" px-4 py-3 text-sm class="text-white/60">
    操作系统级隔离，限制文件系统和网络访问
  </div>
</div>

</div>

---
class: py-10
glowSeed: 1250
---

<div text-2xl font-bold mb-6>CLI 工具 — 最高效的外部交互方式</div>

<div grid grid-cols-4 gap-5 mt-4>
  <div text-center>
    <div flex items-center justify-center mb-3>
      <div i-carbon:logo-github text-4xl />
    </div>
    <div font-bold text-sm mb-1>gh</div>
    <div text-xs class="text-white/50">GitHub CLI</div>
  </div>
  <div text-center>
    <div flex items-center justify-center mb-3>
      <div i-carbon:cloud text-4xl text-amber-400 />
    </div>
    <div font-bold text-sm mb-1>aws</div>
    <div text-xs class="text-white/50">AWS CLI</div>
  </div>
  <div text-center>
    <div flex items-center justify-center mb-3>
      <div i-carbon:cloud text-4xl text-blue-400 />
    </div>
    <div font-bold text-sm mb-1>gcloud</div>
    <div text-xs class="text-white/50">Google Cloud</div>
  </div>
  <div text-center>
    <div flex items-center justify-center mb-3>
      <div i-carbon:analytics text-4xl text-rose-400 />
    </div>
    <div font-bold text-sm mb-1>sentry-cli</div>
    <div text-xs class="text-white/50">错误监控</div>
  </div>
</div>

<div mt-6 text-sm class="text-white/40">
  Claude 也能学习未知的 CLI 工具：Use 'foo-cli --help' to learn, then use it to solve A, B, C.
</div>

---
class: py-8
clicks: 6
glowSeed: 1300
---

<div text-3xl font-bold mb-2>环境配置工具箱</div>
<div class="text-white/50" mb-6>一些设置步骤使 Claude Code 在所有会话中显著更有效</div>

<div grid grid-cols-3 gap-4>
<v-clicks>

<div border="2 solid violet-800/50" rounded-lg bg="violet-800/10">
  <div flex items-center bg="violet-800/30" px-3 py-2 text-violet-300>
    <div i-carbon:security text-sm mr-1 />
    <div text-xs><em>权限配置</em></div>
  </div>
  <div bg="violet-800/10" px-4 py-3 text-xs class="text-white/60">
    Auto mode / 允许列表 / 沙箱
  </div>
</div>

<div border="2 solid blue-800/50" rounded-lg bg="blue-800/10">
  <div flex items-center bg="blue-800/30" px-3 py-2 text-blue-300>
    <div i-carbon:terminal text-sm mr-1 />
    <div text-xs><em>CLI 工具</em></div>
  </div>
  <div bg="blue-800/10" px-4 py-3 text-xs class="text-white/60">
    gh / aws / gcloud / sentry-cli
  </div>
</div>

<div border="2 solid green-800/50" rounded-lg bg="green-800/10">
  <div flex items-center bg="green-800/30" px-3 py-2 text-green-300>
    <div i-carbon:plug text-sm mr-1 />
    <div text-xs><em>MCP 服务器</em></div>
  </div>
  <div bg="green-800/10" px-4 py-3 text-xs class="text-white/60">
    Notion / Figma / 数据库连接
  </div>
</div>

<div border="2 solid amber-800/50" rounded-lg bg="amber-800/10">
  <div flex items-center bg="amber-800/30" px-3 py-2 text-amber-300>
    <div i-carbon:hook text-sm mr-1 />
    <div text-xs><em>Hooks</em></div>
  </div>
  <div bg="amber-800/10" px-4 py-3 text-xs class="text-white/60">
    确定性自动化操作
  </div>
</div>

<div border="2 solid cyan-800/50" rounded-lg bg="cyan-800/10">
  <div flex items-center bg="cyan-800/30" px-3 py-2 text-cyan-300>
    <div i-carbon:skill text-sm mr-1 />
    <div text-xs><em>Skills</em></div>
  </div>
  <div bg="cyan-800/10" px-4 py-3 text-xs class="text-white/60">
    域知识和可重用工作流
  </div>
</div>

<div border="2 solid rose-800/50" rounded-lg bg="rose-800/10">
  <div flex items-center bg="rose-800/30" px-3 py-2 text-rose-300>
    <div i-carbon:bot text-sm mr-1 />
    <div text-xs><em>Subagents</em></div>
  </div>
  <div bg="rose-800/10" px-4 py-3 text-xs class="text-white/60">
    隔离 context 的专门助手
  </div>
</div>

</v-clicks>
</div>

---
class: py-10
glowSeed: 1320
---

<div text-2xl font-bold mb-4>Skills 示例</div>

<div grid grid-cols-2 gap-6>
  <div border="2 solid cyan-800/50" rounded-lg overflow-hidden bg="cyan-800/10">
    <div flex items-center bg="cyan-800/30" px-3 py-2 text-cyan-300>
      <div i-carbon:skill text-sm mr-1 />
      <div font-semibold text-xs>域知识 Skill</div>
    </div>
    <div bg="cyan-900/5" px-4 py-3>

```yaml
# .claude/skills/api-conventions/SKILL.md
name: api-conventions
description: REST API design conventions
---
# API Conventions
- Use kebab-case for URL paths
- Use camelCase for JSON properties
- Always include pagination for list endpoints
```

  </div>
  </div>
  <div border="2 solid amber-800/50" rounded-lg overflow-hidden bg="amber-800/10">
    <div flex items-center bg="amber-800/30" px-3 py-2 text-amber-300>
      <div i-carbon:flow text-sm mr-1 />
      <div font-semibold text-xs>可调用工作流</div>
    </div>
    <div bg="amber-900/5" px-4 py-3>

```yaml
# .claude/skills/fix-issue/SKILL.md
name: fix-issue
description: Fix a GitHub issue
disable-model-invocation: true
---
Analyze and fix the GitHub issue: $ARGUMENTS
```

  </div>
  </div>
</div>

<div mt-4 text-sm class="text-white/40">
  运行 /fix-issue 1234 调用。disable-model-invocation: true 用于需要手动触发副作用的场景
</div>

---
class: py-10
clicks: 2
glowSeed: 1350
---

<div text-2xl font-bold mb-4>Subagents 架构</div>

<div grid grid-cols-2 gap-6 mt-4>

<div flex flex-col items-center gap-3>

<div flex gap-3 w-full>
  <div flex-1 border="2 solid violet-800/50" rounded-lg bg="violet-900/15" px-4 py-3 text-center>
    <div text-sm font-bold text-violet-300>主对话</div>
    <div text-xs class="text-white/40">Main Context</div>
  </div>
</div>

<div text-xl class="opacity-30">⬇ 委托</div>

<div flex gap-3 w-full>
  <div flex-1 border="2 solid rose-800/50" rounded-lg bg="rose-900/15" px-4 py-3 text-center>
    <div text-sm font-bold text-rose-300>Subagent A</div>
    <div text-xs class="text-white/40">独立 Context</div>
  </div>
  <div flex-1 border="2 solid teal-800/50" rounded-lg bg="teal-900/15" px-4 py-3 text-center>
    <div text-sm font-bold text-teal-300>Subagent B</div>
    <div text-xs class="text-white/40">独立 Context</div>
  </div>
</div>

<div text-xl class="opacity-30">⬇ 返回摘要</div>

<div flex gap-3 w-full>
  <div flex-1 border="2 solid green-800/50" rounded-lg bg="green-900/15" px-4 py-3 text-center>
    <div text-sm font-bold text-green-300>主对话继续</div>
    <div text-xs class="text-white/40">Context 不被污染</div>
  </div>
</div>

</div>

<div flex flex-col justify-center>
  <div
    v-click="1"
    mb-4 border-l-2 border-violet-500 pl-4
    transition duration-300
    :class="$clicks < 1 ? 'opacity-30' : 'opacity-100'"
  >
    <div text-sm font-bold text-violet-300>探索代码库</div>
    <div text-xs mt-1 class="text-white/50">读取大量文件但不消耗主 Context</div>
  </div>
  <div
    v-click="2"
    border-l-2 border-green-500 pl-4
    transition duration-300
    :class="$clicks < 2 ? 'opacity-30' : 'opacity-100'"
  >
    <div text-sm font-bold text-green-300>验证代码</div>
    <div text-xs mt-1 class="text-white/50">实现后用 subagent 审查边界情况</div>
  </div>
</div>

</div>

---
class: py-10
glowSeed: 1360
---

<div text-2xl font-bold mb-4>Hooks — 确定性自动化</div>

<div class="text-white/50" mb-6>
  与 CLAUDE.md 指令不同，Hooks 是确定性的，保证操作发生
</div>

<div grid grid-cols-3 gap-5 mt-4>
  <div border="2 solid amber-800/50" rounded-lg bg="amber-800/10">
    <div flex items-center bg="amber-800/30" px-3 py-2 text-amber-300>
      <div i-carbon:edit text-sm mr-1 />
      <div text-xs><em>文件编辑后</em></div>
    </div>
    <div bg="amber-800/10" px-4 py-3 text-sm class="text-white/60">
      自动运行 eslint 检查
    </div>
  </div>
  <div border="2 solid red-800/50" rounded-lg bg="red-800/10">
    <div flex items-center bg="red-800/30" px-3 py-2 text-red-300>
      <div i-carbon:rule text-sm mr-1 />
      <div text-xs><em>写入保护</em></div>
    </div>
    <div bg="red-800/10" px-4 py-3 text-sm class="text-white/60">
      阻止写入迁移文件夹
    </div>
  </div>
  <div border="2 solid green-800/50" rounded-lg bg="green-800/10">
    <div flex items-center bg="green-800/30" px-3 py-2 text-green-300>
      <div i-carbon:terminal text-sm mr-1 />
      <div text-xs><em>自定义触发</em></div>
    </div>
    <div bg="green-800/10" px-4 py-3 text-sm class="text-white/60">
      任何需要保证执行的操作
    </div>
  </div>
</div>

<div mt-6 text-sm class="text-white/40">
  编辑 .claude/settings.json 配置 hooks，或让 Claude 编写："编写一个在每次文件编辑后运行 eslint 的 hook"
</div>

---
layout: section
glowSeed: 1400
---

# 05
有效沟通

---
class: py-10
clicks: 2
glowSeed: 1500
glow: right
---

<div text-3xl font-bold mb-2>提问与采访</div>
<div class="text-white/50" mb-6>问 Claude 你会问资深工程师的问题</div>

<div grid grid-cols-2 gap-6>
  <div
    v-click="1"
    border="2 solid blue-800/50" rounded-lg
    transition duration-500 ease-in-out
    :class="$clicks < 1 ? 'opacity-0 translate-x--10' : 'opacity-100 translate-x-0'"
  >
    <div flex items-center bg="blue-800/30" px-3 py-2 text-blue-300>
      <div i-carbon:chat text-sm mr-1 />
      <div text-xs><em>直接提问</em></div>
    </div>
    <div bg="blue-800/10" px-4 py-3 text-sm class="text-white/70">
      <div>"日志如何工作？"</div>
      <div>"如何创建新的 API 端点？"</div>
      <div>"这段代码为什么用 foo() 而不是 bar()？"</div>
      <div mt-2 class="text-white/50 text-xs">有效的入职工作流，减少对其他工程师的负担</div>
    </div>
  </div>
  <div
    v-click="2"
    border="2 solid purple-800/50" rounded-lg
    transition duration-500 ease-in-out
    :class="$clicks < 2 ? 'opacity-0 translate-x-10' : 'opacity-100 translate-x-0'"
  >
    <div flex items-center bg="purple-800/30" px-3 py-2 text-purple-300>
      <div i-carbon:microphone text-sm mr-1 />
      <div text-xs><em>让 Claude 采访你</em></div>
    </div>
    <div bg="purple-800/10" px-4 py-3 text-sm class="text-white/70">
      <div mb-2>对于更大功能，让 Claude 先采访你</div>
      <div class="text-white/50 text-xs">Claude 会问技术实现、UI/UX、边界情况和权衡</div>
      <div mt-2>完成后启动<strong text-white>新会话</strong>来执行</div>
    </div>
  </div>
</div>

---
class: py-8
glowSeed: 1520
---

<div text-2xl font-bold mb-4>采访提示词模板</div>

```text
I want to build [brief description].
Interview me in detail using the AskUserQuestion tool.

Ask about technical implementation, UI/UX, edge cases,
concerns, and tradeoffs. Don't ask obvious questions,
dig into the hard parts I might not have considered.

Keep interviewing until we've covered everything,
then write a complete spec to SPEC.md.
```

<div mt-6 text-sm class="text-white/40">
  一旦规范完成，启动新会话来执行 — 新会话有干净的 context，完全专注于实现
</div>

---
layout: section
glowSeed: 1600
---

# 06
管理你的会话

---
class: py-8
clicks: 4
glowSeed: 1700
---

<div text-3xl font-bold mb-2>会话管理技巧</div>
<div class="text-white/50" mb-6>对话是持久的和可逆的，充分利用这一点</div>

<div grid grid-cols-2 gap-4>
<v-clicks>

<div border="2 solid orange-800/50" rounded-lg bg="orange-800/10">
  <div flex items-center bg="orange-800/30" px-3 py-2 text-orange-300>
    <div i-carbon:undo text-sm mr-1 />
    <div text-xs><em>尽早改正方向</em></div>
  </div>
  <div bg="orange-800/10" px-4 py-3 text-xs class="text-white/60">
    <div><kbd bg="white/10" px-1 rounded>Esc</kbd> 停止 Claude</div>
    <div><kbd bg="white/10" px-1 rounded>Esc+Esc</kbd> 或 <kbd bg="white/10" px-1 rounded>/rewind</kbd> 回退</div>
    <div>两次改正后 /clear 重新开始</div>
  </div>
</div>

<div border="2 solid teal-800/50" rounded-lg bg="teal-800/10">
  <div flex items-center bg="teal-800/30" px-3 py-2 text-teal-300>
    <div i-carbon:clean text-sm mr-1 />
    <div text-xs><em>积极管理 Context</em></div>
  </div>
  <div bg="teal-800/10" px-4 py-3 text-xs class="text-white/60">
    <div>不相关任务间 /clear</div>
    <div>/compact 自定义压缩</div>
    <div>/btw 快速问题不进历史</div>
  </div>
</div>

<div border="2 solid indigo-800/50" rounded-lg bg="indigo-800/10">
  <div flex items-center bg="indigo-800/30" px-3 py-2 text-indigo-300>
    <div i-carbon:bot text-sm mr-1 />
    <div text-xs><em>Subagents 调查</em></div>
  </div>
  <div bg="indigo-800/10" px-4 py-3 text-xs class="text-white/60">
    <div>委托研究到独立 context</div>
    <div>探索不消耗主对话</div>
    <div>实现后验证代码</div>
  </div>
</div>

<div border="2 solid pink-800/50" rounded-lg bg="pink-800/10">
  <div flex items-center bg="pink-800/30" px-3 py-2 text-pink-300>
    <div i-carbon:checkpoint text-sm mr-1 />
    <div text-xs><em>检查点 Rewind</em></div>
  </div>
  <div bg="pink-800/10" px-4 py-3 text-xs class="text-white/60">
    <div>每个操作自动创建检查点</div>
    <div>恢复对话、代码或两者</div>
    <div>可以尝试冒险，不行就回退</div>
  </div>
</div>

</v-clicks>
</div>

---
class: py-10
glowSeed: 1720
---

<div text-2xl font-bold mb-4>恢复对话</div>

<div class="text-white/50" mb-6>
  Claude Code 在本地保存对话，任务跨越多个会话不必重新解释
</div>

```bash
claude --continue    # 恢复最近的对话
claude --resume      # 从最近的会话中选择
```

<div mt-6 text-sm class="text-white/40">
  使用 /rename 给会话起描述性名称，如 "oauth-migration"。像对待分支一样对待会话
</div>

---
class: py-8
glowSeed: 1740
---

<div text-2xl font-bold mb-4>Context 管理速查</div>

<div grid grid-cols-2 gap-4 mt-6>

<div flex gap-4 border="2 solid violet-800/30" rounded-lg bg="violet-900/10" px-4 py-3>
  <div w-24 shrink-0>
    <div text-sm font-mono font-bold text-violet-300>/clear</div>
  </div>
  <div flex-1 text-sm class="text-white/70">
    完全重置 context，不相关任务间使用
  </div>
</div>

<div flex gap-4 border="2 solid blue-800/30" rounded-lg bg="blue-900/10" px-4 py-3>
  <div w-24 shrink-0>
    <div text-sm font-mono font-bold text-blue-300>/compact</div>
  </div>
  <div flex-1 text-sm class="text-white/70">
    自定义压缩，如 /compact Focus on the API changes
  </div>
</div>

<div flex gap-4 border="2 solid green-800/30" rounded-lg bg="green-900/10" px-4 py-3>
  <div w-24 shrink-0>
    <div text-sm font-mono font-bold text-green-300>/rewind</div>
  </div>
  <div flex-1 text-sm class="text-white/70">
    回退到之前的检查点，恢复对话或代码
  </div>
</div>

<div flex gap-4 border="2 solid amber-800/30" rounded-lg bg="amber-900/10" px-4 py-3>
  <div w-24 shrink-0>
    <div text-sm font-mono font-bold text-amber-300>/btw</div>
  </div>
  <div flex-1 text-sm class="text-white/70">
    快速问题不进入历史，不增加 context
  </div>
</div>

</div>

---
layout: section
glowSeed: 1800
---

# 07
自动化与扩展

---
class: flex justify-center items-center gap-20 px-40 text-xl
glowSeed: 1850
---

<div
  absolute text-5xl
  :class="$clicks < 1 ? 'text-white' : 'translate-y--18 scale-40 text-white/30'"
  transition duration-500 ease-in-out
>
  <span>如何从一对一到一对多？</span>
</div>

<div flex flex-col items-center>
  <v-clicks>
    <div mt-4>
      <h1 flex items-center text="4xl!">
        <span>并行会话 + 非交互模式 + 扇出</span>
      </h1>
    </div>
  </v-clicks>
</div>

---
class: py-10
glowSeed: 1900
---

<div text-2xl font-bold mb-4>非交互模式</div>

<div class="text-white/50" mb-4>CI、pre-commit hooks 或脚本中使用</div>

```bash
# 一次性查询
claude -p "Explain what this project does"

# 结构化输出（脚本用）
claude -p "List all API endpoints" --output-format json

# 流式输出（实时处理）
claude -p "Analyze this log file" --output-format stream-json

# Auto mode 自主运行
claude --permission-mode auto -p "fix all lint errors"
```

<div mt-4 text-sm class="text-white/40">
  --allowedTools 限制权限：--allowedTools "Edit,Bash(git commit *)"
</div>

---
class: py-10
clicks: 3
glowSeed: 1950
glow: left
---

<div text-2xl font-bold mb-4>三种并行会话方式</div>

<div grid grid-cols-3 gap-5>
  <div
    v-click="1"
    border="2 solid violet-800/50" rounded-lg
    transition duration-500 ease-in-out
    :class="$clicks < 1 ? 'opacity-0 translate-y-10' : 'opacity-100 translate-y-0'"
  >
    <div flex items-center bg="violet-800/30" px-3 py-2 text-violet-300>
      <div i-carbon:desktop text-sm mr-1 />
      <div text-xs><em>桌面应用</em></div>
    </div>
    <div bg="violet-800/10" px-4 py-3 text-xs class="text-white/60">
      <div mb-1>视觉化管理多个本地会话</div>
      <div>每个会话隔离 worktree</div>
    </div>
  </div>
  <div
    v-click="2"
    border="2 solid blue-800/50" rounded-lg
    transition duration-500 ease-in-out
    :class="$clicks < 2 ? 'opacity-0 translate-y-10' : 'opacity-100 translate-y-0'"
  >
    <div flex items-center bg="blue-800/30" px-3 py-2 text-blue-300>
      <div i-carbon:cloud text-sm mr-1 />
      <div text-xs><em>Web 版</em></div>
    </div>
    <div bg="blue-800/10" px-4 py-3 text-xs class="text-white/60">
      <div mb-1>Anthropic 安全云基础设施</div>
      <div>隔离 VM 上运行</div>
    </div>
  </div>
  <div
    v-click="3"
    border="2 solid green-800/50" rounded-lg
    transition duration-500 ease-in-out
    :class="$clicks < 3 ? 'opacity-0 translate-y-10' : 'opacity-100 translate-y-0'"
  >
    <div flex items-center bg="green-800/30" px-3 py-2 text-green-300>
      <div i-carbon:group text-sm mr-1 />
      <div text-xs><em>Agent Teams</em></div>
    </div>
    <div bg="green-800/10" px-4 py-3 text-xs class="text-white/60">
      <div mb-1>多个会话自动协调</div>
      <div>共享任务、消息和团队主管</div>
    </div>
  </div>
</div>

---
class: py-10
glowSeed: 1960
---

<div text-2xl font-bold mb-4>Writer/Reviewer 模式</div>

<div class="text-white/50" mb-4>新鲜 context 改进了代码审查 — Claude 不会偏向刚写的代码</div>

<div grid grid-cols-2 gap-8 mt-6>
  <div class="border-2 border-cyan-500/30 rounded-lg p-5 bg-cyan-500/10">
    <div text-xl font-bold mb-4 text-cyan-300>会话 A（Writer）</div>
    <div text-sm class="text-white/70">
      <div mb-3>"为我们的 API 端点实现速率限制器"</div>
      <div mb-3>...编写代码...</div>
      <div>"这是审查反馈：[会话 B 输出]。解决这些问题。"</div>
    </div>
  </div>
  <div class="border-2 border-green-500/30 rounded-lg p-5 bg-green-500/10">
    <div text-xl font-bold mb-4 text-green-300>会话 B（Reviewer）</div>
    <div text-sm class="text-white/70">
      <div>"审查 @src/middleware/rateLimiter.ts 中的速率限制器实现"</div>
      <div mt-2 class="text-white/50">查找边界情况、竞态条件和与现有中间件模式的一致性</div>
    </div>
  </div>
</div>

---
class: py-8
glowSeed: 1970
---

<div text-2xl font-bold mb-4>跨文件扇出模式</div>

<div grid grid-cols-5 gap-4 mt-4>

<div
  rounded-lg
  border="2 solid violet-900" bg="violet-900/20"
  backdrop-blur flex-1
>
  <div px-5 py-6 flex items-center justify-center>
    <div i-carbon:list text-3xl text-violet-400 />
  </div>
  <div bg="violet-900/30" w-full px-3 py-2 flex items-center justify-center text-center>
    <span text-xs>生成任务列表</span>
  </div>
</div>

<div text-2xl class="opacity-30" flex items-center justify-center>→</div>

<div
  rounded-lg
  border="2 solid blue-800" bg="blue-800/20"
  backdrop-blur flex-1
>
  <div px-5 py-6 flex items-center justify-center>
    <div i-carbon:script text-3xl text-blue-400 />
  </div>
  <div bg="blue-800/30" w-full px-3 py-2 flex items-center justify-center text-center>
    <span text-xs>编写循环脚本</span>
  </div>
</div>

<div text-2xl class="opacity-30" flex items-center justify-center>→</div>

<div
  rounded-lg
  border="2 solid green-800" bg="green-800/20"
  backdrop-blur flex-1
>
  <div px-5 py-6 flex items-center justify-center>
    <div i-carbon:rocket text-3xl text-green-400 />
  </div>
  <div bg="green-800/30" w-full px-3 py-2 flex items-center justify-center text-center>
    <span text-xs>测试后大规模运行</span>
  </div>
</div>

</div>

<div mt-6>

```bash
for file in $(cat files.txt); do
  claude -p "Migrate $file from React to Vue. Return OK or FAIL." \
    --allowedTools "Edit,Bash(git commit *)"
done
```

</div>

---
class: py-8
clicks: 5
glowSeed: 2000
glow: right
---

<div text-3xl font-bold mb-2>常见失败模式</div>
<div class="text-white/50" mb-4>尽早识别这些错误可以节省大量时间</div>

<div grid grid-cols-1 gap-3>
<v-clicks>

<div flex items-center gap-4 border="2 solid red-800/30" rounded-lg bg="red-800/10" px-4 py-3>
  <div i-carbon:warning text-2xl text-red-400 />
  <div flex-1>
    <div font-bold text-sm text-red-300>厨房水槽会话</div>
    <div text-xs class="text-white/50">任务间混杂无关信息 → 不相关任务之间 /clear</div>
  </div>
</div>

<div flex items-center gap-4 border="2 solid orange-800/30" rounded-lg bg="orange-800/10" px-4 py-3>
  <div i-carbon:repeat text-2xl text-orange-400 />
  <div flex-1>
    <div font-bold text-sm text-orange-300>一次又一次地改正</div>
    <div text-xs class="text-white/50">Context 被失败方法污染 → 两次失败后 /clear 重写提示</div>
  </div>
</div>

<div flex items-center gap-4 border="2 solid yellow-800/30" rounded-lg bg="yellow-800/10" px-4 py-3>
  <div i-carbon:document text-2xl text-yellow-400 />
  <div flex-1>
    <div font-bold text-sm text-yellow-300>过度指定的 CLAUDE.md</div>
    <div text-xs class="text-white/50">太长导致 Claude 忽略一半 → 无情修剪，转为 hook</div>
  </div>
</div>

<div flex items-center gap-4 border="2 solid amber-800/30" rounded-lg bg="amber-800/10" px-4 py-3>
  <div i-carbon:security text-2xl text-amber-400 />
  <div flex-1>
    <div font-bold text-sm text-amber-300>信任然后验证的差距</div>
    <div text-xs class="text-white/50">看起来合理但不处理边界 → 始终提供验证</div>
  </div>
</div>

<div flex items-center gap-4 border="2 solid pink-800/30" rounded-lg bg="pink-800/10" px-4 py-3>
  <div i-carbon:search text-2xl text-pink-400 />
  <div flex-1>
    <div font-bold text-sm text-pink-300>无限探索</div>
    <div text-xs class="text-white/50">读取数百个文件填充 context → 狭窄限定或用 subagents</div>
  </div>
</div>

</v-clicks>
</div>

---
class: py-10
glowSeed: 2050
---

<div text-2xl font-bold mb-6>Plugins — 扩展生态</div>

<div class="text-white/50" mb-6>
  运行 /plugin 浏览市场。Plugins 将 skills、hooks、subagents 和 MCP 捆绑为单个可安装单元
</div>

<div grid grid-cols-2 gap-5>
  <div border="2 solid violet-800/50" rounded-lg bg="violet-800/10" px-4 py-4>
    <div flex items-center gap-2 mb-2>
      <div i-carbon:integration text-xl text-violet-300 />
      <div font-bold text-sm text-violet-300>代码智能 Plugin</div>
    </div>
    <div text-xs class="text-white/60">
      为 Claude 提供精确的符号导航和编辑后的自动错误检测。类型化语言推荐安装
    </div>
  </div>
  <div border="2 solid blue-800/50" rounded-lg bg="blue-800/10" px-4 py-4>
    <div flex items-center gap-2 mb-2>
      <div i-carbon:store text-xl text-blue-300 />
      <div font-bold text-sm text-blue-300>社区与官方 Plugin</div>
    </div>
    <div text-xs class="text-white/60">
      添加 skills、工具和集成，无需配置。来自社区和 Anthropic 的可安装单元
    </div>
  </div>
</div>

---
layout: center
glowSeed: 2100
---

<div flex flex-col items-center max-w-150>
  <div i-carbon:idea text-5xl text-amber-400 mb-6 />
  <div text-3xl font-bold mb-6>培养你的直觉</div>
  <div text-lg class="text-white/60" text-center leading-relaxed mb-8>
    注意什么有效。当 Claude 产生很好的输出时，注意你做了什么。
    <br>
    当 Claude 遇到困难时，问为什么。
  </div>
  <div grid grid-cols-2 gap-4 w-full>
    <div border="2 solid green-800/50" rounded-lg bg="green-800/10" px-4 py-3 text-center>
      <div text-sm text-green-300 font-bold mb-1>何时具体</div>
      <div text-xs class="text-white/50">明确任务、精确指令</div>
    </div>
    <div border="2 solid blue-800/50" rounded-lg bg="blue-800/10" px-4 py-3 text-center>
      <div text-sm text-blue-300 font-bold mb-1>何时开放</div>
      <div text-xs class="text-white/50">探索性问题、发现意外</div>
    </div>
    <div border="2 solid violet-800/50" rounded-lg bg="violet-800/10" px-4 py-3 text-center>
      <div text-sm text-violet-300 font-bold mb-1>何时规划</div>
      <div text-xs class="text-white/50">多文件修改、不确定方案</div>
    </div>
    <div border="2 solid amber-800/50" rounded-lg bg="amber-800/10" px-4 py-3 text-center>
      <div text-sm text-amber-300 font-bold mb-1>何时清除</div>
      <div text-xs class="text-white/50">任务切换、累积改正</div>
    </div>
  </div>
</div>

---
class: py-10
clicks: 3
glowSeed: 2200
---

<div text-2xl font-bold mb-6>常见问题</div>

<div mt-4 flex flex-col gap-5>

<div
  v-click="1"
  transition duration-300
  border="2 solid violet-800/50"
  rounded-lg bg="violet-900/10" px-5 py-4
  :class="$clicks < 1 ? 'opacity-0' : 'opacity-100'"
>
  <div font-bold text-violet-300>Q: CLAUDE.md 应该多长？</div>
  <div text-sm mt-2 class="text-white/70">A: 保持简洁。对每一行问自己："删除这个会导致 Claude 犯错吗？"如果不会，删除它。膨胀的 CLAUDE.md 会导致 Claude 忽略你的实际指令。</div>
</div>

<div
  v-click="2"
  transition duration-300
  border="2 solid blue-800/50"
  rounded-lg bg="blue-900/10" px-5 py-4
  :class="$clicks < 2 ? 'opacity-0' : 'opacity-100'"
>
  <div font-bold text-blue-300>Q: 如何让 Claude 遵守规则？</div>
  <div text-sm mt-2 class="text-white/70">A: 通过添加强调（如 "IMPORTANT" 或 "YOU MUST"）来改进遵守。将文件检入 git，团队可以贡献。像对待代码一样对待 CLAUDE.md。</div>
</div>

<div
  v-click="3"
  transition duration-300
  border="2 solid green-800/50"
  rounded-lg bg="green-900/10" px-5 py-4
  :class="$clicks < 3 ? 'opacity-0' : 'opacity-100'"
>
  <div font-bold text-green-300>Q: 什么时候用 subagents？</div>
  <div text-sm mt-2 class="text-white/70">A: 当 Claude 需要研究代码库时。Subagents 在单独 context 中运行，不会消耗主对话。使用 "use subagents to investigate X" 委托。</div>
</div>

</div>

---
layout: fact
glowSeed: 2250
---

## Context Window

最重要的事：context 是你的基本约束

一切模式都围绕它展开

---
layout: statement
glowSeed: 2300
---

## 先探索、再规划、后编码

验证 > 假设

---
class: py-10
glowSeed: 2350
---

<div text-2xl font-bold mb-6>相关资源</div>

<div grid grid-cols-2 gap-5 mt-4>
  <div border="2 solid violet-800/50" rounded-lg bg="violet-800/10" px-4 py-4>
    <div flex items-center gap-2 mb-2>
      <div i-carbon:document text-lg text-violet-300 />
      <div font-bold text-sm text-violet-300>Claude Code 如何工作</div>
    </div>
    <div text-xs class="text-white/50">代理循环、工具和 context 管理</div>
  </div>
  <div border="2 solid blue-800/50" rounded-lg bg="blue-800/10" px-4 py-4>
    <div flex items-center gap-2 mb-2>
      <div i-carbon:puzzle text-lg text-blue-300 />
      <div font-bold text-sm text-blue-300>扩展 Claude Code</div>
    </div>
    <div text-xs class="text-white/50">skills、hooks、MCP、subagents 和 plugins</div>
  </div>
  <div border="2 solid green-800/50" rounded-lg bg="green-800/10" px-4 py-4>
    <div flex items-center gap-2 mb-2>
      <div i-carbon:flow text-lg text-green-300 />
      <div font-bold text-sm text-green-300>常见工作流</div>
    </div>
    <div text-xs class="text-white/50">调试、测试、PR 等的分步配方</div>
  </div>
  <div border="2 solid amber-800/50" rounded-lg bg="amber-800/10" px-4 py-4>
    <div flex items-center gap-2 mb-2>
      <div i-carbon:memory text-lg text-amber-300 />
      <div font-bold text-sm text-amber-300>CLAUDE.md</div>
    </div>
    <div text-xs class="text-white/50">存储项目约定和持久 context</div>
  </div>
</div>

---
layout: end
glowSeed: 2400
---

感谢观看

<div class="text-sm opacity-50 mt-4">
  Claude Code 最佳实践 · Anthropic 官方推荐模式
</div>
