# /aula-pesquisa
## Uso: `/aula-pesquisa N`
## Exemplo: `/aula-pesquisa 7`

---

Vamos construir a Aula **{{N}}**.

## PASSO 0A — USAR O MANIFESTO E O CORPUS QUANDO EXISTIREM

Antes de abrir PDF bruto, verificar se já existem:

- `admin/class_manifests/classes/class_{{N}}.json`
- `admin/book_corpus/modern_operating_systems_5e/book_index.json`

Se o manifesto existir, usá-lo como ponto de entrada canônico para:

- capítulo(s) relevantes
- seção(ões) relevantes
- PDF de capítulo correto
- caminhos do corpus textual já extraído

Se `textbook.book_corpus` estiver disponível no manifesto, consultar primeiro:

- `chapter_text_path` para leitura contínua do capítulo
- `requested_sections_found[].section_text_path` para leitura focada das seções da aula

Usar o PDF do Tanenbaum como verificação de fidelidade e fallback quando a extração textual estiver ambígua.

## PASSO 0B — PLANEJAR JÁ EM MODO IMPLEMENTAÇÃO

O objetivo da pesquisa não é produzir um plano bonito e genérico. O objetivo é sair desta etapa com a aula praticamente pronta para ser escrita sem redescobrir decisões.

Por isso, a pesquisa deve deixar explícito:

- quais figuras úteis do livro devem ser extraídas, com **número da figura + nome final do PNG**
- quais códigos do lab vão virar **arquivos-companheiros** (`.py`, `.sh`)
- qual ambiente do lab será usado por padrão (`shell.cloud.google.com` quando houver dependência de Linux)
- quais checagens mecânicas a escrita já deve sair atendendo para passar em `python scripts/check_lesson_ready.py --class {{N}}`

## PASSO 0 — IDENTIFICAR CAPÍTULO DO TANENBAUM

**ANTES DE QUALQUER OUTRA COISA**, consulte a planilha `[PLANILHA].xlsx`, folha "Resumen por clase", linha da Aula {{N}}, coluna **"Base en Tanenbaum"**.

Essa coluna indica qual(is) capítulo(s) e seção(ões) do Tanenbaum são relevantes para esta aula.

**Exemplo:**
- Aula 7 → "Cap. 2, Secciones: 2.4.1–2.4.9"
- Significa: Ler Capítulo 2, seções 2.4.1 até 2.4.9

**Localização do capítulo:**
- Capítulo 1: `[LIVRO]_CAP1.pdf`
- Capítulo 2: `[LIVRO]_CAP2.pdf`
- Capítulo 3: `[LIVRO]_CAP3.pdf`
- (e assim por diante)

## PASSO 1 — LER O TANENBAUM NA ÍNTEGRA

**Leia o(s) capítulo(s) identificado(s) acima na íntegra.**

**Não trabalhe de memória nem resuma sem ler.**

Ao terminar a leitura, responda explicitamente:
- **Quais seções do capítulo são relevantes para esta aula?**
- **Há conceitos importantes no capítulo que um principiante precisa entender e que normalmente são omitidos em resumos?**
- **O capítulo apresenta alguma distinção sutil que costuma ser simplificada demais e que vale preservar?**

**Só depois prossiga com os passos abaixo.**

---

## APÓS LER O TANENBAUM:

### 1. Consultar planilha de planejamento
Leia o arquivo `[PLANILHA].xlsx` e localize a **Aula {{N}}**, principalmente na folha **"Resumen por clase"**.

Confirme:
- **Tema** da aula
- **Tipo** (Clase teórica / Lab. Inf)
- **Unidade**
- **Aula anterior** (continuidade)
- **Próxima aula** (preparação)
- **Hito evaluativo** (se há EC, PE ou SE relacionado)

Se necessário, consulte também:
- Folha **"Cobertura general"** — verificar se o tema está bem distribuído ao longo do semestre
- Folha **"Evaluaciones y hitos"** — situar ECs, parciais, revisões e feedbacks

### 2. Consultar plan de estudios
Leia o arquivo `Plan de estudios - Sistemas operativos.pdf` e identifique o **objetivo de aprendizagem** desta unidade.

### 3. Consultar aulas anteriores
Leia as aulas já prontas no projeto para identificar:
- Quais **termos já foram definidos** (não precisam ser redefinidos, mas podem aparecer no repaso)
- **Tom e estilo visual** já estabelecidos
- **Decisões terminológicas** acumuladas (consultar também `/home/claude/memoria_projeto.md`, seção "Decisões terminológicas")

