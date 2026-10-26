---
title: LU, residuos y mínimos cuadrados / LU、残差与最小二乘定义
subject: Álgebra Lineal
tema: Tema 0 · Guía 1.3
type: definition
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

# LU, residuos y mínimos cuadrados — 定义与算法

**Procedencia:** desarrollo propio para el apartado 1.3 de AL-GD-001 p. 5. No es transcripción de una explicación de aula recibida.

## 1. Sistemas triangulares — 三角方程组

Una matriz $L$ es triangular inferior（下三角）si $l_{ij}=0$ cuando $j>i$. Una matriz $U$ es triangular superior（上三角）si $u_{ij}=0$ cuando $i>j$. Si la diagonal de $L$ es toda $1$, se llama triangular inferior unitaria（单位下三角）.

Con diagonales no nulas, $Ly=c$ se resuelve por sustitución progresiva（前代）:

$$
y_i=\frac{c_i-\sum_{j<i}l_{ij}y_j}{l_{ii}},\quad i=1,\ldots,n.
$$

$Ux=y$ se resuelve por sustitución regresiva（回代）:

$$
x_i=\frac{y_i-\sum_{j>i}u_{ij}x_j}{u_{ii}},\quad i=n,\ldots,1.
$$

**Español.** La dirección importa: en cada paso solo se usan cantidades ya calculadas. Las divisiones exigen diagonal no nula.

**中文。** 三角结构使问题按一个方向依次解开，不是凭公式“同时算出”所有未知数。

## 2. Factorización LU y PA=LU — 分解与约定

Una factorización LU（LU 分解）es $A=LU$，con $L$ inferior unitaria y $U$ superior. Cuando se necesitan intercambios de filas se escribe

$$
PA=LU,
$$

donde $P$ es una matriz de permutación（置换矩阵）que actúa sobre filas. Esta es la convención de todo el módulo. Resolver $Ax=b$ equivale entonces a

$$
Ly=Pb,\qquad Ux=y.
$$

**Español.** LU sin intercambios no existe para toda matriz invertible. La diagonal unitaria de $L$ fija una normalización necesaria para la unicidad. En la versión con permutación, las soluciones usan $Pb$, no $b$ sin transformar.

**中文。** 写成 $PA=LU$ 后，右端也要乘 $P$；与采用其他书籍的 $A=PLU$ 记号不能混用。行交换到后面的步骤时，还要调整 $L$ 中已经记录的乘子。

## 3. Algoritmo de Doolittle y pivoteo — Doolittle 与选主元

Si los pivotes sucesivos son no nulos, una versión sin intercambios calcula

$$
u_{kj}=a_{kj}-\sum_{s<k}l_{ks}u_{sj}\quad(j\ge k),
$$

$$
l_{ik}=\frac{a_{ik}-\sum_{s<k}l_{is}u_{sk}}{u_{kk}}\quad(i>k),\qquad l_{kk}=1.
$$

Las otras entradas se fijan por triangularidad. El pivoteo parcial（部分选主元）elige en la columna activa un elemento de valor absoluto máximo entre las filas activas y lo intercambia a la fila pivote. Para una matriz no singular existe una elección no nula en cada paso.

**Español.** Si se intercambian las filas $k,p$ en un paso posterior, también se intercambian en $L$ sus entradas de las columnas $1,\ldots,k-1$ ya construidas. No se intercambia una matriz $L$ completa como si fuera la matriz de coeficientes actual.

**中文。** 之前列中的乘子对应已经重排的原行；不跟随交换，就会得到乘不回 $PA$ 的错误分解。后面的三阶例题会展示这一点。

## 4. Residuo, error y condición — 残差、误差与条件数

Sea $A$ no singular, $Ax=b$ la solución exacta y $\hat x$ una aproximación. Se define el residuo（残差）$r=b-A\hat x$ y el error（解误差）$e=x-\hat x$。

Para $v\in\mathbb R^n$, $\|v\|_\infty=\max_i|v_i|$。Para una matriz, $\|A\|_\infty=\max_i\sum_j|a_{ij}|$。El número de condición（条件数）es

$$
\kappa_\infty(A)=\|A\|_\infty\|A^{-1}\|_\infty.
$$

**Español.** Se puede calcular un residuo usando datos y aproximación, pero el error necesita conocer la solución exacta o una cota. El número de condición mide cuánto puede amplificarse una perturbación; no mide por sí solo los errores cometidos por un algoritmo concreto.

**中文。** 条件数大意味着问题可能敏感，不表示每个输入都必定达到最坏误差。下面的相对误差界要求 $b\ne0$，避免除以零范数。

Para ilustrar redondeo se usará un modelo declarado de **tres cifras significativas**, redondeando cada producto, resta y división indicada. No se identifica ese modelo pedagógico con toda la aritmética real de una computadora.

## 5. Regresión lineal — 直线回归

Dados $N\ge1$ pares reales $(t_i,y_i)$, se busca una recta $\alpha+\beta t$ que minimice

$$
S(\alpha,\beta)=\sum_{i=1}^{N}\bigl(y_i-\alpha-\beta t_i\bigr)^2.
$$

La matriz de diseño（设计矩阵）y el vector de parámetros son

$$
X=\begin{pmatrix}1&t_1\\\vdots&\vdots\\1&t_N\end{pmatrix},\qquad
\theta=\begin{pmatrix}\alpha\\\beta\end{pmatrix},\qquad S=\|y-X\theta\|_2^2,
$$

con $\|v\|_2^2=\sum_i v_i^2$. Se definen

$$
\bar t=\frac1N\sum_i t_i,\quad\bar y=\frac1N\sum_i y_i,\quad
S_{tt}=\sum_i(t_i-\bar t)^2,\quad
S_{ty}=\sum_i(t_i-\bar t)(y_i-\bar y).
$$

Las ecuaciones normales（正规方程）son $X^{\mathsf T}X\theta=X^{\mathsf T}y$。La transpuesta $X^{\mathsf T}$ intercambia filas y columnas: su entrada $(j,i)$ es $X_{ij}$。

**Español.** Se minimizan desviaciones verticales al cuadrado, no distancias perpendiculares a la recta. Los datos no tienen por qué satisfacer un sistema exacto. La variable $t$ se escribe así para no confundirla con el vector solución de los sistemas anteriores.

**中文。** 最小二乘不是“强行解一个无解系统”；先定义明确的误差目标，再证明所选直线最优。若所有横坐标相同，斜率不能由这些数据唯一确定，必须单独讨论。

继续 [性质](02_Teoremas.md) 与 [证明](03_Demostraciones.md)。
