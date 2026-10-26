---
title: Autoespacios y multiplicidades / 特征空间与重数
subject: Álgebra Lineal
tema: Guía 4.2
type: theorem
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_4_2
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Autoespacios y multiplicidades — 特征空间与重数

**Fuentes verificadas:** AL-GD-001 p. 6, 4.2; suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.

**Organización:** esta unidad integra motivación, definiciones, teoremas, pruebas, conexiones y repaso en un archivo; ejemplos, ejercicios y soluciones se mantienen separados.


## Motivación y definiciones

**Español.** Que una raíz aparezca varias veces en la característica no informa por sí solo de cuántos autovectores independientes existen. Distinguir multiplicidad algebraica de geométrica evita una falsa diagonalización. **中文。** 多项式里“出现几次”与核里“有几个独立方向”是不同计数。

Sea $T:V\to V$ lineal con $\dim V=n<\infty$. Para una raíz $\lambda$ de $\chi_T$, su multiplicidad algebraica（代数重数）$a_\lambda$ es el exponente de $t-\lambda$ en esa característica. La multiplicidad geométrica（几何重数）es $g_\lambda=\dim E_\lambda$. Para una raíz, $g_\lambda\ge1$. El cuerpo debe contener $\lambda$.

## T1. Suma directa de autoespacios distintos

**Hipótesis.** Valores distintos $\lambda_1,\ldots,\lambda_s$. **Tesis.** La suma $E_{\lambda_1}+\cdots+E_{\lambda_s}$ es directa y su dimensión es $\sum_i g_{\lambda_i}$.

**Estrategia ES.** Convertir una descomposición nula en una relación entre autovectores de valores distintos. **策略中文。** 不只证明两两交为零；三个以上还需全局唯一性。

**Demostración.** Si $v_1+\cdots+v_s=0$ con $v_i\in E_{\lambda_i}$, descarte los que sean cero. Si queda alguno, los restantes son autovectores no nulos de valores distintos, independientes por 4.1; la relación con coeficientes todos $1$ sería no trivial. Contradicción. Así todos son cero, que es el criterio de suma directa de varias componentes. Concatenar bases de cada espacio genera la suma y es independiente por separar primero esas componentes y después sus coeficientes; su longitud es la suma indicada. **Conclusión.** Se obtiene la afirmación global, no solo una condición por parejas.

## T2. Comparación de multiplicidades

**Enunciado.** $1\le g_\lambda\le a_\lambda$. Si la característica se escinde, $\sum a_\lambda=n$ y $\sum g_\lambda\le n$.

**Hipótesis/Tesis.** Probar la cota geométrica por la algebraica. **Estrategia ES.** Extender una base del autoespacio y observar un bloque escalar. **策略中文。** 要从真实基结构导出多项式因子，而不是把两个重数按名字视为相同。

**Demostración.** Tome una base de $E_\lambda$ con $g$ elementos y complétela a $V$. Su matriz tiene forma $\begin{pmatrix}\lambda I_g&B\\0&C\end{pmatrix}$, porque cada primer vector básico se escala por $\lambda$. Para una matriz de bloques triangular, el determinante es producto de los determinantes diagonales: en Leibniz, las primeras columnas no pueden usar filas del bloque inferior cero, y por ser una permutación usan exactamente las filas superiores; los términos se separan en las dos permutaciones de los bloques. Así

$$
\chi_T(t)=(t-\lambda)^g\det(tI-C).
$$

Por ello el exponente $a_\lambda$ es al menos $g$. Si la característica se escinde, la suma de exponentes de sus factores lineales es su grado $n$. La suma geométrica es dimensión de un subespacio por T1 y no supera $n$. **Conclusión.** Todas las cotas se justifican. **中文解释。** 若 $a_\lambda=1$，则必有 $g_\lambda=1$；反向不成立。

## Conjugación en matrices reales

Para $A$ real y raíces complejas, $a_\lambda=a_{\bar\lambda}$: conjugando coeficientes de la factorización de $\chi_A$ se mantiene el mismo polinomio real y se intercambian esos factores. La conjugación lleva $E_\lambda$ biyectivamente a $E_{\bar\lambda}$ por 4.1. Aunque es antilineal, conserva independencia: conjugar una relación con coeficientes complejos transforma los coeficientes en sus conjugados; si la familia inicial era independiente, todos son cero. Por tanto $g_\lambda=g_{\bar\lambda}$.

## Límites y uso

Un autoespacio es invariante: $Tv=\lambda v$ sigue dentro del mismo. Una raíz doble puede tener $g=1$ o $g=2$, así no decide sola la existencia de base propia. La cantidad $a_\lambda-g_\lambda$ mide falta de direcciones propias, pero no determina por sí sola todos los tamaños de Jordan: harán falta núcleos de potencias, estudiados después.

前置 [特征值](../01_Autovalores/01_Teoria_Demostraciones.md)；后续 [对角化](../03_Diagonalizacion/01_Teoria_Demostraciones.md)。自测 ES: calcular cada núcleo y justificar la cota por bloques. 中文：不能把代数重数直接当成特征空间维数，也不能由几何重数 1 推出代数重数 1。[例题](04_Ejemplos.md)、[题目](05_Ejercicios.md)、[解答](06_Soluciones.md)。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
