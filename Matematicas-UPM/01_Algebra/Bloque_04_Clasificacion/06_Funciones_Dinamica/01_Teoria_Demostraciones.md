---
title: Funciones de matrices y dinámica discreta / 矩阵函数与离散动力系统
subject: Álgebra Lineal
tema: Guía 4.6
type: theorem
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_4_6
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Funciones de matrices y dinámica discreta — 矩阵函数与离散动力系统

**Fuentes verificadas:** AL-GD-001 p. 6, 4.6; suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.

**Organización:** esta unidad integra motivación, definiciones, teoremas, pruebas, conexiones y repaso en un archivo; ejemplos, ejercicios y soluciones se mantienen separados.


## Motivación e hipótesis — 动机与条件

**Español.** Una recurrencia como $x_{k+1}=Ax_k$ pide calcular muchas potencias de la misma matriz. Jordan convierte este problema en potencias de bloques; el polinomio mínimo permite además definir funciones sin escoger una base particular. Aplicar una función a cada entrada no describe, en general, una función del operador.

**中文。** 矩阵函数的输入是整个线性算子。我们要保留复合、换基和多项式关系，而不是逐个修改矩阵元素。例如零算子的指数应是恒等算子，逐元素取指数却会得到全为 $1$ 的矩阵。离散动力系统（sistema dinámico discreto）研究重复应用同一线性规则后的长期行为。

Trabajamos en dimensión finita $n\geq1$. Para la descripción por autovalores suponemos que el polinomio característico se escinde sobre $\mathbb K$, normalmente $\mathbb C$. Para matrices reales se usa la complejificación y después se interpreta el resultado real. Los resultados sobre límites utilizan la norma usual de $\mathbb R^n$ o $\mathbb C^n$ y hechos elementales del análisis escalar, que se indican donde intervienen.

## 1. Cálculo polinómico y racional — 多项式与有理函数

Para $p(t)=\sum a_jt^j$ se define $p(A)=\sum a_jA^j$. Ya se ha demostrado que esta evaluación respeta suma y producto. Si $B=P^{-1}AP$, entonces $B^j=P^{-1}A^jP$ por inducción y, por tanto, $p(B)=P^{-1}p(A)P$.

Una función racional $p/q$ puede evaluarse como $p(A)q(A)^{-1}$ cuando $q(A)$ es invertible. Si $q$ y el polinomio mínimo $\mu_A$ son coprimos, Bézout da $u q+v\mu_A=1$; al evaluar resulta $u(A)q(A)=I$, así que $q(A)^{-1}=u(A)$. Recíprocamente, si comparten un factor $t-\lambda$ sobre un cuerpo donde $\mu_A$ se escinde, un autovector no nulo $v$ satisface $q(A)v=q(\lambda)v=0$ y no hay inversa. Bajo esta hipótesis, basta exigir $q(\lambda)\ne0$ en todos los autovalores.

**Explicación ES.** La condición se impone en el espectro, no en cada entrada. El resultado sigue siendo una matriz polinómica en $A$ después de reducir módulo $\mu_A$.

**中文。** 分母函数在特征值上不能为零。矩阵某个元素等于零，与整个矩阵是否可逆并不是同一个条件。若两个有理表达式在谱附近相等，其差的分子恒为零，通分并利用分母矩阵可逆可知它们给出相同的矩阵。

## 2. Interpolación de Hermite y funciones — Hermite 插值定义

Sea

$$
\mu_A(t)=\prod_{i=1}^r(t-\lambda_i)^{s_i},\qquad \lambda_i\ne\lambda_j\ (i\ne j).
$$

Para definir $f(A)$ bastan los datos escalares $f^{(j)}(\lambda_i)$ para $0\leq j<s_i$. Se supone que estas derivadas existen; no se pretende deducir aquí la teoría analítica de $f$. Definimos

