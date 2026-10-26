---
title: Leyes de las operaciones matriciales / 矩阵运算法则
subject: Álgebra Lineal
tema: Tema 0 · Matrices · Guía 1.1
type: theorem
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

# Leyes de las operaciones matriciales — 矩阵运算法则

**Fuente de partida:** AL-AP-000, página PDF 2, operaciones, distributividad y anotaciones de conmutatividad. Las leyes generales se desarrollan como suplemento didáctico de AL-GD-001, apartado 1.1. Todas las demostraciones se incluyen en [el archivo de pruebas](03_Demostraciones.md).

## T1. Suma y escalares — 加法与标量规则

**Enunciado.** Para $A,B,C\in M_{m\times n}(\mathbb K)$ y $\lambda,\mu\in\mathbb K$:

$$
\begin{aligned}
A+B&=B+A,&(A+B)+C&=A+(B+C),\\
A+0_{m\times n}&=A,&A+(-A)&=0_{m\times n},\\
\lambda(A+B)&=\lambda A+\lambda B,&(\lambda+\mu)A&=\lambda A+\mu A,\\
(\lambda\mu)A&=\lambda(\mu A),&1A&=A.
\end{aligned}
$$

**Explicación en español.** Estas igualdades se reducen a igualdades entre números en cada posición. En particular, se puede sumar la misma matriz a ambos miembros de una igualdad y después cancelar sumandos.

**中文解释。** 每个位置都独立遵守标量运算，所以加法与数乘的规则可以逐个元素继承。全部矩阵必须在同一个 $M_{m\times n}(\mathbb K)$ 中；不能因符号像普通代数，就忽略对象大小。

**Uso y error típico.** Permiten simplificar una ecuación como $2X+A=3B$ y comprobar igualdad de matrices. No autorizan una suma de tamaños distintos.

## T2. Bilinealidad del producto — 乘法对两边的线性性

**Enunciado.** Si $A\in M_{m\times n}$ y $B,C\in M_{n\times r}$, entonces

$$
A(B+C)=AB+AC.
$$

Si $A,D\in M_{m\times n}$ y $B\in M_{n\times r}$, entonces

$$
(A+D)B=AB+DB.
$$

Además, para $\lambda\in\mathbb K$,

$$
(\lambda A)B=\lambda(AB)=A(\lambda B).
$$

**Explicación en español.** Se puede distribuir el producto sobre una suma a cada lado, siempre manteniendo el orden de los factores. El escalar se puede extraer porque es un número del cuerpo, pero una matriz no puede desplazarse de un lado al otro con la misma justificación.

**中文解释。** 展开不改变“谁在左、谁在右”。例如讲义中的 $A(B+2C)=AB+2AC$ 正是此定理的特例；不能把后项写成 $2CA$。

**Aplicación.** Desarrollar expresiones, comparar dos procedimientos de cálculo o separar un vector columna en suma de columnas. El [ejemplo rectangular](04_Ejemplos.md) muestra el uso numérico.

## T3. Asociatividad — 结合律

**Enunciado.** Para $A\in M_{m\times n}$, $B\in M_{n\times r}$ y $C\in M_{r\times s}$,

$$
(AB)C=A(BC)\in M_{m\times s}.
$$

**Explicación en español.** Cambiar la agrupación conserva la cadena de factores y puede reducir el trabajo de cálculo. No cambia el orden: asociatividad y conmutatividad son propiedades distintas.

**中文解释。** $ABC$ 可先算 $AB$，也可先算 $BC$，因为两种括号方式对中间指标求和的结果一致。它不意味着能把中间的 $B$ 移到 $A$ 前面。

**Uso y condiciones.** Justifica las potencias y el cálculo de $A(Bx)$. Se deben comprobar las dimensiones de toda la cadena, no solo de los dos primeros factores.

## T4. Identidad y producto nulo — 单位矩阵与零乘积

**Enunciado.** Si $A\in M_{m\times n}$, entonces

$$
I_mA=A=AI_n.
$$

Para $B\in M_{n\times r}$,

$$
A0_{n\times r}=0_{m\times r},\qquad0_{m\times n}B=0_{m\times r}.
$$

**Explicación en español.** La identidad selecciona una única entrada de cada suma; una matriz nula aporta solamente sumandos cero. La implicación recíproca «$AB=0$ implica $A=0$ o $B=0$» es falsa.

**中文解释。** 标量中的“零乘积无非零因子”不能直接套用到矩阵。矩阵可能保留一部分信息、同时把另一部分消去，从而两个非零矩阵的乘积为零。

**Contraejemplo.** Para $N=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ se tiene $N\ne0$ y $N^2=0$; se calcula en [ejemplos](04_Ejemplos.md).

## T5. Cuadrado de una suma — 和的平方

**Enunciado.** Si $A,B\in M_{n\times n}(\mathbb K)$,

$$
(A+B)^2=A^2+AB+BA+B^2.
$$

Además,

$$
(A+B)^2=A^2+2AB+B^2\iff AB=BA.
$$

**Explicación en español.** Hay dos términos cruzados y no se pueden agrupar en $2AB$ sin una condición adicional. Algunas matrices sí conmutan, por ejemplo $I_n$ con cualquier matriz del mismo tamaño o dos matrices diagonales.

**中文解释。** “矩阵乘法不交换”意为交换律一般不成立，而不是每一对矩阵都必定不交换。因此不能把讲义中的 $AB\ne BA$ 当成对所有 $A,B$ 的全称断言；必须用反例否定普遍交换律，用具体条件判断某一对是否交换。

**Errores frecuentes.** $A(B+C)=BA+CA$ 改变了顺序；$AB=AC\Rightarrow B=C$ 不能仅靠 $A\ne0$；$AB$ 和 $BA$ 还可能大小不同甚至其中一个未定义。

返回 [定义](01_Definiciones.md)，继续 [逐步证明](03_Demostraciones.md)。
