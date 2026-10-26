---
title: Repaso de complejos y cuerpos / 复数与域复习
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

# Repaso de complejos y cuerpos — 复习与自测

**Fuentes:** AL-GD-001 1.4 y AL-AP-000 pp. 10–16. La forma polar y sus actividades se desarrollan como ampliación didáctica; no hay examen real recibido que permita atribuirlas a preguntas obligatorias.

## Definiciones y condiciones — 定义与前提

**Español.** Poder definir suma y producto complejos, partes real e imaginaria, conjugado, módulo, argumento e inversa. Enunciar los axiomas de cuerpo con operaciones internas, $0\ne1$ y los cuantificadores correctos para inversión.

**中文。** 相反数对所有元素存在，逆元只对非零元素要求存在；复数虚部是实数系数；零无辐角、无倒数。

## Pruebas y métodos — 证明与方法

| 任务 | Método en español | 中文策略 |
| --- | --- | --- |
| 除法 | Multiplicar por conjugado y usar módulo cuadrado | 分母非零，最后乘回原分子 |
| 域的性质 | Identificar el axioma y justificar cada cancelación | 不把乘法消去当作未证公理 |
| 证明复数构成域 | Comprobar todas las leyes por pares | 只验证 $i^2=-1$ 不够 |
| 复系数系统 | Aplicar Gauss sobre $\mathbb C$ | 使用复数域非零逆元 |
| 极形式求幂 | Potenciar módulos y multiplicar argumentos | 模与角度遵循不同规则 |
| 全部方根 | Enumerar, verificar, distinguir y probar exhaustividad | 不漏整圈项及其他根 |

## Errores frecuentes — 易错点

**Español.** No confundir $\operatorname{Im}z$ con $bi$; no invertir cero; no confundir conjugado e inversa; no tratar argumento como único; no extender reglas de raíces reales sin condiciones; no usar una demostración válida en cuerpos para matrices sin comprobar las hipótesis.

**中文。** 公理、公式、例子与反例各自承担不同逻辑任务。能用数值算出几个逆元，不代表已经证明一个结构是域；必须完整核查公理。

## Checklist — 自测

- [ ] 能完整写出域的公理与非零条件。
- [ ] 能从公理证明乘零、逆元唯一和非零消去。
- [ ] 能解释构造复数的实数对定义并检查乘法结合律。
- [ ] 能独立完成课堂复数运算和复系数系统，并逐项验证。
- [ ] 能在补充极形式部分证明 De Moivre 并求全体方根。
- [ ] 能给出共轭不等于逆元、复平方根乘法规则失败的反例。
- [ ] 能用中西双语解释标量域与矩阵运算的差别。

返回 [练习](05_Ejercicios.md)、[学习入口](00_Introduccion.md) 或 [Tema 0](../00_Indice.md)。
