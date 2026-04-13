# claude-aulas-beamer

Sistema de produccion de slides academicos con Claude Code y LaTeX Beamer.

Disenado para profesores universitarios que preparan clases con slides en Beamer y quieren integrar Claude Code como asistente de produccion docente: planificacion, escritura, auditoria pedagogica, correccion y compilacion.

---

## Que incluye

```
claude-aulas-beamer/
├── CLAUDE.md                    # identidad del proyecto y reglas de comportamiento
├── aula-pesquisa.md             # flujo canonico: investigacion y planificacion
├── aula-escrita.md              # flujo canonico: escritura del .tex
├── aula-auditoria.md            # flujo canonico: auditoria pedagogica en 6 pasos
├── aula-correcao.md             # flujo canonico: correccion + compilacion
├── aula-cruzada.md              # auditoria cruzada entre dos clases consecutivas
├── layout.tex                   # template Beamer (tema Madrid, paleta personalizable)
├── .claude/
│   └── commands/                # slash commands que activan cada flujo
│       ├── aula-pesquisa.md
│       ├── aula-escrita.md
│       ├── aula-auditoria.md
│       ├── aula-correcao.md
│       └── aula-cruzada.md
├── docs/
│   ├── regras_pedagogicas.md    # reglas 1-8: contenido y didactica
│   ├── regras_visuais.md        # reglas 8-16: figuras, TikZ, composicion
│   ├── regras_tecnicas_latex.md # reglas T1-T9: LaTeX, compilacion, Overfull
│   ├── criterio_qualidade.md    # criterio de oro de la auditoria final
│   └── fontes_e_precedencia.md  # que fuentes consultar y en que orden
└── scripts/
    └── check_lesson_ready.py    # preflight mecanico antes de auditar
```

---

## Requisitos de software

- **Claude Code** (CLI de Anthropic): [claude.ai/code](https://claude.ai/code)
- **LaTeX** con `latexmk` (TeX Live 2023+ o MiKTeX)
- **Python 3.10+** para los scripts

---

## Archivos que debes preparar antes de empezar

El sistema **no incluye** estos archivos porque son especificos de cada materia o tienen restricciones de copyright. Debes crearlos o conseguirlos tu mismo antes de usar los slash commands.

### 1. Libro de texto en PDF (obligatorio)

El flujo de auditoria verifica fidelidad al libro base. Necesitas el PDF del libro de tu materia, dividido por capitulos o como un unico archivo. Coloca los PDFs en la raiz del proyecto con un nombre descriptivo:

```
Libro_Redes_CAP1.pdf
Libro_Redes_CAP2.pdf
...
```

Luego actualiza `docs/fontes_e_precedencia.md` con el patron de nombres exacto.

### 2. Planilla de planificacion del curso (obligatorio)

El sistema consulta una planilla `.xlsx` antes de cada clase para confirmar:
- Tema y tipo de clase (teoria / lab / evaluacion)
- Capitulo y secciones del libro base
- Relacion con clases anteriores y siguientes
- Evaluaciones y hitos del semestre

**Columnas minimas recomendadas:**

| Clase | Unidad | Tema | Tipo | Capitulo | Secciones | Observaciones |
|-------|--------|------|------|----------|-----------|---------------|
| 1 | 1 | Introduccion a redes | Teoria | Cap. 1 | 1.1, 1.2 | Primera clase |
| 2 | 1 | Topologias | Teoria | Cap. 1 | 1.3, 1.4 | |
| 3 | 1 | Lab: cables y conexion | Lab | — | — | Requiere equipos |

Guarda la planilla en la raiz del proyecto y registra su nombre en `docs/fontes_e_precedencia.md`.

### 3. Plan de estudios oficial (recomendado)

El PDF oficial de la materia con objetivos de aprendizaje por unidad. Coloca en la raiz y registra en `docs/fontes_e_precedencia.md`.

### 4. Archivo de memoria del proyecto (obligatorio, se crea una vez)

Crea `docs/memoria_projeto.md` copiando la plantilla incluida en `docs/memoria_projeto.template.md`. Este archivo registra el estado del proyecto entre sesiones: que clases ya se produjeron, decisiones de diseno acumuladas y terminologia estandarizada.

**No subas este archivo a git** (ya esta en `.gitignore`) — es personal de cada instancia del proyecto.

### 5. Clases anteriores ya producidas (cuando aplica)

Antes de escribir la Clase N, Claude consulta las clases anteriores para mantener coherencia terminologica y visual. Guarda los `.tex` producidos en `2026-1/` (o el directorio del semestre en curso):

```
2026-1/
├── Materia_Unidad_1_Clase_1_2026/
│   └── Materia_Unidad_1_Clase_1_2026.tex
├── Materia_Unidad_1_Clase_2_2026/
│   └── Materia_Unidad_1_Clase_2_2026.tex
...
```

Los `.tex` ya producidos **no** se suben a git por defecto (ver `.gitignore`). Si quieres compartirlos, ajusta el `.gitignore`.

---

## Como usar

### 1. Clonar o hacer fork de este repositorio

```bash
git clone https://github.com/rodrigofmiranda/aulas_beamer.git mi-materia
cd mi-materia
```

### 2. Preparar los archivos de tu materia

Sigue la seccion "Archivos que debes preparar antes de empezar" arriba.

### 3. Adaptar CLAUDE.md a tu materia

Abre `CLAUDE.md` y completa los campos marcados con `[COMPLETAR]`:

- Nombre de la materia, universidad, carrera
- Libro base
- Total de clases
- Idioma de entrega

### 4. Abrir la carpeta en Claude Code

```bash
claude  # desde la carpeta del proyecto
```

Claude Code lee `CLAUDE.md` automaticamente al iniciar.

### 5. Producir una clase

```
/aula-pesquisa 1     # investiga y planifica la Clase 1
/aula-escrita 1      # escribe el .tex completo
/aula-auditoria 1    # auditoria pedagogica en 6 pasos
/aula-correcao 1     # aplica correcciones y compila
```

Cada comando lee el flujo canonico del archivo `.md` correspondiente en la raiz.

---

## Filosofia del sistema

**Un solo lugar para cada regla.** Los slash commands en `.claude/commands/` son wrappers finos que apuntan a los archivos canonicos de la raiz (`aula-*.md`). Si quieres cambiar una regla, la cambias una sola vez en el archivo canonico.

**Flujo con aprobacion.** Cada etapa termina esperando la aprobacion del profesor antes de avanzar: el sistema no avanza solo de pesquisa a escrita, ni de auditoria a correccion.

**Sin teoria nueva en el lab.** La separacion teoria/lab es una regla de compilacion: Claude no pone comandos de terminal en clases teoricas ni introduce conceptos nuevos en laboratorios.

**Auditoria de 6 pasos.** Cada clase pasa obligatoriamente por: inventario de terminos, verificacion de actividades, profundidad de conceptos, progresion pedagogica, fidelidad al libro base y calidad visual.

---

## Adaptar el sistema a otra materia

Los unicos archivos que necesitan adaptacion son:

| Archivo | Que adaptar |
|---------|-------------|
| `CLAUDE.md` | Nombre de materia, libro, cantidad de clases, idioma |
| `docs/fontes_e_precedencia.md` | Nombres de los PDFs del libro y la planilla de planificacion |
| `layout.tex` | Colores, logo, shortauthor |

Los flujos (`aula-*.md`) y las reglas (`docs/regras_*.md`) son genericos y funcionan sin cambios para cualquier materia universitaria con slides Beamer.

---

## Licencia

MIT — libre para usar, adaptar y redistribuir con atribucion.
