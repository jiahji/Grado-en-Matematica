---
title: Pruebas sobre cuerpos y complejos / 域与复数的完整证明
subject: Álgebra Lineal
tema: Tema 0 · Guía 1.4
type: proof
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

# Pruebas sobre cuerpos y complejos — 完整证明

**Fuentes de partida:** AL-AP-000 pp. 11–15. Las ocho pruebas siguientes son desarrollo didáctico propio de los resultados, utilizando [las definiciones](01_Definiciones.md).

## P1. Unicidad de neutros, opuestos e inversos

**Hipótesis.** Un cuerpo $\mathbb K$.

**Tesis.** Las unicidades de T1.

**Estrategia — Español.** Comparar dos candidatos mediante sus propiedades definitorias.

**策略 — 中文。** 先假设有两个候选对象，再用公理证明它们必须相等，而不是把“唯一”偷偷写进存在公理。

**Demostración.** Si $0$ y $0'$ son neutros aditivos, $0=0+0'=0'$.Si $1,1'$ son unidades multiplicativas, $1=1\cdot1'=1'$.Si $a+b=0$ y $a+c=0$, entonces

$$
b=b+0=b+(a+c)=(b+a)+c=0+c=c.
$$

Si $ab=ac=1$ para dos candidatos a inverso de un mismo $a\ne0$, entonces

$$
b=b(ac)=(ba)c=1c=c.
$$

**Explicación — Español.** Se han usado asociatividad, conmutatividad y los neutros, no una regla de cancelación multiplicativa todavía pendiente de prueba.

**中文解释。** 不能先假设可约去 $a$，再用其证明逆元唯一，否则会把待证性质循环使用。

**Conclusión.** Las notaciones $-a$ y $a^{-1}$ son inequívocas.

## P2. Producto por cero y ausencia de inverso de cero

**Hipótesis.** $a\in\mathbb K$, con $0\ne1$.

**Tesis.** $a0=0$ y el cero no tiene inverso.

**Estrategia — Español.** Distribuir $a(0+0)$ y cancelar un sumando usando opuestos aditivos.

**策略 — 中文。** 乘零得零要由域公理推出，再用它说明零不可能乘出 1。

**Demostración.** $a0=a(0+0)=a0+a0$.Sumando el opuesto de $a0$ a ambos miembros resulta $0=a0$.Por conmutatividad $0a=0$ también. Si existiera $u$ con $0u=1$, se tendría $0=1$, contrario a la hipótesis.

**Explicación — Español.** La demostración solo cancela sumandos, que sí tienen opuesto por los axiomas aditivos.

**中文解释。** 若遗漏 $0\ne1$，这个反证就失去前提，也会把退化的单元素系统混入通常域的概念。

**Conclusión.** El dominio de la inversión debe excluir cero.

## P3. Producto nulo y cancelación no nula

**Hipótesis.** $a,b,c\in\mathbb K$.

**Tesis.** Si $ab=0$, alguno es cero; si $a\ne0$ y $ab=ac$, $b=c$.

**Estrategia — Español.** Separar $a=0$ y multiplicar por $a^{-1}$ en el otro caso.

**策略 — 中文。** 唯一允许约因子的步骤明确使用非零元素的逆元。

**Demostración.** Si $a=0$, la primera afirmación ya se cumple. Si $a\ne0$ y $ab=0$, entonces $b=(a^{-1}a)b=a^{-1}(ab)=a^{-1}0=0$ por P2. Si $ab=ac$ y $a\ne0$, multiplicar ambos miembros por $a^{-1}$ y usar asociatividad da $b=c$.

**Explicación — Español.** Para matrices, un factor no nulo puede carecer de inverso; por eso ese razonamiento no se traslada sin condición adicional.

**中文解释。** 不能只因为一个矩阵里有非零元素，就把它当作这里的非零标量约去。

**Conclusión.** Se completan las propiedades de T1.

## P4. Construcción del cuerpo complejo

**Hipótesis.** $\mathbb C=\mathbb R^2$ con las operaciones definidas, usando la aritmética del cuerpo real.

**Tesis.** Se cumplen todos los axiomas de cuerpo y la fórmula de la inversa de T2.

**Estrategia — Español.** Comprobar por coordenadas las leyes aditivas, multiplicativas y distributivas, y construir cada inverso no nulo.

**策略 — 中文。** 不能只验证逆元公式，就直接称整个结构为域；结合律与分配律也必须核实。

