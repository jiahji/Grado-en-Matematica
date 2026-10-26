---
title: Bases, dimensión y Steinitz / 基、维数与交换定理
subject: Álgebra Lineal
tema: Guía 2.4
type: example
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_2_4
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-012/Temas 1 y 2(1)(2).pdf
updated: 2026-10-26
---

# Ejemplos 2.4 — 完整例题

**Fuentes verificadas:** AL-AP-012, pp. 12–18. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Ejemplos de elaboración propia, salvo el modelo de bases canónicas de aula.

## B-01. Extraer una base — 基础

**Enunciado.** De $u=(1,0,1)$, $v=(0,1,1)$, $w=(1,1,2)$, $e_3=(0,0,1)$, extraer base de $\mathbb R^3$. **Análisis ES.** Primero quitar la relación conocida, luego comprobar las tres restantes. **中文。** 不能只凭有三个向量就称为基。

**Resolución.** $w=u+v$ es redundante. Una relación $au+bv+ce_3=0$ da $a=0,b=0$ en primeras coordenadas y después $c=0$. Cualquier $(x,y,z)=xu+yv+(z-x-y)e_3$, por lo que generan. **Conclusión.** $(u,v,e_3)$ es base; se han verificado ambas condiciones. **Error frecuente ES.** La lista $(u,v,w)$ no es base porque el tercero sigue siendo redundante. **中文易错点。** 第三个向量仍冗余，因此这组三元列表不是基。

## B-02. Ampliar independientes — 综合

**Enunciado.** Completar $(1,1,0)$ y $(0,1,1)$ a una base de $\mathbb R^3$. **Análisis ES.** Añadir un vector fuera de su generado. **中文。** 给出一个候选后以零关系验证。

**Resolución.** Añadimos $e_1=(1,0,0)$. Si $a(1,1,0)+b(0,1,1)+ce_1=0$, las coordenadas tercera, segunda y primera dan sucesivamente $b=0,a=0,c=0$. Es base por el criterio finito, o directamente porque $(x,y,z)=(y-z)(1,1,0)+z(0,1,1)+(x-y+z)e_1$. **Conclusión.** Una compleción concreta es válida; no tiene por qué ser única.

## B-03. Dimensión y cuerpo — 大学水平

**Enunciado.** Calcular la dimensión de $\mathbb C$ sobre $\mathbb C$ y sobre $\mathbb R$. **Análisis ES.** El campo cambia las representaciones permitidas. **中文。** 维数必须连同标量域陈述。

**Resolución.** Sobre $\mathbb C$, $(1)$ es base porque cada $z=z\cdot1$ de manera única. Sobre $\mathbb R$, $(1,i)$ genera por $a+bi$ y es independiente por igualdad de partes. Las dimensiones son $1$ y $2$. **Conclusión.** No hay contradicción: son estructuras distintas. **Error frecuente ES.** El criterio de igual dimensión se aplica sobre un mismo cuerpo. **中文误区。** 不能混用两种维数作等维判别。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
