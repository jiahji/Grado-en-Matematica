---
title: Demostraciones de las leyes matriciales / 运算法则的完整证明
subject: Álgebra Lineal
tema: Tema 0 · Matrices · Guía 1.1
type: proof
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

# Demostraciones de las leyes matriciales — 运算法则的完整证明

**Fuentes:** las operaciones y la distributividad parten de AL-AP-000, página PDF 2; el desarrollo completo por índices es elaboración didáctica propia. Se usan únicamente las [definiciones](01_Definiciones.md) y las leyes de los escalares en $\mathbb Q,\mathbb R,\mathbb C$.

## P1. Suma y multiplicación por escalares — 加法与数乘

**Hipótesis.** $A,B,C\in M_{m\times n}(\mathbb K)$ y $\lambda,\mu\in\mathbb K$.

**Tesis.** Las ocho identidades de T1.

**Estrategia — Español.** Dos matrices del mismo tamaño son iguales si y solo si coinciden sus entradas. Fijaremos una entrada arbitraria y aplicaremos la propiedad numérica correspondiente.

**策略 — 中文。** 固定任意一行一列，不做有限个例子的验证，而是证明每个合法下标位置都相等。这样才能得到对任意矩阵成立的结论。

**Demostración.** Para todo $1\le i\le m$ y $1\le j\le n$:

$$
\begin{aligned}
(A+B)_{ij}&=a_{ij}+b_{ij}=b_{ij}+a_{ij}=(B+A)_{ij},\\
((A+B)+C)_{ij}&=(a_{ij}+b_{ij})+c_{ij}
=a_{ij}+(b_{ij}+c_{ij})=(A+(B+C))_{ij},\\
(A+0)_{ij}&=a_{ij}+0=a_{ij},\\
(A+(-A))_{ij}&=a_{ij}-a_{ij}=0,\\
(\lambda(A+B))_{ij}&=\lambda(a_{ij}+b_{ij})
=\lambda a_{ij}+\lambda b_{ij}=(\lambda A+\lambda B)_{ij},\\
((\lambda+\mu)A)_{ij}&=(\lambda+\mu)a_{ij}
=\lambda a_{ij}+\mu a_{ij}=(\lambda A+\mu A)_{ij},\\
((\lambda\mu)A)_{ij}&=(\lambda\mu)a_{ij}
=\lambda(\mu a_{ij})=(\lambda(\mu A))_{ij},\\
(1A)_{ij}&=1a_{ij}=a_{ij}.
\end{aligned}
$$

En cada caso las matrices comparadas tienen tamaño $m\times n$. Como coinciden todas sus entradas, se obtienen las ocho identidades.

**Explicación detallada — Español.** El primer y el segundo renglón usan conmutatividad y asociatividad de la suma de escalares; los dos siguientes, sus elementos neutro y opuesto. Los restantes usan distributividad, asociatividad del producto y unidad del cuerpo. No se ha supuesto ninguna propiedad del producto de matrices.

**逐步解释 — 中文。** 证明的关键不是“矩阵当然像数”，而是把每一条矩阵法则归结到已经知道的标量法则。所用标量规则应明确列出，不能把之后才证明的矩阵结合律提前拿来使用。

**Conclusión.** Se cumple T1. En particular, la suma admite cancelación: de $X+Y=X+Z$, sumando $-X$ a ambos lados y usando asociatividad se deduce $Y=Z$.

## P2. Distributividad a ambos lados — 两侧分配律

**Hipótesis.** Para la primera igualdad, $A\in M_{m\times n}$ y $B,C\in M_{n\times r}$. Para la segunda, $A,D\in M_{m\times n}$ y $B\in M_{n\times r}$.

**Tesis.** $A(B+C)=AB+AC$ y $(A+D)B=AB+DB$.

**Estrategia — Español.** Escribir una entrada del producto como suma finita y distribuir en cada sumando sin alterar el orden.

**策略 — 中文。** 展开的是标量乘积 $a_{ik}(b_{kj}+c_{kj})$；最后重新识别为两个矩阵乘积对应的元素。

**Demostración.** Para cada $i,j$,

