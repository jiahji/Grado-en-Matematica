---
title: Ejemplos de Gauss, rango e inversas / 消元、秩与求逆例题
subject: Álgebra Lineal
tema: Tema 0 · Guía 1.2
type: example
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

# Ejemplos de Gauss, rango e inversas — 完整例题

**Procedencia.** G-01–G-04 conservan enunciados manuscritos de AL-AP-000, pp. 5 y 8; G-05 conserva la matriz del ejemplo de p. 9. Los desarrollos se han recalculado. G-06 es de elaboración propia. No se atribuyen a exámenes reales.

## G-01. Solución única y corrección del original — 唯一解与原件纠错

**Enunciado original.** Resolver

$$
\begin{cases}
3x+2y+z=1,\\2x-5y+2z=6,\\x-2y+z=7.
\end{cases}
$$

**Análisis — Español.** Conviene intercambiar primera y tercera filas para empezar con un pivote $1$. Se operará en toda la matriz ampliada; después se comprobarán los tres enunciados originales.

**分析 — 中文。** 这不是重新猜一个“更漂亮”的答案。先保留原题，逐步定位源笔记中首次不等价的算术步骤，再从正确步骤继续求解。

**Resolución.**

$$
\left(\begin{array}{ccc|c}3&2&1&1\\2&-5&2&6\\1&-2&1&7\end{array}\right)
\xrightarrow{F_1\leftrightarrow F_3}
\left(\begin{array}{ccc|c}1&-2&1&7\\2&-5&2&6\\3&2&1&1\end{array}\right).
$$

Aplicamos $F_2\leftarrow F_2-2F_1$ y $F_3\leftarrow F_3-3F_1$:

$$
\left(\begin{array}{ccc|c}1&-2&1&7\\0&-1&0&-8\\0&8&-2&-20\end{array}\right).
$$

En la tercera fila el coeficiente de $z$ es $1-3\cdot1=-2$, no $-4$ como aparece en las pp. 5 y 8. Ahora $F_2\leftarrow-F_2$ y $F_3\leftarrow F_3-8F_2$ dan

$$
\left(\begin{array}{ccc|c}1&-2&1&7\\0&1&0&8\\0&0&-2&-84\end{array}\right)
\xrightarrow{F_3\leftarrow-\frac12F_3}
\left(\begin{array}{ccc|c}1&-2&1&7\\0&1&0&8\\0&0&1&42\end{array}\right).
$$

Por sustitución, $z=42$, $y=8$ y $x=7+2\cdot8-42=-19$. Equivale a continuar con $F_1\leftarrow F_1-F_3$ y $F_1\leftarrow F_1+2F_2$ hasta $(I_3\mid(-19,8,42)^{\mathsf T})$.

**Comprobación.**

$$
3(-19)+2(8)+42=1,\qquad2(-19)-5(8)+2(42)=6,\qquad-19-2(8)+42=7.
$$

**Conclusión.** $\operatorname{rg}(A)=\operatorname{rg}(A\mid b)=3=n$ y la solución única es $(-19,8,42)$.

**Explicación y errores — Español.** El vector original escrito al final, $(2,8,21)$, cumple las dos últimas ecuaciones, pero en la primera da $43$, no $1$. Verificar solo una ecuación habría ocultado el error. El procedimiento elegido en el apunte es válido; el fallo está en una entrada aritmética.

**中文解释与易错点。** 错误发生在一个中间系数，而不是分类定理。最终还得到三个主元，所以“唯一解”的分类依然正确，但具体解错误。解集分类正确不能替代数值回代。

## G-02. Una variable libre — 一个自由参数

**Enunciado original.** Resolver

$$
x-y=1,\qquad x+z=0,\qquad2x-y+z=1.
$$

**Análisis — Español.** La tercera ecuación es suma de las dos primeras. Gauss debe hacer visible esa redundancia sin introducir una contradicción.

**分析 — 中文。** 有三条方程不代表三条独立约束。应寻找的是有多少个主元，而不是只数方程。

**Resolución.**

$$
\left(\begin{array}{ccc|c}1&-1&0&1\\1&0&1&0\\2&-1&1&1\end{array}\right)
\xrightarrow{\substack{F_2\leftarrow F_2-F_1\\F_3\leftarrow F_3-2F_1}}
\left(\begin{array}{ccc|c}1&-1&0&1\\0&1&1&-1\\0&1&1&-1\end{array}\right)
\xrightarrow{F_3\leftarrow F_3-F_2}
\left(\begin{array}{ccc|c}1&-1&0&1\\0&1&1&-1\\0&0&0&0\end{array}\right).
$$

