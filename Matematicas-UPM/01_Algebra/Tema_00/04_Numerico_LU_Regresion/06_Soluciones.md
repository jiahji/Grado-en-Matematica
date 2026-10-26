---
title: Soluciones de LU y regresión / LU 与回归完整解答
subject: Álgebra Lineal
tema: Tema 0 · Guía 1.3
type: exercises
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

# Soluciones de LU y regresión — 完整解答

**Procedencia:** soluciones propias de [N-E01–N-E12](05_Ejercicios.md).Las pruebas utilizadas están en [el archivo de demostraciones](03_Demostraciones.md).

## N-E01 — Factorización y sistema

**Estrategia — Español.** Guardar el multiplicador $4/2=2$ y después resolver triangularmente.

**策略 — 中文。** 把消元与右端求解分开，检查因子乘积是否恢复原矩阵。

**Solución.** $L=\begin{pmatrix}1&0\\2&1\end{pmatrix}$, $U=\begin{pmatrix}2&1\\0&1\end{pmatrix}$.Su producto es $\begin{pmatrix}2&1\\4&3\end{pmatrix}$.$Ly=(1,0)^{\mathsf T}$ da $y=(1,-2)^{\mathsf T}$.$Ux=y$ da $x_2=-2$ y $x_1=(1+2)/2=3/2$.La sustitución da $A(3/2,-2)^{\mathsf T}=(1,0)^{\mathsf T}$.

**解释。** $L$ 记录的乘子为正 2，虽然消元写的是“减去两倍第一行”。

## N-E02 — Permutación necesaria

**Hipótesis.** La matriz del enunciado y normalización unitaria de $L$.

**Tesis.** Invertibilidad, imposibilidad de LU sin intercambio y una PLU válida.

**Estrategia — Español.** Comparar entradas del producto supuesto y después intercambiar filas.

**策略 — 中文。** 不需要用行列式；直接乘法足以证明和构造。

**Demostración.** $A^2=I$, por lo que $A^{-1}=A$.Si $L=\begin{pmatrix}1&0\\\ell&1\end{pmatrix}$, $U=\begin{pmatrix}u&v\\0&w\end{pmatrix}$ y $LU=A$, entonces $u=0$ y $\ell u=1$, imposible. Tomando $P=A$, $PA=I$, por lo que sirven $L=I$ y $U=I$.

**Conclusión y explicación.** El intercambio resuelve la obstrucción sin cambiar la invertibilidad. 中文：可逆不保证第一位置可以直接当作非零主元。

## N-E03 — Pivoteo parcial

**Estrategia — Español.** El primer pivote debe ser $3$, intercambiando las filas.

**策略 — 中文。** 置换右端后再前代；忽略 $P$ 会解错另一个系统。

**Solución.**

$$
P=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
L=\begin{pmatrix}1&0\\1/3&1\end{pmatrix},\quad
U=\begin{pmatrix}3&4\\0&2/3\end{pmatrix}.
$$

$LU$ tiene filas $(3,4)$ y $(1,2)$, por tanto es $PA$.$Pb=(7,3)^{\mathsf T}$, de modo que $Ly=Pb$ da $y_1=7$, $y_2=3-7/3=2/3$.Luego $x_2=1$ y $x_1=(7-4)/3=1$.$A(1,1)^{\mathsf T}=(3,7)^{\mathsf T}$ verifica el resultado.

**解释。** 新右端第二分量是原右端第一分量，必须与原行顺序一起交换。

## N-E04 — Modelo redondeado

**Estrategia — Español.** Redondear cada operación indicada a tres cifras, no solo la solución final.

**策略 — 中文。** 数值差别来自中间过程，不是最后答案显示几位小数。

**Solución.** Sin intercambio, el multiplicador es $10000$.Los valores $-9999$ y $-9998$ se redondean ambos a $-10000$; se obtiene $\hat x=(0,1)$.Su residuo exacto es $b-A\hat x=(0,1)$.Con intercambio, el multiplicador es $0.0001$; $0.9999$ y $0.9998$ se redondean ambos a $1.00$; se obtiene $\hat x=(1,1)$ y residuo exacto $(-0.0001,0)$.