$$
\begin{aligned}
(A(B+C))_{ij}
&=\sum_{k=1}^{n}a_{ik}(b_{kj}+c_{kj})\\
&=\sum_{k=1}^{n}(a_{ik}b_{kj}+a_{ik}c_{kj})\\
&=\sum_{k=1}^{n}a_{ik}b_{kj}+\sum_{k=1}^{n}a_{ik}c_{kj}
=(AB+AC)_{ij}.
\end{aligned}
$$

Para la otra igualdad,

$$
\begin{aligned}
((A+D)B)_{ij}
&=\sum_{k=1}^{n}(a_{ik}+d_{ik})b_{kj}\\
&=\sum_{k=1}^{n}a_{ik}b_{kj}+\sum_{k=1}^{n}d_{ik}b_{kj}
=(AB+DB)_{ij}.
\end{aligned}
$$

Todas las matrices resultantes son $m\times r$, por lo que la igualdad entrada a entrada prueba ambas afirmaciones.

**Explicación detallada — Español.** Separar una suma finita no requiere ninguna hipótesis de convergencia. El segundo cálculo es necesario: la primera igualdad por sí sola no permite intercambiar los factores matriciales.

**逐步解释 — 中文。** 左分配律与右分配律分别验证，不能通过擅自交换矩阵顺序从一个推出另一个。有限和可以拆分，不涉及分析课程中的收敛问题。

**Conclusión.** Las dos distributividades son válidas conservando el orden.

## P3. Compatibilidad con escalares — 标量与矩阵乘法相容

**Hipótesis.** $A\in M_{m\times n}$, $B\in M_{n\times r}$ y $\lambda\in\mathbb K$.

**Tesis.** $(\lambda A)B=\lambda(AB)=A(\lambda B)$.

**Estrategia — Español.** Sacar un escalar común de una suma finita.

**策略 — 中文。** 标量的交换律允许把 $\lambda$ 移动到每个数乘积前面；这一步只针对域内的数，不能换成任意矩阵。

**Demostración.** Para cada entrada,

$$
\begin{aligned}
((\lambda A)B)_{ij}
&=\sum_k(\lambda a_{ik})b_{kj}
=\lambda\sum_k a_{ik}b_{kj}=(\lambda(AB))_{ij},\\
(A(\lambda B))_{ij}
&=\sum_k a_{ik}(\lambda b_{kj})
=\lambda\sum_k a_{ik}b_{kj}=(\lambda(AB))_{ij}.
\end{aligned}
$$

La igualdad de tamaños y entradas prueba la tesis.

**Explicación detallada — Español.** Se usan asociatividad y conmutatividad de la multiplicación de escalares y distributividad respecto de sumas finitas. En particular, $A(B+2C)=AB+A(2C)=AB+2AC$.

**逐步解释 — 中文。** 最后这个推导完整说明了讲义第 2 页的公式：先用 P2，再用 P3。没有隐含地使用矩阵乘法交换律。

**Conclusión.** Se completa T2.

## P4. Asociatividad — 结合律

**Hipótesis.** $A\in M_{m\times n}$, $B\in M_{n\times r}$ y $C\in M_{r\times s}$.

**Tesis.** $(AB)C=A(BC)$.

**Estrategia — Español.** Desarrollar las dos sumas finitas y cambiar el orden de suma de los índices internos.

**策略 — 中文。** 固定最终位置 $(i,j)$。左边先对 $k$ 求和，右边先对 $\ell$ 求和；两者枚举同一有限指标集合上的全部三项乘积。

**Demostración.** Ambas matrices tienen tamaño $m\times s$. Para todo $i,j$,

$$
\begin{aligned}
((AB)C)_{ij}
&=\sum_{\ell=1}^{r}(AB)_{i\ell}c_{\ell j}\\
&=\sum_{\ell=1}^{r}\sum_{k=1}^{n}(a_{ik}b_{k\ell})c_{\ell j}\\
&=\sum_{k=1}^{n}\sum_{\ell=1}^{r}a_{ik}(b_{k\ell}c_{\ell j})\\
&=\sum_{k=1}^{n}a_{ik}\left(\sum_{\ell=1}^{r}b_{k\ell}c_{\ell j}\right)\\
&=\sum_{k=1}^{n}a_{ik}(BC)_{kj}
=(A(BC))_{ij}.
\end{aligned}
$$

