# 歧义与置信度

**永远不要猜测：**这是第一准则。如果需求、事实或细节存在歧义，远好过承认歧义并请求指导（尽可能附带歧义原因），或通过进一步调研把问题落实，而不是冒着出错的风险随意猜测。

# AI 智能体使用说明

本文档用于指导 AI 智能体在本代码仓库中处理代码时的行为规范。

## 快速参考

-   **主分支**：`latest`
-   **代码格式化**：`yarn nx format --sort-root-tsconfig-paths=false`（提交前执行）
-   **类型检查**：`yarn nx build:types <package>`（提交前执行）
-   **代码检查**：`yarn nx lint <package>`（提交前执行）
-   **构建**：`yarn nx build <package>`
-   **单元测试**：`yarn nx test <package>`
-   **端到端测试**：`yarn nx e2e ag-grid-docs`
-   **开发服务**：`yarn nx dev`（启动于 https://localhost:4610/，启动前先检查是否已运行）
-   **NX 守护进程**：所有 nx 命令均使用 `NX_DAEMON=false`，避免管道挂起（已通过 SessionStart 钩子自动设置）

## 内容位置

-   **Rulesync 源文件**：`.rulesync/`（规则、命令、子智能体）
-   **共享提示词**：`external/ag-shared/prompts/`（已软链接至 .rulesync）

---

# 必知清单

