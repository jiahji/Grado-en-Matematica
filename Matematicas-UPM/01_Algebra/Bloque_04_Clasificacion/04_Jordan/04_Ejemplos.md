---
title: Forma canónica de Jordan / Jordan 标准形
subject: Álgebra Lineal
tema: Guía 4.4
type: example
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_4_4
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Ejemplos de Jordan — 完整例题

**Fuentes verificadas:** AL-GD-001 p. 6, 4.4; suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Suplemento propio del apartado 4.4.

## J-01. Cadena de longitud tres — 基础

**Enunciado.** $N=\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix}$. **Análisis ES.** Empezar con $e_3$ y aplicar $N$. **中文。** 排列时把最底端放第一列。

**Resolución.** $Ne_3=e_2$, $N^2e_3=e_1$, $N^3e_3=0$. La cadena ordenada es $(e_1,e_2,e_3)$, ya base. Las dimensiones de núcleos son $1,2,3$, así hay un bloque de tamaño $3$. Para $T=\lambda I+N$, la forma es $J_3(\lambda)$ y mínimo $(t-\lambda)^3$. **Conclusión.** Tres vectores generalizados no son tres autovectores: solo $e_1$ es propio.

## J-02. Base no canónica explícita — 综合

**Enunciado.** $A=\begin{pmatrix}3&1\\-1&1\end{pmatrix}$. **Análisis ES.** La característica es $(t-2)^2$; hallar un vector propio y levantarlo. **中文。** 解一个线性方程来找广义特征向量，而不是凭空填基。

**Resolución.** $N=A-2I=\begin{pmatrix}1&1\\-1&-1\end{pmatrix}$, $N^2=0$. Tome $v_1=(1,-1)$ y resuelva $Nv_2=v_1$; sirve $v_2=(1,0)$. Así

$$
P=\begin{pmatrix}1&1\\-1&0\end{pmatrix},\quad
J=\begin{pmatrix}2&1\\0&2\end{pmatrix},\quad
P^{-1}=\begin{pmatrix}0&-1\\1&1\end{pmatrix}.
$$

$AP=\begin{pmatrix}2&3\\-2&-1\end{pmatrix}=PJ$. **Conclusión.** Matriz de cambio y forma se verifican simultáneamente; el generador de altura dos no está en el autoespacio.

## J-03. Recuperar bloques de núcleos — 大学水平

**Enunciado.** Único valor $2$, multiplicidad $6$, y $d_1=3,d_2=5,d_3=6,d_4=6$. **Análisis ES.** Calcular incrementos y diferencias. **中文。** 增量计数“至少这么长”，不是“恰好这么长”。

**Resolución.** $b_1=3,b_2=2,b_3=1,b_4=0$. Hay $b_1-b_2=1$ bloque de tamaño uno, $b_2-b_3=1$ de tamaño dos y $b_3-b_4=1$ de tamaño tres. Forma $J_3(2)\oplus J_2(2)\oplus J_1(2)$. El mínimo es $(t-2)^3$, característica $(t-2)^6$ y dimensión propia $3$. **Conclusión.** Los tamaños suman $3+2+1=6$ y reproducen los datos de núcleos.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
