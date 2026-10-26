---
title: "Reglas de trabajo de Codex / 长期工作规则"
subject: "General"
tema: null
type: rules
language: es-zh
status: partial
tags: [reglas, mantenimiento]
sources: []
updated: 2026-10-26
---

# Reglas de trabajo — Codex 长期规则

本项目是 UPM 数学本科中西双语知识库。完整原始要求保存在 [00_Requisitos_Originales.txt](99_Seguimiento/00_Requisitos_Originales.txt)；该文件是工作要求，不是课程来源。结合仓库上层规则执行，新增要求应兼容合并，保留已有规则。

## 1. Inspección y alcance — 开始任务

- 先读取本文件、[总目录](00_Indice_General.md)、[来源登记](00_Fuentes/00_Catalogo_Fuentes.md)、[覆盖矩阵](99_Seguimiento/Cobertura_Temario.md) 和 [待办](99_Seguimiento/Pendientes.md)，再检查相关目录、课程资料与用户现有改动。
- 使用当前知识库目录，不重复嵌套。云任务已有隔离，使用现有检出目录；用户未明确要求时不创建 Git worktree。
- 先读 Ficha Docente / Guía Docente 和课堂笔记，再确定章节。不得把示例目录、常见教材目录或用户提及的课程名当作已核实的官方教学范围。
- 没有课程材料时完成可用的组织与追踪工作，记录缺失；不凭空编写整门课程或把空框架报告成教材完成。
- 大型任务分阶段完成可交付的完整知识模块，准确记录剩余工作。不以节省篇幅为由删去必要定义、证明或解释。
- 用户已明确要求“开始编写教材，无需等待其他资料补齐”。在官方大纲已确认的范围内，现有资料不足处可自主编写标准理论、完整证明及自拟训练，明确标为补充教材。缺少课堂原件只限制教授出处、课堂偏好和具体实践要求的归属，不能作为停止标准教材写作的理由。

## 2. Fuentes y originalidad — 来源与原件

- 优先级：教授实际采用的定义、符号和方法；官方课程范围；必要补充理论；适度拓展。数学正确性始终优先。
- 原始资料不可覆盖、删除或擅自改动。接收时保留原名及原始字节；需要整理位置时保留原件，复制后核对一致性并登记。
- 原始材料、课堂还原、必要补充、自拟例题和模拟题必须明确区分。重要定义、定理、证明及题目尽可能记录真实文件和可靠定位，不伪造页码、引文、考试要求、出现概率或教授偏好。
- PDF 的文件页序和印刷页码分别标明，不凭空补上缺失页码。OCR 只辅助识别；扫描、手写公式逐一核查量词、上下标、正负号、箭头、集合关系和矩阵结构。无法可靠识别处标记 `Pendiente de verificación`，不把猜测当作原文。
- 资料矛盾或数学错误记录到 [Errores_Detectados.md](99_Seguimiento/Errores_Detectados.md)：原始表述、真实定位、问题原因、正确结论、修改依据、受影响文件和处理状态。正式笔记使用正确结论，保留原文可追溯性。
- 未经明确授权，不推送远程、不发布互联网、不将私人资料上传到外部服务。原件的本地读取和核对不需要对外上传。

## 3. Idiomas y rigor — 语言与严谨性

- 所有教学内容实际保存为 UTF-8 `.md`；数学公式采用 MathJax / LaTeX。核心内容不依赖数据库、专有格式或第三方 Obsidian 插件。
- Definiciones、Proposiciones、Teoremas、Lemas、Corolarios、Demostraciones、习题题干和考试解答使用规范西班牙语。
- 中文用于概念动机、数学直觉、量词与符号解释、证明策略、逐步逻辑、方法联系和误区纠正，不能仅机械翻译西班牙语。依据用户 2026-10-26 的补充要求，所有这些讲解部分也必须附上西班牙语；动机、策略、例题分析及关键推理解释均提供 ES + 中文，而不只让正式定义和证明使用西班牙语。
- 专业术语首次出现时同时写西班牙语和中文。双语中的假设与结论保持一致。
- 定义明确对象、变量、量词、假设、条件；区分必要、充分和等价。定理完整列出假设与结论，解释适用条件、用途、误用及必要反例。
- 要求掌握的证明采用 Hipótesis、Tesis、Estrategia（西班牙语＋中文）、Demostración（西班牙语）、Explicación detallada（西班牙语＋中文）、Conclusión；每一步解释推理依据，不以“显然”“容易得到”跳过关键步骤。
- 按材料需要训练直接证明、逆否、反证、数学归纳、结构归纳、分类讨论、双包含、反例构造和等价证明，不能声称某方法已纳入课程而没有依据。

## 4. Unidad didáctica — 教学单元

- 一个文件对应一个逻辑完整、能独立学习的单元。按概念关系拆分，不按任意字数拆分；不把几十个独立概念堆成巨型文件。
- 重要知识点根据实际需要包括 Motivación、Definición formal、Intuición matemática、Propiedades y teoremas、Demostración paso a paso、Ejemplos resueltos、Contraejemplos、Conexiones 和 Aplicación en exámenes。
- 从具体问题进入抽象定义，解释引入新概念的必要性和与已有知识的关系。例题尽量覆盖基础、综合及大学水平，但未经核实不能标为真实考试题。
- 完整例题包括西班牙语题干、问题分析、逐步西班牙语解答、中文关键解释、结论及常见错误。教授例题优先保留，补充例题标明自拟或来源。
- 必要时提供反例检验假设边界，逐项说明为何满足前提、为何不满足结论。

