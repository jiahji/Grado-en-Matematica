---
title: Inyectividad, sobreyectividad y biyectividad / 单射、满射与双射 — soluciones
subject: Álgebra Lineal
tema: Guía 3.3
type: exercises
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

# Soluciones 3.3 — 完整解答

**Fuentes verificadas:** AL-AP-003, pp. 14–16. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Resoluciones propias de [A33-E01–E06](05_Ejercicios.md).

## A33-E01

**Estrategia ES.** Resolver el núcleo y comparar dimensión inicial y final. **中文。** 不仅看输出有三个分量。**Resolución.** $x+y=0$, $y+z=0$ dan $x=z=-y$, y la tercera ecuación $x-z=0$ es redundante. Núcleo $\langle(-1,1,-1)\rangle$, nulidad $1$, rango $2$. Con dominio y destino de dimensión $3$, no es inyectiva ni sobreyectiva. **Conclusión.** Tres fórmulas no garantizan rango tres.

## A33-E02

**Estrategia ES.** Traducir definiciones; después dar proyección e inclusión. **中文。** 复合中有些方向的信息不能倒推。**Demostración.** Si $f(u)=f(v)$, aplicar $g$ da igualdad en $g\circ f$; su inyectividad fuerza $u=v$. Si para todo $z$ existe $v$ con $g(f(v))=z$, $f(v)$ es una preimagen para $g$, así esta es sobreyectiva. Para negar las otras conclusiones, tome $f(t)=(t,0)$ de $\mathbb R$ a $\mathbb R^2$ y $g(x,y)=x$. La composición es identidad, pero $f$ no es sobreyectiva y $g$ no es inyectiva. **Conclusión.** Exactamente las implicaciones probadas son generales.

## A33-E03

**Estrategia ES.** Aplicar los dos criterios de rango. **中文。** 同时用定义域与陪域维数。**Resolución.** Nulidad $4-3=1$, así no inyectiva; rango menor que dimensión del destino, así no sobreyectiva. **Conclusión.** No es biyectiva.

## A33-E04

**Estrategia ES.** Usar que un vector no nulo forma familia independiente. **中文。** 单元素族足以检测核。**Demostración.** Si $v\ne0$ y $f(v)=0$, la familia $(v)$ es independiente pero su imagen $(0)$ es dependiente, contradicción. Luego el núcleo solo contiene cero y T1 da inyectividad. **Conclusión.** El criterio de preservación también tiene recíproco.

## A33-E05

**Estrategia ES.** Dar una inclusión y después usar la cota de rango. **中文。** 不能用某个例子的失败代替一般不可能性。**Resolución.** $f(t)=(t,0)$ es lineal y núcleo cero. Cualquier lineal desde un dominio de dimensión $1$ tiene rango a lo sumo $1$, menor que $2$, así ninguna es sobreyectiva al destino indicado. **Conclusión.** Se distinguen construcción e imposibilidad.

## A33-E06

**Estrategia ES.** Multiplicar polinomios por $x$. **中文。** 不借助无限维减法。**Resolución.** $S(p)=xp$ es lineal. Si $xp=0$ como polinomio, todos los coeficientes de $p$ son cero, así es inyectiva. Ningún $xp$ tiene término constante $1$, así no obtiene el polinomio $1$. **Conclusión.** Endomorfismo inyectivo no sobreyectivo; la hipótesis finita era necesaria.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
