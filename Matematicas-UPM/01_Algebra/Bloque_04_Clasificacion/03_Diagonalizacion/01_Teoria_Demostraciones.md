---
title: Diagonalización / 对角化
subject: Álgebra Lineal
tema: Guía 4.3
type: theorem
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_4_3
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Diagonalización — 对角化

**Fuentes verificadas:** AL-GD-001 p. 6, 4.3; suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.

**Organización:** esta unidad integra motivación, definiciones, teoremas, pruebas, conexiones y repaso en un archivo; ejemplos, ejercicios y soluciones se mantienen separados.


## Motivación y definición

**Español.** Diagonalizar no es anular entradas por filas: es escoger una base en la que cada dirección básica solo se escala. Se conserva el endomorfismo y cambia su representación por semejanza. **中文。** 矩阵可逆不保证可对角化；化成单位矩阵的消元不属于同一种变换。

$T:V\to V$ es un endomorfismo de dimensión finita. Se dice que $T$ es diagonalizable sobre $\mathbb K$ si alguna base da matriz diagonal. Para una matriz $A$ significa que existe $P$ invertible con $P^{-1}AP=D$ diagonal. El cuerpo se declara siempre.

## T1. Criterios equivalentes

**Enunciado.** Son equivalentes: diagonalización; existencia de una base de autovectores; $V$ es suma directa de sus autoespacios. Si $\chi$ se escinde, equivale también a $g_\lambda=a_\lambda$ para cada raíz.

**Estrategia ES.** Leer las columnas de $AP=PD$ y después contar la base de la suma directa. **策略中文。** 独立的特征方向必须正好填满整个空间。

**Demostración.** Si $P^{-1}AP=D$, entonces $AP=PD$ y la columna $j$ de $P$ satisface $Av_j=d_{jj}v_j$; son una base porque $P$ es invertible. Si existe esa base, ponerla como columnas produce la ecuación y diagonaliza. Por 4.2 las sumas de autoespacios distintos son directas; contienen una base propia exactamente cuando su dimensión $\sum g_\lambda$ es $n$. Esto equivale a que su suma sea todo $V$. Si $\chi$ se escinde, $\sum a_\lambda=n$ y $g_\lambda\le a_\lambda$. La suma geométrica es $n$ exactamente cuando todas las desigualdades son igualdades. A la inversa, una matriz diagonal tiene característica partida en los factores de sus entradas. **Conclusión.** Las condiciones incluyen escisión y plenitud de los espacios propios. **中文解释。** 不可省去“特征值在当前域里”这个条件。

## T2. Valores distintos y potencias

Si hay $n$ valores distintos, tomar un vector de cada uno da $n$ independientes por 4.1 y por tanto base, así diagonaliza. No es condición necesaria: $\lambda I$ es diagonal y tiene un único valor en dimensión mayor que uno.

Si $A=PDP^{-1}$, por inducción $A^k=PD^kP^{-1}$ para $k\ge0$: la base $k=0$ es identidad; el paso cancela $P^{-1}P$ al multiplicar. Para un polinomio $q(t)=\sum c_kt^k$, distribuir da $q(A)=P\operatorname{diag}(q(\lambda_i))P^{-1}$. Para exponentes negativos se requiere además todas las $\lambda_i\ne0$, entonces $A^{-1}=PD^{-1}P^{-1}$ y el mismo argumento vale. **中文解释。** 这为后面的矩阵函数和动态迭代提供计算路线，但不把所有函数自动当作多项式。

## T3. Proyecciones e involuciones

**Enunciado.** Si $T^2=T$, es diagonalizable con valores entre $0,1$. Si $T^2=I$ y el cuerpo tiene característica distinta de $2$, es diagonalizable con valores entre $1,-1$.

**Estrategia ES.** Descomponer cada vector en dos componentes propias explícitas. **策略中文。** 不借用后面的最小多项式判据，先给直接构造。

**Demostración.** Para proyección, $v=(v-Tv)+Tv$, con $T(v-Tv)=0$ y $T(Tv)=Tv$. Los dos autoespacios $E_0,E_1$ tienen intersección cero porque sus valores son distintos; así llenan todo $V$ y T1 aplica. Para involución, escribir

$$
v=\frac{v+Tv}{2}+\frac{v-Tv}{2}.
$$

Aplicar $T$ da respectivamente la misma primera componente y el opuesto de la segunda, usando $T^2v=v$. Las componentes están en $E_1,E_{-1}$ y su intersección es cero. La división por dos está permitida en los cuerpos del curso. **Conclusión.** Ambas clases tienen bases propias construibles. **中文解释。** 某个特征空间可以是零空间，不影响直和分解和对角化。

## Algoritmo y límites

Calcular $\chi$, factorizar en el cuerpo, hallar una base de cada $\ker(A-\lambda I)$ y comprobar que las dimensiones suman $n$. Si sí, concatenar esas bases como columnas de $P$ y poner sus valores correspondientes en $D$; verificar $AP=PD$. Si falta alguna dirección, no se inventan vectores ni se rellena con otros arbitrarios: se requerirá Jordan.

前置 [重数](../02_Autoespacios_Multiplicidades/01_Teoria_Demostraciones.md) 与换基；后续 [Jordan](../04_Jordan/01_Teoria_Demostraciones.md)。自测 ES: distinguir condición suficiente de necesaria y justificar el papel del cuerpo. 中文：重复根可能对角化，也可能不能，必须计算几何重数。[例题](04_Ejemplos.md)、[练习](05_Ejercicios.md)、[解答](06_Soluciones.md)。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
