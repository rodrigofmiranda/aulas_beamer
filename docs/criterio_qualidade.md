# criterio_qualidade.md — Critério final + protocolo de auditoria

Este arquivo define o **critério de ouro** para avaliar a qualidade pedagógica de cada aula e o **protocolo de 6 passos** obrigatórios para auditoria completa.

---

## CRITÉRIO DE OURO — REGRA FINAL DE QUALIDADE

### Enunciado:
Um estudante que só leu esta aula, sem acesso a nenhum outro material e sem explicação oral do professor, deve conseguir:

1. **Entender cada termo técnico** quando o vê pela primeira vez
2. **Resolver cada atividade ou experimento** sem conhecimento externo
3. **Ler cada slide de resposta** sem precisar de explicação adicional
4. **Formar imagem mental clara** do conceito (visualizar o que acontece)

Se qualquer um desses quatro pontos falhar para qualquer elemento do slide, é um problema que deve ser corrigido antes de entregar.

Complemento obrigatório:
- a aula deve deixar claro qual é o **conceito nuclear** da unidade e quais itens entram apenas como **mecanismo de apoio**
- contrastes relacionais como `interna/externa`, `lógica/física`, `local/global` só estão claros quando o estudante consegue responder **"em relação a quê?"**

---

## OS 4 CRITÉRIOS EXPANDIDOS

### CRITÉRIO 1 — Termos autoexplicativos
**Teste:** Estudante encontra termo novo no slide. Ele entende o que significa?

**Como verificar:**
- Fazer inventário de todos os termos técnicos na ordem de primeira aparição
- Para cada termo, verificar: há definição inline no MESMO slide?
- Termos que violam: siglas sem expansão, labels de diagrama sem legenda, conceitos citados mas não explicados

**Exemplo de falha:**
```latex
% ❌ FALHA
El \textbf{PCB} almacena toda la información del proceso.
% Estudante não sabe o que é PCB
```

**Exemplo correto:**
```latex
% ✅ CORRETO
El \textbf{PCB (Process Control Block)} almacena toda la 
información del proceso: identificador, estado, registros, 
prioridad, etc.
% Estudante entende na primeira leitura
```

---

### CRITÉRIO 2 — Atividades e experimentos resolvíveis
**Teste:** Estudante lê o enunciado. Ele sabe como resolver usando apenas o que foi ensinado nesta aula e, se for lab, entende o que precisa prever, observar e explicar?

**Como verificar:**
- Para cada atividade, listar conceitos/modelos necessários para resolvê-la
- Verificar se TODOS foram ensinados ANTES da atividade
- Verificar se há exemplo concreto aplicando o conceito ANTES do exercício
- Em labs, verificar se existe previsão antes da execução
- Em labs, verificar se o que observar está explicitado
- Em labs, verificar se há pedido de explicação, comparação ou interpretação do resultado
- Em aulas teóricas, de revisão ou integração, verificar se há uma pequena bateria de `ejercicios para casa` quando isso fizer falta para consolidar o treino

**Exemplo de falha:**
```latex
% ❌ FALHA
\textbf{Ejercicio:} Aplique el algoritmo SRTN para los 
siguientes procesos...

% Aula só definiu SRTN, não mostrou exemplo
% Estudante não sabe como aplicar
```

**Exemplo correto:**
```latex
% Slide 1 — Definição + exemplo
\textbf{SRTN:} ... (definição) ...
\textbf{Ejemplo:} Dados os processos P1(t=5), P2(t=3), P3(t=8)...
(mostra passo a passo como aplicar SRTN)

% Slide 2 — Atividade
\textbf{Ejercicio:} Aplique el algoritmo SRTN para los 
siguientes procesos...

% ✅ Estudante pode resolver porque viu exemplo antes
```

**Exemplo de falha em lab:**
```latex
% ❌ FALHA
\textbf{Tarea:} Copiá el código, ejecutalo y subí una captura.

% Estudante não precisa pensar o conceito
% Só executa e entrega
```

