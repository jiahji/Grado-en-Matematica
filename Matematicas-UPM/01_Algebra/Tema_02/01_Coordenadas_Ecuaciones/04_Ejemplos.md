---
title: Coordenadas y ecuaciones / 坐标与子空间方程
subject: Álgebra Lineal
tema: Guía 2.5
type: example
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_2_5
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-012/Temas 1 y 2(1)(2).pdf
updated: 2026-10-26
---

# Ejemplos 2.5 — 完整例题

**Fuentes verificadas:** AL-AP-012, pp. 19–23. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


## C-01. Ejemplo de aula de coordenadas — 基础

**Enunciado.** AL-AP-012 p. 19: $B'=((1,2),(-1,1))$, hallar coordenadas de $(0,3)$. **Análisis ES.** Las columnas de la base dan el sistema. **中文。** 坐标不是原向量分量的简单重排。

**Resolución.** $a(1,2)+b(-1,1)=(0,3)$ implica $a-b=0$ y $2a+b=3$, de donde $a=b=1$. Sustituir da $(1,2)+(-1,1)=(0,3)$. **Conclusión.** $[(0,3)]_{B'}=(1,1)^{\mathsf T}$. Para general $(x,y)$, $a=(x+y)/3$, $b=(y-2x)/3$, por lo que hay una única representación para todos los vectores.

## C-02. Ecuaciones repetidas — 综合

**Enunciado propio.** $x-y+z=0$, $2x-2y+2z=0$ en $\mathbb R^3$. **Análisis ES.** La segunda fila no añade rango. **中文。** 两方程不等于余维 2。

**Resolución.** Restar dos veces la primera deja fila cero; rango $1$. Tomar $y=s,z=t$ da $(x,y,z)=(s-t,s,t)=s(1,1,0)+t(-1,0,1)$. Los dos generadores son independientes por coordenadas segunda y tercera. **Conclusión.** Dimensión $2=3-1$, no $3-2$. La familia vuelve a satisfacer ambas ecuaciones.

## C-03. Eliminar generadores redundantes — 大学水平

**Enunciado propio.** $W=\langle(1,0,1,0),(0,1,0,1),(1,1,1,1)\rangle$. Obtener implícitas. **Análisis ES.** La tercera columna es suma de las dos primeras. **中文。** 先识别独立生成向量，再找全部限制。

**Resolución.** Los vectores de $W$ son $(s,t,s,t)$, de donde $x_1-x_3=0$, $x_2-x_4=0$. A la inversa, esas ecuaciones obligan exactamente a esa forma, probando igualdad de conjuntos. Las ecuaciones son independientes porque sus primeras dos columnas forman identidad, así su rango es $2$ y dimensión del núcleo $4-2=2$. **Conclusión.** La descripción incluye todas y solo las combinaciones iniciales.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
