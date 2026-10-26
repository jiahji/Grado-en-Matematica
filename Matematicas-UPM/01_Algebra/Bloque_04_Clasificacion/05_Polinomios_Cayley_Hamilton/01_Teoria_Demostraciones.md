---
title: Anuladores, Cayley–Hamilton y polinomio mínimo / 零化与最小多项式
subject: Álgebra Lineal
tema: Guía 4.5
type: theorem
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_4_5
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Anuladores, Cayley–Hamilton y polinomio mínimo — 零化与最小多项式

**Fuentes verificadas:** AL-GD-001 p. 6, 4.5; suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.

**Organización:** esta unidad integra motivación, definiciones, teoremas, pruebas, conexiones y repaso en un archivo; ejemplos, ejercicios y soluciones se mantienen separados.


## Motivación y definiciones

**Español.** Una matriz genera una secuencia infinita de potencias, pero esas potencias viven en un espacio finito de matrices. Una relación polinómica permite reducir cualquier cálculo a un número finito de ellas. El polinomio mínimo detecta además los tamaños de las obstrucciones a diagonalizar. **中文。** 特征多项式给出一个零化关系；最小多项式找最短的本质关系，不能把二者不加证明地当成相同。

Para $q(t)=\sum_{j=0}^d c_jt^j$, $q(T)=\sum c_jT^j$, con $T^0=I$. Como $T^iT^j=T^{i+j}$, distribuir demuestra $(pq)(T)=p(T)q(T)$, $(p+q)(T)=p(T)+q(T)$; en particular todos los polinomios en $T$ conmutan. Un anulador es un polinomio no nulo con $q(T)=0$. El polinomio mínimo $\mu_T$ es el anulador mónico de menor grado. Se supone $\dim V=n\ge1$.

El algoritmo de división de polinomios sobre un cuerpo resta múltiplos del divisor para disminuir el grado hasta obtener un resto de grado menor. Iterarlo en dos polinomios reduce grados estrictamente y termina en un máximo común divisor. Revirtiendo las restas se obtiene la identidad de Bézout: si $p,q$ son coprimos, existen $a,b$ con $ap+bq=1$. Estas operaciones justifican los usos del resultado más abajo; no se supone una identidad sin comprobar coprimalidad.

## T1. Existencia, unicidad y divisibilidad del mínimo

**Hipótesis.** Endomorfismo finito $T$. **Tesis.** Existe único $\mu_T$, y $q(T)=0$ equivale a $\mu_T\mid q$ para polinomios no nulos.

**Estrategia ES.** Usar dependencia en End y dividir por el anulador de grado mínimo. **策略中文。** 除法余项若非零就违背最小次数，这给出整除而不仅是存在。

**Demostración.** $\operatorname{End}(V)$ tiene dimensión $n^2$ por 3.8, así $I,T,\ldots,T^{n^2}$ son dependientes y producen un anulador no nulo. Entre sus grados existe un mínimo natural, y se puede normalizar el coeficiente principal a $1$. Dos mínimos mónicos del mismo grado se restan para obtener un anulador de grado menor; por minimalidad la diferencia debe ser cero. Para cualquier $q$, dividir $q=h\mu_T+r$ con $\deg r<\deg\mu_T$. Si $q(T)=0$, también $r(T)=0$, y por minimalidad $r=0$. Si $\mu_T$ divide $q$, la propiedad del producto evaluado da $q(T)=0$. **Conclusión.** Todos los anuladores son exactamente sus múltiplos. **中文解释。** 常数非零多项式在非零空间上给非零倍单位算子，所以最小次数至少为 1。

## T2. Teorema de Cayley–Hamilton con prueba por coeficientes

**Enunciado.** $\chi_T(T)=0$, y por tanto $\mu_T\mid\chi_T$.

**Hipótesis.** Una matriz $A$ de tamaño $n$ y $\chi_A(t)=t^n+c_{n-1}t^{n-1}+\cdots+c_0$. **Estrategia ES.** Usar la identidad de la adjunta polinómica y telescopar coeficientes. **策略中文。** 不把标量变量 $t$ 在含矩阵系数的式子中随意替换成 $A$；明确比较系数可避开这个问题。

**Demostración.** La identidad de cofactores de 3.7 vale también en el anillo conmutativo $\mathbb K[t]$, pues su prueba usa solo sumas y productos, no división. Escriba

$$
B(t)=\operatorname{adj}(tI-A)=\sum_{j=0}^{n-1}B_jt^j.
$$

De $(tI-A)B(t)=\chi_A(t)I$ se obtiene, comparando coeficientes,

$$
-AB_0=c_0I,\quad B_{j-1}-AB_j=c_jI\ (1\le j<n),\quad B_{n-1}=I.
$$

Multiplicar la ecuación de índice $j$ por $A^j$ **a la izquierda** y sumar da

$$
\begin{aligned}
\sum_{j=0}^n c_jA^j
&=-AB_0+\sum_{j=1}^{n-1}(A^jB_{j-1}-A^{j+1}B_j)+A^nB_{n-1}\\
&=0,
\end{aligned}
$$

