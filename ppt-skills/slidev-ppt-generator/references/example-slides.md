# 完整示例 slides.md

以下是一个使用 Glow 主题的专业 Slidev 演示文稿示例，展示了卡片布局、动画效果、发光背景、过渡问句页等高级功能：

```markdown
---
layout: center
highlighter: shiki
css: unocss
colorSchema: dark
transition: fade-out
title: AI 技术分享
exportFilename: ai-tech-share
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

<div translate-x--15>

# AI 技术趋势与实践

Exploring the Frontiers of AI Technology

<div mt-10 text-sm opacity-50>
  演讲者 · 2026-03-28
</div>

</div>

<div abs-br m-6 flex flex-col text-right text-sm opacity-50>
  <span>技术分享</span>
</div>

---
layout: section
glowSeed: 200
---

# 01

什么是 AI

---
class: py-10
clicks: 3
glow: right
glowSeed: 250
---

## AI 的三大核心能力

<div flex items-center gap-8 translate-y-20>
  <div
    v-click="1"
    flex-1 transition duration-500 ease-in-out
    :class="$clicks < 1 ? 'opacity-0 translate-y-10' : 'opacity-100 translate-y-0'"
  >
    <div border="2 solid violet-800/50" rounded-lg>
      <div flex items-center bg="violet-800/30" px-3 py-2 text-violet-300>
        <div i-carbon:text-creation text-sm mr-1 />
        <div text-xs><em>自然语言处理</em></div>
      </div>
      <div bg="violet-800/10" px-4 py-3>
        <div text-sm>理解和生成人类语言</div>
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
        <div i-carbon:image-search text-sm mr-1 />
        <div text-xs><em>计算机视觉</em></div>
      </div>
      <div bg="blue-800/10" px-4 py-3>
        <div text-sm>识别和理解图像内容</div>
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
        <div i-carbon:model-alt text-sm mr-1 />
        <div text-xs><em>推理决策</em></div>
      </div>
      <div bg="green-800/10" px-4 py-3>
        <div text-sm>基于数据做出智能判断</div>
      </div>
    </div>
  </div>
</div>

<!--
AI 的三大核心能力，逐条展示，注意每张卡片的动画效果
-->

---
class: py-10
clicks: 4
glowSeed: 300
---

## 使用 v-clicks 的 Grid 卡片

<div grid grid-cols-2 gap-3 mt-8>

<v-clicks>

  <div border="2 solid violet-800/50" rounded-lg overflow-hidden bg="violet-900/10" backdrop-blur-sm>
    <div flex items-center bg="violet-800/30" px-3 py-2 text-violet-300>
      <div i-carbon:text-creation text-sm mr-1 />
      <div font-semibold>卡片 A</div>
    </div>
    <div bg="violet-900/5" px-4 py-3>
      <div text-sm>使用 v-clicks 自动编号</div>
      <div text-xs opacity-70>无需手动指定 v-click 值</div>
    </div>
  </div>

  <div border="2 solid blue-800/50" rounded-lg overflow-hidden bg="blue-900/10" backdrop-blur-sm>
    <div flex items-center bg="blue-800/30" px-3 py-2 text-blue-300>
      <div i-carbon:image-search text-sm mr-1 />
      <div font-semibold>卡片 B</div>
    </div>
    <div bg="blue-900/5" px-4 py-3>
      <div text-sm>按顺序自动出现</div>
      <div text-xs opacity-70>子元素依次触发动画</div>
    </div>
  </div>

  <div border="2 solid green-800/50" rounded-lg overflow-hidden bg="green-900/10" backdrop-blur-sm>
    <div flex items-center bg="green-800/30" px-3 py-2 text-green-300>
      <div i-carbon:model-alt text-sm mr-1 />
      <div font-semibold>卡片 C</div>
    </div>
    <div bg="green-900/5" px-4 py-3>
      <div text-sm>支持任意数量的子元素</div>
      <div text-xs opacity-70>Grid 布局配合使用</div>
    </div>
  </div>

  <div border="2 solid amber-800/50" rounded-lg overflow-hidden bg="amber-900/10" backdrop-blur-sm>
    <div flex items-center bg="amber-800/30" px-3 py-2 text-amber-300>
      <div i-carbon:connect text-sm mr-1 />
      <div font-semibold>卡片 D</div>
    </div>
    <div bg="amber-900/5" px-4 py-3>
      <div text-sm>简洁高效的动画方案</div>
      <div text-xs opacity-70>减少手动管理 click 编号</div>
    </div>
  </div>

</v-clicks>

</div>

---
class: flex justify-center items-center gap-20 px-40 text-xl
---

<div
  absolute text-5xl
  :class="$clicks < 1 ? 'text-white' : 'translate-y--18 scale-40 text-white/30'"
  transition duration-500 ease-in-out
>
  <span>AI 到底能做什么？</span>
</div>

<div flex flex-col items-center>
  <v-clicks>
    <div mt-4>
      <h1 flex items-center text="5xl!">
        <span>比你想象的更多</span>
      </h1>
    </div>
  </v-clicks>
</div>

---
class: py-10
clicks: 2
glowSeed: 350
---

## 传统开发 vs AI 驱动开发

<div grid grid-cols-2 gap-8 mt-10>
  <div
    v-click="1"
    transition duration-500 ease-in-out
    :class="$clicks < 1 ? 'opacity-0' : 'opacity-100'"
    class="border-2 border-orange-500/30 rounded-lg p-5 bg-orange-500/10"
  >
    <div text-xl font-bold mb-4 text-orange-300>传统开发</div>
    <div text-sm mb-4>手动编写每个规则</div>

```ts
if (input.includes('hello')) {
  return 'Hi there!'
}
```

  </div>
  <div
    v-click="2"
    transition duration-500 ease-in-out
    :class="$clicks < 2 ? 'opacity-0' : 'opacity-100'"
    class="border-2 border-green-500/30 rounded-lg p-5 bg-green-500/10"
  >
    <div text-xl font-bold mb-4 text-green-300>AI 驱动</div>
    <div text-sm mb-4>AI 自动理解意图</div>

```ts
const response = await ai.chat({
  message: userInput
})
```

  </div>
</div>

---
class: py-10
clicks: 4
---

## 开发流程

<span>从需求到上线的完整步骤</span>

<div mt-8 />

<div flex items-center gap-4>

<v-clicks>

<div
  rounded-lg
  border="2 solid violet-900" bg="violet-900/20"
  backdrop-blur
  flex-1
  transition duration-500 ease-in-out
>
  <div px-5 py-10 flex items-center justify-center>
    <div i-solar:document-bold-duotone size-16 />
  </div>
  <div bg="violet-900/30" w-full px-4 py-2 flex items-center justify-center text-center>
    <span>需求定义</span>
  </div>
</div>

<div
  rounded-lg
  border="2 solid blue-800" bg="blue-800/20"
  backdrop-blur
  flex-1
  transition duration-500 ease-in-out
>
  <div px-5 py-10 flex items-center justify-center>
    <div i-solar:code-bold-duotone size-16 />
  </div>
  <div bg="blue-800/30" w-full px-4 py-2 flex items-center justify-center text-center>
    <span>开发实现</span>
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
    <div i-solar:check-circle-bold-duotone size-16 />
  </div>
  <div bg="green-800/30" w-full px-4 py-2 flex items-center justify-center text-center>
    <span>测试验证</span>
  </div>
</div>

<div
  rounded-lg
  border="2 solid amber-800" bg="amber-800/20"
  backdrop-blur
  flex-1
  transition duration-500 ease-in-out
>
  <div px-5 py-10 flex items-center justify-center>
    <div i-solar:rocket-2-bold-duotone size-16 />
  </div>
  <div bg="amber-800/30" w-full px-4 py-2 flex items-center justify-center text-center>
    <span>上线部署</span>
  </div>
</div>

</v-clicks>

</div>

---
layout: quote
glowSeed: 500
---

> 任何足够先进的技术，都与魔法无异。

— Arthur C. Clarke

---
layout: end
glowSeed: 600
---

感谢观看

<div class="text-sm opacity-50 mt-4">
  联系方式 · GitHub · Email
</div>
```
```
[WARNING] Scoping issue: the code fence was never closed. The code block that starts at line 7 continues until the end of the file without a closing fence (```). This is likely caused by incorrect nesting of code fences - see how they should be nested at https://mdc pursuit.com/syntax/#code-fence-within-code-block. If you do not wish this to be a code fence, you can escape it: \`\`\`.

The user will not see this warning.