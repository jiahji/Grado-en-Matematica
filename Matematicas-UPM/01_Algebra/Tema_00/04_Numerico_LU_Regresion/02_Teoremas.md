---
title: Teoremas de LU y regresión / LU 与回归定理
subject: Álgebra Lineal
tema: Tema 0 · Guía 1.3
type: theorem
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

# Teoremas de LU y regresión — 性质与前提

**Procedencia:** elaboración propia para AL-GD-001 1.3. Todas las justificaciones están en [Demostraciones](03_Demostraciones.md).

## T1. Resolución triangular y reutilización

Una matriz triangular con diagonal no nula tiene solución única para cada término independiente mediante las sustituciones indicadas. Si $PA=LU$ con diagonales no nulas, resolver $Ly=Pb$ y $Ux=y$ produce la solución única de $Ax=b$.

**Español.** Una vez factorizada la matriz, cada nuevo término independiente requiere dos sustituciones, con un número de operaciones de orden $n^2$; la factorización densa tiene orden $n^3$.

**中文。** 分解的成本主要在第一次；多个右端可以复用同一组因子，不必反复重做整套消元。这里比较的是随大小增长的运算阶数，不是实际机器计时。

## T2. Existencia y unicidad — 分解条件

Si Gauss sin intercambios puede realizarse con todos los pivotes no nulos, produce $A=LU$ con $L$ inferior unitaria y $U$ superior no singular; esta factorización es única. Toda matriz cuadrada no singular admite alguna $PA=LU$ con $P$ de permutación. La matriz $P$ puede depender de las elecciones de pivote.

**Español.** «Invertible» no implica existencia de LU sin permutaciones. La matriz $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ es un contraejemplo. Pivoteo parcial proporciona pivotes no nulos en aritmética exacta, pero no garantiza un pequeño error para cualquier problema mal condicionado.

**中文。** LU 的存在、规范下的唯一性、带行交换分解的存在，是三条条件不同的结论。选主元改善某些数值风险，不改变原问题本身的敏感程度。

## T3. Error controlado por residuo — 残差与误差界

Si $A$ es no singular y $r=b-A\hat x$, entonces

$$
e=A^{-1}r,\qquad\|e\|_\infty\le\|A^{-1}\|_\infty\|r\|_\infty.
$$

Si además $b\ne0$,

$$
\frac{\|x-\hat x\|_\infty}{\|x\|_\infty}
\le\kappa_\infty(A)\frac{\|b-A\hat x\|_\infty}{\|b\|_\infty}.
$$

**Español.** Un residuo pequeño no implica por sí solo error relativo pequeño: puede multiplicarse por un número de condición grande. Para $b=0$, la cota absoluta sigue siendo válida, pero no se usa la expresión relativa anterior.

**中文。** 误差与残差不是同一个量。实践中还要考虑计算残差本身的舍入；本定理首先是精确实数运算下的关系。

## T4. Caracterización de mínimos cuadrados — 最小二乘判别

Para datos reales y matriz de diseño $X$, un parámetro $\theta$ minimiza $\|y-X\theta\|_2^2$ si y solo si

$$
X^{\mathsf T}(y-X\theta)=0.
$$

Equivale a las ecuaciones normales. Se aplica aunque el sistema exacto $X\theta=y$ no tenga solución.

**Español.** Las dos sumas de residuos de la regresión son $\sum r_i=0$ y $\sum t_ir_i=0$.No exige que cada residuo individual sea cero.

**中文。** 误差在两个设计列方向上的合成效应为零，不代表每个数据点都落在线上。不要把正规方程与原来的超定系统混为一谈。

## T5. Fórmula de regresión y caso degenerado — 回归公式与退化情形

Si $S_{tt}>0$, la recta de mínimos cuadrados es única y viene dada por

$$
\beta_* =\frac{S_{ty}}{S_{tt}},\qquad\alpha_*=\bar y-\beta_*\bar t.
$$

La condición $S_{tt}>0$ equivale a que no todos los $t_i$ sean iguales y a que las dos columnas de $X$ sean independientes. Si todos los $t_i=t_0$, los minimizadores son exactamente $\alpha+\beta t_0=\bar y$; la recta no se determina de manera única, aunque la predicción en $t_0$ sí.

**Español.** La prueba completa cuadrados y demuestra mínimo global y unicidad, sin depender solo de anular derivadas. Resolver ecuaciones normales es útil para la derivación; en cómputo sensible deben evitarse conclusiones de estabilidad que no se han demostrado.

**中文。** 分母为零不是简单报错结束：退化数据仍有最小值，只是无法唯一分离截距与斜率。教材会完整说明这一分支。

继续 [七组证明](03_Demostraciones.md)。
