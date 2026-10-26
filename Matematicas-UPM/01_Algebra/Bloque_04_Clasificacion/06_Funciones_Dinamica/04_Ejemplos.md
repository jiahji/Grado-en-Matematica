---
title: Funciones de matrices y dinámica discreta / 矩阵函数与离散动力系统
subject: Álgebra Lineal
tema: Guía 4.6
type: example
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_4_6
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Ejemplos — Funciones y dinámica

**Fuentes verificadas:** AL-GD-001 p. 6, 4.6; suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Todos los ejemplos son de elaboración propia; los niveles indican complejidad didáctica, no frecuencia de examen.

## Ejemplo 1 — básico: una función detecta la cadena

**Enunciado.** Calcule $J^k$ y $e^{tJ}$ para $J=\begin{pmatrix}2&1\\0&2\end{pmatrix}$.

**Análisis ES.** Escribir $J=2I+N$ con $N^2=0$ elimina todos los términos de orden dos o superior.

**中文分析。** 两个对角元素相同并不意味着算子只会整体缩放；超对角线会累计前一步的贡献。

**Resolución.** Para $k\geq1$ el binomio da

$$
J^k=2^kI+k2^{k-1}N=\begin{pmatrix}2^k&k2^{k-1}\\0&2^k\end{pmatrix}.
$$

Para $k=0$ se tiene $J^0=I$, por separado. La fórmula funcional da

$$
e^{tJ}=e^{2t}(I+tN)=e^{2t}\begin{pmatrix}1&t\\0&1\end{pmatrix}.
$$

**Conclusión / 中文解释。** El término fuera de la diagonal es la derivada del escalar correspondiente. 矩阵函数需要谱上的导数数据，不能将上右角的 $1$ 直接代入标量指数。El error de tomar exponenciales de entradas daría incluso entradas inferiores no nulas; contradice $e^{0J}=I$.

## Ejemplo 2 — intermedio: dos bloques y dos comportamientos

**Enunciado.** Compare las órbitas de $A=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ y $B=\begin{pmatrix}1/2&1\\0&1/2\end{pmatrix}$ desde $x_0=(a,b)^T$.

**Análisis ES.** Ambos tienen un bloque no diagonalizable; la diferencia es el módulo del autovalor.

**中文分析。** 非对角化并不自动导致发散。要看多项式增长是否被几何衰减压住。

**Resolución.** Para $k\geq0$, $A^k=\begin{pmatrix}1&k\\0&1\end{pmatrix}$, luego $A^kx_0=(a+kb,b)^T$. Si $b\ne0$, la primera coordenada no está acotada; si $b=0$, la órbita es constante. Para $k\geq1$,

$$
B^kx_0=\begin{pmatrix}2^{-k}a+k2^{1-k}b\\2^{-k}b\end{pmatrix}.
$$

Tanto $2^{-k}$ como $k2^{1-k}$ tienden a cero, así que todas las órbitas de $B$ tienden a cero. Para $k=0$, se conserva $x_0$.

**Conclusión ES.** La afirmación sobre todas las órbitas de $A$ es falsa, aunque algunas convergen; para $B$ es verdadera.

**中文解释及易错点。** 对 $A$，初值是否具有第二个链向量的分量至关重要。不能因为“存在发散轨道”便写“所有非零初值都发散”。

## Ejemplo 3 — universitario: Fibonacci por una base propia

**Enunciado.** Sea $F_0=0$, $F_1=1$ y $F_{k+2}=F_{k+1}+F_k$. Obtenga una fórmula cerrada.

**Análisis ES.** La recurrencia de orden dos se convierte en una de primer orden en $\mathbb R^2$; hay dos autovalores distintos.

**中文分析。** 把“连续两个数”视作一个状态，即可应用同一矩阵的幂。初始状态必须按所选顺序放置。

**Resolución.** Ponga $z_k=(F_{k+1},F_k)^T$ y $A=\begin{pmatrix}1&1\\1&0\end{pmatrix}$. Entonces $z_{k+1}=Az_k$ y $z_0=(1,0)^T$. El polinomio característico es $t^2-t-1$; sus raíces son $\varphi=(1+\sqrt5)/2$ y $\psi=(1-\sqrt5)/2$. Para cada raíz $r$, $A(r,1)^T=(r+1,r)^T=(r^2,r)^T=r(r,1)^T$. Los vectores propios son independientes por corresponder a valores distintos. Resolver

$$
\begin{pmatrix}1\\0\end{pmatrix}=a\begin{pmatrix}\varphi\\1\end{pmatrix}+b\begin{pmatrix}\psi\\1\end{pmatrix}
$$

da $a+b=0$ y $a(\varphi-\psi)=1$, luego $a=1/\sqrt5$, $b=-1/\sqrt5$. Aplicando $A^k$ y leyendo la segunda coordenada,

$$
F_k=\frac{\varphi^k-\psi^k}{\sqrt5}.
$$

Para verificar independientemente, en $k=0$ da $0$ y en $k=1$ da $1$; como $r^{k+2}=r^{k+1}+r^k$ para ambas raíces, la fórmula satisface la recurrencia. Por unicidad coincide con $F_k$ para todo $k\geq0$.

**Conclusión ES.** La descomposición espectral separa dos modos y conserva los datos iniciales.

**中文解释及易错点。** 两个特征值是增长模式，不是两个可任选的答案；必须用初值确定二者的系数。不能遗漏第二个模式，否则不能同时满足两个初值。

## Ejemplo 4 — universitario: interpolar una exponencial

**Enunciado.** Suponga $\mu_A(t)=(t-1)^2(t-2)$. Exprese $e^A$ como polinomio de grado menor que tres en $A$.

**Análisis ES.** Hay que imponer valor y derivada en $1$, y valor en $2$; no basta interpolar solo dos valores.

**中文分析。** 最小多项式中平方因子表示特征值 $1$ 至少有一个长度为 $2$ 的链，所以必须保留导数。

**Resolución.** Escriba $h(t)=a+b(t-1)+c(t-1)^2$. Las condiciones $h(1)=e$, $h'(1)=e$, $h(2)=e^2$ dan $a=e$, $b=e$, $c=e^2-2e$. Por la definición intrínseca,

$$
e^A=eI+e(A-I)+(e^2-2e)(A-I)^2.
$$

**Conclusión / 中文解释。** No se necesita calcular una base de Jordan si ya se conoce $\mu_A$. 此处利用三条局部条件构造唯一余式；只在特征值处插值而漏掉导数，会产生另一个不正确的矩阵函数。

Volver a [teoría](01_Teoria_Demostraciones.md). Practicar en [ejercicios](05_Ejercicios.md).

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
