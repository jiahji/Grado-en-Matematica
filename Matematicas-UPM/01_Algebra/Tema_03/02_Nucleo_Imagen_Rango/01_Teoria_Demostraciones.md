---
title: Núcleo, imagen y rango–nulidad / 核、像与秩–零化度
subject: Álgebra Lineal
tema: Guía 3.2
type: theorem
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_3_2
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-003/Tema 3_3783d906f8056ce104fc5d6bc1f5548c.pdf
updated: 2026-10-26
---

# Núcleo, imagen y rango–nulidad — 核、像与秩–零化度

**Fuentes verificadas:** AL-AP-003, pp. 9–13. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.

**Organización:** esta unidad integra motivación, definiciones, teoremas, pruebas, conexiones y repaso en un archivo; ejemplos, ejercicios y soluciones se mantienen separados.


## Motivación y definiciones

**Español.** El núcleo mide qué diferencias de entrada se vuelven invisibles; la imagen recoge qué salidas se pueden alcanzar. No son subconjuntos del mismo espacio en general. **中文。** 核属于定义域，像属于陪域；把它们混写在一起会造成对象类型错误。

Para $f:V\to W$ lineal, $\ker f=\{v:f(v)=0_W\}\subset V$, $\operatorname{Im}f=\{f(v):v\in V\}\subset W$. Para $E\subset W$, $f^{-1}(E)=\{v:f(v)\in E\}$ es **preimagen（原像）** y no supone que exista función inversa. Para $U\subset V$, $f(U)=\{f(u):u\in U\}$. Nulidad y rango son las dimensiones del núcleo y de la imagen cuando se usan dimensiones finitas.

## T1. Subespacios, imágenes y preimágenes

**Enunciado.** Núcleo e imagen son subespacios. La imagen de un subespacio y la preimagen de un subespacio son subespacios. Si $U=\langle u_1,\ldots,u_k\rangle$, $f(U)=\langle f(u_1),\ldots,f(u_k)\rangle$.

**Estrategia ES.** Usar el criterio de combinaciones y demostrar la igualdad de generados en ambos sentidos. **策略中文。** 原像不需要函数可逆；关键是目标集合对线性组合封闭。

**Demostración.** Cero pertenece a todos los conjuntos pertinentes porque $f(0)=0$. Si $f(u)=f(v)=0$, $f(au+bv)=0$, así el núcleo es subespacio. Si dos elementos de la imagen son $f(u),f(v)$, su combinación es $f(au+bv)$, todavía en la imagen; si $u,v$ pertenecen a un subespacio $U$, la misma combinación viene de $U$. Si $f(u),f(v)\in E$ y $E$ es subespacio, $f(au+bv)=af(u)+bf(v)\in E$, así la preimagen también lo es.

Todo $u\in U$ se escribe $\sum c_iu_i$, luego $f(u)=\sum c_if(u_i)$, probando una inclusión. Una combinación cualquiera de los $f(u_i)$ es $f(\sum c_iu_i)$ y su argumento pertenece a $U$, probando la otra. **Conclusión.** Se obtienen todas las afirmaciones de aula pp. 9–12. **中文解释。** 计算像最好从生成向量出发，计算原像最好把目标方程代入 $f$ 的表达式。

## T2. Teorema rango–nulidad

**Hipótesis.** $f:V\to W$ lineal y $\dim V=n<\infty$; $W$ puede ser infinito. **Tesis.** $\dim\ker f+\dim\operatorname{Im}f=n$.

**Estrategia ES.** Completar una base del núcleo y tomar las imágenes de los vectores añadidos. **策略中文。** 核中的方向映成零，其余方向应证明恰好给像的一组基。

**Demostración.** El núcleo, subespacio de un espacio finito, admite base $(u_1,\ldots,u_k)$. Complétese a $(u_1,\ldots,u_k,v_1,\ldots,v_{n-k})$ de $V$. Todo vector se expresa en esa base, y su imagen solo conserva $\sum b_jf(v_j)$; por tanto esas imágenes generan $\operatorname{Im}f$.

Si $\sum b_jf(v_j)=0$, entonces $\sum b_jv_j\in\ker f$ y existe una expresión $\sum a_iu_i$ igual a ella. Su resta es una relación nula en la base total, de donde todos los $b_j=0$ y todos los $a_i=0$. Las imágenes son independientes; su número es $n-k$, así rango $n-k$ y nulidad $k$. **Explicación ES.** El teorema incluye demostrar que la imagen es finita. **中文解释。** 对无限维空间不能在这里使用减法 $\infty-\infty$；打印材料中未重申的有限维前提在本库明确写出。**Conclusión.** La igualdad queda demostrada sin depender de la fórmula aún no probada del cociente.

## T3. Matrices y estructura de fibras

Para $f_A(x)=Ax$, las imágenes de la base canónica son las columnas de $A$, luego la dimensión de imagen coincide con el rango de columnas ya calculado por Gauss. Si $f(v_0)=w$, entonces

$$
f^{-1}(\{w\})=v_0+\ker f.
$$

**Prueba.** Si $f(v)=w$, $f(v-v_0)=0$; si $h\in\ker f$, $f(v_0+h)=w$. Ambas inclusiones demuestran la igualdad. Si $w$ no está en la imagen, la fibra es vacía. **中文解释。** 每个非空纤维的方向都是同一个核，但它不一定过原点；这解释方程组“特解加齐次解”。

**Explicación ES.** Una fibra no vacía es un traslado del núcleo y no necesariamente un subespacio: solo pasa por cero cuando la salida es cero. El teorema utiliza la dimensión finita del dominio, no una resta de cardinales infinitos.

## Cálculo y repaso

En bases, calcular núcleo equivale a resolver $Ax=0$; imagen se calcula seleccionando columnas originales pivote, no las columnas de la escalonada como si fueran iguales a las iniciales. Rango–nulidad debe comprobarse al final, no usarse para inventar una base incorrecta.

前置 [线性映射](../01_Linealidad/01_Teoria_Demostraciones.md) 和有限维基扩充；后续 [单满双射](../03_Inyectividad_Sobreyectividad/01_Teoria_Demostraciones.md)。自测 ES: distinguir cada ambiente y justificar generación e independencia en la prueba central. 中文：练习必须有原像、像及非空纤维，不只做核计算。[例题](04_Ejemplos.md)、[题目](05_Ejercicios.md)、[解答](06_Soluciones.md)。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
