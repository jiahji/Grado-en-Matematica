---
title: Funciones de matrices y dinámica discreta / 矩阵函数与离散动力系统 — soluciones
subject: Álgebra Lineal
tema: Guía 4.6
type: exercises
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_4_6
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Soluciones — Funciones y dinámica

**Fuentes verificadas:** AL-GD-001 p. 6, 4.6; suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Son resoluciones propias. [Enunciados sin respuestas](05_Ejercicios.md).

## A46-E01

**Estrategia ES.** Evaluar la definición por serie o por polinomio mínimo, y distinguir la operación entrada a entrada.

**中文策略。** 零矩阵的所有正整数次幂都为零，但零次幂仍是恒等矩阵。

**Solución.** La serie matricial es $I+0+0+\cdots=I_2$. También, $\mu_0(t)=t$ y el interpolador de $e^t$ módulo $t$ es la constante $1$, que da $I_2$. La operación entrada a entrada produce $\begin{pmatrix}1&1\\1&1\end{pmatrix}$, distinta de $I_2$. La primera respeta el cálculo polinómico y la condición $e^{0A}=I$; la segunda es otra operación.

**Conclusión y error ES / 中文。** La exponencial matricial es $I_2$。不能将函数符号直接解释为对每个位置分别运算。

## A46-E02

**Estrategia ES.** Usar $J=\lambda I+N$, donde $N^2=0$, y tratar la potencia cero antes de dividir por $\lambda$.

**中文策略。** 将幂公式的适用条件写清楚，尤其避免 $k=0$ 时无意写出 $0^{-1}$。

**Solución.** Siempre $J^0=I$. Si $\lambda\ne0$ y $k\geq1$,

$$
J^k=\begin{pmatrix}\lambda^k&k\lambda^{k-1}\\0&\lambda^k\end{pmatrix}.
$$

Se deduce del binomio porque solo sobreviven $N^0$ y $N^1$. Si $\lambda=0$, $J^1=N$ y $J^k=0$ para $k\geq2$. Así, para $k=0$ obtenemos $I$; para $k=1$, la matriz dada; para $k=2$, $\begin{pmatrix}\lambda^2&2\lambda\\0&\lambda^2\end{pmatrix}$, que también es cero cuando $\lambda=0$. La multiplicación directa de $J$ por sí misma confirma este último resultado.

**Conclusión y error ES / 中文。** El caso nilpotente se resuelve sin expresiones indeterminadas。不能把含负指数的形式无条件延伸到零特征值。

## A46-E03

**Estrategia ES.** Calcular $N^2,N^3$ y truncar la serie exactamente.

**中文策略。** 这里截断是精确等式，不是数值近似，因为三次及以上的幂确实为零。

**Solución.** $N^2$ solo tiene un $1$ en la posición $(1,3)$ y $N^3=0$. Luego

$$
e^{tN}=I+tN+\frac{t^2}{2}N^2
=\begin{pmatrix}1&t&t^2/2\\0&1&t\\0&0&1\end{pmatrix}.
$$

En el producto de las dos expresiones, los términos de orden uno dan $(s+t)N$, los de orden dos dan $(s^2/2+st+t^2/2)N^2=(s+t)^2N^2/2$ y los restantes contienen $N^3$ o potencias superiores, que son cero. Así el producto es $e^{(s+t)N}$.

**Conclusión y error ES / 中文。** La ley se ha verificado para estas matrices, que son funciones de un mismo $N$。不能从此推断任意两个不交换矩阵都满足同一指数乘法公式。

## A46-E04

**Estrategia ES.** Calcular las órbitas o las potencias; la acotación y el límite son preguntas diferentes.

**中文策略。** 对每个矩阵分别检查三项，不能把“没有增长”直接视为“趋于零”。

**Solución.**

- $A_1^k=\operatorname{diag}(2^{-k},(-1/3)^k)\to0$. Se cumplen (a), (b) y (c); el operador límite es cero.
- $A_2^k=\operatorname{diag}(1,2^{-k})\to\operatorname{diag}(1,0)$. Se cumplen (b) y (c), pero (a) falla para $x_0=(1,0)^T$, cuya órbita es constante no nula.
- $A_3^2=-I$ y $A_3^4=I$, así que todas las órbitas son periódicas y acotadas: se cumple (b). Para $x_0=(1,0)^T$ se recorren $(1,0),(0,1),(-1,0),(0,-1)$; no hay límite ni decaimiento. Fallan (a) y (c).
- $A_4^k=\begin{pmatrix}1&k\\0&1\end{pmatrix}$. Para $x_0=(0,1)^T$ la órbita $(k,1)^T$ es no acotada. Fallan las tres propiedades universales.

