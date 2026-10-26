---
title: Pruebas de LU, error y regresión / LU、误差与回归完整证明
subject: Álgebra Lineal
tema: Tema 0 · Guía 1.3
type: proof
language: es-zh
status: complete
tags:
- algebra_lineal
- lu
- regresion
- suplemento
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
provenance: suplemento_didactico_basado_en_temario
updated: 2026-10-26
---

# Pruebas de LU, error y regresión — 完整证明

**Procedencia:** pruebas propias para el alcance de AL-GD-001, p. 5, 1.3. Se usan [Gauss](../02_Sistemas_Gauss/03_Demostraciones.md) y aritmética real. No se atribuyen estas pruebas a una página de apuntes inexistente.

## P1. Sustitución triangular y coste de repetición

**Hipótesis.** $L$ inferior y $U$ superior con diagonales no nulas.

**Tesis.** Las sustituciones dan soluciones únicas; con $PA=LU$ resuelven $Ax=b$.

**Estrategia — Español.** Resolver en el único orden que usa valores ya conocidos y después componer las ecuaciones.

**策略 — 中文。** 三角结构给出每一步唯一可解性，不需要重新求逆矩阵。

**Demostración.** En $Ly=c$, la primera ecuación es $l_{11}y_1=c_1$ y fija $y_1$ porque $l_{11}\ne0$.Si ya están determinados $y_1,\ldots,y_{i-1}$, la ecuación $i$ fija de manera única $y_i$ mediante la fórmula de definición. Inducción sobre $i$ prueba existencia y unicidad. Para $Ux=y$ se aplica el mismo argumento empezando por $i=n$ y descendiendo.

Si $Ly=Pb$ y $Ux=y$, entonces $PAx=LUx=Ly=Pb$.Multiplicar por $P^{-1}$ da $Ax=b$.Cualquier otra solución tendría los mismos valores intermedios y finales por unicidad triangular.

Cada sustitución usa sumas de longitudes $0,1,\ldots,n-1$, cuyo total es $n(n-1)/2$, más $n$ divisiones; su coste es de orden $n^2$.En eliminación densa se actualizan bloques de hasta $(n-k)^2$ entradas en el paso $k$; sumar para $k=1,\ldots,n-1$ da orden $n^3$.

**Explicación — Español.** El conteo compara algoritmos algebraicos densos, sin suponer un tiempo concreto de ejecución.

**中文解释。** 两次三角求解复用既有分解，避免为每个新右端再付三次方级的分解成本。

**Conclusión.** Se prueba T1.

## P2. LU sin intercambios y fórmulas

**Hipótesis.** Gauss sobre $A$ sin intercambios encuentra pivotes $u_{kk}\ne0$.

**Tesis.** Existe $A=LU$ con $L$ inferior unitaria, y se cumplen las fórmulas de Doolittle.

**Estrategia — Español.** Registrar multiplicadores y deshacer las eliminaciones; verificar las entradas del producto triangular.

**策略 — 中文。** 消元相当于减掉某行的倍数，逆操作把这些倍数加回来，记录在 $L$ 的对应位置。

**Demostración.** En el primer paso, si el primer pivote es $a_{11}=\gamma\ne0$, particionamos

$$
A=\begin{pmatrix}\gamma&r\\c&B\end{pmatrix}
=\begin{pmatrix}1&0\\c/\gamma&I\end{pmatrix}
\begin{pmatrix}\gamma&r\\0&B-(c/\gamma)r\end{pmatrix}.
$$

La multiplicación de bloques verifica exactamente la igualdad. Si el bloque restante se elimina sin pivotes nulos, se repite la misma construcción recursivamente; el producto de los factores inferiores unitarios sigue siendo inferior unitario y el factor final es superior. Así se obtiene $A=LU$.

Para comprobar las fórmulas, la entrada $(k,j)$ con $j\ge k$ de $LU$ es $\sum_{s<k}l_{ks}u_{sj}+u_{kj}$, porque $l_{kk}=1$ y los términos posteriores son cero. Igualarla a $a_{kj}$ produce la fórmula de $u_{kj}$.La entrada $(i,k)$ con $i>k$ es $\sum_{s<k}l_{is}u_{sk}+l_{ik}u_{kk}$; despejar $l_{ik}$ es posible por $u_{kk}\ne0$ y da la fórmula correspondiente.

**Explicación — Español.** No se divide por un pivote antes de comprobar su no anulación. La construcción recursiva se refiere exactamente a las mismas submatrices que procesa Gauss.

**中文解释。** 公式不是额外的魔法算法，而是把 $A=LU$ 逐元素展开并按三角顺序解出未知因子。

**Conclusión.** Se establece la existencia bajo las condiciones indicadas.

## P3. Unicidad de LU normalizada y un contraejemplo

**Hipótesis.** $A=L_1U_1=L_2U_2$, con $L_i$ inferiores unitarias y $U_i$ superiores no singulares.

**Tesis.** $L_1=L_2$ y $U_1=U_2$; la no singularidad de $A$ no basta para evitar permutaciones.

