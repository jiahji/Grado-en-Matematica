---
title: "Matemáticas UPM — Guía de uso / 使用说明"
subject: "General"
tema: null
type: guide
language: es-zh
status: partial
tags: [navegacion, guia]
sources: []
updated: 2026-10-26
---

# Matemáticas UPM — 数学本科双语知识库

Biblioteca de estudio en español y chino, organizada en archivos Markdown para reconstruir y ampliar materiales reales de las asignaturas. Las definiciones, los enunciados y las demostraciones se redactan en español académico; la motivación, la intuición, las estrategias y las explicaciones se ofrecen tanto en español como en chino.

本库用于完整自学、证明训练、独立练习及考试准备。已开始依据线性代数真实材料编写；讲解、证明策略和例题分析也附上西班牙语，中文用于深入理解。

## Estado actual — 当前状态

截至 2026-10-26，已收到 Álgebra Lineal（线性代数）官方大纲及五份带批注讲义，共 120 页。课程为 UPM 305000100、2026–27。所有原件保留原名和原始字节，详见来源登记。

[Tema 0 / 官方第 1 模块](01_Algebra/Tema_00/00_Indice.md)的四个单元已写齐：矩阵、Gauss 与秩、复数与域、数值/LU/回归，共 32 份学习笔记、25 个例题、48 道独立练习及解答。数值单元与其他扩充已明确标为自主补充，课堂细节不作虚构。其余 23 个官方小节未整体完成，继续按既定范围写作，无需等待全部资料到齐。

用户的建库要求仍保存在 [原始要求](99_Seguimiento/00_Requisitos_Originales.txt)，不计为数学来源。Cálculo 和 Fundamentos 尚缺资料。

## Navegación — 导航

- [总目录](00_Indice_General.md)：课程入口与学习路径的起点。
- [来源登记](00_Fuentes/00_Catalogo_Fuentes.md)：实际收到的课程资料。
- [材料接收规则](00_Fuentes/README.md)：原件、页码、识别与引用。
- [课程覆盖矩阵](99_Seguimiento/Cobertura_Temario.md)：理论、证明、习题与复核状态。
- [待办](99_Seguimiento/Pendientes.md)、[疑点与错误](99_Seguimiento/Errores_Detectados.md)、[修改记录](99_Seguimiento/Registro_Cambios.md)。
- [最新 Tema 0 验证](99_Seguimiento/Validacion_Tema_00.md)、[首批矩阵验证](99_Seguimiento/Validacion_Algebra_Lineal.md) 与 [初始报告](99_Seguimiento/Informe_Validacion.md)：实际检查及限制。
- [Codex 长期规则](AGENTS.md)：后续写作和更新的约束。

## Abrir y editar — 打开与编辑

在 Obsidian 中选择「打开文件夹作为仓库」，选择本 `Matematicas-UPM/` 目录。无需第三方插件；此目录也可以直接用 VS Code、Typora 或普通 Markdown 编辑器打开。

本库不需要启动服务或构建应用。Obsidian 自身创建的设置不属于核心教材内容。标准 Markdown 阅读器的公式显示能力各异；源文件统一使用 MathJax 兼容语法。

文件名使用稳定数字前缀及 ASCII 名称，正文保留完整西班牙语重音和中文。原始资料的文件名优先保持原样。内部导航使用标准 Markdown 相对链接，移动整个知识库时保留目录关系。

## Incorporar materiales — 收到资料后如何处理

1. 指明资料所属课程；有课程代码和学年时一并登记。原件按课程保存到 `00_Fuentes/`，保持内容不变。
2. 在来源目录登记真实文件、类型、读取状态和定位方式。扫描件与手写符号需要核对，未能辨认处写明 `Pendiente de verificación`。
3. 对照官方课程范围和课堂笔记，建立真实章节索引及覆盖条目。课程范围尚不明确时，保留为待核实，不把通用教材目录当作官方目录。
4. 先完成材料支持的第一个逻辑完整单元，包括必要定义、完整证明、中文解释、例题、独立练习及分开的解答。
5. 检查引用、逻辑依赖、数学内容、双语一致性、元数据和实际链接；同步更新目录、覆盖与待办。

教授的定义、符号和方法优先用于还原课堂；有错误或资料冲突时记录原文和依据，在正式笔记中采用正确结论。补充理论、拓展例题和模拟题明确标为补充或自拟。

## Organización — 目录用途

| 目录 | 用途 | 当前情况 |
| --- | --- | --- |
| `00_Fuentes/` | 按科目保存原始课程材料及登记 | 6 份线性代数 PDF，已校验 |
| `01_Algebra/` | Álgebra Lineal（线性代数） | 官方范围已核实，第 1 模块四个单元已写成 |
| `02_Calculo/` | Cálculo（微积分） | 仅课程入口，范围待核实 |
| `03_Fundamentos/` | Fundamentos de Matemáticas（数学基础） | 仅课程入口，范围待核实 |
| `90_Repaso_Global/` | 跨章节复习与综合备考 | 已接入四个单元自测，尚无真实试卷解析 |
| `99_Seguimiento/` | 覆盖、待办、审查、修改与原始要求 | 已建立初始记录 |

线性代数已按真实资料建立 `Tema_00/` 至 `Tema_05/` 索引和 `00_Programa_Docente.md`；有内容时才创建学习笔记，真实试卷到达后再建 `Examenes/`。

## Metadatos y calidad — 元数据与质量

正式学习笔记记录 `title`、`subject`、`tema`、`type`、`language`、`status`、`tags`、`sources` 和 `updated`。`sources` 中仅列已核实、实际存在的来源文件，路径相对于该笔记；正文进一步标明页码或准确定位。自行编写的补充内容明确标注，不伪造教授来源。

学习笔记的类型使用 `definition`、`theorem`、`proof`、`example`、`exercises`、`review`；行政文件另外使用 `guide`、`index`、`rules`、`tracking`。行政文件可保留 `sources: []`；正式笔记通过 `sources` 登记实际数学原件。`status: partial` 表示相应内容仍待补充。

`complete` 仅用于实际写成且通过内容复核的学习笔记，不等于已经过人类教授审核。自动链接或 YAML 检查不能代替数学推理审查。