**Conclusión ES.** El segundo y el tercer ejemplo separan convergencia de decaimiento y acotación de convergencia, respectivamente.

**中文解释及易错点。** 对最后一项仍有不动向量 $(1,0)^T$，所以“并非所有轨道有界”不能改写成“所有轨道无界”。

## A46-E05

**Estrategia ES.** Usar $x_k=(u_{k+1},u_k)^T$ y descomponer el estado inicial en una base propia.

**中文策略。** 特征根给出两种模式，而两个初值决定它们的系数。

**Solución.** La matriz es $A=\begin{pmatrix}3&-2\\1&0\end{pmatrix}$ y $x_0=(1,0)^T$. Su polinomio característico es $t^2-3t+2=(t-2)(t-1)$. Los vectores $(2,1)^T$ y $(1,1)^T$ son propios de valores $2$ y $1$, pues al multiplicar se obtienen $(4,2)^T$ y $(1,1)^T$. Resolver $x_0=a(2,1)^T+b(1,1)^T$ da $a=1,b=-1$. Por tanto $x_k=2^k(2,1)^T-(1,1)^T$ y $u_k=2^k-1$. Se verifica $u_0=0,u_1=1$, y

$$
3(2^{k+1}-1)-2(2^k-1)=2^{k+2}-1=u_{k+2}.
$$

La unicidad de la recurrencia con esos datos concluye la demostración.

**Conclusión y error ES / 中文。** $u_k=2^k-1$ para todo $k\geq0$。若错放初始向量，得到的仍可能满足递推式，却不满足本题初值。

## A46-E06

**Estrategia ES.** Usar $f(\lambda)=1/\lambda$ y $f'(\lambda)=-1/\lambda^2$.

**中文策略。** 最小多项式至多二次，故只需要函数值和一阶导数；乘回去验证可逆性是必要检查。

**Solución.** La fórmula del bloque da $J^{-1}=\lambda^{-1}I-\lambda^{-2}N$. Multiplicando,

$$
(\lambda I+N)(\lambda^{-1}I-\lambda^{-2}N)
=I-\lambda^{-1}N+\lambda^{-1}N-\lambda^{-2}N^2=I.
$$

El producto en el orden contrario es igual porque ambos factores son polinomios en $N$. Si $\lambda=0$, $J=N$ es nilpotente y singular: $N^2=0$ y, si fuera invertible, al multiplicar $N^2=0$ por su inversa dos veces se obtendría $I=0$, imposible en dimensión positiva. Además $1/z$ no está definida en el autovalor cero.

**Conclusión y error ES / 中文。** La restricción $\lambda\ne0$ es esencial。不能只代入形式而忽略分母函数的定义域。

## A46-E07

**Estrategia ES.** Las coordenadas en la base propia separan crecimiento y decaimiento; el primer coeficiente debe anularse.

**中文策略。** 先求初值在特征基下的坐标，而不是查看标准坐标某项是否为零。

**Solución.** $P^{-1}=\begin{pmatrix}0&1\\1&-1\end{pmatrix}$ y

$$
A=\begin{pmatrix}1/2&3/2\\0&2\end{pmatrix}.
$$

Para $x_0=(u,v)^T$, sus coordenadas propias son $(v,u-v)^T$. Así

$$
A^kx_0=2^k v\begin{pmatrix}1\\1\end{pmatrix}+2^{-k}(u-v)\begin{pmatrix}1\\0\end{pmatrix}.
$$

Si $v=0$, la órbita tiende a cero. Si $v\ne0$, su segunda coordenada es $2^kv$, no acotada. Por tanto los estados que decaen son exactamente $\operatorname{span}\{(1,0)^T\}$. Hay estados no nulos en este subespacio; refutan la afirmación propuesta.

**Conclusión ES.** El modo expansivo impide el decaimiento universal, pero deja un subespacio estable de estados particulares.

**中文解释及易错点。** 谱条件的量词必须保留：存在不稳定特征值，推出存在不衰减初值，而非所有非零初值都不衰减。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
