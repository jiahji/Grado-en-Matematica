---
title: Espacios de tipo no finito / 非有限型向量空间
subject: Álgebra Lineal
tema: Guía 2.8
type: theorem
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_2_8
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-012/Temas 1 y 2(1)(2).pdf
updated: 2026-10-26
---

# Espacios de tipo no finito — 非有限型向量空间

**Fuentes verificadas:** AL-AP-012, p. 4: ejemplos de sucesiones y funciones; desarrollo posterior como suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.

**Organización:** esta unidad integra motivación, definiciones, teoremas, pruebas, conexiones y repaso en un archivo; ejemplos, ejercicios y soluciones se mantienen separados.


## Motivación y definiciones

**Español.** Un espacio puede contener familias independientes de cualquier longitud. En tal caso, ninguna lista finita de coordenadas puede describir todos sus elementos. Los ejemplos de sucesiones y funciones de AL-AP-012 p. 4 conducen a esta distinción. **中文。** 对无限对象仍只允许有限项的代数线性组合；不能把无限展开与基的定义混为一谈。

$V$ es de tipo no finito（非有限型）si no tiene conjunto generador finito. Una base algebraica o de Hamel（代数基）es independiente y genera mediante combinaciones finitas. Para una sucesión infinita de vectores, cada relación usada en independencia tiene solo finitos coeficientes no nulos.

## T1. Familias independientes arbitrariamente largas

**Enunciado.** Si para todo entero $n$ hay $n$ vectores independientes en $V$, entonces $V$ no es de tipo finito. **Estrategia ES.** Suponer una lista generadora finita y extraer base. **策略中文。** 用有限维交换定理产生矛盾，不使用无限维的维数减法。

**Demostración.** Si hubiera $r$ generadores, se extraería una base con $d\le r$ elementos por 2.4. Pero una familia independiente con $r+1$ elementos violaría Steinitz frente a esa base. Así no hay tal lista. A la inversa, si $V$ no es de tipo finito, empezar con la familia vacía y añadir un vector fuera de su generado, que nunca puede ser todo $V$ después de finitos pasos. El lema de 2.3 conserva independencia, de modo que se construyen listas de cualquier longitud. **Conclusión.** La caracterización es exacta. **中文解释。** 这里每次只需有限步选取，不需要先建立一个任意无限空间的基。

## T2. Polinomios y sucesiones

$\mathbb K[x]$ tiene base $(1,x,x^2,\ldots)$: todo polinomio tiene solo finitos coeficientes y una relación finita nula fuerza cada coeficiente a cero. Por T1 es no finito.

Sea $\mathbb K^{\mathbb N}$ el espacio de todas las sucesiones, operaciones coordenadas. Los $e_n$ con un $1$ en una sola posición son independientes: evaluar en la posición de cada coeficiente lo recupera. Pero su generado es solo

$$
\mathbb K^{(\mathbb N)}=\{(a_n):\text{solo finitos }a_n\ne0\},
$$

un subespacio propio de todas las sucesiones, porque $(1,1,1,\ldots)$ no pertenece. La lista $(e_n)$ es base del soporte finito, **no** de todas las sucesiones. **Demostración de clausura.** La unión de dos soportes finitos es finita y multiplicar por un escalar no crea nuevas posiciones, así el soporte finito es subespacio. **中文解释。** 把全 1 序列写成“$e_1+e_2+\cdots$”使用了未经定义的无穷求和，不能作为代数生成证明。

## T3. Propiedades finitas que fallan

**Enunciado.** Un subespacio propio puede tener una base del mismo tamaño infinito que el ambiente. Una aplicación lineal de un espacio a sí mismo puede ser inyectiva y no sobreyectiva, o a la inversa.

**Estrategia ES.** Dar construcciones explícitas en polinomios. **策略中文。** 不能把有限维等维判别无条件推广。

**Demostración.** $x\mathbb R[x]$ es propio porque no contiene $1$, pero tiene base $x,x^2,\ldots$, en biyección con la base $1,x,x^2,\ldots$ del ambiente. La regla $S(p)=xp$ es inyectiva: comparar coeficientes en $xp=0$ obliga $p=0$; no es sobreyectiva porque no obtiene $1$. La derivada $D$ tiene constantes en su núcleo, así no es inyectiva. Es sobreyectiva sobre $\mathbb R[x]$: para $q=\sum_{k=0}^d a_kx^k$, el polinomio $p=\sum_{k=0}^d a_kx^{k+1}/(k+1)$ cumple $D(p)=q$. Ambas reglas respetan sumas y escalares por sus fórmulas. **Conclusión.** Cada fallo se verifica con la propiedad específica. **中文解释。** 移位丢掉的是某些输出，求导丢掉的是常数信息，两者方向不同。

## Bases generales: principio usado y límite

Como ampliación fundacional, **si se admite el lema de Zorn**, todo espacio tiene base. Prueba condicional: ordenar por inclusión todos los subconjuntos independientes; la familia no es vacía pues incluye el vacío. La unión de una cadena es independiente porque cualquier subfamilia finita está contenida en un miembro de la cadena. Zorn da un independiente maximal $B$. Si un $v$ no perteneciera a $\langle B\rangle$, el criterio de añadir un vector conservaría independencia, contradiciendo maximalidad. Así genera. No se presenta aquí una demostración del lema de Zorn, principio de teoría de conjuntos externo al contenido algebraico; los ejemplos concretos anteriores no lo necesitan.

**Explicación ES.** La familia de vectores canónicos genera únicamente las sucesiones de soporte finito; escribir una suma infinita no demuestra generación algebraica. La existencia de una base arbitraria es la ampliación condicional a Zorn, mientras los ejemplos explícitos tienen pruebas independientes de él.

## Repaso y conexiones

**Español.** Separar soporte finito, sumas infinitas, cardinal de una base y dimensión finita; no usar una resta de infinitos para clasificar sistemas. **中文。** 本节的核心是可明确展示的多项式、数列、函数空间，不以未证明的无限求和代替定义。前置 [基与维数](../04_Bases_Dimension/01_Teoria_Demostraciones.md)，后续线性映射单满射会复用这些反例。读 [例题](04_Ejemplos.md)、[练习](05_Ejercicios.md)、[解答](06_Soluciones.md)。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
