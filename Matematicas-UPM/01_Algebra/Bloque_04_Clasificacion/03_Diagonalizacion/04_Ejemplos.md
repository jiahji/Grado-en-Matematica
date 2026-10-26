---
title: Diagonalización / 对角化
subject: Álgebra Lineal
tema: Guía 4.3
type: example
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_4_3
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Ejemplos de diagonalización — 完整例题

**Fuentes verificadas:** AL-GD-001 p. 6, 4.3; suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Ejemplos propios del alcance oficial.

## Z-01. Dos valores distintos — 基础

**Enunciado.** $A=\begin{pmatrix}2&1\\0&3\end{pmatrix}$. **Análisis ES.** Usar los espacios ya calculados en 4.1. **中文。** 特征值顺序要与 $P$ 的列顺序一致。

**Resolución.** Tomar $P=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ con columnas para $2,3$. $AP=\begin{pmatrix}2&3\\0&3\end{pmatrix}=P\operatorname{diag}(2,3)$. $P$ es invertible con inversa $\begin{pmatrix}1&-1\\0&1\end{pmatrix}$. **Conclusión.** $P^{-1}AP=\operatorname{diag}(2,3)$.

## Z-02. Una raíz doble insuficiente — 综合

**Enunciado.** $B=\begin{pmatrix}2&1\\0&2\end{pmatrix}$. **Análisis ES.** Examinar geometría, no solo raíces. **中文。** 不能因为特征值都是实数就直接宣称可对角化。

**Resolución.** Su única raíz tiene $a_2=2$, pero el sistema $(B-2I)(x,y)=(y,0)=0$ deja solo la recta $e_1$. No hay dos autovectores independientes; el criterio falla. **Conclusión.** No diagonalizable sobre reales ni complejos.

## Z-03. Potencias de una matriz simétrica concreta — 大学水平

**Enunciado.** $A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$, calcular $A^k$. **Análisis ES.** Resolver espacios de $1$ y $3$, sin invocar un teorema general de matrices simétricas. **中文。** 这里只证明这一具体矩阵，不声称已经证明谱定理。

**Resolución.** Para $1$ sirve $(1,-1)$, para $3$ sirve $(1,1)$. Con $P=\begin{pmatrix}1&1\\-1&1\end{pmatrix}$ y $P^{-1}=\frac12\begin{pmatrix}1&-1\\1&1\end{pmatrix}$,

$$
A^k=\frac12\begin{pmatrix}1+3^k&3^k-1\\3^k-1&1+3^k\end{pmatrix},\qquad k\ge0.
$$

En $k=0$ se obtiene identidad y en $k=1$ el original, verificando extremos básicos. **Conclusión.** La diagonalización organiza todas las iteraciones a la vez.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