---

## COM BASE NESSA LEITURA, APRESENTE:

### A) OBJETIVO DE APRENDIZAGEM
Objetivo desta aula em **uma frase clara**.

Exemplo: "Ao final desta aula, o estudante será capaz de identificar os 5 estados de um processo e explicar as transições entre eles."

---

### B) O QUE O TANENBAUM DIZ (âncoras de fidelidade)
Liste os **3 a 5 pontos mais importantes** do capítulo para esta aula, com indicação de seção.

Isso serve como **âncora de fidelidade** — qualquer slide que contradiga ou omita esses pontos será um problema na auditoria.

Para cada ponto, indicar também:
- se ele é **conceito nuclear** (a ideia central sem a qual o estudante não entende a unidade)
- ou **mecanismo de apoio** (detalhe, implementação, dispositivo ou exemplo que sustenta a ideia central)

Regra de preparação:
- o plano já deve deixar claro **qual abstração precisa receber mais espaço didático**
- se um mecanismo de apoio puder ser reduzido a um exemplo curto sem perda pedagógica, ele **não deve virar o centro da aula**

Exemplo:
- `espacio de direcciones` / `memoria lógica` -> **conceito nuclear**
- `registro base` / `registro límite` -> **mecanismo de apoio inicial**

Exemplo:
1. **Sec. 2.1.3** — PCB contém ~10 campos: PID, estado, registros, prioridade, ponteiros de memória, etc.
2. **Sec. 2.1.4** — Modelo de 5 estados: Nuevo, Listo, Ejecutando, Bloqueado, Terminado
3. **Sec. 2.1.5** — Context switch tem custo (overhead): salvar/carregar registros, TLB flush

---

### C) LISTA DE TERMOS TÉCNICOS
Liste TODOS os termos técnicos que aparecerão, **em ordem de primeira aparição**.

Para cada termo indique:
- **Novo** (precisa de definição inline) ou **Já definido** (em qual aula anterior)
- **Slide aproximado** de primeira aparição
- se o termo é **conceito nuclear**, **mecanismo de apoio** ou **contraste relacional**
- se for contraste relacional, explicitar já aqui **"em relação a quê?"**

Formato de tabela:

| Termo | Status | Slide aprox. | Observação |
|-------|--------|--------------|------------|
| Proceso | Já definido (Aula 1) | Repaso | Retomar conceito |
| PCB | Novo | 4 | Definir inline: Process Control Block |
| PID | Novo | 4 | Definir inline: Process IDentifier |
| Context switch | Novo | 7 | Definir inline: cambio de contexto |

Para contrastes relacionais, não basta listar os nomes. O plano deve registrar o referente:
- `fragmentación interna` -> desperdício **dentro da partición asignada**
- `fragmentación externa` -> huecos livres **entre particiones/procesos**
- `memoria lógica` -> vista **do processo**
- `memoria física` -> RAM **real da máquina**

---

### D) DEPENDÊNCIAS PEDAGÓGICAS
Para cada **conceito novo**, liste quais **conceitos anteriores** são necessários para entendê-lo.

Confirme que **todos os pré-requisitos aparecem antes** na sequência desta aula.

Além das dependências, registrar:
- qual conceito é **núcleo da compreensão** desta parte da aula
- quais itens entram apenas como **mecanismo de apoio**
- quais pares exigem **contraste com referente explícito**

Teste obrigatório nesta etapa:
- a aula gasta mais energia explicando a abstração central ou o mecanismo que a implementa?
- o estudante saberá responder "interna a quê?", "externa a quê?", "lógica de quem?", "física de quê?" ao final da sequência?

Exemplo:
- **Context switch** depende de:
  - PCB (Slide 4)
  - Estados de processo (Slide 3)
  - Planificador (Slide 6)
  
→ OK, todos aparecem antes do context switch (Slide 7)

---

### E) ESTRUTURA DE SLIDES PROPOSTA

Para cada slide: **número, título, conteúdo principal em uma linha, tipo**.

Tipos: `[definição]`, `[exemplo]`, `[diagrama]`, `[atividade]`, `[síntese]`, `[glosário]`

Para slides de diagrama: indicar se usará **imagem do Tanenbaum** (com versão TikZ paralela) ou **só TikZ**.

