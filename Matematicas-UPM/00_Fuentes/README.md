---
title: "Conservación y uso de fuentes / 原始资料管理"
subject: "General"
tema: null
type: guide
language: es-zh
status: partial
tags: [fuentes, trazabilidad]
sources: []
updated: 2026-10-26
---

# Fuentes — 原始资料管理

Las fuentes académicas se conservan sin alterar su contenido. El catálogo registra únicamente archivos realmente recibidos; una instrucción de organización no acredita ningún resultado matemático ni requisito de examen.

目前没有课程资料。建库要求另存于 [原始要求](../99_Seguimiento/00_Requisitos_Originales.txt)，不计入数学来源。

## Recepción y conservación — 接收与保存

1. 确定课程、资料类型、用户提供的标题及可确认的版本或学年；不知道的字段写 `pendiente de verificación`。
2. 在本目录下按课程建立子目录，例如 `Algebra/`、`Calculo/`、`Fundamentos/`。仅在收到资料时建立对应原件目录。
3. 优先保留原始文件名。必要时使用 ASCII 的资料编号目录区分同名文件；不要覆盖已有原件或擅自重命名用户文件。
4. 将接收文件复制到对应目录，核对原始字节或 SHA-256 一致性，保留上传原件。处理稿、提取文本和 OCR 输出应与原件分开标记。
5. 在 [来源登记](00_Catalogo_Fuentes.md) 添加实际记录。不要预填不存在的文件、假定页码或作者。

所有数学笔记使用 UTF-8 Markdown；原始 PDF、图像等保留其原格式，不能用提取文本替代原件。

## Registro mínimo — 来源记录字段

每份实际资料记录：稳定 ID、科目、原始文件的真实相对链接、类型、真实标题、版本或学年（若可核实）、接收日期、读取状态、页码规则与疑点。PDF 或图片可额外记录校验值以核对原件完整性。

ID 应在登记后保持稳定。`Ficha Docente`、`Apuntes`、`Material del profesor`、`Hoja de ejercicios`、`Examen` 与 `Referencia complementaria` 分开归类。资料不完整时写明缺页或覆盖范围。

## Lectura y localización — 读取与定位

- 文本 PDF：先提取文本，再对照页面检查公式。扫描件和手写件按实际可用的本地工具读取，重点核查量词、指标、等号与不等号、箭头、集合符号和矩阵。
- PDF 页序与印刷页码不同，引用时分别说明；没有印刷页码时使用实际 PDF 页序或页面标题。不编造页码。
- 无法可靠辨认之处写 `Pendiente de verificación`，记录具体位置及需要用户核对的符号，不把 OCR 猜测写成正式定义。
- 重要结果在笔记正文记录具体出处；Frontmatter 的 `sources` 记录相对该笔记的真实来源路径。原件登记状态和数学结论审核状态分别追踪。

## Conflictos y suplementos — 冲突与补充

教授采用的定义、符号和方法用于还原课堂，官方大纲用于确认范围。出现矛盾或错误时，在 [错误与疑点记录](../99_Seguimiento/Errores_Detectados.md) 保留原文定位、分析与处理依据，正式教材采用正确数学结论。

为理解而补充的理论、独立设计的例题和模拟卷分别标为补充、自拟或模拟。未经明确授权，不通过外部服务上传私人材料，不向远程仓库推送。

返回 [总目录](../00_Indice_General.md)。