con $c_n=1$, porque cada término se cancela con el vecino. Esto es Cayley–Hamilton. T1 aplicado al anulador $\chi_A$ da divisibilidad. **Explicación ES.** No se ha supuesto que coeficientes matriciales arbitrarios conmuten; la cancelación mantiene el orden escrito. **中文解释。** 伴随恒等式在多项式环中成立，不意味着可以把多项式矩阵当作处处可逆矩阵。**Conclusión.** El teorema se demuestra, no solo se ilustra numéricamente.

## T3. Raíces y diagonalización mediante el mínimo

**Enunciado.** Los valores propios son exactamente las raíces en $\mathbb K$ de $\mu_T$. $T$ es diagonalizable sobre $\mathbb K$ si y solo si $\mu_T$ es producto de factores lineales distintos en $\mathbb K$.

**Estrategia ES.** Evaluar en autovectores y usar interpoladores que proyectan hacia autoespacios. **策略中文。** 判据需要既无重复因子又在当前域分裂，不能只看无重根。

**Demostración.** Si $Tv=\lambda v$ con $v\ne0$, $\mu_T(T)v=\mu_T(\lambda)v=0$, así $\mu_T(\lambda)=0$. A la inversa, una raíz de $\mu_T$ lo es de $\chi_T$ por divisibilidad y, por 4.1, es valor propio.

Si $T$ es diagonalizable, $q(T)=0$ equivale a que $q$ anule cada entrada diagonal. El polinomio mónico de menor grado con esa propiedad es $\prod_{\lambda\text{ distinta}}(t-\lambda)$: cada raíz obliga un factor por división polinómica, y el producto los anula todos.

Recíprocamente, si $\mu_T=\prod_{i=1}^s(t-\lambda_i)$ con raíces distintas, defina

$$
e_i(t)=\prod_{j\ne i}\frac{t-\lambda_j}{\lambda_i-\lambda_j}.
$$

La suma $\sum e_i-1$ tiene grado a lo sumo $s-1$ y se anula en los $s$ puntos distintos, por lo que es cero. Aquí se usa el lema elemental: un polinomio no nulo de grado $d$ tiene a lo sumo $d$ raíces, probado por inducción al dividir por $t-a$ para cada raíz. Además $(t-\lambda_i)e_i$ es múltiplo de $\mu_T$, de modo que $(T-\lambda_i I)e_i(T)=0$. Todo $v=\sum e_i(T)v$ es suma de vectores de los autoespacios. Es suma directa por 4.2 y llena $V$, así diagonaliza por 4.3. **Conclusión.** Ambas direcciones y la hipótesis de escisión están probadas.

## T4. Descomposición primaria por Bézout

**Hipótesis.** $p,q$ coprimos y $(pq)(T)=0$. **Tesis.** $V=\ker p(T)\oplus\ker q(T)$. Para más factores coprimos dos a dos se itera.

**Estrategia ES.** Convertir Bézout en dos componentes complementarias. **策略中文。** 各分量来自一个明确的算子多项式，不能只凭维数猜分解。

**Demostración.** Sean $a,b$ con $ap+bq=1$. Entonces $I=a(T)p(T)+b(T)q(T)$. Para cualquier $v$, el vector $b(T)q(T)v$ está en $\ker p(T)$ porque el producto $pq$ anula; el vector $a(T)p(T)v$ está en $\ker q(T)$. Su suma es $v$. Si $w$ pertenece a ambos núcleos, la misma identidad da $w=0$, así la suma es directa. Para varios factores, cada factor es coprimo al producto de los restantes; aplicar el caso de dos y repetir en los subespacios invariantes demuestra la descomposición por inducción. La invariancia se debe a que $T$ conmuta con cada polinomio en sí mismo.

Si la característica se escinde $\chi_T=\prod_\lambda(t-\lambda)^{a_\lambda}$, Cayley–Hamilton permite aplicar el resultado y da

$$
V=\bigoplus_\lambda G_\lambda,\qquad G_\lambda=\ker(T-\lambda I)^{a_\lambda}.
$$

Sobre $G_\lambda$, $T-\lambda I$ es nilpotente por construcción. **Conclusión.** Se obtiene el soporte lógico de Jordan sin usar aún su existencia. **中文解释。** 先有多项式零化与互素分解，再建立 Jordan 链，推理顺序不循环。

## Inversa y reducción de cálculos

Si $T$ es invertible, $0$ no es valor propio y T3 da $\mu_T(0)\ne0$. Si $\mu_T(t)=c_0+tq(t)$ con $c_0\ne0$, su evaluación da $T(-q(T)/c_0)=I$, y el orden opuesto también es identidad porque los factores conmutan. Así $T^{-1}=-q(T)/c_0$. Dividir un polinomio cualquiera por $\mu_T$ muestra que su valor en $T$ coincide con el resto, de grado menor. Esto reduce potencias sin sumar una serie infinita.

前置为行列式、对偶章节中的 End 维数与对角化；本节官方编号 4.5 但在学习路线中先于 [Jordan 4.4](../04_Jordan/01_Teoria_Demostraciones.md)。自测 ES: reproducir telescopado, división y Bézout, no solo verificar una matriz. 中文：不能把“代入一个例子为零”当成 Cayley–Hamilton 一般证明。[例题](04_Ejemplos.md)、[练习](05_Ejercicios.md)、[解答](06_Soluciones.md)。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