$$
r_i(t)=\sum_{j=0}^{s_i-1}\frac{f^{(j)}(\lambda_i)}{j!}(t-\lambda_i)^j.
$$

### Teorema — existencia y unicidad del polinomio interpolador

**Hipótesis.** $p_i=(t-\lambda_i)^{s_i}$ son coprimos dos a dos y se conocen los $r_i$ anteriores.

**Tesis.** Existe un único $h$ con $\deg h<\deg\mu_A$ tal que $h\equiv r_i\pmod{p_i}$ para todo $i$.

**Estrategia ES.** Construir un polinomio que sea $1$ en un componente y $0$ en todos los demás usando Bézout, y sumar las contribuciones locales.

**策略（中文）。** 每个特征值只要求一组有限阶导数。用互素性构造“选择器”，把不同特征值附近的信息拼成同一个多项式；唯一性保证定义不依赖拼接细节。

**Demostración.** Sea $q_i=\mu_A/p_i$. Como $q_i$ y $p_i$ son coprimos, existen $a_i,b_i$ con $a_iq_i+b_ip_i=1$. Póngase $e_i=a_iq_i$. Entonces $e_i\equiv1\pmod{p_i}$ y $e_i\equiv0\pmod{p_j}$ si $j\ne i$. Por ello $h_0=\sum_i e_i r_i$ satisface todas las congruencias; su resto al dividir por $\mu_A$ también las satisface y tiene el grado requerido.

Si $h$ y $\widetilde h$ satisfacen las congruencias, cada $p_i$ divide su diferencia. Para justificar que divide el producto, sean $p,q$ coprimos y $d=pu$ divisible por $q$. De $ap+bq=1$, multiplicando por $u$, se obtiene $u=apu+bqu$; ambos sumandos son divisibles por $q$ porque $q\mid pu$. Así $q\mid u$ y $pq\mid d$. Aplicando este argumento sucesivamente, $\mu_A\mid h-\widetilde h$. Pero su diferencia tiene grado menor que $\deg\mu_A$; luego es cero. $\square$

**Explicación detallada ES.** Cada congruencia registra un valor y sus derivadas hasta el orden necesario. La división final no cambia estas condiciones. El polinomio mínimo determina cuánto dato local hace falta.

**中文。** 一个长度为 $s_i$ 的最长 Jordan 链，会要求函数在该特征值处直到 $s_i-1$ 阶的导数。只知道 $f(\lambda_i)$，在不能对角化时通常不够。

**Definición y conclusión.** Se define $f(A)=h(A)$ mediante este único resto. Para polinomios coincide con la evaluación habitual, por la fórmula de Taylor exacta para polinomios y $\mu_A(A)=0$. La construcción es intrínseca: si $B=P^{-1}AP$, tiene el mismo polinomio mínimo y los mismos datos de interpolación, de modo que $f(B)=P^{-1}f(A)P$.

### Fórmula en un bloque de Jordan

Para $J_m(\lambda)=\lambda I+N$, donde $N^m=0$, se tiene

$$
f(J_m(\lambda))=\sum_{j=0}^{m-1}\frac{f^{(j)}(\lambda)}{j!}N^j.
$$

**Demostración.** Por la clasificación de Jordan, $m\leq s_i$ para el autovalor $\lambda_i=\lambda$. La congruencia de interpolación implica que $h$ y el Taylor truncado de orden $m-1$ difieren en un múltiplo de $(t-\lambda)^m$. Evaluando en $J_m(\lambda)$, esa diferencia es cero porque $(J_m(\lambda)-\lambda I)^m=N^m=0$. $\square$

**Interpretación ES.** La diagonal usa $f(\lambda)$; las superdiagonales registran derivadas. Una diagonalización es el caso particular $m=1$.

**中文。** 非对角 Jordan 块中，超对角线并非无关的小扰动，它把函数的导数引入计算。多个块逐块计算后，还必须用 $P f(J)P^{-1}$ 返回原坐标。

