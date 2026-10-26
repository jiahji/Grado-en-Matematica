---
title: Soluciones de complejos y cuerpos / 复数与域完整解答
subject: Álgebra Lineal
tema: Tema 0 · Guía 1.4
type: exercises
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

# Soluciones de complejos y cuerpos — 完整解答

**Procedencia:** resoluciones propias de [C-E01–C-E12](05_Ejercicios.md), fundadas en [las pruebas del módulo](03_Demostraciones.md).

## C-E01 — Operaciones

**Estrategia — Español.** Distribuir y separar partes; para invertir, usar el módulo al cuadrado.

**策略 — 中文。** 不要把乘法变成两个分量各自相乘；逆元也不是仅仅虚部变号。

**Solución.** $z+w=(2-1)+(-1+3)i=1+2i$.

$$
zw=(2-i)(-1+3i)=-2+6i+i-3i^2=1+7i.
$$

$\bar z=2+i$, $|z|=\sqrt{2^2+(-1)^2}=\sqrt5$ y $z^{-1}=(2+i)/5$.La comprobación $(2-i)(2+i)/5=(4+1)/5=1$ confirma la inversa.

**解释。** 模是非负实数，逆元的模平方分母为 5，不是 $\sqrt5$。

## C-E02 — Ecuación

**Estrategia — Español.** Dividir por $1+i\ne0$ y racionalizar.

**策略 — 中文。** 先写合法除法条件，再乘分母的共轭。

**Solución.**

$$
z=\frac{3-i}{1+i}=\frac{(3-i)(1-i)}2
=\frac{3-4i+i^2}{2}=1-2i.
$$

$(1+i)(1-2i)=1-2i+i-2i^2=3-i$, así que la respuesta está verificada. Es única porque el coeficiente no nulo tiene inverso.

**解释。** 回代证明候选值确实成立，合法的等价除法说明不存在其他解。

## C-E03 — División

**Estrategia — Español.** Usar conjugados de los denominadores y comprobar que sus módulos no se anulan.

**策略 — 中文。** 分母模平方分别为 13 和 10，因此都能除。

**Solución.**

$$
\frac1{2-3i}=\frac{2+3i}{4+9}=\frac{2+3i}{13},
$$

$$
\frac{1+2i}{3-i}=\frac{(1+2i)(3+i)}{9+1}
=\frac{3+7i+2i^2}{10}=\frac{1+7i}{10}.
$$

Multiplicar cada resultado por su denominador devuelve respectivamente $1$ y $1+2i$, porque se ha multiplicado numerador y denominador por el mismo complejo no nulo.

**解释。** 共轭法的正当性来自逆元，不是任意消去复数项。

## C-E04 — Producto por cero

**Hipótesis.** Axiomas de cuerpo y $0\ne1$.

**Tesis.** $a0=0$ y ausencia de inverso de cero.

**Estrategia — Español.** Distribuir y usar opuesto aditivo, después contradicción.

**策略 — 中文。** 先证明乘零，再排除零倒数，推理顺序不能颠倒。

**Demostración.** $a0=a(0+0)=a0+a0$.Al sumar $-(a0)$ a ambos miembros queda $0=a0$.Si $0$ tuviera inverso $u$, $0u=1$, pero el resultado anterior da $0u=0$; entonces $0=1$, contradicción.

**Conclusión y explicación.** $0\ne1$ es la condición que hace imposible la última igualdad. 中文：只写“不能除以零”是规则复述，不是由公理导出的证明。

## C-E05 — Unicidad

**Hipótesis.** $ab=ac=1$ y $a\ne0$ en un cuerpo.

**Tesis.** $b=c$.

**Estrategia — Español.** Insertar una unidad expresada mediante el otro candidato.

**策略 — 中文。** 用定义和结合律比较候选，不假设尚未证明的约去因子规则。

**Demostración.** $b=b1=b(ac)=(ba)c=1c=c$, donde $ba=ab=1$ por conmutatividad.

**Conclusión y explicación.** Todo inverso no nulo es único. 中文：每个等号都来自单位、结合律、交换律或候选逆元条件。

## C-E06 — Módulo y conjugado

**Estrategia — Español.** Comparar las componentes reales y usar cuadrados no negativos.

**策略 — 中文。** 对模平方为零的判断，要用 $a,b$ 是实数这一条件。

**Solución.** $|z|=0\iff a^2+b^2=0\iff a=b=0\iff z=0$, porque ambos cuadrados son no negativos. Asimismo $\bar z=z$ equivale a $a-bi=a+bi$; por igualdad de componentes implica $-b=b$ y por tanto $b=0$.Recíprocamente, si $b=0$, $\bar z=a=z$.Estos son exactamente los reales identificados dentro de $\mathbb C$.

**解释。** “虚部为零”是复数恰好落在实数子集中的精确条件。

## C-E07 — Todas las raíces cuadradas

**Estrategia — Español.** Escribir $z=a+bi$ y separar las dos ecuaciones reales.

**策略 — 中文。** 分支分析不能只挑 $a=0$；还要排除另一个可能分支。

