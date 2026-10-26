---
title: Espacios vectoriales y subespacios / 向量空间与子空间
subject: Álgebra Lineal
tema: Guía 2.2
type: example
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_2_2
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-012/Temas 1 y 2(1)(2).pdf
updated: 2026-10-26
---

# Ejemplos de espacios y subespacios — 完整例题

**Fuentes verificadas:** AL-AP-012, pp. 3–7. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


前两个为基于课堂齐次系统的自拟展开，第三个使用课堂函数与标量域类型。

## V-01. Un plano homogéneo — 基础

**Enunciado.** ¿Es $W=\{(x,y,z):x-2y+z=0\}$ subespacio de $\mathbb R^3$? **Análisis ES.** Comprobar cero y una combinación arbitraria. **中文。** 不仅仅画一个平面，要检查集合的代数条件。

**Resolución.** Cero satisface la ecuación. Si $u,v$ la satisfacen, la expresión de la combinación $au+bv$ es $a(u_1-2u_2+u_3)+b(v_1-2v_2+v_3)=0$. Así es subespacio. Resolver da $(x,y,z)=(2s-t,s,t)$, consistente con que sus operaciones sean cerradas. **Conclusión.** Es subespacio. **Error frecuente ES.** Los parámetros recorren todo $\mathbb R$, incluidos cero y negativos. **中文误区。** 参数式的自由参数可为任意实数，不是仅取正数。

## V-02. Dos fallos diferentes — 综合

**Enunciado.** Comparar $U=\{(x,y):x+y=1\}$ y $C=\{(x,y):xy=0\}$. **Análisis ES.** El primer fallo es no contener cero; el segundo exige probar que contener cero no basta. **中文。** 不要把唯一的一次验零当成完整判别。

**Resolución.** $0\notin U$, luego no es subespacio. En $C$, sí está cero; están $(1,0)$ y $(0,1)$, pero su suma $(1,1)$ cumple $xy=1\ne0$ y no pertenece a $C$. No es subespacio. **Conclusión.** Fallan condiciones distintas. **中文解释。** 两坐标轴的并集包含零且各轴本身是子空间，但两轴之间的加法会跑出并集。

## V-03. El cuerpo importa — 大学水平

**Enunciado.** Considerar $\mathbb R\subset\mathbb C$. ¿Es subespacio sobre $\mathbb R$? ¿Y sobre $\mathbb C$? **Análisis ES.** La clausura escalar depende del cuerpo elegido. **中文。** 相同的向量集合在不同标量域下可能有不同答案。

**Resolución.** Con escalares reales, suma y múltiplos de reales son reales y contienen cero; es subespacio de $\mathbb C$ como espacio real. Con escalares complejos, $1\in\mathbb R$ pero $i\cdot1=i\notin\mathbb R$, por lo que no es subespacio complejo. **Conclusión.** Siempre se debe declarar el cuerpo. **Error frecuente ES.** El mismo conjunto puede dejar de ser subespacio al ampliar los escalares. **中文误区。** “集合没有改变，所以答案相同”忽略了结构的一部分。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
