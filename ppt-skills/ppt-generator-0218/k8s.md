<!-- .slide: type=cover -->

# Kubernetes 核心概念

## 从架构到实践的完整指南

作者 | 2025.02.19

<!-- .slide: type=toc -->

# 本期内容

## 01 核心架构组件
## 02 工作负载资源
## 03 服务发现与负载均衡
## 04 存储管理
## 05 配置与密钥
## 06 元数据与权限

<!-- .slide: type=chapter -->

# 01

## 核心架构组件

<!-- .slide: type=content -->

## 集群架构概览

Kubernetes 集群由 Master 节点和 Worker 节点组成

- Master：集群的大脑，负责管理和决策
- Node：集群的工人，真正运行业务应用
- etcd：集群的数据库，保存所有状态
- 容器运行时：Docker、containerd 等

<!-- .slide: type=grid -->

## Master 组件

### API Server
- icon: ◉
- color: cyan
- desc: 集群入口门户，所有操作都通过它

### Scheduler
- icon: ◈
- color: purple
- desc: 调度器，决定 Pod 运行在哪个节点

### Controller
- icon: ◆
- color: pink
- desc: 控制器，确保实际状态向期望状态靠拢

### etcd
- icon: ▣
- color: orange
- desc: 键值数据库，保存所有集群数据

<!-- .slide: type=grid -->

## Node 组件

### kubelet
- icon: ◉
- color: cyan
- desc: 节点代理，与 Master 通信管理 Pod

### kube-proxy
- icon: ◈
- color: purple
- desc: 网络代理，维护节点网络规则

### 容器运行时
- icon: ◆
- color: pink
- desc: Docker/containerd，真正运行容器

### Pod
- icon: ▣
- color: orange
- desc: 最小部署单元，一组容器的集合

<!-- .slide: type=chapter -->

# 02

## 工作负载资源

<!-- .slide: type=content -->

## Pod - 最小部署单元

Kubernetes 中最小的部署单元，一个或多个容器的组合

- 共享网络：同一 Pod 内容器共享网络命名空间
- 共享存储：可以挂载共享卷
- 同生共死：一起调度、一起销毁
- 类比：一个"逻辑主机"，里面运行紧密协作的进程

<!-- .slide: type=two-column -->

## Deployment vs StatefulSet

### Deployment

无状态应用管理

- 副本数可伸缩
- 滚动更新
- Pod 身份不固定
- 适合 Web 服务、API

---

### StatefulSet

有状态应用管理

- 稳定的网络标识
- 持久化存储
- 有序部署和扩展
- 适合数据库、缓存

<!-- .slide: type=grid -->

## 其他工作负载类型

### DaemonSet
- icon: ◉
- color: cyan
- desc: 每个节点运行一个 Pod 副本

### Job
- icon: ◈
- color: purple
- desc: 一次性任务，完成后退出

### CronJob
- icon: ◆
- color: pink
- desc: 定时任务，按计划周期执行

### ReplicaSet
- icon: ▣
- color: orange
- desc: 维持指定数量的 Pod 副本

<!-- .slide: type=content -->

## DaemonSet 使用场景

确保每个节点上都运行一个 Pod 副本的控制器

- 日志收集：Fluentd、Filebeat
- 监控采集：Prometheus Node Exporter
- 网络插件：Calico、Flannel
- 存储插件：Ceph、GlusterFS

<!-- .slide: type=chapter -->

# 03

## 服务发现与负载均衡

<!-- .slide: type=content -->

## Service 核心概念

将一组 Pod 暴露为网络服务的抽象方式

- 固定入口：Pod IP 会变化，Service 提供稳定访问点
- 负载均衡：自动将请求分发到后端 Pod
- 服务发现：通过 DNS 名称访问服务
- 解耦：前端不需要知道后端 Pod 的具体 IP

<!-- .slide: type=data -->

## Service 四种类型

| 类型 | 访问范围 | 使用场景 |
|-----|---------|---------|
| ClusterIP | 集群内部 | 内部服务通信 |
| NodePort | 节点IP:端口 | 开发测试环境 |
| LoadBalancer | 外部负载均衡 | 生产环境暴露 |
| ExternalName | 外部域名映射 | 访问外部服务 |

<!-- .slide: type=content -->

## Ingress - 七层路由入口

管理集群外部访问集群内部服务的 API 对象

- 7层负载：基于域名、URL 路径的路由
- SSL 终止：统一处理 HTTPS 证书
- 虚拟主机：一个 IP 托管多个服务
- 需要控制器：Nginx Ingress、Traefik 等

<!-- .slide: type=chapter -->

# 04

## 存储管理

<!-- .slide: type=grid -->

