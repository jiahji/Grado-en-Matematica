---
title: Espacios vectoriales y subespacios / 向量空间与子空间
subject: Álgebra Lineal
tema: Guía 2.2
type: theorem
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_2_2
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-012/Temas 1 y 2(1)(2).pdf
updated: 2026-10-26
---

# Espacios vectoriales y subespacios — 向量空间与子空间

**Fuentes verificadas:** AL-AP-012, pp. 3–7. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.

**Organización:** esta unidad integra motivación, definiciones, teoremas, pruebas, conexiones y repaso en un archivo; ejemplos, ejercicios y soluciones se mantienen separados.


## Motivación — 动机

**Español.** Los vectores no tienen que ser flechas: matrices, polinomios y funciones se pueden sumar y escalar con las mismas reglas. La definición abstrae esas reglas; un subespacio conserva una parte del universo sin perder las operaciones.

**中文。** 抽象定义让“平面向量的线性方法”能用在函数和矩阵上。判断时要检查运算是否保持在集合内，而不是只凭图形像一条直线。

## Definición y tipos de operaciones

Un espacio vectorial（向量空间）sobre un cuerpo $\mathbb K$ es un conjunto $V$ con $+:V\times V\to V$ y $\mathbb K\times V\to V$, tal que $(V,+)$ es grupo abeliano y, para $u,v\in V$, $a,b\in\mathbb K$,

$$
a(u+v)=au+av,\quad(a+b)u=au+bu,\quad a(bu)=(ab)u,\quad1u=u.
$$

El grupo abeliano aporta las cuatro primeras leyes de la lista de ocho de AL-AP-012 p. 3: asociatividad y conmutatividad de suma, cero vectorial y opuestos. Hay que distinguir el escalar $0_{\mathbb K}$ del vector $0_V$ y la multiplicación en $\mathbb K$ de la acción de escalares sobre $V$.

Un subespacio（向量子空间）$W\subset V$ es un subconjunto que, con las operaciones restringidas, es espacio vectorial sobre el mismo cuerpo. Se conserva la convención de aula: $\subset$ incluye igualdad. Los casos $\{0_V\}$ y $V$ son subespacios.

## T1. Las seis propiedades básicas de la página 5

**Hipótesis.** $V$ espacio vectorial. **Tesis.** Cero y opuesto únicos; $a0_V=0_V$, $0_{\mathbb K}u=0_V$; $au=0_V$ implica $a=0$ o $u=0_V$; $(-a)u=-(au)=a(-u)$.

**Estrategia ES.** Usar los axiomas y cancelar sumandos; solo dividir por un escalar después de exigir que no sea cero. **策略中文。** 每一条都是公理的结果，不能把它们作为未证明的附加公理来循环使用。

**Demostración.** Si $z,z'$ son ceros, $z=z+z'=z'$. Si $u+v=u+w=0_V$, sumando $-u$ se obtiene $v=w$. Para $a0_V$, distribuir $a(0_V+0_V)=a0_V+a0_V$ y cancelar un sumando da $a0_V=0_V$. Del mismo modo $(0+0)u=0u+0u$ implica $0u=0_V$.

Si $au=0_V$ y $a\ne0$, aplicar $a^{-1}$ da $u=(a^{-1}a)u=a^{-1}0_V=0_V$; el otro caso es $a=0$. Finalmente,

$$
au+(-a)u=(a-a)u=0_V,\quad au+a(-u)=a(u-u)=a0_V=0_V.
$$

La unicidad del opuesto implica las dos igualdades restantes. **Explicación ES.** Se han probado exactamente las propiedades anunciadas, respetando el tipo de cada cero. **中文解释。** 取消标量因子只在非零条件下合法；取消加项则来自向量加法群。**Conclusión.** Todas las reglas de p. 5 se deducen de los ocho axiomas.

## T2. Criterio de subespacio

