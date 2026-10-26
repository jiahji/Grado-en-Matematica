---
title: Autovalores y polinomio característico / 特征值与特征多项式 — soluciones
subject: Álgebra Lineal
tema: Guía 4.1
type: exercises
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_4_1
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Soluciones 4.1 — 完整解答

**Fuentes verificadas:** AL-GD-001 p. 6, 4.1; suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Resoluciones propias de [A41-E01–E06](05_Ejercicios.md).

## A41-E01

**Estrategia ES.** Resolver diagonalmente. **中文。** 重复特征值只列一个特征空间。**Resolución.** $\chi=(t-1)(t-2)^2$. $E_1=\langle e_1\rangle$, $E_2=\langle e_2,e_3\rangle$. No hay otros valores por T1. **Conclusión.** Una misma raíz puede corresponder a más de una dirección independiente.

## A41-E02

**Estrategia ES.** Aplicar el criterio del núcleo. **中文。** 非零核与非可逆性等价。**Demostración.** $0$ es valor propio si existe $v\ne0$ con $Av=0$. Eso equivale a que el sistema homogéneo tenga solución no trivial y, por Gauss, a singularidad. También $\chi_A(0)=(-1)^n\det A=0$ da la misma equivalencia. **Conclusión.** Dos criterios consistentes.

## A41-E03

**Estrategia ES.** Expandir determinante de orden dos. **中文。** 保持 $tI-A$ 的符号。**Resolución.** $(t-1)(t-4)-(-2)(-3)=t^2-5t-2$. La traza es $5$ y determinante $-2$, como los coeficientes. Las raíces reales son $(5\pm\sqrt{33})/2$, si se desea listarlas. **Conclusión.** No cambiar a $\det(A-tI)$ sin controlar paridad.

## A41-E04

**Estrategia ES.** Usar linealidad y después dividir por el escalar no nulo. **中文。** $a=0$ 时逆推失效。**Demostración.** $(aT+bI)v=a\lambda v+bv=(a\lambda+b)v$. Si $(aT+bI)v=\mu v$ y $a\ne0$, entonces $Tv=((\mu-b)/a)v$. Si $a=0$, el operador es $bI$ y cualquier no cero es propio independientemente de $T$. **Conclusión.** El recíproco exige exactamente esa condición.

## A41-E05

**Estrategia ES.** Conjugar cada coordenada de la igualdad. **中文。** 实矩阵条目不受共轭改变。**Demostración.** $Av=\lambda v$ implica $A\bar v=\overline{Av}=\bar\lambda\bar v$. Si $\bar v=0$, conjugando se tendría $v=0$, imposible. **Conclusión.** Se obtiene un autovector válido para el conjugado.

## A41-E06

**Estrategia ES.** Aplicar preservación de cero. **中文。** 特征向量定义中非零条件不能删。**Resolución.** Para todo escalar, $T0=0=\lambda0$, así una definición que lo permitiera no distinguiría valores. En el espacio de dimensión cero no hay vectores no nulos y por tanto no hay autovalores bajo la definición; la característica vacía es $1$. **Conclusión.** El caso trivial es compatible con el criterio de raíces.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
