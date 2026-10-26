---
title: "Errores y dudas detectados / 错误与疑点"
subject: "General"
tema: null
type: tracking
language: es-zh
status: partial
tags: [errores, verificacion]
sources: []
updated: 2026-10-26
---

# Errores y dudas detectados — 错误与疑点

Se han identificado las incidencias siguientes mediante contraste del texto impreso con páginas renderizadas. Se conservan los originales y las anotaciones. La autoría de los errores o de las correcciones manuscritas no se presume.

以下问题已按实际 PDF 页面定位。修正用于本库的后续正式教材；不表示整份讲义已经完成数学审核。

## Protocolo de registro — 实际问题的登记方式

发现问题时分配稳定编号，记录：

1. 科目、相关 Tema 和真实来源链接。
2. 页码或可复查定位，以及准确原始表述；无法辨认的内容明确标记。
3. 问题类型：疑似 OCR 错误、定义歧义、符号冲突、缺失假设、错误结论、证明漏洞、缺页或资料矛盾。
4. 数学分析：为什么可疑或不成立；必要时给出满足前提但否定结论的有效反例。
5. 正确结论或建议修正，及其依据。尚不能确定时保持 `Pendiente de verificación`，不能自行认定教授原意。
6. 影响的已有笔记、习题、解答和知识链接，以及采取的最小必要修改。
7. 状态、处理日期、尚需核实的事项，以及是否得到用户或教授的明确确认。

## Estados — 处理状态

- `Pendiente de verificación`：原文、符号或结论尚不能确认。
- `En análisis`：已定位，正在检查数学原因和影响范围。
- `Corregido en las notas`：正式笔记已使用正确结论，原件保留；不自动表示已得到教授确认。
- `Resuelto`：问题与依据已明确，关联文件完成必要更新，记录结论和复核范围。

没有实际问题时不预填虚构原话、页码或教授纠正说明。原始材料始终保留；修正不会静默抹去原始表述的可追溯性。

参见 [来源管理](../00_Fuentes/README.md)、[待办](Pendientes.md) 和 [覆盖矩阵](Cobertura_Temario.md)。

## AL-ERR-001 — Inversos y definición de cuerpo / 域公理条件

**Fuente:** [AL-AP-000](../00_Fuentes/Algebra_Lineal/AL-AP-000/Tema%200%286%29.pdf), p. 15; [AL-AP-012](../00_Fuentes/Algebra_Lineal/AL-AP-012/Temas%201%20y%202%281%29%282%29.pdf), p. 2, ítem 8. 原印刷表述在全体 $a,b,c\in K$ 的统一范围下写：

> existe un elemento $1/a$ tal que $(1/a)\cdot a=1$.

**Análisis — Español.** Falta restringir $a\ne0$ y explicitar $0\ne1$. En los cuerpos usuales, $0$ no tiene inverso, pues $0x=0$ para todo $x$ y no puede ser $1$.

**中文。** 不是每个数都可取倒数；若把零也包括进去，就与域中 $0\ne1$ 矛盾。正式定义应要求加法群、非零元素的乘法群及分配律，或等价地在公理列表中补足这两项。

**Estado:** 条件缺失已确认；本批矩阵模块仅在 $\mathbb Q,\mathbb R,\mathbb C$ 上使用正确的非零标量逆元条件，完整域定义及其证明已在 Tema 0 的复数与域单元落实。

## AL-ERR-002 — Inverso complejo / 复数逆元

**Fuente:** [AL-AP-000](../00_Fuentes/Algebra_Lineal/AL-AP-000/Tema%200%286%29.pdf), p. 12. 印刷写：

> En $\mathbb C$, todo número $a+bi$ tiene inverso $c+di$.

手写批注在该处补了非零条件。p. 10 有理数表示的印刷集合也省略 $b\ne0$，而手写已补。

**Análisis — Español.** La fórmula de la inversa exige $a^2+b^2\ne0$, equivalente a $a+bi\ne0$. La fracción racional exige denominador no nulo. Las correcciones manuscritas concuerdan con las condiciones correctas.

**中文。** 原件的批注本身提供了正确修正，正式笔记应保留“印刷遗漏、批注已补”的追踪信息。不能只抄印刷层，把零的逆元写进教材。

**Estado:** 已确认并记录；复数单元已明确非零条件，并通过构造验证逆元。

## AL-ERR-003 — Dominio de la derivada / 微分映射的定义域

**Fuente:** [AL-AP-003](../00_Fuentes/Algebra_Lineal/AL-AP-003/Tema%203_3783d906f8056ce104fc5d6bc1f5548c.pdf), p. 6. 印刷给出 $D:\mathcal F(\mathbb R,\mathbb R)\to\mathcal F(\mathbb R,\mathbb R)$，并定义 $D(f)=f'$。