## 3. Potencias y exponencial — 幂与指数

### Proposición — fórmula de potencias

**Hipótesis.** $J=\lambda I+N$, $N^m=0$, $k$ es un entero no negativo.

**Tesis.** Si $\lambda\ne0$,

$$
J^k=\sum_{j=0}^{\min(k,m-1)}\binom{k}{j}\lambda^{k-j}N^j.
$$

Si $\lambda=0$, $J^k=N^k$, con $J^0=I$; para $k\geq m$, $J^k=0$.

**Estrategia ES / 中文。** Usar el binomio para dos operadores que conmutan y eliminar las potencias nulas de $N$。先验证可交换条件，再使用二项式；零特征值单独处理，避免写出负幂或未说明的 $0^0$。

**Demostración.** Para $k=0$ el resultado es $I$. Suponiendo la expansión para $k$, al multiplicar por $\lambda I+N$ se obtienen dos sumas. Como $N$ conmuta con $\lambda I$, el coeficiente de $\lambda^{k+1-j}N^j$ es $\binom{k}{j}+\binom{k}{j-1}=\binom{k+1}{j}$. Los extremos corresponden a coeficientes $1$. Esta es la expansión para $k+1$; los términos $N^j$ con $j\geq m$ desaparecen. Si $\lambda=0$, la identidad $J=N$ da directamente la segunda afirmación. $\square$

**Conclusión ES.** Si $A=PJP^{-1}$, entonces $A^k=PJ^kP^{-1}$. La fórmula se refiere a potencias matriciales, no a potencias de las entradas.

**中文。** 公式中出现的 $k$、$k(k-1)$ 等因子来自 Jordan 链；它们决定了单位圆上的长期行为。

Para $f(z)=e^{tz}$, las derivadas escalares son $t^je^{t\lambda}$; por el cálculo anterior,

$$
e^{tJ_m(\lambda)}=e^{t\lambda}\sum_{j=0}^{m-1}\frac{t^j}{j!}N^j.
$$

Esta definición coincide con $\sum_{k\geq0}t^kA^k/k!$: en la norma de suma máxima por filas, $\|AB\|\leq\|A\|\|B\|$, porque cada suma de valores absolutos de una fila de $AB$ se acota por la suma ponderada de las filas de $B$. Por tanto, la serie está acotada por $\sum |t|^k\|A\|^k/k!=e^{|t|\|A\|}$ y converge absolutamente, usando la serie exponencial escalar. En un bloque, la expansión binomial y la suma absolutamente convergente dan, para cada $j<m$,

$$
\sum_{k=j}^\infty\frac{t^k}{k!}\binom{k}{j}\lambda^{k-j}
=\frac{t^j}{j!}\sum_{\ell=0}^\infty\frac{(t\lambda)^\ell}{\ell!}
=\frac{t^j}{j!}e^{t\lambda}.
$$

Así se recupera la fórmula finita, también para $\lambda=0$ mediante la suma de la serie.

**Ley exponencial, con prueba.** Para el mismo $A$, $e^{sA}e^{tA}=e^{(s+t)A}$. En cada bloque el coeficiente de $N^j$ en el producto de las sumas finitas es $\sum_{a+b=j}s^at^b/(a!b!)=(s+t)^j/j!$ por el binomio escalar. Los factores escalares se multiplican como $e^{s\lambda}e^{t\lambda}=e^{(s+t)\lambda}$. Volviendo por semejanza se obtiene la identidad. En particular $e^{0A}=I$ y $(e^{tA})^{-1}=e^{-tA}$. Para matrices distintas esta ley requiere hipótesis adicionales, por ejemplo conmutatividad; no se infiere para cualesquiera $A,B$.

## 4. Recurrencias lineales — 线性递推

