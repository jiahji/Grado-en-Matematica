---
title: Representación matricial y composición / 矩阵表示与复合 — soluciones
subject: Álgebra Lineal
tema: Guía 3.5
type: exercises
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_3_5
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-004/Tema 4_65298606b99b4fa875367ddfc0765632.pdf
updated: 2026-10-26
---

# Soluciones 3.5 — 完整解答

**Fuentes verificadas:** AL-AP-004, pp. 2–7. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Resoluciones propias de [A35-E01–E06](05_Ejercicios.md).

## A35-E01

**Estrategia ES.** Usar imágenes de los dos canónicos. **中文。** 每列对应一个输入基向量。**Resolución.** $A=\begin{pmatrix}2&-1\\1&3\end{pmatrix}$ y $A(1,2)^{\mathsf T}=(0,7)^{\mathsf T}$. La fórmula original también da $(2-2,1+6)=(0,7)$. **Conclusión.** Las coordenadas canónicas coinciden con las entradas usuales.

## A35-E02

**Estrategia ES.** Evaluar la nueva base. **中文。** 只变定义域，目标仍是标准坐标。**Resolución.** $f(1,1)=(1,4)$, $f(1,-1)=(3,-2)$, así matriz $\begin{pmatrix}1&3\\4&-2\end{pmatrix}$. **Conclusión.** No es la misma matriz que E01 aunque la regla $f$ sea la misma.

## A35-E03

**Estrategia ES.** Derivar $1,x,x^2,x^3$. **中文。** 保留每次幂降的系数。**Resolución.** La matriz es $\begin{pmatrix}0&1&0&0\\0&0&2&0\\0&0&0&3\end{pmatrix}$. Tiene tres columnas no nulas independientes, rango $3$; núcleo consta de coordenadas $(a,0,0,0)$, las constantes. **Conclusión.** Rango más nulidad es $3+1=4$.

## A35-E04

**Estrategia ES.** Multiplicar llegada por salida previa. **中文。** 先 $f$ 后 $g$，矩阵顺序相反于口头书写顺序。**Resolución.** $F=\begin{pmatrix}1&0\\0&1\\1&1\end{pmatrix}$, $G=\begin{pmatrix}1&0&1\\0&1&-1\end{pmatrix}$, $GF=\begin{pmatrix}2&1\\-1&0\end{pmatrix}$. Directamente $g(f(x,y))=(2x+y,-x)$, consistente. **Conclusión.** El producto correcto es $GF$.

## A35-E05

**Estrategia ES.** Aplicar la fórmula de acción a cada vector. **中文。** 比较之前先固定同一种坐标描述。**Demostración.** Si la matriz común es $A$, $[f(v)]_C=A[v]_B=[g(v)]_C$ para todo $v$. Como las coordenadas son inyectivas, $f(v)=g(v)$. Si cambian bases, la misma identidad puede tener matrices distintas, y una igualdad numérica aislada no compara automáticamente la misma regla abstracta. **Conclusión.** La fijación de bases es parte de la hipótesis.

## A35-E06

**Estrategia ES.** Usar que las coordenadas son isomorfismos. **中文。** 秩是像的维数，不是特定列坐标的外形。**Demostración.** Para cualquier base de llegada, el isomorfismo coordenada lleva la imagen de $f$ al generado de las columnas de su matriz y conserva bases. Por tanto la dimensión de ese generado es siempre $\dim\operatorname{Im}f$, independientemente de la base inicial y final. **Conclusión.** Invariancia sin suponer una fórmula aún no demostrada.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
