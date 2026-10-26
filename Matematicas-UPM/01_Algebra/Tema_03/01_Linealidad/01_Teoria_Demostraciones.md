---
title: Aplicaciones lineales / 线性映射
subject: Álgebra Lineal
tema: Guía 3.1
type: theorem
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

# Aplicaciones lineales — 线性映射

**Fuentes verificadas:** AL-AP-003, pp. 2–8. Las pruebas detalladas y actividades marcadas como propias son desarrollo didáctico; no se atribuyen a una hoja de ejercicios o examen recibido.

**Organización:** esta unidad integra motivación, definiciones, teoremas, pruebas, conexiones y repaso en un archivo; ejemplos, ejercicios y soluciones se mantienen separados.


## Motivación y definición formal

**Español.** Una regla lineal transporta la construcción por combinaciones sin alterar sus coeficientes. Por eso conocerla en una base basta para conocerla en todos los vectores. **中文。** 线性映射保存的是线性构造，不是长度、角度或向量的具体图形。

Sean $V,W$ espacios sobre el **mismo** cuerpo $\mathbb K$. $f:V\to W$ es lineal si $f(u+v)=f(u)+f(v)$ y $f(av)=af(v)$ para todos $u,v\in V$, $a\in\mathbb K$. La composición $g\circ f$ aplica primero $f$ y después $g$.

## T1. Combinaciones finitas y consecuencias

**Enunciado.** Linealidad equivale a conservar toda combinación finita: $f(\sum a_iv_i)=\sum a_if(v_i)$. Además $f(0_V)=0_W$ y $f(-v)=-f(v)$.

**Hipótesis/Tesis.** Probar equivalencia y consecuencias. **Estrategia ES.** Usar inducción para sumas y escoger casos especiales en el recíproco. **策略中文。** 不能把“对两个向量可加”直接当成对任意有限和的未证结论。

**Demostración.** De $f(0+0)=f(0)+f(0)$, cancelar da $f(0)=0$. Como $f(v)+f(-v)=f(0)=0$, la unicidad de opuesto da la segunda propiedad. Para una combinación de un término vale homogeneidad. Si la fórmula vale para $r$ términos, separar el término $r+1$, aplicar aditividad y homogeneidad, y después la hipótesis inductiva prueba la fórmula para $r+1$. El caso vacío es $f(0)=0$. Recíprocamente, escoger dos términos con coeficientes $1$ da aditividad; uno con coeficiente $a$ da homogeneidad. **Conclusión.** La equivalencia no añade hipótesis ocultas. **中文解释。** 线性必须对所有标量成立，不能仅检查正数或某几个系数。

## T2. Imágenes de una base determinan una única aplicación

**Enunciado de aula p. 7.** Si $B=(v_1,\ldots,v_n)$ es base de $V$ y $w_1,\ldots,w_n\in W$ son cualesquiera, existe única lineal $f$ con $f(v_i)=w_i$.

**Estrategia ES.** Definir con coordenadas y comprobar que las operaciones respetan esas coordenadas. **策略中文。** 定义良好依赖基表示唯一；目标向量不必无关，也不必构成基。

**Demostración.** Para $v=\sum a_iv_i$, definir $f(v)=\sum a_iw_i$. La unicidad de coeficientes asegura que un vector no recibe dos salidas. Si $u=\sum b_iv_i$, $\alpha v+\beta u=\sum(\alpha a_i+\beta b_i)v_i$, de donde

$$
f(\alpha v+\beta u)=\sum_i(\alpha a_i+\beta b_i)w_i=\alpha f(v)+\beta f(u).
$$

Así es lineal y sus valores en base son los indicados. Cualquier otra lineal $g$ con esos valores cumple $g(v)=\sum a_ig(v_i)=\sum a_iw_i=f(v)$ para todo $v$. **Explicación ES.** Para una lista dependiente no se pueden asignar imágenes arbitrarias: deben respetar sus relaciones. **中文解释。** 原像基压缩了需要给出的信息，但不会限制所有输出一定不同。**Conclusión.** Existencia y unicidad están probadas.

## T3. Composición y mapas matriciales

Si $f:V\to W$ y $g:W\to Z$ son lineales, $g\circ f$ es lineal: aplicar ambas reglas a $\alpha u+\beta v$ da $\alpha g(f(u))+\beta g(f(v))$. Si $A\in M_{m\times n}(\mathbb K)$, $f_A(x)=Ax$ es lineal por distributividad y compatibilidad con escalares ya demostradas. No hace falta que $A$ sea cuadrada ni invertible.

Una regla afín $x\mapsto Ax+b$ es lineal si y solo si $b=0$: la necesidad sale de $f(0)=b$ y T1; la suficiencia es el caso matricial. La recíproca «$f(0)=0$ implica lineal» es falsa: $f(x)=x^2$ cumple la condición en cero pero $f(1+1)=4\ne2=f(1)+f(1)$ sobre $\mathbb R$.

## Dominios correctos y repaso

La derivada no está definida en todas las funciones de $\mathbb R$ a $\mathbb R$: $|x|$ no es derivable en cero. Se corrige el ejemplo de AL-AP-003 p. 6 usando $D:\mathbb R[x]\to\mathbb R[x]$; derivar coeficientes prueba ambas leyes. Alternativamente $D:C^1\to C^0$ requiere la teoría analítica correspondiente y no se supone aquí demostrada.

前置为 [基](../../Tema_01/04_Bases_Dimension/01_Teoria_Demostraciones.md)。后续 [核与像](../02_Nucleo_Imagen_Rango/01_Teoria_Demostraciones.md)。自测 ES: declarar dominios y cuerpo, probar dos leyes, construir el mapa por base. 中文：不要把保零条件当成充分条件，也不混淆映射复合顺序。[例题](04_Ejemplos.md)、[题目](05_Ejercicios.md)、[解答](06_Soluciones.md)。

## Navegación de la unidad — 单元导航

[Teoría y demostraciones / 理论与证明](01_Teoria_Demostraciones.md) · [Ejemplos / 例题](04_Ejemplos.md) · [Ejercicios / 习题](05_Ejercicios.md) · [Soluciones / 解答](06_Soluciones.md) · [Índice del Tema / 章节目录](../00_Indice.md).
