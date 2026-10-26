---
title: Espacios de tipo no finito / 非有限型向量空间 — soluciones
subject: Álgebra Lineal
tema: Guía 2.8
type: exercises
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_2_8
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-012/Temas 1 y 2(1)(2).pdf
updated: 2026-10-26
---

# Soluciones 2.8 — 完整解答

**Fuentes verificadas:** AL-AP-012, p. 4: ejemplos de sucesiones y funciones; desarrollo posterior como suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Resoluciones propias de [A28-E01–E05](05_Ejercicios.md).

## A28-E01

**Estrategia ES.** Comparar coeficientes y recordar que cada polinomio tiene soporte finito. **中文。** 没有常数项就从 $x$ 开始。**Resolución.** Todo polinomio de término constante cero es una suma finita $\sum_{n=1}^d a_nx^n$. Si una de estas sumas es cero, todos los coeficientes son cero, así la familia es independiente. No contiene $1$, de modo que el subespacio es propio. **Conclusión.** Base infinita explícita, sin contradicción con la propiedad finita de igualdad de dimensiones.

## A28-E02

**Estrategia ES.** Observar los ceros después del último índice usado. **中文。** “最终常数”允许非零常数尾部。**Resolución.** Toda combinación finita de canónicos tiene soporte finito, y toda sucesión de soporte finito se expresa por sus entradas. La sucesión $(1,1,1,\ldots)$ es eventualmente constante y no tiene soporte finito, así no está en el generado. **Conclusión.** No genera todo el ambiente propuesto.

## A28-E03

**Estrategia ES.** Separar la primera coordenada y usar la condición de suma cero. **中文。** 所有求和在这里都是有限的。**Demostración.** Cero pertenece; suma y múltiplos conservan soporte finito y suma total cero, así es subespacio. Para $v=(a_n)\in H$, $a_1=-\sum_{n\ge2}a_n$, y por tanto $v=\sum_{n\ge2}a_n(e_n-e_1)$, una suma finita. Una relación entre esos vectores se evalúa en cada coordenada $n\ge2$ y fuerza cada coeficiente cero. **Conclusión.** La familia genera y es independiente.

## A28-E04

**Estrategia ES.** Construir primitivas polinómicas y dar un elemento no nulo del núcleo. **中文。** 可证明的具体结构优于无意义的“无限减无限”。**Resolución.** Para $q=\sum_{k=0}^d a_kx^k$, $p=\sum a_kx^{k+1}/(k+1)$ tiene derivada $q$. Las divisiones son válidas en $\mathbb R$. Pero $D(1)=D(0)=0$ y $1\ne0$, así no es inyectiva. **Conclusión.** Sobreyectiva y no inyectiva en el mismo espacio infinito.

## A28-E05

**Estrategia ES.** Usar la definición y un contraejemplo de dimensión pequeña. **中文。** 环境无限维并不强迫所有子空间无限维。**Resolución.** Si $W=V$ y $W$ tuviera generadores finitos, serían generadores finitos de $V$, contradicción. La segunda afirmación es falsa: las constantes forman un subespacio unidimensional propio de $\mathbb R[x]$, y $\{0\}$ también es propio. **Conclusión.** Las dos implicaciones no son equivalentes.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
