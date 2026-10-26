---
title: Cambio de base y semejanza / 换基与相似
subject: Álgebra Lineal
tema: Guía 3.6
type: theorem
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_3_6
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-004/Tema 4_65298606b99b4fa875367ddfc0765632.pdf
updated: 2026-10-26
---

# Cambio de base y semejanza — 换基与矩阵相似

**Fuentes verificadas:** AL-AP-004, pp. 8–12. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.

**Organización:** esta unidad integra motivación, definiciones, teoremas, pruebas, conexiones y repaso en un archivo; ejemplos, ejercicios y soluciones se mantienen separados.


## Motivación y convención de aula

**Español.** El vector no cambia al cambiar base, pero sí la columna que lo describe. Hay dos cambios independientes en una aplicación: uno para la entrada y otro para la salida. **中文。** 方向与乘法顺序必须一起固定，不能靠记忆“一个逆夹一个矩阵”。

Se define $P_{B,C}=M_{B,C}(I_V)$: transforma **coordenadas en $B$ a coordenadas en $C$**. Sus columnas son $[b_j]_C$. Se conserva exactamente la dirección de AL-AP-004 pp. 8–11; la frase de p. 10 que menciona vectores de $C$ cuando debería usar los de $B$ está corregida en este desarrollo.

## T1. Fórmulas de transición

**Hipótesis.** $B,C,D$ bases del mismo espacio finito; en $\mathbb K^n$, $S_B,S_C$ contienen vectores de cada base en la canónica. **Tesis.**

$$
[v]_C=P_{B,C}[v]_B,\quad P_{C,B}=P_{B,C}^{-1},\quad
P_{B,D}=P_{C,D}P_{B,C},\quad P_{B,C}=S_C^{-1}S_B.
$$

**Estrategia ES.** Usar la identidad como aplicación y comparar las dos reconstrucciones del mismo vector. **策略中文。** 所有公式都可由输入、输出的基标签串接，而不是无方向地背诵。

**Demostración.** La primera es la fórmula de acción de la identidad de 3.5. Aplicarla de $B$ a $C$ y volver produce $P_{C,B}P_{B,C}[v]_B=[v]_B$ para todas las columnas, y al invertir el recorrido se obtiene el producto identidad opuesto; son inversas. Recorrer $B\to C\to D$ y comparar con $B\to D$ prueba la composición. Finalmente $v=S_B[v]_B=S_C[v]_C$ y la invertibilidad de $S_C$ dan la última fórmula. **Conclusión.** Cada dirección ha sido justificada. **中文解释。** 目标标准基时，排进矩阵的是源基向量的标准坐标，绝不是目标基自身。

## T2. Cambio en una aplicación

**Hipótesis.** $f:V\to W$, bases antiguas $B_1,C_1$, nuevas $B_2,C_2$. **Tesis.**

$$
M_{B_2,C_2}(f)=P_{C_1,C_2}\,M_{B_1,C_1}(f)\,P_{B_2,B_1}.
$$

**Estrategia ES.** Convertir entrada a la base antigua, aplicar la matriz antigua y convertir salida a la nueva. **策略中文。** 三步对应右、中、左三个因子。

**Demostración.** Para cualquier $v$, su nueva columna se transforma según

$$
[f(v)]_{C_2}=P_{C_1,C_2}[f(v)]_{C_1}
=P_{C_1,C_2}M_{B_1,C_1}(f)P_{B_2,B_1}[v]_{B_2}.
$$

Comparar todas las columnas prueba la tesis. Para endomorfismo con una sola base por representación, poner $P=P_{B_2,B_1}$ da $A_2=P^{-1}A_1P$. **Conclusión.** Se obtiene la fórmula de aula con etiquetas completas, no una inversión arbitraria.

## Semejanza e invariantes

Dos matrices cuadradas son semejantes（相似）si $A_2=P^{-1}A_1P$ con $P$ invertible. Esto equivale a representar el mismo endomorfismo en dos bases: la fórmula prueba una dirección; para la otra, tome el endomorfismo de matriz $A_1$ en canónica y la nueva base formada por columnas de $P$; T2 da $A_2$.

Es relación de equivalencia: identidad usa $I$; simetría usa $P^{-1}$; si el siguiente cambio es $Q$, el cambio total es $PQ$, porque $Q^{-1}(P^{-1}A_1P)Q=(PQ)^{-1}A_1(PQ)$. Preserva rango porque multiplicar por isomorfismos conserva dimensión de imagen. También preserva traza: definir $\operatorname{tr}A=\sum_i a_{ii}$ y observar

$$
\operatorname{tr}(XY)=\sum_{i,j}x_{ij}y_{ji}
=\sum_{j,i}y_{ji}x_{ij}=\operatorname{tr}(YX).
$$

Así $\operatorname{tr}(P^{-1}AP)=\operatorname{tr}(APP^{-1})=\operatorname{tr}A$. Las potencias cumplen $(P^{-1}AP)^k=P^{-1}A^kP$ por inducción y cancelación $PP^{-1}$ en cada producto.

**Español.** Igual rango y traza no bastan para semejanza. Diagonalizar buscará una base que simplifique un endomorfismo, no aplicar filas arbitrarias a su matriz. **中文。** 行等价、两侧独立换基和相似是不同关系；相似的两侧换基由同一空间的同一基变更关联。

## Repaso y conexiones

前置 [矩阵表示](../01_Matriz_Composicion/01_Teoria_Demostraciones.md)，后续谱理论使用相似分类。自测 ES: reconstruir cada fórmula siguiendo el recorrido de coordenadas. 中文：必须能解释哪组基的向量放哪一列，以及一般映射为什么不是总能写成相似式。[例题](04_Ejemplos.md)、[练习](05_Ejercicios.md)、[解答](06_Soluciones.md)。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
