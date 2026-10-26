---
title: Cambio de base y semejanza / 换基与相似 — soluciones
subject: Álgebra Lineal
tema: Guía 3.6
type: exercises
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

# Soluciones 3.6 — 完整解答

**Fuentes verificadas:** AL-AP-004, pp. 8–12. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Resoluciones propias de [A36-E01–E06](05_Ejercicios.md).

## A36-E01

**Estrategia ES.** Las columnas de $B$ ya están en la canónica. **中文。** 反方向需要求逆。**Resolución.** $P_{B,C}=\begin{pmatrix}1&0\\1&1\end{pmatrix}$ y su inversa $P_{C,B}=\begin{pmatrix}1&0\\-1&1\end{pmatrix}$. Aplicar al vector $(2,3)$ da $(2,1)$; $2(1,1)+(0,1)=(2,3)$. **Conclusión.** Se comprueba el recorrido completo.

## A36-E02

**Estrategia ES.** Conjugación por $P=P_{B,C}$. **中文。** 新基到旧基矩阵放右侧。**Resolución.** $P^{-1}AP=\begin{pmatrix}1&0\\1&2\end{pmatrix}$. Las imágenes nuevas son $f(1,1)=(1,2)=1(1,1)+1(0,1)$ y $f(0,1)=(0,2)=0(1,1)+2(0,1)$, dando esas columnas. **Conclusión.** Ambas rutas coinciden.

## A36-E03

**Estrategia ES.** Inducir y cancelar $PP^{-1}$ entre factores. **中文。** 不能通过交换矩阵来推导。**Demostración.** Para $k=0$, $I=P^{-1}IP$. Si vale para $k$, $A_2^{k+1}=(P^{-1}A_1^kP)(P^{-1}A_1P)=P^{-1}A_1^{k+1}P$ por asociatividad. **Conclusión.** Todos los exponentes no negativos quedan cubiertos.

## A36-E04

**Estrategia ES.** Usar el cuadrado como invariante, sin requerir aún autovalores. **中文。** 迹和秩相同只是必要条件。**Resolución.** Ambas son invertibles y tienen traza cero. El cuadrado de la diagonal es $I$, y el de la otra es $-I$. Si fueran semejantes, E03 forzaría que el segundo cuadrado fuese semejante a $I$, pero $P^{-1}IP=I$ siempre y $-I\ne I$ sobre reales. **Conclusión.** No son semejantes.

## A36-E05

**Estrategia ES.** Seguir las columnas desde la derecha. **中文。** 左乘因子最后发生。**Resolución.** $[v]_C=P_{B,C}[v]_B$ y $[v]_D=P_{C,D}[v]_C=P_{C,D}P_{B,C}[v]_B$. Por unicidad para todo vector, $P_{B,D}=P_{C,D}P_{B,C}$. **Conclusión.** El producto opuesto representa un recorrido diferente o puede no corresponder a las etiquetas.

## A36-E06

**Estrategia ES.** Comparar con la rigidez de identidad bajo semejanza. **中文。** 行变换改变一个方程系统的描述，不是同一线性算子的单一换基。**Resolución.** Toda invertible es fila-equivalente a $I$, pero si $P^{-1}AP=I$ entonces $A=PIP^{-1}=I$. Por ejemplo $A=2I$ es invertible y reducible por filas a $I$, pero no semejante a $I$. **Conclusión.** Las relaciones no son intercambiables.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
