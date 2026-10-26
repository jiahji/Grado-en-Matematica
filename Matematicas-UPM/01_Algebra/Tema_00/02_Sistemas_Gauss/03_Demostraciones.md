---
title: Pruebas de Gauss y Rouché–Frobenius / 消元与相容定理的完整证明
subject: Álgebra Lineal
tema: Tema 0 · Guía 1.2
type: proof
language: es-zh
status: complete
tags:
- algebra_lineal
- gauss
- sistemas
- rango
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-000/Tema 0(6).pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-004/Tema 4_65298606b99b4fa875367ddfc0765632.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Pruebas de Gauss y Rouché–Frobenius — 完整证明

**Fuentes de los resultados:** AL-AP-000 pp. 3–9; AL-AP-004 pp. 13–20. El desarrollo detallado y la ruta sin rango–nulidad son suplemento didáctico. Se usan las definiciones de este módulo y las leyes matriciales ya demostradas en [Matrices](../01_Matrices/03_Demostraciones.md).

## P1. Operaciones reversibles y matrices elementales

**Hipótesis.** Un sistema $Ax=b$ y una operación elemental sobre filas completas.

**Tesis.** El nuevo sistema tiene exactamente las mismas soluciones; la operación es multiplicación por una matriz invertible.

**Estrategia — Español.** Mostrar la operación inversa en cada caso, conservando las otras ecuaciones.

**策略 — 中文。** 每次既证明原解仍满足新式，也证明新解能还原到旧式，避免只做一个方向的推导。

**Demostración.** Intercambiar dos ecuaciones no altera que todas deban cumplirse; un segundo intercambio restaura el sistema. Reemplazar una ecuación por su múltiplo $\lambda\ne0$ es reversible multiplicando por $1/\lambda$. En la tercera operación se sustituye la ecuación $E_i$ por $E_i+\lambda E_j$, manteniendo $E_j$. Si se satisfacen $E_i,E_j$, se satisface la suma. Si se satisfacen $E_i+\lambda E_j$ y $E_j$, restar $\lambda E_j$ recupera $E_i$. Esto prueba ambos sentidos.

Sea $E$ el resultado de hacer la operación sobre $I_m$. La fórmula de producto muestra que la fila $i$ de $EA$ es la combinación de filas indicada por la fila $i$ de $E$; lo mismo ocurre con $Eb$. La operación inversa también se representa por una matriz $F$. Aplicar ambas sucesivamente a cada columna de $I_m$ da $FE=EF=I_m$. Luego $E$ es invertible. Una sucesión produce $S=E_k\cdots E_1$, con inversa $E_1^{-1}\cdots E_k^{-1}$.

**Explicación — Español.** La suma de una ecuación consigo misma no se incluye como caso $i=j$ de la tercera operación: podría anularla. La restricción evita ese problema.

**中文解释。** 矩阵 $S$ 记录了整个过程，且可逆。因此从 $SAx=Sb$ 可以乘回 $S^{-1}$，恢复原方程组。

**Conclusión.** Se prueba T1, incluido su fundamento matricial.

## P2. Terminación de Gauss y parametrización por sustitución

**Hipótesis.** Una matriz ampliada finita $(A\mid b)$ con $m$ filas y $n$ columnas de coeficientes.

**Tesis.** Se puede escalonar; sin contradicción, cada elección de variables libres determina exactamente una solución.

**Estrategia — Español.** Avanzar siempre hacia una nueva columna o una nueva fila; después resolver las ecuaciones pivote de abajo hacia arriba.

**策略 — 中文。** 有限指标保证算法结束，非零主元保证回代每一步既可执行又唯一。

**Demostración.** En una columna activa, si hay un coeficiente no nulo entre las filas activas, se intercambia para colocarlo primero. Para anular una entrada inferior $a$, se resta de su fila $(a/p)$ veces la fila pivote, donde $p\ne0$ es el pivote. Así aparecen ceros debajo y no se cambian las columnas pivote anteriores, cuyos coeficientes en las filas activas ya son cero. Se avanza una fila y se prosigue a la derecha. Si no hay entrada no nula, se avanza solo de columna. Como solo existen $m$ filas y $n$ columnas, el proceso termina en forma escalonada.

