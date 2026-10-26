---
title: Aplicaciones lineales / 线性映射 — soluciones
subject: Álgebra Lineal
tema: Guía 3.1
type: exercises
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_3_1
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-003/Tema 3_3783d906f8056ce104fc5d6bc1f5548c.pdf
updated: 2026-10-26
---

# Soluciones 3.1 — 完整解答

**Fuentes verificadas:** AL-AP-003, pp. 2–8. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Resoluciones propias de [A31-E01–E06](05_Ejercicios.md).

## A31-E01

**Estrategia ES.** Aplicar primero la condición necesaria en cero. **中文。** 然后验证充分性。**Resolución.** Linealidad exige $f(0)=b=0$. Para $b=0$, $f(\alpha x+\beta y)=a\alpha x+a\beta y=\alpha f(x)+\beta f(y)$ para todo $a$. **Conclusión.** Exactamente $b=0$, sin restricción adicional a $a$.

## A31-E02

**Estrategia ES.** Evaluar una combinación de polinomios. **中文。** 证明应作用于任意多项式。**Resolución.** $E(\alpha p+\beta q)=(\alpha p+\beta q)(2)=\alpha p(2)+\beta q(2)$. Los valores son $1,2,4$. **Conclusión.** La regla es lineal pese a que el argumento evaluado sea fijo y distinto de cero.

## A31-E03

**Estrategia ES.** Hallar coeficientes en la base dada. **中文。** 先分解，再传递系数。**Resolución.** $(x,y)=((x+y)/2)(1,1)+((x-y)/2)(1,-1)$. Así $f(x,y)=((x+y)/2,(x-y)/2)$. Ambas asignaciones se comprueban por sustitución y la fórmula preserva combinaciones. **Conclusión.** T2 garantiza unicidad.

## A31-E04

**Estrategia ES.** Usar la relación de los vectores de partida. **中文。** 相关向量的像不能任意指定。**Resolución.** $(1,1)=(1,0)+(0,1)$ exige $f(1,1)=1+2=3$, incompatible con $4$. **Conclusión.** No existe tal aplicación lineal.

## A31-E05

**Estrategia ES.** Derivar la expresión por coeficientes. **中文。** 定义域和陪域都应封闭。**Resolución.** Si $p=a_0+a_1x+a_2x^2+a_3x^3$, $D(p)=a_1+2a_2x+3a_3x^2$, que pertenece al destino. Sumar coeficientes o multiplicarlos por un escalar antes de derivar tiene el mismo efecto que hacerlo después, probando ambas leyes. La función $|x|$ no es derivable en cero, así la derivada no es una regla definida sobre todas las funciones. **Conclusión.** El dominio correcto es parte de la afirmación matemática.

## A31-E06

**Estrategia ES.** Aplicar las dos linealidades en orden. **中文。** 反例只需保零而破坏一种线性律。**Demostración.** $g(f(\alpha u+\beta v))=g(\alpha f(u)+\beta f(v))=\alpha g(f(u))+\beta g(f(v))$. Para el contraejemplo, $h(x)=x^2$ preserva cero pero $h(2)=4\ne2h(1)$. **Conclusión.** Composición preserva linealidad, condición en cero aislada no basta.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