**Estrategia — Español.** Comparar un producto inferior unitario con uno superior y usar el solapamiento de ambas estructuras.

**策略 — 中文。** 同时为上三角与单位下三角的矩阵只能是单位矩阵；规范化固定了可在两因子之间移动的对角缩放。

**Demostración.** Resolver columnas de un sistema triangular muestra que su inversa conserva la triangularidad: al resolver una columna de identidad, las entradas forzadas antes o después del correspondiente índice son cero por sustitución. Las inversas de inferiores unitarias son además unitarias. Así

$$
L_2^{-1}L_1=U_2U_1^{-1}
$$

es a la vez inferior unitario y superior, por lo que tiene todos los elementos fuera de la diagonal nulos y diagonal $1$; es $I$.Se deduce $L_1=L_2$ y luego $U_1=U_2$.

Para $A=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, $A^2=I$ y por tanto $A$ es invertible. Si $A=LU$ con $L=\begin{pmatrix}1&0\\\ell&1\end{pmatrix}$ y $U=\begin{pmatrix}u&v\\0&w\end{pmatrix}$, la entrada $(1,1)$ obliga a $u=0$, pero la $(2,1)$ sería $\ell u=0$, contrario a $a_{21}=1$.No existe tal LU sin permutación.

**Explicación — Español.** La unicidad no dice que toda elección de pivote produzca la misma permutación. El contraejemplo separa claramente existencia sin pivoteo de invertibilidad.

**中文解释。** 三角矩阵非零对角保证可逆；若允许改变 $L$ 的对角规范，就不应使用这里的唯一性结论。

**Conclusión.** Se prueba la parte de unicidad de T2 y su límite.

## P4. Existencia de PA=LU para matrices no singulares

**Hipótesis.** $A\in M_{n\times n}(\mathbb R)$ no singular.

**Tesis.** Existe una permutación $P$ y factores $L,U$ del tipo indicado con $PA=LU$.

**Estrategia — Español.** Inducción por bloques, eligiendo un pivote no nulo y aplicando la hipótesis al complemento restante.

**策略 — 中文。** 证明剩余块仍可逆，才能合理地继续归纳；不能只说“不断做下去”。

**Demostración.** Para $n=1$, $A=(a)$ con $a\ne0$ y bastan $P=L=(1)$, $U=(a)$.Para $n>1$, la primera columna contiene un no nulo, pues una columna nula daría un vector no cero en el núcleo. Elija una permutación $P_1$ que lo coloque arriba y escriba

$$
P_1A=\begin{pmatrix}\gamma&r\\c&B\end{pmatrix},\quad\gamma\ne0,\quad S=B-(c/\gamma)r.
$$

El bloque $S$ es no singular: si $Sv=0$ con $v\ne0$, entonces el vector $(-rv/\gamma,v)$ no es cero y su producto por $P_1A$ es cero, contradiciendo la no singularidad de $A$.Por inducción hay $Q S=L_2U_2$ con $Q$ de permutación. Definimos

$$
P=\begin{pmatrix}1&0\\0&Q\end{pmatrix}P_1,\quad
L=\begin{pmatrix}1&0\\Qc/\gamma&L_2\end{pmatrix},\quad
U=\begin{pmatrix}\gamma&r\\0&U_2\end{pmatrix}.
$$

La multiplicación da

$$
LU=\begin{pmatrix}\gamma&r\\Qc&(Qc/\gamma)r+L_2U_2\end{pmatrix}
=\begin{pmatrix}\gamma&r\\Qc&QB\end{pmatrix}=PA.
$$

Las estructuras de $L,U$ y sus diagonales no nulas se preservan. Elegir en cada paso el candidato de máximo valor absoluto es una elección no nula permitida y corresponde al pivoteo parcial.

**Explicación — Español.** El factor $Qc/\gamma$ muestra por qué una permutación posterior reordena también multiplicadores de columnas de $L$ ya calculadas.

**中文解释。** 行交换不仅影响当前上三角化矩阵，也改变已记录乘子与原行的对应关系。块证明明确给出这种调整的来源。

**Conclusión.** Se completa T2. No se ha demostrado una cota universal de error flotante para todo problema.

## P5. Cota de error por residuo

**Hipótesis.** $A$ no singular, $Ax=b$, $r=b-A\hat x$.

**Tesis.** T3.

**Estrategia — Español.** Escribir el error como un sistema con término independiente residual y demostrar la desigualdad de norma necesaria por filas.

**策略 — 中文。** 从精确恒等式出发，再取范数；相对界额外检查分母非零。

**Demostración.** $A(x-\hat x)=r$, luego $e=A^{-1}r$.Para cualquier matriz $C$ y vector $v$,

$$
|(Cv)_i|\le\sum_j|c_{ij}||v_j|
\le\left(\sum_j|c_{ij}|\right)\|v\|_\infty.
$$

Tomar el máximo da $\|Cv\|_\infty\le\|C\|_\infty\|v\|_\infty$.Aplicado a $A^{-1}r$ produce la cota absoluta. Si $b\ne0$, $x\ne0$ y $\|b\|_\infty=\|Ax\|_\infty\le\|A\|_\infty\|x\|_\infty$; de ahí $1/\|x\|_\infty\le\|A\|_\infty/\|b\|_\infty$.Multiplicando la cota absoluta por esta desigualdad resulta la cota relativa.

