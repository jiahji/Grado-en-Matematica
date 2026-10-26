---
title: Funciones de matrices y dinámica discreta / 矩阵函数与离散动力系统
subject: Álgebra Lineal
tema: Guía 4.6
type: exercises
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_4_6
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Ejercicios — Funciones y dinámica

**Fuentes verificadas:** AL-GD-001 p. 6, 4.6; suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


**Instrucciones ES.** Todos los ejercicios son propios. Justifique las condiciones y distinga afirmaciones sobre un estado de las que valen para todos. Niveles orientativos: E01–E03 básicos; E04–E06 intermedios; E07 de síntesis.

**中文。** 先独立写出状态与假设，再做矩阵计算。每个结论应说明是针对一个初值还是所有初值。[理论](01_Teoria_Demostraciones.md)；完成后查看[独立解答](06_Soluciones.md)。

## A46-E01 — función de una matriz

Compare $e^{0_{2\times2}}$ con la matriz obtenida al aplicar la función escalar $e^x$ a cada entrada de $0_{2\times2}$. Explique cuál corresponde a la exponencial del operador y por qué.

## A46-E02 — potencias y caso cero

Para $J=\begin{pmatrix}\lambda&1\\0&\lambda\end{pmatrix}$, calcule $J^k$ para todos los enteros $k\geq0$. Separe $\lambda=0$ de $\lambda\ne0$ y compruebe $k=0,1,2$.

## A46-E03 — exponencial nilpotente

Sea $N=\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix}$. Calcule $e^{tN}$ y pruebe directamente que $e^{sN}e^{tN}=e^{(s+t)N}$.

## A46-E04 — tres propiedades distintas

Para cada matriz, decida si todas las órbitas (a) tienden a cero, (b) están acotadas, (c) convergen. Si convergen, dé el operador límite. Si falla alguna propiedad, exhiba un estado que lo demuestre:

$$
A_1=\operatorname{diag}(1/2,-1/3),\quad A_2=\operatorname{diag}(1,1/2),\quad
A_3=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad A_4=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
$$

## A46-E05 — recurrencia escalar

Resuelva $u_{k+2}=3u_{k+1}-2u_k$ con $u_0=0$, $u_1=1$, mediante un sistema matricial y compruebe la fórmula obtenida por sustitución.

## A46-E06 — función racional en un bloque

Para $J=\lambda I+N$ con $N^2=0$, $\lambda\ne0$, deduzca $J^{-1}$ a partir de $f(z)=1/z$ y verifique multiplicando que es una inversa bilateral. ¿Por qué falla si $\lambda=0$ y $N$ es un bloque nilpotente no nulo?

## A46-E07 — qué estados decaen

Sea $A=P\operatorname{diag}(2,1/2)P^{-1}$ con $P=\begin{pmatrix}1&1\\1&0\end{pmatrix}$. Determine exactamente los estados $x_0$ para los que $A^kx_0\to0$. Calcule $A$ y contraste con la afirmación «hay un autovalor mayor que uno, luego todo estado no nulo crece sin cota».

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
