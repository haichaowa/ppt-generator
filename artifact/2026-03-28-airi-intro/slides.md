---
layout: center
highlighter: shiki
css: unocss
colorSchema: dark
transition: fade-out
title: 'Project AIRI：从小众 side project 到 GitHub 万星的开源之旅'
exportFilename: project-airi-introduction
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

<div translate-x--14 translate-y-10>

<h1>
Project AIRI<br />从小众 side project 到 GitHub 万星的开源之旅
</h1>

Behind the scenes of developing an AI VTuber project

<div mt-8 flex items-center gap-3>
  <img src="/person/neko.jpeg" w-12 h-12 rounded-full object-cover />
  <span class="text-white/50">奶扣 Neko</span>
</div>

</div>

---
layout: intro
class: px-35
glowSeed: 128
---

<div flex items-center gap-3>
  <div
    v-click="1"
    :class="$clicks < 1 ? 'translate-x--5 opacity-0' : 'translate-x-0 opacity-100'"
    flex flex-col items-start transition duration-500 ease-in-out min-w-60
  >
    <img src="/person/neko.jpeg" w-40 h-40 rounded-full object-cover mb-5>
    <span font-semibold text-3xl>Neko</span>
    <div>
      <div>
        <span class="opacity-70">Full-stack Developer</span>
      </div>
      <div text-sm flex items-center gap-2 mt-4>
        <div i-ri:github-fill /><span underline decoration-dashed font-mono decoration-zinc-300>nekomeowww</span>
      </div>
    </div>
  </div>
  <div flex-1 />
  <div flex flex-col gap-8>
    <div mb-4 v-click="2">
      <div mb-4 text-zinc-400>
        <span>社区</span>
      </div>
      <div
        flex flex-wrap items-start content-start gap-4 transition duration-500 ease-in-out
        :class="$clicks < 2 ? 'translate-y-5' : 'translate-y-0'"
      >
        <div flex items-center gap-2 text-2xl w-fit h-fit>
          <img src="/proj-airi-logo.svg" size="6.5" >
          <div>Project AIRI</div>
        </div>
        <div flex items-center gap-2 text-2xl w-fit h-fit>
          <div i-logos:hugging-face-icon inline-block /> Hugging Face
        </div>
        <div flex items-center gap-2 text-2xl w-fit h-fit>
          <div i-logos:vue /><div>Vue</div>
        </div>
        <div flex items-center gap-2 text-2xl w-fit h-fit>
          <div i-simple-icons:ollama inline-block /> Ollama
        </div>
      </div>
    </div>
    <div v-click="3">
      <div mb-4 text-zinc-400>
        <span>其他项目</span>
      </div>
      <div
        flex flex-wrap items-start content-start gap-4 transition duration-500 ease-in-out
        :class="$clicks < 3 ? 'translate-y-5' : 'translate-y-0'"
      >
        <div flex items-center gap-2 text-2xl w-fit h-fit>
          <img src="/moeru-ai-logo.png" size="6.5" />
          <div>Moeru AI</div>
        </div>
      </div>
    </div>
  </div>
</div>

---
title: 往期分享
glowSeed: 203
---

<div>
  <div grid="~ cols-2" gap-4>
    <div
      relative
      class="[&_.qr]:hover:opacity-100 [&_.img]:hover:opacity-50 hover:cursor-pointer hover:grayscale-100"
      rounded-lg overflow-hidden bg="black" h-fit
      transition="all duration-250 ease-in-out"
    >
      <img src="/session-1.png" class="img" opacity-100 transition="all duration-250 ease-in-out">
      <img src="/session-1-qr.png" class="qr" w-60 absolute top-0 left-0 translate-x="[40%]" opacity-0 transition="all duration-250 ease-in-out">
    </div>
    <div
      relative
      class="[&_.qr]:hover:opacity-100 [&_.img]:hover:opacity-50 hover:cursor-pointer hover:grayscale-100"
      rounded-lg overflow-hidden bg="black" h-fit
      transition="all duration-250 ease-in-out"
    >
      <img src="/session-2.png" class="img" opacity-100 transition="all duration-250 ease-in-out">
      <img src="/session-2-qr.png" class="qr" w-60 absolute top-0 left-0 translate-x="[40%]" opacity-0 transition="all duration-250 ease-in-out">
    </div>
    <div
      relative
      class="[&_.qr]:hover:opacity-100 [&_.img]:hover:opacity-50 hover:cursor-pointer hover:grayscale-100"
      rounded-lg overflow-hidden bg="black" h-fit
      transition="all duration-250 ease-in-out"
    >
      <img src="/session-3.png" class="img" opacity-100 transition="all duration-250 ease-in-out">
      <img src="/session-3-qr.png" class="qr" w-60 absolute top-0 left-0 translate-x="[40%]" opacity-0 transition="all duration-250 ease-in-out">
    </div>
    <div
      relative
      class="[&_.qr]:hover:opacity-100 [&_.img]:hover:opacity-50 hover:cursor-pointer hover:grayscale-100"
      rounded-lg overflow-hidden bg="black" h-fit
      transition="all duration-250 ease-in-out"
    >
      <img src="/session-4.png" class="img" opacity-100 transition="all duration-250 ease-in-out">
      <img src="/session-4-qr.png" class="qr" w-60 absolute top-0 left-0 translate-x="[40%]" opacity-0 transition="all duration-250 ease-in-out">
    </div>
  </div>
