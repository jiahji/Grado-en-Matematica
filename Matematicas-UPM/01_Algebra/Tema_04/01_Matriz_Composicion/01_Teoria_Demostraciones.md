---
title: Representación matricial y composición / 矩阵表示与复合
subject: Álgebra Lineal
tema: Guía 3.5
type: theorem
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_3_5
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-004/Tema 4_65298606b99b4fa875367ddfc0765632.pdf
updated: 2026-10-26
---

# Representación matricial y composición — 矩阵表示与复合

**Fuentes verificadas:** AL-AP-004, pp. 2–7. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.

**Organización:** esta unidad integra motivación, definiciones, teoremas, pruebas, conexiones y repaso en un archivo; ejemplos, ejercicios y soluciones se mantienen separados.


## Motivación y definición

**Español.** Una matriz de una aplicación no almacena los vectores de salida como objetos abstractos, sino sus coordenadas en una base de llegada. Cambiar cualquiera de las bases puede cambiar la matriz sin cambiar la aplicación. **中文。** 必须同时标明定义域基与陪域基，尤其不能默认把像直接当作标准列。

Para $f:V\to W$ lineal, bases ordenadas $B=(v_1,\ldots,v_n)$ y $C=(w_1,\ldots,w_m)$, se conserva la notación de aula

$$
M_{B,C}(f)=\bigl([f(v_1)]_C\ \cdots\ [f(v_n)]_C\bigr)\in M_{m\times n}(\mathbb K).
$$

Primer subíndice: base del dominio; segundo: base del destino. Los cálculos matriciales usan columnas aunque en texto un vector de $\mathbb K^n$ también se escriba como tupla. La columna $j$ contiene $m$ números, no el símbolo abstracto $f(v_j)$ sin coordenadas.

## T1. Fórmula de acción y correspondencia

**Hipótesis.** Bases finitas anteriores. **Tesis.** $[f(v)]_C=A[v]_B$, y toda matriz de tamaño $m\times n$ representa una única lineal.

**Estrategia ES.** Expandir en la base inicial y reagrupar coordenadas de imágenes. **策略中文。** 矩阵的列对应基向量的像，乘法中的系数来自输入坐标。

**Demostración.** Si $v=\sum_j x_jv_j$, por linealidad $f(v)=\sum_jx_jf(v_j)$. Escribiendo $f(v_j)=\sum_i a_{ij}w_i$, se obtiene $f(v)=\sum_i(\sum_ja_{ij}x_j)w_i$; por unicidad de coordenadas la columna es $Ax$. Para una matriz arbitraria, defina $f(v_j)=\sum_i a_{ij}w_i$ y aplique el teorema de determinación por base de 3.1; hay una única lineal y su matriz es la dada. **Conclusión.** La correspondencia no exige matrices cuadradas. **中文解释。** 定义式不仅给算法，也证明任意矩阵确实对应一个映射，且没有两个映射拥有同一基下的同一矩阵。

## T2. Composición en el orden correcto

**Hipótesis.** $f:V\to W$, $g:W\to Z$, bases $B,C,D$. **Tesis.**

$$
M_{B,D}(g\circ f)=M_{C,D}(g)M_{B,C}(f).
$$

**Estrategia ES.** Aplicar T1 dos veces a una coordenada arbitraria. **策略中文。** 先发生的映射写在右侧，因为它先作用于列向量。

**Demostración.** Para todo $v$, $[g(f(v))]_D=M_{C,D}(g)[f(v)]_C=M_{C,D}(g)M_{B,C}(f)[v]_B$. Toda columna de $\mathbb K^n$ es coordenada de algún vector; en particular aplicar a las columnas canónicas permite comparar todas las columnas y determina la matriz. **Conclusión.** La composición coincide con multiplicación en ese orden. **中文解释。** 中间空间必须使用同一组基 $C$；若不同，需要插入换基矩阵，而不是直接把两矩阵相乘。

## T3. Identidad, inversa, núcleo e imagen

En la misma base, la identidad tiene matriz $I_n$ porque sus columnas son $[v_j]_B=e_j$. Si $f$ es isomorfismo, sus dos composiciones con $f^{-1}$ y T2 dan

$$
M_{C,B}(f^{-1})=M_{B,C}(f)^{-1}.
$$

Esto también obliga $m=n$. Para el núcleo, T1 y la inyectividad de coordenadas muestran $f(v)=0$ si y solo si $A[v]_B=0$. Para la imagen, las coordenadas de sus generadores son precisamente las columnas de $A$. La aplicación coordenada, isomorfismo, conserva independencia y bases; así rango y nulidad de $f$ coinciden con los de esa matriz. **中文解释。** 列空间是像在目标坐标中的表示，不是把抽象像与一个任意坐标集合不加说明地等同。

**Explicación ES.** El espacio de columnas expresa la imagen en las coordenadas de llegada. Núcleo e imagen abstractos se transportan por los isomorfismos coordenada; no se identifican sin indicar esos mapas. La composición exige la misma base intermedia, y cualquier diferencia se corrige insertando la transición.

## Procedimiento y repaso

Para hallar $M_{B,C}(f)$: aplicar $f$ a cada $v_j$, resolver sus coordenadas en $C$ y colocarlas en columnas sin alterar el orden. Para reconstruir la imagen de un vector: calcular sus coordenadas en $B$, multiplicar y volver a la base $C$.

前置 [同构与坐标](../../Tema_03/04_Isomorfismos/01_Teoria_Demostraciones.md)，后续 [换基](../02_Cambio_Base_Semejanza/01_Teoria_Demostraciones.md)。自测 ES: deducir fórmulas por coordenadas, no memorizarlas solo por tamaño. 中文：维数匹配是必要条件，但两矩阵即使大小匹配，中间基不同仍需处理。[例题](04_Ejemplos.md)、[练习](05_Ejercicios.md)、[解答](06_Soluciones.md)。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
