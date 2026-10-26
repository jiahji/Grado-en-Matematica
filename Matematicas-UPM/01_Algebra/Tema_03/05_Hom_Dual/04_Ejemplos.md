---
title: Espacio de aplicaciones y dual / 映射空间与对偶空间
subject: Álgebra Lineal
tema: Guía 3.8
type: example
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_3_8
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-003/Tema 3_3783d906f8056ce104fc5d6bc1f5548c.pdf
updated: 2026-10-26
---

# Ejemplos de dualidad — 完整例题

**Fuentes verificadas:** AL-AP-003, p. 19: terminología de forma lineal; desarrollo de Hom y dual como suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Todos son desarrollo suplementario propio.

## U-01. Coeficientes frente a evaluación — 基础

**Enunciado.** $V=\mathbb R_{\le2}[x]$, base $(1,x,x^2)$. Hallar dual y coordenadas de $E(p)=p(1)$. **Análisis ES.** Cada funcional dual extrae un coeficiente. **中文。** 求值函数不是某一个系数函数。

**Resolución.** $\varphi_0(a+bx+cx^2)=a$, $\varphi_1=b$, $\varphi_2=c$. Como $p(1)=a+b+c$, $E=\varphi_0+\varphi_1+\varphi_2$, con coordenadas $(1,1,1)$. **Conclusión.** Una forma puede combinar varias mediciones básicas.

## U-02. Anulador — 综合

**Enunciado.** $U=\langle(1,1,0)\rangle\le\mathbb R^3$. **Análisis ES.** Escribir una forma general $ax+by+cz$. **中文。** 零化子里的元素是这样的函数，不是直接一组三维向量。

**Resolución.** Anular el generador exige $a+b=0$, sin restricción a $c$. Así $U^0=\langle x-y,z\rangle$ como espacio de funcionales; ambos son independientes y dimensión $2=3-1$. **Conclusión.** La representación por coeficientes es una identificación elegida, no una definición por perpendicularidad.

## U-03. Traspuesta rectangular — 大学水平

**Enunciado.** $f(x,y,z)=(x+2y-z,y+z)$. **Análisis ES.** Componer una forma de salida $\ell(u,v)=au+bv$ con $f$. **中文。** 输出测量被拉回三维输入。

**Resolución.** $f^*(\ell)(x,y,z)=a x+(2a+b)y+(-a+b)z$. Su matriz es $\begin{pmatrix}1&0\\2&1\\-1&1\end{pmatrix}=M(f)^{\mathsf T}$. Si sus coeficientes son cero, $a=0$ y luego $b=0$, así dual es inyectiva, consistente con que $f$ sea sobreyectiva. **Conclusión.** Los tamaños y la dirección cambian de $2\times3$ a $3\times2$.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