Un sistema homogéneo discreto es $x_{k+1}=Ax_k$ con $x_0$ dado. Su solución es $x_k=A^kx_0$: vale para $k=0$ y, si vale para $k$, entonces $x_{k+1}=A(A^kx_0)=A^{k+1}x_0$. Esto prueba existencia; la misma recurrencia determina cada estado de manera única.

Para una recurrencia escalar de orden dos,

$$
u_{k+2}=a u_{k+1}+b u_k,\qquad
x_k=\begin{pmatrix}u_{k+1}\\u_k\end{pmatrix},\qquad
A=\begin{pmatrix}a&b\\1&0\end{pmatrix},
$$

la igualdad $x_{k+1}=Ax_k$ traduce el problema a potencias. El estado inicial es $(u_1,u_0)^T$; intercambiarlo cambia la solución.

## 5. Comportamiento de todas las órbitas — 所有轨道的长期行为

Sea $\rho(A)=\max\{|\lambda|:\lambda\text{ autovalor complejo de }A\}$ el radio espectral（谱半径）.

### Teorema — convergencia a cero

**Hipótesis.** $A$ es una matriz real o compleja de tamaño finito.

**Tesis.** $A^kx_0\to0$ para todo $x_0$ si y solo si $\rho(A)<1$.

**Estrategia ES.** En cada bloque, comparar crecimiento polinómico y decaimiento geométrico; para la necesidad probar la condición sobre un autovector.

**策略（中文）。** 对所有初值成立与对某一个初值成立不同。充分性要控制每个 Jordan 块；必要性只要找出一个不能衰减的特征向量。

**Demostración.** Si $0<r<1$, la sucesión $k^dr^k$ tiende a cero para cada entero $d\geq0$: para $k\geq1$ el cociente de términos consecutivos es $r(1+1/k)^d$, que tiende a $r$; eligiendo $q$ con $r<q<1$, desde cierto índice los términos están acotados por una progresión geométrica de razón $q$. Para $\lambda\ne0$ con $|\lambda|<1$, cada entrada de $J_m(\lambda)^k$ es una constante por un polinomio en $k$ por $\lambda^k$ y tiende a cero. Para $\lambda=0$ el bloque se anula desde $k=m$. Por tanto $J^k\to0$ entrada a entrada y $A^k=PJ^kP^{-1}\to0$; cada $A^kx_0$ tiende a cero.

Si hay un autovalor con $|\lambda|\geq1$, un autovector $v\ne0$ cumple $A^kv=\lambda^kv$, que no tiende a cero. Para una matriz real cuyo autovector sea complejo, escriba $v=u+iw$. Si todas las órbitas reales tendieran a cero, tanto $A^ku$ como $A^kw$ lo harían y su combinación compleja también, contradicción. $\square$

**Explicación ES.** Un bloque no diagonalizable con $|\lambda|<1$ puede tener crecimiento inicial, pero termina decayendo. Un autovalor expansivo impide la afirmación universal, aunque algunos estados iniciales todavía decaigan.

**中文。** 谱半径控制“所有初值”的最终衰减，不能据此声称每一步范数都下降，也不能把某个特征值大于 $1$ 解释成所有非零初值都发散。

### Teorema — acotación y existencia de límite

**Hipótesis.** Las mismas del teorema anterior; los bloques se consideran sobre $\mathbb C$.

**Tesis.**

1. Todas las órbitas son acotadas si y solo si $|\lambda|\leq1$ para todo autovalor y cada bloque con $|\lambda|=1$ tiene tamaño $1$.
2. Todas las órbitas convergen si y solo si cada autovalor cumple $|\lambda|<1$ o $\lambda=1$, y los bloques de $\lambda=1$ tienen tamaño $1$.

**Estrategia ES / 中文。** Separar bloques interiores al disco, bloques en la frontera y bloques exteriores。单位圆内部衰减；边界上的非平凡 Jordan 链产生多项式增长；边界上的旋转可能有界却不收敛。

