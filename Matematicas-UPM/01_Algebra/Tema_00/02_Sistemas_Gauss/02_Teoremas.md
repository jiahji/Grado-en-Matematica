---
title: Clasificación, rango e inversas / 分类、秩与逆矩阵定理
subject: Álgebra Lineal
tema: Tema 0 · Guía 1.2
type: theorem
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

# Clasificación, rango e inversas — 分类、秩与逆矩阵定理

**Fuentes:** AL-AP-000 pp. 3–9; AL-AP-004 pp. 13–20. Las pruebas completas se encuentran en [Demostraciones](03_Demostraciones.md). Se trabaja sobre $\mathbb K=\mathbb Q,\mathbb R$ o $\mathbb C$.

## T1. Equivalencia por filas — 行变换保解集

Cada operación elemental aplicada a $(A\mid b)$ produce un sistema equivalente. Una sucesión finita también conserva el conjunto de soluciones. Cada matriz elemental es invertible.

**Español.** Esta es la justificación de Gauss: cada paso mantiene tanto la implicación hacia el sistema nuevo como la implicación de regreso al original.

**中文。** 仅仅由原方程推导出一个新方程不一定同解；必须保证能把被替换的旧方程恢复。乘零或只保留两方程之和一般做不到。

## T2. Existencia de escalonamiento y parámetros — 阶梯化与参数

El algoritmo de Gauss termina tras un número finito de operaciones y obtiene forma escalonada. Si el sistema reducido es compatible y hay $r$ pivotes de coeficientes, asignar valores arbitrarios a las $n-r$ variables libres determina **exactamente una** elección de las restantes variables.

**Español.** Las variables libres parametrizan las soluciones de forma biyectiva. Una ecuación redundante no quita parámetros; una contradicción elimina todas las soluciones.

**中文。** 从最后一个主元向上回代，每一步只除以已经确认非零的主元。因此参数化既给出全部解，也不重复描述同一个解。

## T3. Rango y pivotes — 秩与主元数

Las operaciones elementales conservan todas las relaciones lineales entre columnas. Si una forma escalonada de $A$ tiene $r$ filas no nulas, entonces $\operatorname{rg}(A)=r$. Las columnas originales con los índices pivote son independientes y generan todas las columnas originales. En particular,

$$
0\le\operatorname{rg}(A)\le\min(m,n).
$$

El rango de filas, definido como máximo número de filas independientes, coincide con el de columnas.

**Español.** Dos rutas de eliminación pueden producir escalonadas distintas, pero tienen el mismo número de pivotes. Los índices elegidos describen columnas de la matriz original, no las columnas transformadas como si fueran geométricamente idénticas.

**中文。** 这才使课堂的“数台阶”成为合法算法，而不是一个可能依赖操作选择的猜测。不要在未阶梯化的矩阵里只数非零行。

## T4. Teorema de Rouché–Frobenius — 相容判别与分类

Sean $A\in M_{m\times n}$, $b\in\mathbb K^m$ y $\bar A=(A\mid b)$.

$$
Ax=b\text{ es compatible}\iff\operatorname{rg}(A)=\operatorname{rg}(\bar A).
$$

Más precisamente:

| 条件 | Clasificación | 中文含义 |
| --- | --- | --- |
| $\operatorname{rg}(A)<\operatorname{rg}(\bar A)$ | incompatible | 无解 |
| $\operatorname{rg}(A)=\operatorname{rg}(\bar A)=n$ | compatible determinado | 唯一解 |
| $\operatorname{rg}(A)=\operatorname{rg}(\bar A)=r<n$ | compatible indeterminado | 在本课程的无限域上有无穷多解，含 $n-r$ 个独立参数 |

Además $\operatorname{rg}(A)\le\operatorname{rg}(\bar A)\le\operatorname{rg}(A)+1$.

**Español.** Se compara el rango con el número de incógnitas $n$, no con el número de ecuaciones $m$. La conclusión «infinitas» usa que el cuerpo es infinito. Sobre un cuerpo finito, la parametrización sigue siendo válida, pero el número de soluciones compatibles es $|\mathbb K|^{n-r}$.

**中文。** 矩阵秩为未知数个数，并不单独保证有解：还要检查增广秩。多出的方程可能冗余，也可能矛盾，不能仅凭方程多或少分类。

## T5. Interpretación por columnas — 列向量解释

Si $a_1,\ldots,a_n$ son las columnas de $A$, entonces

$$
Ax=b\iff x_1a_1+\cdots+x_na_n=b.
$$

Por tanto la compatibilidad equivale a $b\in\langle a_1,\ldots,a_n\rangle$.

**Español.** El sistema pregunta si el término independiente se puede construir con las columnas y, si es así, con qué coeficientes. Añadir $b$ no aumenta el rango exactamente cuando no aporta una dirección nueva.

**中文。** 这与 AL-AP-004 p. 20 的证明思路一致；本库修正原件中右端向量长度和缺写 $\dim$ 的排印问题，不改动原文件。

## T6. Estructura de las soluciones — 非齐次解是一个平移

Si $x_p$ es una solución de $Ax=b$, entonces

$$
S(A,b)=\{x_p+h:Ah=0\}.
$$

Si el rango es $r$, existen soluciones homogéneas $h_1,\ldots,h_{n-r}$ tales que toda solución tiene una expresión única

$$
x=x_p+t_1h_1+\cdots+t_{n-r}h_{n-r}.
$$

**Español.** Se elige cada $h_j$ asignando $1$ a una variable libre y $0$ a las restantes en el sistema homogéneo. La unicidad se comprueba mirando esas coordenadas libres.

**中文。** 不是把任意几个解直接相加。两个非齐次解之和通常不再是原系统的解；它们的差才是齐次解。$b\ne0$ 时，非空解集不含零向量，所以不是原点处的向量子空间。

## T7. Invertibilidad y Gauss–Jordan — 可逆判别与求逆

Para $A\in M_{n\times n}$ son equivalentes:

1. $A$ es invertible.
2. $\operatorname{rg}(A)=n$.
3. $Ax=0$ solo tiene la solución $0$.
4. Para cada $b\in\mathbb K^n$, $Ax=b$ tiene solución única.

Si $(A\mid I_n)$ se transforma por filas en $(I_n\mid B)$, entonces $B=A^{-1}$. La inversa es única. Si el rango es menor que $n$, no se puede llevar el bloque izquierdo a $I_n$.

**Español.** Es importante cuantificar «para cada $b$». Un sistema concreto puede ser compatible aunque $A$ sea singular, pero nunca tendrá solución única si $A$ es cuadrada y singular.

**中文。** 一次消元同时解出标准列向量对应的全部方程组，就是在构造逆矩阵的每一列。需要检查最后是双侧逆，而非只凭某个乘积成立就略过证明。

## T8. Varios términos independientes — 多个右端

Una misma sucesión de operaciones transforma $(A\mid b^{(1)}\mid\cdots\mid b^{(k)})$ y resuelve cada columna por separado. Si $A$ es invertible, $AX=B$ tiene la única solución $X=A^{-1}B$.

**Español.** Si $A$ es singular, cada columna debe comprobarse: una puede ser compatible y otra no. La presencia de varios términos independientes no añade incógnitas al mismo sistema vectorial.

**中文。** 不要把每个右端列都误认为一个新未知量；它们是多个共享系数矩阵的系统。证明和例题均在本模块提供。

继续 [完整证明](03_Demostraciones.md) 或 [例题](04_Ejemplos.md)。
