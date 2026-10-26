---
title: Aplicaciones lineales / 线性映射
subject: Álgebra Lineal
tema: Guía 3.1
type: example
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_3_1
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-003/Tema 3_3783d906f8056ce104fc5d6bc1f5548c.pdf
updated: 2026-10-26
---

# Ejemplos de linealidad — 完整例题

**Fuentes verificadas:** AL-AP-003, pp. 2–8. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


## F-01. Un mapa rectangular — 基础

**Enunciado propio basado en p. 6.** $f(x,y,z)=(x+2y-z,y+z)$. **Análisis ES.** Escribir una matriz de coeficientes y verificar la combinación. **中文。** 输出维数可与输入不同。

**Resolución.** $f(v)=Av$ con $A=\begin{pmatrix}1&2&-1\\0&1&1\end{pmatrix}$. Para cualesquiera $a,b,u,v$, $A(au+bv)=aAu+bAv$, así es lineal. Por ejemplo $f(1,0,1)=(0,1)$, consistente con la fórmula. **Conclusión.** La matriz rectangular define un mapa válido, no requiere inversa.

## F-02. Asignación en una base — 综合

**Enunciado propio.** $f(1,0)=(1,1)$, $f(1,1)=(0,1)$. Hallar la única lineal. **Análisis ES.** La lista de partida es base; expresar un vector en ella. **中文。** 不能把给出的两列当作标准基的像。

**Resolución.** $(x,y)=(x-y)(1,0)+y(1,1)$, por tanto $f(x,y)=(x-y)(1,1)+y(0,1)=(x-y,x)$. Sustituir los dos vectores dados verifica las condiciones; T2 da unicidad. **Conclusión.** Primero se resuelven coordenadas en la base especificada.

## F-03. Conjugación — 大学水平

**Enunciado propio.** Estudiar $C(z)=\bar z$ como mapa de $\mathbb C$ a sí mismo sobre $\mathbb R$ y sobre $\mathbb C$. **Análisis ES.** La homogeneidad depende del cuerpo. **中文。** 加法保存还不够，系数范围也要检查。

**Resolución.** Siempre $\overline{z+w}=\bar z+\bar w$. Para $a\in\mathbb R$, $\overline{az}=a\bar z$, así es real lineal. Sobre $\mathbb C$, $C(i\cdot1)=-i$, mientras $iC(1)=i$, así falla homogeneidad. **Conclusión.** Lineal sobre reales, no sobre complejos. **Error frecuente ES.** Una fórmula no determina la linealidad sin su cuerpo de escalares. **中文误区。** 相同的公式不自动拥有相同的线性结构。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