-   **基于 Yarn + Nx 的仓库**：使用 Yarn 管理依赖，Nx 统筹构建与测试。
-   **核心约束**：社区版与企业版运行时包，除 AG Grid 自身代码外**无任何第三方运行时依赖**。
-   **默认分支**：目标分支为 `latest`；主题分支遵循下方 release/JIRA 命名规范。
-   **构建监控**：通过 `node_modules/.cache/ag-watch-status.json` 监控监听状态（`yarn nx dev`）与构建健康度（详见[开发服务指南](sslocal://flow/file_open?url=.rulesync%2Frules%2Fdev-server.md&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)）。
-   **提交前自我审查**：像审查他人 PR 一样重读你的修改，并确认：
    -   每个新函数/类职责单一清晰
    -   命名有意义
    -   无不必要复杂度
    -   无应抽取却直接复制粘贴的逻辑
    -   新代码遵循项目现有代码风格与模式
-   **格式化**：提交前从仓库根目录执行 `yarn nx format --sort-root-tsconfig-paths=false`
-   **类型检查**：提交前从仓库根目录执行 `yarn nx build:types <package>`
-   **代码检查**：提交前从仓库根目录执行 `yarn nx lint <package>`
-   **基线验证**：对网格进行重要修改后，需执行：
    -   `yarn nx test ag-grid-community`
    -   `yarn nx test ag-grid-enterprise`
    -   `yarn nx e2e ag-grid-docs`
-   **测试验证规范**：编写或修改测试时，参考同类测试以保持验证逻辑一致（详见[测试指南](sslocal://flow/file_open?url=.rulesync%2Frules%2Ftesting.md&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)）。
-   **上下文文档**：引入新模式前，先浏览 [technology-stack.md](sslocal://flow/file_open?url=.rulesync%2Frules%2Ftechnology-stack.md&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=) 了解技术栈与架构决策。

# 工具健康检查

对话**首次回复**时，通过系统提醒技能列表检查项目技能是否可用。
如果**任意**关键技能缺失，在执行其他操作前**仅显示一次警告**，后续回复不再重复。

**关键技能（哨兵技能）**：`example`、`dev-server`、`debug`、`git-conventions`、`jira`

**缺失时显示的警告**：

> **智能体工具未初始化。** 预期技能（example、dev-server、debug、git-conventions、jira）缺失或不完整。请在仓库根目录执行 `yarn` 完成 AI 工具配置，然后重启会话。若处于工作树（worktree）环境，确保在工作树目录（而非仅主检出目录）执行 `yarn`。

显示警告后继续为用户提供协助。

# 专项指南

如需特定主题的详细说明，查阅以下指南：

-   **[测试指南](sslocal://flow/file_open?url=.rulesync%2Frules%2Ftesting.md&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)** — 测试策略、最佳实践与理念
-   **[示例指南](sslocal://flow/file_open?url=.rulesync%2Frules%2Fexamples.md&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)** — 示例编写、校验与路径映射
-   **[文档页面指南](sslocal://flow/file_open?url=.rulesync%2Frules%2Fdocs-pages.md&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)** — 创建统一、高质量的文档页面
-   **[JIRA 指南](sslocal://flow/file_open?url=.rulesync%2Frules%2Fjira.md&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)** — JIRA 工单搜索与创建规范
-   **[代码质量指南](sslocal://flow/file_open?url=.rulesync%2Frules%2Fcode-quality.md&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)** — 避免代码臃肿、注释规范与审查实践
-   **[开发服务指南](sslocal://flow/file_open?url=.rulesync%2Frules%2Fdev-server.md&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)** — 开发服务配置与构建监听监控
-   **[基准测试指南](sslocal://flow/file_open?url=.rulesync%2Frules%2Fbenchmarks.md&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)** — 运行与创建性能基准测试

# 项目概览

AG Grid 是一个复杂的 TypeScript 单体仓库（monorepo），提供高性能数据表格组件，包含社区版（MIT 协议）与企业版（商业授权）。基于 Nx 构建，支持 React、Angular、Vue 3 框架。

# 技术栈

如需首选技术与架构约束详情，参见[技术栈文档](sslocal://flow/file_open?url=.rulesync%2Frules%2Ftechnology-stack.md&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)。

**核心约束**：AG Grid 主库**运行时零第三方依赖**。

# 仓库规范

-   主分支：`latest`
-   发布分支命名：`b33.0.0` 格式
-   JIRA 相关分支命名：`ag-12345/${短横线分隔的修改说明}`
-   **语言规范**：文档文本、注释、JSDoc 使用**英式英语**；API 配置项名称使用**美式英语**。

# 核心命令

-   `yarn install` — 克隆后或 yarn lock 文件变更时安装依赖
    -   `./external/ag-shared/scripts/install-for-cloud/install-for-cloud.sh` — 远程环境安装依赖与工具，优先使用此脚本而非 `yarn install`，确保全局工具完整安装
-   `yarn nx clean` — 切换分支或打包发布前清空所有 dist 目录
-   `yarn nx format --sort-root-tsconfig-paths=false` — 格式化仓库文件，提交前从项目根目录执行
-   `yarn nx build <package>` — 代码修改后编译指定包
-   `yarn nx build:types <package>` — 修改导出 API 时重新生成声明文件
-   `yarn nx build:package <package>` — 生成 ESM/CJS bundle 验证可发布产物
-   `yarn nx build:umd <package>` — 生成 UMD bundle 用于浏览器分发冒烟测试
-   `yarn nx run-many -t build` — 跨包依赖修改时重新构建所有包
-   `./behave.sh` — 运行 `testing/behavioural/` 行为测试（主测试套件，基于 Vitest）
-   `./behave.sh "<文件匹配模式>"` — 运行指定行为测试文件
-   `./behave.sh "<文件匹配模式>" -t "<测试名称>"` — 按名称运行指定行为测试
-   `./behave.sh --watch` — 监听模式运行行为测试
-   `./behave.sh --update-grid-rows` — 图表格式变更后更新 GridRows 内联快照
-   `./behave.sh --update-grid-rows "<匹配模式>"` — 仅更新匹配测试文件的快照
-   `./behave.sh --update-grid-rows=dry` — 试运行，仅展示变更不写入文件
-   `yarn nx test <package>` — 对受影响包执行 Jest 单元测试
-   `yarn nx test <package> --testPathPattern="<文件名>"` — 测试指定文件
-   `yarn nx test <package> --testPathPattern="<文件名>" --testNamePattern="<测试名>"` — 测试指定文件中的指定用例
-   `yarn nx e2e <package>` — 修改站点行为时运行 Playwright 流程
-   `yarn nx lint <package>` — 最终审查前执行 ESLint 与自定义规则

# 斜杠命令

通过斜杠语法运行 rulesync 命令：

-   `/pr-review` — 审查拉取请求
-   `/code-cleanup` — 精简代码臃肿、生产化优化
-   `/code-fixup` — 修复构建与 lint 错误
-   `/batch-lint-cleanup` — ESLint 自动修复工具
-   `/git-split` — 拆分大文件并保留 Git 历史
-   `/git-bisect` — 定位引入问题的提交
-   `/remember` — 保存分支上下文或项目经验为记忆
-   `/recall` — 加载分支上下文并浏览项目记忆
-   `/docs-review` — 审查文档页面技术准确性
-   `/release-docs-review` — 审查版本间所有文档变更

# 架构

## 单体仓库结构

-   **packages/ag-grid-community/**：MIT 协议版，核心表格功能
-   **packages/ag-grid-enterprise/**：商业版，包含高级特性
-   **packages/ag-grid-react/angular/vue3/**：框架封装层
-   **community-modules/locale/**：国际化支持
-   **community-modules/styles/**：表格样式与主题
-   **documentation/ag-grid-docs/**：Astro 文档站点
-   **testing/**：E2E、行为、可访问性、性能测试
-   **plugins/**：用于代码生成的 Nx 插件
-   **external/**：AG 生态共享代码（ag-shared）

## 构建依赖

核心依赖链：
`ag-grid-community` → `ag-grid-enterprise` → 框架封装层

## 核心模式

-   **虚拟 DOM 渲染**：高性能自定义渲染引擎
-   **模块化特性架构**：通过模块注册实现可扩展表格特性
-   **框架无关核心**：核心与框架特定封装层清晰分离
-   **企业版/社区版分离**：通过独立包实现特性标记

# 开发工作流

## 测试

完整测试说明参见[测试指南](sslocal://flow/file_open?url=.rulesync%2Frules%2Ftesting.md&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)。

**行为测试为主测试套件**。验证表格修改时优先运行行为测试。
主要测试工具：

-   **行为测试（主）**：`testing/behavioural/`，用于验证表格行为 — 使用 Vitest
-   **单元测试**：Jest + jsdom 环境，包级别测试
-   **E2E 测试**：Playwright，站点交互测试
-   **可访问性测试**：`testing/accessibility/`，a11y 合规校验
-   **性能测试**：`testing/performance/`，性能回归测试

## 代码质量

代码质量规范参见[代码质量指南](sslocal://flow/file_open?url=.rulesync%2Frules%2Fcode-quality.md&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)。

核心实践：

-   提交前执行 `yarn nx format --sort-root-tsconfig-paths=false`
-   提交前自我审查修改
-   确保测试覆盖真实实现，而非仅测试辅助工具

## 样式

表格正从**传统主题**（`/community-modules/styles/` 下的 Sass .scss）
向**主题 API**（`/packages/` 下的现代嵌套 CSS .css）迁移。

迁移期间，对主题 API 的修改必须同步到传统主题。
若 PR 修改了主题 API CSS 但未同步传统主题，应标记为 **P1 级问题**。

# 常见开发任务

## 快速流程

### 缺陷修复或特性开发（社区版/企业版）

1. 修改对应实现（通常在 `packages/ag-grid-*/src/`）
2. 同步相关文档/示例
3. 运行：
    - `yarn nx test ag-grid-community`
    - `yarn nx test ag-grid-enterprise`

### 文档/内容更新

1. 查阅[文档页面指南](sslocal://flow/file_open?url=.rulesync%2Frules%2Fdocs-pages.md&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)了解结构与模式
2. 在 `documentation/ag-grid-docs/` 下修改对应内容
3. 按[示例指南](sslocal://flow/file_open?url=.rulesync%2Frules%2Fexamples.md&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)在 `_examples/` 创建或更新示例
4. 确保所有示例兼容各框架
5. 使用 `yarn nx dev` 在开发服务中跨框架测试页面
6. 重大文档变更需用 `yarn nx e2e ag-grid-docs` 做完整性检查

### 仅示例修改（参见[示例指南](sslocal://flow/file_open?url=.rulesync%2Frules%2Fexamples.md&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)）

1. 编辑示例文件
2. 在对应文档页面同步更新
3. 执行相关生成/类型检查命令

# 技术要求

-   **Node.js**：版本见 `.nvmrc`
-   **包管理器**：Yarn
-   **构建目标**：ES2020
-   **TypeScript**：所有包启用严格模式

# JIRA 工单

JIRA 工单规范参见[JIRA 指南](sslocal://flow/file_open?url=.rulesync%2Frules%2Fjira.md&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)。

为本仓库创建工单时，组件选择 **Grid** 而非 **Charts**。

# 文档资源

-   AG Grid 官方文档：https://ag-grid.com/documentation/
