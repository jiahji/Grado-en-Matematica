---
title: Forma canónica de Jordan / Jordan 标准形
subject: Álgebra Lineal
tema: Guía 4.4
type: theorem
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_4_4
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Forma canónica de Jordan — Jordan 标准形

**Fuentes verificadas:** AL-GD-001 p. 6, 4.4; suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.

**Organización:** esta unidad integra motivación, definiciones, teoremas, pruebas, conexiones y repaso en un archivo; ejemplos, ejercicios y soluciones se mantienen separados.


## Motivación y definiciones

**Español.** Cuando faltan autovectores, se añaden vectores cuyas imágenes caen en los anteriores: cadenas de vectores generalizados. Las entradas fuera de la diagonal registran exactamente esa pérdida de direcciones propias. **中文。** Jordan 形不是给对角线随意添 1；每个 1 都对应一条满足特定递推关系的链。

Sea $T:V\to V$ un endomorfismo de dimensión finita. Se supone primero que $\chi_T$ se escinde en el cuerpo. Un vector generalizado de $\lambda$ satisface $(T-\lambda I)^k v=0$ para algún $k\ge1$. El autoespacio generalizado es $G_\lambda=\ker(T-\lambda I)^{a_\lambda}$. Una cadena de longitud $m$ es $(v_1,\ldots,v_m)$ con $v_1\ne0$, $Nv_1=0$, $Nv_j=v_{j-1}$ para $j>1$, donde $N=T-\lambda I$. En ella la matriz es

$$
J_m(\lambda)=\begin{pmatrix}
\lambda&1&0&\cdots&0\\0&\lambda&1&\cdots&0\\
\vdots&&\ddots&\ddots&\vdots\\0&\cdots&0&\lambda&1\\0&\cdots&0&0&\lambda
\end{pmatrix}.
$$

Los unos están en la superdiagonal porque la columna $j$ manda $v_j$ a $\lambda v_j+v_{j-1}$. Escoger un vector de altura exacta $m$ significa $N^mv=0$ pero $N^{m-1}v\ne0$; genera una cadena al ordenar sus imágenes desde $N^{m-1}v$ hasta $v$.

## T1. Existencia de base de cadenas para nilpotentes

**Hipótesis.** $N:V\to V$ nilpotente y $V$ finito. **Tesis.** Hay una base formada por cadenas de $N$.

**Estrategia ES.** Inducir sobre dimensión usando $W=\operatorname{Im}N$, levantar los extremos de sus cadenas y completar con vectores del núcleo. **策略中文。** 简单任取长链可能遗漏或重叠方向；递归到像空间并控制核补空间，才能保证是一整组基。

**Demostración.** Si $N=0$, cualquier base da cadenas de longitud uno; el espacio cero usa base vacía. Si $N\ne0$, $W$ es propio: de ser $N$ sobreyectivo en dimensión finita, sería invertible; ninguna potencia suya podría ser cero en un espacio no nulo. Así $\dim W<\dim V$. La restricción a $W$ es nilpotente e invariante, de modo que la inducción da una base de cadenas

$$
w_{j,1},\ldots,w_{j,\ell_j}\quad(j=1,\ldots,s)
$$

de $W$, con $Nw_{j,k}=w_{j,k-1}$. En $W/NW$, las clases de sus extremos $w_{j,\ell_j}$ forman base: $NW$ está generado por todos los vectores de cadena salvo esos extremos, y la base completa de $W$ garantiza independencia de sus clases.

Como cada extremo pertenece a $W=NV$, elija $v_j\in V$ con $Nv_j=w_{j,\ell_j}$. Prolongue cada cadena con $v_j$ y sea $U=W+\langle v_1,\ldots,v_s\rangle$. Estas prolongaciones son independientes: si $\sum a_jv_j+w=0$ con $w\in W$, aplicar $N$ y pasar a $W/NW$ da $\sum a_j[w_{j,\ell_j}]=0$, de donde todos los $a_j=0$ y después $w=0$. Además $NU=NW+\langle w_{j,\ell_j}\rangle=W$.

