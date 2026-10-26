---
title: Espacio de aplicaciones y dual / 映射空间与对偶空间 — soluciones
subject: Álgebra Lineal
tema: Guía 3.8
type: exercises
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_3_8
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-003/Tema 3_3783d906f8056ce104fc5d6bc1f5548c.pdf
updated: 2026-10-26
---

# Soluciones 3.8 — 完整解答

**Fuentes verificadas:** AL-AP-003, p. 19: terminología de forma lineal; desarrollo de Hom y dual como suplemento. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Resoluciones propias de [A38-E01–E06](05_Ejercicios.md).

## A38-E01

**Estrategia ES.** Las formas duales extraen los coeficientes en $B$. **中文。** 系数是原形式在基向量上的值。**Resolución.** $\varphi_1=(x+y)/2$, $\varphi_2=(x-y)/2$. Se comprueba $\varphi_i(b_j)=\delta_{ij}$. $\ell(b_1)=5$, $\ell(b_2)=-1$, así $\ell=5\varphi_1-\varphi_2$; expandir devuelve $2x+3y$. **Conclusión.** La fila de coeficientes estándar $(2,3)$ no es automáticamente la nueva coordenada.

## A38-E02

**Estrategia ES.** Escoger una salida básica para cada entrada básica. **中文。** 两个输入基向量各有三个独立输出系数。**Resolución.** Hay seis mapas $E_{ij}$, $i=1,2,3$, $j=1,2$, que llevan $e_j$ a $e_i$ y la otra entrada básica a cero. Evaluar una relación en $e_1,e_2$ demuestra independencia, y asignar las dos columnas de cualquier mapa demuestra generación. **Conclusión.** Dimensión $6$.

## A38-E03

**Estrategia ES.** Usar dos generadores del plano. **中文。** 不只验证一个方向。**Resolución.** El plano tiene base $(1,-1,0),(1,0,-1)$. Una forma $ax+by+cz$ los anula exactamente si $a-b=0$ y $a-c=0$, así $a=b=c$. El anulador es $\langle x+y+z\rangle$, de dimensión $1$. **Conclusión.** Se verifica $3-2=1$.

## A38-E04

**Estrategia ES.** Trasponer y componer. **中文。** 对偶形式坐标是列向量 $(3,-1)$。**Resolución.** $M(f^*)=A^{\mathsf T}=\begin{pmatrix}1&0\\2&1\end{pmatrix}$. Aplicado a $(3,-1)$ da $(3,5)$. Directamente $f(x,y)=(x+2y,y)$ y $\ell(f(x,y))=3x+5y$. **Conclusión.** Ambos procedimientos coinciden.

## A38-E05

**Estrategia ES.** Aplicar contravarianza a las dos identidades de inversa. **中文。** 方向颠倒但两个复合仍都是恒等。**Demostración.** $(f^{-1}\circ f)^*=f^*\circ(f^{-1})^*=I_{V^*}$ y $(f\circ f^{-1})^*=(f^{-1})^*\circ f^*=I_{W^*}$. Ambas aplicaciones son lineales, por lo que son inversas bilaterales. **Conclusión.** Dualidad preserva isomorfismos invirtiendo flechas.

## A38-E06

**Estrategia ES.** Examinar la definición antes de usar coordenadas. **中文。** 自然映射不需要先选基才能定义。**Resolución.** $J(v)$ actúa sobre una forma tomando su valor en $v$; ni $v$ ni $\ell$ necesitan una base en esa regla. Si se elige $B$, la forma dual $\varphi_i$ extrae la coordenada $i$, así $J(v)(\varphi_i)=\varphi_i(v)=[v]_{B,i}$. **Conclusión.** La fórmula por coordenadas describe un mapa ya definido intrínsecamente.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
