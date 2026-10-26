---
title: Cambio de base y semejanza / 换基与相似
subject: Álgebra Lineal
tema: Guía 3.6
type: example
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_3_6
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-004/Tema 4_65298606b99b4fa875367ddfc0765632.pdf
updated: 2026-10-26
---

# Ejemplos de cambio de base — 完整例题

**Fuentes verificadas:** AL-AP-004, pp. 8–12. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Ejemplos propios siguiendo la convención exacta de aula.

## P-01. Canónica a otra base — 基础

**Enunciado.** $B$ canónica, $C=((1,1),(1,-1))$. Hallar ambas transiciones. **Análisis ES.** $S_C$ contiene la nueva base, pero convierte de $C$ a canónica. **中文。** 直接排新基得到的矩阵方向容易记反。

**Resolución.** $P_{C,B}=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ y $P_{B,C}=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$. El vector canónico $(2,4)$ tiene coordenadas $C$ iguales a $(3,-1)$; reconstruir $3(1,1)-(1,-1)=(2,4)$. **Conclusión.** Las dos matrices son inversas, no iguales.

## P-02. Endomorfismo — 综合

**Enunciado.** $f(x,y)=(2x,3y)$ y nueva base $C$ de P-01. **Análisis ES.** Usar $P$ de nueva a antigua. **中文。** 此时才是同一个基变更在两侧关联。

**Resolución.** Con $P=S_C$, $A=\operatorname{diag}(2,3)$,

$$
P^{-1}AP=\frac12\begin{pmatrix}5&-1\\-1&5\end{pmatrix}.
$$

Directamente $f(1,1)=(2,3)$ tiene coordenadas $(5/2,-1/2)$, y $f(1,-1)=(2,-3)$ tiene $(-1/2,5/2)$, comprobando ambas columnas. **Conclusión.** Traza $5$ y rango $2$ se conservan aunque desaparezca la forma diagonal.

## P-03. Dos cambios distintos — 大学水平

**Enunciado.** $A=\begin{pmatrix}1&2\\3&-1\end{pmatrix}$ en canónicas; nuevas bases $B=((1,1),(1,-1))$, $C=((1,0),(1,1))$. **Análisis ES.** Usar $S_C^{-1}AS_B$, no una conjugación por una sola matriz. **中文。** 定义域与陪域基可以独立选择。

**Resolución.** $S_C^{-1}=\begin{pmatrix}1&-1\\0&1\end{pmatrix}$ y $S_B=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$. Su producto con $A$ da $\begin{pmatrix}1&-5\\2&4\end{pmatrix}$, coincidiendo con el cálculo por imágenes del ejemplo R-02 de 3.5. **Conclusión.** La doble comprobación verifica tanto dirección como valores.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
