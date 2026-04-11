---
layout: center
highlighter: shiki
css: unocss
colorSchema: dark
transition: fade-out
title: React 井字棋教程
exportFilename: react-tic-tac-toe
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
  <div flex items-center gap-3 mb-6>
    <div i-logos:react text-5xl />
    <div text-5xl font-bold>
      井字棋教程
    </div>
  </div>
  <div text-xl opacity-60 mb-8>
    从零开始学习 React 核心概念
  </div>
  <div flex items-center gap-2 text-sm opacity-40>
    <div i-carbon:link text-xs />
    <span>zh-hans.react.dev/learn/tutorial-tic-tac-toe</span>
  </div>
</div>

---
layout: section
glowSeed: 200
---

# 课程概览

---
class: py-10
clicks: 4
glow: right
glowSeed: 250
---

## 我们要构建什么

<div grid grid-cols-2 gap-6 mt-8>
<v-clicks>

<div border="2 solid cyan-800/50" rounded-lg>
  <div flex items-center bg="cyan-800/30" px-3 py-2 text-cyan-300>
    <div i-carbon:game-console text-sm mr-1 />
    <div text-xs><em>交互式井字棋</em></div>
  </div>
  <div bg="cyan-800/10" px-4 py-3>
    一个完整的两人对战井字棋游戏
  </div>
</div>

<div border="2 solid violet-800/50" rounded-lg>
  <div flex items-center bg="violet-800/30" px-3 py-2 text-violet-300>
    <div i-carbon:trophy text-sm mr-1 />
    <div text-xs><em>胜负判定</em></div>
  </div>
  <div bg="violet-800/10" px-4 py-3>
    自动检测获胜者并显示结果
  </div>
</div>

<div border="2 solid amber-800/50" rounded-lg>
  <div flex items-center bg="amber-800/30" px-3 py-2 text-amber-300>
    <div i-carbon:time text-sm mr-1 />
    <div text-xs><em>时间旅行</em></div>
  </div>
  <div bg="amber-800/10" px-4 py-3>
    回顾并跳转到游戏历史中的任意步骤
  </div>
</div>

<div border="2 solid green-800/50" rounded-lg>
  <div flex items-center bg="green-800/30" px-3 py-2 text-green-300>
    <div i-carbon:code text-sm mr-1 />
    <div text-xs><em>React 基础</em></div>
  </div>
  <div bg="green-800/10" px-4 py-3>
    组件、Props、State 核心概念
  </div>
</div>

</v-clicks>
</div>

---
layout: section
glowSeed: 300
---

# React 核心概念

---
class: py-10
clicks: 3
glowSeed: 350
---

## 组件 (Components)

<div mt-6 />

组件是 React 的**构建块** — 可重用的 UI 单元

<div grid grid-cols-3 gap-6 mt-8>
  <div
    v-click="1"
    transition duration-500 ease-in-out
    :class="$clicks < 1 ? 'opacity-0 translate-y-10' : 'opacity-100 translate-y-0'"
  >
    <div flex items-center justify-center mb-4>
      <div i-carbon:assembly-cluster text-5xl text-cyan-400 />
    </div>
    <div text-center font-bold mb-2>可复用</div>
    <div text-sm text-center opacity-70>定义一次，多处使用</div>
  </div>
  <div
    v-click="2"
    transition duration-500 ease-in-out
    :class="$clicks < 2 ? 'opacity-0 translate-y-10' : 'opacity-100 translate-y-0'"
  >
    <div flex items-center justify-center mb-4>
      <div i-carbon:nested-loops text-5xl text-violet-400 />
    </div>
    <div text-center font-bold mb-2>可嵌套</div>
    <div text-sm text-center opacity-70>组件组合形成完整 UI</div>
  </div>
  <div
    v-click="3"
    transition duration-500 ease-in-out
    :class="$clicks < 3 ? 'opacity-0 translate-y-10' : 'opacity-100 translate-y-0'"
  >
    <div flex items-center justify-center mb-4>
      <div i-carbon:export text-5xl text-amber-400 />
    </div>
    <div text-center font-bold mb-2>可导出</div>
    <div text-sm text-center opacity-70>export default 公开组件</div>
  </div>
