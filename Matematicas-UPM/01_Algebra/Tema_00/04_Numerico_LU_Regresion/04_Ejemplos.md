---
title: Ejemplos de LU y regresión / LU 与回归完整例题
subject: Álgebra Lineal
tema: Tema 0 · Guía 1.3
type: example
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

# Ejemplos de LU y regresión — 完整例题

**Procedencia:** N-01–N-06 son elaboración propia para AL-GD-001 1.3. Ningún enunciado se atribuye a una hoja del profesor o a un examen real. Todos los cálculos exactos y el modelo decimal indicado se comprueban por separado.

## N-01. LU y dos sustituciones — 分解与两次三角求解

**Enunciado.** Factorizar y resolver $Ax=b$ con

$$
A=\begin{pmatrix}2&1&1\\4&-6&0\\-2&7&2\end{pmatrix},\qquad b=\begin{pmatrix}7\\-8\\18\end{pmatrix}.
$$

**Análisis — Español.** En la primera columna los multiplicadores son $2$ y $-1$.En la segunda, tras eliminar, el multiplicador será $-1$.

**分析 — 中文。** 把每次“减去主元行几倍”的乘子记录进 $L$，而不是记录减法后的零。

**Resolución.** Aplicar $F_2\leftarrow F_2-2F_1$ y $F_3\leftarrow F_3+F_1$ produce filas inferiores $(0,-8,-2)$ y $(0,8,3)$.Después $F_3\leftarrow F_3+F_2$ da $(0,0,1)$.Por tanto

$$
L=\begin{pmatrix}1&0&0\\2&1&0\\-1&-1&1\end{pmatrix},\qquad
U=\begin{pmatrix}2&1&1\\0&-8&-2\\0&0&1\end{pmatrix}.
$$

El producto tiene filas $(2,1,1)$, $2(2,1,1)+(0,-8,-2)=(4,-6,0)$ y $-(2,1,1)-(0,-8,-2)+(0,0,1)=(-2,7,2)$, confirmando $LU=A$.

Resolver $Ly=b$ da $y_1=7$, $y_2=-8-2\cdot7=-22$, $y_3=18+y_1+y_2=3$.Resolver $Ux=y$ da $x_3=3$, $x_2=(-22+2\cdot3)/(-8)=2$ y $x_1=(7-2-3)/2=1$.

**Conclusión.** $x=(1,2,3)^{\mathsf T}$ y la sustitución en $A$ devuelve $(7,-8,18)^{\mathsf T}$.

**Explicación — Español.** El multiplicador de la segunda etapa es $8/(-8)=-1$, aunque la operación se escriba como suma de filas.

**中文解释。** $L$ 的位置存的是消元乘子，符号由原系数除以主元得到；看到“加一行”不能把乘子误记成 $+1$。

## N-02. Dos intercambios y ajuste de L — 选主元与历史乘子

**Enunciado.** Obtener $PA=LU$ mediante pivoteo parcial para

$$
A=\begin{pmatrix}0&2&1\\1&1&0\\2&0&1\end{pmatrix}.
$$

**Análisis — Español.** El mayor valor absoluto de la primera columna es $2$, por lo que se intercambian filas 1 y 3. En la segunda etapa habrá otro intercambio, que también debe reflejarse en la primera columna de multiplicadores de $L$.

**分析 — 中文。** 这个例题专门展示“后续行交换也要调整过去乘子”的必要性。

**Resolución.** Tras el primer intercambio las filas son $(2,0,1)$, $(1,1,0)$, $(0,2,1)$.Los multiplicadores son $1/2$ y $0$, y las filas activas quedan $(0,1,-1/2)$ y $(0,2,1)$.Para la segunda columna se intercambian esas dos filas, por ser $2$ mayor que $1$.En $L$ se intercambian entonces los multiplicadores previos $1/2$ y $0$.El último multiplicador es $1/2$, y la última fila se vuelve $(0,0,-1)$.