## 存储核心概念

### Volume
- icon: ◉
- color: cyan
- desc: Pod 内容器共享的存储目录

### PV
- icon: ◈
- color: purple
- desc: 持久卷，管理员准备的存储资源

### PVC
- icon: ◆
- color: pink
- desc: 持久卷声明，用户对存储的申请

### StorageClass
- icon: ▣
- color: orange
- desc: 存储类型模板，动态创建 PV

<!-- .slide: type=two-column -->

## PV 与 PVC 的关系

### PV（持久卷）

管理员准备的资源

- 独立于 Pod 存在
- 定义容量和访问模式
- 绑定后专属于 PVC
- 类比：一块硬盘

---

### PVC（持久卷声明）

用户的存储申请

- 声明所需容量和类型
- 自动匹配满足条件的 PV
- 被 Pod 挂载使用
- 类比：申请单

<!-- .slide: type=content -->

## StorageClass 动态供给

定义存储的类型模板，实现 PV 的动态创建

- 按需创建：创建 PVC 时自动创建 PV
- 类型定义：关联 SSD、HDD 等存储类型
- 回收策略：Delete 或 Retain
- 解耦应用：开发者无需关心底层存储实现

<!-- .slide: type=chapter -->

# 05

## 配置与密钥

<!-- .slide: type=two-column -->

## ConfigMap vs Secret

### ConfigMap

非敏感配置数据

- 配置文件内容
- 环境变量
- 命令行参数
- 明文存储

---

### Secret

敏感信息数据

- 密码、Token
- SSH 密钥
- OAuth 令牌
- Base64 编码

<!-- .slide: type=content -->

## ConfigMap 使用方式

将应用的配置信息与容器镜像分离

- 环境变量注入：作为 Pod 的环境变量
- 配置文件挂载：作为 Volume 挂载到容器
- 命令行参数：在启动命令中引用
- 热更新：修改 ConfigMap 可触发 Pod 更新

<!-- .slide: type=chapter -->

# 06

## 元数据与权限

<!-- .slide: type=content -->

## Namespace 资源隔离

在同一个物理集群内实现资源隔离的虚拟集群

- 环境隔离：dev、test、prod 环境分开
- 团队隔离：不同团队使用不同命名空间
- 资源配额：可限制每个 Namespace 的资源使用
- 访问控制：可针对 Namespace 设置权限

<!-- .slide: type=grid -->

## Label 与 Selector

### Label
- icon: ◉
- color: cyan
- desc: 键值对标签，标识对象属性

### Selector
- icon: ◈
- color: purple
- desc: 根据标签筛选对象

### Annotation
- icon: ◆
- color: pink
- desc: 非标识性元数据

### LimitRange
- icon: ▣
- color: orange
- desc: 资源限制范围

<!-- .slide: type=data -->

## RBAC 权限模型

| 组件 | 作用范围 | 功能 |
|-----|---------|-----|
| Role | Namespace | 定义命名空间内权限 |
| ClusterRole | 集群 | 定义集群级别权限 |
| RoleBinding | Namespace | 绑定角色到用户 |
| ClusterRoleBinding | 集群 | 绑定集群角色到用户 |

<!-- .slide: type=content -->

## ServiceAccount

为 Pod 中的进程提供的身份标识

- Pod 身份：让 Pod 可以访问 Kubernetes API
- 自动挂载：Token 自动挂载到 Pod 内
- 权限绑定：通过 RoleBinding 关联权限
- 安全隔离：不同 Pod 使用不同 ServiceAccount

<!-- .slide: type=quote -->

## 设计哲学

> Kubernetes 让开发者专注于应用本身，而不是基础设施的复杂性。

### — K8s 设计理念

<!-- .slide: type=timeline -->

## 典型工作流程

### 1. 编写 Deployment
定义 Pod 模板，包含镜像和端口

### 2. 创建 Service
通过 Label Selector 找到后端 Pod

### 3. 配置 Ingress
设置域名路由规则

### 4. 注入配置
创建 ConfigMap 和 Secret

### 5. 挂载存储
创建 PVC 并挂载到 Pod

<!-- .slide: type=grid -->

## 核心概念回顾

### 架构
- icon: ◉
- color: cyan
- desc: Master + Node，控制与工作分离

### 工作负载
- icon: ◈
- color: purple
- desc: Pod、Deployment、StatefulSet

### 网络
- icon: ◆
- color: pink
- desc: Service、Ingress 服务发现

### 存储
- icon: ▣
- color: orange
- desc: PV、PVC、StorageClass

<!-- .slide: type=end -->

# 感谢观看

## 点赞关注不迷路

作者 | B站/公众号
