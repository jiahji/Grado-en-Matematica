---
title: Bases, dimensión y Steinitz / 基、维数与交换定理
subject: Álgebra Lineal
tema: Guía 2.4
type: theorem
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

# Bases, dimensión y Steinitz — 基、维数与交换定理

**Fuentes verificadas:** AL-AP-012, pp. 12–18. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.

**Organización:** esta unidad integra motivación, definiciones, teoremas, pruebas, conexiones y repaso en un archivo; ejemplos, ejercicios y soluciones se mantienen separados.


## Motivación y definiciones

**Español.** Una base es un sistema de descripción sin pérdidas ni redundancia. La dimensión solo se define después de demostrar que todas las bases finitas tienen el mismo tamaño. **中文。** 先证明“最小坐标数”不依赖选基，才能把它定义为维数，不能反过来用维数来证明基的等势。

Una base（基）de $V$ es una familia independiente que genera $V$. Una base finita ordenada $B=(v_1,\ldots,v_n)$ identifica cada vector con sus coeficientes únicos. $V$ es de tipo finito si admite una familia generadora finita. La base del espacio cero es vacía y su dimensión será $0$.

## T1. Base y representación única

**Enunciado.** $B$ es base si y solo si todo vector de $V$ admite una expresión única en $B$. **Hipótesis/Tesis.** Existencia y unicidad deben corresponder a dos condiciones diferentes. **Estrategia ES.** Usar la definición de generado y restar representaciones. **策略中文。** 两个方向都要处理，特别是零向量的表示。

**Demostración.** Si $B$ es base, generar proporciona existencia; independencia y resta de dos expresiones proporciona unicidad por 2.3. Recíprocamente, la existencia hace que $B$ genere. Si una combinación de $B$ da cero, se compara con la combinación de coeficientes cero; la unicidad obliga a que los coeficientes sean cero. Así es independiente. **Conclusión.** Se obtiene la proposición de AL-AP-012 p. 12.

## T2. Extraer una base y lema de intercambio

**Enunciado.** Toda familia generadora finita se reduce a una base. Si $B=(u_1,\ldots,u_n)$ es base y $v=\sum a_iu_i$ con $a_j\ne0$, sustituir $u_j$ por $v$ da otra base.

**Estrategia ES.** Eliminar redundancias finitamente y comprobar generación e independencia de la sustitución. **策略中文。** “数量没变”还不是证明；替换后仍需两项性质。

**Demostración.** Si una familia generadora es dependiente, 2.3 permite quitar un vector sin cambiar generado. Repetir disminuye la longitud y debe terminar; la familia final es independiente y sigue generando. Para la sustitución, despejar $u_j=(v-\sum_{i\ne j}a_iu_i)/a_j$ muestra generación. En una relación $cv+\sum_{i\ne j}b_iu_i=0$, sustituir la expansión de $v$ produce una relación en $B$ con coeficiente $ca_j$ en $u_j$. Independencia y $a_j\ne0$ dan $c=0$ y luego todos los $b_i=0$. **Conclusión.** Se prueba el lema sin usar dimensión.

## T3. Teorema de Steinitz y compleción

**Enunciado.** Si $B$ es base de $n$ elementos y $v_1,\ldots,v_m$ son independientes, entonces $m\le n$ y se pueden reemplazar $m$ elementos de $B$ para obtener una base que contiene a todos los $v_i$.

**Hipótesis.** Base finita y familia independiente. **Tesis.** Cota, intercambio y extensión. **Estrategia ES.** Insertar los $v_i$ uno a uno, preservando siempre una base. **策略中文。** 每次必须从尚未替换的原基元素中选可移除者，否则会破坏之前已插入的向量。

**Demostración.** Supongamos que se han insertado $v_1,\ldots,v_r$ en una base que conserva $n-r$ vectores originales. Expresar $v_{r+1}$ en ella requiere algún coeficiente no nulo de un vector original restante: si todos fueran cero, $v_{r+1}$ estaría en el generado de $v_1,\ldots,v_r$, contradiciendo independencia. Sustituir ese vector usando T2 mantiene una base y todos los insertados. Si $m>n$, tras insertar los primeros $n$, el siguiente sería combinación de ellos, otra contradicción. Por tanto $m\le n$ y el proceso termina con todos los $v_i$ dentro de una base. El caso $m=0$ no requiere sustitución. **Explicación ES.** El argumento es una inducción sobre inserciones y demuestra la cota simultáneamente. **中文解释。** 没有先假设“所有基等长”，因此推理没有循环。**Conclusión.** Queda probado Steinitz de la p. 15 y el corolario de compleción.

## T4. Dimensión y subespacios finitos

**Enunciado.** Dos bases finitas de $V$ tienen igual longitud. Se define esa longitud como $\dim V$. Es el máximo número de vectores independientes y el mínimo de generadores. Si $W\le V$ con $V$ finito, $W$ admite base, $\dim W\le\dim V$ y la igualdad equivale a $W=V$.

**Estrategia ES.** Aplicar Steinitz en ambos sentidos y construir una familia independiente maximal dentro de $W$. **策略中文。** 子空间存在有限基也要证明，不能先把它的维数写出来。

**Demostración.** Si las bases tienen longitudes $n,m$, aplicar T3 a cada una como familia independiente frente a la otra da $m\le n$ y $n\le m$. Para cualquier familia generadora finita, T2 extrae una base de $n$ elementos, por lo que tenía al menos $n$; T3 limita a $n$ las familias independientes y una base alcanza ese número.

En $W$, empezar por la familia vacía y añadir un vector fuera del generado mientras exista. Por 2.3 se preserva independencia y por T3 no se pueden añadir más de $n$ vectores; así se termina en una base de $W$. La cota sigue de T3. Si $W$ tiene base de $n$ vectores y $v\in V\setminus W$, añadirlo daría $n+1$ independientes, imposible. Luego igualdad de dimensiones obliga a $W=V$. La implicación inversa es inmediata. **Explicación ES.** La finitud es esencial para esta última equivalencia; no se utiliza una resta de cardinales infinitos. **中文解释。** 无限维情形中真子空间可与整体有相同维数，后续 2.8 会给反例。**Conclusión.** La dimensión está bien definida y los criterios son legítimos.

**Español.** Las bases canónicas de $\mathbb K^n$, matrices y polinomios se justifican por la representación única de entradas o coeficientes. Sus tamaños son $n$, $mn$ y $d+1$, incluyendo el término constante; en todos los casos se incluye el objeto cero.

## Bases canónicas y repaso

AL-AP-012 pp. 12、17 的三类例子：$\mathbb K^n$ 的 $e_i$；$M_{m\times n}$ 的 $E_{ij}$；$\mathbb K_{\le d}[x]$ 的 $1,x,\ldots,x^d$，都由逐坐标或逐系数唯一表示证明是基，故维数分别为 $n,mn,d+1$。多项式空间明确包括零多项式。

**Español.** Un conjunto de $n$ vectores en dimensión $n$ es base si basta demostrar independencia o generación: en el primer caso T3 los extiende sin espacio para añadir, y en el segundo T2 extrae una base sin poder quitar elementos. **中文。** 这个快捷判别必须在有限维且数量恰好相同的前提下使用。

前置 [线性组合](../03_Combinaciones_Independencia/01_Teoria_Demostraciones.md)。后续坐标与 Grassmann 会直接使用这里的交换和扩充定理。先读 [例题](04_Ejemplos.md)，再独立作 [练习](05_Ejercicios.md)，[解答](06_Soluciones.md) 单列。自测：完整复现交换步骤与等维真子空间不可能的证明，而不只背结论。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