**Análisis — Español.** Si $\mathcal F$ denota todas las funciones, $D$ no está definida para todas ellas: $f(x)=|x|$ no es derivable en $0$. Una versión correcta es $D:\mathbb R[x]\to\mathbb R[x]$, o $D:C^1(\mathbb R)\to C^0(\mathbb R)$, con los dominios correspondientes bien definidos.

**中文。** 线性映射首先必须是一个对定义域每个元素都有输出的函数；尚未验证存在导数，就不能只讨论其线性性。

**Estado:** `Corregido en las notas`。已在 [3.1 线性映射](../01_Algebra/Tema_03/01_Linealidad/01_Teoria_Demostraciones.md) 使用多项式定义域并说明 $C^1$ 到 $C^0$ 的正确版本。

## AL-ERR-004 — Sobreyectiva frente a biyectiva / 满射与双侧逆

**Fuente:** [AL-AP-003](../00_Fuentes/Algebra_Lineal/AL-AP-003/Tema%203_3783d906f8056ce104fc5d6bc1f5548c.pdf), p. 16. 印刷命题以「Si $f:V\to W$ es sobreyectiva」推出存在 $f^{-1}$ 且同时满足 $f\circ f^{-1}=\operatorname{Id}_W$、$f^{-1}\circ f=\operatorname{Id}_V$。旁边的手写蓝字已明确改为 lineal y biyectiva。

**Análisis — Español.** La existencia de inversa por ambos lados requiere biyectividad. La proyección $f:\mathbb R^2\to\mathbb R$, $f(x,y)=x$, es lineal y sobreyectiva, pero no inyectiva. Tiene una inversa por la derecha $g(t)=(t,0)$: $f\circ g=\operatorname{Id}_{\mathbb R}$, mientras que $g\circ f(x,y)=(x,0)\ne(x,y)$ en general.

**中文。** 能让每个输出找到至少一个原像，只保证满射；要唯一地倒回原对象还需要单射。反例中 $(0,1)$ 和 $(0,0)$ 输出相同，因此不可能存在双侧逆。

**Estado:** `Corregido en las notas`。已在 [3.4 同构与逆](../01_Algebra/Tema_03/04_Isomorfismos/01_Teoria_Demostraciones.md) 完整证明双射与双侧逆条件，保留原有手写更正的归属边界。

## AL-ERR-005 — Número de ecuaciones / 方程数必须独立

**Fuente:** [AL-AP-012](../00_Fuentes/Algebra_Lineal/AL-AP-012/Temas%201%20y%202%281%29%282%29.pdf), p. 21, proposition：$\dim W=\dim V-\{\text{número de ecuaciones implícitas de }W\}$。[AL-AP-004](../00_Fuentes/Algebra_Lineal/AL-AP-004/Tema%204_65298606b99b4fa875367ddfc0765632.pdf), p. 15 的后续说明已明确提到方程独立性。

**Análisis — Español.** Para $W=\{x\in\mathbb K^n:Ax=0\}$ la fórmula correcta es $\dim W=n-\operatorname{rg}(A)$, no $n$ menos el número de filas sin más. En $\mathbb R^2$, repetir dos veces $x=0$ deja la recta $\{(0,y)\}$, de dimensión $1$, no $0$.

**中文。** 重复或相互依赖的方程不产生新的约束。原件后续已给出正确限制；教材应在第一次表述时就写清“独立方程数”，并注明后续证明来源。

**Estado:** `Corregido en las notas`。[2.5 坐标与方程](../01_Algebra/Tema_02/01_Coordenadas_Ecuaciones/01_Teoria_Demostraciones.md) 使用秩而非方程总数，并配重复方程反例。

## AL-ERR-006 — Base de una suma directa / 直和中的环境空间

**Fuente:** [AL-AP-012](../00_Fuentes/Algebra_Lineal/AL-AP-012/Temas%201%20y%202%281%29%282%29.pdf), p. 29，步骤 1 在直和条件下写拼接两组基「es base de $V$」。手写批注补充其为 $V_1\oplus V_2$ 的基。

**Análisis — Español.** La unión de bases de dos subespacios con intersección cero es base de $V_1+V_2$. Solo será base de $V$ si además $V_1+V_2=V$. En $\mathbb R^3$, $V_1=\langle(1,0,0)\rangle$ y $V_2=\langle(0,1,0)\rangle$ tienen intersección cero, pero su suma no contiene $(0,0,1)$.

**中文。** “两子空间是直和”与“整个环境空间分解成它们的直和”是不同命题。反例满足直和条件但张不满环境空间，准确暴露了缺失假设。

**Estado:** `Corregido en las notas`。[2.6 直和与补空间](../01_Algebra/Tema_02/02_Suma_Directa_Complementarios/01_Teoria_Demostraciones.md) 将拼接基的环境明确为 $U+W$，只有和为 $V$ 时才是 $V$ 的基。

## AL-ERR-007 — Columnas del cambio de base / 换基矩阵取哪一组基

