---
title: Representación matricial y composición / 矩阵表示与复合
subject: Álgebra Lineal
tema: Guía 3.5
type: example
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_3_5
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-004/Tema 4_65298606b99b4fa875367ddfc0765632.pdf
updated: 2026-10-26
---

# Ejemplos de representación — 完整例题

**Fuentes verificadas:** AL-AP-004, pp. 2–7. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Ejemplos propios sobre modelos funcionales y matriciales de aula.

## R-01. Derivada — 基础

**Enunciado.** $D:\mathbb R_{\le2}[x]\to\mathbb R_{\le1}[x]$, bases $B=(1,x,x^2)$, $C=(1,x)$. **Análisis ES.** Derivar cada base y expresar en llegada. **中文。** 输入有三个坐标，输出有两个。

**Resolución.** $D(1)=0$, $D(x)=1$, $D(x^2)=2x$, así $A=\begin{pmatrix}0&1&0\\0&0&2\end{pmatrix}$. Multiplicar por $(a,b,c)^{\mathsf T}$ da $(b,2c)^{\mathsf T}$, las coordenadas de $b+2cx$. **Conclusión.** El factor $2$ no puede omitirse.

## R-02. Dos bases no canónicas — 综合

**Enunciado.** $f(x,y)=(x+2y,3x-y)$, $B=((1,1),(1,-1))$, $C=((1,0),(1,1))$. **Análisis ES.** Resolver coordenadas de cada imagen, no copiar sus entradas. **中文。** 陪域不是标准基。

**Resolución.** $f(1,1)=(3,2)=1(1,0)+2(1,1)$; $f(1,-1)=(-1,4)=-5(1,0)+4(1,1)$. Así $M_{B,C}(f)=\begin{pmatrix}1&-5\\2&4\end{pmatrix}$. Para $v=(3,1)$, $[v]_B=(2,1)$, el resultado es $(-3,8)$; reconstruir en $C$ da $(5,8)$, coincidente con $f(3,1)$. **Conclusión.** Las columnas son coordenadas, no directamente $(3,2)$ y $(-1,4)$.

## R-03. Composición rectangular — 大学水平

**Enunciado.** Con $D$ anterior y $J(a+bx)=ax+(b/2)x^2$, calcular $DJ$ y $JD$. **Análisis ES.** Usar tamaños y orden. **中文。** 两个方向不一定给同一个恒等映射。

**Resolución.** $M(J)=\begin{pmatrix}0&0\\1&0\\0&1/2\end{pmatrix}$. Entonces $M(D)M(J)=I_2$, mientras $M(J)M(D)=\operatorname{diag}(0,1,1)$. Por tanto $DJ$ es identidad en grado a lo sumo $1$, pero $JD(a+bx+cx^2)=bx+cx^2$ pierde la constante. **Conclusión.** $J$ es una inversa por la derecha de $D$, no una inversa bilateral.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
