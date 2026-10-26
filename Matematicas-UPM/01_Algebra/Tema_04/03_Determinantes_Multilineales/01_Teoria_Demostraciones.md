---
title: Determinantes y formas alternadas / 行列式与交替多线性形式
subject: Álgebra Lineal
tema: Guía 3.7
type: theorem
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_3_7
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Determinantes y formas alternadas — 行列式与交替多线性形式

**Fuentes verificadas:** AL-GD-001 p. 6, 3.7; desarrollo propio sin apuntes específicos recibidos. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.

**Organización:** esta unidad integra motivación, definiciones, teoremas, pruebas, conexiones y repaso en un archivo; ejemplos, ejercicios y soluciones se mantienen separados.


## Motivación y definiciones

**Español.** El determinante resume si $n$ direcciones de un espacio de dimensión $n$ son independientes. La multilinealidad y la anulación de direcciones repetidas explican sus reglas, en vez de tratarlo como una fórmula de signos sin significado. **中文。** 先建立交替形式，再导出计算与可逆判别，避免把一个算法当作全部理论。

Una forma $k$-lineal（$k$ 重线性形式）es $\omega:V^k\to\mathbb K$, lineal en cada argumento manteniendo los otros fijos. Es alternada（交替）si vale cero cuando dos argumentos coinciden. Para nuestro cuerpo $\mathbb Q,\mathbb R$ o $\mathbb C$, intercambiar dos argumentos cambia el signo: expandir la igualdad con $u+v$ en las dos posiciones deja $\omega(\ldots,u,\ldots,v,\ldots)+\omega(\ldots,v,\ldots,u,\ldots)=0$, porque los dos términos repetidos se anulan.

Para $A\in M_{n\times n}$ se define

$$
\det A=\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)\prod_{j=1}^n a_{\sigma(j),j}.
$$

$S_n$ es el conjunto de permutaciones y $\operatorname{sgn}(\sigma)=(-1)^{\text{número de inversiones}}$. Un intercambio adyacente cambia esa paridad; ordenar una permutación mediante ellos demuestra que cada intercambio cambia signo y que signos se multiplican al componer. Se usa $\det I=1$ y, como convenio de menores, determinante de la matriz $0\times0$ igual a $1$.

## T1. Existencia y unicidad de la forma volumen

**Hipótesis.** Base ordenada $B=(e_1,\ldots,e_n)$ de $V$. **Tesis.** Una forma alternada $n$-lineal queda determinada por $c=\omega(e_1,\ldots,e_n)$ y vale $c$ por el determinante de coordenadas de los argumentos.

**Estrategia ES.** Expandir todos los argumentos y eliminar términos repetidos. **策略中文。** 只有恰好选中所有不同基向量的项能够存活。

**Demostración.** Escribiendo $v_j=\sum_i a_{ij}e_i$, la multilinealidad da una suma sobre todas las listas $(i_1,\ldots,i_n)$. Las que repiten índice dan cero. Las restantes son permutaciones; reordenarlas por intercambios adyacentes da $\omega(e_{\sigma(1)},\ldots,e_{\sigma(n)})=\operatorname{sgn}(\sigma)c$. Así aparece exactamente la fórmula indicada. A la inversa, la suma de Leibniz es lineal en cada columna porque cada monomio usa una sola entrada de ella. Si dos columnas coinciden, emparejar cada permutación con la que intercambia esas dos posiciones da productos iguales y signos opuestos, luego cero. En $I$ solo sobrevive la permutación identidad y da $1$. Esto construye la forma normalizada y prueba existencia y unicidad. **Conclusión.** La fórmula y la interpretación se justifican conjuntamente.

Además toda forma alternada de $k>\dim V$ argumentos es cero: los argumentos son dependientes; despejar uno de ellos en combinación de los restantes y distribuir produce solo términos con dos argumentos repetidos. **中文解释。** 交替形式的存在反映独立方向的数量，不是任意维数都能有非零的“最高体积”。

## T2. Producto, trasposición e invertibilidad

**Enunciado.** $\det(AB)=\det A\det B$, $\det A^{\mathsf T}=\det A$, y $\det A\ne0$ si y solo si $A$ es invertible.

