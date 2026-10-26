---
title: Operaciones con matrices / 矩阵运算：学习入口
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

# Operaciones con matrices — 矩阵运算

## Alcance y fuentes — 范围与来源

**Fuente de aula:** AL-AP-000, *Tema 0(6).pdf*, página PDF 2, «Operaciones con matrices», con anotaciones manuscritas. **Alcance oficial:** AL-GD-001, página 5, apartado 1.1. Las definiciones por índices, las demostraciones desarrolladas, los contraejemplos y los ejercicios señalados como propios son ampliación didáctica; no se atribuyen al profesor.

本模块完整展开官方 1.1：矩阵、相等、加法、数乘和乘法。零矩阵、单位矩阵及矩阵幂服务于这些运算。Gauss、秩、逆矩阵算法、复数和域的系统学习属于本章后续内容，不以本模块完成代替整章完成。

## Motivación — 为什么需要矩阵

**Explicación en español.** Una matriz（矩阵）permite registrar simultáneamente muchas cantidades y las relaciones entre ellas. Por ejemplo, las filas de una tabla pueden representar dos semanas y sus columnas tres productos. Si otra tabla indica cuánto material necesita cada producto, combinar las dos tablas debe sumar las contribuciones de los tres productos. Esta necesidad conduce al producto fila por columna, no a multiplicar las entradas situadas en la misma posición.

**中文解释。** 单张表只是整理数据；线性代数关心的是“怎样把一组输入系统地变成一组输出”。例如第一张表记录每周生产各种产品的数量，第二张表记录每种产品消耗的材料，结果要告诉我们每周共消耗多少材料。每种产品都作出贡献，所以要先逐项相乘，再对产品编号求和。

Un ejemplo de elaboración propia es

$$
Q=\begin{pmatrix}1&2&0\\0&1&3\end{pmatrix},\qquad
P=\begin{pmatrix}2&1\\1&4\\3&0\end{pmatrix}.
$$

Las filas de $Q$ son semanas; sus columnas, productos. Las filas de $P$ son esos mismos productos; sus columnas, materiales. Entonces

$$
QP=\begin{pmatrix}4&9\\10&4\end{pmatrix}.
$$

La primera entrada es $1\cdot2+2\cdot1+0\cdot3=4$. El índice que recorre los productos se suma y desaparece; quedan los índices semana y material.

中文：中间的“产品”必须对齐。这正是 $(2\times3)(3\times2)$ 能相乘且结果为 $2\times2$ 的原因，维数条件来自问题含义，而不是死记格式。

## Conocimientos previos — 前置知识

Trabajaremos sobre $\mathbb K=\mathbb Q,\mathbb R$ o $\mathbb C$, como indican AL-AP-000, página 15, y la guía, apartado 1.4. Basta conocer la aritmética de los escalares y las sumas finitas. Los ejemplos iniciales usan números reales o racionales.

中文：本模块不依赖向量空间、基或行列式。需要区分“一个数”和“一个数表”，以及熟悉有限求和。复数尚不熟练时，可先把 $\mathbb K$ 理解为 $\mathbb R$；它不会改变矩阵下标和维数规则。

## Ruta de estudio — 学习顺序

1. [严格定义与符号](01_Definiciones.md)：把行、列、下标和运算条件写清楚。
2. [性质与适用条件](02_Teoremas.md)：学习哪些数的规则可以推广到矩阵。
3. [逐步证明](03_Demostraciones.md)：通过比较每个位置的元素证明矩阵等式。
4. [完整例题](04_Ejemplos.md)：先辨认类型，再计算，再解释。
5. [独立练习](05_Ejercicios.md)：先独立作答。
6. [完整解答](06_Soluciones.md)：对照题号查阅，核对证明依据。
7. [复习与自测](07_Repaso_Examen.md)：检验定义、计算与论证能力。

## Conexiones y continuación — 关联与后续

**En español.** El producto matriz-columna permitirá escribir un sistema como $Ax=b$. La distributividad y la asociatividad explicarán por qué las matrices representan transformaciones compatibles con las combinaciones lineales. Estas son conexiones futuras, no requisitos previos de este módulo.

**中文。** 之后的 Gauss 方法会把矩阵当作线性方程组的编码；线性映射课程会把矩阵当作映射在基下的表示。现在先掌握运算本身，避免用尚未证明的秩、行列式或维数定理绕回证明这些基本规则。

返回 [Tema 0 索引](../00_Indice.md) 或 [课程索引](../../00_Indice.md)。
