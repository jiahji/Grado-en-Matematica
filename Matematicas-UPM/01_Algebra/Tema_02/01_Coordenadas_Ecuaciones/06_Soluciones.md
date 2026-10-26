---
title: Coordenadas y ecuaciones / 坐标与子空间方程 — soluciones
subject: Álgebra Lineal
tema: Guía 2.5
type: exercises
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

# Soluciones 2.5 — 完整解答

**Fuentes verificadas:** AL-AP-012, pp. 19–23. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Resoluciones propias de [A25-E01–E06](05_Ejercicios.md).

## A25-E01

**Estrategia ES.** Resolver suma y diferencia. **中文。** 基向量按列展开。**Resolución.** $a+b=x$, $a-b=y$ dan $a=(x+y)/2$, $b=(x-y)/2$. Para $(3,1)$ se obtiene $(2,1)$. La combinación $2(1,1)+(1,-1)=(3,1)$ verifica. **Conclusión.** Fórmula única para todos los vectores.

## A25-E02

**Estrategia ES.** Sustituir $y=z$. **中文。** 不丢掉一个自由参数。**Resolución.** Con $z=t$, $y=t$ y $x=-2t$, todo vector es $t(-2,1,1)$. El generador es no nulo, por lo que constituye una base; dimensión $1$. Su sustitución en las ecuaciones da cero. **Conclusión.** Dos ecuaciones independientes en tres incógnitas dejan un parámetro.

## A25-E03

**Estrategia ES.** Eliminar los dos parámetros. **中文。** 必须给出反向生成验证。**Resolución.** Las combinaciones son $(s,2s+t,t)$, así $y=2x+z$. Recíprocamente, si se cumple, tomar $s=x,t=z$ da el vector. Para $(2,5,1)$, $5=4+1$, y sus coeficientes son $(2,1)$. **Conclusión.** La única ecuación independiente es $2x-y+z=0$.

## A25-E04

**Estrategia ES.** Comparar condiciones, no contar filas. **中文。** 重复约束不缩小集合。**Demostración.** Todo vector que anula las filas anteriores anula el doble de una de ellas, así pertenece al núcleo ampliado. Quien satisface todas las filas nuevas satisface en particular las anteriores. Los núcleos son iguales como conjuntos y, por tanto, tienen la misma dimensión. **Conclusión.** El rango y no el número bruto de filas determina la dimensión.

## A25-E05

**Estrategia ES.** Reconstruir $v=\xi_1(1,1)+\xi_2(0,1)$. **中文。** 坐标方程中的变量不是默认标准分量。**Resolución.** $\xi_1=0$ da $v=(0,\xi_2)$, el eje vertical canónico. En este ejemplo coincide con la ecuación canónica $x=0$ por la forma particular de la primera coordenada; no es una regla universal. Por ejemplo, imponer $\xi_2=0$ daría $v=(\xi_1,\xi_1)$, ecuación canónica $y=x$, no $y=0$. **Conclusión.** La base debe mantenerse explícita incluso cuando una ecuación coincide accidentalmente.

## A25-E06

**Estrategia ES.** Aplicar la estructura de soluciones de Gauss. **中文。** 非唯一来源是参数空间里的零方向。**Demostración.** $Gc=Gc_0$ equivale a $G(c-c_0)=0$, de modo que todos los parámetros son $c=c_0+h$, $h\in\ker G$. Por Gauss hay $k-r>0$ variables libres en el sistema homogéneo, así hay $h\ne0$. Entonces $c_0+h\ne c_0$ representa el mismo vector. **Conclusión.** Una lista generadora redundante no da coordenadas únicas.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
