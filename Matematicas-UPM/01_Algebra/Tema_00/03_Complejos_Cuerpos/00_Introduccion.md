---
title: Números complejos y cuerpos / 复数与域：学习入口
subject: Álgebra Lineal
tema: Tema 0 · Guía 1.4
type: review
language: es-zh
status: complete
tags:
- algebra_lineal
- complejos
- cuerpos
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-000/Tema 0(6).pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
updated: 2026-10-26
---

# Números complejos y cuerpos — 复数与域

**Fuentes:** AL-AP-000, pp. 10–16; AL-GD-001, p. 5, apartado 1.4. Las anotaciones de la p. 11 mencionan formas cartesiana y polar. La formalización por pares, las demostraciones completas y las raíces en forma polar son desarrollo didáctico propio, no requisitos de examen atribuidos al profesor.

## Motivación — 为何扩充实数

**Español.** La ecuación $x^2+1=0$ no tiene solución real, porque el cuadrado de un real es no negativo. Se busca una estructura que conserve las operaciones aritméticas y contenga un elemento $i$ cuyo cuadrado sea $-1$. No basta escribir un símbolo: hay que definir las operaciones y demostrar sus propiedades.

**中文。** 引入 $i$ 不是随意宣称“负数也能开根号”，而是建立一个比实数更大的代数系统，并检查原来的运算规律在新系统中仍一致。二维实数对提供一种明确构造。

El cuerpo（域）resume qué propiedades permiten sumar, restar, multiplicar y dividir por un elemento no nulo. Esta última restricción es imprescindible tanto en fracciones complejas como en los pivotes de Gauss.

中文：复数除法和行消元看似不同，实际都依赖非零标量有逆元。矩阵也能相加相乘，却不因此构成域；前面的非零零乘积反例正好说明差别。

## Ruta de estudio — 学习路径

1. [定义：复数、共轭、模、辐角与域](01_Definiciones.md)。
2. [性质与适用条件](02_Teoremas.md)。
3. [八组完整证明](03_Demostraciones.md)。
4. [六个例题](04_Ejemplos.md)，含课堂复数运算及复系数 Gauss。
5. [十二道独立练习](05_Ejercicios.md) 与 [分开的完整解答](06_Soluciones.md)。
6. [复习自测](07_Repaso_Examen.md)。

## Prerrequisitos y conexiones — 前置与关联

**Español.** Se utiliza la aritmética real y, para la forma polar, trigonometría elemental. La construcción del cuerpo real y la teoría general de funciones exponenciales complejas no se presuponen como resultados de este módulo. La notación $r(\cos\theta+i\sin\theta)$ no necesita definir una exponencial compleja.

**中文。** 基础部分不依赖三角函数；极形式部分需要正弦、余弦和角度加法公式。极形式与根的计算明确标为对材料的教学扩充，不据此推断教授的考核范围。

学习复系数方程组时可回看 [Gauss 单元](../02_Sistemas_Gauss/00_Introduccion.md)。之后的向量空间会使用域作为标量来源；本模块只建立所需标量结构，不把整个“群与域”官方 2.1 宣称完成。

返回 [Tema 0](../00_Indice.md)。