**Solución.** $z^2=(a^2-b^2)+2abi=-4$ equivale a $a^2-b^2=-4$ y $2ab=0$.Si $b=0$, la primera exigiría $a^2=-4$, imposible en $\mathbb R$.Por tanto $a=0$ y $b^2=4$, de donde $b=2$ o $b=-2$.Ambos candidatos $z=\pm2i$ cumplen $z^2=-4$.

**解释。** 列出两根并完成反向验证，才说明没有漏解且两个候选都有效。

## C-E08 — Raíces cuartas

**Estrategia — Español.** Elegir argumento $\pi$ de $-16$ y tomar los cuatro ángulos distintos.

**策略 — 中文。** 先算正模四次方根，再把 $\pi+2k\pi$ 整体除以 4。

**Solución.** El módulo es $16^{1/4}=2$ y los argumentos son $\pi/4$, $3\pi/4$, $5\pi/4$, $7\pi/4$.Los resultados cartesianos son

$$
\sqrt2+i\sqrt2,\quad-\sqrt2+i\sqrt2,\quad
-\sqrt2-i\sqrt2,\quad\sqrt2-i\sqrt2.
$$

Tienen partes reales e imaginarias con cuatro pares distintos de signos, luego son distintos. Al elevar a la cuarta potencia, cada módulo es $16$ y cada argumento es un múltiplo impar de $\pi$, por lo que todos dan $-16$.La fórmula general demuestra que no hay más.

**解释。** 只写正实数的 $\sqrt[4]{16}=2$ 并没有解决复数方根问题。

## C-E09 — Sistema

**Estrategia — Español.** Restar $i$ veces la primera fila a la segunda.

**策略 — 中文。** $i^2=-1$ 改变消元系数，不能把它误算成 $1$。

**Solución.**

$$
\left(\begin{array}{cc|c}1&i&1\\i&1&0\end{array}\right)
\xrightarrow{F_2\leftarrow F_2-iF_1}
\left(\begin{array}{cc|c}1&i&1\\0&2&-i\end{array}\right).
$$

$y=-i/2$, $x=1-iy=1-1/2=1/2$.Comprobando: $x+iy=1/2+i(-i/2)=1$ y $ix+y=i/2-i/2=0$.Hay dos pivotes no nulos y la solución es única.

**解释。** 这里的中间系数为 $1-i^2=2$，完整写出这一步能避免最常见的符号错误。

## C-E10 — Una regla que no se extiende

**Estrategia — Español.** Evaluar ambos miembros con las elecciones de raíces indicadas.

**策略 — 中文。** 反例必须固定根的约定，不能在等式两边临时换不同根。

**Solución.** $\sqrt{(-1)(-1)}=\sqrt1=1$, mientras que $\sqrt{-1}\sqrt{-1}=i^2=-1$.Luego no vale en general la regla $\sqrt{zw}=\sqrt z\sqrt w$ para raíces complejas principales. Para números reales no negativos sí vale con sus raíces no negativas; ese dominio no incluye el par usado en el contraejemplo.

**解释。** 失败的是无条件推广，不是实数非负范围内的原定理。

## C-E11 — Matrices que no forman un cuerpo

**Hipótesis.** $n\ge2$ y operaciones matriciales usuales.

**Tesis.** $M_{n\times n}(\mathbb R)$ no es cuerpo.

**Estrategia — Español.** Usar la matriz $N$ con única entrada no nula $N_{12}=1$.

**策略 — 中文。** 两个非零因子乘积为零，与已证的域性质矛盾，足以否定域结构。

**Demostración.** En $N^2$, un producto de entradas solo podría ser no nulo si el índice interno fuera a la vez $2$ y $1$, imposible. Así $N^2=0$ pero $N\ne0$.En un cuerpo P3 exigiría que alguno de los dos factores fuera cero. Contradicción. Equivalentemente, si $N$ tuviera inverso, multiplicar $N^2=0$ por él daría $N=0$.

**Conclusión y explicación.** El conjunto no es cuerpo para $n\ge2$。中文：这与矩阵单元的零乘积反例相连；不能只因矩阵有加法和乘法就使用全部标量规则。

## C-E12 — Inverso y conjugado

**Hipótesis.** $z\ne0$.

**Tesis.** $z^{-1}=\bar z\iff |z|=1$.

**Estrategia — Español.** Usar $z\bar z=|z|^2$ y separar ambos sentidos.

**策略 — 中文。** 逆元与共轭相同，是一个有条件的结论，不是除法的通用规则。

**Demostración.** Si $z^{-1}=\bar z$, entonces $1=zz^{-1}=z\bar z=|z|^2$, y como $|z|\ge0$, $|z|=1$.Recíprocamente, si $|z|=1$, la fórmula del inverso da $z^{-1}=\bar z/|z|^2=\bar z$.Para $z=1+i$, el conjugado es $1-i$ y la inversa $(1-i)/2$, distintos.

**Conclusión y explicación.** La equivalencia vale exactamente en el círculo de módulo $1$。中文：模平方分母何时可省略，由这个等价命题精确刻画。

返回 [复习](07_Repaso_Examen.md) 或 [学习入口](00_Introduccion.md)。