Si una fila tiene todos sus coeficientes cero y término independiente $c\ne0$, ninguna asignación satisface $0=c$. En ausencia de tal fila, sean $j_1<\cdots<j_r$ las columnas pivote. Se asignan arbitrariamente las $n-r$ coordenadas no pivote. La última ecuación pivote contiene su variable con coeficiente no nulo y solo variables situadas a su derecha; estas ya están fijadas. Despejar determina una única variable. Repitiendo hacia arriba se obtiene una asignación que satisface todas las ecuaciones no nulas, y las nulas se cumplen automáticamente. La reversibilidad de P1 devuelve una solución del sistema original. Cualquier solución con las mismas coordenadas libres debe tener los mismos valores pivote por el mismo razonamiento descendente.

**Explicación — Español.** Se ha probado tanto existencia como unicidad para cada elección de parámetros. Si el sistema tiene más incógnitas que ecuaciones, necesariamente queda alguna variable libre cuando es compatible.

**中文解释。** 主元数不超过行数。以后证明秩时使用这一算法事实，不依赖尚未证明的秩公式，因此没有循环论证。

**Conclusión.** Se prueba T2. Gauss–Jordan puede continuar normalizando los pivotes y anulando encima, también por operaciones reversibles.

## P3. Las relaciones entre columnas se conservan

**Hipótesis.** $U=SA$ con $S$ producto de matrices elementales invertibles; columnas $a_j$ de $A$ y $u_j=Sa_j$ de $U$.

**Tesis.** Para cualesquiera escalares $\lambda_j$,

$$
\sum_j\lambda_ja_j=0\iff\sum_j\lambda_ju_j=0.
$$

**Estrategia — Español.** Multiplicar la relación por $S$ o por $S^{-1}$.

**策略 — 中文。** 变换前后用完全相同的系数，才能保留“哪些原列之间相关”的信息。

**Demostración.** Si la primera suma es cero, la distributividad da $\sum_j\lambda_jSa_j=S0=0$. Recíprocamente, si esta última suma es cero, multiplicar por $S^{-1}$ da $\sum_j\lambda_ja_j=0$. Para estudiar un subconjunto de columnas basta fijar en cero los coeficientes restantes. Por tanto cada subconjunto es independiente antes si y solo si lo es después; su cardinal máximo, el rango, se conserva. Asimismo, una expresión de una columna como combinación de otras conserva sus coeficientes.

**Explicación — Español.** No se deduce que $a_j=u_j$ ni que sus espacios generados sean el mismo subconjunto de $\mathbb K^m$; solo se transportan mediante $S$.

**中文解释。** 行交换会把列向量的坐标交换，可能把一条直线换到另一条直线；但同一批列之间的代数关系保持。

**Conclusión.** Queda probado el invariante necesario para definir y calcular el rango sin depender del camino de Gauss.

## P4. El rango de una escalonada es su número de pivotes

**Hipótesis.** $U$ escalonada con $r$ filas no nulas y columnas pivote $j_1<\cdots<j_r$.

**Tesis.** $\operatorname{rg}(U)=r$ y sus columnas pivote generan las demás.

**Estrategia — Español.** Usar el bloque de filas no nulas y columnas pivote, que es triangular con diagonal no nula. Justificar también por qué no caben $r+1$ columnas independientes.

**策略 — 中文。** 找到 $r$ 个独立列只证明秩至少为 $r$；还必须证明任何更多列都相关，才得出相等。

**Demostración.** Si $r=0$, $U$ es nula y ninguna columna no vacía es independiente; el rango es cero. Sea $r>0$. Al tomar las primeras $r$ filas y las $r$ columnas pivote se obtiene una matriz triangular superior $D$ con diagonal no nula. La sustitución descendente de P2 implica que $D\alpha=0$ solo tiene $\alpha=0$. Por tanto las columnas pivote de $U$ son independientes.

