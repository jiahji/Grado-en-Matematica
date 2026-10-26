---
title: Autovalores y polinomio característico / 特征值与特征多项式
subject: Álgebra Lineal
tema: Guía 4.1
type: theorem
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_4_1
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Autovalores y polinomio característico — 特征值与特征多项式

**Fuentes verificadas:** AL-GD-001 p. 6, 4.1; suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.

**Organización:** esta unidad integra motivación, definiciones, teoremas, pruebas, conexiones y repaso en un archivo; ejemplos, ejercicios y soluciones se mantienen separados.


## Motivación y definición

**Español.** Una dirección propia no mezcla otras direcciones al aplicar un endomorfismo: solo se escala. Encontrar suficientes direcciones así simplifica la dinámica de iteraciones. **中文。** 特征向量必须非零，否则零向量会对每个标量满足同一等式，失去区分意义。

Sea $T:V\to V$ un endomorfismo lineal, $\dim V=n\ge1$, sobre $\mathbb K$. Un autovalor（特征值）$\lambda\in\mathbb K$ tiene algún $v\ne0$ con $T(v)=\lambda v$; tal $v$ es autovector（特征向量）. El autoespacio（特征空间）es $E_\lambda=\ker(T-\lambda I)$ e incluye cero, aunque cero no sea autovector. Para una matriz $A$ de $T$,

$$
\chi_A(t)=\det(tI-A)
$$

es el polinomio característico（特征多项式）. Se fija esta convención mónica, no $\det(A-tI)$, que difiere por $(-1)^n$.

## T1. Criterio de raíz e invariancia

**Hipótesis.** $A$ cuadrada sobre $\mathbb K$. **Tesis.** $\lambda$ es autovalor si y solo si $\chi_A(\lambda)=0$; la característica y los autovalores no dependen de la base.

**Estrategia ES.** Conectar núcleo no nulo, singularidad y determinante; después aplicar semejanza. **策略中文。** 必须把多项式根限制在当前标量域中。

**Demostración.** Existe $v\ne0$ con $(A-\lambda I)v=0$ exactamente cuando esa matriz es singular por Gauss. Por 3.7 equivale a determinante cero, y cambiar signo a las $n$ columnas no cambia su anulación; es $\chi_A(\lambda)=0$. Si $A'=P^{-1}AP$, $tI-A'=P^{-1}(tI-A)P$. Multiplicatividad de determinante da $\chi_{A'}=\chi_A$. Además $Av=\lambda v$ se transforma en $A'(P^{-1}v)=\lambda(P^{-1}v)$; este vector es no nulo porque $P$ es invertible. **Conclusión.** El criterio y la invariancia son estructurales. **中文解释。** 求根只是找候选特征值；每个值还应解对应核，列出非零特征向量。

## T2. Grado, traza y determinante

**Enunciado.** $\chi_A$ es mónico de grado $n$, su coeficiente de $t^{n-1}$ es $-\operatorname{tr}A$ y su término constante es $(-1)^n\det A$.

**Estrategia ES.** Examinar grados en la expansión de Leibniz. **策略中文。** 不能只用二维公式猜测任意维结论。

**Demostración.** El término de la permutación identidad es $\prod_i(t-a_{ii})$, con coeficientes superiores $1$ y $-\sum_i a_{ii}$. Toda permutación distinta mueve al menos dos índices, por lo que su producto usa al menos dos entradas fuera de diagonal, que no contienen $t$; su grado es a lo sumo $n-2$. No altera esos dos coeficientes. El término constante se obtiene evaluando $t=0$: $\det(-A)=(-1)^n\det A$. **Conclusión.** Las tres fórmulas proporcionan comprobaciones independientes de un cálculo.

## T3. Vectores de valores distintos son independientes

**Hipótesis.** $v_i\ne0$ con $T(v_i)=\lambda_i v_i$, valores $\lambda_i$ distintos. **Tesis.** $v_1,\ldots,v_r$ independientes.

**Estrategia ES.** Aplicar $T-\lambda_r I$ a una relación y usar inducción. **策略中文。** 用算子消去最后一个方向，再利用各特征值差非零。

**Demostración.** Para un vector la afirmación sigue de ser no nulo. Suponga probada para $r-1$ y considere $\sum_{i=1}^r a_iv_i=0$. Aplicar $T-\lambda_r I$ produce $\sum_{i<r}a_i(\lambda_i-\lambda_r)v_i=0$. Por inducción todos esos coeficientes son cero; las diferencias no nulas dan $a_i=0$ para $i<r$. La relación original queda $a_rv_r=0$, así $a_r=0$. **Conclusión.** Un endomorfismo en dimensión $n$ tiene a lo sumo $n$ autovalores distintos. **中文解释。** 并不要求同一特征空间内所有不同向量也无关。

## El cuerpo y la factorización

En $\mathbb R$, $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ tiene característica $t^2+1$ sin raíz real, aunque sobre $\mathbb C$ tiene $\pm i$. En $\mathbb Q$, $t^2-2$ tampoco tiene raíces en el cuerpo, aunque sí en $\mathbb R$. Toda afirmación posterior que usa un polinomio «escindido» exige que se factorice en lineales en el cuerpo seleccionado. Sobre $\mathbb C$ esa factorización está garantizada por el teorema fundamental del álgebra, resultado externo de teoría de polinomios/análisis cuya demostración no se atribuye ni se da por realizada aquí; los teoremas lineales se demostrarán bajo su hipótesis explícita de escisión.

前置 [行列式](../../Tema_04/03_Determinantes_Multilineales/01_Teoria_Demostraciones.md)。后续 [重数](../02_Autoespacios_Multiplicidades/01_Teoria_Demostraciones.md)。自测 ES: calcular característica, verificar coeficientes y resolver cada núcleo. 中文：区分多项式根、非零特征向量和包含零的特征空间。[例题](04_Ejemplos.md)、[练习](05_Ejercicios.md)、[解答](06_Soluciones.md)。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
