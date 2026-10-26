---
title: Soluciones de sistemas y Gauss / 方程组与消元完整解答
subject: Álgebra Lineal
tema: Tema 0 · Guía 1.2
type: exercises
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

# Soluciones de sistemas y Gauss — 完整解答

**Procedencia:** soluciones propias de [G-E01–G-E12](05_Ejercicios.md); las reglas se prueban en [Demostraciones](03_Demostraciones.md). Los ejercicios son entrenamiento propio, no una hoja oficial.

## G-E01 — Linealidad

**Estrategia — Español.** Fijar primero qué símbolos representan incógnitas; después examinar sus productos y exponentes.

**策略 — 中文。** 线性性相对于未知量，而不是相对于纸上出现的所有字母。

**Solución.** $2x-3y=1$ es lineal. $xy=1$ no lo es, por contener un producto entre incógnitas. $x+y^2=0$ no lo es, por el exponente $2$ de $y$. $(1+i)x-y=0$ es lineal sobre $\mathbb C$, porque $1+i$ es un escalar fijo. Para $a$ fijado, $ax+y=1$ es lineal en $x,y$; si $a$ es una tercera incógnita, el producto $ax$ impide que sea una ecuación lineal en $a,x,y$.

**解释与易错点。** 系数不是实数不会自动破坏线性；需要看它是否属于所选标量域，并且是否固定。

## G-E02 — Operaciones inválidas

**Estrategia — Español.** Comparar directamente las soluciones y exigir reversibilidad.

**策略 — 中文。** 原方程的一个解仍满足新方程，只能证明单向包含，不能证明等价。

**Solución.** $x=1$ tiene conjunto de soluciones $\{1\}$; $0=0$ lo tiene igual a todo $\mathbb R$.Se han introducido soluciones y no existe operación inversa que recupere la restricción. Las inversas permitidas son: intercambiar otra vez las mismas filas; multiplicar por $1/\lambda$ cuando $\lambda\ne0$; y sustituir $F_i\leftarrow F_i-\lambda F_j$ para deshacer $F_i\leftarrow F_i+\lambda F_j$.

**解释与易错点。** 非零条件正是保证不丢失约束的条件；不能将它当作可忽略的技术细节。

## G-E03 — Una variable libre

**Estrategia — Español.** Restar el doble de la primera fila a la segunda y tomar $z$ libre.

**策略 — 中文。** 该系统有两个主元和三个未知量，剩下一个参数；最后验证整个参数族。

**Solución.**

$$
\left(\begin{array}{ccc|c}1&1&1&2\\2&3&1&5\end{array}\right)
\xrightarrow{F_2\leftarrow F_2-2F_1}
\left(\begin{array}{ccc|c}1&1&1&2\\0&1&-1&1\end{array}\right).
$$

Sea $z=t$. La segunda fila da $y=1+t$ y la primera $x=1-2t$. Ambos rangos son $2$, con un parámetro. La familia es $S=\{(1-2t,1+t,t):t\in\mathbb K\}$. Sustituyendo se obtiene $(1-2t)+(1+t)+t=2$ y $2(1-2t)+3(1+t)+t=5$ para todo $t$.

**解释与易错点。** 回代验证了所有 $t$ 都给解；消元与参数化的可逆性保证没有漏解。

## G-E04 — Incompatibilidad

**Estrategia — Español.** Eliminar la primera columna y observar también el término independiente.

**策略 — 中文。** 系数行相关本身不产生矛盾，关键在右端是否满足相同倍数关系。

**Solución.**

$$
\left(\begin{array}{cc|c}1&1&1\\2&2&3\end{array}\right)
\xrightarrow{F_2\leftarrow F_2-2F_1}
\left(\begin{array}{cc|c}1&1&1\\0&0&1\end{array}\right).
$$

La última fila dice $0=1$. Así $\operatorname{rg}(A)=1$ y $\operatorname{rg}(A\mid b)=2$; el sistema es incompatible y $S=\varnothing$.

**解释与易错点。** 不能把增广列中的主元算成第二个未知量的主元。

## G-E05 — Rango y columnas originales

**Estrategia — Español.** Eliminar la segunda fila redundante y usar la tercera para el segundo pivote; volver después a las columnas originales.

**策略 — 中文。** 先用阶梯形选编号，再在原矩阵写生成关系，不混用变换后的具体列向量。

**Solución.** $F_2\leftarrow F_2-2F_1$ y después $F_2\leftrightarrow F_3$ producen

$$
U=\begin{pmatrix}1&2&3&4\\0&1&1&0\\0&0&0&0\end{pmatrix}.
$$

Hay dos pivotes, por lo que $\operatorname{rg}(A)=2$. Las columnas originales $a_1=(1,2,0)^{\mathsf T}$ y $a_2=(2,4,1)^{\mathsf T}$ son independientes: $\alpha a_1+\beta a_2=0$ da primero $\beta=0$ en la tercera coordenada y después $\alpha=0$ en la primera. Las otras son $a_3=a_1+a_2$ y $a_4=4a_1$, como se comprueba por sus tres entradas.

