---
title: Determinantes y formas alternadas / 行列式与交替多线性形式
subject: Álgebra Lineal
tema: Guía 3.7
type: example
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_3_7
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Ejemplos de determinantes — 完整例题

**Fuentes verificadas:** AL-GD-001 p. 6, 3.7; desarrollo propio sin apuntes específicos recibidos. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Todo el desarrollo es suplemento propio del alcance oficial.

## D-01. Dos cálculos del mismo determinante — 基础

**Enunciado.** $A=\begin{pmatrix}1&2&0\\0&3&1\\2&0&1\end{pmatrix}$. **Análisis ES.** Expansión y eliminación deben coincidir. **中文。** 不同方法可用于交叉检查符号。

**Resolución.** Por primera fila, $\det A=1(3\cdot1-1\cdot0)-2(0\cdot1-1\cdot2)=7$. Por Gauss, $F_3\leftarrow F_3-2F_1$ da $(0,-4,1)$ y después sumar $(4/3)F_2$ da $(0,0,7/3)$. Ninguna operación cambia determinante; producto diagonal $1\cdot3\cdot7/3=7$. **Conclusión.** Coinciden ambos cálculos.

## D-02. Adjunta e inversa — 综合

**Enunciado.** Invertir $A=\begin{pmatrix}2&1\\3&2\end{pmatrix}$. **Análisis ES.** Calcular determinante y trasponer cofactores. **中文。** 对角余子式和非对角符号都要正确。

**Resolución.** $\det A=4-3=1$, matriz de cofactores $\begin{pmatrix}2&-3\\-1&2\end{pmatrix}$, adjunta $\begin{pmatrix}2&-1\\-3&2\end{pmatrix}$. Es la inversa; multiplicar por $A$ a cada lado da identidad. **Conclusión.** Omitir la trasposición daría un resultado incorrecto.

## D-03. Una forma alternada — 大学水平

**Enunciado.** Clasificar formas bilineales alternadas en $\mathbb R^2$. **Análisis ES.** Expandir en $e_1,e_2$. **中文。** 一个数应决定所有输入的输出。

**Resolución.** Sea $c=\omega(e_1,e_2)$. Por alternación, valores diagonales son cero y $\omega(e_2,e_1)=-c$. Para $u=(a,b)$ y $v=(d,e)$, multilinealidad da $\omega(u,v)=c(ae-bd)$. A la inversa, cualquier $c$ produce una forma bilineal alternada por esa fórmula. **Conclusión.** El espacio de tales formas tiene una sola dirección y el determinante es la normalizada con $c=1$.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
