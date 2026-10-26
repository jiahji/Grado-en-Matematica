---
title: Ejercicios de LU y regresión / LU 与回归独立练习
subject: Álgebra Lineal
tema: Tema 0 · Guía 1.3
type: exercises
language: es-zh
status: complete
tags:
- algebra_lineal
- lu
- regresion
- suplemento
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
provenance: suplemento_didactico_basado_en_temario
updated: 2026-10-26
---

# Ejercicios de LU y regresión — 独立练习

**Procedencia:** doce ejercicios de elaboración propia para guía 1.3, sin hoja oficial recibida.

**Instrucciones en español.** Declarar la convención $PA=LU$, verificar factores por multiplicación y distinguir cálculo exacto de modelo redondeado. Justificar mínimo y unicidad en regresión. Las respuestas están en [otro archivo](06_Soluciones.md).

**中文说明。** 不只交一个分解或拟合公式；写出条件、计算过程和验证。舍入题明确用三位有效数字模型。

## N-E01 — LU y resolución · básico

Factorizar $A=\begin{pmatrix}2&1\\4&3\end{pmatrix}$ sin intercambios y resolver $Ax=(1,0)^{\mathsf T}$ con las dos sustituciones.

## N-E02 — Necesidad de permutación · demostración

Probar que $A=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ es invertible y no admite $A=LU$ con $L$ inferior unitaria. Construir una factorización $PA=LU$ válida.

## N-E03 — Pivoteo parcial · intermedio

Calcular $PA=LU$ para $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ con pivoteo parcial y resolver $Ax=(3,7)^{\mathsf T}$.Comprobar que se utiliza $Pb$.

## N-E04 — Redondeo · intermedio

Repetir el sistema de N-03 de los ejemplos con $\varepsilon=10^{-4}$ y tres cifras significativas, con y sin intercambio. Calcular después los residuos usando los datos originales exactos.

## N-E05 — Identidad residual · demostración

Para $A$ invertible y $r=b-A\hat x$, probar $x-\hat x=A^{-1}r$ y deducir que $r=0$ equivale a $\hat x=x$ en aritmética exacta. Explicar por qué un residuo simplemente pequeño exige más información.

## N-E06 — Regresión única · intermedio

Hallar la recta de mínimos cuadrados para $(1,2)$, $(2,2)$, $(3,4)$.Calcular residuos, suma de cuadrados y verificar las dos ecuaciones normales.

## N-E07 — Regresión degenerada · intermedio

Describir todos los minimizadores para $(1,0)$, $(1,2)$, $(1,4)$.Dar el error mínimo y explicar qué predicción sí queda determinada.

## N-E08 — Condición de mínimo · demostración

Demostrar necesidad y suficiencia de $X^{\mathsf T}(y-X\theta)=0$ para minimizar $\|y-X\theta\|_2^2$, usando incrementos y sin depender de derivadas.

## N-E09 — Traslación de respuestas · razonamiento

Si los $t_i$ no son todos iguales, probar que sustituir todos los $y_i$ por $y_i+c$ mantiene la pendiente de regresión y suma $c$ al intercepto. ¿Qué ocurre con los residuos?

## N-E10 — Muchos términos independientes · razonamiento

Explicar por qué, para $k$ sistemas con una misma matriz no singular de tamaño $n$, reutilizar $PA=LU$ tiene coste de orden $n^3+kn^2$, frente a repetir $k$ eliminaciones de coste de orden $kn^3$.No se pide medir tiempos de una computadora.

## N-E11 — Rango de la matriz de diseño · demostración

Probar que $X=(1,t_i)_{i=1}^{N}$ tiene dos columnas independientes si y solo si $S_{tt}>0$.Escalonar la matriz $X^{\mathsf T}X$ para mostrar sus pivotes $N$ y $S_{tt}$, sin usar determinantes.

## N-E12 — Condicionamiento explícito · ampliación

Para $0<\varepsilon<1$, sean $A=\operatorname{diag}(\varepsilon,1)$, $b=(\varepsilon,1)^{\mathsf T}$ y $\hat x=(0,1)^{\mathsf T}$.Hallar solución exacta, residuo, error relativo, residuo relativo y $\kappa_\infty(A)$.Comprobar la cota de error.

返回 [学习入口](00_Introduccion.md)。