Sea $u$ cualquier columna de $U$. Sus últimas $m-r$ entradas son cero. P2 aplicado a $D\alpha=(u_1,\ldots,u_r)^{\mathsf T}$ da una solución única porque hay un pivote por variable. Con estos coeficientes, la combinación de las columnas pivote coincide con $u$ en las primeras $r$ posiciones y también en las restantes, que son cero. Así todas las columnas se generan con ellas.

Para justificar la cota superior sin usar aún teoremas de dimensión, elijamos $q>r$ columnas cualesquiera de $U$. Buscar una combinación nula de ellas equivale a un sistema homogéneo de $r$ ecuaciones con $q$ incógnitas, pues las últimas filas son cero. Según P2 hay a lo sumo $r$ pivotes, y al menos una variable libre. Asignar $1$ a una libre y $0$ a las demás produce una solución no nula de coeficientes. Las $q$ columnas son dependientes. Luego el máximo número de columnas independientes es exactamente $r$.

Por P3, el rango de $A$ es el de cualquier escalonada $U$ y los índices pivote identifican columnas originales independientes que generan las restantes. Esto prueba además que todo escalonamiento tiene el mismo número de pivotes.

**Explicación — Español.** La definición de rango es independiente del algoritmo; P4 demuestra que el algoritmo calcula esa cantidad. No se ha usado rango–nulidad ni determinantes.

**中文解释。** 证明用到了“未知量多于方程的齐次系统有非零解”，但它已在 P2 中通过自由变量直接得到，因此不是偷用秩结论来证明秩本身。

**Conclusión.** Se obtiene T3 y la cota $r\le\min(m,n)$.

## P5. Igualdad de rango de filas y columnas

**Hipótesis.** $A$ se reduce a una escalonada $U$ con $r$ filas no nulas.

**Tesis.** El máximo número de filas independientes de $A$ es $r$.

**Estrategia — Español.** Las operaciones por filas conservan su espacio generado. Las filas no nulas de $U$ son independientes; luego controlar el tamaño máximo de cualquier familia en ese espacio.

**策略 — 中文。** 行本身会改变，但所有原行能生成的向量集合不变；这里与 P3 的“列关系不变”是不同的不变量。

**Demostración.** Cada fila nueva es combinación de las antiguas y, por reversibilidad, cada antigua es combinación de las nuevas. Los dos conjuntos de filas generan el mismo espacio. Las $r$ filas no nulas $w_1,\ldots,w_r$ de $U$ son independientes: en una relación $\sum\alpha_iw_i=0$, la columna pivote de la primera fila fuerza $\alpha_1=0$; después la de la segunda fuerza $\alpha_2=0$, y así hasta $\alpha_r=0$.

Cualquier familia de $q>r$ vectores del espacio común tiene expresiones mediante $w_1,\ldots,w_r$. Sus coeficientes forman una matriz $r\times q$. Como en P4, el sistema homogéneo de esos coeficientes tiene solución no nula, que da una dependencia de los $q$ vectores. Por tanto ninguna familia independiente del espacio tiene más de $r$ elementos.

Falta asegurar que entre las filas originales se pueden seleccionar $r$ independientes. Tome una subfamilia independiente maximal de ellas. Cada fila no seleccionada pertenece a su generado: en efecto, al añadirla aparece una dependencia y su coeficiente debe ser no nulo, pues las seleccionadas eran independientes; despejarla da la combinación. Si se hubieran seleccionado $q<r$, las $r$ filas independientes de $U$, expresadas mediante esas $q$ generadoras, serían dependientes por el mismo argumento de sistema homogéneo. Contradicción. Por tanto la selección tiene $r$ elementos y el rango de filas coincide con el de columnas.

**Explicación — Español.** Se han demostrado las dos desigualdades, no solo que las filas escalonadas son independientes.

**中文解释。** “消元后的非零行独立”并不足以直接声称原矩阵也有同样数量的独立原行；最后的极大无关组选取补上了这个推理环节。

**Conclusión.** Se completa T3, incluida la igualdad de ambos rangos.

## P6. Rouché–Frobenius y clasificación

**Hipótesis.** $A\in M_{m\times n}(\mathbb K)$, $b\in\mathbb K^m$; se aplica Gauss a las columnas de coeficientes de $(A\mid b)$.