Los factores son

$$
P=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix},\quad
L=\begin{pmatrix}1&0&0\\0&1&0\\1/2&1/2&1\end{pmatrix},\quad
U=\begin{pmatrix}2&0&1\\0&2&1\\0&0&-1\end{pmatrix}.
$$

La primera fila de $LU$ es $(2,0,1)$, la segunda $(0,2,1)$ y la tercera $(1,1,1/2+1/2-1)=(1,1,0)$.Son las filas 3, 1, 2 de $A$, exactamente $PA$.

**Conclusión.** La factorización queda verificada entrada a entrada.

**Explicación — Español.** Si se conservara $l_{21}=1/2$ sin intercambiarlo, el producto no reproduciría las filas permutadas correctas.

**中文解释。** $P$ 记录最终原行顺序；当前活跃矩阵的交换与 $L$ 历史列的交换各自承担不同作用。

## N-03. Pequeño pivote y redondeo — 小主元与舍入

**Enunciado.** Con $\varepsilon=10^{-4}$, resolver aproximadamente

$$
\begin{pmatrix}\varepsilon&1\\1&1\end{pmatrix}x=\begin{pmatrix}1\\2\end{pmatrix}
$$

con tres cifras significativas, redondeando cada operación indicada, con y sin intercambio de filas.

**Análisis — Español.** La matriz es invertible y su solución exacta es $(1/(1-\varepsilon),(1-2\varepsilon)/(1-\varepsilon))$.El riesgo sin intercambio es el multiplicador $10^4$.

**分析 — 中文。** 这是一个明确指定的三位有效数字模型，不冒充所有真实浮点硬件行为。目的是解释中间舍入如何消掉有用信息。

**Resolución sin intercambio.** $m=1/\varepsilon=10000$.El nuevo coeficiente $1-10000=-9999$ se redondea a $-10000$; el nuevo término $2-10000=-9998$ también a $-10000$.Así $\hat x_2=1$ y la primera ecuación da $\hat x_1=(1-1)/\varepsilon=0$.El resultado aproximado es $(0,1)$.

**Resolución con intercambio.** Se empieza por $x_1+x_2=2$.El multiplicador es $\varepsilon$; $1-\varepsilon=0.9999$ se redondea a $1.00$ y $1-2\varepsilon=0.9998$ también a $1.00$.Entonces $\hat x_2=1$ y $\hat x_1=2-1=1$.

**Comprobación con los datos exactos.** El residuo para $(0,1)$ es $(0,1)$; para $(1,1)$ es $(-\varepsilon,0)$.El segundo procedimiento da una aproximación mucho mejor en este modelo.

**Explicación — Español.** El intercambio evitó un multiplicador enorme. No se concluye que todo problema esté bien condicionado ni que pivoteo parcial elimine cualquier error de redondeo.

**中文解释。** 精确代数里两种路线同解；有限精度里中间数值大小不同，可能产生明显不同的误差。

## N-04. Residuo pequeño y error grande — 小残差不保证小误差

**Enunciado.** Sean $\delta=10^{-8}$,

$$
A=\begin{pmatrix}1&1\\1&1+\delta\end{pmatrix},\quad
b=\begin{pmatrix}2\\2+\delta\end{pmatrix},\quad
\hat x=\begin{pmatrix}2\\0\end{pmatrix}.
$$

Comparar residuo, error y condición.

**Análisis — Español.** La solución exacta es $x=(1,1)^{\mathsf T}$.La segunda ecuación es casi una repetición de la primera, por lo que el problema es sensible.

**分析 — 中文。** 两条几乎重合的约束可能容许误差很大的向量也看起来“几乎满足”。

**Resolución.** $r=b-A\hat x=(0,\delta)^{\mathsf T}$, por lo que $\|r\|_\infty=\delta$.Pero $e=x-\hat x=(-1,1)^{\mathsf T}$ y $\|e\|_\infty=1$; como $\|x\|_\infty=1$, el error relativo es $1$.

