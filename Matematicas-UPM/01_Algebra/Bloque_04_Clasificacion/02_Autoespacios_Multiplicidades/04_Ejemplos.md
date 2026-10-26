---
title: Autoespacios y multiplicidades / 特征空间与重数
subject: Álgebra Lineal
tema: Guía 4.2
type: example
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_4_2
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Ejemplos de multiplicidades — 完整例题

**Fuentes verificadas:** AL-GD-001 p. 6, 4.2; suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Ejemplos propios del temario confirmado.

## M-01. Escalar y bloque — 基础

**Enunciado.** Comparar $2I_2$ con $B=\begin{pmatrix}2&1\\0&2\end{pmatrix}$. **Análisis ES.** Tienen igual característica, calcular núcleos. **中文。** 相同多项式不等于相同方向结构。

**Resolución.** Ambas características son $(t-2)^2$. En la primera, $A-2I=0$, así $g_2=2$. En la segunda, $(B-2I)(x,y)=(y,0)$, así $E_2=\langle e_1\rangle$ y $g_2=1$. **Conclusión.** Mismo $a_2=2$, distinta multiplicidad geométrica.

## M-02. Una raíz simple y otra doble — 综合

**Enunciado.** $A=\begin{pmatrix}1&0&0\\0&2&1\\0&0&2\end{pmatrix}$. **Análisis ES.** Separar los dos sistemas. **中文。** 只按对角值计数会漏掉非对角项造成的约束。

**Resolución.** Característica $(t-1)(t-2)^2$. $E_1=\langle e_1\rangle$. Para $2$, $x=0$ y $z=0$, de modo que $E_2=\langle e_2\rangle$. Las dimensiones geométricas suman $2<3$. **Conclusión.** No hay tres direcciones propias independientes.

## M-03. Cota exacta con dos planos — 大学水平

**Enunciado.** $A=\operatorname{diag}(1,1,2,2)$. **Análisis ES.** Identificar componentes directas. **中文。** 重复根也可能完全拥有足够独立方向。

**Resolución.** $E_1=\langle e_1,e_2\rangle$, $E_2=\langle e_3,e_4\rangle$. Ambos tienen $g=a=2$, y su suma directa es todo $\mathbb R^4$ por la base canónica. **Conclusión.** La repetición de valores no impide diagonalizar.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
