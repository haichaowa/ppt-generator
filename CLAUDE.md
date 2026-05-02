# PPT Generator - Project Guidelines

## UnoCSS Web Fonts

- 国内网络无法访问 Google Fonts，`presetWebFonts` 必须使用 `provider: 'bunny'`（fonts.bunny.net 是国内可访问的 Google Fonts 镜像）
- `timeouts.failure` 建议设为 `60000`

## 幻灯片布局间距

- `translate-y-*` 下移容器后，其下方的兄弟元素不会跟着移动，导致重叠。解决方案：减小 `translate-y` 值（如 `translate-y-8`），同时增大下方元素的 `mt-*` 间距（如 `mt-20`）来避免重叠

## 表情包资源

- 表情包目录：`/Users/wanghaichao/develop/VsCodeProject/ChineseBQB-master`
