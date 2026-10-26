---
title: Fórmula de Grassmann / Grassmann 维数公式
subject: Álgebra Lineal
tema: Guía 2.7
type: example
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_2_7
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-012/Temas 1 y 2(1)(2).pdf
updated: 2026-10-26
---

# Ejemplos de Grassmann — 完整例题

**Fuentes verificadas:** AL-AP-012, p. 24. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Ejemplos propios de dificultad creciente.

## H-01. Dos planos coordenados

**Enunciado.** $U=\langle e_1,e_2\rangle$, $W=\langle e_2,e_3\rangle$ en $\mathbb R^3$. **Análisis ES.** Calcular la intersección antes de usar la fórmula. **中文。** 不可先假定两平面一定相交成线。

**Resolución.** Un vector común tiene primera y tercera coordenadas cero, así $U\cap W=\langle e_2\rangle$. Grassmann da dimensión de la suma $2+2-1=3$. Su inclusión en $\mathbb R^3$ y dimensión completa prueban que es todo el espacio. **Conclusión.** No es directa, aunque llene el ambiente.

## H-02. Forzar una intersección

**Enunciado.** $\dim U=4$, $\dim W=3$ en $\mathbb R^5$. ¿Pueden intersectar solo en cero? **Análisis ES.** Aplicar la cota inferior. **中文。** 两边总共七维的信息无法在五维环境中完全独立。

**Resolución.** $\dim(U\cap W)\ge4+3-5=2$. No puede ser cero. La cota se alcanza con $U=\langle e_1,e_2,e_3,e_4\rangle$, $W=\langle e_3,e_4,e_5\rangle$: intersección generada por $e_3,e_4$, suma total. **Conclusión.** El argumento da imposibilidad y un caso de igualdad.

## H-03. Cálculo de tres espacios

**Enunciado.** Sean las tres rectas $U=\langle e_1\rangle$, $W=\langle e_2\rangle$, $Z=\langle e_1+e_2\rangle$ en $\mathbb R^2$. **Análisis ES.** Agrupar dos primero. **中文。** 不能照搬集合容斥公式。

**Resolución.** $U+W=\mathbb R^2$, dimensión $2$. Después $(U+W)\cap Z=Z$, dimensión $1$. Grassmann aplicado a esos dos espacios da dimensión final $2+1-1=2$. **Conclusión.** La intersección con la suma contiene información que no está en las intersecciones por parejas.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
