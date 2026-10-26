---
title: Inyectividad, sobreyectividad y biyectividad / 单射、满射与双射
subject: Álgebra Lineal
tema: Guía 3.3
type: theorem
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_3_3
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-003/Tema 3_3783d906f8056ce104fc5d6bc1f5548c.pdf
updated: 2026-10-26
---

# Inyectividad, sobreyectividad y biyectividad — 单射、满射与双射

**Fuentes verificadas:** AL-AP-003, pp. 14–16. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.

**Organización:** esta unidad integra motivación, definiciones, teoremas, pruebas, conexiones y repaso en un archivo; ejemplos, ejercicios y soluciones se mantienen separados.


## Motivación y definiciones

**Español.** Inyectividad prohíbe perder diferencias de entrada; sobreyectividad exige alcanzar cada salida del destino declarado. Biyectividad reúne ambas. No basta conocer la fórmula sin su dominio y codominio. **中文。** “没有信息丢失”与“没有输出缺失”是不同问题，陪域改变会改变满射性。

$f:V\to W$ es inyectiva si $f(u)=f(v)$ implica $u=v$ para todos $u,v$; es sobreyectiva si para cada $w\in W$ existe $v\in V$ con $f(v)=w$; es biyectiva si cumple ambas. Para mapas lineales también se usan monomorfismo, epimorfismo e isomorfismo, respectivamente.

## T1. Criterio del núcleo

**Hipótesis.** $f$ lineal. **Tesis.** $f$ inyectiva si y solo si $\ker f=\{0\}$.

**Estrategia ES.** Comparar dos entradas mediante su diferencia. **策略中文。** 线性把任意碰撞转换为核里的一个向量。

**Demostración.** Si $f$ es inyectiva y $v\in\ker f$, $f(v)=0=f(0)$ implica $v=0$. A la inversa, si $f(u)=f(v)$, entonces $f(u-v)=0$, así $u-v\in\ker f=0$ y $u=v$. **Explicación ES.** Sin linealidad el núcleo no es el criterio adecuado: solo controlar la fibra de cero no impide otras colisiones. **中文解释。** 判别依赖差能被映成输出之差，不能给任意非线性函数套用。**Conclusión.** El criterio es una equivalencia exacta.

## T2. Independencia y generación

**Enunciado.** Una lineal inyectiva lleva familias independientes a independientes. Si $S$ genera $V$, entonces $f$ es sobreyectiva si y solo si $f(S)$ genera $W$.

**Estrategia ES.** Transportar relaciones y usar la fórmula de imagen del generado. **策略中文。** 无关需要控制核，生成需要控制整个像。

**Demostración.** Si $\sum a_if(v_i)=0$, entonces $f(\sum a_iv_i)=0$. Por T1, la suma original es cero, e independencia da todos los $a_i=0$. Para generadores, 3.2 prueba $\operatorname{Im}f=f(\langle S\rangle)=\langle f(S)\rangle$. Por tanto imagen total equivale a que ese generado sea $W$. **Explicación ES.** Las imágenes de generadores pueden ser dependientes aunque todavía generen el destino. **中文解释。** 满射可能压缩冗余方向，不能由它推出保无关。**Conclusión.** Se obtienen los criterios de aula sin confundir sus hipótesis.

## T3. Criterios de rango y dimensión finita

**Hipótesis.** $\dim V=n$, $\dim W=m$ finitas. **Tesis.** Inyectiva equivale a rango $n$; sobreyectiva a rango $m$; biyectiva a $n=m=\operatorname{rg}f$.

**Estrategia ES.** Aplicar rango–nulidad e inclusión de imagen. **策略中文。** 对单射用定义域维数，对满射用陪域维数。

**Demostración.** Por 3.2, nulidad es $n-\operatorname{rg}f$. T1 la hace cero exactamente cuando rango $n$. Imagen es subespacio de $W$; por igualdad de dimensión finita es todo $W$ exactamente cuando rango $m$. Las dos condiciones juntas dan $n=m=r$. **Corolario probado.** Si $n=m$, cualquiera de inyectividad o sobreyectividad implica la otra; si $n>m$, no puede haber inyección; si $n<m$, no puede haber sobreyección, porque rango $\le\min(n,m)$. **Conclusión.** Las desigualdades y equivalencias quedan justificadas.

## Alcance y contraejemplos

En dimensión infinita, $S(p)=xp$ en $\mathbb R[x]$ es inyectiva y no sobreyectiva, mientras derivar es sobreyectivo y no inyectivo; sus pruebas concretas están en [2.8](../../Tema_01/05_Tipo_No_Finito/01_Teoria_Demostraciones.md). No se reemplaza la hipótesis finita por una resta de infinitos. Incluso en dimensión finita, decir «lineal» no obliga ninguna de las dos propiedades: el mapa cero entre espacios no nulos no es ni inyectivo ni sobreyectivo.

## Repaso y conexiones

前置 [核、像与秩–零化度](../02_Nucleo_Imagen_Rango/01_Teoria_Demostraciones.md)，后续 [同构与逆映射](../04_Isomorfismos/01_Teoria_Demostraciones.md)。**Español.** Para un mapa concreto, escribir dominio y destino antes de calcular el rango; para una familia con parámetros, separar cada pivote que puede anularse. **中文。** 自测必须能给单但不满、满但不单、既不单也不满的三个例子，并说明有限等维为何排除前两种。[例题](04_Ejemplos.md)、[题目](05_Ejercicios.md)、[解答](06_Soluciones.md)。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