**Explicación — Español.** La desigualdad de norma es una consecuencia de sumas de valores absolutos, no una suposición de que todo residuo pequeño garantice exactitud.

**中文解释。** 右侧条件数可能很大，所以残差小与误差大并不矛盾。$b=0$ 时只能使用这里的绝对界，不能除以零范数。

**Conclusión.** Se prueba T3 con todas sus condiciones.

## P6. Ecuaciones normales y mínimo global

**Hipótesis.** $X$ y $y$ reales, $r=y-X\theta$.

**Tesis.** $\theta$ minimiza la suma de cuadrados si y solo si $X^{\mathsf T}r=0$.

**Estrategia — Español.** Expandir la diferencia de errores al desplazar parámetros, y elegir un desplazamiento que reduzca el error si la condición falla.

**策略 — 中文。** 不仅证明正规方程必要，还要证明充分；用平方展开直接得到全局极小，而非只找驻点。

**Demostración.** Para cualquier incremento $h$,

$$
\|y-X(\theta+h)\|_2^2
=\|r\|_2^2-2h^{\mathsf T}X^{\mathsf T}r+\|Xh\|_2^2.
$$

Si $X^{\mathsf T}r=0$, el incremento de error es $\|Xh\|_2^2\ge0$ para todo $h$, lo que prueba suficiencia y mínimo global. Recíprocamente, si $w=X^{\mathsf T}r\ne0$, tomemos $h=tw$ con $t>0$.El incremento es $-2t\|w\|_2^2+t^2\|Xw\|_2^2$.Si $Xw=0$, es negativo para todo $t>0$.Si $Xw\ne0$, es negativo para $0<t<2\|w\|_2^2/\|Xw\|_2^2$.En ambos casos contradice la minimalidad. Luego necesariamente $w=0$.

Para la matriz de regresión con columnas $1,t_i$, las dos componentes de $X^{\mathsf T}r=0$ son $\sum r_i=0$ y $\sum t_ir_i=0$.

**Explicación — Español.** La prueba no usa derivadas ni garantiza por sí sola unicidad; esta depende de las columnas de diseño y se trata a continuación.

**中文解释。** 即使某些参数给同样的预测，误差也可能有多个相同的最优参数。极小存在、最优条件与唯一性要分开处理。

**Conclusión.** Se prueba T4.

## P7. Fórmula centrada y degeneración

**Hipótesis.** $N\ge1$ datos $(t_i,y_i)$, con medias y sumas centradas definidas.

**Tesis.** T5, incluidos existencia, unicidad y caso degenerado.

**Estrategia — Español.** Centrar los datos para eliminar términos cruzados y completar cuadrados.

**策略 — 中文。** 先把截距与斜率的耦合分离，再完成平方，直接展示最小值及其全部取得条件。

**Demostración.** Sean $u_i=t_i-\bar t$ y $v_i=y_i-\bar y$.Sus sumas son cero. Por tanto

$$
S(\alpha,\beta)=\sum_i(v_i-\beta u_i)^2+N(\alpha+\beta\bar t-\bar y)^2,
$$

porque el término cruzado contiene $\sum_i(v_i-\beta u_i)=0$.Si $S_{tt}=\sum u_i^2>0$, completar cuadrados da

$$
S=\sum_i v_i^2-\frac{S_{ty}^2}{S_{tt}}
+S_{tt}\left(\beta-\frac{S_{ty}}{S_{tt}}\right)^2
+N(\alpha+\beta\bar t-\bar y)^2.
$$

Los dos últimos términos son no negativos y se anulan simultáneamente exactamente cuando $\beta=\beta_*$ y $\alpha=\bar y-\beta_*\bar t$.Existe, pues, un único minimizador.

$S_{tt}=0$ equivale a $u_i=0$ para todo $i$, es decir, todos los $t_i=t_0$.En ese caso el error es $\sum_i(y_i-\bar y)^2+N(\alpha+\beta t_0-\bar y)^2$, y sus minimizadores son exactamente $\alpha+\beta t_0=\bar y$, sin unicidad de ambos parámetros.

Para la independencia de columnas de diseño, si hay dos $t_i\ne t_j$, una relación $c+d t_k=0$ para todo $k$ implica al restar esas dos ecuaciones $d(t_i-t_j)=0$, por lo que $d=0$ y $c=0$.Si todos son $t_0$, la relación con coeficientes $(-t_0,1)$ es no trivial. Queda probada la equivalencia con independencia.

**Explicación — Español.** Los cuadrados identifican el conjunto completo de minimizadores y no solo candidatos. La fórmula exige variación en los valores de entrada.

**中文解释。** 横坐标全相同时，数据只观察到同一位置，无法分辨许多具有相同位置预测的不同斜率。这是数据本身的信息缺失，不是算法失效。

**Conclusión.** Se prueba T5. Continúe con [ejemplos](04_Ejemplos.md).
