---
title: Combinaciones, generadores e independencia / 线性组合、生成与无关
subject: Álgebra Lineal
tema: Guía 2.3
type: example
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_2_3
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-012/Temas 1 y 2(1)(2).pdf
updated: 2026-10-26
---

# Ejemplos 2.3 — 完整例题

**Fuentes verificadas:** AL-AP-012, pp. 8–11. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Todos son desarrollo propio de las definiciones de aula.

## L-01. Pertenencia y redundancia — 基础

**Enunciado.** $u=(1,0,1)$, $v=(0,1,1)$, $w=(1,1,2)$. Describir el generado y decidir pertenencia de $(1,2,3)$ y $(1,2,4)$. **Análisis ES.** Identificar primero la relación $w=u+v$. **中文。** 删除冗余后，保留的两个参数应描述同一个集合。

**Resolución.** $au+bv=(a,b,a+b)$. Por tanto el generado es $z=x+y$. $(1,2,3)=u+2v$ pertenece; $(1,2,4)$ no porque $4\ne1+2$. La lista triple es dependiente por $u+v-w=0$, mientras $u,v$ son independientes pues sus dos primeras coordenadas fuerzan $a=b=0$. **Conclusión.** Se genera un plano, no todo $\mathbb R^3$. **Error frecuente ES.** Tres vectores pueden generar solo un plano si son dependientes. **中文误区。** 三个向量不保证生成三维空间。

## L-02. Polinomios — 综合

**Enunciado.** Estudiar $p=1+x$, $q=1-x$ en $\mathbb R_{\le1}[x]$. **Análisis ES.** Comparar coeficientes del polinomio resultante. **中文。** 多项式相等要求每个系数相等，不能只代入一个点。

**Resolución.** $ap+bq=(a+b)+(a-b)x$. La relación nula exige $a+b=a-b=0$, de donde $a=b=0$. Para obtener $c+dx$, resolver da $a=(c+d)/2$, $b=(c-d)/2$. Así son independientes y generan todos los polinomios del espacio. **Conclusión.** Hay representación única de cada uno. **边界。** La división por $2$ usa el cuerpo real; no se extrapola a característica $2$ sin revisar.

## L-03. Un cambio de cuerpo — 大学水平

**Enunciado.** Comparar independencia de $1,i$ en $\mathbb C$ sobre $\mathbb R$ y sobre $\mathbb C$. **Análisis ES.** La definición cuantifica sobre escalares del cuerpo. **中文。** 改变允许使用的系数，就改变哪些关系算线性关系。

**Resolución.** Para $a,b\in\mathbb R$, $a+bi=0$ fuerza $a=b=0$ por igualdad de partes. Para coeficientes complejos existe $(-i)1+1i=0$ no trivial. **Conclusión.** Independientes sobre $\mathbb R$, dependientes sobre $\mathbb C$. **Error frecuente ES.** Una pregunta de independencia necesita especificar el cuerpo. **中文误区。** 不声明标量域的“无关”问题不完整。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
