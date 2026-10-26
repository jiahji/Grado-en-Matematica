---
title: Autoespacios y multiplicidades / 特征空间与重数 — soluciones
subject: Álgebra Lineal
tema: Guía 4.2
type: exercises
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_4_2
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Soluciones 4.2 — 完整解答

**Fuentes verificadas:** AL-GD-001 p. 6, 4.2; suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Resoluciones propias de [A42-E01–E05](05_Ejercicios.md).

## A42-E01

**Estrategia ES.** Triangularidad para característica, sistemas para geometría. **中文。** 两步独立计算。**Resolución.** $\chi=(t-3)^2(t-4)$. Para $3$, $(A-3I)(x,y,z)=(y,0,z)$ fuerza $y=z=0$, así $g_3=1,a_3=2$. Para $4$, $(-x+y,-y,0)=0$ fuerza $x=y=0$, así $g_4=a_4=1$. **Conclusión.** Suma propia de dimensión $2$.

## A42-E02

**Estrategia ES.** Usar ambas cotas y un bloque explícito. **中文。** 几何重数从 1 到代数重数之间。**Demostración.** Si $a_\lambda=1$, $1\le g_\lambda\le1$, así $g=1$. La matriz $\begin{pmatrix}\lambda&1\\0&\lambda\end{pmatrix}$ tiene característica $(t-\lambda)^2$ y núcleo de $A-\lambda I$ generado por $e_1$, por lo que el recíproco falla. **Conclusión.** Raíz simple es condición suficiente, no necesaria para una recta propia.

## A42-E03

**Estrategia ES.** Usar suma directa de valores distintos y grado de la característica. **中文。** 比较实际方向总数与环境维数。**Resolución.** El ambiente tiene dimensión $5$, y la suma de los dos autoespacios tiene dimensión $2+1=3$ por T1. No llena $V$. **Conclusión.** Hay un déficit de direcciones propias y no se pueden obtener cinco autovectores independientes.

## A42-E04

**Estrategia ES.** Aplicar $T$ a una combinación de sus generadores. **中文。** 每个特征向量可以对应不同特征值。**Demostración.** Si $U=\langle v_1,\ldots,v_k\rangle$ con $Tv_i=\lambda_i v_i$, para $u=\sum a_iv_i$ se tiene $Tu=\sum a_i\lambda_i v_i\in U$. **Conclusión.** La invariancia no requiere una sola raíz común.

## A42-E05

**Estrategia ES.** Examinar una descomposición nula completa. **中文。** 一般三个子空间两两无交仍可能相关。**Demostración.** De $u_1+u_2+u_3=0$ con $u_i\in E_{\lambda_i}$, eliminar ceros deja una relación no trivial entre autovectores de valores distintos, imposible por 4.1. Así todos son cero. El ejemplo de tres rectas $e_1,e_2,e_1+e_2$ muestra que solo citar intersecciones por parejas no bastaría para subespacios generales. **Conclusión.** La propiedad espectral extra es esencial.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
