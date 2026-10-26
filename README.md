# Grado en Matemáticas — UPM

中西双语数学学习知识库位于 [Matematicas-UPM](Matematicas-UPM/README.md)。

- [总目录 / Índice general](Matematicas-UPM/00_Indice_General.md)
- [材料接收与来源目录 / Fuentes](Matematicas-UPM/00_Fuentes/00_Catalogo_Fuentes.md)
- [课程覆盖情况 / Cobertura](Matematicas-UPM/99_Seguimiento/Cobertura_Temario.md)
- [下一步 / Pendientes](Matematicas-UPM/99_Seguimiento/Pendientes.md)

在 Obsidian 中选择「打开文件夹作为仓库」，打开本仓库中的 `Matematicas-UPM/`。正文采用 UTF-8 Markdown、相对路径链接及 MathJax 数学公式。

线性代数官方 **27 个小节的教材已写齐**，包括本次补齐的 23 小节。现有 124 份学习文件、95 个例题、186 道独立练习及解答，讲解同时使用西班牙语和中文。由[课程入口](Matematicas-UPM/01_Algebra/00_Indice.md)开始；[验证报告](Matematicas-UPM/99_Seguimiento/Validacion_23_Apartados.md)说明复核范围与仍待核对的课堂材料。

## 本地检查 / Verificación local

从仓库根目录运行 `python3 scripts/validar_biblioteca.py`（需 PyYAML），可检查 UTF-8、YAML、相对路径、基础公式分隔符、题解编号和原件哈希。运行 `python3 scripts/comprobar_calculos_algebra.py`（需 SymPy）可复现本次 132 项精确计算核对。两者均在本地执行，无网络调用；它们不替代数学证明审查或 Obsidian 显示验证。阅读 Markdown 教材不依赖这些脚本。
