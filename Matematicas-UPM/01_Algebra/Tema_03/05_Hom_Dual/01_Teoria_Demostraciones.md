---
title: Espacio de aplicaciones y dual / 映射空间与对偶空间
subject: Álgebra Lineal
tema: Guía 3.8
type: theorem
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_3_8
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-003/Tema 3_3783d906f8056ce104fc5d6bc1f5548c.pdf
updated: 2026-10-26
---

# Espacio de aplicaciones y dual — 映射空间与对偶空间

**Fuentes verificadas:** AL-AP-003, p. 19: terminología de forma lineal; desarrollo de Hom y dual como suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.

**Organización:** esta unidad integra motivación, definiciones, teoremas, pruebas, conexiones y repaso en un archivo; ejemplos, ejercicios y soluciones se mantienen separados.


## Motivación y definiciones

**Español.** Una forma lineal mide un vector produciendo un escalar. El dual reúne todas esas mediciones; no se debe confundir con un conjunto de vectores perpendiculares sin haber dado un producto escalar. **中文。** 对偶元素本身是函数，坐标可以把它写成数组，但不会因此让它变成原向量。

$\operatorname{Hom}_{\mathbb K}(V,W)$ es el conjunto de mapas lineales con operaciones $(af+bg)(v)=af(v)+bg(v)$. El dual（对偶空间）es $V^*=\operatorname{Hom}(V,\mathbb K)$. Para $U\le V$, su anulador（零化子）es $U^0=\{\ell\in V^*: \ell(u)=0\ \forall u\in U\}$. Para $f:V\to W$, la aplicación dual o traspuesta es $f^*:W^*\to V^*$, $f^*(\ell)=\ell\circ f$.

Las nociones de forma lineal aparecen en AL-AP-003 p. 19; el desarrollo completo siguiente es suplemento explícito del apartado oficial 3.8.

## T1. Estructura y dimensión de Hom

**Hipótesis.** Bases $B=(v_1,\ldots,v_n)$, $C=(w_1,\ldots,w_m)$. **Tesis.** Hom es espacio vectorial de dimensión $mn$.

**Estrategia ES.** Comprobar clausura de combinaciones de mapas y construir matrices de una sola entrada. **策略中文。** 运算是逐点定义，但结果还必须是线性映射。

**Demostración.** Si $h=af+bg$, para $\alpha u+\beta v$ se expanden ambas linealidades y, agrupando escalares, resulta $h(\alpha u+\beta v)=\alpha h(u)+\beta h(v)$. Cero y opuestos se obtienen punto a punto, y todos los axiomas se heredan de $W$ al evaluar en cada vector. Defina $E_{ij}$ como el mapa que envía $v_j$ a $w_i$ y los otros básicos a cero. Existen por 3.1. Si la matriz de $f$ tiene entradas $a_{ij}$, sus valores en la base prueban $f=\sum_{ij}a_{ij}E_{ij}$. Si tal suma es cero, evaluar en cada $v_j$ y usar independencia de los $w_i$ fuerza todos los coeficientes cero. **Conclusión.** Los $mn$ mapas forman base. **中文解释。** 这也证明 $f\mapsto M_{B,C}(f)$ 是到矩阵空间的线性同构，而不只是一个数值对应。

## T2. Base dual y doble dual

**Enunciado.** Existen únicas $\varphi_i$ con $\varphi_i(v_j)=\delta_{ij}$; forman base de $V^*$ y toda $\ell$ es $\sum_i\ell(v_i)\varphi_i$. El mapa canónico $J:V\to V^{**}$, $J(v)(\ell)=\ell(v)$, es isomorfismo en dimensión finita.

**Estrategia ES.** Extraer coordenadas con funcionales y reconstruir un vector desde evaluaciones en la base dual. **策略中文。** $V$ 到 $V^*$ 的基依赖识别与到双对偶的自然映射是不同对象。

**Demostración.** Para $v=\sum x_jv_j$, definir $\varphi_i(v)=x_i$; son lineales por coordenadas. Cualquier lineal con esos valores básicos coincide por 3.1. La expresión de $\ell$ se verifica evaluando en $v$; si $\sum a_i\varphi_i=0$, evaluar en $v_j$ da $a_j=0$, así forman base y $\dim V^*=n$.

Para cada $v$, $J(v)$ es lineal en $\ell$, y la linealidad de $J$ en $v$ sigue evaluando sobre cualquier $\ell$. Si $J(v)=0$, todos los $\varphi_i(v)=0$, así $v=0$. Para cualquier $F\in V^{**}$, ponga $v=\sum_iF(\varphi_i)v_i$. Entonces para $\ell=\sum_i\ell(v_i)\varphi_i$,

