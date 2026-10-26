---
title: Combinaciones, generadores e independencia / 线性组合、生成与无关
subject: Álgebra Lineal
tema: Guía 2.3
type: theorem
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_2_3
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-012/Temas 1 y 2(1)(2).pdf
updated: 2026-10-26
---

# Combinaciones, generadores e independencia — 线性组合、生成与无关

**Fuentes verificadas:** AL-AP-012, pp. 8–11. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.

**Organización:** esta unidad integra motivación, definiciones, teoremas, pruebas, conexiones y repaso en un archivo; ejemplos, ejercicios y soluciones se mantienen separados.


## Motivación y definiciones

**Español.** Una lista puede construir muchos vectores y aun contener información repetida. Generar estudia todo lo que se puede construir; independencia estudia si existe redundancia. Son dos preguntas distintas. **中文。** 生成是“够不够覆盖目标”，无关是“有没有可删的重复信息”；单独满足其中一个都不能自动推出另一个。

Sea $V$ un $\mathbb K$-espacio. Una combinación lineal de $v_1,\ldots,v_r$ es $\sum_{i=1}^r a_iv_i$ con $a_i\in\mathbb K$. Su generado $\langle v_1,\ldots,v_r\rangle$ es el conjunto de todas esas sumas. La lista genera $V$ si ese conjunto es $V$. Es linealmente independiente（线性无关）si

$$
\sum_i a_iv_i=0_V\Longrightarrow a_1=\cdots=a_r=0;
$$

es dependiente si existe una relación nula no trivial. Para un conjunto $S$ posiblemente infinito, $\langle S\rangle$ utiliza solo sumas **finitas**; independencia significa que cada subfamilia finita distinta es independiente. Por convenio la familia vacía es independiente y genera $\{0_V\}$.

**Español.** Las familias tienen índices: repetir un mismo vector dos veces da una lista dependiente, aunque el conjunto que olvida repeticiones cambie. El cuerpo de escalares es parte del problema. **中文。** 不能在处理无限个函数时擅自把“有限线性组合”换成无穷级数；那需要额外的收敛结构。

## T1. El generado es el menor subespacio

**Hipótesis.** $S\subset V$. **Tesis.** $\langle S\rangle$ es subespacio, contiene $S$ y está incluido en todo subespacio que contiene $S$.

**Estrategia ES.** Combinar sumas finitas y usar clausura de cualquier subespacio. **策略中文。** 分别证明“它是子空间”和“它是最小的”，不只举生成向量的例子。

**Demostración.** La suma vacía es cero. Sumar dos combinaciones finitas produce una combinación finita de la unión de sus soportes; multiplicarla por un escalar multiplica sus coeficientes. El criterio de subespacio prueba la primera afirmación. Cada $s\in S$ se escribe $1s$. Si $W$ contiene $S$, su clausura incluye todas las combinaciones finitas de elementos de $S$, luego $\langle S\rangle\subset W$. **Explicación ES.** La minimalidad es una inclusión universal, no una comparación del tamaño de listas. **中文解释。** “由这些向量生成”确定的是一个子空间，而不是某一种特定参数写法。**Conclusión.** Se justifica el concepto de generado.

## T2. Dependencia y eliminación de redundancias

**Enunciado.** Una lista finita no vacía es dependiente si y solo si algún vector es combinación de los otros. Suprimir ese vector no cambia el generado.

**Hipótesis/Tesis.** Probar la equivalencia y la igualdad de generados. **Estrategia ES.** Despejar un coeficiente no nulo. **策略中文。** 非平凡关系保证至少有一个可除的非零系数。

**Demostración.** De $\sum a_iv_i=0$ con algún $a_j\ne0$ resulta $v_j=-\sum_{i\ne j}(a_i/a_j)v_i$. A la inversa, una expresión $v_j=\sum_{i\ne j}b_iv_i$ da una relación nula con coeficiente $1$ en $v_j$, no trivial. Al suprimirlo, toda combinación antigua puede sustituir su término usando esa expresión, por lo que queda dentro del generado restante. La inclusión opuesta es inmediata porque se utilizan menos generadores. **Explicación ES.** Solo se puede eliminar un vector cuya expresión se haya justificado. **中文解释。** “向量多”不直接等于某个特定向量冗余，必须展示关系。**Conclusión.** Se obtiene el mecanismo para extraer bases.

## T3. Añadir un vector y unicidad de coeficientes

**Enunciado.** Si $v_1,\ldots,v_r$ son independientes, añadir $w$ conserva independencia si y solo si $w\notin\langle v_1,\ldots,v_r\rangle$. Además, una familia es independiente si y solo si cada vector de su generado admite una única expresión en ella.

**Estrategia ES.** Separar el coeficiente de $w$ y restar dos representaciones. **策略中文。** 两种表示之差会产生零向量关系，这把“唯一”与“无关”连接起来。

**Demostración.** Si $w$ está en el generado, T2 da dependencia. Si $\sum a_iv_i+bw=0$ y $w$ no está, $b\ne0$ permitiría despejar $w$, contradicción. Así $b=0$ y la independencia inicial fuerza todos los $a_i=0$. Para la unicidad, dos representaciones de un vector se restan: $\sum(a_i-b_i)v_i=0$; independencia da $a_i=b_i$. Recíprocamente, el cero ya tiene representación con todos los coeficientes cero; si la representación es única, ninguna relación no trivial puede dar cero. **Conclusión.** Todas las equivalencias quedan probadas.

**Explicación ES.** «Cada vector del generado» siempre tiene existencia por definición; lo nuevo es unicidad. Para hablar de todo $V$ hace falta además generar $V$. **中文解释。** 无关保证不重复，生成保证不遗漏，两者将在基的定义中合并。

## Cálculo, límites y repaso

En $\mathbb K^n$, colocar los vectores como columnas en $A$ convierte independencia en que $Ac=0$ solo tenga cero; pertenencia de $b$ al generado equivale a compatibilidad de $Ac=b$. Gauss ya demuestra estos hechos sin necesidad de determinantes. Las columnas pivote se seleccionan de la matriz original.

前置为 [子空间](../02_Espacios_Subespacios/01_Teoria_Demostraciones.md)，后续为 [基与维数](../04_Bases_Dimension/01_Teoria_Demostraciones.md)。Repaso ES: distinguir existencia de coeficientes, unicidad y papel del cuerpo; justificar cada vector eliminado. 中文：自测需要覆盖零向量、重复向量、空族及无限族的有限支持约定。继续 [例题](04_Ejemplos.md)、[题目](05_Ejercicios.md) 与 [解答](06_Soluciones.md)。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
