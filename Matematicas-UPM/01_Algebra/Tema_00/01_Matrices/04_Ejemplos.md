---
title: Ejemplos resueltos de matrices / 矩阵完整例题
subject: Álgebra Lineal
tema: Tema 0 · Matrices · Guía 1.1
type: example
language: es-zh
status: complete
tags:
- algebra_lineal
- matrices
- tema_00
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-000/Tema 0(6).pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Ejemplos resueltos — 矩阵完整例题

**Procedencia.** M-01 conserva un ejemplo manuscrito legible de AL-AP-000, página PDF 2. M-02 a M-07 son ejemplos de elaboración propia para desarrollar el apartado oficial 1.1; no son preguntas de exámenes reales. Las anotaciones pequeñas no transcritas del original permanecen en el PDF.

## M-01. Producto por un escalar — 数乘（课堂批注例题）

**Enunciado.** Calcular $2\begin{pmatrix}1&3\\0&2\end{pmatrix}$.

**Análisis — Español.** El factor $2$ es un escalar; no hay sumatorios ni se cambia el tamaño.

**分析 — 中文。** 不需要“行乘列”，只把每个元素都乘以 2，矩阵仍为 $2\times2$。

**Resolución.** Por la definición de producto por un escalar,

$$
2\begin{pmatrix}1&3\\0&2\end{pmatrix}
=\begin{pmatrix}2\cdot1&2\cdot3\\2\cdot0&2\cdot2\end{pmatrix}
=\begin{pmatrix}2&6\\0&4\end{pmatrix}.
$$

**Conclusión y error frecuente — 结论与易错点。** El resultado sigue siendo $2\times2$. 中文：要乘全部元素，不是只乘对角线；本题来自原笔记的批注，展开步骤为教材补充。

## M-02. Combinar suma y escalares — 加法与数乘（基础）

**Enunciado.** Sean $A=\begin{pmatrix}1&-2\\3&0\end{pmatrix}$ y $B=\begin{pmatrix}0&4\\-1&2\end{pmatrix}$. Calcular $2A-3B$.

**Análisis — Español.** Las matrices tienen el mismo tamaño; se calculan los dos productos por escalares y después se resta entrada a entrada.

**分析 — 中文。** 外面的负号作用于 $3B$ 的全部元素，特别要检查 $B$ 中负数所在的位置。

**Resolución.**

$$
2A=\begin{pmatrix}2&-4\\6&0\end{pmatrix},\quad
3B=\begin{pmatrix}0&12\\-3&6\end{pmatrix},\quad
2A-3B=\begin{pmatrix}2&-16\\9&-6\end{pmatrix}.
$$

**Conclusión — 结论。** La entrada $(2,1)$ es $6-(-3)=9$. 中文：括号中的负数被减去，符号必须翻转；这比只检查结果大小更容易发现计算错误。

## M-03. Producto rectangular — 长方矩阵乘法（综合）

**Enunciado.** Sean

$$
A=\begin{pmatrix}1&2&-1\\0&3&4\end{pmatrix},\quad
B=\begin{pmatrix}2&1\\1&0\\-1&2\end{pmatrix}.
$$

Calcular $AB$ y $BA$.

**Análisis — Español.** $AB$ es $2\times2$ y $BA$ es $3\times3$. Ambos existen, pero tienen tipos distintos.

**分析 — 中文。** 两种顺序都能乘，不意味着结果大小相同。先写大小，可以立即避免把某个 $3\times3$ 结果误当成 $AB$。

**Resolución.** Las cuatro entradas de $AB$ son

$$
AB=\begin{pmatrix}
1\cdot2+2\cdot1+(-1)(-1)&1\cdot1+2\cdot0+(-1)2\\
0\cdot2+3\cdot1+4(-1)&0\cdot1+3\cdot0+4\cdot2
\end{pmatrix}
=\begin{pmatrix}5&-1\\-1&8\end{pmatrix}.
$$

Para el otro orden se obtiene

$$
BA=\begin{pmatrix}
2&7&2\\1&2&-1\\-1&4&9
\end{pmatrix}.
$$

Por ejemplo, $(BA)_{12}=2\cdot2+1\cdot3=7$ y $(BA)_{33}=(-1)(-1)+2\cdot4=9$; las demás entradas se calculan con la misma definición fila-columna.

**Conclusión — 结论。** $AB$ y $BA$ pertenecen a conjuntos de matrices de distinto tamaño. 中文：不要把它们相减，也不要只因二者都存在就使用标量交换律。

## M-04. No conmutatividad con tamaños iguales — 同型方阵也不一定交换

