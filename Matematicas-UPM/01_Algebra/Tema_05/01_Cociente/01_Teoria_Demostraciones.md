---
title: Espacio cociente / 商向量空间
subject: Álgebra Lineal
tema: Guía 2.9
type: theorem
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

# Espacio cociente — 商向量空间

**Fuentes verificadas:** AL-AP-005, pp. 2–19. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.

**Organización:** esta unidad integra motivación, definiciones, teoremas, pruebas, conexiones y repaso en un archivo; ejemplos, ejercicios y soluciones se mantienen separados.


## Motivación y equivalencia

**Español.** A veces se quiere olvidar una dirección completa de información. El cociente identifica vectores que difieren en esa dirección y convierte clases enteras en nuevos vectores. **中文。** 商空间的一个向量是整个等价类，不是任意选出的原向量；运算必须与代表元选择无关。

Una relación de equivalencia es reflexiva, simétrica y transitiva. Para un subespacio $W\le V$, definir $u\sim v$ si $u-v\in W$. Es equivalencia: $u-u=0\in W$; invertir la diferencia da simetría; sumar dos diferencias da transitividad. La clase $[v]=v+W=\{v+w:w\in W\}$. Dos clases son iguales o disjuntas: si comparten un elemento, restar sus representaciones muestra diferencia de representantes en $W$, de donde cada elemento de una clase está en la otra. Así forman una partición. Se define $V/W=\{[v]:v\in V\}$.

## T1. Operaciones bien definidas y estructura

Se proponen $[u]+[v]=[u+v]$ y $a[u]=[au]$.

**Hipótesis.** $W$ subespacio. **Tesis.** Las reglas no dependen de representantes y convierten $V/W$ en espacio vectorial, con cero $[0]=W$.

**Estrategia ES.** Comparar dos representantes de cada clase mediante sus diferencias en $W$. **策略中文。** 良定义是新对象成立的前提，不能在写公式后直接跳过。

**Demostración.** Si $u-u',v-v'\in W$, entonces $(u+v)-(u'+v')=(u-u')+(v-v')\in W$, por lo que ambas sumas dan la misma clase. Asimismo $au-au'=a(u-u')\in W$. Una vez bien definidas, asociatividad y conmutatividad se heredan de $V$ al tomar clases. El neutro es $[0]$ y el opuesto $[-u]$ porque $[u]+[-u]=[0]$. Las dos distributividades y compatibilidad escalar resultan de las igualdades correspondientes en $V$, por ejemplo $a([u]+[v])=[a(u+v)]=[au+av]=a[u]+a[v]$, y $1[u]=[u]$. Así se cumplen todos los axiomas. $[v]=[0]$ equivale exactamente a $v\in W$. **Conclusión.** La construcción es legítima. **中文解释。** 一般陪集 $v+W$ 本身不是原空间的子空间，除非 $v\in W$；新零是整个 $W$，不是集合只含原零。

## T2. Base y dimensión finita del cociente

**Hipótesis.** $\dim V=n$, $W$ de base $(w_1,\ldots,w_r)$, completada a $(w_1,\ldots,w_r,v_{r+1},\ldots,v_n)$. **Tesis.** $([v_{r+1}],\ldots,[v_n])$ es base y $\dim(V/W)=n-r$.

**Estrategia ES.** Descartar en clases los términos de $W$ y probar independencia usando la base original. **策略中文。** 不能简单把“去掉 $r$ 个方向”作为维数公式证明。

**Demostración.** Todo $u$ se escribe $\sum a_iw_i+\sum b_jv_j$, así $[u]=\sum b_j[v_j]$, probando generación. Si esa última combinación es $[0]$, $\sum b_jv_j\in W$ y puede escribirse $\sum c_iw_i$. La relación resultante en la base total obliga todos los $b_j=0$. Son independientes y hay $n-r$. **Conclusión.** También se obtienen las coordenadas de una clase a partir de la base adaptada. **中文解释。** 代表元的 $W$ 坐标可改变，但剩余坐标在同一类内固定。

## T3. Proyección, propiedad universal y primer teorema de isomorfía

La proyección $\pi:V\to V/W$, $v\mapsto[v]$, es lineal por definición de operaciones, sobreyectiva porque toda clase tiene representante y tiene núcleo $W$.

**Enunciado.** Si $f:V\to U$ es lineal y $W\subset\ker f$, existe única lineal $\bar f:V/W\to U$ con $f=\bar f\circ\pi$. Para $W=\ker f$, su restricción de destino a $\operatorname{Im}f$ es isomorfismo.

**Estrategia ES.** Definir $\bar f([v])=f(v)$, comprobar representantes y calcular su núcleo. **策略中文。** 像空间作为陪域必须明确，不能把映到整个 $U$ 的规则无条件称为满射。

**Demostración.** Si $[v]=[v']$, $v-v'\in W\subset\ker f$, así $f(v)=f(v')$. La regla está bien definida, preserva combinaciones porque $f$ lo hace y cumple la factorización. Cualquier regla que la cumpla debe enviar $[v]=\pi(v)$ a $f(v)$, demostrando unicidad. Para $W=\ker f$, $\bar f([v])=0$ equivale a $v\in\ker f$, es decir $[v]=[0]$, así es inyectiva. Toda salida en $\operatorname{Im}f$ es $f(v)$ y tiene preimagen $[v]$, así es sobreyectiva sobre ese destino. **Conclusión.** $V/\ker f\cong\operatorname{Im}f$, sin necesitar dimensión finita. **中文解释。** 这比“两个空间维数相同所以同构”更自然，它保留了原映射如何压缩核的信息。

## Dos teoremas adicionales de isomorfía — 补充同构定理

Se ofrecen como **suplemento propio**, no transcripción de Hoja 5 mencionada en p. 17. Para $U,W\le V$,

$$
U/(U\cap W)\cong(U+W)/W.
$$

**Prueba.** $g:U\to(U+W)/W$, $u\mapsto[u]$, es lineal, sobreyectiva porque $[u+w]=[u]$, y núcleo $U\cap W$. Aplicar T3 da la fórmula. Si $W\subset U\subset V$,

$$
(V/W)/(U/W)\cong V/U.
$$

**Prueba.** $q:V/W\to V/U$, $[v]_W\mapsto[v]_U$, está bien definida porque diferencias en $W$ están en $U$; es lineal y sobreyectiva, y su núcleo son las clases con representante en $U$, exactamente $U/W$. T3 da la fórmula. Estas comprobaciones también prueban las condiciones de cada uso del teorema.

**Español.** La clase cero es todo $W$; un representante aislado no es el nuevo vector. La buena definición elimina la dependencia del representante, y la base adaptada demuestra qué coordenadas sobreviven. Se recomienda estudiar esta unidad después de aplicaciones e isomorfismos, conservando su número oficial 2.9.

## Repaso y dependencias

本节放在已建立 [线性映射与同构](../../Tema_03/04_Isomorfismos/01_Teoria_Demostraciones.md) 之后学习，尽管其官方编号是 2.9；这是一条明确的逻辑学习顺序，不改官方编号。**Español.** Dominar representante, clase, igualdad de clases, buena definición y destino de la aplicación inducida. **中文。** 避免把陪集当成原空间子空间、把有限维差公式用于无限基数。[例题](04_Ejemplos.md)、[题目](05_Ejercicios.md)、[解答](06_Soluciones.md)。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
