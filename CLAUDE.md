# CLAUDE.md — Archivo raiz del proyecto
# Leido automaticamente por Claude Code

## IDENTIDAD DEL PROYECTO

**Profesor:** [COMPLETAR: nombre completo]
**Disciplina:** [COMPLETAR: nombre de la materia]
**Universidad:** [COMPLETAR: universidad y sede]
**Carrera:** [COMPLETAR: nombre de la carrera]
**Semestre:** [COMPLETAR: numero de semestre — disciplina obligatoria/optativa]
**Carga horaria:** [COMPLETAR: ej. 4h/semana, 120h total, 8 creditos]
**Pre-requisito:** [COMPLETAR: materia anterior requerida]
**Publico:** Estudiantes de grado, nivel inicial/intermedio

**Idioma de entrega:** [COMPLETAR: espanol rioplatense / portugues / otro]
**Idioma de comunicacion con el profesor:** [COMPLETAR: portugues / espanol / otro]
**Tono de los slides:** Docente, claro, cercano, profesional, accesible sin perder precision tecnica

**Libro base:** [COMPLETAR: Autor, Titulo, edicion]
**Total de clases:** [COMPLETAR: ej. 30 clases presenciales de 2 horas]

---

## WORKFLOW POR CLASE (4 pasos obligatorios)

### PASO 1 — Investigacion y planificacion
1. Consultar `docs/memoria_projeto.md` para ver clase actual y decisiones acumuladas
2. Consultar `docs/fontes_e_precedencia.md` para identificar fuentes necesarias
3. Consultar la planilla de planificacion para confirmar capitulo y secciones del libro base
4. Leer el capitulo relevante del libro
5. Consultar clases anteriores ya producidas para mantener consistencia terminologica
6. Generar planificacion completa con `/aula-pesquisa N`
7. **Esperar aprobacion del profesor**

### PASO 2 — Escritura de los slides
1. Tras aprobacion del planificacion, releer todas las reglas:
   - `docs/regras_pedagogicas.md` (Reglas 1-8)
   - `docs/regras_visuais.md` (Reglas 8-16)
   - `docs/regras_tecnicas_latex.md` (Reglas T1-T9)
2. Releer `layout.tex` para seguir la estructura visual exacta
3. Escribir el `.tex` completo con `/aula-escrita N`
4. **NO compilar aun — esperar auditoria**

### PASO 3 — Auditoria (6 pasos obligatorios)
1. Ejecutar auditoria completa con `/aula-auditoria N`
2. Generar reporte con clasificacion: `[CRITICO]`, `[IMPORTANTE]`, `[MENOR]`
3. **NO corregir aun — esperar aprobacion del profesor**

### PASO 4 — Correccion y compilacion
1. Tras aprobacion del reporte, aplicar correcciones con `/aula-correcao N`
2. Verificar cero errores fatales, cero Overfull reales > 5pt
3. Ejecutar segunda auditoria automaticamente
4. Repetir hasta cero `[CRITICOS]`
5. Actualizar `docs/memoria_projeto.md` al concluir

---

## TABLA DE ARCHIVOS DE REGLAS

| Archivo | Cuando consultar |
|---------|-----------------|
| `docs/regras_pedagogicas.md` | Al crear o auditar contenido de slides |
| `docs/regras_visuais.md` | Al integrar figuras, TikZ o composicion visual |
| `docs/regras_tecnicas_latex.md` | Al generar o compilar archivos `.tex` |
| `docs/criterio_qualidade.md` | En la auditoria final de cada clase |
| `docs/fontes_e_precedencia.md` | Para saber que fuentes consultar en cada situacion |
| `docs/memoria_projeto.md` | Al inicio (consultar) y final (actualizar) de cada clase |

**Politica de wrappers:** `.claude/commands/` existe solo para exponer slash commands a Claude Code. La logica canonica del workflow queda en los archivos raiz (`aula-*.md`). Si una regla cambia, actualizar el archivo canonico; los wrappers no deben mantener copias largas y paralelas.

---

## REGLAS DE COMPORTAMIENTO CRITICAS

### 1. MERGE, NUNCA REPLACE
Cuando el profesor comparte un archivo editado, SIEMPRE hacer diff-and-merge linea por linea. Nunca sustituir el archivo entero sin verificar cambios manuales del profesor.

### 2. DEFINICION INLINE INNEGOCIABLE (Regla 1)
Todo termino tecnico debe ser definido EN EL MISMO SLIDE donde aparece por primera vez. No vale:
- Estar solo en el glosario
- Haber sido mencionado antes sin definicion
- Nota diciendo "veremos en el proximo slide"

Aplica a: labels de diagramas, titulos de columnas, preguntas de repaso, enunciados de actividad.

### 3. ANALOGIA ANTES DE ABSTRACCION (Regla 3)
Siempre introducir intuicion o analogia antes de la definicion tecnica. Nunca comenzar slide con definicion formal sin preparacion.

### 4. ENTREGABLE: ARCHIVO .TEX SOLAMENTE
El profesor compila localmente o via Overleaf. Claude nunca debe enviar PDF directamente, solo el archivo `.tex` completo.

### 5. FIGURAS: EXTRAER DEL MATERIAL, NUNCA PARSE DIRECTO
Para figuras del libro:
- Usar script Python con PIL + NumPy para crop automatico
- NUNCA usar coordenadas manuales
- Seguir nomenclatura: `figN-N_descripcion.png`

### 6. ANTI-RETRABAJO TECNICO
- En ajustes pequenos, reutilizar colores, macros, estilos y estructuras ya existentes
- Si algo nuevo es inevitable, definirlo antes del primer uso en el mismo patch
- Compilar inmediatamente tras cambios en preambulo, TikZ o macros

---

## CONOCIMIENTOS PREVIOS ASUMIDOS

[COMPLETAR: listar que conceptos el estudiante ya domina al llegar a esta materia]

Cualquier concepto fuera de esa lista **debe ser definido inline en la primera aparicion** (Regla 1).

---

## NOTAS CRITICAS

- **El libro base es autoridad:** la auditoria verifica omisiones, distorsiones y contradicciones con el libro
- **Progresion antes que profundidad:** Concepto → intuicion → ejemplo → ejercicio
- **Teoria vs Lab:** Teoria = cero comandos/terminal. Lab = cero concepto nuevo no visto en la teoria
- **Actividades:** Resolver en 15min maximo, usar solo contenido ya ensenado en esta clase
- **Compilacion:** usar `latexmk`; criterio: cero errores fatales, cero Overfull reales
- **Layout fijo:** Seguir `layout.tex` exactamente

---

**Este archivo es la puerta de entrada del proyecto. Para detalles de cada regla, consultar los archivos especificos listados en la tabla de arriba.**
