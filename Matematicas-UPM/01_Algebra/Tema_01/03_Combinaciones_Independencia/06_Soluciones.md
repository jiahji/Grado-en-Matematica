---
title: Combinaciones, generadores e independencia / 线性组合、生成与无关 — soluciones
subject: Álgebra Lineal
tema: Guía 2.3
type: exercises
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

# Soluciones 2.3 — 完整解答

**Fuentes verificadas:** AL-AP-012, pp. 8–11. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Resoluciones propias de [A23-E01–E06](05_Ejercicios.md).

## A23-E01

**Estrategia ES.** Construir una relación concreta. **中文。** 非平凡是指系数不全零，不是向量和不为零。**Resolución.** Si $v_j=0$, el coeficiente $1$ en esa posición y cero en las demás da suma cero no trivial. Si $v_i=v_j$ con $i\ne j$, usar $1,-1$ en esas posiciones; no son ambos cero en ningún cuerpo. **Conclusión.** Ambas familias son dependientes.

## A23-E02

**Estrategia ES.** Igualar las dos coordenadas a cero. **中文。** 参数退化处单独处理。**Resolución.** $a(1,1)+b(1,t)=0$ da $a+b=0$ y $a+tb=0$, luego $(t-1)b=0$. Si $t\ne1$, $b=a=0$; para cualquier $(x,y)$, $b=(y-x)/(t-1)$, $a=x-b$, por lo que el generado es $\mathbb R^2$. Si $t=1$, los vectores coinciden y generan la recta $\{(s,s):s\in\mathbb R\}$. **Conclusión.** Independencia exactamente para $t\ne1$.

## A23-E03

**Estrategia ES.** Usar las primeras coordenadas para fijar coeficientes. **中文。** 剩下坐标产生相容条件。**Resolución.** $a(1,0,1)+b(0,1,1)=(a,b,a+b)$. Igualar a $(1,2,c)$ fuerza $a=1,b=2,c=3$. La combinación con esos valores sí funciona. **Conclusión.** Solo $c=3$, con coeficientes únicos $1,2$.

## A23-E04

**Estrategia ES.** Extender por ceros una relación de la subfamilia; para generadores usar inclusiones. **中文。** 不新增理论，直接运用定义。**Demostración.** Una relación nula en una subfamilia se convierte en relación de la familia completa poniendo cero en las posiciones ausentes; independencia fuerza todos los coeficientes cero. Si $S\subset T\subset V$ y $\langle S\rangle=V$, entonces $V=\langle S\rangle\subset\langle T\rangle\subset V$, luego igualdad. **Conclusión.** Quitar conserva independencia; añadir conserva generación, no necesariamente las propiedades opuestas.

## A23-E05

**Estrategia ES.** Usar minimalidad y probar ambas inclusiones. **中文。** 交集中的子空间族不空，因为至少包含 $V$。**Demostración.** Todo subespacio que contiene $S$ contiene $\langle S\rangle$, así este generado está en la intersección. Por T1 el propio $\langle S\rangle$ es uno de los subespacios de la familia, así la intersección está en él. Si $S$ es vacío, todos los subespacios lo contienen y uno de ellos es $\{0\}$; su intersección es $\{0\}$, como el generado vacío. **Conclusión.** Vale en todos los casos indicados.

## A23-E06

**Estrategia ES.** Comparar coeficientes formales. **中文。** 有限次数的组合不会凭空产生更高次项。**Resolución.** $a+bx+cx^2=0$ como polinomio exige $a=b=c=0$. Ninguna combinación tiene coeficiente no nulo de $x^3$, por lo que no genera $x^3$. **Conclusión.** Independencia no implica generar el ambiente; el ejemplo triple de L-01 genera su plano con redundancia y muestra que generar tampoco implica independencia.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
