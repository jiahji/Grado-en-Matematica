---
title: Sistemas lineales y Gauss / 线性方程组与消元：学习入口
subject: Álgebra Lineal
tema: Tema 0 · Guía 1.2
type: review
language: es-zh
status: complete
tags:
- algebra_lineal
- gauss
- sistemas
- rango
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-000/Tema 0(6).pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-004/Tema 4_65298606b99b4fa875367ddfc0765632.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Sistemas lineales y Gauss — 线性方程组与消元

## Fuentes y alcance — 来源与范围

**Fuentes de aula:** AL-AP-000, páginas PDF 3–9, y AL-AP-004, páginas PDF 13–20. **Alcance oficial:** AL-GD-001, p. 5, apartado 1.2. Se usan páginas PDF contadas desde 1. Las pruebas desarrolladas y las actividades propias están identificadas; no se inventa una hoja de problemas oficial.

本模块覆盖线性方程组、等价变形、Gauss 与 Gauss–Jordan、秩、Rouché–Frobenius、自由变量与解集，并展开原讲义第 9 页的同时求解和逆矩阵算法。所有讲解均附西班牙语，完整证明采用正式西班牙语。

## Motivación — 为什么做消元

**Español.** Un sistema puede tener muchas ecuaciones, pero algunas repiten información y otras pueden contradecirse. Eliminar no significa borrar arbitrariamente restricciones: significa sustituir el sistema por otro con exactamente las mismas soluciones, haciendo visibles las restricciones independientes.

**中文。** Gauss 的目的不是“把数字弄小”或“每行都化成 1”，而是保持解集不变，同时让每个新约束负责一个新的未知量。最后出现的零行可能只是重复信息；只有出现 $0=c$ 且 $c\ne0$ 时才是矛盾。

**Ejemplo motivador de elaboración propia.** Las ecuaciones $x+y=2$ y $2x+2y=4$ describen la misma recta: la segunda no reduce las soluciones. Si se cambia el segundo término independiente a $5$, restar el doble de la primera ecuación produce $0=1$, y no existe solución.

中文：系数相关不等于无解；必须同时检查右端。这个区别解释了为何要比较系数矩阵与增广矩阵的秩。

## Prerrequisitos — 前置知识

学习 [矩阵定义与乘法](../01_Matrices/01_Definiciones.md) 和 [运算法则的证明](../01_Matrices/03_Demostraciones.md)，熟悉非零标量的除法。先在 $\mathbb Q$ 或 $\mathbb R$ 上练习；算法也适用于 $\mathbb C$。

**Español.** No se exige haber estudiado determinantes ni el teorema rango–nulidad. Para evitar una prueba circular, el rango se define mediante independencia de columnas y se demuestra por eliminación que coincide con los pivotes. Se explican localmente combinación lineal e independencia, sin dar por estudiado todo el capítulo de espacios vectoriales.

**中文。** “阶梯行数”为何不依赖消元路径，是本单元要证明的内容，不能把它直接当成不需解释的定义。我们用有限个列向量的关系建立不变量，再证明它与主元数相等。

## Ruta de estudio — 学习路线

1. [定义、符号与算法](01_Definiciones.md)。
2. [定理与适用条件](02_Teoremas.md)。
3. [九组完整证明](03_Demostraciones.md)。
4. [六个完整例题](04_Ejemplos.md)：三个原笔记系统、同时求解、求逆和参数讨论。
5. [十二道独立练习](05_Ejercicios.md)，之后查阅 [完整解答](06_Soluciones.md)。
6. [复习与方法选择](07_Repaso_Examen.md)。

## Lectura crítica del material — 原件核对

原件 AL-AP-000 pp. 5、8 的第一个手写例题在 $F_3\leftarrow F_3-3F_1$ 时把第三个系数算成 $-4$，正确值为 $-2$。原记录的 $(2,8,21)$ 不满足第一条方程；正确解为 $(-19,8,42)$。完整重算见例题 G-01，原文追踪见 [错误记录](../../../99_Seguimiento/Errores_Detectados.md)。

**Español.** Se conserva el enunciado original y se corrige el cálculo, sin atribuir el error a una persona cuya autoría no se ha verificado. La comprobación por sustitución es una parte del razonamiento, no un adorno al final.

返回 [Tema 0](../00_Indice.md) 或 [课程索引](../../00_Indice.md)。