$$
F(\ell)=\sum_i\ell(v_i)F(\varphi_i)=\ell(v)=J(v)(\ell).
$$

Así $J$ también es sobreyectiva. **Conclusión.** Isomorfismo canónico probado sin elegir una identificación arbitraria de $V$ con $V^*$. **中文解释。** 构造逆时可用某组基计算，但 $J(v)(\ell)=\ell(v)$ 本身与基无关。

## T3. Anuladores y separación

**Hipótesis.** $\dim V=n$, $\dim U=r$. **Tesis.** $U^0$ es subespacio de dimensión $n-r$, y $v\in U$ si y solo si toda $\ell\in U^0$ satisface $\ell(v)=0$.

**Estrategia ES.** Completar una base de $U$ y usar la base dual adaptada. **策略中文。** 约束原子空间等于在对偶里排除前 $r$ 个坐标函数。

**Demostración.** Cero y combinaciones de formas que anulan $U$ lo siguen anulando, así es subespacio. Complete una base de $U$ a $B=(v_1,\ldots,v_n)$. La condición equivale a que los coeficientes $\ell(v_1),\ldots,\ell(v_r)$ sean cero; por T2 queda la base $\varphi_{r+1},\ldots,\varphi_n$. Si $v\in U$, toda forma anuladora lo anula. Si $v\notin U$, alguna coordenada $j>r$ de $v$ es no nula y $\varphi_j\in U^0$ no lo anula, contradiciendo la condición. **Conclusión.** Bajo $J$, el doble anulador recupera exactamente $U$. **中文解释。** 这给出不依赖正交或长度概念的线性分离。

## T4. Matriz de la traspuesta y contravarianza

**Hipótesis.** $A=M_{B,C}(f)$ y bases duales $B^*,C^*$. **Tesis.** $M_{C^*,B^*}(f^*)=A^{\mathsf T}$; $\ker f^*=(\operatorname{Im}f)^0$ y $\operatorname{Im}f^*=(\ker f)^0$ en dimensión finita.

**Estrategia ES.** Evaluar un funcional dual del destino en la imagen de cada vector básico. **策略中文。** 对偶箭头反向，是因为先把一个输出测量拉回定义域。

**Demostración.** La composición y las operaciones punto a punto prueban linealidad de $f^*$. Si $\psi_j$ es dual de $w_j$, el coeficiente $i$ de $f^*(\psi_j)$ en $B^*$ es $f^*(\psi_j)(v_i)=\psi_j(f(v_i))=a_{ji}$. Así la columna $j$ es la correspondiente de $A^{\mathsf T}$. El núcleo consta exactamente de formas que anulan toda la imagen, probando la primera igualdad. La imagen anula $\ker f$ porque $\ell(f(v))=0$ para $v$ en él. Su dimensión es $\operatorname{rg}A^{\mathsf T}=\operatorname{rg}A$ por igualdad fila-columna. El anulador del núcleo tiene dimensión $n-\dim\ker f=\operatorname{rg}f$ por T3 y rango–nulidad; inclusión y dimensión iguales prueban la segunda igualdad.

Para composiciones, $((g\circ f)^*\ell)(v)=\ell(g(f(v)))=(f^*(g^*\ell))(v)$, por lo que $(g\circ f)^*=f^*\circ g^*$. **Conclusión.** La dirección y el orden se invierten de forma demostrada.

**Explicación ES.** La dualidad se define mediante funciones lineales y evaluaciones. No presupone una longitud ni perpendicularidad; esas nociones exigirían datos adicionales. El doble dual recupera cada subespacio por la separación demostrada, mediante el mapa canónico.

## Cambio de base dual y repaso

Si los vectores de la nueva base tienen columnas $P$ en la antigua, $[v]_B=P[v]_{B'}$. La forma nueva dual $\varphi_i'$ extrae la coordenada $i$ de $P^{-1}[v]_B$, así $\varphi_i'=\sum_j(P^{-1})_{ij}\varphi_j$. Por tanto las columnas de la nueva base dual en la antigua son $P^{-\mathsf T}$. No se confunde con las coordenadas de una forma fija: estas son sus valores en los nuevos vectores, de modo que se transforman por $P^{\mathsf T}$.

前置 [换基](../../Tema_04/02_Cambio_Base_Semejanza/01_Teoria_Demostraciones.md) 和基。**Español.** Distinguir vector, forma, coordenadas de forma y base dual; justificar cada anulación por una evaluación. **中文。** “对偶等于正交补”没有内积前提时是错误说法。[例题](04_Ejemplos.md)、[题目](05_Ejercicios.md)、[解答](06_Soluciones.md)。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