**Estrategia ES.** Fijar el primer mapa como transformación de una forma alternada; para trasposición, cambiar una permutación por su inversa. **策略中文。** 先证明乘法定理，再用已知矩阵可逆性，避免循环定义。

**Demostración.** Para $A$ fija, $\eta(v_1,\ldots,v_n)=\det(Av_1,\ldots,Av_n)$ es alternada y multilineal porque $A$ es lineal. Por T1, $\eta$ es $\det A$ veces la forma normalizada, ya que al evaluar en los canónicos se obtiene $\det A$. Poner los $v_j$ iguales a las columnas de $B$ da multiplicatividad.

En la fórmula de $\det A^{\mathsf T}$, el producto es $\prod_j a_{j,\sigma(j)}$. Reindexar con $\tau=\sigma^{-1}$ produce $\prod_i a_{\tau(i),i}$, y la inversa tiene el mismo signo porque $\operatorname{sgn}(\sigma)\operatorname{sgn}(\sigma^{-1})=1$. Se obtiene la misma suma que para $A$.

Si las columnas son dependientes, una es combinación de las otras; multilinealidad y alternación dan determinante cero. Si son independientes, forman base en dimensión $n$, así $A$ tiene inversa por Gauss. Multiplicatividad da $1=\det I=\det A\det A^{-1}$, obligando a $\det A\ne0$. Las equivalencias entre independencia cuadrada e inversa ya se probaron sin determinantes, así no hay circularidad. **Conclusión.** Se prueban todas las afirmaciones.

## T3. Operaciones y cálculo triangular

Intercambiar dos columnas cambia signo; multiplicar una por $a$ multiplica determinante por $a$; añadir un múltiplo de otra no lo cambia. **Prueba.** Las primeras dos son alternación y multilinealidad. En la tercera, distribuir produce el determinante original más uno con dos columnas iguales, que es cero. Por trasposición, valen las mismas reglas para filas.

Si $A$ es triangular superior, un término no nulo de Leibniz necesita $\sigma(j)\le j$ para cada $j$. Como ambas sumas de índices son iguales, todas esas desigualdades son igualdades y solo queda la identidad; así $\det A=\prod_i a_{ii}$. Para triangular inferior se transpone. Estas reglas permiten usar Gauss recordando intercambios y escalados. No se aplica una regla de Sarrus de orden tres a órdenes mayores.

## T4. Cofactores y adjunta

Sea $A_{ij}$ la matriz que suprime fila $i$ y columna $j$ y $C_{ij}=(-1)^{i+j}\det A_{ij}$. Entonces

$$
\det A=\sum_i a_{ij}C_{ij}=\sum_j a_{ij}C_{ij},
$$

con columna fija en la primera suma y fila fija en la segunda. **Prueba.** Agrupar en Leibniz las permutaciones con $\sigma(j)=i$ deja las permutaciones del menor. Llevar esa fila y columna a la primera posición necesita $(i-1)+(j-1)$ intercambios, de paridad $i+j$, dando el signo del cofactor. La fórmula de fila se sigue por trasposición.

Defina $\operatorname{adj}A=(C_{ji})$. El producto satisface

$$
A\operatorname{adj}A=\operatorname{adj}A\,A=(\det A)I.
$$

**Demostración.** La entrada $(i,j)$ del primer producto es $\sum_k a_{ik}C_{jk}$. Si $i=j$, expansión por esa fila da $\det A$. Si $i\ne j$, es la expansión de la matriz que sustituye la fila $j$ por la $i$, con dos filas iguales; da cero porque los menores que eliminan $j$ no cambian. El producto opuesto se comprueba con columnas de la misma manera. Así, si $\det A\ne0$, $A^{-1}=\operatorname{adj}A/\det A$. **中文解释。** 伴随矩阵需要转置余子式索引；只排列 $C_{ij}$ 不转置通常不是所需矩阵。

## T5. Rango y menores