</div>

---
class: py-10 text-center
---

<h1 font-rounded>
Project AIRI
</h1>

尝试重现 Neuro-sama，可以看作是装载 AI 角色的灵魂容器

<img src="/airi-screenshot-2.png" w-full rounded-xl />

---
class: py-10 relative text-center
---

<h1 font-rounded>
Project AIRI
</h1>

<img src="/airi-github_qr.png" w-50 absolute bottom-3 />

<img src="/airi-screenshot-1.png" w-full />

---
class: py-10 text-center
---

<h1 font-rounded>
我们有超过 15200 颗星星
</h1>

<img src="/airi-stars.png" w-full rounded-xl />

---
layout: section
glowSeed: 400
---

# 01

AIRI 是什么

---
class: flex justify-center items-center gap-20 px-40 text-xl
---

<div
  absolute text-6xl
  :class="$clicks < 1 ? 'text-white' : 'translate-y--18 scale-40 text-white/30'"
  transition duration-500 ease-in-out
>
  <span>AI 主播？</span>
</div>

<div flex flex-col items-center>
  <v-clicks>
    <div mt-4>
      <h1 flex items-center text="5xl!">
        <span>就是带货的那种数字人对吗？</span>
      </h1>
    </div>
  </v-clicks>
</div>

---
class: flex justify-center items-center gap-20 px-40 text-xl
---

<div
  absolute text-6xl
  :class="$clicks < 1 ? 'text-white' : 'translate-y--18 scale-40 text-white/30'"
  transition duration-500 ease-in-out
>
  <span>Neuro-sama 又是什么？</span>
</div>

---
class: py-10
clicks: 5
---

# 目前的效果

<span>确实是工程落地了一部分</span>

<div mt-10 />

<div flex items-center gap-4>

<v-clicks>

<div
  :class="$clicks < 1 ? 'translate-x--20 opacity-0' : 'translate-x-0 opacity-100'"
  rounded-lg
  border="2 solid green-800" bg="green-800/20"
  backdrop-blur
  flex-1 h-full
  transition duration-500 ease-in-out
>
  <div px-5 py-16 flex items-center justify-center>
    <div i-solar:database-bold-duotone size-20 />
  </div>
  <div bg="green-800/30" w-full px-4 py-2 h="5rem" flex items-center justify-center text-center text-base>
    <span>仿生记忆层</span>
  </div>
</div>

<div
  :class="$clicks < 2 ? 'translate-x--20 opacity-0' : 'translate-x-0 opacity-100'"
  rounded-lg
  border="2 solid emerald-800" bg="emerald-800/20"
  backdrop-blur
  flex-1 h-full
  transition duration-500 ease-in-out
>
  <div px-5 py-16 flex items-center justify-center>
    <div i-solar:microphone-3-bold-duotone size-20 />
  </div>
  <div bg="emerald-800/30" w-full px-4 py-2 h="5rem" flex items-center justify-center text-center text-base>
    <span>实时语音流水线</span>
  </div>
</div>

<div
  :class="$clicks < 3 ? 'translate-x--20 opacity-0' : 'translate-x-0 opacity-100'"
  rounded-lg
  border="2 solid teal-800" bg="teal-800/20"
  backdrop-blur
  flex-1 h-full
  transition duration-500 ease-in-out
>
  <div px-5 py-16 flex items-center justify-center>
    <div i-solar:gamepad-minimalistic-bold-duotone size-20 />
  </div>
  <div bg="teal-800/30" w-full px-4 py-2 h="5rem" flex items-center justify-center text-center>
    <span>游戏陪玩</span>
  </div>
</div>

