---
title: Espacios vectoriales y subespacios / 向量空间与子空间 — soluciones
subject: Álgebra Lineal
tema: Guía 2.2
type: exercises
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_2_2
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-012/Temas 1 y 2(1)(2).pdf
updated: 2026-10-26
---

# Soluciones 2.2 — 完整解答

**Fuentes verificadas:** AL-AP-012, pp. 3–7. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Resoluciones propias de [A22-E01–E06](05_Ejercicios.md).

## A22-E01

**Estrategia ES.** Distribuir y cancelar por suma. **中文。** 不使用待证性质本身。**Demostración.** $0v=(0+0)v=0v+0v$; sumar $-(0v)$ da $0v=0_V$. Luego $v+(-1)v=(1-1)v=0v=0_V$; por unicidad del opuesto, $(-1)v=-v$. **Conclusión.** Ambas reglas proceden de los axiomas, no de una identificación informal entre cero escalar y vectorial.

## A22-E02

**Estrategia ES.** Usar el sistema homogéneo y despejar. **中文。** 既判断结构，也写全参数。**Resolución.** Es el conjunto de soluciones de un sistema homogéneo, por lo que es subespacio. De $y=z=t$ y $x=-y$ resulta $W=\{(-t,t,t):t\in\mathbb R\}$. Sustituir da $-t+t=0$ y $t-t=0$ para todos $t$. **Conclusión.** La parametrización cubre exactamente el conjunto.

## A22-E03

**Estrategia ES.** Evaluar combinaciones en $1$ y buscar fallos concretos en los otros casos. **中文。** 次数恰为 2 与次数至多 2 不同。**Resolución.** Si $p(1)=q(1)=0$, $(ap+bq)(1)=0$ y el polinomio cero pertenece; es subespacio. Si se pide $p(1)=1$, el cero falla. Los de grado exactamente $2$ tampoco contienen cero; además $x^2$ y $-x^2$ suman cero y salen del conjunto. **Conclusión.** Solo el primer conjunto es subespacio.

## A22-E04

**Estrategia ES.** Comprobar entradas traspuestas y después verificar el cero. **中文。** 可逆集合必须先过零矩阵这一关。**Resolución.** $0^{\mathsf T}=0$. Para simétricas $A,B$, la entrada $(i,j)$ de $\alpha A+\beta B$ es $\alpha a_{ij}+\beta b_{ij}$ y coincide con su entrada $(j,i)$ porque $a_{ij}=a_{ji}$ y $b_{ij}=b_{ji}$. Es subespacio. Las matrices invertibles no contienen la matriz cero, por lo que no forman subespacio. **Conclusión.** Una buena estructura multiplicativa no implica subespacio aditivo.

## A22-E05

**Estrategia ES.** Recuperar cero, opuestos y suma. **中文。** 从差的封闭性逐步推出所需条件。**Demostración.** Elija $w\in W$; $w-w=0\in W$. Para $v\in W$, $0-v=-v\in W$. Para $u,v\in W$, $u-(-v)=u+v\in W$. Junto a la clausura escalar, el criterio prueba subespacio. Sin la clausura escalar, $\mathbb Z\subset\mathbb R$ es no vacío y cerrado por diferencia, pero $(1/2)1\notin\mathbb Z$. **Conclusión.** Las dos hipótesis desempeñan papeles distintos.

## A22-E06

**Estrategia ES.** Usar igualdad funcional para las pares y comprobar el cero en las positivas. **中文。** 函数条件应对每个实数验证。**Resolución.** La función cero es par. Si $f(-x)=f(x)$ y $g(-x)=g(x)$ para todo $x$, entonces $(af+bg)(-x)=af(x)+bg(x)=(af+bg)(x)$ para todo $x$; es subespacio. Las estrictamente positivas no contienen la función cero, y el opuesto de una positiva es negativo; no son subespacio. **Conclusión.** Los argumentos son punto a punto, no solo en valores de muestra.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
