---
title: Ejercicios de sistemas y Gauss / 方程组与消元独立练习
subject: Álgebra Lineal
tema: Tema 0 · Guía 1.2
type: exercises
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

# Ejercicios de sistemas y Gauss — 独立练习

**Procedencia:** G-E01–G-E12 son de elaboración propia, basados en AL-GD-001 1.2 y AL-AP-000 pp. 3–9. No se ha recibido una hoja oficial. Las etiquetas de dificultad son orientativas.

**Instrucciones en español.** Indicar incógnitas, campo de escalares y operaciones de fila. No dividir por un parámetro sin discutir cuándo se anula. Escribir el conjunto de todas las soluciones y comprobarlo. Consultar [las soluciones](06_Soluciones.md) después de un intento independiente.

**中文说明。** 先写大小、符号与参数条件，每步记录完整行变换。题干和答案分开保存，避免尚未独立思考就看到答案。

## G-E01 — Linealidad / 线性性 · básico

Considerando $x,y$ como incógnitas, decidir cuáles son ecuaciones lineales: $2x-3y=1$, $xy=1$, $x+y^2=0$ y $(1+i)x-y=0$ sobre $\mathbb C$. Explicar por qué $ax+y=1$ es lineal si $a$ es un parámetro fijado y puede no serlo si $a$ pasa a ser otra incógnita.

## G-E02 — Operaciones inválidas / 非法变换 · básico

Una persona multiplica por cero la única ecuación $x=1$ y concluye que es equivalente a $0=0$. Comparar los conjuntos de soluciones y explicar qué condición ha incumplido. Dar la operación inversa de cada una de las tres operaciones elementales permitidas.

## G-E03 — Una variable libre / 一个自由参数 · intermedio

Resolver por Gauss $x+y+z=2$, $2x+3y+z=5$. Indicar rangos, número de parámetros y comprobar la familia completa.

## G-E04 — Incompatibilidad / 不相容 · básico

Clasificar y resolver $x+y=1$, $2x+2y=3$. Escribir la fila contradictoria y ambos rangos.

## G-E05 — Rango y columnas originales / 秩与原矩阵列 · intermedio

Sea

$$
A=\begin{pmatrix}1&2&3&4\\2&4&6&8\\0&1&1&0\end{pmatrix}.
$$

Escalonar, hallar su rango y seleccionar el máximo número de columnas originales independientes. Expresar las restantes en función de las seleccionadas. Resolver $Ax=0$ con todos sus parámetros.

## G-E06 — Dos parámetros en los coeficientes y el término / 参数分类 · universitario

Discutir, para $a,b\in\mathbb R$, el sistema $x+y+z=1$, $x+ay+z=1$, $x+y+az=b$. Justificar por qué los casos separados son exhaustivos y dar el conjunto de soluciones en cada uno.

## G-E07 — Inversa y resolución / 求逆与求解 · intermedio

Obtener por Gauss–Jordan la inversa de $A=\begin{pmatrix}1&2\\3&5\end{pmatrix}$ y resolver $Ax=(1,0)^{\mathsf T}$. Comprobar ambos productos de inversa y sustituir la solución.

## G-E08 — Resolución simultánea / 同时求解 · intermedio

Resolver $AX=B$ con

$$
A=\begin{pmatrix}2&1\\1&1\end{pmatrix},\quad B=\begin{pmatrix}1&3\\0&2\end{pmatrix}.
$$

Hacer una única eliminación sobre $(A\mid B)$ e interpretar sus dos columnas de solución.

## G-E09 — Conjunto afín / 解集的平移 · demostración

Suponiendo $Ax_p=b$, demostrar las dos inclusiones de $S(A,b)=x_p+S(A,0)$. Probar que la diferencia de dos soluciones no homogéneas es homogénea y dar un contraejemplo a la afirmación «la suma de dos soluciones no homogéneas siempre es solución».

## G-E10 — Ecuaciones frente a incógnitas / 方程数与未知数 · razonamiento

Demostrar que un sistema compatible con $m<n$ no puede tener solución única sobre $\mathbb R$. Construir un sistema con $m>n$ que sí tenga solución única. Explicar por qué «más ecuaciones que incógnitas» no implica incompatibilidad.

## G-E11 — Qué se conserva / 哪些对象被保留 · contraejemplos

Para $A=\begin{pmatrix}1&1\\0&0\end{pmatrix}$, intercambiar las filas y comparar los espacios generados por las columnas antes y después, las relaciones entre sus columnas y los rangos. Después, comparar $x+2y=1$ con el resultado de intercambiar sus columnas sin renombrar incógnitas. ¿Por qué son fenómenos diferentes?

## G-E12 — Un cuerpo finito / 有限域边界 · ampliación

En este ejercicio se amplía el campo habitual: $\mathbb F_2=\{0,1\}$ con suma y producto módulo $2$. Resolver $x+y=1$ en $\mathbb F_2^2$. Comparar rangos, número de parámetros y número de soluciones con el mismo sistema sobre $\mathbb R$. Precisar qué hipótesis necesita la conclusión «infinitas soluciones».

此最后一题为自拟拓展，不据此宣称有限域已列入教授必考范围。返回 [学习入口](00_Introduccion.md)。
