---
title: Soluciones de los ejercicios de matrices / 矩阵练习完整解答
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

# Soluciones — 矩阵练习完整解答

**Procedencia:** resolución propia de los ejercicios M-E01–M-E12 del [archivo de enunciados](05_Ejercicios.md). Las reglas usadas se prueban en [Demostraciones](03_Demostraciones.md). No se trata de soluciones oficiales del profesor.

## M-E01 — Dimensiones

**Estrategia — Español.** Comparar columnas del factor izquierdo con filas del derecho; conservar las dimensiones exteriores.

**思路 — 中文。** 不按元素总数判断。对三项乘积，还要分别检查中间结果的大小。

**Solución.** $AB\in M_{2\times4}$, $BC\in M_{3\times2}$ y $CA\in M_{4\times3}$. $BA$ no existe porque $4\ne2$; $AC$ no existe porque $3\ne4$.

Para $ABC$, $(AB)C$ tiene tamaño $(2\times4)(4\times2)=2\times2$, mientras que $A(BC)$ tiene tamaño $(2\times3)(3\times2)=2\times2$. Para $CAB$, $(CA)B$ tiene tamaño $(4\times3)(3\times4)=4\times4$, mientras que $C(AB)$ tiene tamaño $(4\times2)(2\times4)=4\times4$. La asociatividad garantiza la igualdad de las agrupaciones correspondientes.

**解释与易错点。** 判断 $BA$ 时不能因为 $AB$ 存在就直接通过；“三项结果大小相同”本身也不是结合律证明。

## M-E02 — Igualdad

**Estrategia — Español.** Igualar las cuatro entradas correspondientes.

**思路 — 中文。** 每个位置给出一个条件，重复的恒等式不增加约束。

**Solución.** La igualdad equivale a $a+1=4$, $2b=-6$, $c-d=0$ y $3=3$. Por tanto $a=3$, $b=-3$, $c=d=t$, donde $t\in\mathbb R$ es arbitrario. Recíprocamente, al sustituir estos valores coinciden las cuatro entradas. Las soluciones son exactamente $(a,b,c,d)=(3,-3,t,t)$。

**解释与易错点。** $c=d$ 不是 $c=d=0$；相等条件允许一个自由参数。应回代证明所有这些取值都有效。

## M-E03 — Combinación matricial

**Estrategia — Español.** Multiplicar cada entrada antes de restar.

**思路 — 中文。** 两矩阵同为 $2\times2$，因此加法定义适用；减去负元素时注意符号。

**Solución.**

$$
2A=\begin{pmatrix}4&-2\\0&6\end{pmatrix},\quad
3B=\begin{pmatrix}-3&6\\12&0\end{pmatrix},\quad
2A-3B=\begin{pmatrix}7&-8\\-12&6\end{pmatrix}.
$$

El resultado es $2\times2$, y su entrada $(1,1)$ es $4-(-3)=7$。

**解释与易错点。** 数乘和相减不改变大小；矩阵的负号作用于全部元素。

## M-E04 — Producto rectangular

**Estrategia — Español.** Calcular primero cada producto con dimensiones compatibles y comparar al final.

**思路 — 中文。** 左右两条计算路线分别进行，避免把一个尚未检验的结果复制到另一边。

**Solución.**

$$
AB=\begin{pmatrix}
1\cdot2+0\cdot0+2\cdot1&1\cdot1+0(-1)+2\cdot2\\
(-1)2+3\cdot0+1\cdot1&(-1)1+3(-1)+1\cdot2
\end{pmatrix}
=\begin{pmatrix}4&5\\-1&-2\end{pmatrix}.
$$

Además,

$$
Bx=\begin{pmatrix}4\\-2\\5\end{pmatrix},\quad
A(Bx)=\begin{pmatrix}4+0+10\\-4-6+5\end{pmatrix}
=\begin{pmatrix}14\\-5\end{pmatrix},\quad
(AB)x=\begin{pmatrix}4+10\\-1-4\end{pmatrix}
=\begin{pmatrix}14\\-5\end{pmatrix}.
$$

Se verifica la igualdad en este caso. La prueba general exige matrices arbitrarias y se da en P4 del archivo de demostraciones.

**解释与易错点。** 一个具体例子只能检验这一组数据，不能把有限次成功当作全称命题的证明。

## M-E05 — Cuadrado de una suma

**Estrategia — Español.** Mantener separados los términos $AB$ y $BA$.

**思路 — 中文。** 错误三项式与正确四项式只在交叉项不同，因此重点检查两个乘法顺序。

**Solución.**

$$
AB=\begin{pmatrix}2&1\\1&1\end{pmatrix},\quad
BA=\begin{pmatrix}1&1\\1&2\end{pmatrix},\quad
(A+B)^2=\begin{pmatrix}2&1\\1&2\end{pmatrix}^2
=\begin{pmatrix}5&4\\4&5\end{pmatrix}.
$$

