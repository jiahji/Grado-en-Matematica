---
title: Determinantes y formas alternadas / 行列式与交替多线性形式 — soluciones
subject: Álgebra Lineal
tema: Guía 3.7
type: exercises
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_3_7
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Soluciones 3.7 — 完整解答

**Fuentes verificadas:** AL-GD-001 p. 6, 3.7; desarrollo propio sin apuntes específicos recibidos. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Resoluciones propias de [A37-E01–E07](05_Ejercicios.md).

## A37-E01

**Estrategia ES.** Expansión de orden dos y condición no nula. **中文。** 退化参数单列。**Resolución.** $\det A_t=t-1$. Para $t\ne1$, $A_t^{-1}=(t-1)^{-1}\begin{pmatrix}t&-1\\-1&1\end{pmatrix}$; ambos productos con $A_t$ son identidad. Para $t=1$ hay filas iguales y es singular. **Conclusión.** No se divide por $t-1$ sin condición.

## A37-E02

**Estrategia ES.** Distribuir el escalar en las $n$ columnas y usar un caso pequeño para refutar aditividad. **中文。** 矩阵整体乘标量等于每列都乘一次。**Demostración.** Multilinealidad extrae un factor $a$ por columna, total $a^n$. Para $A=B=I_2$, $\det(A+B)=4$ y $\det A+\det B=2$. **Conclusión.** Determinante no es función lineal de toda la matriz.

## A37-E03

**Estrategia ES.** Multiplicar los factores de cada operación. **中文。** 加行操作与倍乘操作作用不同。**Resolución.** Intercambiar cambia signo; escalar por $3$ multiplica por $3$; añadir múltiplo de otra fila no cambia. El resultado es $-3\det A$. Esto también vale cuando el inicial es cero. **Conclusión.** Se deben contabilizar todas las operaciones, sin inferir que todas conservan determinante.

## A37-E04

**Estrategia ES.** Usar trasposición y escalado. **中文。** 实数域中 2 非零是最后一步的条件。**Demostración.** $\det A=\det A^{\mathsf T}=\det(-A)=(-1)^n\det A=-\det A$. Luego $2\det A=0$ y $\det A=0$ sobre reales. Por T2 es singular. **Conclusión.** El resultado necesita orden impar y la condición de característica distinta de dos que cumple el curso.

## A37-E05

**Estrategia ES.** Despejar un argumento con coeficiente no nulo. **中文。** 逐项会出现重复方向。**Demostración.** En una relación no trivial, expresar $v_j$ como combinación de los otros. Al distribuir en esa posición, cada término contiene dos argumentos iguales y se anula por alternación. Toda la suma es cero. **Conclusión.** El resultado no supone una matriz cuadrada de coordenadas particular.

## A37-E06

**Estrategia ES.** Usar menores y la identidad con la adjunta. **中文。** 必须证明秩上界与非零性。**Demostración.** Si rango $\le n-2$, todos los menores de orden $n-1$ son cero por T5, así todos los cofactores son cero. Si rango $n-1$, algún menor de ese orden no es cero, así adjunta no nula. Como $\det A=0$, $A\operatorname{adj}A=0$, y cada columna de la adjunta pertenece al núcleo unidimensional de $A$ por rango–nulidad. Su rango es a lo sumo $1$ y, por no ser nula, al menos $1$. **Conclusión.** Rango exactamente uno.

## A37-E07

**Estrategia ES.** Aplicar multiplicatividad y dar matrices escalares diferentes. **中文。** 必要不变量不自动分类。**Demostración.** $\det(P^{-1}AP)=\det P^{-1}\det A\det P=\det A$. Pero $I_2$ y $-I_2$ tienen determinante $1$ y no son semejantes, porque $P^{-1}I_2P=I_2$ para todo $P$. **Conclusión.** Igual determinante es solo condición necesaria.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
