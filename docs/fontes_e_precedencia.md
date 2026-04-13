# fontes_e_precedencia.md — Fuentes del proyecto y orden de uso

## LISTA DE FUENTES DEL PROYECTO

Consultar activamente antes de ejecutar cualquier tarea.

### 1. `layout.tex`
**Tipo:** Fuente de verdad para estructura visual y tecnica
**Contenido:** Paleta de colores, tema Beamer, footline, bullets, comandos de imagen, estructura de portada y glosario
**Cuando usar:** Antes de escribir cualquier linea de LaTeX. Si hay conflicto entre una instruccion y `layout.tex`, `layout.tex` prevalece.

### 2. Planilla de planificacion
**Tipo:** Fuente principal de secuenciamiento del curso
**Nombre de archivo:** [COMPLETAR: nombre del archivo .xlsx]
**Contenido:** Clases con vision clase a clase, incluyendo laboratorios, evaluaciones continuas y parciales
**Cuando usar:** Antes de planificar cualquier clase para confirmar objetivo, posicion en la secuencia, clase anterior, clase siguiente y relacion con evaluaciones.

### 3. Plan de estudios oficial
**Tipo:** Programa oficial de la disciplina
**Nombre de archivo:** [COMPLETAR: nombre del PDF del plan de estudios]
**Contenido:** Objetivos de aprendizaje, contenidos por unidad y criterios de evaluacion
**Cuando usar:** Para alinear cada clase con los objetivos formales de la unidad.

### 4. Libro base
**Tipo:** Fuente de contenido tecnico
**Nombre de archivo:** [COMPLETAR: patron de nombres, ej. Libro_CAP*.pdf]
**Cuando usar:** Leer el capitulo relevante antes de planificar y antes de auditar. Es la autoridad para verificar fidelidad de contenido.

### 5. Clases anteriores ya producidas
**Tipo:** Referencia de consistencia terminologica y visual
**Ubicacion:** `2026-1/` (o el directorio de clases del semestre en curso)
**Cuando usar:** Antes de escribir una clase nueva, leer al menos la clase anterior para mantener coherencia de terminos, colores, estilos TikZ y nivel de profundidad.

---

## ORDEN DE PRECEDENCIA

Cuando hay conflicto entre fuentes:

1. `layout.tex` — prevalece en todo lo visual y tecnico LaTeX
2. Libro base — prevalece en todo lo de contenido tecnico
3. Plan de estudios — prevalece en objetivos y alcance
4. Planilla de planificacion — orienta el secuenciamiento
5. Clases anteriores — orientan consistencia, no son normativas

---

## ARCHIVOS DE REGLAS (en `docs/`)

| Archivo | Prioridad | Cuando usar |
|---------|-----------|-------------|
| `docs/regras_pedagogicas.md` | Alta | Siempre al crear o auditar contenido |
| `docs/regras_visuais.md` | Alta | Al trabajar con figuras, TikZ o composicion |
| `docs/regras_tecnicas_latex.md` | Alta | Al generar o compilar `.tex` |
| `docs/criterio_qualidade.md` | Referencia | En la auditoria final |
| `docs/fontes_e_precedencia.md` | Este archivo | Al inicio de cada sesion de trabajo |
