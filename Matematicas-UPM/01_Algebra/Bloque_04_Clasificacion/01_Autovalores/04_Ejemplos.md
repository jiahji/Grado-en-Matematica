---
title: Autovalores y polinomio característico / 特征值与特征多项式
subject: Álgebra Lineal
tema: Guía 4.1
type: example
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_4_1
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Ejemplos de autovalores — 完整例题

**Fuentes verificadas:** AL-GD-001 p. 6, 4.1; suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Todo este bloque es suplemento propio basado en el temario confirmado, sin apuntes específicos recibidos.

## E-01. Triangular con dos valores — 基础

**Enunciado.** $A=\begin{pmatrix}2&1\\0&3\end{pmatrix}$. **Análisis ES.** Factorizar la característica y resolver ambos sistemas. **中文。** 上三角对角线给候选值，但向量仍需计算。

**Resolución.** $\chi=(t-2)(t-3)$. Para $\lambda=2$, $(A-2I)v=0$ exige $y=0$, así $E_2=\langle(1,0)\rangle$. Para $3$, $-x+y=0$, así $E_3=\langle(1,1)\rangle$. **Conclusión.** Los autovectores son los múltiplos no nulos de cada generador; la traza $5$ y determinante $6$ verifican coeficientes.

## E-02. Rotación real — 综合

**Enunciado.** $R=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$. **Análisis ES.** Indicar el cuerpo antes de resolver. **中文。** 实数域与复数域答案不同。

**Resolución.** $\chi=t^2+1$. Sobre reales no hay valores propios. Sobre complejos, para $i$ sirve $(1,-i)$ porque $R(1,-i)=(i,1)=i(1,-i)$; para $-i$ sirve $(1,i)$. **Conclusión.** Mismo arreglo numérico, diferente clasificación según el cuerpo.

## E-03. Una matriz racional — 大学水平

**Enunciado.** $A=\begin{pmatrix}0&1\\2&0\end{pmatrix}$, comparar $\mathbb Q$ y $\mathbb R$. **Análisis ES.** Las raíces necesitan pertenecer al campo. **中文。** 有理系数矩阵不保证有有理特征值。

**Resolución.** $\chi=t^2-2$, raíces $\pm\sqrt2$ reales pero no racionales. Para cada raíz $\lambda$, $(1,\lambda)$ es autovector porque $A(1,\lambda)=(\lambda,2)=\lambda(1,\lambda)$. **Conclusión.** No tiene autovalores racionales y sí dos reales distintos.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
