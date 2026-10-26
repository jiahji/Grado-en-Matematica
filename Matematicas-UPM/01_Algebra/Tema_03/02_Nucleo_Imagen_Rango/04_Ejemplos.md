---
title: Núcleo, imagen y rango–nulidad / 核、像与秩–零化度
subject: Álgebra Lineal
tema: Guía 3.2
type: example
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_3_2
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-003/Tema 3_3783d906f8056ce104fc5d6bc1f5548c.pdf
updated: 2026-10-26
---

# Ejemplos de núcleo e imagen — 完整例题

**Fuentes verificadas:** AL-AP-003, pp. 9–13. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Ejemplos propios basados en el modelo matricial y funcional de aula.

## K-01. Matriz rectangular — 基础

**Enunciado.** $f(x,y,z)=(x+2y-z,y+z)$. **Análisis ES.** Resolver núcleo y localizar dos imágenes independientes. **中文。** 核用定义域坐标，像用二维输出坐标。

**Resolución.** El núcleo exige $y=-z$, $x=3z$, así $\ker f=\langle(3,-1,1)\rangle$. Las imágenes de $e_1,e_2$ son $(1,0),(2,1)$, independientes y generan $\mathbb R^2$; por tanto imagen total. Nulidad $1$ y rango $2$ suman $3$. **Conclusión.** No se debe escribir el núcleo como línea de $\mathbb R^2$.

## K-02. Derivada polinómica — 综合

**Enunciado.** $D:\mathbb R_{\le3}[x]\to\mathbb R_{\le2}[x]$. **Análisis ES.** Comparar coeficientes de la derivada y construir una preimagen. **中文。** 要核实像是整个陪域，而非只给几个像的例子。

**Resolución.** $D(a+bx+cx^2+dx^3)=b+2cx+3dx^2$. Es cero si y solo si $b=c=d=0$, así núcleo son constantes, dimensión $1$. Cada $u+vx+wx^2$ es derivada de $ux+(v/2)x^2+(w/3)x^3$, así rango $3$. $1+3=4$ coincide con dimensión inicial. **Conclusión.** La no inyectividad no impide sobreyectividad.

## K-03. Preimagen de una recta — 大学水平

**Enunciado.** Para $p(x,y,z)=(x,y)$, hallar $p^{-1}(E)$ con $E=\{(a,a)\}$. **Análisis ES.** Incorporar la ecuación del destino. **中文。** $p$ 不可逆，但子空间原像仍有意义。

**Resolución.** $p(v)\in E$ equivale a $x=y$, sin restricción sobre $z$. Así la preimagen es $\{(s,s,t)\}=\langle(1,1,0),(0,0,1)\rangle$. Ambos generadores son independientes; dimensión $2$. **Conclusión.** Preimagen no significa aplicar una inexistente inversa a una recta.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