## 5. Archivos y enlaces — 文件与链接

- 文件名优先采用无空格 ASCII、稳定数字前缀与明确数学概念。已有稳定文件名不随意改变，不产生 `final_final_v3` 等重复版本。
- 章节按真实 Ficha Docente 组织。常规 Tema 可按需要建立 `00_Introduccion.md`、`01_Definiciones.md`、`02_Teoremas.md`、`03_Demostraciones.md`、`04_Ejemplos.md`、`05_Ejercicios.md`、`06_Soluciones.md`、`07_Repaso_Examen.md`，并建立章节索引；无内容时只登记待办，不批量创建空笔记。
- 已写的官方 2.1–4.6 单元采用四份逻辑完整文件：`01_Teoria_Demostraciones.md`、`04_Ejemplos.md`、`05_Ejercicios.md`、`06_Soluciones.md`。理论文件内含动机、定义、完整证明、双语解释及复习；不为凑齐八文件而拆出空页。官方第 4 模块保留独立目录 `Bloque_04_Clasificacion/`，不得与讲义 `Tema_04/` 混淆。
- 大型主题可分 `Conceptos/`、`Teoremas/`、`Demostraciones/`。名称与层级由实际内容决定。
- 标题使用标准 Markdown 层级。行内公式用单美元符号，独立公式用单独成行的双美元符号，多步推导可用 `aligned`。能表达为 LaTeX 的公式不以图片替代，不放入代码块，展示语法除外。
- 默认用标准 Markdown 相对链接，按实际文件位置计算；链接目标必须存在。未明确要求时不用 Wikilink，不写本机绝对路径到知识库导航中。
- 明确区分必要前置知识、定理的实际逻辑依赖、一般关联、后续学习顺序；不能将所有相关内容都写成严格前提。重要笔记按需要列 Conocimientos previos、Conexiones、Siguientes temas。
- 新增笔记时检查出入链接，并更新所属 Tema 索引、课程索引和必要的总目录。

## 6. Metadatos — 元数据

- 正式学习笔记必须有合法 YAML Frontmatter，记录 `title`、`subject`、`tema`、`type`、`language: es-zh`、`status`、`tags`、`sources`、`updated`。
- 学习类型使用 `definition / theorem / proof / example / exercises / review`；导航和管理文件可使用 `index / guide / rules / tracking`，不要混入教学完成数量。
- 状态使用 `partial / pending_review / complete`。未经内容审查不标 `complete`；已写但未复核的笔记可标 `pending_review`。`complete` 不表示人类教授审核。
- `sources` 只登记真实、已核实来源文件，路径相对笔记本身；正文进一步写明具体页码或定位。无实际数学来源时用空列表，并明确补充或原创内容的性质，不伪造引用。
- 日期使用真实最后编辑日期；行政索引的完成不能替代数学内容的完成。

## 7. Ejercicios y exámenes — 练习与备考

- 练习与解答分文件。题目保留稳定编号、真实出处、所属知识点及有依据的难度；新增题明确标为补充训练。
- 解答沿用题号，西班牙语完整推导，中文解释策略与易错点。不要在每道独立练习下直接放答案。
- 大题集拆分时维护编号和题目—解答链接，不复制互相矛盾的版本。
- 真实试卷到达后才建立相应 `Examenes/` 解析，年份、考试类型和来源据原件登记；自拟模拟卷明确写 `Simulacro de elaboración propia`。
- 复习整理必要定义、重要定理、基本证明、代表习题、常见错误和考试检查单，考试重点的判断必须有真实材料支持。

## 8. Actualización y control — 增量维护与复核

- 每次新资料到达：检查已有内容 → 登记并核对原件 → 对应真实 Tema → 比较新增、修订、矛盾和重复 → 最小必要修改 → 修复链接 → 更新目录、覆盖及重要修改记录。
- 保留用户批注、例题、个人理解及手动修改，不整库重建，不擅自移动、删除或重命名已有文件。
- 在 [Cobertura_Temario.md](99_Seguimiento/Cobertura_Temario.md) 为每个真实 Tema 跟踪尚未开始、正在编写、理论完成、证明检查、习题与解答整理、全部复核。所有大纲内未覆盖条目保留待办。
- 数学复核：定义完整，定理条件准确，推导与证明无逻辑缺口，反例有效；教学复核：能独立学习，有足够直觉、解释和例题，覆盖实际课堂内容；语言复核：西班牙语规范、中文清楚、双语一致。
- 文件复核：UTF-8、Markdown 层级、公式分隔符与明显 LaTeX 问题、合法 YAML、实际相对链接、图片附件、章节目录及落盘情况。可使用本地脚本辅助，但不能用语法检查替代数学证明审查。
- 只报告真正执行的检查，记录不能确认的事项。没有资料时不能写“数学审核通过”或虚构覆盖率。
- 结束时简洁报告新增/修改文件、实际完成知识范围、缺失材料、未核实事项和下一步。教材以磁盘文件为准，聊天中不重复粘贴整本教材。

优先级：数学正确性 > 内容完整性 > 理解深度 > 证明严谨性 > 文件组织 > 可维护性。