**Enunciado.** $W$ es subespacio si y solo si $0_V\in W$ y $au+bv\in W$ para cualesquiera $u,v\in W$, $a,b\in\mathbb K$. Equivale al criterio de aula: contener cero y estar cerrado por suma y producto escalar.

**Hipótesis/Tesis.** Probar ambas implicaciones y equivalencia de los criterios. **Estrategia ES.** Recuperar clausura y heredar las igualdades del ambiente. **策略中文。** 不必把结合律等八条重新逐个从头证明，但要说明哪些存在性条件已落在子集内。

**Demostración.** Un subespacio contiene su cero, que por T1 coincide con el de $V$, y sus operaciones dan toda combinación de dos vectores. Recíprocamente, poner $a=b=1$ da clausura de suma; poner $b=0$ da clausura escalar. Para $u\in W$, $-u=(-1)u\in W$. Asociatividad, conmutatividad, distributividades y compatibilidades se heredan porque son las mismas operaciones. El cero está dentro y los opuestos también; se cumplen todos los axiomas. La clausura separada por suma y escalares produce $au+bv$ mediante dos aplicaciones escalares y una suma, probando la última equivalencia.

**Explicación ES.** También basta no vaciedad y clausura bajo todas las combinaciones, pues $0u+0u=0_V$ para un $u$ disponible. La no vaciedad no debe omitirse. **中文解释。** 空集会使关于两向量的全称条件空真，但没有零向量，因此不是子空间。**Conclusión.** El criterio justifica las comprobaciones habituales.

## T3. Sistemas homogéneos y funciones

**Enunciado.** Para $A\in M_{m\times n}(\mathbb K)$, $W=\{x:Ax=0\}$ es subespacio de $\mathbb K^n$. Si $b\ne0$, el conjunto $\{x:Ax=b\}$ no es subespacio, incluso si no está vacío.

**Estrategia ES.** Aplicar el criterio con distributividad matricial. **策略中文。** 先验零，再验证一般组合，而不是试几个数值。

**Demostración.** $A0=0$. Si $Ax=Ay=0$, $A(ax+by)=aAx+bAy=0$, así que el criterio prueba el primer caso. Si $b\ne0$, el cero no satisface $A0=b$; por ello el conjunto no puede ser subespacio. Si es vacío, tampoco contiene cero. **Conclusión.** Los sistemas homogéneos son el ejemplo tipo de p. 6.

La misma lógica punto a punto prueba que $\mathcal F(X,\mathbb K)$ es espacio vectorial: $(f+g)(x)=f(x)+g(x)$ y $(af)(x)=af(x)$; cada axioma evaluado en cualquier $x$ es un axioma del cuerpo. El cero es la función constantemente cero y el opuesto es $x\mapsto-f(x)$. Esta verificación también cubre matrices y sucesiones por coordenadas, como en p. 4.

**Explicación ES.** En los sistemas homogéneos, las ecuaciones respetan toda combinación; con término independiente no nulo ya falla el vector cero. Los conocimientos previos son grupos y cuerpos; la combinación lineal es el paso siguiente, mientras que las operaciones entre subespacios se demostrarán después.

## Conexiones, contraejemplos y repaso

前置 [群与域](../01_Grupos_Cuerpos/01_Teoria_Demostraciones.md)，后续 [线性组合与无关](../03_Combinaciones_Independencia/01_Teoria_Demostraciones.md)。子空间的交和直和将在后续独立证明，不把一般关联误写成这里的逻辑前提。

**Español.** Una recta que no pasa por cero no es subespacio; una unión de subespacios puede no serlo. Debe poder probarse el criterio y cada propiedad de T1 sin «es evidente». **中文。** 自测应包含“子集有相同运算却不封闭”的反例与“包含零但仍非子空间”的反例。见 [例题](04_Ejemplos.md)、[练习](05_Ejercicios.md) 与 [解答](06_Soluciones.md)。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