**Tesis.** El criterio de compatibilidad y las tres clases de T4, con $n-r$ parámetros en el caso compatible.

**Estrategia — Español.** Comparar $(U\mid c)$ con $U$; los únicos pivotes adicionales posibles están en la última columna y en filas con coeficientes cero.

**策略 — 中文。** 先保持系数部分为阶梯形。若零系数行对应的右端非零，就有矛盾，也恰好产生增广矩阵多出的一个主元。

**Demostración.** Sea $U$ escalonada con $r$ filas no nulas. Por P3–P4, $\operatorname{rg}(A)=r$ y $\operatorname{rg}(A\mid b)=\operatorname{rg}(U\mid c)$, porque se hicieron operaciones completas. Si $c_i=0$ para toda fila $i>r$, $(U\mid c)$ ya tiene $r$ filas no nulas y rango $r$. P2 da soluciones.

Si algún $c_i\ne0$ con $i>r$, esa ecuación es $0=c_i$ y no hay soluciones. Se intercambia tal fila a la posición $r+1$, se normaliza su entrada de la última columna y se eliminan las entradas de esa columna en las filas inferiores. Queda una escalonada con $r+1$ pivotes. Por P4 el rango ampliado es $r+1$. Esto prueba ambas implicaciones de compatibilidad y las cotas del rango ampliado.

Si el sistema es compatible, P2 establece una correspondencia biyectiva entre las soluciones y $\mathbb K^{n-r}$. Si $r=n$, no hay variables libres y la solución es única. Si $r<n$, existe al menos una libre. Variar esa coordenada produce soluciones distintas; como $\mathbb Q,\mathbb R,\mathbb C$ son infinitos, hay infinitas soluciones. Sobre un cuerpo finito de $q$ elementos, el mismo argumento daría exactamente $q^{n-r}$ soluciones.

Finalmente, la entrada $i$ de $Ax$ es $\sum_j a_{ij}x_j$, que es la entrada $i$ de $\sum_jx_ja_j$. Así $Ax=b$ equivale a expresar $b$ como combinación de las columnas, probando T5 y conectando con la prueba de AL-AP-004 p. 20.

**Explicación — Español.** La eliminación prueba el criterio sin presuponer el lenguaje de dimensiones. La formulación por columnas expresa el mismo hecho algebraico y corrige los errores de tipos de la diapositiva.

**中文解释。** $n$ 是未知量数，不是方程数；无限多解还依赖标量域无限。增广秩只能增加至多 1，因为右端只有一列。

**Conclusión.** Se prueban T4 y T5 con todas sus condiciones.

## P7. Solución particular más soluciones homogéneas

**Hipótesis.** $Ax_p=b$ y $r=\operatorname{rg}(A)$.

**Tesis.** T6 y unicidad de sus parámetros.

**Estrategia — Español.** Restar una solución particular y construir los vectores homogéneos con coordenadas libres canónicas.

**策略 — 中文。** 先证明解集的平移等式，再证明那组齐次方向确实生成全部解且无重复参数。

**Demostración.** Si $Ah=0$, entonces $A(x_p+h)=Ax_p+Ah=b$. Si $Ax=b$, entonces $A(x-x_p)=b-b=0$. Ambas inclusiones prueban la igualdad de conjuntos.

Sea $d=n-r$ y sean $h_j$ las soluciones homogéneas obtenidas al poner $1$ en la $j$-ésima coordenada libre y cero en las restantes; existen y son únicas por P2. Para cualquier elección $t_1,\ldots,t_d$, $h=\sum_j t_jh_j$ satisface $Ah=0$ y tiene coordenadas libres $t_1,\ldots,t_d$. Por la unicidad de P2, es la única solución homogénea con esas coordenadas. De ahí que se obtengan todas las homogéneas. Si dos sumas dan el mismo vector, sus coordenadas libres coinciden, y todos los parámetros son iguales.

**Explicación — Español.** La elección de $x_p$ no es única cuando hay parámetros, pero el conjunto trasladado sí es el mismo. La diferencia entre dos soluciones particulares es homogénea.