**Fuente:** [AL-AP-004](../00_Fuentes/Algebra_Lineal/AL-AP-004/Tema%204_65298606b99b4fa875367ddfc0765632.pdf), p. 10，第二条文字说第二组基 $B'$ 为标准基时，把「los vectores de $B'$」的标准坐标排入矩阵。

**Análisis — Español.** Con la convención de las páginas 8–11, $M_{B,B'}$ transforma coordenadas en $B$ en coordenadas en $B'$. Sus columnas son los vectores de **$B$** expresados en **$B'$**. Si $B'$ es canónica, se colocan los vectores de $B$, no de $B'$. Para $B=((1,1),(0,1))$, la matriz correcta es $\begin{pmatrix}1&0\\1&1\end{pmatrix}$, no $I_2$.

**中文。** 矩阵乘标准坐标列 $e_j$ 会取出第 $j$ 列；这必须是源基第 $j$ 个向量在目标基下的坐标。把目标基自身放进去通常只会得到单位矩阵，丢失换基信息。

**Estado:** `Corregido en las notas`。[3.6 换基](../01_Algebra/Tema_04/02_Cambio_Base_Semejanza/01_Teoria_Demostraciones.md) 沿用课堂方向，证明各列取源基在目标基下的坐标。

## AL-ERR-008 — Tipos y dimensiones en Rouché–Frobenius / 右端向量与维数排印

**Fuente:** [AL-AP-004](../00_Fuentes/Algebra_Lineal/AL-AP-004/Tema%204_65298606b99b4fa875367ddfc0765632.pdf), p. 20。原文把右端向量写成 $(b_1,\ldots,b_n)$，但同页方程有 $m$ 个右端分量；并印有

$$
\dim\langle v_1,\ldots,v_n\rangle=\langle v_1,\ldots,v_n,v\rangle.
$$

**Análisis — Español.** El término independiente pertenece a $\mathbb K^m$ y debe ser $v=(b_1,\ldots,b_m)^{\mathsf T}$. La igualdad debe comparar dos dimensiones:

$$
\dim\langle v_1,\ldots,v_n\rangle
=\dim\langle v_1,\ldots,v_n,v\rangle.
$$

La inclusión de subespacios, junto con dimensión finita, hace que esta igualdad equivalga a que $v$ pertenezca al subespacio generado por las columnas originales.

**中文。** 左边是整数、右边是子空间的等式存在对象类型错误。补上第二个 $\dim$ 后，才能通过有限维且包含的关系推导两个生成空间相同。右端向量长度也必须与系数矩阵行数一致。

**Estado:** 两处排印问题已确认；本批 Gauss 单元已用正确长度的右端和列关系解释，完整证明相容判别，原件保持不变。

## AL-ERR-009 — Pie de página de Tema 5 / 页脚编号

**Fuente:** [AL-AP-005](../00_Fuentes/Algebra_Lineal/AL-AP-005/Tema%205_83d0e9c7501214116f707ed90d6a34d8.pdf), p. 1，封面写「Tema 5: Espacio cociente」，页脚写「Tema 4」；后续页脚沿用。

**Análisis — Español.** Es una discrepancia editorial, no una refutación de las matemáticas del documento. Se identifica el archivo por su título, contenido e ID AL-AP-005.

**中文。** 不修改原件、不把商空间误归到矩阵表示；目录保留讲义 Tema 5，官方对应 2.9。

**Estado:** 已登记，目录映射已处理，原文件保持不变。


## AL-ERR-010 — Error aritmético en Gauss / 消元系数错误

**Fuente:** [AL-AP-000](../00_Fuentes/Algebra_Lineal/AL-AP-000/Tema%200%286%29.pdf), pp. 5 y 8, primer sistema manuscrito:

$$
3x+2y+z=1,\qquad2x-5y+2z=6,\qquad x-2y+z=7.
$$

Tras intercambiar la primera y tercera filas，la operación $F_3\leftarrow F_3-3F_1$ debe dar coeficiente de $z$ igual a $1-3\cdot1=-2$，pero el original escribe $-4$。La fila correcta es $(0,8,-2\mid-20)$，no $(0,8,-4\mid-20)$。

**Análisis — Español.** El error continúa hasta el vector final $(2,8,21)$。En el primer enunciado，ese vector produce $3\cdot2+2\cdot8+21=43\ne1$；las dos ecuaciones restantes sí se cumplen. Con la entrada corregida se obtiene $z=42$，$y=8$，$x=-19$，que satisface los tres enunciados.

**中文。** 原方法选择合法，错误发生在一个算术系数，并重复出现在第 8 页。只检查某个原方程或只检查主元数，都不能排除这个数值错误；必须逐条回代。没有证据将错误归属于某个具体作者。

**Estado:** `Corregido en las notas`。完整重算和三条回代见 [Gauss 例题 G-01](../01_Algebra/Tema_00/02_Sistemas_Gauss/04_Ejemplos.md)。原 PDF 原样保存，未擦除原错误。
