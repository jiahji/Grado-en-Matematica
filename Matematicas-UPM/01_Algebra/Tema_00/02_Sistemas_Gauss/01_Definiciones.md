---
title: Sistemas, pivotes y rango / 方程组、主元与秩
subject: Álgebra Lineal
tema: Tema 0 · Guía 1.2
type: definition
language: es-zh
status: complete
tags:
- algebra_lineal
- gauss
- sistemas
- rango
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-000/Tema 0(6).pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-004/Tema 4_65298606b99b4fa875367ddfc0765632.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Sistemas, pivotes y rango — 方程组、主元与秩

**Fuentes:** AL-AP-000, pp. 3–9; AL-AP-004, pp. 13–18. Las definiciones por índices y las precisiones de escalonamiento desarrollan el material de clase.

## 1. Sistema lineal y conjunto de soluciones — 线性方程组与解集

Sea $\mathbb K\in\{\mathbb Q,\mathbb R,\mathbb C\}$, $A=(a_{ij})\in M_{m\times n}(\mathbb K)$ y $b=(b_1,\ldots,b_m)^{\mathsf T}\in\mathbb K^m$. Un sistema lineal（线性方程组）es

$$
\sum_{j=1}^{n}a_{ij}x_j=b_i\quad(1\le i\le m),\qquad Ax=b.
$$

Las incógnitas son $x_1,\ldots,x_n$; los coeficientes $a_{ij}$ y los términos independientes $b_i$ están fijados. Su conjunto de soluciones es

$$
S(A,b)=\{x\in\mathbb K^n:Ax=b\}.
$$

La matriz ampliada（增广矩阵）es $(A\mid b)\in M_{m\times(n+1)}$. El sistema es homogéneo（齐次）si $b=0$; en caso contrario es no homogéneo. Es compatible（相容）si tiene al menos una solución e incompatible（不相容）si no tiene ninguna. Compatible determinado significa solución única; compatible indeterminado significa más de una solución.

**Español.** La linealidad se refiere a las incógnitas: no aparecen productos entre ellas, potencias no lineales ni funciones como seno de una incógnita. Un parámetro puede aparecer en un coeficiente si se fija antes de resolver el sistema.

**中文。** 参数 $a$ 固定时，$ax+y=1$ 对未知量 $x,y$ 仍是线性的；若 $a$ 也被当作未知量，就要重新检查。齐次系统总有零解，因此不能不相容。

## 2. Equivalencia y operaciones elementales — 等价与初等行变换

Dos sistemas con las mismas incógnitas son equivalentes（同解）si sus conjuntos de soluciones son iguales. Se permiten:

1. $F_i\leftrightarrow F_j$: intercambiar filas.
2. $F_i\leftarrow\lambda F_i$, con $\lambda\ne0$: multiplicar una fila por un escalar no nulo.
3. $F_i\leftarrow F_i+\lambda F_j$, con $i\ne j$: sumar a una fila un múltiplo de otra.

Todas se aplican a la **fila completa de la matriz ampliada**, incluidos todos los términos independientes.

**Español.** La operación debe ser reversible. Multiplicar una fila por cero destruye una restricción, por lo que no es una operación elemental admitida. Las operaciones por columnas no conservan en general las soluciones en las mismas incógnitas.

**中文。** 变换系数而不变换右端，会改变方程。交换未知量所在的列也会改变坐标含义；若要交换列，必须另外追踪变量排列，本模块的普通消元只做行变换。

Una matriz elemental（初等矩阵）es la que se obtiene aplicando una operación elemental a $I_m$. Multiplicar una matriz por esa matriz elemental a la izquierda efectúa la misma operación en sus filas. La reversibilidad y esta representación se prueban en el archivo de demostraciones.

## 3. Forma escalonada y reducida — 阶梯形与最简阶梯形

Una matriz está en forma escalonada por filas（行阶梯形）si:

- todas las filas nulas están debajo de las no nulas;
- la primera entrada no nula de cada fila no nula está estrictamente a la derecha de la de la fila anterior.

La primera entrada no nula de una fila no nula se llama pivote（主元）y su columna, columna pivote（主元列）. No se exige que el pivote sea $1$.