Tomamos $y=t$. Entonces $x=1+t$ y $z=-1-t$; todos los $t\in\mathbb K$ satisfacen las tres ecuaciones, pues

$$
(1+t)-t=1,\quad(1+t)+(-1-t)=0,\quad2(1+t)-t+(-1-t)=1.
$$

**Conclusión.** Los dos rangos son $2<3$ y

$$
S=\{(1+t,t,-1-t):t\in\mathbb K\}
=(1,0,-1)+\{t(1,1,-1):t\in\mathbb K\}.
$$

**Explicación — Español.** Aunque $y$ no es la variable no pivote de esta escalonada, se puede elegir como parámetro porque la relación $y+z=-1$ determina $z$ de forma única. La parametrización sigue siendo biyectiva.

**中文解释。** 按最机械的主元规则可取 $z$ 自由；这里沿用原笔记取 $y=t$，已明确验证其同样一一描述全部解。零行代表冗余，不是无解。

## G-03. Contradicción — 无解

**Enunciado original.** Resolver $y+z=1$, $x-y=2$, $x+z=2$.

**Análisis — Español.** Las dos primeras ecuaciones suman $x+z=3$, en conflicto con la tercera. La matriz ampliada debe exhibir la misma contradicción.

**分析 — 中文。** 先看方程关系能预判结果，再通过消元精确显示哪一行产生矛盾。

**Resolución.**

$$
\left(\begin{array}{ccc|c}0&1&1&1\\1&-1&0&2\\1&0&1&2\end{array}\right)
\xrightarrow{F_1\leftrightarrow F_2}
\left(\begin{array}{ccc|c}1&-1&0&2\\0&1&1&1\\1&0&1&2\end{array}\right)
\xrightarrow{F_3\leftarrow F_3-F_1}
\left(\begin{array}{ccc|c}1&-1&0&2\\0&1&1&1\\0&1&1&0\end{array}\right)
\xrightarrow{F_3\leftarrow F_3-F_2}
\left(\begin{array}{ccc|c}1&-1&0&2\\0&1&1&1\\0&0&0&-1\end{array}\right).
$$

**Conclusión.** La última fila es $0=-1$. $\operatorname{rg}(A)=2$, $\operatorname{rg}(A\mid b)=3$ y $S=\varnothing$.

**Explicación — Español.** No se debe tratar el pivote de la columna ampliada como variable libre ni continuar buscando valores para $x,y,z$.

**中文解释。** 任意选择未知量都不能让 $0=-1$ 成立；这条矛盾足以排除所有候选解。

## G-04. Dos sistemas simultáneos — 两个右端同时求解

**Enunciado original.** Resolver con el mismo coeficiente $A=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ los sistemas con $b^{(1)}=(2,0)^{\mathsf T}$ y $b^{(2)}=(1,1)^{\mathsf T}$.

**Análisis — Español.** Una misma sucesión de filas se aplica a ambos términos independientes. Se conservan dos columnas de resultados separadas.

**分析 — 中文。** 同样的消元左侧只做一次；两个右端各自跟随同一变换，不把两个系统的解混在一起。

**Resolución.**

$$
\left(\begin{array}{cc|cc}1&1&2&1\\1&-1&0&1\end{array}\right)
\xrightarrow{F_2\leftarrow F_2-F_1}
\left(\begin{array}{cc|cc}1&1&2&1\\0&-2&-2&0\end{array}\right)
\xrightarrow{F_2\leftarrow-\frac12F_2}
\left(\begin{array}{cc|cc}1&1&2&1\\0&1&1&0\end{array}\right)
\xrightarrow{F_1\leftarrow F_1-F_2}
\left(\begin{array}{cc|cc}1&0&1&1\\0&1&1&0\end{array}\right).
$$

**Conclusión.** $x^{(1)}=(1,1)^{\mathsf T}$ y $x^{(2)}=(1,0)^{\mathsf T}$. Multiplicar por $A$ devuelve $(2,0)^{\mathsf T}$ y $(1,1)^{\mathsf T}$, respectivamente.