**Exemplo de falha em aula teórica curta:**
```latex
% ❌ FALHA
% A aula termina sem atividade de fechamento nem exercícios para casa,
% mesmo precisando de mais prática para fixação.
```

---

### CRITÉRIO 3 — Respostas legíveis
**Teste:** Estudante lê slide de resposta esperada. Ele entende a solução usando apenas notação já ensinada?

**Como verificar:**
- Verificar se slide de resposta usa notação textual plana (não `\xrightarrow{}`)
- Verificar se cada passo da solução é explicado, não apenas apresentado
- Verificar se a resposta está completa (não "exercício para casa")

**Exemplo de falha:**
```latex
% ❌ FALHA
\textbf{Respuesta:}
Nuevo $\xrightarrow{\text{admitted}}$ Listo

% Estudante não entende notação matemática
% Resposta incompleta (falta explicar o que aconteceu)
```

**Exemplo correto:**
```latex
% ✅ CORRETO
\textbf{Respuesta:}
El proceso pasa de Nuevo --admitted--> Listo cuando el 
planificador lo acepta en memoria principal y está listo 
para ejecutar.

% Notação textual plana + explicação do que aconteceu
```

---

### CRITÉRIO 4 — Imagem mental clara
**Teste:** Estudante lê explicação de um conceito. Ele consegue visualizar mentalmente o que acontece?

**Como verificar:**
- Para processos/algoritmos: estudante consegue imaginar a sequência de passos?
- Para estruturas de dados: estudante consegue desenhar um esquema mental?
- Para estados/transições: estudante consegue visualizar o ciclo de vida?

**Exemplo de falha:**
```latex
% ❌ FALHA
\textbf{Context switch:} el SO guarda el estado del proceso 
saliente y carga el estado del proceso entrante.

% Definição correta, mas estudante não visualiza o QUE é 
% guardado, ONDE é guardado, QUANDO acontece
```

**Exemplo correto:**
```latex
% ✅ CORRETO
\textbf{Context switch:} cuando el SO necesita cambiar de 
proceso, ejecuta estos pasos:
\begin{enumerate}
  \item Guarda registros de CPU del proceso A en su PCB
  \item Carga registros del proceso B desde su PCB
  \item Actualiza punteros de memoria para el proceso B
  \item Reanuda ejecución del proceso B
\end{enumerate}

% Estudante visualiza: 4 passos, PCB como lugar de armazenamento,
% registros sendo salvos/carregados
```

### CRITÉRIO 5 — Foco na abstração certa
**Teste:** Ao final da aula, o estudante sai lembrando a ideia central da unidade ou apenas um mecanismo auxiliar?

**Como verificar:**
- identificar qual é o **conceito nuclear**
- identificar quais itens são apenas **mecanismos de apoio**
- verificar se a abstração central recebeu mais espaço, mais exemplos e mais clareza visual do que o mecanismo

**Exemplo de falha:**
```latex
% ❌ FALHA
% Aula sobre memoria lógica dedica vários slides a registros base/límite,
% mas quase não consolida a ideia de espacio de direcciones.
```

**Exemplo correto:**
```latex
% ✅ CORRETO
% Aula primeiro consolida a ideia de que cada processo "vê" seu próprio
% espaço de direções e só depois mostra base/límite como mecanismo inicial.
```

### CRITÉRIO 6 — Contrastes com referente explícito
**Teste:** Quando a aula usa um par relacional, o estudante sabe dizer "X em relação a quê?" sem adivinhar?

**Como verificar:**
- procurar pares como `interna/externa`, `lógica/física`, `usuario/kernel`
- confirmar que o texto nomeia explicitamente o referente
- confirmar que o visual usa base comparável, legenda comum ou contraste ancorado

**Exemplo de falha:**
```latex
% ❌ FALHA
\textbf{Fragmentación interna:} desperdicio de memoria.
\textbf{Fragmentación externa:} huecos libres.

% Falta dizer: dentro de quê? fora de quê?
```

