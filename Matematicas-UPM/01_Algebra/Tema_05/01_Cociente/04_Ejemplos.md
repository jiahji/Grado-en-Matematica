---
title: Espacio cociente / 商向量空间
subject: Álgebra Lineal
tema: Guía 2.9
type: example
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_2_9
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-005/Tema 5_83d0e9c7501214116f707ed90d6a34d8.pdf
updated: 2026-10-26
---

# Ejemplos de cocientes — 完整例题

**Fuentes verificadas:** AL-AP-005, pp. 2–19. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


## Q-01. Rectas paralelas de aula — 基础

**Enunciado.** AL-AP-005 p. 9: $V=\mathbb R^2$, $W=\{(t,t)\}$. Describir las clases. **Análisis ES.** La diferencia de coordenadas ignora exactamente $W$. **中文。** 每一类是一条平行于对角线的仿射直线。

**Resolución.** $(a,b)\sim(c,d)$ equivale a $a-c=b-d$, o $a-b=c-d$. Las clases quedan identificadas por el real $a-b$. La regla $[(a,b)]\mapsto a-b$ está bien definida, lineal, sobreyectiva y núcleo cero. Además $[(a,b)]=(a-b)[e_1]$ porque la diferencia es $(b,b)\in W$. **Conclusión.** El cociente tiene base $([e_1])$ y dimensión $1$; una clase con $a-b\ne0$ no contiene al origen.

## Q-02. Constantes olvidadas — 综合

**Enunciado propio.** $V=\mathbb R_{\le2}[x]$, $W=\langle1\rangle$. **Análisis ES.** Usar base adaptada y derivada. **中文。** 同一类允许常数项改变。

**Resolución.** Toda clase es $b[x]+c[x^2]$; si esa combinación está en $W$, comparar coeficientes da $b=c=0$. Base $([x],[x^2])$, dimensión $2$. La derivada tiene núcleo $W$ e imagen $\mathbb R_{\le1}[x]$, así induce el isomorfismo $[a+bx+cx^2]\mapsto b+2cx$. **Conclusión.** No se identifica automáticamente con $(b,c)$ sin indicar el mapa; el factor $2$ importa.

## Q-03. Complementario y cociente — 大学水平

**Enunciado propio basado en p. 17.** Si $V=U\oplus W$, identificar $V/W$ con $U$. **Análisis ES.** Elegir la componente única en $U$. **中文。** 这种识别依赖选择的补空间，而商空间本身不依赖补空间。

**Resolución.** Para $v=u+w$, definir $F([v])=u$. Si cambia representante en $W$, las componentes $U$ no cambian por unicidad de descomposición. La regla es lineal, inversa de $u\mapsto[u]$. Ambas composiciones son identidad. **Conclusión.** $V/W\cong U$, pero distintos complementarios dan distintas realizaciones de las clases.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
