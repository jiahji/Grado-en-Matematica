---
title: Inyectividad, sobreyectividad y biyectividad / 单射、满射与双射
subject: Álgebra Lineal
tema: Guía 3.3
type: example
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_3_3
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-003/Tema 3_3783d906f8056ce104fc5d6bc1f5548c.pdf
updated: 2026-10-26
---

# Ejemplos 3.3 — 完整例题

**Fuentes verificadas:** AL-AP-003, pp. 14–16. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Ejemplos propios para los criterios de pp. 14–16.

## J-01. Inyectiva sin ser sobreyectiva — 基础

**Enunciado.** $f:\mathbb R^2\to\mathbb R^3$, $f(x,y)=(x,y,x+y)$. **Análisis ES.** El núcleo se detecta en las dos primeras coordenadas. **中文。** 还要检查是否填满三维输出。

**Resolución.** $f(x,y)=0$ fuerza $x=y=0$, así es inyectiva. Su imagen satisface $z=x+y$ y no contiene $(0,0,1)$; no es sobreyectiva. **Conclusión.** Rango $2$, dominio dimensión $2$, destino dimensión $3$.

## J-02. Sobreyectiva sin ser inyectiva — 综合

**Enunciado.** $p:\mathbb R^3\to\mathbb R^2$, $p(x,y,z)=(x,y)$. **Análisis ES.** Construir preimagen de un destino cualquiera. **中文。** 一个输出例子不够证明满射。

**Resolución.** Para todo $(a,b)$, $(a,b,0)$ es una preimagen; es sobreyectiva. Pero todos los $(0,0,z)$ van a cero, y $p(0,0,1)=p(0,0,0)$, así no es inyectiva. **Conclusión.** Rango $2$, nulidad $1$, consistentes con 3.2.

## J-03. Una familia parametrizada — 大学水平

**Enunciado.** $f_a(x,y)=(x+ay,ax+y)$ en $\mathbb R^2$. **Análisis ES.** Gauss da segundo pivote $1-a^2$. **中文。** 退化点需分别解释像。

**Resolución.** El núcleo exige $x=-ay$ y $(1-a^2)y=0$. Si $a\ne\pm1$, solo hay cero y por igual dimensión es biyectiva. Para salida $(u,v)$, su inversa da $x=(u-av)/(1-a^2)$, $y=(v-au)/(1-a^2)$. Si $a=1$, imagen es $\langle(1,1)\rangle$, núcleo $\langle(-1,1)\rangle$; si $a=-1$, imagen $\langle(1,-1)\rangle$, núcleo $\langle(1,1)\rangle$. **Conclusión.** En los dos valores excepcionales no es ni inyectiva ni sobreyectiva.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