El cambio de orden recorre los mismos $nr$ términos; es válido por asociatividad y conmutatividad de la suma de escalares. Por igualdad entrada a entrada queda demostrado el resultado.

**Explicación detallada — Español.** La multiplicación escalar se reagrupa, pero nunca se permutan los factores matriciales. Los índices libres $i,j$ permanecen fijos; los índices $k,\ell$ son los que se suman.

**逐步解释 — 中文。** 这证明对任意兼容大小成立，不需要矩阵是方阵。三个矩阵在式子里的先后一直是 $A,B,C$，只有计算括号和有限求和次序改变。

**Conclusión.** Se cumple T3 y el producto $ABC$ no necesita especificar agrupación cuando la cadena es compatible.

## P5. Identidad y matriz nula — 单位矩阵与零矩阵

**Hipótesis.** $A\in M_{m\times n}$ y, para los productos nulos, $B\in M_{n\times r}$.

**Tesis.** Las igualdades de T4.

**Estrategia — Español.** En una suma con $\delta_{ij}$ solo sobrevive un término; en una suma de productos por cero todos los términos son cero.

**策略 — 中文。** 不展开整个大矩阵，只检查固定位置：单位矩阵的对应行或列只选中原矩阵的一个元素。

**Demostración.** Para $1\le i\le m$, $1\le j\le n$:

$$
(I_mA)_{ij}=\sum_{k=1}^{m}\delta_{ik}a_{kj}=a_{ij},\qquad
(AI_n)_{ij}=\sum_{k=1}^{n}a_{ik}\delta_{kj}=a_{ij}.
$$

En el primer sumatorio solo el término $k=i$ puede ser no nulo; en el segundo, solo $k=j$. Para las matrices nulas,

$$
(A0)_{ij}=\sum_{k=1}^{n}a_{ik}0=0,\qquad
(0B)_{ij}=\sum_{k=1}^{n}0b_{kj}=0.
$$

Los tamaños son los indicados en T4. Luego coinciden todas las entradas correspondientes.

**Explicación detallada — Español.** Se ha probado que un factor nulo produce un producto nulo. No se ha demostrado, ni es cierto, que un producto nulo obligue a que alguno de sus factores sea nulo.

**逐步解释 — 中文。** 结论的方向不能反过来。后续计算中的非零零乘积反例说明这里的逻辑差别是实质性的。

**Conclusión.** Se cumple T4.

## P6. Cuadrado de una suma y condición de conmutación — 平方展开与交换条件

**Hipótesis.** $A,B\in M_{n\times n}(\mathbb K)$.

**Tesis.** T5, incluida su equivalencia.

**Estrategia — Español.** Distribuir dos veces y después cancelar sumandos usando P1.

**策略 — 中文。** 先展开正确的四项式，再比较常见但有条件的三项式；两者之差只有 $BA-AB$。

**Demostración.** Por P2,

$$
(A+B)^2=(A+B)A+(A+B)B=A^2+BA+AB+B^2.
$$

Por conmutatividad de la suma, esto es $A^2+AB+BA+B^2$. Si $AB=BA$, los términos cruzados suman $2AB$, lo que prueba una implicación. Recíprocamente, si

$$
A^2+AB+BA+B^2=A^2+2AB+B^2,
$$

se suman los opuestos de $A^2$, $B^2$ y $AB$ a ambos miembros y se aplican las leyes de P1. Se obtiene $BA=AB$.

**Explicación detallada — Español.** En el paso de cancelación se cancelan sumandos, no factores. Ninguna matriz se ha dividido ni invertido.

**逐步解释 — 中文。** “消去相同加项”和“约去矩阵乘积的因子”是两种完全不同的运算。前者已证明，后者没有一般性保证。

**Conclusión.** La fórmula abreviada del cuadrado vale exactamente para los pares que conmutan.

继续 [完整例题](04_Ejemplos.md) 或返回 [模块入口](00_Introduccion.md)。
