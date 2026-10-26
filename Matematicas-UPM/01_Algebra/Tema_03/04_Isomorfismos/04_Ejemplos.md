---
title: Isomorfismos, coordenadas y productos / 同构、坐标映射与乘积
subject: Álgebra Lineal
tema: Guía 3.4
type: example
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_3_4
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-003/Tema 3_3783d906f8056ce104fc5d6bc1f5548c.pdf
updated: 2026-10-26
---

# Ejemplos de isomorfismos — 完整例题

**Fuentes verificadas:** AL-AP-003, pp. 16–19. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Ejemplos propios que desarrollan coordenadas y productos de AL-AP-003 p. 17.

## O-01. Polinomios y coordenadas — 基础

**Enunciado.** $C(a+bx+cx^2)=(a,b,c)$. **Análisis ES.** Dar inversa además de linealidad. **中文。** 三维对象不是只能是三元数组。

**Resolución.** Coeficientes de una combinación se combinan con los mismos escalares, así es lineal. La inversa $(a,b,c)\mapsto a+bx+cx^2$ compone a identidad en ambos sentidos. **Conclusión.** $\mathbb R_{\le2}[x]\cong\mathbb R^3$ sobre $\mathbb R$.

## O-02. Reales y complejos — 综合

**Enunciado.** Probar $\mathbb R^2\cong\mathbb C$ como espacios reales. **Análisis ES.** La igualdad de partes proporciona la inversa. **中文。** 要明确整个命题使用实数系数。

**Resolución.** $F(a,b)=a+bi$ preserva sumas y escalares reales; inversa es $(\operatorname{Re}z,\operatorname{Im}z)$. Ambas composiciones son identidad. En cambio $\mathbb R$ y $\mathbb C$ como espacios reales tienen dimensiones $1$ y $2$, así no son isomorfos reales. **Conclusión.** No se mezclan dimensiones de cuerpos distintos.

## O-03. Interpolación en tres puntos — 大学水平

**Enunciado.** $E(p)=(p(-1),p(0),p(1))$ en grado a lo sumo $2$. **Análisis ES.** Resolver los coeficientes para salidas arbitrarias. **中文。** 需要证明所有三元数据都恰好对应一个二次以下多项式。

**Resolución.** Para salida $(u,v,w)$, $a=v$, $a-b+c=u$, $a+b+c=w$ dan $b=(w-u)/2$, $c=(w+u)/2-v$. La fórmula define un polinomio para toda salida, y sustitución comprueba los tres valores. Evaluación es lineal y la solución de coeficientes es única. **Conclusión.** Es isomorfismo; no se precisa invocar un teorema de interpolación sin demostrar.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
