---
title: Complejos, forma polar y cuerpo / 复数、极形式与域的定义
subject: Álgebra Lineal
tema: Tema 0 · Guía 1.4
type: definition
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

# Complejos, forma polar y cuerpo — 定义

**Fuentes:** AL-AP-000 pp. 10–15; guía 1.4. La construcción por pares y las precisiones lógicas son ampliación rigurosa del material; la parte polar desarrolla la anotación de p. 11.

## 1. Construcción y forma cartesiana — 构造与直角坐标形式

Se define $\mathbb C=\mathbb R^2$ con

$$
(a,b)+(c,d)=(a+c,b+d),\qquad(a,b)(c,d)=(ac-bd,ad+bc).
$$

Se identifica el real $a$ con $(a,0)$ y se define $i=(0,1)$. Entonces $i^2=(-1,0)$ y se escribe $(a,b)=a+bi$, llamado forma cartesiana o binómica（直角坐标形式）. La parte real（实部）es $\operatorname{Re}z=a$ y la parte imaginaria（虚部）es $\operatorname{Im}z=b$, **no** $bi$.

Dos complejos son iguales si y solo si sus partes reales e imaginarias coinciden. El cero es $0+0i$ y la unidad $1+0i$.

**Español.** Escribir $a+bi$ no introduce dos representaciones distintas: la pareja $(a,b)$ determina ambas partes de manera única. Las fórmulas de suma y producto son definiciones que después se comprueban compatibles con las de los reales.

**中文。** 虚部是一个实数 $b$，不是“带着 $i$ 的项”。$i^2=-1$ 在这套构造里是可直接算出的结论，不是用实数平方根规则倒推的假设。

## 2. Conjugado, módulo y división — 共轭、模与除法

Para $z=a+bi$ se define el conjugado（共轭）$\bar z=a-bi$ y el módulo（模）

$$
|z|=\sqrt{a^2+b^2}\in\mathbb R_{\ge0}.
$$

Si $z\ne0$, se demostrará que

$$
z^{-1}=\frac{a-bi}{a^2+b^2}.
$$

Para $w\ne0$, $z/w$ significa $zw^{-1}$.

**Español.** El denominador $a^2+b^2$ es positivo exactamente cuando $z\ne0$. Conjugar no es lo mismo que invertir: el conjugado debe dividirse por el cuadrado del módulo.

**中文。** 共轭保持到原点的距离，改变虚部符号；逆元要让乘积变为 1，因此一般还要除以模平方。零的逆元没有定义。

## 3. Forma polar y argumento — 极形式与辐角

Para $z\ne0$，sea $r=|z|>0$. Un argumento（辐角）de $z$ es un ángulo real $\theta$ tal que

$$
\cos\theta=\frac{a}{r},\qquad\sin\theta=\frac{b}{r}.
$$

Entonces $z=r(\cos\theta+i\sin\theta)$. Todos sus argumentos son $\theta+2k\pi$, $k\in\mathbb Z$. El cero no tiene argumento definido en este sentido.

Una raíz $n$-ésima（$n$ 次方根）de $z$ es un $w$ tal que $w^n=z$, con $n\ge1$ entero. No se identifica una raíz elegida con el conjunto de todas las raíces.

**Español.** Un argumento no es único; si se escoge uno principal, debe declararse el intervalo utilizado. Las fórmulas de raíces deben recuperar todas las soluciones, no solo una.

**中文。** 同一个点可以绕整圈后用不同角度表示；这是根的公式中出现 $2k\pi$ 的原因。本文求根时不需要固定主辐角约定。

## 4. Definición de cuerpo — 域的完整公理

Un cuerpo es un conjunto $\mathbb K$ con operaciones internas $+$ y $\cdot$, elementos $0,1$ distintos y las siguientes propiedades:

1. Para todo $a,b,c\in\mathbb K$, $(a+b)+c=a+(b+c)$ y $a+b=b+a$.
2. Para todo $a\in\mathbb K$, $a+0=a$, y existe $-a\in\mathbb K$ con $a+(-a)=0$.
3. Para todo $a,b,c\in\mathbb K$, $(ab)c=a(bc)$ y $ab=ba$.
4. Para todo $a\in\mathbb K$, $a1=a$; para todo **$a\ne0$**, existe $a^{-1}$ con $aa^{-1}=1$.
5. Para todo $a,b,c\in\mathbb K$, $a(b+c)=ab+ac$.

**Español.** «Operaciones internas» significa que sus resultados pertenecen a $\mathbb K$. La suma permite opuestos para todos los elementos; la multiplicación permite inversos solo para los no nulos. Las condiciones $0\ne1$ y $a\ne0$ no se pueden omitir.

**中文。** 加法逆元与乘法逆元的量词不同：每个元素都有相反数，但只有非零元素要求有倒数。原件 p. 15 的逆元条目没有写清非零条件；本定义补足并保留 [来源问题记录](../../../99_Seguimiento/Errores_Detectados.md)。

$\mathbb Q,\mathbb R,\mathbb C$ son los cuerpos usados en el curso. $\mathbb N$ no es cuerpo porque $1$ no tiene opuesto en él; $\mathbb Z$ no es cuerpo porque $2$ no tiene inverso entero. Tener símbolos de suma y producto no basta para ser un cuerpo.

## 5. Notación y advertencias — 记号与边界

La anotación $\sqrt{-1}=i$ se interpreta escogiendo una raíz; $-i$ también tiene cuadrado $-1$. No se puede extender sin condiciones la identidad real $\sqrt{xy}=\sqrt{x}\sqrt{y}$ a raíces complejas principales. Las pruebas y un contraejemplo están en los archivos siguientes.

继续 [性质](02_Teoremas.md)，返回 [学习入口](00_Introduccion.md)。
