# Slidev 组件参考

Slidev 内置组件和 Vue 指令的完整参考，适用于所有主题。

---

## v-click — 点击动画

单个元素在点击后出现：

```html
<div v-click>点击后出现</div>
```

指定出现顺序：

```html
<div v-click="1">第一次点击出现</div>
<div v-click="2">第二次点击出现</div>
<div v-click="3">第三次点击出现</div>
```

注意：使用 `v-click` 时，slide frontmatter 中的 `clicks` 值需要与最大点击编号匹配。

### 配合 :class 动态样式

```html
<div
  v-click="1"
  :class="$clicks < 1 ? 'opacity-0 translate-y-10' : 'opacity-100 translate-y-0'"
>
  内容
</div>
```

---

## v-clicks — 批量动画

自动为子元素添加递进的 v-click 动画，无需手动编号：

```html
<v-clicks>
- 要点一
- 要点二
- 要点三
</v-clicks>
```

或用于卡片组件：

```html
<div grid grid-cols-2 gap-3>
<v-clicks>
  <div>卡片 A</div>
  <div>卡片 B</div>
  <div>卡片 C</div>
  <div>卡片 D</div>
</v-clicks>
</div>
```

---

## Link — 页面链接

幻灯片间跳转：

```html
<Link to="3">跳转到第3页</Link>
<Link to="intro">跳转到别名页</Link>
```

使用 slide name 属性命名页面：

```yaml
---
name: intro
---
```

---

## Toc — 目录

自动生成目录：

```html
<Toc />
<Toc maxDepth="2" />
```

---

## Arrow — 箭头

绘制箭头连接元素：

```html
<Arrow x1="100" y1="100" x2="400" y2="200" color="green" />
```

使用动态绑定：

```html
<Arrow v-bind="arrow1" />
```

---

## Transform — 缩放

缩放内容：

```html
<Transform :scale="0.8">
  <div>缩小到80%</div>
</Transform>
```

---

## Mermaid — 图表

使用 Mermaid 语法绘制图表：

````markdown
```mermaid
graph LR
  A[开始] --> B[过程] --> C[结束]
```
````

---

## LaTeX — 数学公式

行内公式：

```markdown
行内公式: $E = mc^2$
```

块级公式：

```markdown
$$
\frac{a}{b} = c
$$
```

---

## 代码块高级功能

### 行号

````markdown
```ts {6,7}{lines:true,startLine:5}
function add(
  a: Ref<number> | number,
  b: Ref<number> | number
) {
  return computed(() => unref(a) + unref(b))
}
```
````

### 行高亮

````markdown
```typescript {2,3}
function add(a: number, b: number) {
  return a + b  // 高亮
}
```
````

### 点击式高亮

````markdown
```typescript {1|2-3|all}
const a = 1
function add(x: number, y: number) {
  return x + y
}
```
````

### 最大高度与滚动

````markdown
```ts {2|3|7|12}{maxHeight:'350px'}
```
````

**语法**：`{行高亮}{maxHeight:'<value>'}`

**推荐值**：
- `maxHeight:'100px'` — 约 5 行代码
- `maxHeight:'200px'` — 约 10 行代码
- `maxHeight:'350px'` — 约 18 行代码

超过 15 行的代码块**必须**使用 `maxHeight` 防止溢出。

### Monaco 编辑器

````markdown
```ts {monaco}
console.log('HelloWorld')
```
````

### Monaco 差异编辑器

````markdown
```ts {monaco-diff}
console.log('Original text')
~~~
console.log('Modified text')
```
````

### Shiki Magic Move

````markdown
````md magic-move {lines: true}
```js
console.log(`Step ${1}`)
```
```js
console.log(`Step ${1 + 1}`)
```
```ts
console.log(`Step ${3}` as string)
```
````
````

---

## 演讲者注释

```markdown
# 幻灯片标题

内容

<!--
演讲者注释：只在演示者视图中显示
-->
```
