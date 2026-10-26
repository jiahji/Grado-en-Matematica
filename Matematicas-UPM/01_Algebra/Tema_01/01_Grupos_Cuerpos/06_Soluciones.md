---
title: Grupos y cuerpos / 群与域 — soluciones
subject: Álgebra Lineal
tema: Guía 2.1
type: exercises
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_2_1
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-012/Temas 1 y 2(1)(2).pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-000/Tema 0(6).pdf
updated: 2026-10-26
---

# Soluciones 2.1 — 完整解答

**Fuentes verificadas:** AL-AP-012, p. 2; AL-AP-000 pp. 14–15; estructura de grupo como suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Resoluciones propias de [A21-E01–E06](05_Ejercicios.md).

## A21-E01

**Estrategia ES.** Comprobar internos e inversos en cada conjunto. **中文。** 不允许借用集合外的逆元。**Resolución.** El producto de positivos es positivo, $1>0$, $1/a>0$, y se heredan asociatividad y conmutatividad reales; es grupo abeliano. Los enteros no nulos fallan porque el inverso multiplicativo de $2$ es $1/2$, no entero. **Conclusión.** El primer conjunto cumple todos los axiomas y el segundo no.

## A21-E02

**Estrategia ES.** Aplicar diferencia de elementos. **中文。** 加法记号下，子群判别为 $x-y\in H$。**Resolución.** $0\in2\mathbb Z$ y $2m-2n=2(m-n)$ es par, así que el criterio da subgrupo. Los impares no contienen $0$ y además $1-1=0$ no es impar. **Conclusión.** Los pares son subgrupo; los impares no.

## A21-E03

**Estrategia ES.** Multiplicar por $a^{-1}$ a la izquierda y por $b^{-1}$ a la derecha. **中文。** 两侧顺序不能颠倒。**Resolución.** De $axb=c$ resulta $x=a^{-1}cb^{-1}$. Sustituir da $a(a^{-1}cb^{-1})b=(aa^{-1})c(b^{-1}b)=c$. Las transformaciones son reversibles, luego es la única solución. **误区。** $a^{-1}b^{-1}c$ no es una expresión equivalente en un grupo arbitrario.

## A21-E04

**Estrategia ES.** Verificar ambos productos y usar unicidad. **中文。** 给出候选逆元还要检查其定义。**Resolución.** $aa^{-1}=a^{-1}a=e$, por lo que $a$ es inverso de $a^{-1}$ y $(a^{-1})^{-1}=a$. Aplicando dos veces la fórmula de producto, $(abc)^{-1}=c^{-1}(ab)^{-1}=c^{-1}b^{-1}a^{-1}$; al multiplicar por $abc$ a cada lado se cancelan factores vecinos y se obtiene $e$. **Conclusión.** El orden se invierte en toda la cadena.

## A21-E05

**Estrategia ES.** Usar repetición de potencias dentro del grupo ambiente. **中文。** 有限性迫使幂重复，才能从只知乘法封闭恢复单位和逆元。**Demostración.** Para $h\in H$, las potencias positivas $h,h^2,\ldots$ están en $H$. Por finitud hay $i<j$ con $h^i=h^j$. Cancelar en $G$ da $h^{j-i}=e$, de modo que $e\in H$. Si $j-i=1$, $h=e$ y su inverso está en $H$; si es mayor, $h^{j-i-1}\in H$ y es inverso de $h$. Esto vale para cada $h$, y la asociatividad se hereda; $H$ es subgrupo. En el grupo aditivo entero, los positivos son no vacíos y cerrados por suma, pero no contienen $0$ ni opuestos; son infinitos. **Conclusión.** Sin finitud la afirmación falla.

## A21-E06

**Estrategia ES.** Separar los dos grupos asociados al cuerpo. **中文。** 域的加法群包括零，乘法群不包括零。**Resolución.** $\mathbb Z$ tiene grupo aditivo y producto interno, pero $2$ no tiene inverso en $\mathbb Z$, así que no es cuerpo. Para $a/b\in\mathbb Q\setminus\{0\}$, $a,b$ son enteros no nulos y su inverso $b/a$ también es racional no nulo. El producto de dos de tales elementos vuelve a ser racional no nulo, $1$ es neutro y se heredan asociatividad y conmutatividad. **Conclusión.** El grupo multiplicativo racional excluye cero y ello es perfectamente compatible con la definición de cuerpo.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