**解释。** 后者的原数据残差小得多；这个例子说明选主元的作用，但不构成针对所有矩阵的误差保证。

## N-E05 — Residuo y error

**Hipótesis.** $Ax=b$ y $A$ invertible.

**Tesis.** La identidad y la equivalencia para residuo nulo.

**Estrategia — Español.** Restar $A\hat x$ a la ecuación exacta y multiplicar por la inversa.

**策略 — 中文。** 先得到精确关系，再判断“小”如何受逆矩阵放大。

**Demostración.** $A(x-\hat x)=b-A\hat x=r$, luego $x-\hat x=A^{-1}r$.Si $r=0$, el error es cero y $\hat x=x$.Si $\hat x=x$, su residuo es $b-Ax=0$.Para $r$ pequeño, la cota $\|x-\hat x\|_\infty\le\|A^{-1}\|_\infty\|r\|_\infty$ contiene un posible factor de amplificación grande.

**Conclusión y explicación.** Residuo nulo en aritmética exacta certifica la solución; residuo pequeño necesita considerar la condición. 中文：真实计算还要区分计算得到的舍入残差与精确残差。

## N-E06 — Regresión

**Estrategia — Español.** Centrar los datos y verificar con residuos y ecuaciones normales.

**策略 — 中文。** 先证明处于唯一情形，再计算斜率和截距。

**Solución.** $\bar t=2$, $\bar y=8/3$, $S_{tt}=2$, $S_{ty}=(-1)(-2/3)+0(-2/3)+1(4/3)=2$.Por tanto $\beta=1$ y $\alpha=2/3$.Las predicciones son $5/3$, $8/3$, $11/3$; los residuos $1/3,-2/3,1/3$ y $S=1/9+4/9+1/9=2/3$.

Las ecuaciones normales son $3\alpha+6\beta=8$ y $6\alpha+14\beta=18$.Con $(2/3,1)$ dan $2+6=8$ y $4+14=18$.$S_{tt}>0$ garantiza mínimo global único por la prueba del módulo.

**解释。** 残差正负可抵消，但目标是平方和，不是简单残差和；最优性要依赖已证定理。

## N-E07 — Degeneración

**Estrategia — Español.** Reemplazar la predicción común por una sola cantidad $c=\alpha+\beta$.

**策略 — 中文。** 全部数据只观察 $t=1$，先求该处的最佳预测，再描述全部参数。

**Solución.** $\bar y=2$ y

$$
S=(0-c)^2+(2-c)^2+(4-c)^2=8+3(c-2)^2.
$$

El mínimo es $8$, alcanzado exactamente si $c=2$.Así todos los minimizadores son $\alpha=2-\beta$, con $\beta\in\mathbb R$ arbitrario. La predicción en $t=1$ queda fijada en $2$, pero no la pendiente.

**解释。** 这不是“没有回归解”；是最优参数不唯一。

## N-E08 — Mínimo y ecuaciones normales

**Hipótesis.** Datos y matriz $X$ reales.

**Tesis.** Necesidad y suficiencia del criterio.

**Estrategia — Español.** Expandir el error al incrementar los parámetros y escoger una dirección de descenso cuando falle la condición.

**策略 — 中文。** 两个方向都必须写，不能把正规方程仅作为一套需要背诵的公式。

**Demostración.** Sea $r=y-X\theta$.Para cualquier $h$, el cambio del cuadrado de error es $-2h^{\mathsf T}X^{\mathsf T}r+\|Xh\|_2^2$.Si $X^{\mathsf T}r=0$, ese cambio es no negativo para todo $h$, y $\theta$ minimiza. Si $w=X^{\mathsf T}r\ne0$, tomar $h=tw$ da $-2t\|w\|_2^2+t^2\|Xw\|_2^2$.Para $t>0$ suficientemente pequeño es negativo: si $\|Xw\|=0$, cualquier $t>0$ sirve; si no, basta $t<2\|w\|^2/\|Xw\|^2$.Esto contradice un mínimo, de donde la condición es necesaria.

**Conclusión y explicación.** La equivalencia prueba mínimo global，sin concluir unicidad sin hipótesis extra. 中文：当设计列相关时，不同参数可能具有相同预测与同一最小误差。

## N-E09 — Traslación vertical