Para $Ax=0$, la segunda fila da $x_2=-x_3$ y la primera $x_1=-x_3-4x_4$. Con $x_3=s$, $x_4=t$:

$$
x=(-s-4t,-s,s,t)=s(-1,-1,1,0)+t(-4,0,0,1).
$$

La sustitución en las tres filas de $A$ da respectivamente $0$, $0$ y $-s+s=0$. Son dos parámetros independientes porque se recuperan directamente de $x_3,x_4$.

**解释与易错点。** 原矩阵有三行非零，但秩只有 2；没有阶梯化就数非零行会出错。

## G-E06 — Discusión de parámetros

**Estrategia — Español.** Reducir antes de dividir y distinguir $a=1$ de $a\ne1$.

**策略 — 中文。** 所有实数参数要覆盖完整：先分 $a$，在退化情形再分 $b$，不能漏掉边界。

**Solución.** Restando la primera ecuación a las otras queda $(a-1)y=0$ y $(a-1)z=b-1$, junto con $x+y+z=1$.

Si $a\ne1$, $y=0$, $z=(b-1)/(a-1)$ y $x=(a-b)/(a-1)$; ambos rangos valen $3$ y la solución es única. Si $a=1,b=1$, queda solo la primera ecuación: ambos rangos valen $1$ y $S=\{(1-s-t,s,t):s,t\in\mathbb R\}$.Si $a=1,b\ne1$, la tercera ecuación reducida da $0=b-1\ne0$; los rangos son $1$ y $2$, y no hay soluciones.

La primera familia se verifica mediante $x+z=1$ y $x+az=b$; la segunda mediante la suma de coordenadas igual a $1$. Los casos son exhaustivos porque o bien $a\ne1$ o bien $a=1$, y en este último caso o bien $b=1$ o bien $b\ne1$.

**解释与易错点。** 最终答案包括条件、秩和解集，而不只是一个含参数分母的公式。

## G-E07 — Inversa y sistema

**Estrategia — Español.** Reducir $(A\mid I_2)$ sin omitir las operaciones sobre la derecha.

**策略 — 中文。** 求出的逆矩阵还要同时检查左乘和右乘，并用其解原系统。

**Solución.**

$$
\left(\begin{array}{cc|cc}1&2&1&0\\3&5&0&1\end{array}\right)
\xrightarrow{F_2\leftarrow F_2-3F_1}
\left(\begin{array}{cc|cc}1&2&1&0\\0&-1&-3&1\end{array}\right)
\xrightarrow{F_2\leftarrow-F_2}
\left(\begin{array}{cc|cc}1&2&1&0\\0&1&3&-1\end{array}\right)
\xrightarrow{F_1\leftarrow F_1-2F_2}
\left(\begin{array}{cc|cc}1&0&-5&2\\0&1&3&-1\end{array}\right).
$$

Así $B=A^{-1}=\begin{pmatrix}-5&2\\3&-1\end{pmatrix}$. Los productos son

$$
AB=\begin{pmatrix}-5+6&2-2\\-15+15&6-5\end{pmatrix}=I_2,\quad
BA=\begin{pmatrix}-5+6&-10+10\\3-3&6-5\end{pmatrix}=I_2.
$$

La solución es $x=B(1,0)^{\mathsf T}=(-5,3)^{\mathsf T}$, y $A(-5,3)^{\mathsf T}=(-5+6,-15+15)^{\mathsf T}=(1,0)^{\mathsf T}$.

**解释与易错点。** 若右端换了，只需把新的右端与同一逆矩阵相乘；但数值实践中通常优先复用消元分解，见后续数值模块。

## G-E08 — Dos términos independientes

**Estrategia — Español.** Empezar con la fila que ya tiene un coeficiente $1$.

**策略 — 中文。** 交换整行后两列右端一起跟随，不能只交换左侧系数。

**Solución.**

$$
\left(\begin{array}{cc|cc}2&1&1&3\\1&1&0&2\end{array}\right)
\xrightarrow{F_1\leftrightarrow F_2}
\left(\begin{array}{cc|cc}1&1&0&2\\2&1&1&3\end{array}\right)
\xrightarrow{F_2\leftarrow F_2-2F_1}
\left(\begin{array}{cc|cc}1&1&0&2\\0&-1&1&-1\end{array}\right)
\xrightarrow{F_2\leftarrow-F_2}
\left(\begin{array}{cc|cc}1&1&0&2\\0&1&-1&1\end{array}\right)
\xrightarrow{F_1\leftarrow F_1-F_2}
\left(\begin{array}{cc|cc}1&0&1&1\\0&1&-1&1\end{array}\right).
$$

Por tanto $X=\begin{pmatrix}1&1\\-1&1\end{pmatrix}$ y

$$
AX=\begin{pmatrix}2-1&2+1\\1-1&1+1\end{pmatrix}
=\begin{pmatrix}1&3\\0&2\end{pmatrix}=B.
$$