El rango de $A$ es el mayor orden de un menor no nulo. **Prueba.** Un menor no nulo de orden $r$ implica que esas $r$ columnas restringidas son independientes; una relación de columnas originales daría relación restringida y sería trivial, así rango al menos $r$. Si el rango real es $r$, elegir $r$ columnas independientes da una matriz $G$ de rango $r$; por igualdad de rango de filas y columnas, elegir $r$ filas independientes de $G$ produce una submatriz cuadrada invertible, con determinante no nulo por T2. Un menor de mayor orden contradice el primer argumento. El caso rango cero corresponde a todas las entradas cero y usa el menor vacío como convenio.

**Explicación ES.** La adjunta usa los cofactores traspuestos. La forma alternada se anula en familias dependientes; esa propiedad, junto con multilinealidad, sustenta las reglas de cálculo. La interpretación de volumen ayuda en el caso real, pero la prueba es algebraica.

## T6. Todas las formas alternadas de grado $k$

**Hipótesis.** $\dim V=n$, base $B=(e_1,\ldots,e_n)$, $1\leq k\leq n$.

**Tesis.** El espacio de formas alternadas $k$-lineales tiene dimensión $\binom nk$. Una forma queda determinada por sus valores sobre las listas $e_{i_1},\ldots,e_{i_k}$ con $i_1<\cdots<i_k$.

**Estrategia ES.** Expandir cada argumento en la base, descartar repeticiones y agrupar por el conjunto de índices usados. Cada grupo es un determinante de orden $k$.

**策略（中文）。** 顶次形式只需要一个数，一般 $k$ 次形式则要为每组不同的 $k$ 个基方向指定一个数。不是任意的 $n^k$ 个数据都独立，交替条件把重复与换序的信息固定下来。

**Demostración.** Para cada conjunto ordenado $I=(i_1<\cdots<i_k)$ defina $\omega_I(v_1,\ldots,v_k)$ como el determinante de la matriz de las coordenadas de los $v_j$ restringidas a las filas $i_1,\ldots,i_k$. Por las propiedades de determinante es alternada y $k$-lineal. Si se evalúa en otra lista creciente $e_{j_1},\ldots,e_{j_k}$, el resultado es $1$ cuando $I=J$ y $0$ en otro caso: si los conjuntos difieren, alguna columna de esa submatriz es cero; si coinciden, es identidad.

Sea ahora $\omega$ cualquier forma alternada. Escriba $v_j=\sum_i a_{ij}e_i$ y distribuya por multilinealidad. Los términos con índices repetidos se anulan. Para un conjunto creciente $I$ fijo, los demás términos recorren sus permutaciones y suman

$$
\omega(e_{i_1},\ldots,e_{i_k})
\sum_{\sigma\in S_k}\operatorname{sgn}(\sigma)\prod_{j=1}^k a_{i_{\sigma(j)},j}
=\omega(e_{i_1},\ldots,e_{i_k})\,\omega_I(v_1,\ldots,v_k).
$$

Sumando sobre todos los $I$ se expresa $\omega$ como combinación de los $\omega_I$, lo que prueba generación. En una relación $\sum_I c_I\omega_I=0$, evaluar en la lista creciente de cada $J$ da $c_J=0$ por los valores calculados; se prueba independencia. Hay $\binom nk$ subconjuntos de $k$ índices, así esa es la dimensión. $\square$

**Explicación ES.** Para $k=n$ solo hay un conjunto de índices y se recupera T1. Para $k>n$ todas las formas se anulan, como ya se probó por dependencia. Esta clasificación no requiere introducir productos exteriores como objetos nuevos.

**中文。** 在三维空间中，交替双线性形式可独立测量三组坐标方向的有向面积；一个三线性体积形式则只剩一个比例系数。坐标选择影响这些基形式的表达，但不改变分类维数。

## Repaso y dependencia

前置 [基、线性映射及矩阵表示](../01_Matriz_Composicion/01_Teoria_Demostraciones.md)，后续特征多项式将使用乘法和相似不变性：$\det(P^{-1}(tI-A)P)=\det(tI-A)$，由 T2 和 $\det P^{-1}\det P=1$。**Español.** Probar reglas mediante alternación, controlar signos y distinguir determinante, cofactor y adjunta. **中文。** 体积直觉辅助理解，不代替任意域上的代数证明。[例题](04_Ejemplos.md)、[练习](05_Ejercicios.md)、[解答](06_Soluciones.md)。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