</div>

---
class: py-10
glowSeed: 400
---

## 组件示例

```jsx {1,4|all}
export default function Square() {
  return <button className="square">X</button>;
}
```

<div mt-8 grid grid-cols-2 gap-6>
  <div border="2 solid blue-800/50" rounded-lg bg="blue-800/10" p-4>
    <div text-blue-300 text-sm font-bold mb-2>要点</div>
    <div text-sm>
      <div>`export default` — 主入口组件</div>
      <div mt-1>`function` — 函数式组件</div>
      <div mt-1>`return` — 返回 JSX</div>
    </div>
  </div>
  <div border="2 solid green-800/50" rounded-lg bg="green-800/10" p-4>
    <div text-green-300 text-sm font-bold mb-2>规则</div>
    <div text-sm>
      <div>组件名必须大写开头</div>
      <div mt-1>必须返回单个 JSX 元素</div>
      <div mt-1>可用 Fragment（空标签）包裹</div>
    </div>
  </div>
</div>

---
class: py-10
glowSeed: 420
---

## JSX 语法

JSX = **JavaScript + HTML** — 描述 UI 的方式

<div mt-6 grid grid-cols-2 gap-6>
  <div>
    <div text-sm opacity-50 mb-2>JSX 中的变量</div>
    <div border="2 solid violet-800/50" rounded-lg bg="violet-900/10" p-4>
```jsx
// 变量用 {} 包裹
<button>{value}</button>

// 属性赋值
<Square value={squares[0]} />
```
    </div>
  </div>
  <div>
    <div text-sm opacity-50 mb-2>JSX 中的事件</div>
    <div border="2 solid cyan-800/50" rounded-lg bg="cyan-900/10" p-4>
```jsx
// 事件处理用 {} 包裹
<button onClick={handleClick}>
  Click me
</button>
```
    </div>
  </div>
</div>

<div mt-4 border="2 solid amber-800/50" rounded-lg bg="amber-900/10" p-4>
  <div text-amber-300 text-xs mb-1>注意</div>
  <div text-sm>React 组件必须返回单个 JSX 根元素，多个元素需用 Fragment 包裹</div>
</div>

---
class: py-10
clicks: 2
glowSeed: 450
---

## Props — 数据传递

<div mt-4 text-sm opacity-60>父组件向子组件传递数据的机制</div>

<div mt-6 grid grid-cols-2 gap-6>
  <div
    v-click="1"
    border="2 solid blue-800/50" rounded-lg bg="blue-900/10" p-4
    transition duration-500 ease-in-out
    :class="$clicks < 1 ? 'opacity-0' : 'opacity-100'"
  >
    <div text-blue-300 text-sm font-bold mb-2>接收方（子组件）</div>
```jsx
function Square({ value }) {
  return (
    <button className="square">
      {value}
    </button>
  );
}
```
  </div>
  <div
    v-click="2"
    border="2 solid green-800/50" rounded-lg bg="green-900/10" p-4
    transition duration-500 ease-in-out
    :class="$clicks < 2 ? 'opacity-0' : 'opacity-100'"
  >
    <div text-green-300 text-sm font-bold mb-2>传递方（父组件）</div>
```jsx
<Square value="1" />
<Square value="2" />
<Square value="3" />
```
  </div>
</div>

---
class: py-10
clicks: 2
glowSeed: 480
---

## State — 组件记忆

<div mt-4 text-sm opacity-60>使用 `useState` 让组件"记住"数据</div>

<div mt-6>
  <div
    v-click="1"
    transition duration-500 ease-in-out
    :class="$clicks < 1 ? 'opacity-0 translate-y-5' : 'opacity-100 translate-y-0'"
  >
```jsx
import { useState } from 'react';

function Square() {
  const [value, setValue] = useState(null);
  //      ↑ 当前值  ↑ 设置函数   ↑ 初始值

  return (
    <button onClick={() => setValue('X')}>
      {value}
    </button>
  );
}
```
  </div>