Regras obrigatórias ao montar a sequência:
- o **conceito nuclear** deve aparecer antes e ocupar mais espaço didático do que o mecanismo de apoio
- mecanismos de apoio devem entrar como sustentação da intuição, não como desvio do foco principal
- todo **contraste relacional** deve ser planejado com texto e visual que respondam explicitamente "em relação a quê?"
- quando houver contraste como `interna/externa`, `lógica/física`, `local/global`, preferir mapas paralelos ou a mesma base visual com legenda comparável

Exemplo de estrutura:

```
1. Portada
2. Índice
3. Repaso — retomar conceitos de Aula anterior
4. [definición] Concepto de proceso — programa vs. proceso
5. [ejemplo] Ejemplos cotidianos — Word, Chrome, Spotify
6. [diagrama] Modelo de 5 estados — imagem Tanenbaum + TikZ
7. [definición] PCB — qué es, para qué sirve, qué contiene
8. [diagrama] Estructura del PCB — TikZ colorido por categoría
9. [definición] Context switch — qué es, cuándo ocurre
10. [ejemplo] Context switch en multiprogramación
11. [actividad] Transiciones de estados — enunciado
12. [actividad] Transiciones de estados — respuestas esperadas
13. [síntesis] Cierre y síntesis de la clase
14. [glosário] Glosario (I) — 5 termos
15. [glosário] Glosario (II) — 4 termos
```

---

### F) ATIVIDADES (se houver)
Esboço do enunciado, indicando **explicitamente qual modelo ou conceito** o estudante deve usar.

Estimar em **quanto tempo** deve ser resolúvel (máximo 15min).

Exemplo:
```
ATIVIDADE — Transiciones de estados

Enunciado:
"Usando el modelo de 5 estados (Nuevo, Listo, Ejecutando, 
Bloqueado, Terminado), describe las transiciones que ocurren 
cuando un proceso está Ejecutando y solicita leer un archivo 
del disco."

Modelo especificado: ✓ Modelo de 5 estados
Conhecimentos necessários:
  - Estados (Slide 6)
  - Transições (Slide 7)
  - Evento de E/S (Slide 8)
Tempo estimado: 10 minutos
```

---

### G) FIGURAS DO TANENBAUM (se houver)
Liste as figuras que devem ser extraídas do capítulo.

Para cada figura:
- **Número da figura** no Tanenbaum (ex: Fig. 2-2)
- **Descrição** do que mostra
- **Nome final do arquivo** na pasta da aula (ex: `fig2-2_estados_proceso.png`)
- **Decisão:** imagem + TikZ (slides duplos) ou só TikZ

Exemplo:
- **Fig. 2-2** — Modelo de 5 estados → `fig2-2_estados_proceso.png` → Imagem + TikZ (slides duplos)
- **Fig. 2-3** — Estrutura do PCB → `fig2-3_pcb_campos.png` → Só TikZ (reconstruir nas cores UTEC-SO)

---

### H) NOTAS OFF-SLIDE (se necessário)
Se algum slide depender de contexto oral do professor, deixar **nota em comentário LaTeX** para o professor saber como conduzir.

Exemplo:
```latex
% NOTA PARA O PROFESSOR: Antes de revelar o próximo slide,
% perguntar aos estudantes: "¿Qué creen que pasa cuando un
% proceso solicita E/S?" — Esperar respostas.
```

---

### I) PLANO OPERACIONAL DIRETO

Feche a pesquisa com um bloco curto e acionável:

```
PLANO OPERACIONAL

- Arquivo final esperado:
  2026-1/SO___Unidad_X_Clase_{{N}}___2026/SO___Unidad_X_Clase_{{N}}___2026.tex
- Figuras a extrair agora:
  - Fig. N-N -> figN-N_descricao.png
- Arquivos-companheiros a criar agora:
  - ejemplo_1.py
  - ejemplo_2.sh
- Ambiente do lab:
  - shell.cloud.google.com
- Checagens mecânicas que a escrita já deve sair passando:
  - sem `IfFileExists` para figura central
  - sem numeração de linhas
  - glossário em `\glosscard`
  - experimento com previsão/observação/explicação
```

---

## AGUARDAR APROVAÇÃO

Apresente **A até I** e **aguarde aprovação de Rodrigo** antes de escrever qualquer slide.

NÃO prossiga para a escrita sem aprovação explícita.

---

**Este comando prepara o terreno. Próxima etapa: `/aula-escrita {{N}}`**