Como $A^2=\begin{pmatrix}1&2\\0&1\end{pmatrix}$ y $B^2=\begin{pmatrix}1&0\\2&1\end{pmatrix}$,

$$
A^2+2AB+B^2=\begin{pmatrix}6&4\\4&4\end{pmatrix}.
$$

La diferencia entre el cuadrado real y esa expresión es $\operatorname{diag}(-1,1)=BA-AB$, que no es cero.

**解释与易错点。** 两边大小相同且具体元素不同，这是有效反例。不能仅把“矩阵一般不交换”当成这两矩阵确实不交换的计算依据。

## M-E06 — Escalar no nulo

**Hipótesis.** $\lambda\ne0$ y $\lambda A=0$.

**Tesis.** $A=0$.

**Estrategia — Español.** Usar el inverso del escalar, no una inversa matricial.

**策略 — 中文。** 域中每个非零标量都有乘法逆元，这是能够逐元素约去 $\lambda$ 的依据。

**Demostración.** Para cada $i,j$, $\lambda a_{ij}=0$. Puesto que $\lambda\ne0$, existe $\lambda^{-1}$ en $\mathbb K$. Multiplicando por él obtenemos $a_{ij}=\lambda^{-1}0=0$. Así, todas las entradas de $A$ son cero. Si $\lambda=0$, la matriz $A=(1)\in M_{1\times1}$ satisface $\lambda A=0$ pero no es nula.

**Conclusión y explicación.** La hipótesis $\lambda\ne0$ se usa exactamente para disponer de $\lambda^{-1}$. 中文：这不是“非零矩阵都可约”的证明，乘法对象不同。

## M-E07 — Cancelación falsa

**Estrategia — Español.** Buscar una matriz no nula cuyo cuadrado sea cero.

**思路 — 中文。** 把同一个非零矩阵放在两个因子位置，可以同时完成零乘积反例和错误消去反例。

**Solución.** Sea $N=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ y tómense $A=B=N$, $C=0_{2\times2}$. La entrada $(1,2)$ muestra que $A\ne0$ y $B\ne C$. Las cuatro entradas de $N^2$ son cero: en la primera fila se obtienen $0\cdot0+1\cdot0=0$ y $0\cdot1+1\cdot0=0$; la segunda fila es nula. Por tanto $AB=N^2=0=NC=AC$. Además, $N\ne0$ en ambos factores de $N^2$.

**解释与易错点。** 三个要求都已验证；只写 $AB=AC$ 而不检查 $B\ne C$，不是反例。

## M-E08 — Conmutación con una diagonal

**Estrategia — Español.** Obtener las ecuaciones de las entradas y distinguir si $\alpha-\beta$ es cero.

**思路 — 中文。** 不要在尚未区分参数时除以 $\alpha-\beta$，否则会丢掉重要情形。

**Solución.** Para $X=\begin{pmatrix}a&b\\c&d\end{pmatrix}$,

$$
DX=\begin{pmatrix}\alpha a&\alpha b\\\beta c&\beta d\end{pmatrix},\quad
XD=\begin{pmatrix}\alpha a&\beta b\\\alpha c&\beta d\end{pmatrix}.
$$

La igualdad equivale a $(\alpha-\beta)b=0$ y $(\beta-\alpha)c=0$. Si $\alpha\ne\beta$, resulta $b=c=0$, sin restricción sobre $a,d$; estas matrices diagonales satisfacen la igualdad al sustituir. Si $\alpha=\beta$, las ecuaciones se cumplen para cualquier $a,b,c,d$, por lo que todas las matrices $2\times2$ son solución.

**解释与易错点。** “与一个对角矩阵交换的矩阵必为对角矩阵”需要该对角矩阵的对角元素不同；单位矩阵就是条件缺失的反例。

## M-E09 — Ecuación matricial

**Estrategia — Español.** Restar $A$ y multiplicar por el escalar $1/2$.

**思路 — 中文。** 此处“除以 2”是合法标量数乘；没有对矩阵求逆。

**Solución.** La ecuación equivale a

$$
X=\frac12(3B-A)=\frac12\begin{pmatrix}-5&7\\12&-3\end{pmatrix}
=\begin{pmatrix}-5/2&7/2\\6&-3/2\end{pmatrix}.
$$

La sustitución da

$$
2X+A=\begin{pmatrix}-5&7\\12&-3\end{pmatrix}
+\begin{pmatrix}2&-1\\0&3\end{pmatrix}
=\begin{pmatrix}-3&6\\12&0\end{pmatrix}=3B.
$$

Las transformaciones son reversibles porque $2\ne0$ en $\mathbb R$, así que la solución es única.

