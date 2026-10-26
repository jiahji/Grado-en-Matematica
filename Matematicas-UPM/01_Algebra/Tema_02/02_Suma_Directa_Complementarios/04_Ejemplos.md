---
title: Intersección, suma y complementarios / 交、和、直和与补空间
subject: Álgebra Lineal
tema: Guía 2.6
type: example
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_2_6
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-012/Temas 1 y 2(1)(2).pdf
updated: 2026-10-26
---

# Ejemplos 2.6 — 完整例题

**Fuentes verificadas:** AL-AP-012, pp. 24–33. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Tres ejemplos propios que desarrollan los métodos de las pp. 24–33.

## S-01. Intersección y suma — 基础

**Enunciado.** $U=\{(x,y,z):z=0\}$ y $W=\{(x,y,z):x=0\}$. **Análisis ES.** Reunir restricciones para intersección y direcciones para suma. **中文。** 两种操作不能混淆。

**Resolución.** La intersección exige $x=z=0$, así es $\langle e_2\rangle$. $U=\langle e_1,e_2\rangle$, $W=\langle e_2,e_3\rangle$, por lo que la suma genera toda la canónica de $\mathbb R^3$. No es directa porque $e_2\ne0$ está en ambos. **Conclusión.** Suma total no significa suma directa.

## S-02. Directa sin llenar el ambiente — 综合

**Enunciado.** $U=\langle e_1\rangle$, $W=\langle e_2\rangle$ en $\mathbb R^3$. **Análisis ES.** Separar intersección y generación total. **中文。** 该例正是课堂条件缺失的边界。

**Resolución.** $ae_1=be_2$ implica $a=b=0$, así la suma es directa. Su conjunto es $\{(a,b,0)\}$ y no contiene $e_3$. **Conclusión.** $U\oplus W$ es un plano, no $\mathbb R^3$, y la lista $(e_1,e_2)$ es base de ese plano, no del ambiente.

## S-03. Muchos complementarios — 大学水平

**Enunciado.** Para $U=\langle(1,0)\rangle$, hallar todos los complementarios unidimensionales en $\mathbb R^2$. **Análisis ES.** Una dirección complementaria debe tener segunda coordenada no nula y puede normalizarse. **中文。** 归一化可把所有候选放进同一参数族。

**Resolución.** Todo tal complementario tiene forma $W_c=\langle(c,1)\rangle$, $c\in\mathbb R$. Su intersección con $U$ es cero por segunda coordenada. Cada $(x,y)=(x-cy,0)+y(c,1)$, así llenan el ambiente. Si $W_c=W_d$, normalizar segunda coordenada de su generador obliga a $c=d$. **Conclusión.** Infinitos complementarios distintos; la descomposición sí es única una vez fijado $c$.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
