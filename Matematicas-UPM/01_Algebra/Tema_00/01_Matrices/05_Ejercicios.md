---
title: Ejercicios de matrices / 矩阵独立练习
subject: Álgebra Lineal
tema: Tema 0 · Matrices · Guía 1.1
type: exercises
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

# Ejercicios — 矩阵独立练习

**Procedencia:** los doce ejercicios son de elaboración propia, basados en el alcance de AL-GD-001, 1.1, y las operaciones de AL-AP-000, página PDF 2. No se ha recibido una hoja oficial de problemas ni un examen; las dificultades indican el esfuerzo didáctico estimado, no una clasificación del profesor.

**Instrucciones en español.** Resolver los ejercicios por escrito, en español, comprobando primero los tamaños y justificando cada transformación. Intentar una solución propia antes de consultar el archivo separado de soluciones. Los identificadores M-E01–M-E12 se mantienen estables para relacionar cada enunciado con su resolución.

**中文说明。** 先检查大小，再独立书写西班牙语解答，完成后查阅 [单独解答文件](06_Soluciones.md)。这里不放答案；题号 M-E01 至 M-E12 保持稳定，以便追踪练习和解答。

## M-E01 — Dimensiones / 大小检查 · básico

Sean $A\in M_{2\times3}$, $B\in M_{3\times4}$ y $C\in M_{4\times2}$. Indicar cuáles de las expresiones $AB$, $BA$, $BC$, $CA$, $AC$, $ABC$ y $CAB$ están definidas y dar sus tamaños. Justificar las dos posibles agrupaciones de cada producto triple definido.

## M-E02 — Igualdad / 相等条件 · básico

Determinar todos los $a,b,c,d\in\mathbb R$ para los que

$$
\begin{pmatrix}a+1&2b\\c-d&3\end{pmatrix}
=\begin{pmatrix}4&-6\\0&3\end{pmatrix}.
$$

## M-E03 — Combinación matricial / 加法与数乘 · básico

Para

$$
A=\begin{pmatrix}2&-1\\0&3\end{pmatrix},\quad
B=\begin{pmatrix}-1&2\\4&0\end{pmatrix},
$$

calcular $2A-3B$ y justificar su tamaño.

## M-E04 — Producto rectangular / 长方矩阵乘法 · intermedio

Sean

$$
A=\begin{pmatrix}1&0&2\\-1&3&1\end{pmatrix},\quad
B=\begin{pmatrix}2&1\\0&-1\\1&2\end{pmatrix},\quad
x=\begin{pmatrix}1\\2\end{pmatrix}.
$$

Calcular $AB$, $Bx$, $A(Bx)$ y $(AB)x$. Explicar qué se ha comprobado y por qué no constituye una demostración general de asociatividad.

## M-E05 — Cuadrado de una suma / 平方展开 · intermedio

Con $A=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ y $B=\begin{pmatrix}1&0\\1&1\end{pmatrix}$, calcular $AB$, $BA$, $(A+B)^2$ y $A^2+2AB+B^2$. Interpretar la diferencia.

## M-E06 — Escalar no nulo / 非零标量 · demostración

Sean $A\in M_{m\times n}(\mathbb K)$ y $\lambda\in\mathbb K\setminus\{0\}$. Demostrar que $\lambda A=0$ implica $A=0$. Precisar dónde se usa $\lambda\ne0$ y explicar por qué la afirmación falla para $\lambda=0$.

## M-E07 — Cancelación falsa / 错误的因子消去 · contraejemplo

Construir matrices $A,B,C\in M_{2\times2}(\mathbb R)$ tales que $A\ne0$, $AB=AC$ y $B\ne C$. Verificar todas las condiciones. Mostrar también que puede haber dos factores matriciales no nulos cuyo producto sea cero.

## M-E08 — Conmutación con una diagonal / 对角矩阵交换条件 · intermedio

Sea $D=\operatorname{diag}(\alpha,\beta)$ con $\alpha,\beta\in\mathbb R$. Hallar todas las $X\in M_{2\times2}(\mathbb R)$ que satisfacen $DX=XD$, distinguiendo $\alpha=\beta$ y $\alpha\ne\beta$.

## M-E09 — Ecuación matricial / 矩阵方程 · intermedio

Usando $A,B$ de M-E03, resolver $2X+A=3B$ y comprobar el resultado por sustitución.

## M-E10 — Equivalencia / 等价命题 · demostración

Para $A,B\in M_{n\times n}(\mathbb K)$, demostrar

$$
(A+B)^2=A^2+2AB+B^2\iff AB=BA.
$$

Separar explícitamente las dos implicaciones e identificar si se cancelan sumandos o factores.

## M-E11 — Matrices elementales de posición / 单位置矩阵 · ampliación

Para $1\le i,j\le n$, sea $E_{ij}$ la matriz con un $1$ en la posición $(i,j)$ y ceros en las demás. Demostrar

$$
E_{ij}E_{k\ell}=\delta_{jk}E_{i\ell},
$$

donde $\delta_{jk}=1$ si $j=k$ y $0$ en caso contrario.

## M-E12 — Matrices que conmutan con todas / 与所有矩阵交换 · ampliación universitaria

Sea $n\ge1$ y $X\in M_{n\times n}(\mathbb R)$. Demostrar que $XA=AX$ para toda $A\in M_{n\times n}(\mathbb R)$ si y solo si existe $\lambda\in\mathbb R$ tal que $X=\lambda I_n$.

Las dos últimas actividades profundizan en el producto; no se afirma que sean preguntas exigidas por el profesor. 返回 [模块入口](00_Introduccion.md)。
