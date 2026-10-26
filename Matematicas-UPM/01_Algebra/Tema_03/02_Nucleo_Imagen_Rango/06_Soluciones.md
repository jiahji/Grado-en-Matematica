---
title: Núcleo, imagen y rango–nulidad / 核、像与秩–零化度 — soluciones
subject: Álgebra Lineal
tema: Guía 3.2
type: exercises
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_3_2
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-003/Tema 3_3783d906f8056ce104fc5d6bc1f5548c.pdf
updated: 2026-10-26
---

# Soluciones 3.2 — 完整解答

**Fuentes verificadas:** AL-AP-003, pp. 9–13. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Resoluciones propias de [A32-E01–E06](05_Ejercicios.md).

## A32-E01

**Estrategia ES.** Resolver dos ecuaciones y seleccionar columnas independientes. **中文。** 使用同一个未知量参数表示全部核。**Resolución.** $x=-y$, $z=-y$, así núcleo $\langle(-1,1,-1)\rangle$. Las imágenes de $e_1,e_3$ son $(1,0),(0,1)$, por lo que imagen $\mathbb R^2$. Dimensiones $1+2=3$. **Conclusión.** Las bases pertenecen a espacios de dimensiones distintas.

## A32-E02

**Estrategia ES.** Escribir $p=a+bx+cx^2$. **中文。** 纤维不是核，先找一个特解。**Resolución.** Núcleo exige $a+b+c=0$, así $p=b(x-1)+c(x^2-1)$; ambas polinomios son independientes por coeficientes de $x,x^2$. La imagen es $\mathbb R$ porque las constantes toman todo valor. Un particular de salida $2$ es el polinomio constante $2$, así la fibra es $2+\langle x-1,x^2-1\rangle$. **Conclusión.** La fibra no contiene cero y no es subespacio.

## A32-E03

**Estrategia ES.** Probar las dos inclusiones usando una descomposición. **中文。** 不假设分解唯一。**Demostración.** Si $z=f(u+w)$, linealidad lo escribe $f(u)+f(w)$ en la suma de imágenes. Recíprocamente, cualquier $f(u)+f(w)=f(u+w)$ proviene de $U+W$. **Conclusión.** La igualdad no requiere suma directa ni inyectividad.

## A32-E04

**Estrategia ES.** La inclusión es inmediata por pertenencia; para estricta, hacer coincidir imágenes de vectores distintos. **中文。** 两个像集相交不代表原像来自同一个共同向量。**Resolución.** Si $z=f(v)$ con $v\in U\cap W$, pertenece a ambas imágenes. Para estricta, tome $f(x,y)=x$, $U=\langle(1,0)\rangle$, $W=\langle(1,1)\rangle$. Su intersección es cero, así $f(U\cap W)=0$, pero ambas imágenes son $\mathbb R$ y su intersección también. **Conclusión.** La inclusión puede ser estricta.

## A32-E05

**Estrategia ES.** Aplicar el teorema con el dominio finito dado. **中文。** 像的维数不是自动等于陪域维数。**Resolución.** Rango $5-2=3$. Si $\dim W=3$, la imagen es todo $W$ por igualdad finita; si $\dim W>3$, no puede serlo. Sin dato del destino, la sobreyectividad no está determinada. **Conclusión.** Rango y codimensión tienen papeles distintos.

## A32-E06

**Estrategia ES.** Traducir pertenencia de conjuntos. **中文。** 这是一般函数的集合论性质。**Demostración.** $v\in f^{-1}(E\cap F)$ equivale a $f(v)\in E$ y $f(v)\in F$, equivalente a pertenecer a las dos preimágenes. Todas las equivalencias son de definición y no usan operaciones vectoriales. **Conclusión.** No debe confundirse con propiedades de imágenes que sí pueden necesitar hipótesis extra.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
