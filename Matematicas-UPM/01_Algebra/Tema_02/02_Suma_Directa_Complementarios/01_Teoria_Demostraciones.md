---
title: Intersección, suma y complementarios / 交、和、直和与补空间
subject: Álgebra Lineal
tema: Guía 2.6
type: theorem
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_2_6
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-012/Temas 1 y 2(1)(2).pdf
updated: 2026-10-26
---

# Intersección, suma y complementarios — 交、和、直和与补空间

**Fuentes verificadas:** AL-AP-012, pp. 24–33. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.

**Organización:** esta unidad integra motivación, definiciones, teoremas, pruebas, conexiones y repaso en un archivo; ejemplos, ejercicios y soluciones se mantienen separados.


## Motivación y definiciones

**Español.** Para combinar restricciones se intersectan subespacios; para combinar direcciones se suman. La unión no hace ninguna de estas dos operaciones correctamente en general. **中文。** “同时满足”与“用两边向量共同生成”是两种不同逻辑。

Sean $U,W\le V$. Se define $U+W=\{u+w:u\in U,w\in W\}$. La suma es **directa（直和）** si $U\cap W=\{0\}$, y se escribe $U\oplus W$. Son **complementarios（互补子空间）** si además $U+W=V$. La palabra directa por sí sola no afirma que se obtenga todo $V$.

## T1. Intersección, suma y unión

**Enunciado.** Toda intersección de subespacios es subespacio; $U+W$ es el menor subespacio que contiene ambos. $U\cup W$ es subespacio si y solo si uno está contenido en el otro.

**Estrategia ES.** Aplicar combinaciones arbitrarias; para la unión, construir dos vectores de lados distintos. **策略中文。** 交要求每个条件同时成立，和需要允许跨两边相加。

**Demostración.** Cero pertenece a cada subespacio, y una combinación de dos vectores de la intersección pertenece a todos ellos. Para la suma, cero es $0+0$, y $a(u+w)+b(u'+w')=(au+bu')+(aw+bw')$ pertenece a $U+W$. Contiene $U$ y $W$ porque pueden sumarse con cero; cualquier subespacio que contenga ambos contiene todas sus sumas, probando minimalidad.

Si $U\subset W$ o viceversa, la unión es el mayor de ellos. Si ninguna inclusión vale, escoja $u\in U\setminus W$, $w\in W\setminus U$. Si $u+w$ perteneciera a $U$, restar $u$ pondría $w$ en $U$, contradicción; si perteneciera a $W$, restar $w$ pondría $u$ en $W$. Así no está en la unión, que falla clausura. **Conclusión.** Se prueban ambas direcciones. **中文解释。** 两子空间的并集失败不是例外细节，而是跨方向加法被漏掉的必然结果。

## T2. Directa equivale a descomposición única

**Hipótesis.** $U,W$ subespacios. **Tesis.** $U\cap W=0$ si y solo si cada $v\in U+W$ tiene una única expresión $v=u+w$.

**Estrategia ES.** Restar dos descomposiciones y usar la intersección. **策略中文。** 生成定义已保证存在，直和条件新增的是唯一。

**Demostración.** Si $u+w=u'+w'$, entonces $u-u'=w'-w\in U\cap W$. Si la intersección es cero, ambas diferencias son cero y la descomposición es única. Recíprocamente, para $z\in U\cap W$, el cero tiene descomposiciones $0+0=z+(-z)$ con los sumandos en los conjuntos indicados. La unicidad fuerza $z=0$. **Explicación ES.** Si se requiere descomponer todo $V$, hace falta además $U+W=V$. **中文解释。** 这修正课堂 p. 29 把和空间的基误说成整个环境空间的基所缺的条件。**Conclusión.** Se obtiene el criterio completo.

## T3. Bases de sumas directas y existencia de complementarios

**Hipótesis.** $V$ finito, bases $B_U,B_W$. **Tesis.** Si la suma es directa, concatenarlas da base de $U+W$. Todo subespacio de $V$ tiene un complementario.

**Estrategia ES.** Usar unicidad para independencia y completar una base. **策略中文。** 先在和空间证明拼接基，再加上张满环境的条件。

**Demostración.** Cada $u+w$ se expresa usando ambas bases. Una relación entre la lista concatenada se separa como $u+w=0$. Por T2, $u=w=0$, y por independencia de cada base todos los coeficientes son cero. Luego es base de la suma, que solo es base de $V$ si la suma lo llena.

Para existencia, tome una base $(u_1,\ldots,u_r)$ de $U$ y complétela a $(u_1,\ldots,u_r,w_1,\ldots,w_s)$ de $V$ por Steinitz. Sea $W=\langle w_1,\ldots,w_s\rangle$. Toda combinación de la base total separa un elemento de $U$ y uno de $W$. Si ambos representan el mismo vector, restar sus expresiones da una relación de la base total, forzando todos los coeficientes cero; su intersección es cero. Así $V=U\oplus W$. **Conclusión.** Existe un complementario; no se ha afirmado que sea único. **中文解释。** 在无限维环境中推广存在性需要额外的选基原理，本单元有限维证明不偷用该结论。

## Métodos de cálculo y repaso

Para intersecar, expresar ambos subespacios por ecuaciones en la misma base y reunir las ecuaciones. Para sumar, reunir generadores y extraer independientes. Alternativamente resolver $G\alpha=H\beta$ obtiene vectores comunes; si las columnas son redundantes, los parámetros pueden no ser únicos y se deben reducir los vectores resultantes.

前置 [坐标与方程](../01_Coordenadas_Ecuaciones/01_Teoria_Demostraciones.md)，后续 [Grassmann](../03_Grassmann/01_Teoria_Demostraciones.md)。自测 ES: demostrar por qué unión y suma difieren, y distinguir directa de complementarios. 中文：切勿把“某个补空间”当作唯一标准对象；补空间通常有很多。见 [例题](04_Ejemplos.md)、[练习](05_Ejercicios.md)、[解答](06_Soluciones.md)。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
