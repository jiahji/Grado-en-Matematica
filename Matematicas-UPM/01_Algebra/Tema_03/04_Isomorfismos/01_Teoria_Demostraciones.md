---
title: Isomorfismos, coordenadas y productos / 同构、坐标映射与乘积
subject: Álgebra Lineal
tema: Guía 3.4
type: theorem
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

# Isomorfismos, coordenadas y productos — 同构、坐标映射与乘积

**Fuentes verificadas:** AL-AP-003, pp. 16–19. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.

**Organización:** esta unidad integra motivación, definiciones, teoremas, pruebas, conexiones y repaso en un archivo; ejemplos, ejercicios y soluciones se mantienen separados.


## Motivación y definiciones

**Español.** Un isomorfismo permite cambiar el lenguaje de un problema sin cambiar su estructura lineal. Una base hace precisamente eso al transformar vectores en coordenadas. **中文。** 同构不是说对象字面相同，而是存在可逆且保线性组合的对应。

Un isomorfismo $f:V\to W$ es una aplicación lineal biyectiva sobre el mismo cuerpo. Se escribe $V\cong W$. Un endomorfismo tiene dominio y destino iguales; un automorfismo es un endomorfismo que además es isomorfismo. El producto cartesiano $U\times W$ usa operaciones por componentes, distintas de sumar ambos dentro de un ambiente común.

## T1. La inversa existe exactamente para una biyección y es lineal

**Hipótesis.** $f$ lineal biyectiva. **Tesis.** Su inversa funcional es lineal y satisface ambos productos identidad; una inversa bilateral implica biyectividad.

**Estrategia ES.** Usar preimágenes únicas de dos salidas. **策略中文。** 满射只保证存在，单射保证唯一，两项都不能省略。

**Demostración.** Por biyectividad cada $w$ tiene único $v$, definiendo $f^{-1}$. Para $w=f(u)$ y $z=f(v)$, linealidad da $f(au+bv)=aw+bz$; unicidad de la preimagen implica $f^{-1}(aw+bz)=au+bv=af^{-1}(w)+bf^{-1}(z)$. Las dos composiciones son identidades por definición. Si $h$ satisface $hf=I_V$ y $fh=I_W$, de $f(u)=f(v)$ se obtiene $u=v$ aplicando $h$; para cada $w$, $w=f(h(w))$, así hay sobreyectividad. **Explicación ES.** Se corrige la proposición impresa de AL-AP-003 p. 16, que decía solo sobreyectiva y tiene corrección manuscrita. **中文解释。** 投影 $\mathbb R^2\to\mathbb R$ 有右逆却没有双侧逆，不能混淆。**Conclusión.** La condición correcta es biyectividad.

## T2. Bases y clasificación finita

**Enunciado.** Un isomorfismo transporta bases a bases. Dos espacios de dimensión finita sobre un mismo cuerpo son isomorfos si y solo si sus dimensiones son iguales.

**Estrategia ES.** Combinar preservación de independencia con generación, y construir un mapa por bases en el recíproco. **策略中文。** 等维必须建立实际映射，不能只说“看起来一样”。

**Demostración.** Si $B$ es base, inyectividad conserva independencia por 3.3 y sobreyectividad hace que sus imágenes generen todo el destino por 3.2; son base. Así un isomorfismo obliga igualdad de dimensiones. Recíprocamente, si ambas dimensiones son $n$, escoja bases $v_i,w_i$. El teorema de determinación por base define una lineal $f(v_i)=w_i$. Si $f(\sum a_iv_i)=0$, independencia de los $w_i$ da $a_i=0$, así es inyectiva. Como toda salida es combinación de los $w_i$, es sobreyectiva. **Conclusión.** Se construye un isomorfismo concreto. **中文解释。** “同一个域”是必要条件，不能把实维数与复维数直接比较。

## T3. Aplicación coordenada

Si $B=(v_1,\ldots,v_n)$ es base, $C_B:V\to\mathbb K^n$, $v\mapsto[v]_B$ es isomorfismo, con inversa $(a_i)\mapsto\sum a_iv_i$.

**Prueba completa.** La representación de $au+bv$ se obtiene sumando los coeficientes correspondientes, así $C_B$ es lineal. La unicidad de representación da inyectividad y la existencia del vector $\sum a_iv_i$ para todo coeficiente da sobreyectividad. Las dos composiciones con la fórmula inversa devuelven el vector o sus coeficientes, respectivamente. **中文解释。** 坐标映射让抽象问题可用矩阵求解，而不是把抽象向量偷偷定义成数列。

## T4. Producto externo y suma directa interna

**Enunciado.** Si $\dim U=r$, $\dim W=s$, entonces $\dim(U\times W)=r+s$. Si son subespacios de un mismo ambiente, $\Phi:U\times W\to U+W$, $(u,w)\mapsto u+w$, es sobreyectiva y es isomorfismo si y solo si $U\cap W=0$.

**Estrategia ES.** Construir una base por componentes y calcular núcleo de la suma. **策略中文。** 外直积总有有序对结构，内部相加可能把不同对混在同一向量上。

**Demostración.** Si $u_i,w_j$ son bases, los pares $(u_i,0)$ y $(0,w_j)$ generan todo par; una relación se separa por componentes y obliga todos los coeficientes cero. Son base de tamaño $r+s$. La regla $\Phi$ es lineal por operaciones componentes y sobreyectiva por definición de $U+W$. Su núcleo está formado por $(u,-u)$ con $u\in U\cap W$. Por el criterio del núcleo, es inyectiva exactamente cuando esa intersección es cero. **Conclusión.** En el caso complementario se obtiene $V\cong U\times W$. **中文解释。** 这里得到的是自然同构，而不是把内部向量与有序对字面等同。

**Explicación ES.** La aplicación coordenada cambia la representación, sin convertir por definición cada vector abstracto en una lista. El producto externo y la suma directa interna son naturalmente isomorfos en las condiciones demostradas, pero no son literalmente los mismos objetos.

## Repaso y conexiones

前置 [单满射](../03_Inyectividad_Sobreyectividad/01_Teoria_Demostraciones.md) 和直和。后续 [商空间](../../Tema_05/01_Cociente/01_Teoria_Demostraciones.md) 将构造一个不是靠任选两组基给出的自然同构。**Español.** Poder probar ambas identidades de inversa y construir una coordenada o producto explícito. **中文。** 不把原像集合 $f^{-1}(E)$ 与逆函数混用。[例题](04_Ejemplos.md)、[练习](05_Ejercicios.md)、[解答](06_Soluciones.md)。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