**Exemplo correto:**
```latex
% ✅ CORRETO
\textbf{Fragmentación interna:} espacio desperdiciado dentro de una
partición ya asignada.
\textbf{Fragmentación externa:} huecos libres entre particiones ya
ocupadas por procesos.
```

---

## PROTOCOLO DE AUDITORIA — 6 PASSOS OBRIGATÓRIOS

Toda aula deve passar por estes 6 passos antes de ser considerada concluída.

**Gate mecânico antes da auditoria humana:** rodar `python scripts/check_lesson_ready.py --class N` para capturar placeholders, assets ausentes, sinais de código não copiável e glossário fora do padrão fixo. A auditoria humana continua obrigatória; o script só elimina retrabalho repetitivo.

---

### PASSO 1 — INVENTÁRIO DE TERMOS
**Objetivo:** Verificar se TODO termo técnico está definido inline na primeira aparição (Regra 1).

**Como fazer:**
1. Ler o arquivo `.tex` sequencialmente
2. Listar todos os termos técnicos na ordem de primeira aparição:
   - Conceitos (processo, PCB, planificador, quantum, etc.)
   - Siglas (SO, E/S, CPU, GUI, TLB, etc.)
   - Nomes de estados/algoritmos (Listo, FCFS, Round Robin, etc.)
   - Labels de diagramas, títulos de colunas, termos em atividades
3. Para cada termo, indicar:
   - Slide de primeira aparição
   - Slide de definição inline (deve ser o MESMO)
   - Se já foi definido em aula anterior (não precisa redefinir)

**Formato de saída:**
```
PASSO 1 — INVENTÁRIO DE TERMOS

Total de termos novos: N

| Termo | 1ª aparição | Definição | Status |
|-------|-------------|-----------|--------|
| Proceso | Slide 3 | Slide 3 | ✓ Definido inline |
| PCB | Slide 4 | — | ✗ NÃO definido |
| Planificador | Slide 5 | Slide 5 | ✓ Definido inline |
| Sistema Operativo | Slide 2 | (Aula 1) | ✓ Já definido antes |

PROBLEMAS ENCONTRADOS:
[CRÍTICO] Slide 4 — PCB usado sem definição inline
```

**Critério de falha:**
- Se termo novo aparece sem definição inline → `[CRÍTICO]`
- Se termo aparece em diagrama/tabela sem legenda → `[CRÍTICO]`

---

### PASSO 2 — VERIFICAÇÃO DE ATIVIDADES E EXPERIMENTOS
**Objetivo:** Verificar se atividades e experimentos são resolvíveis em 15min usando apenas conteúdo ensinado nesta aula e se, no lab, não viram execução mecânica (Regra 6).

**Como fazer:**
1. Localizar todos os slides de atividade (enunciado + resposta)
2. Para cada atividade:
   - Verificar se modelo/conceito está especificado no enunciado
   - Listar conhecimentos necessários para resolver
   - Verificar se TODOS foram ensinados ANTES da atividade
   - Verificar se há exemplo concreto ANTES do exercício
   - Verificar se slide de resposta usa notação textual plana
   - Se for lab, verificar previsão antes da execução
   - Se for lab, verificar o que observar
   - Se for lab, verificar pedido de explicação/comparação
   - Estimar tempo de resolução (deve ser ≤15min)