La forma escalonada reducida（最简行阶梯形）exige además que cada pivote sea $1$ y que sea la única entrada no nula de su columna. Gauss obtiene una forma escalonada; Gauss–Jordan continúa eliminando por encima de los pivotes.

**Español.** Una matriz triangular con ceros en posiciones diagonales no tiene necesariamente un pivote en cada posición diagonal. Los pivotes se localizan por filas no nulas y primeras entradas no nulas, no suponiendo que el sistema sea cuadrado.

**中文。** 方程组可能有自由变量，阶梯形不必化成单位矩阵。这里不把最简形的唯一性作为未证前提：分类所需的主元数不变性将单独证明。

## 4. Algoritmo y sustitución — 算法与回代

**Algoritmo de Gauss.** Se empieza por la primera fila activa y se inspeccionan las columnas de izquierda a derecha. Si en la columna hay una entrada no nula entre las filas activas, se intercambia su fila con la primera activa; se usa ese pivote para anular las entradas inferiores y se avanza una fila. Si todas las entradas activas son cero, se pasa a la siguiente columna. Se termina al agotar filas o columnas.

**Español.** Resolver $Ax=b$ requiere elegir pivotes en las primeras $n$ columnas, las de coeficientes. Al terminar, una fila de coeficientes cero con término independiente no nulo indica contradicción. Si no aparece, las columnas de coeficientes sin pivote corresponden a variables libres（自由变量）; se les asignan parámetros y se despejan las variables pivote desde abajo hacia arriba.

**中文。** 右端列中的主元表示一个矛盾约束，而不是一个“额外未知量”。当讨论系数矩阵的秩时，只数系数部分的主元；当讨论增广矩阵的秩时，才把右端列也算进去。

## 5. Combinaciones, independencia y rango — 列关系与秩的严格定义

Para columnas $v_1,\ldots,v_k\in\mathbb K^m$, una combinación lineal（线性组合）es $\lambda_1v_1+\cdots+\lambda_kv_k$. Su conjunto se denota $\langle v_1,\ldots,v_k\rangle$, llamado espacio generado（生成空间）. Las columnas son linealmente independientes（线性无关）si

$$
\lambda_1v_1+\cdots+\lambda_kv_k=0\ \Longrightarrow\ \lambda_1=\cdots=\lambda_k=0.
$$

El rango（秩）$\operatorname{rg}(A)$ es el máximo número de columnas linealmente independientes que se pueden seleccionar de $A$. Se admite la selección vacía, de tamaño cero. Como hay $n$ columnas, el máximo existe.

**Español.** Más adelante se identificará con la dimensión del espacio columna. Aquí basta esta definición finita: no depende de ninguna elección del algoritmo y permite demostrar que el número de pivotes es un invariante.

**中文。** 消元保留列之间的线性关系，并不一定保留列张成的那个具体几何子空间。取原矩阵的独立列时，应根据阶梯形确定列编号，再回到原矩阵取列。

## 6. Inversa y varios términos independientes — 逆矩阵与多个右端

Una matriz cuadrada $A\in M_{n\times n}$ es invertible（可逆）si existe $B$ tal que $AB=BA=I_n$. Su inversa se denota $A^{-1}$ y es única, como se probará.

Para $B=(b^{(1)}\ \cdots\ b^{(k)})$, resolver $AX=B$ equivale a resolver cada sistema $Ax^{(j)}=b^{(j)}$. Las operaciones se hacen sobre $(A\mid B)$. Para buscar la inversa se parte de $(A\mid I_n)$ y se intenta obtener $(I_n\mid A^{-1})$.

**Español.** Esta técnica exige una matriz cuadrada de rango completo para obtener inversa. Un sistema rectangular puede tener solución única sin que exista una inversa matricial por ambos lados.

**中文。** “这个右端对应唯一解”和“矩阵可逆”在长方矩阵情形不是同一件事。矩阵必须是方阵，才讨论本模块定义的双侧逆。

继续 [定理](02_Teoremas.md) 与 [证明](03_Demostraciones.md)，返回 [学习入口](00_Introduccion.md)。
