---
title: Fórmula de Grassmann / Grassmann 维数公式 — soluciones
subject: Álgebra Lineal
tema: Guía 2.7
type: exercises
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_2_7
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-012/Temas 1 y 2(1)(2).pdf
updated: 2026-10-26
---

# Soluciones 2.7 — 完整解答

**Fuentes verificadas:** AL-AP-012, p. 24. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Resoluciones propias de [A27-E01–E05](05_Ejercicios.md).

## A27-E01

**Estrategia ES.** Despejar la dimensión compartida. **中文。** 再检查它不超过较小维数。**Resolución.** Grassmann da $\dim(U\cap W)=3+2-4=1$. Está entre cero y $2$, por lo que la información es consistente. **Conclusión.** La intersección es unidimensional.

## A27-E02

**Estrategia ES.** Usar cotas e igualdad de subespacios de la misma dimensión. **中文。** 排除交集二维，而不是靠图形猜测。**Demostración.** La intersección tiene dimensión al menos $2+2-3=1$ y a lo sumo $2$. Si tuviera $2$, su inclusión en cada plano y la igualdad de dimensiones darían $U=W$, contrario a distintos. Luego su dimensión es $1$. Grassmann da $\dim(U+W)=3$, así la suma es $\mathbb R^3$. **Conclusión.** Ambas afirmaciones quedan justificadas.

## A27-E03

**Estrategia ES.** Usar conjuntos de vectores de la base canónica con solapamientos controlados. **中文。** 共有基向量的数量在这些特定例子中直接给交集维数。**Resolución.** Fijar $U=\langle e_1,e_2,e_3\rangle$. Para dimensión $1$, tomar $W=\langle e_3,e_4,e_5\rangle$; para $2$, $W=\langle e_2,e_3,e_4\rangle$; para $3$, $W=U$. Comparar coordenadas muestra que las intersecciones son respectivamente los generados de $e_3$, de $e_2,e_3$ y de $e_1,e_2,e_3$. **Conclusión.** Se alcanzan todas las posibilidades permitidas por las cotas.

## A27-E04

**Estrategia ES.** Calcular la dimensión de la suma. **中文。** 总维数相同本身不能排除重叠。**Demostración.** Con intersección cero, Grassmann da $\dim(U+W)=\dim V$. La inclusión en $V$ fuerza igualdad, y T2 de suma directa da complementarios. Sin intersección cero, no basta: en $\mathbb R^2$, tomar $U=W=\langle e_1\rangle$; las dimensiones suman $2$ pero la suma sigue siendo solo esa recta. **Conclusión.** El segundo supuesto es esencial.

## A27-E05

**Estrategia ES.** Aplicar la fórmula primero a $U,W$ y después a su suma con $Z$. **中文。** 保留真实的整体交集。**Resolución.**

$$
\dim(U+W+Z)=\dim U+\dim W-\dim(U\cap W)+\dim Z-\dim((U+W)\cap Z).
$$

En general $(U+W)\cap Z$ no coincide con $(U\cap Z)+(W\cap Z)$: las tres rectas de H-03 dan a la izquierda $Z\ne0$ y a la derecha cero. **Conclusión.** Sustituir indebidamente ese término genera la falsa fórmula por parejas.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