**Demostración.** Las dos operaciones son internas porque sus componentes son sumas y productos reales. La suma es asociativa y conmutativa componente a componente: por ejemplo, con $z=(a,b)$, $w=(c,d)$, $u=(e,f)$, ambos agrupamientos de su suma son $(a+c+e,b+d+f)$.Su neutro es $(0,0)$ y el opuesto de $(a,b)$ es $(-a,-b)$.

La conmutatividad del producto se sigue de $ac-bd=ca-db$ y $ad+bc=cb+da$.Su unidad es $(1,0)$, distinta de $(0,0)$, ya que $(a,b)(1,0)=(a,b)$.

Para la asociatividad, $((a,b)(c,d))(e,f)$ tiene componentes

$$
ace-bde-adf-bcf,\qquad acf-bdf+ade+bce.
$$

El otro agrupamiento $(a,b)((c,d)(e,f))$ tiene componentes

$$
a(ce-df)-b(cf+de),\qquad a(cf+de)+b(ce-df),
$$

que, al distribuir en $\mathbb R$, son las mismas expresiones. Para la distributividad, $z(w+u)$ tiene componentes

$$
a(c+e)-b(d+f),\qquad a(d+f)+b(c+e),
$$

y al distribuir resultan $(ac-bd)+(ae-bf)$ y $(ad+bc)+(af+be)$, las componentes de $zw+zu$.

Si $(a,b)\ne(0,0)$, $a^2+b^2>0$.La pareja

$$
\left(\frac a{a^2+b^2},\frac{-b}{a^2+b^2}\right)
$$

multiplicada por $(a,b)$ da $(1,0)$, pues la primera componente es $(a^2+b^2)/(a^2+b^2)=1$ y la segunda $(-ab+ba)/(a^2+b^2)=0$.La conmutatividad ya probada da el inverso por ambos lados. Así se verifican todos los axiomas.

Finalmente, $(a,0)+(c,0)=(a+c,0)$ y $(a,0)(c,0)=(ac,0)$, de modo que los reales identificados conservan sus operaciones. Con $i=(0,1)$, $i^2=(-1,0)$ y $(a,b)=(a,0)+(b,0)i$.

**Explicación — Español.** La positividad del denominador usa que $a,b$ son reales. La representación como pareja evita usar reglas de raíces complejas antes de construirlas.

**中文解释。** 把实数嵌入为第二坐标为零的复数，使“扩充实数”成为一个精确的代数结论。零的倒数始终没有被定义。

**Conclusión.** $\mathbb C$ es un cuerpo que contiene una copia de $\mathbb R$.

## P5. Conjugación y módulo multiplicativo

**Hipótesis.** $z=a+bi$, $w=c+di$.

**Tesis.** Las identidades de conjugación, $z\bar z=|z|^2$ y $|zw|=|z||w|$.

**Estrategia — Español.** Expandir y comparar partes reales e imaginarias; para módulos, comparar cuadrados no negativos.

**策略 — 中文。** 两个非负实数的平方相等才可推出它们相等；模的非负性不能省略。

**Demostración.**

$$
\overline{z+w}=(a+c)-(b+d)i=\bar z+\bar w,
$$

$$
\overline{zw}=(ac-bd)-(ad+bc)i=(a-bi)(c-di)=\bar z\bar w.
$$

Conjugar dos veces cambia dos veces el signo de $b$, por lo que $\overline{\bar z}=z$.Además $(a+bi)(a-bi)=a^2+b^2=|z|^2$.Por tanto

$$
|zw|^2=(zw)\overline{zw}=zw\bar z\bar w=(z\bar z)(w\bar w)=|z|^2|w|^2.
$$

Ambos $|zw|$ y $|z||w|$ son no negativos, luego sus cuadrados iguales implican igualdad. Por último, $|z|=0$ equivale a $a^2+b^2=0$, que para reales equivale a $a=b=0$.

**Explicación — Español.** Se usa la conmutatividad de los complejos, ya probada. El mismo reordenamiento no sería válido para matrices arbitrarias.

**中文解释。** 共轭乘积产生模平方，既给出长度关系，也解释分母有理化。它没有把共轭本身直接变成逆元。

**Conclusión.** Se prueban las identidades algebraicas de T3.

## P6. Desigualdad triangular

**Hipótesis.** $z=a+bi$, $w=c+di$.

**Tesis.** $|z+w|\le|z|+|w|$.

**Estrategia — Español.** Probar primero la desigualdad escalar necesaria mediante un cuadrado no negativo.

