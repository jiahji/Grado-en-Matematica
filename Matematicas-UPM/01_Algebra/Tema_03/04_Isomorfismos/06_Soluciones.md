---
title: Isomorfismos, coordenadas y productos / 同构、坐标映射与乘积 — soluciones
subject: Álgebra Lineal
tema: Guía 3.4
type: exercises
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_3_4
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-003/Tema 3_3783d906f8056ce104fc5d6bc1f5548c.pdf
updated: 2026-10-26
---

# Soluciones 3.4 — 完整解答

**Fuentes verificadas:** AL-AP-003, pp. 16–19. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Resoluciones propias de [A34-E01–E06](05_Ejercicios.md).

## A34-E01

**Estrategia ES.** Resolver dos ecuaciones de salida. **中文。** 检查两个复合方向。**Resolución.** Para $(u,v)$, $x=(u+v)/2$, $y=(u-v)/2$. La fórmula inversa es lineal por sus coeficientes constantes. Sustituirla en $f$ da $(u,v)$ y aplicarla a $f(x,y)$ devuelve $(x,y)$. **Conclusión.** Inversa bilateral explícita.

## A34-E02

**Estrategia ES.** Usar identidad, inversa y composición. **中文。** 每一项也要确保仍是线性映射。**Demostración.** Identidad es lineal y biyectiva; la inversa de un isomorfismo es lineal biyectiva por T1; la composición de lineales es lineal y su inversa es la composición inversa en orden opuesto. Así se verifican reflexividad, simetría y transitividad. **Conclusión.** Se justifica hablar de clases de estructuras isomorfas.

## A34-E03

**Estrategia ES.** Fijar orden por filas. **中文。** 不存在默认唯一的展平顺序。**Resolución.** $F(\begin{smallmatrix}a&b\\c&d\end{smallmatrix})=(a,b,c,d)$ es lineal porque las operaciones son por entradas. Su inversa reconstruye esa matriz y ambas composiciones son identidad. **Conclusión.** Isomorfismo explícito, no una identificación multiplicativa de matrices con un cuerpo.

## A34-E04

**Estrategia ES.** Usar la descomposición única del ejemplo de complementarios. **中文。** 输出是一个有序对，其中每项是原环境的向量。**Resolución.** $\Phi^{-1}(x,y)=((x-cy,0),(cy,y))$. El segundo vector es $y(c,1)$ y el primero está en $U$. Su suma es $(x,y)$. Para un par $((a,0),t(c,1))$, la fórmula aplicada a su suma devuelve el mismo par. **Conclusión.** Las dos identidades se verifican sin confundir coordenadas con componentes del producto.

## A34-E05

**Estrategia ES.** Proyección e inclusión. **中文。** 用具体向量暴露丢失的信息。**Resolución.** $f(x,y)=x$ y $g(t)=(t,0)$ dan $f\circ g(t)=t$. Pero $g\circ f(0,1)=(0,0)\ne(0,1)$. $f$ es sobreyectiva y no inyectiva, así ninguna inversa bilateral puede existir. **Conclusión.** Derecha no implica dos lados; es la corrección necesaria en p. 16.

## A34-E06

**Estrategia ES.** Aplicar los teoremas hacia delante y a $f^{-1}$ hacia atrás. **中文。** 逆向不靠猜测，而是逆映射也线性。**Demostración.** Inyectividad de $f$ conserva independencia; sobreyectividad y linealidad conservan generación total por 3.2. Si las imágenes son independientes o generadoras, aplicar los mismos argumentos al isomorfismo inverso devuelve la correspondiente propiedad de la lista original. **Conclusión.** Ambas propiedades son invariantes por isomorfismo.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
