---
title: Anuladores, Cayley–Hamilton y polinomio mínimo / 零化与最小多项式
subject: Álgebra Lineal
tema: Guía 4.5
type: example
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_4_5
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Ejemplos de polinomios de operadores — 完整例题

**Fuentes verificadas:** AL-GD-001 p. 6, 4.5; suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Todo es suplemento propio de 4.5.

## P-01. Inversa y recurrencia — 基础

**Enunciado.** $A=\begin{pmatrix}2&1\\0&3\end{pmatrix}$. **Análisis ES.** Usar $\chi=t^2-5t+6$. **中文。** 零化关系可以同时给逆和高次幂递推。

**Resolución.** $A^2-5A+6I=0$ por Cayley–Hamilton. Los dos valores distintos obligan a que el mínimo tenga ambos factores, así $\mu=\chi$. Despejando y multiplicando, $A^{-1}=(5I-A)/6=\begin{pmatrix}1/2&-1/6\\0&1/3\end{pmatrix}$. Multiplicar ambos lados por $A$ verifica identidad. Para $k\ge0$, $A^{k+2}=5A^{k+1}-6A^k$. **Conclusión.** Todo polinomio se reduce a combinación de $I,A$.

## P-02. Igual característica, distinto mínimo — 综合

**Enunciado.** Comparar $2I_2$ con $J=\begin{pmatrix}2&1\\0&2\end{pmatrix}$. **Análisis ES.** No suponer que característica sea siempre mínima. **中文。** 检查一次因子与二次因子分别是否零化。

**Resolución.** Ambas características son $(t-2)^2$. Para $2I$, $T-2I=0$, así mínimo $t-2$. Para $J$, $N=J-2I\ne0$ pero $N^2=0$. Por divisibilidad del mínimo y falta de anulación lineal, mínimo $(t-2)^2$. **Conclusión.** La segunda no diagonaliza por la raíz repetida del mínimo, aunque las características coincidan.

## P-03. Bézout como proyección — 大学水平

**Enunciado.** Suponer $T^2=T$. **Análisis ES.** Los factores $t$ y $t-1$ son coprimos. **中文。** 互素多项式构造出两个投影分量。

**Resolución.** $1=t-(t-1)$. Evaluando, $v=Tv+(I-T)v$, donde $Tv\in\ker(T-I)$ y $(I-T)v\in\ker T$. La intersección cero se comprueba si $Tv=0$ y $Tv=v$, que fuerzan $v=0$. **Conclusión.** Se recupera la descomposición de proyecciones por la teoría polinómica general; no se usa para probar retrospectivamente un resultado del que dependiera T4.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