**中文解释。** $x_p$ 换成另一个特解，只会改变“从哪个点开始描述”，不会改变解集本身。若 $b\ne0$，零向量不是解，因此解集不能直接当作过原点的子空间。

**Conclusión.** Se prueba T6 sin usar una fórmula de dimensión aún no estudiada.

## P8. Inversa, rango completo y cálculo por Gauss–Jordan

**Hipótesis.** $A\in M_{n\times n}$.

**Tesis.** Las equivalencias y el algoritmo de T7; unicidad de la inversa.

**Estrategia — Español.** Relacionar ausencia de variables libres con Gauss–Jordan y registrar las operaciones por una matriz invertible $S$.

**策略 — 中文。** 不把“左逆自动是右逆”当作未证明事实，而是利用初等变换矩阵本来就可逆这一已证结论。

**Demostración.** Si $A$ tiene inversa y $Ah=0$, multiplicar por $A^{-1}$ da $h=0$. Por P2 y P4, el sistema homogéneo solo tiene cero si y solo si no tiene variables libres, esto es, si y solo si $\operatorname{rg}(A)=n$.

Si el rango es $n$, Gauss–Jordan lleva $A$ a $I_n$: hay un pivote en cada fila y columna, y se normalizan y anulan las entradas superiores. Sea $S$ la matriz de operaciones de P1; entonces $SA=I_n$ y $S$ es invertible. Multiplicar por $S^{-1}$ da $A=S^{-1}$, luego $AS=I_n$. Por tanto $S=A^{-1}$. Aplicar las mismas operaciones a $(A\mid I_n)$ da $(I_n\mid S)$.

Si $A$ es invertible, para cualquier $b$ el vector $A^{-1}b$ es solución y cualquier solución $x$ satisface $x=A^{-1}b$; es única. Recíprocamente, si cada $Ax=b$ tiene solución única, en particular $Ax=0$ solo tiene cero, y por los pasos anteriores $A$ es invertible. Quedan conectadas las cuatro afirmaciones.

Si $B$ y $C$ son inversas, entonces $B=B(AC)=(BA)C=C$, usando asociatividad. Si el rango es menor que $n$, Gauss–Jordan no puede producir $I_n$ porque el rango se conserva.

**Explicación — Español.** No se necesita el determinante para esta equivalencia. El tamaño cuadrado es esencial: para matrices rectangulares, una inyectividad o sobreyectividad aislada no garantiza inversa bilateral.

**中文解释。** 求逆右侧得到的每一列都是一个标准右端的解；矩阵 $S$ 的可逆性也使最后得到的确实是双侧逆。

**Conclusión.** Se prueba T7, incluida la legitimidad del algoritmo.

## P9. Varios sistemas con la misma matriz

**Hipótesis.** $B=(b^{(1)}\ \cdots\ b^{(k)})$ y $X=(x^{(1)}\ \cdots\ x^{(k)})$.

**Tesis.** T8.

**Estrategia — Español.** Comparar columnas y aplicar a todas ellas las mismas operaciones.

**策略 — 中文。** 一个矩阵方程按列拆开，每一列都由相同系数矩阵作用；行变换不混合不同右端的未知列。

**Demostración.** La columna $j$ de $AX$ es $Ax^{(j)}$ por la definición de producto. Por tanto $AX=B$ equivale a $Ax^{(j)}=b^{(j)}$ para todo $j$. Si $S$ registra operaciones invertibles, $AX=B$ equivale a $SAX=SB$. Las columnas de $SB$ son $Sb^{(j)}$, de modo que cada sistema conserva sus soluciones. Si $A$ es invertible, multiplicar por $A^{-1}$ da $X=A^{-1}B$; la sustitución confirma que esta matriz satisface la ecuación y el paso reversible prueba su unicidad.

**Explicación — Español.** Cuando $A$ es singular, la comprobación de contradicciones se hace para cada término independiente; no se debe declarar que todos tienen la misma compatibilidad solo porque comparten $A$.

**中文解释。** 同一系数矩阵对应的两个不同右端可以一个相容、另一个不相容，这是学习增广矩阵时应保留的区别。

**Conclusión.** Se prueba T8. Continúe con [ejemplos completos](04_Ejemplos.md).
