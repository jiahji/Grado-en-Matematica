---
title: 'Matrices: definiciones y operaciones / 矩阵定义与运算'
subject: Álgebra Lineal
tema: Tema 0 · Matrices · Guía 1.1
type: definition
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

# Matrices: definiciones y operaciones — 矩阵定义与运算

**Fuente:** AL-AP-000, página PDF 2; AL-GD-001, página 5, apartado 1.1. La formulación por índices y las aclaraciones siguientes desarrollan el contenido de la diapositiva.

## 1. Matriz, tamaño e igualdad — 矩阵、大小与相等

**Definición formal.** Sean $m,n\ge1$ enteros y $\mathbb K\in\{\mathbb Q,\mathbb R,\mathbb C\}$. Una matriz de tamaño $m\times n$ con entradas en $\mathbb K$ es una familia ordenada

$$
A=(a_{ij})_{\substack{1\le i\le m\\1\le j\le n}},\qquad a_{ij}\in\mathbb K.
$$

El índice $i$ identifica la fila（行）y $j$ la columna（列）. El conjunto de estas matrices se denota $M_{m\times n}(\mathbb K)$. Si $m=n$, la matriz es cuadrada（方阵）. Dos matrices son iguales si tienen el mismo tamaño y coinciden todas sus entradas:

$$
A=B\iff a_{ij}=b_{ij}\quad\text{para todo }i,j.
$$

**Explicación en español.** El tamaño forma parte del objeto: una fila con tres entradas no es la misma matriz que una columna con tres entradas. Tampoco basta tener el mismo número total de entradas para poder sumar matrices.

**中文解释。** 矩阵不只是“数的集合”，因为位置决定意义。$\begin{pmatrix}1&2\end{pmatrix}$ 与 $\begin{pmatrix}1\\2\end{pmatrix}$ 大小不同；交换某两行通常得到另一矩阵。源材料第 2 页用 $n\times m$ 表示 $n$ 行 $m$ 列；本文改用 $m$ 行 $n$ 列以与其第 3 页的方程组一致，只改变哑字母，不改变规则。

## 2. Suma y producto por un escalar — 加法与数乘

**Definición.** Para $A,B\in M_{m\times n}(\mathbb K)$ y $\lambda\in\mathbb K$:

$$
A+B=(a_{ij}+b_{ij}),\qquad \lambda A=(\lambda a_{ij}).
$$

La matriz nula（零矩阵）$0_{m\times n}$ tiene todas sus entradas iguales a cero. El opuesto（加法逆元）de $A$ es $-A=(-a_{ij})$ y $A-B:=A+(-B)$.

**Explicación en español.** Ambas operaciones actúan entrada a entrada. En la suma se exige que cada posición tenga una posición correspondiente en la otra matriz; por eso las dimensiones deben coincidir. En el producto por un escalar, un único número multiplica todas las entradas.

**中文解释。** 数乘 $\lambda A$ 中的 $\lambda$ 是一个数，不是一张矩阵。加法是同一位置配对；$2\times3$ 与 $3\times2$ 虽然各有六个元素，仍不能按这里的定义相加。

## 3. Producto de matrices — 矩阵乘法

**Definición formal.** Si $A\in M_{m\times n}(\mathbb K)$ y $B\in M_{n\times r}(\mathbb K)$, su producto es la matriz $AB=C\in M_{m\times r}(\mathbb K)$ dada por

$$
c_{ij}=\sum_{k=1}^{n}a_{ik}b_{kj},\qquad 1\le i\le m,\quad 1\le j\le r.
$$

La suma se realiza sobre el índice compartido $k$. El producto se define cuando el número de columnas del factor izquierdo coincide con el número de filas del derecho.

**Explicación en español.** Para obtener $c_{ij}$ se fija la fila $i$ de $A$ y la columna $j$ de $B$. Se multiplican sus primeras entradas entre sí, después las segundas, y así sucesivamente, y se suman los resultados. Los índices $i,j$ quedan libres y determinan la posición de la entrada final.

**中文解释。** $a_{ik}$ 中 $k$ 是列，$b_{kj}$ 中同一个 $k$ 是行，表示前一个过程的中间输出与后一个过程的中间输入逐项配对。不要把式子误写成 $a_{ij}b_{ij}$；那是另一种运算，不是本课程此处的矩阵乘法。

Por ejemplo,

$$
\begin{pmatrix}1&2&3\end{pmatrix}
\begin{pmatrix}4\\5\\6\end{pmatrix}
=\begin{pmatrix}32\end{pmatrix},
$$

mientras que el producto en el orden opuesto es

$$
\begin{pmatrix}4\\5\\6\end{pmatrix}
\begin{pmatrix}1&2&3\end{pmatrix}
=\begin{pmatrix}4&8&12\\5&10&15\\6&12&18\end{pmatrix}.
$$

Son productos de tamaños distintos; no tiene sentido declararlos iguales ni restarlos entre sí.

## 4. Identidad y potencias — 单位矩阵与幂

**Definición.** La matriz identidad（单位矩阵）$I_n=(\delta_{ij})\in M_{n\times n}(\mathbb K)$ tiene $\delta_{ij}=1$ si $i=j$ y $\delta_{ij}=0$ si $i\ne j$.

Para una matriz cuadrada $A$, se define $A^0=I_n$ y recursivamente $A^{k+1}=A^kA$ para $k\ge0$. La asociatividad, demostrada en el módulo, permitirá omitir los paréntesis de productos sucesivos.

**Explicación en español.** La identidad tiene el tamaño que permite el producto: si $A$ es $m\times n$, a la izquierda se usa $I_m$ y a la derecha $I_n$. Las potencias mediante productos repetidos requieren una matriz cuadrada.

**中文解释。** “乘以单位矩阵不变”必须连同维数理解：$I_mA=AI_n=A$。对一般长方矩阵不能写 $A^2$，因为矩阵乘法中的内侧维数不匹配。

## 5. Vocabulario y control de tipos — 术语与类型检查

| Español | 中文 | 检查要点 |
| --- | --- | --- |
| entrada o coeficiente $a_{ij}$ | 矩阵元素 | 先行后列 |
| tamaño $m\times n$ | 大小、维数规格 | $m$ 行 $n$ 列，不是向量空间维数 |
| producto por un escalar | 数乘 | 标量来自 $\mathbb K$ |
| producto matricial | 矩阵乘积 | 先检查内侧维数 |
| matriz nula | 零矩阵 | 大小由上下文确定 |
| matriz identidad | 单位矩阵 | 必为方阵 |

El rango（秩）y la inversa matricial（逆矩阵）no se definen aquí: requieren el siguiente módulo de Gauss. No debe inferirse de $A\ne0$ que $A$ tenga inversa.

继续 [性质](02_Teoremas.md)；返回 [模块入口](00_Introduccion.md)。
