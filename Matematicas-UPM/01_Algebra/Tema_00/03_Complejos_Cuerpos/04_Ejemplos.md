---
title: Ejemplos resueltos de complejos / 复数完整例题
subject: Álgebra Lineal
tema: Tema 0 · Guía 1.4
type: example
language: es-zh
status: complete
tags:
- algebra_lineal
- complejos
- cuerpos
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-000/Tema 0(6).pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Ejemplos resueltos de complejos — 完整例题

**Procedencia.** C-01 y C-02 conservan operaciones legibles de AL-AP-000 p. 13; C-03 conserva el sistema de p. 16. Los desarrollos se rehacen y verifican. C-04–C-06 son ampliaciones propias, no preguntas confirmadas de examen.

## C-01. Suma y producto — 课堂运算

**Enunciado.** Calcular $(1+i)+(3-2i)$ y $(1+i)(3-2i)$.

**Análisis — Español.** Sumar partes correspondientes; en el producto distribuir y sustituir $i^2=-1$.

**分析 — 中文。** 虚部系数可以相加，但乘法会产生 $i^2$ 项，不能把两个分量只按位置相乘。

**Resolución.**

$$
(1+i)+(3-2i)=(1+3)+(1-2)i=4-i,
$$

$$
(1+i)(3-2i)=3-2i+3i-2i^2=3+i+2=5+i.
$$

**Conclusión y error — 结论与易错点。** La parte imaginaria de $5+i$ es $1$, no $i$. 中文：$-2i^2=2$，而不是 $-2$；实部与虚部都应整理到最后。

## C-02. Inversos y división — 课堂除法

**Enunciado.** Calcular $1/i$, $1/(1+i)$ y $(3+i)/(1-i)$.

**Análisis — Español.** Los tres denominadores son no nulos. Multiplicar por su conjugado y dividir por el módulo al cuadrado.

**分析 — 中文。** 先检查非零条件，再对分子与分母同乘共轭，不能只把分母变成共轭而不改分子。

**Resolución.**

$$
\frac1i=\frac{-i}{i(-i)}=-i,\qquad
\frac1{1+i}=\frac{1-i}{(1+i)(1-i)}=\frac{1-i}{2},
$$

$$
\frac{3+i}{1-i}=\frac{(3+i)(1+i)}{(1-i)(1+i)}
=\frac{3+4i+i^2}{2}=1+2i.
$$

**Comprobación.** $i(-i)=1$, $(1+i)(1-i)/2=1$, $(1-i)(1+2i)=3+i$.

**Explicación — Español.** Conjugar sirve para crear un denominador real; la división sigue siendo la operación definida por el inverso.

**中文解释。** 相乘回原分子是快速可靠的除法检查。只记“虚部改号”会把共轭和倒数混淆。

## C-03. Sistema complejo — 课堂复系数方程组

**Enunciado original.** Resolver $x-iy=2$, $x+y=i$ en $\mathbb C$.

**Análisis — Español.** Las reglas de Gauss siguen siendo válidas porque $\mathbb C$ es un cuerpo. Se resta la primera ecuación a la segunda.

**分析 — 中文。** 未知量本身是复数；不用先把每个未知量拆成实部、虚部，也能直接在复数域中消元。

**Resolución.**

$$
\left(\begin{array}{cc|c}1&-i&2\\1&1&i\end{array}\right)
\xrightarrow{F_2\leftarrow F_2-F_1}
\left(\begin{array}{cc|c}1&-i&2\\0&1+i&i-2\end{array}\right).
$$

Como $1+i\ne0$,

$$
y=\frac{-2+i}{1+i}=\frac{(-2+i)(1-i)}2
=\frac{-1+3i}{2},\qquad
x=2+iy=\frac{1-i}{2}.
$$

**Comprobación.**

$$
x-iy=\frac{1-i-i(-1+3i)}2=2,\qquad
x+y=\frac{1-i-1+3i}2=i.
$$

**Conclusión.** La solución única es $x=\frac12-\frac12i$, $y=-\frac12+\frac32i$, coincidiendo con la anotación final legible de la p. 16.

**中文解释与易错点。** 在 $\mathbb C$ 中可以除以 $1+i$，但不能把它的逆元误写成 $1-i$ 而忘记除以 2。两个原方程均已回代。

## C-04. Potencias — 极形式算幂（补充）

**Enunciado.** Calcular $(1+i)^8$.

**Análisis — Español.** $|1+i|=\sqrt2$ y puede tomarse argumento $\pi/4$.Aplicar De Moivre y verificar con productos pequeños.

**分析 — 中文。** 直接展开八次幂会出现很多项；极形式把问题化成模的幂与角度乘 8。

**Resolución.**

$$
(1+i)^8=(\sqrt2)^8\bigl(\cos(2\pi)+i\sin(2\pi)\bigr)=16.
$$

Para comprobar, $(1+i)^2=2i$, $(1+i)^4=(2i)^2=-4$ y $(1+i)^8=(-4)^2=16$.

**Conclusión y error — 结论与易错点。** El módulo final es $16$, no $8\sqrt2$. 中文：模要乘方，辐角才乘整数；两者的规则不同。

## C-05. Todas las raíces cúbicas — 全部三次方根（补充）

**Enunciado.** Resolver $w^3=8$ en $\mathbb C$.

**Análisis — Español.** Escribir $8=8(\cos0+i\sin0)$ y conservar los tres valores distintos de argumento tras dividir por $3$.

**分析 — 中文。** 实数根 2 只是其中一个；必须保留整圈角度项，才能找全复数根。

**Resolución.** El módulo de cada raíz es $8^{1/3}=2$.Los argumentos son $0$, $2\pi/3$ y $4\pi/3$, por lo que

$$
w_0=2,\qquad w_1=-1+i\sqrt3,\qquad w_2=-1-i\sqrt3.
$$

Cada candidato elevado al cubo tiene módulo $8$ y argumento múltiplo entero de $2\pi$.Los argumentos iniciales son distintos módulo $2\pi$; por el teorema de raíces no falta ninguna.

**Explicación — Español.** Se comprueban existencia, distinción y exhaustividad; repetir $k=3$ daría de nuevo $w_0$, no una cuarta raíz.

**中文解释。** 这些根在平面上均匀分布，但“画出三点”本身不能证明没有遗漏；完备性来自已证的根公式。

## C-06. Qué conjunto es un cuerpo — 域与非域

**Enunciado.** Explicar por qué $\mathbb N$ y $\mathbb Z$ no son cuerpos, mientras que los inversos complejos calculados antes sí pertenecen a $\mathbb C$.

**Análisis — Español.** Para refutar una lista de axiomas basta identificar un axioma y un elemento que lo incumpla; para demostrar un cuerpo hay que verificar todos.

**分析 — 中文。** 一个反例可以否定域结构，但几个成功除法例子不能证明全部公理成立。

**Resolución.** En $\mathbb N$ no hay $n$ con $1+n=0$, por lo que falla el axioma de opuesto aditivo. En $\mathbb Z$ no hay entero $k$ con $2k=1$, por lo que falla la inversión multiplicativa no nula. En $\mathbb C$, para cualquier $a+bi\ne0$, $(a-bi)/(a^2+b^2)$ vuelve a tener componentes reales y es inverso; las restantes leyes se verifican en la demostración completa P4.

**Conclusión.** Las obstrucciones son distintas en $\mathbb N$ y $\mathbb Z$。中文：区分失败的具体公理，比只背“这些集合不是域”更能训练结构判断。

继续 [独立练习](05_Ejercicios.md)，返回 [学习入口](00_Introduccion.md)。