**解释与易错点。** 验证一个候选解只证明存在；通过可逆的等价变形才能同时说明没有遗漏其他解。

## M-E10 — Equivalencia

**Hipótesis.** $A,B$ son cuadradas del mismo tamaño.

**Tesis.** La equivalencia del enunciado.

**Estrategia — Español.** Desarrollar el cuadrado y comparar términos cruzados.

**策略 — 中文。** 必须分两个方向；仅证明交换时公式成立，还不够得到“当且仅当”。

**Demostración.** Si $AB=BA$, la distributividad da $(A+B)^2=A^2+AB+BA+B^2=A^2+2AB+B^2$. Recíprocamente, si vale la fórmula abreviada, se compara con el desarrollo de cuatro términos y se obtiene $AB+BA=2AB$. Sumando $-AB$ a ambos lados queda $BA=AB$. Se han cancelado sumandos, nunca factores.

**Conclusión y explicación.** Las dos implicaciones quedan probadas. 中文：此处可取消加项，因为所有矩阵大小相同且加法有逆元。

## M-E11 — Matrices elementales de posición

**Hipótesis.** Los índices $i,j,k,\ell$ pertenecen a $\{1,\ldots,n\}$.

**Tesis.** $E_{ij}E_{k\ell}=\delta_{jk}E_{i\ell}$.

**Estrategia — Español.** Calcular una entrada arbitraria mediante deltas.

**策略 — 中文。** 第一个矩阵只在位置 $(i,j)$ 非零，第二个只在 $(k,\ell)$ 非零；乘积中间指标必须同时等于 $j$ 和 $k$。

**Demostración.** Para cualquier entrada $(p,q)$,

$$
\begin{aligned}
(E_{ij}E_{k\ell})_{pq}
&=\sum_{r=1}^{n}(E_{ij})_{pr}(E_{k\ell})_{rq}\\
&=\sum_{r=1}^{n}\delta_{pi}\delta_{rj}\delta_{rk}\delta_{q\ell}
=\delta_{jk}\delta_{pi}\delta_{q\ell}
=(\delta_{jk}E_{i\ell})_{pq}.
\end{aligned}
$$

Si $j\ne k$, todos los sumandos son cero. Si $j=k$, solo el término $r=j$ puede contribuir. Así se justifican ambas posibilidades y la igualdad de matrices.

**Conclusión y explicación.** La regla se deduce de la definición, sin emplear teorías posteriores. 中文：记住乘积成立的连接条件比机械记忆四个下标更可靠。

## M-E12 — Matrices que conmutan con todas

**Hipótesis.** $X\in M_{n\times n}(\mathbb R)$ conmuta con toda matriz del mismo tamaño.

**Tesis.** $X=\lambda I_n$; demostrar también el recíproco.

**Estrategia — Español.** Conmutar primero con cada $E_{jj}$ para anular las entradas fuera de la diagonal y después con $E_{ij}$ para igualar las entradas diagonales.

**策略 — 中文。** “与所有矩阵交换”是很强的条件，特别包括那些只在一个位置非零的测试矩阵。先消去非对角元，再比较对角元，两个步骤解决不同问题。

**Demostración.** Para cada $j$, la igualdad $XE_{jj}=E_{jj}X$ implica lo siguiente. Si $p\ne j$, su entrada $(p,j)$ da $x_{pj}=0$, pues el miembro derecho tiene nula toda fila distinta de $j$. Si $q\ne j$, su entrada $(j,q)$ da $x_{jq}=0$, pues el miembro izquierdo tiene nula toda columna distinta de $j$. Haciendo variar $j$, todas las entradas fuera de la diagonal son cero, y $X=\operatorname{diag}(d_1,\ldots,d_n)$.

Para $i\ne j$, la entrada $(i,j)$ de $XE_{ij}$ vale $d_i$, y la de $E_{ij}X$ vale $d_j$. La hipótesis obliga a $d_i=d_j$. Por tanto todos los $d_i$ son un mismo escalar $\lambda$ y $X=\lambda I_n$. Para $n=1$ esta última descripción ya se cumple sin comparar índices distintos.

Recíprocamente, si $X=\lambda I_n$, para cualquier $A$ las leyes de identidad y compatibilidad con escalares dan $XA=(\lambda I_n)A=\lambda A=A(\lambda I_n)=AX$.

**Conclusión y explicación.** Se han probado necesidad y suficiencia, incluido $n=1$. 中文：这个结论谈的是“与全部矩阵交换”，与只和某个给定矩阵交换的 M-E08 有本质区别，不能混用量词。

完成后前往 [复习与自测](07_Repaso_Examen.md)，返回 [题目](05_Ejercicios.md) 或 [模块入口](00_Introduccion.md)。