Para cualquier $x\in V$, $Nx\in W=NU$, así existe $u\in U$ con $Nu=Nx$, y $x-u\in\ker N$. Por ello $V=U+\ker N$. Tome una base de $U\cap\ker N$ y complétela dentro de $\ker N$ con vectores $z_1,\ldots,z_r$. Su generado intersecta $U$ solo en cero, porque todo vector de tal intersección estaría en $U\cap\ker N$, y las dos partes de la base del núcleo son independientes. Por tanto $V=U\oplus\langle z_1,\ldots,z_r\rangle$. Añadir esos $z_i$ como cadenas de longitud uno completa las cadenas prolongadas a una base de todo $V$.

**Explicación ES.** Los levantamientos tienen altura exacta $\ell_j+1$, pues su imagen tras $\ell_j$ aplicaciones es $w_{j,1}\ne0$. Se ha demostrado generación e independencia de toda la lista. **中文解释。** 关键是证明 $NU=W$，使任何尚未覆盖的方向都可以通过一个核向量补进来。**Conclusión.** La inducción proporciona una base de cadenas, no solo una colección incompleta.

## T2. Existencia de Jordan general

**Hipótesis.** $\chi_T=\prod_\lambda(t-\lambda)^{a_\lambda}$ se escinde. **Tesis.** Existe una base en que $T$ es diagonal por bloques $J_m(\lambda)$.

**Estrategia ES.** Usar descomposición primaria ya probada y aplicar T1 en cada componente. **策略中文。** 先分离不同特征值，再处理每个值内部的幂零部分。

**Demostración.** Por [Bézout y Cayley–Hamilton](../05_Polinomios_Cayley_Hamilton/01_Teoria_Demostraciones.md), $V=\bigoplus_\lambda G_\lambda$. En $G_\lambda$, $N_\lambda=T-\lambda I$ satisface $N_\lambda^{a_\lambda}=0$. T1 produce una base de cadenas de ese nilpotente. En cada cadena, las relaciones de definición dan el bloque $J_m(\lambda)$. Reunir las bases de las componentes directas da base de $V$. Cada bloque tiene característica $(t-\lambda)^m$, por triangularidad, y la característica de la matriz diagonal por bloques es el producto de las de sus bloques por la expansión de determinante. Comparar con $\chi_T$ muestra que las longitudes para un mismo $\lambda$ suman $a_\lambda$. **Conclusión.** También se deduce $\dim G_\lambda=a_\lambda$. **中文解释。** Jordan 存在性在分裂条件下证明；不能无条件在有理数域或实数域要求所有块为实线性特征值块。

## T3. Unicidad y recuperación de tamaños

Defina $d_k(\lambda)=\dim\ker(T-\lambda I)^k$, con $d_0=0$. Entonces

$$
d_k=\sum_{\text{bloques de }\lambda}\min(k,m),\qquad
b_k=d_k-d_{k-1}=\#\{\text{bloques de tamaño al menos }k\}.
$$

El número de bloques de tamaño exactamente $k$ es

$$
b_k-b_{k+1}=2d_k-d_{k-1}-d_{k+1}.
$$

**Hipótesis/Tesis.** Probar las fórmulas y que determinan una única forma salvo orden de bloques. **Estrategia ES.** Calcular núcleos en cada cadena y reconocer invariantes de semejanza. **策略中文。** 先证明数据如何来自块，再证明从数据可反推每种块的数量。

**Demostración.** En una cadena de longitud $m$, $N^k$ anula exactamente el generado de los primeros $\min(k,m)$ vectores; los restantes tienen imágenes independientes en los lugares anteriores. En las componentes de otros valores $\mu\ne\lambda$, $T-\lambda I=(\mu-\lambda)I+N_\mu$ es invertible: su inversa es la suma geométrica finita

$$
\frac1{\mu-\lambda}\sum_{j=0}^{a_\mu-1}\left(-\frac{N_\mu}{\mu-\lambda}\right)^j.
$$

Multiplicar cancela todos los términos salvo identidad y una potencia nilpotente cero. Esas componentes no aportan núcleo. Sumando contribuciones se obtiene la primera fórmula. La diferencia $\min(k,m)-\min(k-1,m)$ es $1$ exactamente si $m\ge k$, dando la segunda y después la tercera.

Las dimensiones de núcleos de potencias no cambian por semejanza, pues $(P^{-1}(A-\lambda I)P)^k=P^{-1}(A-\lambda I)^kP$ y el núcleo se transporta por $P^{-1}$. Por tanto determinan todos los tamaños. Si dos formas tienen esos tamaños, permutar bloques iguala las matrices, y esa permutación es un cambio de base. **Conclusión.** Jordan es único salvo orden de bloques y clasifica semejanza cuando la característica se escinde.