<div
  :class="$clicks < 4 ? 'translate-x--20 opacity-0' : 'translate-x-0 opacity-100'"
  rounded-lg
  border="2 solid cyan-800" bg="cyan-800/20"
  backdrop-blur
  flex-1 h-full
  transition duration-500 ease-in-out
>
  <div px-5 py-16 flex items-center justify-center>
    <div i-solar:face-scan-square-bold-duotone size-20 />
  </div>
  <div bg="cyan-800/30" w-full px-4 py-2 h="5rem" flex items-center justify-center text-center text-base>
    <span>表情与动作</span>
  </div>
</div>

<div
  :class="$clicks < 5 ? 'translate-x--20 opacity-0' : 'translate-x-0 opacity-100'"
  rounded-lg
  border="2 solid sky-800" bg="sky-800/20"
  backdrop-blur
  flex-1 h-full
  transition duration-500 ease-in-out
>
  <div px-5 py-16 flex items-center justify-center>
    <div i-solar:link-circle-line-duotone size-20 />
  </div>
  <div bg="sky-800/30" w-full px-4 py-2 h="5rem" flex items-center justify-center text-center>
    <span>MCP & A2A</span>
  </div>
</div>

</v-clicks>

</div>

---
layout: section
glowSeed: 550
---

# 02

看看效果

---
class: px-0! pt-6!
---

<div px-10 text-4xl mb-4>
  一起玩 我的世界 Minecraft
</div>

<video autoplay muted>
  <source src="/airi-plays-minecraft.mp4" />
</video>

---
class: px-0! pt-6!
---

<div px-10 text-4xl mb-4>
  一起玩 异星工厂 Factorio
</div>

<video autoplay muted>
  <source src="/airi-plays-factorio.mp4" />
</video>

---
class: px-0! pt-6!
---

<div px-10 text-4xl mb-4>
  一起玩小丑牌 Balatro
</div>

<video autoplay muted>
  <source src="/airi-plays-balatro.mp4" />
</video>

---
class: px-0! pt-6!
---

<div px-10 text-4xl mb-4>
  AIRI 操作 ADB 控制设备
</div>

<video autoplay muted>
  <source src="/airi-browses-x.mp4" />
</video>

---
layout: section
glowSeed: 650
---

# 03

技术挑战

---
class: py-10
glowSeed: 100
clicks: 3
---

# 事情远比想象的复杂

<span>为什么没那么简单？</span>

<div mt-6 />

<div flex flex-col gap-4>

<v-clicks>

<div border="2 solid teal-800/50" rounded-lg>
  <div flex items-center bg="teal-800/30" px-3 py-2 text-teal-300>
    <div i-carbon:web-services-container text-sm mr-1 />
    <div text-xs><em>记忆系统的挑战</em></div>
  </div>
  <div bg="teal-800/10" px-4 py-3>
    <div text-sm>记忆层不是 RAG 就结束了，还要考虑遗忘曲线和情绪</div>
    <div text-xs flex gap-2 mt-1 text-zinc-400>
      <span>目前的方案都是纯粹面向 RAG</span>
      <span>没有遗忘曲线和情绪化能力</span>
    </div>
  </div>
</div>

<div border="2 solid cyan-800/50" rounded-lg>
  <div flex items-center bg="cyan-800/30" px-3 py-2 text-cyan-300>
    <div i-carbon:sysplex-distributor text-sm mr-1 />
    <div text-xs><em>多模态交互</em></div>
  </div>
  <div bg="cyan-800/10" px-4 py-3>
    <div text-sm>实时语音、身体控制、视觉和游戏能力需要多流水线衔接</div>
    <div text-xs flex gap-2 mt-1 text-zinc-400>
      <span>端到端可定制化程度低</span>
      <span>需要潜心优化延迟</span>
    </div>
  </div>
</div>

<div border="2 solid sky-800/50" rounded-lg>
  <div flex items-center bg="sky-800/30" px-3 py-2 text-sky-300>
    <div i-carbon:name-space text-sm mr-1 />
    <div text-xs><em>工程化也是难题</em></div>
  </div>
  <div bg="sky-800/10" px-4 py-3>
    <div text-sm>系统模块多，工程化难度比 CRUD 高</div>
    <div text-xs flex gap-2 mt-1 text-zinc-400>
      <span>提示词和角色卡是分裂的生态</span>
      <span>有状态 Agent 全部靠回调</span>
    </div>
  </div>
</div>

</v-clicks>

</div>

---
layout: section
glowSeed: 700
---

# 04

生态与成长

---
class: py-10
---

# 部分形成生态

我们尽最大努力让大家都可以用上先进的工具和工作流