</div>

<div mt-4
  v-click="2"
  transition duration-500 ease-in-out
  :class="$clicks < 2 ? 'opacity-0' : 'opacity-100'"
>
  <div border="2 solid violet-800/50" rounded-lg bg="violet-900/10" p-3>
    <div text-sm>调用 `setValue` 时，React 会自动重新渲染该组件及其子组件</div>
  </div>
</div>

---
layout: section
glowSeed: 500
---

# 构建井字棋游戏

---
class: py-10
glowSeed: 520
---

## 构建棋盘

<div mt-4 text-sm opacity-60>用 `div` 分行 + CSS 构建三行三列的棋盘</div>

<div mt-4 grid grid-cols-2 gap-6>
  <div>
```jsx {1,5,9|all}{maxHeight:'260px'}
export default function Board() {
  return (
    <>
      <div className="board-row">
        <Square value={squares[0]} />
        <Square value={squares[1]} />
        <Square value={squares[2]} />
      </div>
      <div className="board-row">
        <Square value={squares[3]} />
        <Square value={squares[4]} />
        <Square value={squares[5]} />
      </div>
      <div className="board-row">
        <Square value={squares[6]} />
        <Square value={squares[7]} />
        <Square value={squares[8]} />
      </div>
    </>
  );
}
```
  </div>
  <div flex flex-col justify-center gap-4>
    <div border="2 solid cyan-800/50" rounded-lg bg="cyan-900/10" p-4>
      <div text-cyan-300 text-sm font-bold mb-2>组件结构</div>
      <div text-sm>
        <div>`Game` → 顶层游戏组件</div>
        <div mt-1>`Board` → 棋盘（3x3 网格）</div>
        <div mt-1>`Square` → 单个方块</div>
      </div>
    </div>
    <div border="2 solid amber-800/50" rounded-lg bg="amber-900/10" p-4>
      <div text-amber-300 text-sm font-bold mb-2>数据流</div>
      <div text-sm>`squares` 数组（9 个元素）→ 通过 Props 传递给每个 `Square`</div>
    </div>
  </div>
</div>

---
class: py-10
clicks: 3
glowSeed: 550
---

## 状态提升 (Lifting State Up)

<div mt-4 text-sm opacity-60>将共享状态移到最近的公共父组件中</div>

<div mt-6>
<v-clicks>

<div border="2 solid violet-800/50" rounded-lg bg="violet-900/10" p-4 mb-4>
  <div text-violet-300 text-sm font-bold mb-1>问题</div>
  <div text-sm>每个 `Square` 维护自己的 state，Board 无法获知全局状态</div>
</div>

<div border="2 solid cyan-800/50" rounded-lg bg="cyan-900/10" p-4 mb-4>
  <div text-cyan-300 text-sm font-bold mb-1>解决方案</div>
  <div text-sm>将 `squares` 状态提升到 `Board` 组件，通过 props 向下传递</div>
</div>

<div border="2 solid green-800/50" rounded-lg bg="green-900/10" p-4>
  <div text-green-300 text-sm font-bold mb-1>核心原则</div>
  <div text-sm>要在多个子组件间共享数据，在其最近的公共父组件中声明共享 state</div>
</div>

</v-clicks>
</div>

---
class: py-10
clicks: 2
glowSeed: 580
---

## 状态提升 — 代码实现

<div mt-4 grid grid-cols-2 gap-6>
  <div
    v-click="1"
    transition duration-500 ease-in-out
    :class="$clicks < 1 ? 'opacity-0' : 'opacity-100'"
  >
    <div text-sm opacity-50 mb-2>Board 组件管理状态</div>
