---
title: Forma canónica de Jordan / Jordan 标准形 — soluciones
subject: Álgebra Lineal
tema: Guía 4.4
type: exercises
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_4_4
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Soluciones 4.4 — 完整解答

**Fuentes verificadas:** AL-GD-001 p. 6, 4.4; suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Resoluciones propias de [A44-E01–E07](05_Ejercicios.md).

## A44-E01

**Estrategia ES.** Escribir $A=I+N$ y prolongar una cadena. **中文。** 与例题不同，这里的特征值是 1。**Resolución.** $N=\begin{pmatrix}1&1\\-1&-1\end{pmatrix}$, con $N^2=0$. Sirven $v_1=(1,-1)$, $v_2=(1,0)$. Con $P=\begin{pmatrix}1&1\\-1&0\end{pmatrix}$ y $J=\begin{pmatrix}1&1\\0&1\end{pmatrix}$, $AP=\begin{pmatrix}1&2\\-1&-1\end{pmatrix}=PJ$. La inversa $\begin{pmatrix}0&-1\\1&1\end{pmatrix}$ verifica independencia. **Conclusión.** Una única cadena de longitud dos.

## A44-E02

**Estrategia ES.** Calcular $b_k=d_k-d_{k-1}$. **中文。** 达到维数后保持稳定。**Resolución.** Los incrementos son $3,2,1,0$. Hay un bloque de cada tamaño $1,2,3$. Rango $6-d_1=3$ por rango–nulidad; mínimo $t^3$ y característica $t^6$. **Conclusión.** La multiplicidad propia es número de bloques, no su longitud máxima.

## A44-E03

**Estrategia ES.** Sumar $\min(k,m)$ bloque a bloque. **中文。** 更多幂的核才能区分形状。**Resolución.** Para $(3,1)$, dimensiones $d_1=2,d_2=3,d_3=4$ y mínimo $t^3$. Para $(2,2)$, $d_1=2,d_2=4$ y mínimo $t^2$. Ambas tienen característica $t^4$ y espacio propio de dimensión $2$, así esos dos datos no bastan. **Conclusión.** Los núcleos de potencias aportan información adicional esencial.

## A44-E04

**Estrategia ES.** Aplicar sucesivamente potencias para eliminar coeficientes desde el extremo. **中文。** 最高高度非零保证首个被隔离的项不消失。**Demostración.** En una relación $a_1N^{m-1}v+\cdots+a_mv=0$, aplicar $N^{m-1}$ deja $a_mN^{m-1}v=0$, así $a_m=0$. Con ese coeficiente fuera, aplicar $N^{m-2}$ deja $a_{m-1}N^{m-1}v=0$; repetir determina todos cero. **Conclusión.** La cadena individual es independiente, aunque para varias cadenas aún hay que controlar su independencia conjunta.

## A44-E05

**Estrategia ES.** Calcular característica y usar vectores complejos conjugados. **中文。** 实二维块不是实对角块。**Resolución.** $\chi=(t-a)^2+b^2$ no tiene raíces reales si $b\ne0$, así no es diagonalizable real. Sobre complejos tiene $a+bi$ con vector $(1,-i)$ y $a-bi$ con vector $(1,i)$; son independientes y diagonalizan. La propia matriz $C$ es el bloque real que representa el par conjugado. **Conclusión.** La forma real conserva una pareja de dimensiones reales.

## A44-E06

**Estrategia ES.** Usar monotonicidad de incrementos o una inyección natural. **中文。** 数据不满足链结构的必要条件。**Resolución.** $b_1=1$, $b_2=2$ aumentan, imposible porque número de bloques de longitud al menos dos no puede superar el total. Sin usar tamaños, la aplicación $\ker N^2/\ker N\to\ker N$, $[v]\mapsto Nv$, está bien definida y es inyectiva: cambiar por un elemento del núcleo no cambia imagen, y $Nv=0$ obliga clase cero. Luego $d_2-d_1\le d_1$, pero aquí $2>1$. **Conclusión.** No existe tal nilpotente.

## A44-E07

**Estrategia ES.** Aplicar invariancia de núcleos y después unir los cambios de base. **中文。** 分类需要必要与充分两个方向。**Demostración.** Matrices semejantes tienen las mismas dimensiones de cada núcleo de potencia desplazada y las mismas características, así T3 da los mismos tamaños para cada valor. Si tienen iguales bloques, se pueden ordenar para que sus formas coincidan en una matriz $J$. Si $A=PJP^{-1}$ y $B=QJQ^{-1}$, entonces $B=(PQ^{-1})^{-1}A(PQ^{-1})$. **Conclusión.** Son semejantes exactamente en ese caso.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
