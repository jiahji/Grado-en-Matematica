---
title: Espacio cociente / 商向量空间 — soluciones
subject: Álgebra Lineal
tema: Guía 2.9
type: exercises
language: es-zh
status: complete
tags:
- algebra_lineal
- apartado_2_9
sources:
- ../../../00_Fuentes/Algebra_Lineal/AL-GD-001/GA_30GM_305000100_ES_2026-27.pdf
- ../../../00_Fuentes/Algebra_Lineal/AL-AP-005/Tema 5_83d0e9c7501214116f707ed90d6a34d8.pdf
updated: 2026-10-26
---

# Soluciones 2.9 — 完整解答

**Fuentes verificadas:** AL-AP-005, pp. 2–19. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.


Resoluciones propias de [A29-E01–E06](05_Ejercicios.md).

## A29-E01

**Estrategia ES.** Usar diferencia de representantes y condición de contener cero. **中文。** 类本身与类作为新向量的角色不同。**Resolución.** $[v]=[0]$ equivale por definición a $v-0\in W$. Si $v+W$ es subespacio, contiene cero, así $0=v+w$ para algún $w\in W$, dando $v=-w\in W$. Si $v\in W$, $v+W=W$, que sí es subespacio. **Conclusión.** Se prueban las dos equivalencias.

## A29-E02

**Estrategia ES.** Eliminar la tercera componente mediante el vector de $W$. **中文。** 不把第三分量直接丢掉，而是减去同一个对角方向。**Resolución.** $(a,b,c)-c(1,1,1)=(a-c,b-c,0)$, así la clase es $(a-c)[e_1]+(b-c)[e_2]$. Si $ue_1+ve_2\in W$, su tercera coordenada cero obliga a que el múltiplo de $(1,1,1)$ sea cero, y luego $u=v=0$. **Conclusión.** Base y coordenadas $(a-c,b-c)$ verificadas.

## A29-E03

**Estrategia ES.** Calcular núcleo e imagen antes de inducir. **中文。** 定义目标为实际像。**Resolución.** Núcleo $\langle(-1,1,-1)\rangle$, imagen $\mathbb R^2$ por las imágenes de $e_1,e_3$. La regla $\bar f([(x,y,z)])=(x+y,y+z)$ está bien definida porque diferencias en el núcleo se anulan. Si su valor es cero, el representante está en el núcleo y su clase es cero; es inyectiva. Para salida $(a,b)$, el representante $(a,0,b)$ la produce, así es sobreyectiva. **Conclusión.** Isomorfismo explícito del cociente con $\mathbb R^2$.

## A29-E04

**Estrategia ES.** Examinar cuándo dos representantes son equivalentes. **中文。** 极端情况也遵循同一定义。**Resolución.** En $V/V$ toda diferencia pertenece a $V$, así hay una sola clase, el espacio cero. En $V/\{0\}$, dos clases coinciden solo si sus representantes son iguales, y $v\mapsto[v]$ es lineal biyectiva con inversa $[v]\mapsto v$. **Conclusión.** No se intercambian estos dos casos.

## A29-E05

**Estrategia ES.** Usar el subgrupo aditivo entero y dos representantes de la misma clase. **中文。** 加法商的存在不自动给实向量空间。**Demostración.** Reflexividad: $x-x=0\in\mathbb Z$; simetría: cambiar signo mantiene entero; transitividad: sumar diferencias enteras. Pero $[0]=[1]$, mientras multiplicar por $1/2$ daría $[0]$ y $[1/2]$, distintos porque su diferencia no es entera. **Conclusión.** $\mathbb Z$ no es subespacio real, y la operación escalar propuesta falla buena definición.

## A29-E06

**Estrategia ES.** Tomar dimensiones finitas de los dos cocientes. **中文。** 这是对已有 Grassmann 证明的另一条推导，而不是最初用它循环证明商维数。**Resolución.** El isomorfismo da $\dim U-\dim(U\cap W)=\dim(U+W)-\dim W$. Reordenar produce Grassmann. La fórmula de dimensión del cociente se probó por base adaptada sin usar Grassmann, así esta deducción alternativa no es circular. **Conclusión.** Ambas rutas son consistentes.

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