**中文解释。** $d_k$ 最终稳定为 $a_\lambda$，不是有其他特征值时的整个 $n$。增量 $b_k$ 必须非负且递减，可用于拒绝不可能的核维数数据。

**Explicación ES.** Los incrementos de dimensiones de núcleos son no negativos y no crecientes. La estabilización para un valor propio da su multiplicidad algebraica, no necesariamente toda la dimensión cuando hay otros valores propios.

## T4. Mínimo, número de bloques y diagonalización

El número de bloques de $\lambda$ es $b_1=d_1=g_\lambda$. El mayor tamaño $s_\lambda$ es el exponente de $t-\lambda$ en $\mu_T$. Así

$$
\mu_T(t)=\prod_\lambda(t-\lambda)^{s_\lambda}.
$$

**Prueba completa.** En un bloque $\lambda I+N$ de longitud $m$, escriba un polinomio no nulo $q=(t-\lambda)^rh$ con $h(\lambda)\ne0$. Entonces $h(\lambda I+N)=h(\lambda)I+NR(N)$ para algún polinomio $R$. El segundo sumando es nilpotente, por lo que la misma suma geométrica finita muestra que $h(\lambda I+N)$ es invertible. Por conmutación de polinomios, $q(\lambda I+N)=0$ equivale a $N^r=0$, esto es $r\ge m$. Un polinomio anula todos los bloques exactamente cuando contiene cada factor con exponente al menos el mayor tamaño de su valor. El producto indicado es mónico, anula y divide todo anulador, así es el mínimo por 4.5. En particular diagonalizable equivale a todos los tamaños uno, en acuerdo con el criterio del mínimo sin factores repetidos.

## Cómo construir una base, no solo una lista de tamaños

Calcular raíces y $d_k$ para deducir tamaños. Para construir vectores con garantías, usar la inducción de T1 dentro de cada $G_\lambda$: obtener una base de $\operatorname{Im}N$ por Gauss, expresar la restricción en ella, construir recursivamente sus cadenas, resolver $Nv_j=w_{j,\ell_j}$ para prolongar extremos y completar $\ker N$ por vectores fuera de las cadenas ya generadas. Todo son sistemas y extensiones finitas de bases. Al reunir las cadenas como columnas de $P$, verificar **$AP=PJ$** y la independencia de $P$. No elegir arbitrariamente varios extremos en núcleos de potencias sin probar que sus cadenas conjuntas sean independientes.

## Matrices reales y pares conjugados

Si una matriz real tiene valores no reales $a\pm bi$ con $b>0$, no existe Jordan con todas esas entradas en $\mathbb R$ del tipo escalar anterior. Se trabaja en la complejificación y se eligen cadenas conjugadas. Para una cadena $v_j=u_j+iw_j$ del valor $a+bi$, usar vectores reales ordenados $(u_j,-w_j)$. Sus fórmulas son

$$
Tu_j=au_j-bw_j+u_{j-1},\quad T(-w_j)=-bu_j+a(-w_j)-w_{j-1},
$$

con componentes previas cero al inicio. Producen bloques diagonales $C=\begin{pmatrix}a&-b\\b&a\end{pmatrix}$ y superdiagonales $I_2$. Son independientes: una relación real entre $u_j,-w_j$, escrita con $v_j,\bar v_j$, tendría coeficientes conjugados y violaría la independencia de las dos familias complejas. Generan la parte real porque todo vector fijo por conjugación tiene coeficientes conjugados en esas cadenas. Para valores reales se escogen cadenas reales con T1. Esto da la forma real correspondiente. Para matrices racionales con característica no escindida, la forma escalar puede requerir extender el cuerpo; no se afirma que exista con todas las entradas racionales.

## Repaso

前置 [多项式分解与 Cayley–Hamilton](../05_Polinomios_Cayley_Hamilton/01_Teoria_Demostraciones.md)。后续 [矩阵函数与动力系统](../06_Funciones_Dinamica/01_Teoria_Demostraciones.md)。自测 ES: probar existencia por imagen y núcleo, deducir tamaños de diferencias y construir un $P$ verificable. 中文：只给块大小而不说明链如何形成，不是完整的 Jordan 理论学习。[例题](04_Ejemplos.md)、[练习](05_Ejercicios.md)、[解答](06_Soluciones.md)。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