**Formato de saída:**
```
PASSO 2 — VERIFICAÇÃO DE ATIVIDADES E EXPERIMENTOS

Total de atividades: N

ATIVIDADE 1 — Slide X: "Transiciones de estados"
  Modelo especificado: ✓ "modelo de 5 estados"
  Conhecimentos necessários:
    - Estados (Nuevo, Listo, Ejecutando, Bloqueado, Terminado) → ✓ Slide 3
    - Transições → ✓ Slide 4
    - Exemplo concreto → ✗ NÃO há exemplo antes
  Notação de resposta: ✓ Textual plana
  Tempo estimado: 10min
  
  PROBLEMAS:
  [IMPORTANTE] Falta exemplo concreto antes da atividade

ATIVIDADE 2 — Slide Y: "Diagrama Gantt"
  Modelo especificado: ✗ "aplicar algoritmo" (qual algoritmo?)
  ...
  
  PROBLEMAS:
  [CRÍTICO] Modelo não especificado no enunciado

EXPERIMENTO 3 — Slide Z: "Mutex entre procesos"
  Previsão antes de executar: ✗ NÃO há
  Observação pedida: ✓ saída indicada
  Explicação/comparação: ✗ NÃO há

  PROBLEMAS:
  [EXPERIMENTO MECÂNICO] [CRÍTICO] O lab se resume a copiar e executar
```

**Critério de falha:**
- Se modelo não está especificado → `[IMPORTANTE]`
- Se falta exemplo antes da atividade → `[IMPORTANTE]`
- Se conhecimento necessário não foi ensinado → `[CRÍTICO]` (atividade irresolvível)
- Se resposta usa `\xrightarrow{}` → `[CRÍTICO]` (notação proibida)
- Se tempo >15min → `[IMPORTANTE]`
- Se lab não pede previsão/observação/explicação → `[EXPERIMENTO MECÂNICO]` `[CRÍTICO]`

---

### PASSO 3 — PROFUNDIDADE (4 perguntas)
**Objetivo:** Verificar se cada conceito novo responde: o que é / para que serve / como funciona / onde aparece (Regra 2).

**Como fazer:**
1. Listar todos os conceitos novos introduzidos na aula
2. Para cada conceito, verificar se o conjunto de slides responde as 4 perguntas:
   - **(a) O que é?** — Definição clara e acessível
   - **(b) Para que serve?** — Função, propósito, problema que resolve
   - **(c) Como funciona?** — Mecanismo básico
   - **(d) Onde aparece?** — Contexto de uso, exemplos cotidianos
3. Verificar se o conceito foi classificado corretamente como:
   - **conceito nuclear**
   - **mecanismo de apoio**
4. Verificar se o mecanismo não está ocupando mais espaço didático do que a abstração central

**Formato de saída:**
```
PASSO 3 — PROFUNDIDADE (4 perguntas)

Total de conceitos novos: N

CONCEITO: PCB (Process Control Block)
  (a) O que é? → ✓ Slide 4: "estructura de datos..."
  (b) Para que serve? → ✓ Slide 4: "almacenar información..."
  (c) Como funciona? → ✗ NÃO explicado
  (d) Onde aparece? → ✓ Slide 5: "cada proceso tiene su PCB..."
  
  PROBLEMAS:
  [IMPORTANTE] Falta explicar COMO funciona (quais campos, como SO usa)

CONCEITO: Context switch
  (a) O que é? → ✓ Slide 7
  (b) Para que serve? → ✓ Slide 7
  (c) Como funciona? → ✓ Slide 8 (4 passos)
  (d) Onde aparece? → ✓ Slide 9 (multiprogramação)
  
  OK — 4 perguntas respondidas
```

**Critério de falha:**
- Se falta resposta para 2+ perguntas → `[IMPORTANTE]`
- Se conceito é usado em atividade mas profundidade insuficiente → `[CRÍTICO]`
- Se mecanismo de apoio eclipsa a abstração central → `[PRIORIZAÇÃO DIDÁTICA]` `[IMPORTANTE]`

---

### PASSO 4 — PROGRESSÃO PEDAGÓGICA
**Objetivo:** Verificar se sequência de slides segue progressão lógica: intuição antes de abstração, exemplo antes de exercício (Regra 3).

**Como fazer:**
1. Ler slides sequencialmente
2. Para cada slide de conteúdo novo, verificar:
   - Há preparação (pergunta, situação cotidiana, conexão com prévio)?
   - Definição vem depois da preparação (não antes)?
   - Há exemplo concreto ilustrando o conceito?
   - Exemplo vem antes de atividade (não depois)?
   - Há frase-puente conectando com slide anterior (se necessário)?
   - Se houver contraste relacional, o texto responde explicitamente "em relação a quê"?
   - O visual compara sobre a mesma base ou com referente comum?

