---
title: Coordenadas y ecuaciones / 坐标与子空间方程
subject: Álgebra Lineal
tema: Guía 2.5
type: theorem
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_2_5
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-012/Temas 1 y 2(1)(2).pdf
updated: 2026-10-26
---

# Coordenadas y ecuaciones — 坐标与子空间方程

**Fuentes verificadas:** AL-AP-012, pp. 19–23. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.

**Organización:** esta unidad integra motivación, definiciones, teoremas, pruebas, conexiones y repaso en un archivo; ejemplos, ejercicios y soluciones se mantienen separados.


## Motivación y definición

**Español.** Un vector es el objeto; sus coordenadas son una descripción dependiente de una base ordenada. Cambiar la descripción no cambia el vector. **中文。** 必须声明基的顺序，不能把非标准基坐标直接当作标准坐标来代入方程。

Sea $B=(b_1,\ldots,b_n)$ base ordenada. Para $v=\sum x_ib_i$, se define $[v]_B=(x_1,\ldots,x_n)^{\mathsf T}$. Existencia y unicidad proceden de 2.4. En $\mathbb K^n$, si $S$ tiene columnas $b_i$ escritas en la canónica, entonces $S[v]_B=v$. $S$ es invertible porque sus columnas forman base; las coordenadas se hallan resolviendo este sistema, no interpretando columnas como filas.

Una descripción paramétrica（参数描述）de $W$ es $[w]_B=Gc$ con parámetros $c$; una descripción implícita（隐式描述）es $A[w]_B=0$. Ambas dependen de la base. Los parámetros de una lista generadora redundante no son coordenadas únicas.

## T1. De implícitas a base paramétrica y dimensión

**Hipótesis.** $W=\{v:A[v]_B=0\}$, $A$ tiene $n$ columnas y rango $r$. **Tesis.** Gauss da una base de $W$ con $n-r$ elementos.

**Estrategia ES.** Tomar una solución por cada coordenada libre unitaria. **策略中文。** 参数化不仅要覆盖解，还要证明所得方向独立。

**Demostración.** Por el módulo Gauss, cada elección de las $d=n-r$ variables libres determina una única solución del sistema homogéneo. Para $j=1,\ldots,d$, sea $h_j$ la solución con la $j$-ésima libre igual a $1$ y las otras cero. Cada solución con libres $c_j$ es $\sum c_jh_j$, pues esta combinación es solución y tiene exactamente esas libres. Si $\sum c_jh_j=0$, mirar las libres da todos los $c_j=0$. Las coordenadas $h_j$ corresponden a los vectores $\sum_i(h_j)_ib_i$ de $W$; el mismo argumento de representación única conserva generación e independencia. Así forman base y $\dim W=n-r$. **Explicación ES.** Se resta el rango, no el número bruto de ecuaciones. **中文解释。** 重复方程不增加独立约束，原讲义 p. 21 的公式必须补上这个条件。**Conclusión.** Se justifica rigurosamente la conversión y el cómputo de dimensión.

## T2. De generadores a ecuaciones

**Hipótesis.** Las columnas de $G\in M_{n\times k}$ son coordenadas de generadores de $W$, con rango $r$. **Tesis.** Si las filas de $A$ son una base del sistema $G^{\mathsf T}a=0$, entonces $W=\{v:A[v]_B=0\}$.

**Estrategia ES.** Construir todas las ecuaciones que anulan las columnas y después comparar dimensiones. **策略中文。** 仅证明每个生成向量满足方程只得到包含关系，还要排除多余解。

**Demostración.** La igualdad $G^{\mathsf T}a=0$ equivale a $a^{\mathsf T}G=0$. Por T1 y la igualdad de rangos de filas y columnas, su espacio de soluciones tiene dimensión $n-r$. Tomar sus $n-r$ soluciones independientes como filas de $A$ produce $AG=0$ y rango de $A$ igual a $n-r$. Por tanto los vectores generados por $G$ satisfacen las ecuaciones: $W\subset\ker A$ en coordenadas. T1 da $\dim\ker A=n-(n-r)=r$. Las columnas pivote de $G$ forman base de su generado, también de dimensión $r$. La inclusión entre subespacios finitos de igual dimensión implica igualdad por 2.4. **Explicación ES.** Si se omiten ecuaciones independientes pueden quedar soluciones extra. **中文解释。** 左零空间给出全部线性约束，而不是任意挑几条看起来正确的条件。**Conclusión.** Se obtiene un procedimiento general sin usar determinantes.

## Uso, conexiones y repaso

La pertenencia paramétrica se comprueba resolviendo $Gc=[v]_B$; la implícita, evaluando $A[v]_B$. Una base paramétrica contiene exactamente $r$ parámetros únicos; una lista de $k>r$ generadores puede repetir descripciones. Las ecuaciones implícitas de subespacios son homogéneas. Un término independiente no nulo describe, si es compatible, un conjunto afín, no un subespacio.

前置 [基与维数](../../Tema_01/04_Bases_Dimension/01_Teoria_Demostraciones.md) 和 Gauss；后续交与和会分别拼接方程和生成向量。**Español.** El rango es una cantidad independiente de la representación redundante. **中文。** 自测要能从任一描述恢复另一描述，并标明所用坐标基。继续 [例题](04_Ejemplos.md)、[练习](05_Ejercicios.md)、[解答](06_Soluciones.md)。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