```jsx {1,4-5|8-12|all}{maxHeight:'280px'}
export default function Board() {
  // 状态提升到 Board
  const [squares, setSquares] =
    useState(Array(9).fill(null));

  function handleClick(i) {
    const next = squares.slice();
    next[i] = 'X';
    setSquares(next);
  }

  return (
    <>
      <Square value={squares[0]}
        onSquareClick={() =>
          handleClick(0)} />
      // ...其他 8 个 Square
    </>
  );
}
```
  </div>
  <div
    v-click="2"
    transition duration-500 ease-in-out
    :class="$clicks < 2 ? 'opacity-0' : 'opacity-100'"
  >
    <div text-sm opacity-50 mb-2>Square 变为受控组件</div>
```jsx
function Square({ value, onSquareClick }) {
  return (
    <button
      className="square"
      onClick={onSquareClick}
    >
      {value}
    </button>
  );
}
```
    <div mt-4 border="2 solid amber-800/50" rounded-lg bg="amber-900/10" p-3>
      <div text-sm>`Square` 不再管理自己的状态，完全由 `Board` 控制</div>
    </div>
  </div>
</div>

---
class: py-10
glowSeed: 600
---

## 为什么不变性很重要

<div mt-4 grid grid-cols-2 gap-6>
  <div>
    <div text-sm opacity-50 mb-2>直接修改 (Mutation)</div>
    <div border="2 solid red-900/50" rounded-lg bg="red-900/10" p-4>
```js
const squares = [null, null, null];
squares[0] = 'X';
// 原数组被修改了！
```
    </div>
  </div>
  <div>
    <div text-sm opacity-50 mb-2>不可变更新 (Immutable)</div>
    <div border="2 solid green-800/50" rounded-lg bg="green-900/10" p-4>
```js
const squares = [null, null, null];
const next = squares.slice();
next[0] = 'X';
// 原数组保持不变
```
    </div>
  </div>
</div>

<div mt-6 grid grid-cols-3 gap-4>
  <div border="2 solid cyan-800/50" rounded-lg bg="cyan-900/10" p-3>
    <div text-cyan-300 text-xs font-bold mb-1>时间旅行</div>
    <div text-xs>保留历史版本，支持撤销/重做</div>
  </div>
  <div border="2 solid violet-800/50" rounded-lg bg="violet-900/10" p-3>
    <div text-violet-300 text-xs font-bold mb-1>性能优化</div>
    <div text-xs>低成本比较数据是否变化</div>
  </div>
  <div border="2 solid amber-800/50" rounded-lg bg="amber-900/10" p-3>
    <div text-amber-300 text-xs font-bold mb-1>避免 Bug</div>
    <div text-xs>数据变化可追踪、可预测</div>
  </div>
</div>

---
class: py-10
glowSeed: 620
---

## 交替落子 — X 和 O

<div mt-4 text-sm opacity-60>添加 `xIsNext` 状态追踪当前轮次</div>

<div mt-4>
```jsx {1|3-7|8}{maxHeight:'280px'}
export default function Board() {
  const [xIsNext, setXIsNext] = useState(true);
  const [squares, setSquares] = useState(Array(9).fill(null));

  function handleClick(i) {
    if (squares[i]) return;  // 已有棋子则跳过
    const next = squares.slice();
    next[i] = xIsNext ? 'X' : 'O';  // 根据轮次落子
    setSquares(next);
    setXIsNext(!xIsNext);            // 翻转轮次
  }
  // ...
}
```
</div>

<div mt-4 grid grid-cols-2 gap-4>
  <div border="2 solid blue-800/50" rounded-lg bg="blue-900/10" p-3>
    <div text-sm>`xIsNext` 为 `true` → 落 X，否则落 O</div>
  </div>
  <div border="2 solid green-800/50" rounded-lg bg="green-900/10" p-3>
    <div text-sm>`if (squares[i]) return` — 防止覆盖已落子位置</div>
  </div>
</div>

---
class: py-10
glowSeed: 650
---

## 判定获胜

<div mt-4 text-sm opacity-60>`calculateWinner` 检查 8 种获胜组合</div>

<div mt-4 grid grid-cols-2 gap-6>
  <div>