**Formato de saída:**
```
PASSO 4 — PROGRESSÃO PEDAGÓGICA

SLIDE 3: "Concepto de proceso"
  Preparação: ✓ "¿Qué pasa cuando abrís una aplicación?"
  Definição após preparação: ✓
  Exemplo concreto: ✓ "Word, Chrome, Spotify ejecutándose"
  OK

SLIDE 5: "Cambio de contexto"
  Preparação: ✗ Começa direto com definição
  Definição após preparação: ✗
  Exemplo concreto: ✓
  
  PROBLEMAS:
  [PROGRESSÃO QUEBRADA] [CRÍTICO] Definição sem preparação

SLIDE 10: "Actividad: estados"
SLIDE 11: "Ejemplo: transiciones"
  
  PROBLEMAS:
  [PROGRESSÃO QUEBRADA] [CRÍTICO] Exemplo DEPOIS da atividade
```

**Critério de falha:**
- Se definição sem preparação → `[CRÍTICO]` (progressão quebrada)
- Se exemplo depois de atividade → `[CRÍTICO]` (progressão quebrada)
- Se conexão entre slides não é clara → `[IMPORTANTE]` (slide sem coesão)
- Se contraste relacional fica implícito ou ambíguo → `[CONTRASTE OPACO]` `[IMPORTANTE]`

---

### PASSO 5 — FIDELIDADE AO TANENBAUM
**Objetivo:** Verificar se conteúdo está alinhado com o livro base: sem omissões críticas, sem distorções, sem contradições.

**Pré-requisito:** Ter lido o capítulo relevante do Tanenbaum ANTES da auditoria.

**Como fazer:**
1. Reler pontos essenciais identificados no planejamento (Prompt 1, item B)
2. Verificar se TODOS os pontos essenciais aparecem nos slides
3. Verificar se há simplificações excessivas que distorcem o conceito
4. Verificar se há afirmações que contradizem o livro

**Formato de saída:**
```
PASSO 5 — FIDELIDADE AO TANENBAUM

PONTOS ESSENCIAIS (do planejamento):
1. Processo tem 5 estados: Nuevo, Listo, Ejecutando, Bloqueado, Terminado
   → ✓ Presente: Slide 3
2. Transições entre estados são provocadas por eventos específicos
   → ✓ Presente: Slide 4
3. PCB contém informação para gerenciar processo
   → ✓ Presente: Slide 5
4. Context switch tem custo (overhead)
   → ✗ OMITIDO: não mencionado

VERIFICAÇÃO DE DISTORÇÕES:
Slide 6: "El PCB solo tiene el PID y el estado"
  → ✗ DISTORÇÃO: Tanenbaum (Sec. 2.1.3) lista ~10 campos, não só 2

PROBLEMAS:
[OMISSÃO TANENBAUM] [CRÍTICO] Overhead de context switch não mencionado
[DISTORÇÃO TANENBAUM] [CRÍTICO] Slide 6 simplifica PCB demais
```

**Critério de falha:**
- Se omissão de ponto essencial → `[OMISSÃO TANENBAUM]` `[CRÍTICO]`
- Se distorção que confunde → `[DISTORÇÃO TANENBAUM]` `[CRÍTICO]`
- Se contradição direta → `[DISTORÇÃO TANENBAUM]` `[CRÍTICO]`

---

### PASSO 6 — QUALIDADE PEDAGÓGICA GERAL E COPIABILIDADE DE CÓDIGO
**Objetivo:** Verificar aspectos gerais: autoexplicatividade, coesão, separação teoria/lab, composição visual e copiabilidade de código.

