---
title: Fórmula de Grassmann / Grassmann 维数公式
subject: Álgebra Lineal
tema: Guía 2.7
type: theorem
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_2_7
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-012/Temas 1 y 2(1)(2).pdf
updated: 2026-10-26
---

# Fórmula de Grassmann — Grassmann 维数公式

**Fuentes verificadas:** AL-AP-012, p. 24. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.

**Organización:** esta unidad integra motivación, definiciones, teoremas, pruebas, conexiones y repaso en un archivo; ejemplos, ejercicios y soluciones se mantienen separados.


## Motivación y enunciado

**Español.** Al unir bases de dos subespacios, las direcciones compartidas se cuentan dos veces. La fórmula resta exactamente esa duplicación, no una cantidad deducida de un dibujo particular. **中文。** “两个平面相交于一条线”的图像是例子，不是一般维数公式的证明。

Sean $U,W$ subespacios **de dimensión finita** de un mismo espacio. Entonces $U+W$ también es finito y

$$
\dim(U+W)+\dim(U\cap W)=\dim U+\dim W.
$$

La fórmula es la anunciada en AL-AP-012 p. 24. El requisito finito evita restar cardinales infinitos. No requiere que el ambiente completo sea finito mientras los dos subespacios sí lo sean.

## Demostración completa por bases

**Hipótesis.** $\dim U,\dim W<\infty$. **Tesis.** Igualdad de Grassmann. **Estrategia ES.** Elegir base de la intersección y extenderla dentro de cada subespacio. **策略中文。** 从共同部分开始，新增两组分别代表每边不共享的信息。

**Demostración.** Sea $I=(a_1,\ldots,a_r)$ una base de $U\cap W$. Por el teorema de compleción, se amplía a

$$
B_U=(a_1,\ldots,a_r,u_1,\ldots,u_p),\quad
B_W=(a_1,\ldots,a_r,w_1,\ldots,w_q).
$$

La lista $B=(a_1,\ldots,a_r,u_1,\ldots,u_p,w_1,\ldots,w_q)$ genera $U+W$: se expanden ambos sumandos en sus bases y se reúnen los coeficientes de los $a_i$.

Para independencia, supongamos

$$
\sum_i\alpha_ia_i+\sum_j\beta_ju_j+\sum_k\gamma_kw_k=0.
$$

La suma $u=\sum_j\beta_ju_j$ está en $U$ y, por esa igualdad, también en $W$, pues es el opuesto de una suma de $a_i,w_k$. Luego $u\in U\cap W$ y se escribe $u=\sum_i\delta_ia_i$. Comparar estas dos expresiones en la base $B_U$ obliga a todos los $\beta_j=0$ y $\delta_i=0$. La relación inicial queda entre $a_i,w_k$, una base de $W$, y fuerza todos los $\alpha_i,\gamma_k=0$. Por tanto $B$ es base. Contando,

$$
\dim(U+W)=r+p+q=(r+p)+(r+q)-r,
$$

que es la fórmula. **Explicación ES.** La independencia de la lista concatenada no se ha supuesto: se demuestra mediante la pertenencia de una suma a la intersección. **中文解释。** 恰恰在这一步消除了共享部分可能引起的依赖，不能以“显然是基”跳过。**Conclusión.** Queda probada en todas las dimensiones finitas indicadas, incluso intersección cero o uno de los espacios cero.

## Corolarios y sus condiciones

Si el ambiente tiene dimensión $n$, entonces

$$
\max(0,\dim U+\dim W-n)\le\dim(U\cap W)\le\min(\dim U,\dim W).
$$

**Prueba.** La cota inferior procede de $\dim(U+W)\le n$ en la fórmula y de no negatividad. Las superiores son inclusiones $U\cap W\subset U,W$ y monotonicidad de dimensión. Además, $\dim(U+W)=\dim U+\dim W$ equivale a $U\cap W=0$, pues el único subespacio de dimensión cero es $\{0\}$. Si esa suma de dimensiones vale $n$, la intersección cero equivale a que sean complementarios: Grassmann da suma de dimensión $n$, que por inclusión debe ser todo el ambiente. **中文解释。** 这个补空间快捷判据必须同时知道维数与交集条件。

## Límite: no es inclusión–exclusión de tres subespacios

No se puede sumar simplemente dimensiones individuales y restar intersecciones por parejas para tres o más subespacios. Las tres rectas de $\mathbb R^2$ dadas por $e_1,e_2,e_1+e_2$ tienen intersecciones por parejas y triple cero; esa expresión daría $3$, pero su suma es $\mathbb R^2$ de dimensión $2$. Para tres subespacios, aplicar Grassmann sucesivamente a $(U+W)+Z$, calculando la intersección $(U+W)\cap Z$ completa.

前置 [基与 Steinitz](../../Tema_01/04_Bases_Dimension/01_Teoria_Demostraciones.md) 和 [交与和](../02_Suma_Directa_Complementarios/01_Teoria_Demostraciones.md)。自测 ES: reproducir la prueba de independencia y justificar cada cota. 中文：不把可视化直觉当成高维结论的前提。[例题](04_Ejemplos.md)、[练习](05_Ejercicios.md)、[解答](06_Soluciones.md)。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