**Demostración.** En los bloques interiores las potencias tienden a cero por la prueba previa y, en particular, están acotadas. Un bloque de tamaño $1$ con $|\lambda|=1$ produce $\lambda^k$, de módulo $1$, y está acotado. Como $P$ y $P^{-1}$ son matrices fijas, cada coordenada de $PJ^kP^{-1}x_0$ es una combinación lineal finita con coeficientes fijos de coordenadas acotadas; se conserva la acotación.

Si $|\lambda|>1$, la órbita de un autovector es no acotada. Si $|\lambda|=1$ y existe una cadena con $Nv_2=v_1\ne0$, entonces $A^kv_2=\lambda^kv_2+k\lambda^{k-1}v_1$. En coordenadas de Jordan su primera coordenada tiene módulo $k$, así que la órbita no es acotada; una transformación inversible fija no puede convertir una sucesión no acotada en acotada, pues su inversa lleva sucesiones acotadas a acotadas. Esto prueba 1.

Para 2, la convergencia implica acotación y, por 1, solo quedan bloques interiores o bloques unitarios de tamaño $1$. Si $|\lambda|=1$ y $\lambda\ne1$, la sucesión $\lambda^k$ no converge: sus diferencias consecutivas tienen módulo $|\lambda-1|>0$, mientras que en una sucesión convergente estas diferencias tienden a cero. Por tanto solo puede quedar $\lambda=1$. A la inversa, los bloques interiores tienden a cero y los bloques $(1)$ permanecen iguales a $1$, luego $J^k$ y $A^k$ convergen. Para matrices reales la argumentación mediante partes real e imaginaria usada antes prueba también estas necesidades. $\square$

**Conclusión y límite.** Cuando todas las órbitas convergen, la matriz límite es la proyección sobre $E_1=\ker(A-I)$ a lo largo de la suma de los demás espacios propios generalizados. En la base de Jordan es diagonal con $1$ en los bloques $(1)$ y $0$ en los demás; de aquí se comprueba que su cuadrado es ella misma y que su imagen y núcleo son los indicados. Si no existe autovalor $1$, la proyección es cero.

**Explicación ES.** Acotado no significa convergente, y convergente no significa convergente a cero. Las condiciones son diferentes y se comprueban por separado.

**中文。** 纯旋转给出有界但不断变化的轨道；投影可使每条轨道都收敛，但极限依初值而定。只有全部特征值严格在单位圆内部时，所有初值的极限才统一为零。

## Repaso, errores y conexiones — 复习与联系

- Saber deducir la potencia de un bloque y resolver una recurrencia con su estado inicial. 能从二项式推导幂公式，而不是只背最终矩阵。
- Distinguir valor propio, tamaño de bloque y condición sobre **todos** los estados. 特征值模为 $1$ 时必须检查块大小。
- No aplicar $f$ entrada a entrada ni olvidar $P^{-1}$. 不能只根据对角元素判断一般矩阵的稳定性。
- Las propiedades de las series, la derivada escalar exponencial y los límites geométricos proceden del análisis elemental; aquí se ha justificado su utilización matricial. 不将所用分析事实冒充课堂已证结论。
- Son objetivos de autoevaluación, no predicciones de exámenes reales: no se han recibido pruebas anteriores de esta parte.

**Conocimientos previos.** [Polinomio mínimo y Bézout](../05_Polinomios_Cayley_Hamilton/01_Teoria_Demostraciones.md), [Jordan y sus cadenas](../04_Jordan/01_Teoria_Demostraciones.md).

**Conexiones.** [Diagonalización](../03_Diagonalizacion/01_Teoria_Demostraciones.md): reduce las fórmulas a bloques de tamaño uno; la dinámica explica por qué la parte nilpotente importa.

**Práctica.** [Ejemplos](04_Ejemplos.md), [ejercicios sin respuestas](05_Ejercicios.md), [soluciones separadas](06_Soluciones.md). [Índice del bloque](../00_Indice.md).

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