**Como fazer:**
1. **Autoexplicatividade:** Simular leitura de cada slide sem fala do professor. Faz sentido?
2. **Coesão:** Cada slide tem ideia central clara? Ou é lista de fatos soltos?
3. **Separação teoria/lab:** Aula teórica tem comandos? Lab tem conceito novo?
4. **Composição visual:** Algum elemento cortado, ilegível, desequilibrado?
5. **Micro-composição TikZ:** Flechas atravessam texto? Labels sobrepostos?
6. **Código copiável:** Há numeração de linhas, mojibake, quebra ruim ou layout que dificulta copiar do PDF?

**Formato de saída:**
```
PASSO 6 — QUALIDADE PEDAGÓGICA GERAL E COPIABILIDADE DE CÓDIGO

AUTOEXPLICATIVIDADE:
Slide 4: Lista de campos do PCB sem explicar para que serve cada um
  → [SLIDE SEM COESÃO] [IMPORTANTE]

SEPARAÇÃO TEORIA/LAB:
Slide 10: Comando "ps aux" em aula teórica
  → [SEPARAÇÃO] [CRÍTICO] Aula teórica não pode ter comandos

COMPOSIÇÃO VISUAL:
Slide 7: Diagrama TikZ com label "solicita leitura de disco 
  y queda esperando hasta terminar" cortado à direita
  → [COMPOSIÇÃO VISUAL] [CRÍTICO] Label muito longo, sai da área

MICRO-COMPOSIÇÃO TIKZ:
Slide 8: Flecha de "Bloqueado" para "Listo" atravessa texto 
  do nodo "Ejecutando"
  → [MICROCOMPOSIÇÃO] [IMPORTANTE] Reposicionar flecha

CÓDIGO COPIÁVEL:
Slide 12: bloco Python com numeração de linhas
  → [CÓDIGO NÃO COPIÁVEL] [CRÍTICO] Números entram junto ao copiar

Slide 13: comando quebrado de forma ruim no PDF
  → [CÓDIGO NÃO COPIÁVEL] [IMPORTANTE] Colagem no terminal fica insegura
```

**Critério de falha:**
- Se slide depende de fala oral → `[IMPORTANTE]`
- Se slide é lista de fatos sem coesão → `[SLIDE SEM COESÃO]` `[IMPORTANTE]`
- Se aula teórica tem comandos → `[SEPARAÇÃO]` `[CRÍTICO]`
- Se lab introduz conceito novo → `[SEPARAÇÃO]` `[CRÍTICO]`
- Se elemento cortado/ilegível → `[COMPOSIÇÃO VISUAL]` `[CRÍTICO]`
- Se TikZ mal resolvido → `[MICROCOMPOSIÇÃO]` `[IMPORTANTE]`
- Se código tem numeração/mojibake → `[CÓDIGO NÃO COPIÁVEL]` `[CRÍTICO]`
- Se quebra de linha atrapalha copiar/colar → `[CÓDIGO NÃO COPIÁVEL]` `[IMPORTANTE]`

---

## TAGS DE CLASSIFICAÇÃO DE PROBLEMAS

Toda auditoria deve usar estas tags para classificar problemas:

