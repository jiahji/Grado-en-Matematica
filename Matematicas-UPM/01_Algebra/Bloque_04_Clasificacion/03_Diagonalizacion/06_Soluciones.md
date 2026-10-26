---
title: Diagonalización / 对角化 — soluciones
subject: Álgebra Lineal
tema: Guía 4.3
type: exercises
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_4_3
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Soluciones 4.3 — 完整解答

**Fuentes verificadas:** AL-GD-001 p. 6, 4.3; suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Resoluciones propias de [A43-E01–E06](05_Ejercicios.md).

## A43-E01

**Estrategia ES.** Encontrar vectores para $1$ y $2$. **中文。** 验证列顺序。**Resolución.** $P=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ y $D=\operatorname{diag}(1,2)$ satisfacen $AP=PD$, con $P^{-1}=\begin{pmatrix}1&-1\\0&1\end{pmatrix}$. Así $A^k=\begin{pmatrix}1&2^k-1\\0&2^k\end{pmatrix}$; $k=0$ da identidad. **Conclusión.** Fórmula exacta para todos los enteros no negativos.

## A43-E02

**Estrategia ES.** Revisar escisión en cada campo. **中文。** 实对角矩阵必须有实对角值。**Resolución.** No hay raíces reales de $t^2+1$, así no es diagonalizable real. Sobre complejos, las columnas $(1,-i),(1,i)$ son independientes por valores distintos y diagonalizan con diagonal $i,-i$. **Conclusión.** La clasificación depende del campo.

## A43-E03

**Estrategia ES.** Elevar la diagonal. **中文。** 非零幂零矩阵不可能拥有特征基。**Demostración.** Si $T$ es semejante a $D$ diagonal y $T^m=0$, entonces $D^m=0$. Cada entrada satisface $\lambda_j^m=0$ en un cuerpo, así $\lambda_j=0$. Luego $D=0$ y $T=0$. A la inversa, cero ya es diagonal. **Conclusión.** El único nilpotente diagonalizable es el cero.

## A43-E04

**Estrategia ES.** Descomponer en $v-Tv$ y $Tv$. **中文。** 核与像在投影条件下恰好互补。**Demostración.** $T(v-Tv)=0$ y $Tv\in\operatorname{Im}T$. Si $w=Tu$ y $Tw=0$, entonces $w=T^2u=Tw=0$. Así $V=\ker T\oplus\operatorname{Im}T$. En la primera parte actúa como cero y en la segunda como identidad; concatenar bases diagonaliza. **Conclusión.** No se requieren cálculos de determinantes.

## A43-E05

**Estrategia ES.** Usar $v_+=(v+Tv)/2$, $v_-=(v-Tv)/2$. **中文。** 两个分量在各自特征空间内。**Demostración.** $Tv_+=v_+$ y $Tv_-=-v_-$, y su suma es $v$. Si un vector está en ambos espacios, $v=-v$ y por $2\ne0$ debe ser cero. Tomar bases de esos espacios y unirlas da base de $V$; el operador es diagonal con entradas $1,-1$. **Conclusión.** La división por dos tiene una hipótesis explícita.

## A43-E06

**Estrategia ES.** Conmutación hace invariante cada autoespacio de $A$. **中文。** 简单特征值使每个特征空间是一维。**Demostración.** Si $Av_i=\lambda_i v_i$, entonces $A(Bv_i)=BAv_i=\lambda_i Bv_i$, así $Bv_i\in E_{\lambda_i}(A)$. Ese espacio tiene dimensión uno, por $n$ valores distintos y 4.2; por tanto $Bv_i=\mu_i v_i$ para algún escalar, incluso cero. Los $v_i$ forman base y en ella $B$ es diagonal. **Conclusión.** No se ha supuesto indebidamente que cualquier par de matrices conmute.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