**Enunciado.** Comprobar que las matrices

$$
E=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
F=\begin{pmatrix}0&0\\1&0\end{pmatrix}
$$

no conmutan.

**Análisis — Español.** Esta vez los dos productos son $2\times2$ y sí se pueden comparar.

**分析 — 中文。** 要反驳“任意方阵都交换”，只需要一个大小一致、能比较且结果不同的明确反例。

**Resolución.**

$$
EF=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
FE=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
$$

La entrada $(1,1)$ vale $1$ en $EF$ y $0$ en $FE$, por lo que $EF\ne FE$.

**Conclusión y error frecuente — 结论与误区。** La multiplicación matricial no es conmutativa en general. Esto no dice que ninguna pareja conmute: $I_2$ sí conmuta con $E$ y con $F$。

## M-05. Producto nulo sin factores nulos — 非零矩阵的零乘积

**Enunciado.** Para $N=\begin{pmatrix}0&1\\0&0\end{pmatrix}$, calcular $N^2$ y explicar por qué no se puede cancelar un factor matricial solo por ser distinto de cero.

**Análisis — Español.** Hay que comprobar que el factor es no nulo y que el producto sí es nulo; ambas condiciones son necesarias para el contraejemplo.

**分析 — 中文。** 不能只写一个零乘积；必须同时展示两个因子都非零，才真正否定标量规则的直接推广。

**Resolución.** $N_{12}=1$, luego $N\ne0$. En cambio,

$$
N^2=\begin{pmatrix}0\cdot0+1\cdot0&0\cdot1+1\cdot0\\0&0\end{pmatrix}=0.
$$

Tomando $A=N$, $B=N$, $C=0$ se cumple $AB=AC=0$, pero $B\ne C$.

**Conclusión — 结论。** $A\ne0$ no basta para cancelar $A$ en $AB=AC$. 中文：可逆矩阵允许通过乘逆矩阵约去因子，但“非零”远弱于“可逆”；逆矩阵在后续 Gauss 单元系统讨论。

## M-06. Ecuación de conmutación — 交换条件（大学证明训练）

**Enunciado.** Hallar todas las matrices $X=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ que conmutan con $D=\begin{pmatrix}1&0\\0&2\end{pmatrix}$.

**Análisis — Español.** Se escriben $DX$ y $XD$ y se igualan las entradas; no es necesario resolver mediante determinantes.

**分析 — 中文。** 左乘对角矩阵缩放行，右乘缩放列；要两者相同，非对角位置必须受到限制。

**Resolución.**

$$
DX=\begin{pmatrix}a&b\\2c&2d\end{pmatrix},\quad
XD=\begin{pmatrix}a&2b\\c&2d\end{pmatrix}.
$$

La igualdad exige $b=2b$ y $2c=c$, de donde $b=c=0$. No impone restricciones a $a,d$. Recíprocamente, si $b=c=0$, los dos productos son $\operatorname{diag}(a,2d)$.

**Conclusión — 结论。** Las soluciones son exactamente las matrices diagonales $\operatorname{diag}(a,d)$. 中文：必须证明必要性与充分性；仅推出 $b=c=0$ 而不代回验证，会漏掉等价条件的一半。

## M-07. Asociatividad con una columna — 与列向量组合

**Enunciado.** Usar las matrices de M-03 y $x=\begin{pmatrix}1\\-1\end{pmatrix}$ para comprobar $A(Bx)=(AB)x$.

**Análisis — Español.** $B$ transforma dos entradas en tres; después $A$ transforma esas tres en dos. La cadena es compatible.

**分析 — 中文。** 此例把结合律理解为“分步执行”和“先合成再执行”给出同一输出；它是结合律的一次计算检验，普遍证明仍由证明文件提供。

**Resolución.**

$$
Bx=\begin{pmatrix}1\\1\\-3\end{pmatrix},\qquad
A(Bx)=\begin{pmatrix}1+2+3\\3-12\end{pmatrix}
=\begin{pmatrix}6\\-9\end{pmatrix}.
$$

Por otra parte,

$$
(AB)x=\begin{pmatrix}5&-1\\-1&8\end{pmatrix}\begin{pmatrix}1\\-1\end{pmatrix}
=\begin{pmatrix}6\\-9\end{pmatrix}.
$$

**Conclusión — 结论。** Las dos agrupaciones coinciden. 中文：一个例子帮助理解定理，但不能替代对任意矩阵的证明。

接下来 [独立练习](05_Ejercicios.md)，或返回 [模块入口](00_Introduccion.md)。
