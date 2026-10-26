---
title: Bases, dimensión y Steinitz / 基、维数与交换定理 — soluciones
subject: Álgebra Lineal
tema: Guía 2.4
type: exercises
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_2_4
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-012/Temas 1 y 2(1)(2).pdf
updated: 2026-10-26
---

# Soluciones 2.4 — 完整解答

**Fuentes verificadas:** AL-AP-012, pp. 12–18. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Resoluciones propias de [A24-E01–E06](05_Ejercicios.md).

## A24-E01

**Estrategia ES.** Usar definición de polinomio y comparación de coeficientes. **中文。** 表示存在与唯一都来自系数。**Resolución.** Todo $p$ es $a+bx+cx^2$, así se genera. Si esa expresión es cero, sus tres coeficientes son cero, así hay independencia. La base tiene tres elementos; por invariancia de longitud, la dimensión es $3$. **Conclusión.** No se cuenta solo el grado máximo: también cuenta la constante.

## A24-E02

**Estrategia ES.** Resolver las dos coordenadas y separar $t=1$. **中文。** 不能在退化参数处使用含 $t-1$ 的分母。**Resolución.** Para $t\ne1$, $\lambda+\mu=a$, $\lambda+t\mu=b$ dan $\mu=(b-a)/(t-1)$ y $\lambda=(ta-b)/(t-1)$. Son únicos para cada $(a,b)$, por lo que hay base. Si $t=1$, los dos vectores coinciden y son dependientes. **Conclusión.** Base exactamente cuando $t\ne1$.

## A24-E03

**Estrategia ES.** Exhibir expresiones redundantes. **中文。** 删除时保留生成空间。**Resolución.** Si $u=(1,0,1)$ y $v=(0,1,1)$, el tercero es $u+v$ y el cuarto $2u+v$, así pueden eliminarse. $au+bv=0$ exige $a=b=0$ por primeras coordenadas. $(u,v)$ es base del generado, de dimensión $2$. **Conclusión.** No es base de $\mathbb R^3$, pues no genera todo el ambiente.

## A24-E04

**Estrategia ES.** Aplicar convenios de vacío y el criterio de cero en una familia. **中文。** 基可以有零个元素，不能把零向量本身当作其一个基向量。**Resolución.** La familia vacía genera $\{0\}$ y es independiente porque no hay una relación con coeficientes no nulos. Toda familia no vacía de vectores del espacio cero contiene $0$, luego es dependiente por 2.3. **Conclusión.** Base única como conjunto: vacía; dimensión $0$.

## A24-E05

**Estrategia ES.** Usar longitud de bases e intercambio. **中文。** 数量判据只有在环境维数已知时才能用。**Resolución.** La base canónica prueba $\dim\mathbb R^4=4$. Extraer una base de cuatro generadores no puede quitar ninguno porque la base final debe tener cuatro; son independientes. Cinco independientes contradirían Steinitz frente a la base canónica. Tres independientes no bastan: $(e_1,e_2,e_3)$ no genera $e_4$. **Conclusión.** Generar e independencia tienen límites distintos.

## A24-E06

**Estrategia ES.** Elegir dos segundos vectores fuera de la recta de $e_1$. **中文。** 同一向量可以与不同方向组成基。**Resolución.** $(e_1,e_2)$ y $(e_1,e_1+e_2)$ son bases: en la segunda una relación $ae_1+b(e_1+e_2)=0$ fuerza $b=0$ y $a=0$, y $(x,y)=(x-y)e_1+y(e_1+e_2)$. Son distintas y ambas contienen $e_1$. **Conclusión.** Steinitz garantiza existencia, no elección canónica de compleción.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