Se verifica por multiplicación que

$$
A^{-1}=\frac1\delta\begin{pmatrix}1+\delta&-1\\-1&1\end{pmatrix}.
$$

Así $\|A\|_\infty=2+\delta$, $\|A^{-1}\|_\infty=(2+\delta)/\delta$ y $\kappa_\infty(A)=(2+\delta)^2/\delta$, que es grande.

**Conclusión.** El residuo relativo es $\delta/(2+\delta)$, pequeño, pero la cota de error incluye un factor de condición grande y no promete precisión alta.

**Explicación — Español.** Aquí el problema es la sensibilidad de la matriz, distinta del mero pequeño pivote evitable del ejemplo anterior.

**中文解释。** 残差、条件数、实际解误差应结合分析；只展示很小的残差数值不能证明计算可靠。

## N-05. Recta de regresión única — 唯一最小二乘直线

**Enunciado.** Ajustar una recta a $(0,1)$, $(1,2)$, $(2,2)$ mediante mínimos cuadrados verticales.

**Análisis — Español.** No existe una recta que pase por los tres puntos: las pendientes entre puntos consecutivos son $1$ y $0$.Se minimiza la suma de cuadrados, no se fuerza un sistema incompatible.

**分析 — 中文。** 先明确近似目标；下面同时用中心化公式与正规方程检查结果。

**Resolución.** $\bar t=1$, $\bar y=5/3$, $S_{tt}=(-1)^2+0^2+1^2=2$, $S_{ty}=(-1)(-2/3)+0(1/3)+1(1/3)=1$.Luego

$$
\beta_*=\frac12,\qquad\alpha_*=\frac53-\frac12=\frac76,
\qquad\hat y(t)=\frac76+\frac12t.
$$

Las predicciones son $7/6$, $5/3$, $13/6$; los residuos son $(-1/6,1/3,-1/6)$ y

$$
S_{\min}=\frac1{36}+\frac19+\frac1{36}=\frac16.
$$

La suma de residuos es cero y su suma ponderada por $t_i$ también: $0(-1/6)+1(1/3)+2(-1/6)=0$.Las ecuaciones normales son $3\alpha+3\beta=5$, $3\alpha+5\beta=6$, satisfechas por los parámetros obtenidos.

**Conclusión.** La recta es única porque $S_{tt}>0$.

**Explicación — Español.** La prueba por cuadrados del módulo garantiza que no hay otra recta con menor error, no solo que se cumplen dos ecuaciones.

**中文解释。** 残差不必逐项为零；它们在两个设计列方向的合成项为零，才是最优性的条件。

## N-06. Todos los tiempos iguales — 退化数据

**Enunciado.** Ajustar por el mismo criterio los datos $(2,1)$, $(2,3)$, $(2,5)$.

**Análisis — Español.** No existe variación en las entradas; los datos solo informan sobre la predicción en $t=2$.

**分析 — 中文。** 分母 $S_{tt}=0$ 不意味着没有最佳预测，只意味着不能唯一恢复截距和斜率。

**Resolución.** $\bar t=2$, $\bar y=3$, $S_{tt}=0$.Todos los minimizadores satisfacen $\alpha+2\beta=3$, es decir $\alpha=3-2\beta$ con $\beta$ arbitrario. En todos ellos las predicciones son $(3,3,3)$, los residuos $(-2,0,2)$ y el error mínimo $4+0+4=8$.

**Conclusión.** Hay infinitas rectas minimizadoras, pero una sola predicción óptima en el único tiempo observado.

**Explicación — Español.** No se divide por cero ni se declara fallo del método; se identifica toda la familia óptima.

**中文解释。** 对同一个横坐标做再多观测也不能提供不同横坐标之间的变化信息，这是真实的数据识别问题。

继续 [独立练习](05_Ejercicios.md)。