```js {1-8|10-14}{maxHeight:'260px'}
function calculateWinner(squares) {
  const lines = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], // 横
    [0, 3, 6], [1, 4, 7], [2, 5, 8], // 竖
    [0, 4, 8], [2, 4, 6],            // 对角
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b]
        && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}
```
  </div>
  <div flex flex-col justify-center gap-4>
    <div border="2 solid violet-800/50" rounded-lg bg="violet-900/10" p-4>
      <div text-violet-300 text-sm font-bold mb-2>获胜判定逻辑</div>
      <div text-sm>检查横、竖、对角共 8 条线</div>
      <div mt-1 text-sm>三格相同且非空 → 返回胜者</div>
    </div>
    <div border="2 solid cyan-800/50" rounded-lg bg="cyan-900/10" p-4>
      <div text-cyan-300 text-sm font-bold mb-2>状态显示</div>
```jsx
const winner = calculateWinner(squares);
let status;
if (winner) {
  status = 'Winner: ' + winner;
} else {
  status = 'Next: ' + (xIsNext ? 'X' : 'O');
}
```
    </div>
  </div>
</div>

---
layout: section
glowSeed: 700
---

# 时间旅行

---
class: py-10
clicks: 3
glowSeed: 720
---

## 存储落子历史

<div mt-4 text-sm opacity-60>利用不可变性，保存每一步的棋盘快照</div>

<div mt-6>
<v-clicks>

<div border="2 solid violet-800/50" rounded-lg bg="violet-900/10" p-4 mb-4>
  <div text-violet-300 text-sm font-bold mb-1>History 数组</div>
```js
[
  [null, null, null, null, null, null, null, null, null],  // 初始状态
  [null, null, null, null, 'X', null, null, null, null],   // 第 1 步
  [null, null, null, null, 'X', null, null, null, 'O'],    // 第 2 步
  // ...
]
```
</div>

<div border="2 solid cyan-800/50" rounded-lg bg="cyan-900/10" p-4 mb-4>
  <div text-cyan-300 text-sm font-bold mb-1>Game 组件管理历史</div>
```jsx
const [history, setHistory] = useState([Array(9).fill(null)]);
const [currentMove, setCurrentMove] = useState(0);
const xIsNext = currentMove % 2 === 0;
const currentSquares = history[currentMove];
```
</div>

<div border="2 solid green-800/50" rounded-lg bg="green-900/10" p-4>
  <div text-green-300 text-sm font-bold mb-1>关键优化</div>
  <div text-sm>`xIsNext` 从 `currentMove` 计算得出 — 消除冗余状态</div>
</div>

</v-clicks>
</div>

---
class: py-10
glowSeed: 750
---

## 再一次状态提升

<div mt-4 text-sm opacity-60>将状态从 Board 提升到 Game 组件</div>

<div mt-4 grid grid-cols-2 gap-6>
  <div>
    <div text-sm opacity-50 mb-2>Game 组件</div>
```jsx {1-3|5-8|10-14}{maxHeight:'280px'}
export default function Game() {
  const [history, setHistory] =
    useState([Array(9).fill(null)]);
  const [currentMove, setCurrentMove] =
    useState(0);
  const xIsNext = currentMove % 2 === 0;
  const currentSquares =
    history[currentMove];

  function handlePlay(nextSquares) {
    const next = [...history
      .slice(0, currentMove + 1), nextSquares];
    setHistory(next);
    setCurrentMove(next.length - 1);
  }
  // ...
}
```
  </div>
  <div>
    <div text-sm opacity-50 mb-2>Board 变为纯展示</div>
```jsx
function Board({ xIsNext, squares, onPlay }) {
  function handleClick(i) {
    if (calculateWinner(squares)
      || squares[i]) return;
    const next = squares.slice();
    next[i] = xIsNext ? 'X' : 'O';
    onPlay(next);
  }
  // ...
}
```
    <div mt-4 border="2 solid amber-800/50" rounded-lg bg="amber-900/10" p-3>
      <div text-sm>Board 不再有自己的 state，完全由 Game 控制</div>
    </div>
  </div>
</div>

---
class: py-10
clicks: 2
glowSeed: 780
---

## Key 的重要性