Las columnas $(1,-1)^{\mathsf T}$ y $(1,1)^{\mathsf T}$ son las soluciones únicas para cada columna de $B$.

**解释与易错点。** 解矩阵的列对应原右端的列；不要按行把结果拆成两个系统。

## G-E09 — Estructura del conjunto de soluciones

**Hipótesis.** $Ax_p=b$.

**Tesis.** Las dos inclusiones y la afirmación sobre diferencias.

**Estrategia — Español.** Distribuir $A$ sobre suma y resta.

**策略 — 中文。** 把集合等式拆成两个方向，不能只验证构造出的向量都是解而不证明覆盖所有解。

**Demostración.** Si $h\in S(A,0)$, $A(x_p+h)=b+0=b$, por lo que $x_p+S(A,0)\subset S(A,b)$.Si $x\in S(A,b)$, $A(x-x_p)=b-b=0$, luego $x=x_p+(x-x_p)$ pertenece a $x_p+S(A,0)$.Así vale la igualdad. Si $Ax=Ay=b$, entonces $A(x-y)=0$.

Para la suma, considérese la única ecuación $x=1$. Dos soluciones, ambas iguales a $1$, suman $2$, que no es solución. En general $A(x+y)=2b$, que no es $b$ cuando $b\ne0$ sobre los cuerpos de este curso.

**Conclusión y explicación.** Las diferencias son homogéneas; las sumas no conservan un término independiente no nulo. 中文：这解释了为什么非齐次解集是一个平移，而不是过原点的空间。

## G-E10 — Ecuaciones y número de soluciones

**Hipótesis.** Sistema compatible sobre $\mathbb R$ con $m<n$.

**Tesis.** No hay solución única; construir el caso contrario de conteo $m>n$.

**Estrategia — Español.** Usar el límite del número de pivotes y luego añadir una ecuación redundante a un sistema determinado.

**策略 — 中文。** 方程数只给主元数上界；它不提供所有实际约束之间的关系。

**Demostración.** $r\le m<n$, así que $n-r\ge1$.Por la parametrización hay al menos una coordenada libre que toma infinitos valores reales, produciendo soluciones distintas. Para $m>n$, considérese $x=1$, $y=2$, $x+y=3$: tres ecuaciones y dos incógnitas, con única solución $(1,2)$.La tercera ecuación es redundante, no contradictoria.

**Conclusión y explicación.** Un sistema compatible con menos ecuaciones que incógnitas es indeterminado; tener más ecuaciones no obliga a incompatibilidad. 中文：不相容的判定依赖右端与系数关系，不能由行数与列数单独决定。

## G-E11 — Relaciones y espacios concretos

**Estrategia — Español.** Escribir las columnas antes y después, no solo contar pivotes.

**策略 — 中文。** 保留线性关系与保留几何位置是不同陈述，需要分别比较。

**Solución.** Antes del intercambio, las dos columnas de $A$ son $(1,0)^{\mathsf T}$ y generan $\{(t,0):t\in\mathbb R\}$.Después son ambas $(0,1)^{\mathsf T}$ y generan $\{(0,t):t\in\mathbb R\}$.Los subespacios son distintos. Sin embargo, una combinación de las dos columnas es cero si y solo si sus coeficientes suman cero en ambos casos. Se conserva toda relación y el rango es $1$ en ambos.

Intercambiar las columnas de $(1\ 2)$ sin renombrar $x,y$ cambia $x+2y=1$ por $2x+y=1$.El vector $(1,0)$ satisface la primera y no la segunda, de modo que no son sistemas equivalentes en las mismas incógnitas. En cambio, intercambiar filas solo permuta ecuaciones que siguen debiendo cumplirse todas.

**解释与易错点。** 列变换可以用于某些算法，但要额外追踪变量变换；普通 Gauss 的“同解”不能无条件移用过去。

## G-E12 — Cuerpo finito

**Estrategia — Español.** Enumerar los posibles valores de una variable libre en $\mathbb F_2$.

**策略 — 中文。** 有一个自由参数不必意味着无限多个取值，关键在参数的标量域。

**Solución.** En $\mathbb F_2$, si $y=0$, $x=1$; si $y=1$, $x=0$ porque $1+1=0$ módulo $2$.Las únicas soluciones son $(1,0)$ y $(0,1)$.Ambos rangos son $1$ y hay un parámetro con dos valores: $2^{2-1}=2$ soluciones. Sobre $\mathbb R$ el mismo sistema tiene $(1-t,t)$ para cualquier $t\in\mathbb R$, con los mismos rangos y un parámetro, pero infinitas soluciones.

**Conclusión y explicación.** La clasificación por compatibilidad y parámetros no cambia; la infinitud usa que el cuerpo sea infinito. 中文：这道拓展题核查的是定理条件，不能据它推定教授会考有限域。

完成后阅读 [复习与自测](07_Repaso_Examen.md)，返回 [独立练习](05_Ejercicios.md)。