**策略 — 中文。** 不直接借用尚未讲授的内积不等式；在二维实数坐标中把差写成一个平方即可。

**Demostración.**

$$
(a^2+b^2)(c^2+d^2)-(ac+bd)^2=(ad-bc)^2\ge0.
$$

De ello se deduce $ac+bd\le\sqrt{(a^2+b^2)(c^2+d^2)}=|z||w|$.Así

$$
|z+w|^2=|z|^2+|w|^2+2(ac+bd)
\le(|z|+|w|)^2.
$$

Tomar raíces cuadradas de ambos lados es lícito porque ambos lados proceden de cantidades no negativas, y da la tesis.

**Explicación — Español.** Del primer paso se obtiene una cota para el valor absoluto de $ac+bd$, que implica también la cota superior que se necesita.

**中文解释。** 两个复数对应平面向量，三角不等式表达合位移长度不超过两段路径长度；证明仍完全基于实数恒等式。

**Conclusión.** Se completa T3.

## P7. Producto polar y De Moivre

**Hipótesis.** $z=r(\cos\theta+i\sin\theta)$ y $w=s(\cos\varphi+i\sin\varphi)$.

**Tesis.** El producto polar y la fórmula para potencias naturales.

**Estrategia — Español.** Expandir el producto y usar fórmulas trigonométricas de suma; después inducción en el exponente.

**策略 — 中文。** 先证明两项相乘时角度相加，再用归纳法推广到重复乘法，而不是把整数倍角公式直接当作定义。

**Demostración.** Distribuir da parte real $rs(\cos\theta\cos\varphi-\sin\theta\sin\varphi)=rs\cos(\theta+\varphi)$ y parte imaginaria $rs(\sin\theta\cos\varphi+\cos\theta\sin\varphi)=rs\sin(\theta+\varphi)$.Esto prueba el producto. Para $n=0$, $z^0=1=r^0(\cos0+i\sin0)$.Si la fórmula vale para $n$, multiplicar por $z$ y usar el producto probado da módulo $r^{n+1}$ y argumento $(n+1)\theta$.La inducción concluye para todo $n\ge0$.

**Explicación — Español.** Los argumentos pueden variar en múltiplos de $2\pi$ sin cambiar el complejo resultante.

**中文解释。** 公式建立在极形式和三角加法公式上，不要求提前定义复指数 $e^{i\theta}$。

**Conclusión.** Se prueba T4.

## P8. Exhaustividad de las raíces

**Hipótesis.** $z=r(\cos\theta+i\sin\theta)\ne0$ y $n\ge1$.

**Tesis.** T5, incluidos número, distinción y exhaustividad de raíces.

**Estrategia — Español.** Elevar las candidatas, comparar argumentos módulo $2\pi$ y forzar módulo y argumento de cualquier otra raíz.

**策略 — 中文。** 证明分三步：候选都有效、彼此不同、任何解都已经列入。

**Demostración.** Para cada $k=0,\ldots,n-1$, De Moivre da $w_k^n=r(\cos(\theta+2k\pi)+i\sin(\theta+2k\pi))=z$.Si $w_k=w_\ell$, sus argumentos difieren en un múltiplo entero de $2\pi$, por lo que $(k-\ell)/n$ es entero. Como $|k-\ell|<n$, se deduce $k=\ell$.

Sea ahora $w=\rho(\cos\varphi+i\sin\varphi)$ cualquier raíz. No es cero porque $z\ne0$. La igualdad de módulos da $\rho^n=r$ y $\rho=r^{1/n}>0$.La igualdad angular implica $n\varphi=\theta+2q\pi$ para algún entero $q$. Escribiendo $q=kn+j$ con $0\le j<n$, se tiene $\varphi=(\theta+2j\pi)/n+2k\pi$, de modo que $w=w_j$.Esto prueba exhaustividad.

Si $w^n=0$, entonces $|w|^n=0$ y por P5 $w=0$; por eso cero tiene una sola raíz como valor.

**Explicación — Español.** El argumento de una raíz no se obtiene simplemente dividiendo un argumento elegido por $n$ y olvidando su ambigüedad de $2\pi$.

**中文解释。** 除角之前必须保留整圈项；除以 $n$ 后，原来等价的整圈会分成 $n$ 个不同方向，这正是全部根的来源。

**Conclusión.** Se prueba T5. Continúe con [ejemplos](04_Ejemplos.md).