<div mt-6 />

<div grid grid-cols-2 gap-3>

<div border="2 solid green-800/50" rounded-lg bg="green-900/10" px-4 py-3>
  <div font-bold mb-1 text-green-300 text-sm>xsAI</div>
  <div text-xs opacity-70>Vercel AI SDK 替代品，超迷你可扩展</div>
</div>

<div border="2 solid emerald-800/50" rounded-lg bg="emerald-900/10" px-4 py-3>
  <div font-bold mb-1 text-emerald-300 text-sm>Velin</div>
  <div text-xs opacity-70>用 Vue 或 JSX 书写提示词</div>
</div>

<div border="2 solid teal-800/50" rounded-lg bg="teal-900/10" px-4 py-3>
  <div font-bold mb-1 text-teal-300 text-sm>unspeech</div>
  <div text-xs opacity-70>语音界 LiteLLM，代理 TTS/STT 云服务</div>
</div>

<div border="2 solid cyan-800/50" rounded-lg bg="cyan-900/10" px-4 py-3>
  <div font-bold mb-1 text-cyan-300 text-sm>ortts</div>
  <div text-xs opacity-70>语音合成推理引擎</div>
</div>

<div border="2 solid sky-800/50" rounded-lg bg="sky-900/10" px-4 py-3>
  <div font-bold mb-1 text-sky-300 text-sm>AIRI + Factorio</div>
  <div text-xs opacity-70>让 AIRI 玩 Factorio</div>
</div>

<div border="2 solid blue-800/50" rounded-lg bg="blue-900/10" px-4 py-3>
  <div font-bold mb-1 text-blue-300 text-sm>AIRI + Balatro</div>
  <div text-xs opacity-70>让 AIRI 玩小丑牌</div>
</div>

<div border="2 solid indigo-800/50" rounded-lg bg="indigo-900/10" px-4 py-3>
  <div font-bold mb-1 text-indigo-300 text-sm>MikuMikuDance + Three.js</div>
  <div text-xs opacity-70>3D 角色渲染和动作生成</div>
</div>

<div border="2 solid violet-800/50" rounded-lg bg="violet-900/10" px-4 py-3>
  <div font-bold mb-1 text-violet-300 text-sm>eventa</div>
  <div text-xs opacity-70>事件调度库</div>
</div>

</div>

---
layout: center
class: py-20 flex flex-col items-center gap-10
---

<div flex flex-col items-center gap-5>

<img src="/moeru-ai-followers.png" w="[calc(100%-20%)]" rounded-xl />
<img src="/proj-airi-followers.png" w="[calc(100%-20%)]" rounded-xl />

</div>

---
class: py-10 text-center
---

# 获得星星

<img src="/star-growth.png" w="[calc(100%-20%)]" rounded-xl />

---
layout: section
glowSeed: 800
---

# 05

加入我们

---
class: py-10
glowSeed: 1298
---

# 感兴趣吗？

虽然是开源项目，也欢迎设计师、产品经理、工程师们一起实现

<div flex>
  <div text-sm text="zinc-300" text-right flex flex-row gap-2 mt-6 translate-x-2>
    <div flex items-center flex-col font-bold text-xl>
      <img src="/github_qr.png" w-70 />
      <div translate-y--4>GitHub</div>
    </div>
    <div flex items-center flex-col font-bold text-xl>
      <img src="/discord_qr.png" w-70 style="filter: brightness(1.5);" />
      <div translate-y--4>Discord</div>
    </div>
    <div flex items-center flex-col font-bold text-xl>
      <img src="/telegram_qr.png" w-70 style="filter: brightness(1.5);" />
      <div translate-y--4>Telegram</div>
    </div>
  </div>
</div>

---
title: Thank you
class: py-10
glowSeed: 230
---

<div flex>
  <div flex-1>
    <div mt-50 />
    <div flex flex-col gap-4 translate="y--52" h-full>
      <div flex flex-col translate="y-4" flex-1>
        <div text="[48px]">
          谢谢
        </div>
        <div class="text-white/50">
          Thank you
        </div>
      </div>
      <img src="/relu-art-6.gif" size-50 rounded-2xl overflow-hidden translate-y--20>
    </div>
  </div>
  <div text-lg text="zinc-300" text-right flex flex-col gap-3 mt-3>
    <div>
      演示文稿使用 <div inline-block mr-1 translate-y-0.8 i-logos:slidev />sli.dev 构建
    </div>
    <div text-sm text="zinc-500" mt-4>
      Powered by Slidev + Glow Theme
    </div>
  </div>
</div>
