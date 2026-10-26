---
title: Grupos y cuerpos / 群与域
subject: Álgebra Lineal
tema: Guía 2.1
type: theorem
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_2_1
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-012/Temas 1 y 2(1)(2).pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-000/Tema 0(6).pdf
updated: 2026-10-26
---

# Grupos y cuerpos — 群与域

**Fuentes verificadas:** AL-AP-012, p. 2; AL-AP-000 pp. 14–15; estructura de grupo como suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.

**Organización:** esta unidad integra motivación, definiciones, teoremas, pruebas, conexiones y repaso en un archivo; ejemplos, ejercicios y soluciones se mantienen separados.


## Motivación y lenguaje — 动机与语言

**Español.** Antes de sumar vectores hay que saber qué parte de la aritmética depende solo de una operación reversible. Un grupo organiza esa operación; un cuerpo añade una segunda operación compatible para poder usar escalares. No son dos nombres para la misma estructura.

**中文。** 群研究一种运算下的结合、单位与可逆性；域同时组织加法和乘法，并通过分配律连接二者。把零排除出乘法逆元的定义域，不代表把零排除出整个域。

## Definiciones formales — 严格定义

Un **grupo（群）** es un conjunto no vacío $G$ con una operación interna $*:G\times G\to G$ tal que: para cualesquiera $a,b,c$ se cumple $(a*b)*c=a*(b*c)$; existe $e\in G$ con $e*a=a*e=a$ para todo $a$; y para cada $a$ existe $a^{-1}$ con $a*a^{-1}=a^{-1}*a=e$. Es **abeliano（交换群）** si $a*b=b*a$ para todo par. La existencia de inversos no implica conmutatividad.

Un **subgrupo（子群）** $H\le G$ es un subconjunto no vacío que, con la misma operación, es grupo. En notación aditiva se escriben $0$, $-a$ y $a+b$; en multiplicativa, $e$, $a^{-1}$ y $ab$.

Un **cuerpo（域）** $\mathbb K$ tiene operaciones internas $+$ y $\cdot$, con $(\mathbb K,+)$ grupo abeliano, $0\ne1$, $(\mathbb K\setminus\{0\},\cdot)$ grupo abeliano y distributividad $a(b+c)=ab+ac$. Son cuantificadores distintos: todo elemento tiene opuesto, solo los no nulos tienen inverso multiplicativo. La construcción completa de $\mathbb C$ y las consecuencias de estos axiomas se demuestran en [el módulo de cuerpos](../../Tema_00/03_Complejos_Cuerpos/03_Demostraciones.md).

**Español.** La clausura forma parte de «operación interna». No basta efectuar una suma o un cociente en un universo mayor si el resultado sale del conjunto considerado.

**中文。** 判断结构时先确定集合和运算，再逐条核查。相同集合使用不同运算会产生不同结构，例如整数加法是群，整数乘法不是群。

## T1. Unicidad, cancelación y orden de inversos

**Hipótesis.** $G$ grupo, sin suponerlo abeliano. **Tesis.** Neutro e inversos son únicos; $ab=ac$ implica $b=c$ y $ba=ca$ implica $b=c$; $(ab)^{-1}=b^{-1}a^{-1}$.

**Estrategia ES.** Insertar las unidades pertinentes y multiplicar por el inverso por el lado correcto. **策略中文。** 非交换结构中必须区分左乘与右乘；只有括号可以用结合律改变。

**Demostración.** Si $e,f$ son neutros, $e=ef=f$. Si $b,c$ son inversos de $a$, $b=b(ac)=(ba)c=c$. De $ab=ac$, multiplicar a la izquierda por $a^{-1}$ da $(a^{-1}a)b=(a^{-1}a)c$, luego $b=c$; para $ba=ca$ se multiplica a la derecha. Finalmente

$$
(ab)(b^{-1}a^{-1})=a(bb^{-1})a^{-1}=e,
\quad(b^{-1}a^{-1})(ab)=b^{-1}(a^{-1}a)b=e.
$$

La unicidad del inverso prueba la fórmula. **Explicación ES.** No se han intercambiado $a,b$; se invierte el orden para que aparezcan factores adyacentes inversos. **中文解释。** “乘积的逆”若不倒序，通常无法把相应因子相邻配对。**Conclusión.** Se obtiene cancelación legítima por ambos lados y la fórmula general.

## T2. Criterio de subgrupo

**Enunciado.** Un subconjunto no vacío $H\subset G$ es subgrupo si y solo si $xy^{-1}\in H$ para todos $x,y\in H$.

**Hipótesis/Tesis.** La clausura indicada debe equivaler a todos los axiomas heredados. **Estrategia ES.** Recuperar primero neutro e inversos y después productos. **策略中文。** 非空条件提供一个起点，不能把它遗漏。

**Demostración.** Un subgrupo cumple el criterio por sus operaciones internas. Recíprocamente, elija $h\in H$; entonces $hh^{-1}=e\in H$. Para $y\in H$, $ey^{-1}=y^{-1}\in H$. Para $x,y\in H$, como $y^{-1}\in H$, el criterio aplicado a $x,y^{-1}$ da $x(y^{-1})^{-1}=xy\in H$. La asociatividad se hereda de $G$ y el neutro e inversos están dentro de $H$; luego es grupo. **Explicación ES.** La asociatividad no se vuelve a demostrar porque se restringe la misma operación. **中文解释。** 空集会让一个全称封闭条件空真，却没有单位元；所以必须另外要求非空。**Conclusión.** Queda probado el criterio en ambas direcciones.

## Puente con cuerpos y vectores — 与标量及向量的联系

Por los axiomas, $\mathbb Q,\mathbb R,\mathbb C$ tienen grupo aditivo y grupo multiplicativo de no nulos. Para justificar que los no nulos se mantienen al multiplicar, si $ab=0$ y $a\ne0$, multiplicar por $a^{-1}$ fuerza $b=0$, contradicción. En un espacio vectorial la suma de vectores será un grupo abeliano; la multiplicación por escalares es otra operación con entradas de dos conjuntos diferentes, $\mathbb K\times V\to V$.

中文：不要把“向量乘向量”硬加到向量空间公理里。矩阵方阵的可逆元素组成乘法群，但所有矩阵并不构成域。

**Español.** La acción escalar tiene dominio $\mathbb K\times V$ y no es un producto interno de dos vectores. Para el repaso, formular las cuatro estructuras y reconstruir las pruebas de cancelación y subgrupos antes de pasar a espacios vectoriales.

## Repaso y dependencias — 自测与依赖

应能用规范西班牙语给出群、交换群、子群、域定义，证明取消律和子群判别，解释非交换时逆元顺序。前置仅为集合与运算；后续是向量空间。练习 [题目](05_Ejercicios.md) 与 [解答](06_Soluciones.md) 分开，先读 [例题](04_Ejemplos.md)。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