**Explicación — Español.** Las dos columnas de la derecha son dos vectores solución, no un único vector de cuatro incógnitas.

**中文解释。** 若今后增加更多右端，左侧的变换仍可复用。这也是 LU 分解加速重复求解的动机之一。

## G-05. Inversa por Gauss–Jordan — 求逆

**Enunciado original.** Hallar la inversa de $A=\begin{pmatrix}1&1\\2&1\end{pmatrix}$, matriz de la anotación de AL-AP-000 p. 9.

**Análisis — Español.** Se resuelven simultáneamente los sistemas con los dos vectores de la base canónica como términos independientes.

**分析 — 中文。** 右侧放单位矩阵；左侧每次做什么，右侧也必须做什么，最后右侧记录整个逆变换。

**Resolución.**

$$
\left(\begin{array}{cc|cc}1&1&1&0\\2&1&0&1\end{array}\right)
\xrightarrow{F_2\leftarrow F_2-2F_1}
\left(\begin{array}{cc|cc}1&1&1&0\\0&-1&-2&1\end{array}\right)
\xrightarrow{F_2\leftarrow-F_2}
\left(\begin{array}{cc|cc}1&1&1&0\\0&1&2&-1\end{array}\right)
\xrightarrow{F_1\leftarrow F_1-F_2}
\left(\begin{array}{cc|cc}1&0&-1&1\\0&1&2&-1\end{array}\right).
$$

Luego $B=\begin{pmatrix}-1&1\\2&-1\end{pmatrix}$. Comprobamos ambos productos:

$$
AB=\begin{pmatrix}-1+2&1-1\\-2+2&2-1\end{pmatrix}=I_2,\qquad
BA=\begin{pmatrix}-1+2&-1+1\\2-2&2-1\end{pmatrix}=I_2.
$$

**Conclusión.** $A^{-1}=B$. La matriz y el resultado coinciden con la anotación legible del original.

**Explicación — Español.** El algoritmo solo puede llevar el bloque izquierdo a identidad cuando hay dos pivotes de coeficientes. Si aparece una fila nula en ese bloque, no se puede ignorarla para fabricar una inversa.

**中文解释。** “非零矩阵”不等于“可逆矩阵”；是否得到足够多主元，才是这里的判别。

## G-06. Discusión de parámetros — 参数分类（自拟）

**Enunciado.** Discutir en función de $a,b\in\mathbb R$:

$$
x+y+z=1,\qquad x+ay+z=1,\qquad x+y+az=b.
$$

**Análisis — Español.** No se puede dividir por $a-1$ antes de separar su posible anulación.

**分析 — 中文。** 参数不是“通常非零”；如果某个分母可能变零，必须先分类。被除掉的参数值往往正是出现无穷解或无解的地方。

**Resolución.** Restar la primera ecuación a las otras dos produce

$$
\left(\begin{array}{ccc|c}1&1&1&1\\0&a-1&0&0\\0&0&a-1&b-1\end{array}\right).
$$

- Si $a\ne1$, los tres pivotes son no nulos. $y=0$, $z=(b-1)/(a-1)$ y $x=(a-b)/(a-1)$; los dos rangos son $3$.
- Si $a=1$ y $b=1$, las dos últimas filas son cero. Los dos rangos son $1$ y las soluciones son $(1-s-t,s,t)$, con $s,t\in\mathbb R$.
- Si $a=1$ y $b\ne1$, aparece $0=b-1\ne0$. El rango de coeficientes es $1$, el ampliado es $2$ y no hay solución.

**Conclusión y comprobación.** Para $a\ne1$, $x+z=1$, por lo que las dos primeras ecuaciones se cumplen con $y=0$; en la tercera,

$$
x+az=\frac{a-b+a(b-1)}{a-1}=b.
$$

Para $a=b=1$, las tres ecuaciones coinciden y $(1-s-t)+s+t=1$. El caso incompatible queda probado por su fila contradictoria.

**Explicación — Español.** El rango cambia precisamente cuando se anulan los pivotes parametrizados. No hay una sola fórmula válida para todos los valores de los parámetros.

**中文解释。** 这类题应同时交代参数条件、两种秩、解集和回代，而不是只列一个不适用于分母为零情形的分式答案。

继续 [独立练习](05_Ejercicios.md)，或返回 [学习入口](00_Introduccion.md)。
