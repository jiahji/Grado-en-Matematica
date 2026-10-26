---
title: Intersección, suma y complementarios / 交、和、直和与补空间 — soluciones
subject: Álgebra Lineal
tema: Guía 2.6
type: exercises
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

# Soluciones 2.6 — 完整解答

**Fuentes verificadas:** AL-AP-012, pp. 24–33. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Resoluciones propias de [A26-E01–E06](05_Ejercicios.md).

## A26-E01

**Estrategia ES.** Parametrizar $U$ e imponer la ecuación de $W$. **中文。** 再用生成向量计算和。**Resolución.** $U=\{(a,b,a)\}$; condición de $W$ da $a+b=0$, así $U\cap W=\langle(1,-1,1)\rangle$. $W$ genera $(1,-1,0),(0,0,1)$. La suma contiene $e_2$ desde $U$, $e_3$ desde $W$ y $(1,-1,0)+e_2=e_1$, por lo que es $\mathbb R^3$. **Conclusión.** Intersección línea, suma total, no directa.

## A26-E02

**Estrategia ES.** Usar la inclusión de cada sumando y la clausura. **中文。** 两个方向都验证。**Demostración.** Si $U+W=U$, para $w\in W$, $w=0+w\in U$. Si $W\subset U$, todo $u+w$ está en $U$, y cada $u=u+0$ está en $U+W$. Las dos inclusiones dan igualdad. **Conclusión.** La identidad caracteriza exactamente la inclusión.

## A26-E03

**Estrategia ES.** Buscar dos direcciones independientes en un ambiente mayor. **中文。** 反例需满足前提又否定张满环境。**Resolución.** En $\mathbb R^3$, $U=\langle e_1\rangle$, $W=\langle e_2\rangle$ tienen intersección cero. Su suma no contiene $e_3$. **Conclusión.** Falta $U+W=V$.

## A26-E04

**Estrategia ES.** Resolver coeficientes y comprobar la intersección. **中文。** 固定补空间之后分解唯一。**Resolución.** $(x,y)=a(1,1)+b(1,-1)$ da $a=(x+y)/2$, $b=(x-y)/2$. Una igualdad entre elementos de las dos rectas exige $(a,a)=(b,-b)$, así $a=b=0$. Por T2 la descomposición calculada es única. **Conclusión.** Es una suma directa que llena $\mathbb R^2$.

## A26-E05

**Estrategia ES.** Agrupar sumas y dar un ejemplo de relación entre tres lados. **中文。** 三个子空间的全局唯一性比两两无交更强。**Demostración.** $(U+W)+Z$ es subespacio por T1, y la asociatividad vectorial lo identifica con todas las sumas $u+w+z$. En $\mathbb R^2$, las rectas $\langle e_1\rangle$, $\langle e_2\rangle$, $\langle e_1+e_2\rangle$ tienen intersecciones por parejas cero, pero $e_1+e_2-(e_1+e_2)=0$ es una descomposición nula con tres componentes no todos cero. **Conclusión.** No es suma directa triple.

## A26-E06

**Estrategia ES.** Usar descomposición única para que la regla esté bien definida. **中文。** 先确认同一向量不会给出不同输出。**Demostración.** T2 proporciona único par $(u,w)$. Para $u\in U$, su descomposición es $u+0$, luego $P(u)=u$. Así $P^2(u+w)=P(u)=u=P(u+w)$. Todo valor de $P$ está en $U$ y todo $u$ se obtiene, así $P(V)=U$. $P(u+w)=0$ equivale a $u=0$, es decir a que $v=w\in W$. **Conclusión.** Es la proyección sobre $U$ a lo largo de $W$; su linealidad se formaliza en el capítulo de aplicaciones.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