**Estrategia — Español.** Comparar datos centrados antes y después de sumar $c$.

**策略 — 中文。** 横坐标未改变，新的纵坐标平均数也增加 $c$，因此中心化纵坐标不变。

**Solución.** $\bar y'=\bar y+c$ y $y_i'-\bar y'=(y_i+c)-(\bar y+c)=y_i-\bar y$.Así $S_{ty}'=S_{ty}$ y $S_{tt}'=S_{tt}>0$; por tanto $\beta'_* =\beta_*$ y $\alpha'_* =\bar y+c-\beta_*\bar t=\alpha_*+c$.Cada residuo nuevo es $(y_i+c)-(\alpha_*+c)-\beta_*t_i=y_i-\alpha_*-\beta_*t_i$, el mismo de antes.

**解释。** 整体竖直平移数据只平移最优直线，不改变斜率与拟合误差。这是对回归公式的结构检查。

## N-E10 — Reutilización

**Estrategia — Español.** Separar el coste común y el coste de cada término independiente.

**策略 — 中文。** 一次分解只支付一次，其余右端复用因子。

**Solución.** La factorización densa requiere orden $n^3$ operaciones. Cada uno de los $k$ términos necesita una permutación de orden $n$ y dos sustituciones de orden $n^2$, sumando orden $kn^2$.El total es orden $n^3+kn^2$.Rehacer Gauss para cada término repite el orden $n^3$, dando orden $kn^3$.Este conteo no supone tiempos idénticos por operación en toda computadora, ni considera estructura dispersa especial.

**解释。** 当右端数量增大时，复用收益明显；这正是把消元独立保存为分解的意义。

## N-E11 — Rango de diseño

**Hipótesis.** $N\ge1$, matriz de diseño con columnas $1$ y $t_i$.

**Tesis.** Independencia equivalente a $S_{tt}>0$ y pivotes de la matriz normal.

**Estrategia — Español.** Comparar dos entradas distintas para la independencia y hacer una eliminación en la matriz de tamaño $2$.

**策略 — 中文。** 不借用尚未系统讲解的行列式，以已学的行消元直接判断。

**Demostración.** $S_{tt}>0$ equivale a que al menos dos valores $t_i$ sean distintos. Si $a+bt_k=0$ para todos los $k$, restar dos índices con tiempos distintos fuerza $b=0$ y después $a=0$; las columnas son independientes. Si todos los tiempos son $t_0$, los coeficientes $(-t_0,1)$ dan una relación no trivial.

Por producto matricial,

$$
X^{\mathsf T}X=\begin{pmatrix}N&\sum_i t_i\\\sum_i t_i&\sum_i t_i^2\end{pmatrix}.
$$

Hacer $F_2\leftarrow F_2-\bar t F_1$ deja segunda fila $(0,\sum_i t_i^2-N\bar t^2)=(0,S_{tt})$, mientras el primer pivote es $N>0$.Así la normal es invertible exactamente cuando $S_{tt}>0$.

**Conclusión y explicación.** Los dos enfoques coinciden. 中文：一条公式同时具有数据变化量与代数秩的解释。

## N-E12 — Condición y cota

**Estrategia — Español.** Usar las diagonales para calcular solución e inversa exactamente.

**策略 — 中文。** 这个例子把残差放大效应写成可精确核对的等式。

**Solución.** $x=(1,1)^{\mathsf T}$, $r=b-A\hat x=(\varepsilon,0)^{\mathsf T}$ y $e=(1,0)^{\mathsf T}$.$\|x\|_\infty=\|b\|_\infty=1$, de modo que el error relativo es $1$ y el residuo relativo $\varepsilon$.$A^{-1}=\operatorname{diag}(1/\varepsilon,1)$, por lo que $\|A\|_\infty=1$, $\|A^{-1}\|_\infty=1/\varepsilon$ y $\kappa_\infty(A)=1/\varepsilon$.La cota queda $1\le(1/\varepsilon)\varepsilon=1$, alcanzándose igualdad.

**解释。** 残差可以任意小，而解的相对误差保持为 1；条件数准确反映了这一放大。

返回 [复习](07_Repaso_Examen.md) 或 [学习入口](00_Introduccion.md)。
