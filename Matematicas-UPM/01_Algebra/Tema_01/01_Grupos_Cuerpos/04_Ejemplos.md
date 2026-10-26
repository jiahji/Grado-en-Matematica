---
title: Grupos y cuerpos / 群与域
subject: Álgebra Lineal
tema: Guía 2.1
type: example
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_2_1
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-012/Temas 1 y 2(1)(2).pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-000/Tema 0(6).pdf
updated: 2026-10-26
---

# Ejemplos de grupos y cuerpos — 例题

**Fuentes verificadas:** AL-AP-012, p. 2; AL-AP-000 pp. 14–15; estructura de grupo como suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


三个例子为补充，配合课堂域定义。正式计算和解释均在下文。

## G-01. Enteros y naturales — 基础

**Enunciado.** Comparar $(\mathbb Z,+)$ y $(\mathbb N,+)$, con $0\in\mathbb N$ según AL-AP-000 p. 10. **Análisis ES.** Casi todos los axiomas coinciden; hay que localizar el que falla. **中文。** 集合包含零，并不能保证加法群。

**Resolución.** En $\mathbb Z$ la suma es interna, asociativa y conmutativa por aritmética entera; $0$ es neutro y el opuesto de $n$ es $-n\in\mathbb Z$. Es grupo abeliano. En $\mathbb N$, $1$ no tiene un $m\ge0$ con $1+m=0$, así que no es grupo. **Conclusión.** Falta un inverso, no la asociatividad. **Error frecuente ES.** El inverso debe pertenecer al conjunto estudiado. **中文易错点。** 不能把存在于整数集里的 $-1$ 当成自然数集内部的元素。

## G-02. Multiplicación real — 综合

**Enunciado.** Comparar $(\mathbb R,\cdot)$ y $(\mathbb R\setminus\{0\},\cdot)$. **Análisis ES.** El neutro multiplicativo es $1$; hay que excluir exactamente el elemento sin inverso. **中文。** 零必须留在实数域里，但不能留在其乘法群里。

**Resolución.** Todo real no nulo $a$ tiene $1/a\ne0$, y el producto de dos no nulos es no nulo. Asociatividad y conmutatividad se heredan; $1$ pertenece al conjunto. Así los no nulos forman grupo abeliano. En todo $\mathbb R$, $0b=0\ne1$ para cualquier $b$, por lo que $0$ carece de inverso. **Conclusión.** Solo el segundo conjunto es grupo multiplicativo. **Error frecuente ES.** $\mathbb R$ sigue siendo un cuerpo: el grupo multiplicativo se exige solo en los no nulos. **中文误区。** 实数仍然是域，不能把“整个集合不是乘法群”误说成“不是域”。

## G-03. Un grupo no conmutativo — 大学水平

**Enunciado.** Justificar que $GL_2(\mathbb R)$, matrices invertibles, es grupo no abeliano. **Análisis ES.** Probar clausura mediante la fórmula del inverso y dar un par que no conmute. **中文。** 一个非交换例子只否定交换律，仍需核实群公理。

**Resolución.** Para invertibles $A,B$, $(AB)(B^{-1}A^{-1})=(B^{-1}A^{-1})(AB)=I$, luego $AB$ es invertible. La identidad pertenece al conjunto; cada inverso es invertible con inverso $A$; la asociatividad matricial ya está probada. Tomando

$$
A=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad B=\begin{pmatrix}1&0\\1&1\end{pmatrix},
$$

sus inversas cambian a $-1$ sus entradas fuera de la diagonal. Sin embargo $AB=\begin{pmatrix}2&1\\1&1\end{pmatrix}$ y $BA=\begin{pmatrix}1&1\\1&2\end{pmatrix}$. **Conclusión.** Es grupo, pero no abeliano. **中文解释。** 非交换不是“不存在逆元”，这两类性质必须分开。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
