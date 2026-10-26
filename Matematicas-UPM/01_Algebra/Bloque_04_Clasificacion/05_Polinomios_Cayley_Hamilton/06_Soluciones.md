---
title: Anuladores, Cayley–Hamilton y polinomio mínimo / 零化与最小多项式 — soluciones
subject: Álgebra Lineal
tema: Guía 4.5
type: exercises
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_4_5
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Soluciones 4.5 — 完整解答

**Fuentes verificadas:** AL-GD-001 p. 6, 4.5; suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Resoluciones propias de [A45-E01–E06](05_Ejercicios.md).

## A45-E01

**Estrategia ES.** Evaluar en diagonal y exigir ambas raíces distintas. **中文。** 特征值的重复次数不一定进入最小多项式。**Resolución.** La característica es $(t-1)^2(t-3)$. Todo anulador debe anular $1$ y $3$, así es divisible por $(t-1)(t-3)$; ese producto anula toda la diagonal. Por minimalidad, es el mínimo. **Conclusión.** Grados $3$ y $2$, respectivamente.

## A45-E02

**Estrategia ES.** Calcular potencias y usar independencia de sus posiciones no nulas. **中文。** 仅有 $N^3=0$ 还要排除更低次零化。**Resolución.** $N^2$ tiene único $1$ en posición $(1,3)$ y $N^3=0$. Si $aI+bN+cN^2=0$, mirar diagonal da $a=0$, posición $(1,2)$ da $b=0$ y $(1,3)$ da $c=0$. Ningún polinomio no nulo de grado menor que $3$ anula. Así $\mu=t^3=\chi$, y Cayley–Hamilton da exactamente la potencia nula calculada. **Conclusión.** Índice nilpotente $3$.

## A45-E03

**Estrategia ES.** Despejar identidad y aplicar el criterio del mínimo. **中文。** 不必直接求特征多项式。**Resolución.** $A(3I-A)/2=I$ y el producto opuesto también, por lo que $A^{-1}=(3I-A)/2$. Su mínimo divide $(t-1)(t-2)$, un producto de lineales distintos; cualquier divisor mónico también tiene esa forma sin repeticiones, así diagonaliza por T3. **Conclusión.** La relación dada basta para ambas afirmaciones.

## A45-E04

**Estrategia ES.** Usar potencias, y para el recíproco tomar un operador escalar. **中文。** 单向包含不等于所有可交换矩阵都来自多项式。**Demostración.** $AA^k=A^kA$ para cada $k$ y distribuir prueba conmutación con toda combinación polinómica. Si $A=I_2$, todos los polinomios en él son matrices escalares, pero $\operatorname{diag}(1,2)$ conmuta con $I_2$ y no es escalar. **Conclusión.** El recíproco general es falso.

## A45-E05

**Estrategia ES.** Aplicar T4 a los factores coprimos. **中文。** 精确区分零化指数上界与实际链长度。**Resolución.** $V=\ker(T-I)^2\oplus\ker(T+I)$. En la primera componente $T=I+N$, $N^2=0$; en la segunda $T=-I$. Como el mínimo tiene factor cuadrado, $T-I$ no se anula en toda la primera componente, pues de lo contrario $(t-1)(t+1)$ anularía todo $V$, contradiciendo minimalidad. **Conclusión.** La primera tiene nilpotencia realmente no trivial; el tamaño total de esa componente aún necesita más información.

## A45-E06

**Estrategia ES.** Separar evidencia puntual de identidad universal. **中文。** 一般证明要对任意条目成立。**Resolución.** En tamaño dos, escriba $B(t)=B_0+tB_1$ y $\chi=t^2+c_1t+c_0$. La identidad de adjunta da $-AB_0=c_0I$, $B_0-AB_1=c_1I$, $B_1=I$. Así $c_0I+c_1A+A^2=-AB_0+(AB_0-A^2B_1)+A^2B_1=0$. Esto usa matrices arbitrarias, mientras un cálculo numérico solo verifica un caso. **Conclusión.** La diferencia lógica es explícita.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
