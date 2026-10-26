---
title: Propiedades de cuerpos y complejos / 域与复数的性质
subject: Álgebra Lineal
tema: Tema 0 · Guía 1.4
type: theorem
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

# Propiedades de cuerpos y complejos — 性质与定理

**Fuentes:** operaciones y cuerpos en AL-AP-000 pp. 11–15; propiedades generales, módulo y raíces desarrollados como suplemento del apartado oficial 1.4. [Pruebas completas](03_Demostraciones.md).

## T1. Elementos distinguidos y cancelación — 唯一性与消去

En un cuerpo son únicos $0$, $1$, el opuesto de cada elemento y el inverso de cada elemento no nulo. Para cualesquiera $a,b,c$:

$$
a0=0,\qquad ab=0\Longrightarrow a=0\text{ o }b=0.
$$

Si $a\ne0$, $ab=ac$ implica $b=c$. El cero no tiene inverso.

**Español.** Estas propiedades justifican dividir por un pivote no nulo y simplificar fracciones. La hipótesis no nula se usa para disponer de un inverso; no es una condición decorativa.

**中文。** 矩阵一般不满足非零标量的这些性质。之前的非零矩阵平方为零反例说明，不能把“能写乘法”的对象都当作域内的数。

## T2. Los complejos forman un cuerpo — 复数构成域

Con las operaciones por pares definidas en este módulo, $\mathbb C$ es un cuerpo, $\mathbb R$ se identifica con el subconjunto $\{a+0i\}$, y todo $a+bi\ne0$ tiene inversa $(a-bi)/(a^2+b^2)$.

**Español.** La afirmación incluye verificar asociatividad, distributividad y todos los axiomas, no únicamente calcular $i^2=-1$.

**中文。** 拓展系统后要检查运算整体相容，不能只验证几个漂亮例子。完整的公理检验见证明 P4。

## T3. Conjugación y módulo — 共轭与模

Para $z,w\in\mathbb C$:

$$
\overline{z+w}=\bar z+\bar w,\quad\overline{zw}=\bar z\bar w,\quad
\overline{\bar z}=z,\quad z\bar z=|z|^2,\quad |zw|=|z||w|.
$$

Además, $|z|=0$ si y solo si $z=0$ y $|z+w|\le|z|+|w|$.

**Español.** El módulo mide una longitud real no negativa; no es una relación de orden entre complejos. La identidad $z\bar z=|z|^2$ explica la racionalización del denominador.

**中文。** 模是实数，可比较大小；一般复数本身不能像实数那样用一个与域运算相容的线性大小顺序处理。除法时乘共轭，是把分母变成一个严格正的实数。

## T4. Producto polar y De Moivre — 极形式乘法与幂

Si $z=r(\cos\theta+i\sin\theta)$ y $w=s(\cos\varphi+i\sin\varphi)$ son no nulos, entonces

$$
zw=rs\bigl(\cos(\theta+\varphi)+i\sin(\theta+\varphi)\bigr).
$$

Para $n\ge0$ entero,

$$
z^n=r^n(\cos(n\theta)+i\sin(n\theta)).
$$

**Español.** En el producto se multiplican módulos y se suman argumentos. La fórmula para potencias se prueba por inducción y no depende de escoger el argumento principal.

**中文。** 绕原点的角度在乘法下相加，长度相乘；极形式把重复乘法化成简单的整数倍角。角度相差整圈表示同一复数。

## T5. Todas las raíces — 全部方根

Sea $z=r(\cos\theta+i\sin\theta)\ne0$ y $n\ge1$. Sus raíces $n$-ésimas son exactamente los $n$ complejos distintos

$$
w_k=r^{1/n}\left(\cos\frac{\theta+2k\pi}{n}+i\sin\frac{\theta+2k\pi}{n}\right),\quad k=0,\ldots,n-1.
$$

El cero tiene una sola raíz $n$-ésima como valor: $0$.

**Español.** Hay que probar que los valores propuestos funcionan, que son distintos y que no falta ninguno. Esta afirmación resuelve potencias puras; no sustituye una prueba del teorema fundamental del álgebra para polinomios generales.

**中文。** 列出 $n$ 个式子还不够，需要证明它们互不重复，并且任意根都能写成其中一个。本文不借此声称任意多项式的全部理论已经建立。

## Uso y errores — 应用与误区

Las propiedades sirven para dividir, resolver sistemas complejos, calcular potencias y enumerar raíces. Errores típicos: considerar $bi$ como parte imaginaria; invertir cero; olvidar dividir por $|z|^2$ al usar el conjugado; usar un solo argumento como si fuera único; perder raíces; aplicar una regla real de raíces cuadradas sin sus condiciones.

中文：这些错误分别涉及对象、定义域、比例、周期性与定理前提，应在解题中逐项检查。继续 [证明](03_Demostraciones.md)。