| Tag | Significado | Quando usar |
|-----|-------------|-------------|
| `[CRÍTICO]` | Impede estudante de completar a aula | Termo não definido, atividade irresolvível, progressão quebrada, omissão/distorção Tanenbaum, erro LaTeX fatal |
| `[IMPORTANTE]` | Compromete qualidade pedagógica | Profundidade insuficiente, exemplo ausente, slide sem coesão, composição visual problemática |
| `[MENOR]` | Melhoria desejável mas não urgente | Oportunidade de contexto LIDIA perdida, margem excessiva em figura |
| `[OMISSÃO TANENBAUM]` | Ponto essencial do livro não aparece | Conceito central omitido |
| `[DISTORÇÃO TANENBAUM]` | Simplificação excessiva ou contradição | Conceito simplificado de forma que confunde |
| `[FIGURA DO LIVRO AUSENTE]` | Figura útil do livro ficou só como placeholder | Slide final com `IfFileExists`, alerta de imagem ausente ou asset não extraído |
| `[PROGRESSÃO QUEBRADA]` | Sequência pedagógica violada | Definição sem preparo, exemplo após exercício |
| `[ANALOGIA PROBLEMÁTICA]` | Analogia imprecisa ou que introduz ideia errada | Comparação que confunde mais do que esclarece |
| `[SLIDE SEM COESÃO]` | Lista de fatos sem ideia central | Slide sobrecarregado ou sem foco |
| `[COMPOSIÇÃO VISUAL]` | Slide compila mas fica cortado/ilegível | Elemento fora da área visível, figura ilegível |
| `[MICROCOMPOSIÇÃO]` | Detalhes finos de TikZ mal resolvidos | Flechas atravessam texto, labels sobrepostos |
| `[TÉCNICO LATEX]` | Erro de compilação ou warning grave | enumerate, colorbox+parbox, \\ em node, babel, Overfull |
| `[SEPARAÇÃO]` | Violação teoria vs lab | Teoria com comandos, lab com conceito novo |
| `[ATIVIDADE IRRESOLVÍVEL]` | Exercício exige conhecimento não ensinado | Conceito usado mas não explicado antes |
| `[EXPERIMENTO MECÂNICO]` | Lab virou execução sem interpretação | Copiar/executar/entregar sem prever e explicar |
| `[CÓDIGO NÃO COPIÁVEL]` | Código ruim para copiar do PDF | Numeração, mojibake, wrapping nocivo |
| `[PRIORIZAÇÃO DIDÁTICA]` | Mecanismo de apoio tomou o lugar do conceito nuclear | A aula detalha o meio e não consolida a ideia central |
| `[CONTRASTE OPACO]` | Contraste relacional sem referente explícito | `interna/externa`, `lógica/física` etc. sem dizer "em relação a quê" |
| `[CONSISTÊNCIA]` | (Auditoria cruzada) Terminologia inconsistente | Termo definido diferente em duas aulas |
| `[CONTINUIDADE]` | (Auditoria cruzada) Conexão entre aulas quebrada | Síntese não anuncia próxima aula, repaso não retoma |
| `[GLOSSÁRIO]` | Glossário mal agrupado, subocupado, desequilibrado ou com cara de apostila | Página quase vazia, bloco sem lógica pedagógica, colunas desbalanceadas, lista crua |

---

## RESUMO FINAL OBRIGATÓRIO

Ao final da auditoria, apresentar resumo consolidado:

```
┌─────────────────────────────────────────────┐
│ RELATÓRIO DE AUDITORIA — Aula N             │
│                                             │
│ TOTAL DE PROBLEMAS: N                       │
│                                             │
│ [CRÍTICOS] (impedem completar a aula): N    │
│   — Slide X: Termo Y não definido           │
│   — Slide Z: Exemplo após atividade         │
│                                             │
│ [IMPORTANTES] (comprometem a qualidade): N  │
│   — Slide A: Profundidade insuficiente      │
│   — Slide B: Composição visual cortada      │
│                                             │
│ [MENORES] (melhorias desejáveis): N         │
│   — Slide C: Oportunidade LIDIA perdida     │
│                                             │
└─────────────────────────────────────────────┘

STATUS: AGUARDANDO APROVAÇÃO PARA CORREÇÃO
```

**NÃO corrigir nada antes de apresentar o relatório e aguardar aprovação de Rodrigo.**

---

## CRITÉRIO DE COMPLETUDE

A aula está concluída quando:
1. ✅ Auditoria retorna **zero `[CRÍTICOS]`** em todos os 6 passos
2. ✅ Compilação retorna **zero erros fatais, zero Overfull reais > 5pt**
3. ✅ Rodrigo aprovou o resultado final

Até que esses 3 critérios sejam atendidos, a aula **não está pronta**.

---

**Este arquivo é a garantia de qualidade do projeto. Nenhuma aula é entregue sem passar por estes 6 passos.**
