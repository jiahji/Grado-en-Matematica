---
title: Espacios de tipo no finito / 非有限型向量空间
subject: Álgebra Lineal
tema: Guía 2.8
type: example
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_2_8
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-012/Temas 1 y 2(1)(2).pdf
updated: 2026-10-26
---

# Ejemplos 2.8 — 完整例题

**Fuentes verificadas:** AL-AP-012, p. 4: ejemplos de sucesiones y funciones; desarrollo posterior como suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Basados en los tipos de espacios de aula, con argumentos propios.

## I-01. Ningún grado máximo sirve — 基础

**Enunciado.** ¿Pueden $p_1,\ldots,p_r$ generar $\mathbb R[x]$? **Análisis ES.** Limitar el grado de sus combinaciones. **中文。** 每份有限列表都有一个有限最高次数。

**Resolución.** Si todos son cero no generan $1$. En otro caso sea $d$ el máximo grado de los no nulos. Una combinación tiene grado a lo sumo $d$ o es cero, así nunca es $x^{d+1}$. **Conclusión.** Ninguna lista finita genera todo el espacio. **Límite ES.** La cancelación del término principal puede bajar el grado, pero no aumentarlo. **中文边界。** 约去最高项只会降低次数，不会产生更高次。

## I-02. Base de soporte finito — 综合

**Enunciado.** Expresar $(2,0,-1,0,\ldots)$ y comparar con $(1,1,\ldots)$. **Análisis ES.** Usar la definición algebraica de generado. **中文。** 只允许有限个非零系数。

**Resolución.** El primer vector es $2e_1-e_3$, con representación única por sus coordenadas. Toda combinación de $e_1,\ldots,e_N$ tiene ceros después de $N$, así no obtiene la sucesión constante. **Conclusión.** La misma familia es base de un subespacio propio, no del ambiente de todas las sucesiones.

## I-03. Funciones de soporte puntual — 大学水平

**Enunciado.** Mostrar que $\mathcal F(\mathbb R,\mathbb R)$ no es finito. **Análisis ES.** Construir familias independientes sin usar continuidad o cálculo. **中文。** 全体函数空间允许在单点支撑的函数。

**Resolución.** Para puntos distintos $t_1,\ldots,t_n$, sea $\delta_{t_j}(x)=1$ si $x=t_j$ y cero en otro caso. Una relación $\sum a_j\delta_{t_j}=0$ evaluada en $t_k$ da $a_k=0$ para cada $k$. Como se pueden elegir arbitrariamente muchos puntos, T1 da no finitud. **Conclusión.** El argumento no afirma que estas funciones sean continuas; trabaja en el espacio indicado, no en un subespacio diferente.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
