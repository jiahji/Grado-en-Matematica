---
title: "Registro de cambios / 重要修改记录"
subject: "General"
tema: null
type: tracking
language: es-zh
status: partial
tags: [cambios, seguimiento]
sources: []
updated: 2026-10-26
---

# Registro de cambios — 重要修改记录

Se registran cambios de contenido, organización y revisión que afectan al estudio o a la trazabilidad. Cada entrada debe describir lo realmente realizado, sin convertir la creación de archivos en una declaración de cobertura matemática.

## 2026-10-26 — Inicialización / 首次建库

- 检查现有空仓库与上传内容；确认上传文件为完整建库要求，未包含官方大纲、课堂笔记、习题或试卷。
- 在现有仓库内建立 `Matematicas-UPM/`，作为可直接打开的 Obsidian Vault；创建仓库入口与规则指引。
- 将原始用户要求逐字节复制到 [00_Requisitos_Originales.txt](00_Requisitos_Originales.txt)，保存大小与校验值，保留上传原件不变；不将其列作数学资料。
- 建立使用说明、长期规则、总目录、来源登记及 Álgebra、Cálculo、Fundamentos de Matemáticas 三门课程入口。
- 建立跨章节复习入口、大纲覆盖矩阵、待办、错误与疑点登记及验证报告。
- 尚无可核实课程单元，未创建 `Tema_XX/`、正式数学笔记或试卷解析；正式学习模块为 0。
- 原有仓库无内容文件可修改；本次为新增知识库基础文件。文件检查和限制详见 [验证报告](Informe_Validacion.md)。

## 2026-10-26 — Sincronización Git / Git 同步授权

- 用户明确要求“上传至git”，授权将当前知识库同步至原仓库 `jiahji/Grado-en-Matematica`。
- 同步范围为仓库入口与规则、Vault 内 14 份 Markdown 以及原始要求副本，共 17 个文件。
- 已核对远端仓库为空；首次提交的推送目标为 `main` 分支。实际提交与同步结果以 Git 历史和远端分支记录为准。
- 将初始验证报告中的 Git 状态明确为当时的检查结果，保留建库阶段的历史记录。

## 2026-10-26 — Álgebra Lineal: fuentes y primer módulo / 线性代数首批材料

- 接收并原样保存 6 份 PDF，共 120 页，登记真实课程 305000100、2026–27 与来源 ID、页数和 SHA-256。
- 用户新增要求：讲解部分也附西班牙语。已在长期规则中持久化，首个模块的动机、直觉、策略、例题分析均提供 ES + 中文。
- 保留稳定目录名 `01_Algebra/`；建立官方 4 个模块、27 个小节与讲义 Tema 0–5 的对应关系，不混淆两套编号。
- 完成官方 1.1 矩阵运算的 8 份学习文件：定义、定理、六组完整证明、7 个例题、12 道独立练习与解答、复习自测；一个例题保留可辨认的课堂批注，其余补充材料明确标为自拟。
- 记录 9 项已确认的条件缺失、文字/编号问题及现有手写纠正，不修改原 PDF，不声称所有手写页均已复核。
- 保留其余 26 项的待办；单列 1.3、3.7、3.8、4.1–4.6 等缺少专项材料的内容，更新总目录、来源、覆盖与复习入口。
- 本批检查、数学复核范围及限制见 [Validacion_Algebra_Lineal.md](Validacion_Algebra_Lineal.md)。本记录描述本地文件工作，远程同步状态另以 Git 实际记录为准。

## 2026-10-26 — Continuación del bloque 1 / 第 1 模块持续编写

- 按用户“无需等待其他资料补齐”的要求继续实际教材写作，将此规则持久化；标准补充不冒充课堂原文。
- 新增 Gauss/秩/相容判别、复数与域、数值/LU/回归三个完整单元，共 24 份学习笔记、24 组逐步证明、18 个例题和 36 道自拟练习及独立解答。
- 与此前矩阵单元共同构成官方 1.1–1.4 的四个单元：共 32 份学习文件、30 组证明、25 个例题和 48 道练习；不按文件数虚增模块完成数。
- 原样保留并高分辨率重读课堂手写例题，确认原系统消元中的 -4 应为 -2，记录 AL-ERR-010，并用正确解 (-19,8,42) 回代所有原方程。
- 数值部分由大纲 1.3 的范围自主展开，包括带选主元 LU 的存在性、残差与条件数、三位有效数字例子、正规方程充要条件和退化回归；未伪造课堂页码。
- 本阶段新增 60 项精确与舍入计算核对全部通过；另重跑原矩阵的 20 项核对。文件与推理检查的完整范围见 [Validacion_Tema_00.md](Validacion_Tema_00.md)。
- 更新课程、全库导航、覆盖、待办与复习链接；保留首批验证报告作为历史，不将尚未编写的后续官方章节标为完成。

## Criterio para futuras entradas — 后续记录要求

新材料到达后记录其实际来源 ID、影响的章节、定义或证明的重要修订、题目编号变化、已处理冲突和覆盖状态的实际改变。保留既有历史及用户记录，只做最小必要追加或修正。

返回 [总目录](../00_Indice_General.md)。