<div mt-4 text-sm opacity-60>列表渲染时，React 需要 key 来追踪元素身份</div>

<div mt-6 grid grid-cols-2 gap-6>
  <div
    v-click="1"
    border="2 solid red-900/50" rounded-lg bg="red-900/10" p-4
    transition duration-500 ease-in-out
    :class="$clicks < 1 ? 'opacity-0' : 'opacity-100'"
  >
    <div text-red-300 text-sm font-bold mb-2>没有 Key 的警告</div>
    <div text-sm mb-2 font-mono>Warning: Each child in an array should have a unique "key" prop.</div>
    <div text-sm>React 无法正确识别哪些元素发生了变化</div>
  </div>
  <div
    v-click="2"
    border="2 solid green-800/50" rounded-lg bg="green-900/10" p-4
    transition duration-500 ease-in-out
    :class="$clicks < 2 ? 'opacity-0' : 'opacity-100'"
  >
    <div text-green-300 text-sm font-bold mb-2>正确使用 Key</div>
```jsx
const moves = history.map(
  (squares, move) => {
  return (
    <li key={move}>
      <button onClick={() =>
        jumpTo(move)}>
        {move > 0
          ? `Go to #${move}`
          : 'Go to start'}
      </button>
    </li>
  );
});
```
  </div>
</div>

---
class: py-10
glowSeed: 800
---

## 实现时间旅行

<div mt-4 text-sm opacity-60>`jumpTo` 函数实现历史跳转</div>

<div mt-4>
```jsx {1-3|5-12|14-18}{maxHeight:'300px'}
function jumpTo(nextMove) {
  setCurrentMove(nextMove);
}

function handlePlay(nextSquares) {
  // 截断到当前步 + 追加新状态
  const nextHistory = [
    ...history.slice(0, currentMove + 1),
    nextSquares
  ];
  setHistory(nextHistory);
  setCurrentMove(nextHistory.length - 1);
}

const moves = history.map((squares, move) => (
  <li key={move}>
    <button onClick={() => jumpTo(move)}>
      {move > 0 ? `Go to move #${move}` : 'Go to game start'}
    </button>
  </li>
));
```
</div>

---
class: py-10
glowSeed: 820
---

## 最终完整代码

```jsx {1-7|9-12|14-24|26-37|all}{maxHeight:'350px'}
import { useState } from 'react';

function Square({ value, onSquareClick }) {
  return <button className="square" onClick={onSquareClick}>{value}</button>;
}

function Board({ xIsNext, squares, onPlay }) {
  function handleClick(i) {
    if (calculateWinner(squares) || squares[i]) return;
    const next = squares.slice();
    next[i] = xIsNext ? 'X' : 'O';
    onPlay(next);
  }
  const winner = calculateWinner(squares);
  const status = winner
    ? 'Winner: ' + winner
    : 'Next player: ' + (xIsNext ? 'X' : 'O');
  return (<>
    <div className="status">{status}</div>
    {/* 3x3 grid of Square components */}
  </>);
}

export default function Game() {
  const [history, setHistory] = useState([Array(9).fill(null)]);
  const [currentMove, setCurrentMove] = useState(0);
  const xIsNext = currentMove % 2 === 0;
  const currentSquares = history[currentMove];
  // handlePlay, jumpTo, moves rendering...
}

