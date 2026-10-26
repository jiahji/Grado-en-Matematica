---
title: Repaso y autoevaluación de matrices / 矩阵复习与自测
subject: Álgebra Lineal
tema: Tema 0 · Matrices · Guía 1.1
type: review
language: es-zh
status: complete
tags:
- algebra_lineal
- matrices
- tema_00
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-000/Tema 0(6).pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Repaso y autoevaluación — 矩阵复习与自测

**Fuentes:** AL-GD-001, página 5, apartado 1.1; AL-AP-000, página PDF 2. Este documento propone una autoevaluación del módulo. No se han recibido exámenes reales ni instrucciones de corrección del profesor, por lo que no se atribuyen frecuencias, puntuaciones ni preguntas obligatorias.

## Definiciones esenciales — 应能准确表述的定义

**En español.** Explicar qué significa $A\in M_{m\times n}(\mathbb K)$, definir igualdad, suma, producto por un escalar y producto matricial por sus entradas. Indicar para cada operación cuándo está definida y el tamaño del resultado.

**中文。** 不能只会“行乘列”的口令。应写出 $(AB)_{ij}=\sum_k a_{ik}b_{kj}$，说明哪些下标固定、哪个求和，以及求和上限为什么是内侧大小。

## Teoremas y demostraciones — 定理与证明训练

**En español.** Poder justificar por entradas la distributividad, la compatibilidad con escalares, la asociatividad y las identidades. En el cuadrado de una suma, separar $AB$ y $BA$ y demostrar cuándo se pueden agrupar.

**中文。** 证明前先列大小；中间每一行都应知道使用的是定义、标量规则还是之前已证的矩阵规则。不能把几个计算例子作为结合律的一般证明。

完整论证见 [证明文件](03_Demostraciones.md)。这份自测建议不等于已核实的教授必考证明清单。

## Reconocer el método — 如何识别解题方法

| 题目结构 | Método en español | 中文操作思路 |
| --- | --- | --- |
| 判断表达式是否有意义 | Comprobar dimensiones antes de operar | 先写每个因子的行数、列数 |
| 矩阵相等或含参数 | Igualar entradas correspondientes | 化成标量条件并验证反向成立 |
| 一般矩阵恒等式 | Comparar una entrada arbitraria | 对任意合法下标证明，不只举例 |
| 否定一般规则 | Construir y verificar un contraejemplo | 检查满足所有前提且确实否定结论 |
| $2X+A=3B$ | Usar suma y escalares de forma reversible | 取消加项合法，非零标量可约 |
| $DX=XD$ | Comparar ambos órdenes y discutir parámetros | 参数差可能为零，分情况处理 |

## Errores frecuentes — 常见失误

**Español.** No confundir $m\times n$ con $n\times m$; no sumar matrices incompatibles; no multiplicar entrada a entrada; no intercambiar factores; no cancelar una matriz por el solo hecho de ser no nula; no confundir «no conmutativo en general» con «ninguna pareja conmuta».

**中文。** 一个高效复查顺序是：对象类型 → 结果大小 → 固定位置的计算 → 符号 → 所用定理的前提 → 最终结论。如果出现不成立的等式，先检查顺序和维数，再重算数值。

## Checklist — 独立完成后自检

- [ ] 能不看笔记写出四种基本定义及相应量词和维数。
- [ ] 能独立完成 M-E01–M-E05 的计算并解释结果大小。
- [ ] 能用完整西班牙语证明分配律和结合律。
- [ ] 能解释加法取消与乘法因子取消的差别，并给有效反例。
- [ ] 能完成 M-E08 的参数分类并证明充分性。
- [ ] 能给出某一对矩阵交换和另一对不交换的例子。
- [ ] 能在中文和西班牙语中准确解释矩阵乘法的中间指标。
- [ ] 对每个未完成项目，记录具体卡在哪条定义、哪一步推理，而非只写“不会”。

M-E11–M-E12 为补充提高题，帮助理解下标和全称量词；目前没有证据把它们视为课程指定考试题。真实考核方式见 [课程大纲整理](../../00_Programa_Docente.md)。

返回 [独立练习](05_Ejercicios.md)、[模块入口](00_Introduccion.md) 或 [Tema 0](../00_Indice.md)。