function calculateWinner(squares) { /* 8 lines check */ }
```

---
layout: section
glowSeed: 850
---

# 回顾与总结

---
class: py-10
clicks: 6
glowSeed: 880
---

## 你学到了什么

<div grid grid-cols-2 gap-4 mt-8>
<v-clicks>

<div border="2 solid cyan-800/50" rounded-lg bg="cyan-900/10" p-4>
  <div flex items-center gap-2 mb-2>
    <div i-carbon:assembly-cluster text-lg text-cyan-400 />
    <span class="text-cyan-300" text-sm font-bold>组件</span>
  </div>
  <div text-sm>函数式组件、export default、JSX 语法</div>
</div>

<div border="2 solid violet-800/50" rounded-lg bg="violet-900/10" p-4>
  <div flex items-center gap-2 mb-2>
    <div i-carbon:flow-stream text-lg text-violet-400 />
    <span class="text-violet-300" text-sm font-bold>Props</span>
  </div>
  <div text-sm>父传子的数据流、事件回调传递</div>
</div>

<div border="2 solid green-800/50" rounded-lg bg="green-900/10" p-4>
  <div flex items-center gap-2 mb-2>
    <div i-carbon:data-base text-lg text-green-400 />
    <span class="text-green-300" text-sm font-bold>State</span>
  </div>
  <div text-sm>useState、状态提升、不可变更新</div>
</div>

<div border="2 solid amber-800/50" rounded-lg bg="amber-900/10" p-4>
  <div flex items-center gap-2 mb-2>
    <div i-carbon:key text-lg text-amber-400 />
    <span class="text-amber-300" text-sm font-bold>Key</span>
  </div>
  <div text-sm>列表渲染、元素追踪、key 的正确使用</div>
</div>

<div border="2 solid rose-800/50" rounded-lg bg="rose-900/10" p-4>
  <div flex items-center gap-2 mb-2>
    <div i-carbon:time text-lg text-rose-400 />
    <span class="text-rose-300" text-sm font-bold>时间旅行</span>
  </div>
  <div text-sm>历史记录存储、状态跳转与恢复</div>
</div>

<div border="2 solid blue-800/50" rounded-lg bg="blue-900/10" p-4>
  <div flex items-center gap-2 mb-2>
    <div i-carbon:clean text-lg text-blue-400 />
    <span class="text-blue-300" text-sm font-bold>代码优化</span>
  </div>
  <div text-sm>消除冗余 state、派生状态</div>
</div>

</v-clicks>
</div>

---
class: py-10
glowSeed: 900
---

## 进阶挑战

<div mt-6 grid grid-cols-2 gap-4>
  <div border="2 solid cyan-800/50" rounded-lg bg="cyan-900/10" p-4>
    <div text-cyan-300 text-sm font-bold mb-1>1. 当前步骤提示</div>
    <div text-sm>当前步骤显示"You are at move #..."而非按钮</div>
  </div>
  <div border="2 solid violet-800/50" rounded-lg bg="violet-900/10" p-4>
    <div text-violet-300 text-sm font-bold mb-1>2. 循环渲染棋盘</div>
    <div text-sm>用循环替代硬编码的 9 个 Square</div>
  </div>
  <div border="2 solid green-800/50" rounded-lg bg="green-900/10" p-4>
    <div text-green-300 text-sm font-bold mb-1>3. 排序切换</div>
    <div text-sm>添加升序/降序切换按钮</div>
  </div>
  <div border="2 solid amber-800/50" rounded-lg bg="amber-900/10" p-4>
    <div text-amber-300 text-sm font-bold mb-1>4. 高亮获胜线</div>
    <div text-sm>获胜时高亮三个方块，平局时提示</div>
  </div>
  <div border="2 solid rose-800/50" rounded-lg bg="rose-900/10" p-4>
    <div text-rose-300 text-sm font-bold mb-1>5. 落子坐标</div>
    <div text-sm>在历史列表中显示 (row, col) 格式位置</div>
  </div>
  <div border="2 solid blue-800/50" rounded-lg bg="blue-900/10" p-4>
    <div text-blue-300 text-sm font-bold mb-1>下一步学习</div>
    <div text-sm>阅读 React 哲学 — 理解如何构建应用 UI</div>
  </div>
</div>

---
layout: center
glowSeed: 950
---

<div flex flex-col items-center>
  <div text-6xl font-bold mb-6>
    恭喜!
  </div>
  <div text-xl opacity-60 mb-8>
    你已经完成了 React 井字棋教程
  </div>
  <div flex items-center gap-4>
    <div i-logos:react text-4xl />
    <div text-2xl font-bold>React</div>
  </div>
  <div mt-8 text-sm opacity-40>
    zh-hans.react.dev
  </div>
</div>
