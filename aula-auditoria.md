# /aula-auditoria
## Uso: `/aula-auditoria N`
## Exemplo: `/aula-auditoria 7`

---

Execute auditoria completa da Aula **{{N}}**.

Localização do arquivo: `SO___Unidad_*_Clase_{{N}}___2026.tex`

---

## PRÉ-REQUISITO: IDENTIFICAR E RELER O TANENBAUM

**Antes de auditar:**

1. **Consulte a planilha** `[PLANILHA].xlsx`, folha "Resumen por clase", linha da Aula {{N}}, coluna **"Base en Tanenbaum"** para identificar qual capítulo e seções são relevantes.

2. **Releia o capítulo identificado** do Tanenbaum para verificar fidelidade.

**Localização dos capítulos:**
- Cap 1: `[LIVRO]_CAP1.pdf`
- Cap 2: `[LIVRO]_CAP2.pdf`
- Cap 3: `[LIVRO]_CAP3.pdf`
- (e assim por diante)

3. **Consulte especialmente os pontos essenciais** identificados no planejamento (Prompt 1, item B).

---

## PASSO 0 — PREFLIGHT MECÂNICO OBRIGATÓRIO

Antes de entrar nos 6 passos, rode:

```bash
python scripts/check_lesson_ready.py --class {{N}}
```

Use esse resultado para acelerar a parte repetitiva da auditoria:
- placeholders de figura que sobreviveram
- assets ausentes
- glossário fora do padrão novo
- código com numeração ou sinais de baixa copiabilidade

**Importante:** o preflight não substitui a auditoria pedagógica. Ele apenas limpa o terreno para que os 6 passos foquem no que exige julgamento docente.

---

## PROTOCOLO DE 6 PASSOS OBRIGATÓRIOS

Execute os 6 passos na ordem. **NÃO pule nenhum passo.**

---

### PASSO 1 — INVENTÁRIO DE TERMOS

**Objetivo:** Verificar se TODO termo técnico está definido inline na primeira aparição (Regra 1).

**Como fazer:**
1. Ler o arquivo `.tex` sequencialmente
2. Listar todos os termos técnicos na ordem de primeira aparição, **varrendo também títulos de seção (`\section{}`) e títulos de slides (`\begin{frame}{...}`) como fontes de termos novos** — um termo no título de seção aparece antes do corpo de qualquer slide dessa seção:
   - Títulos de seção e de slide
   - Conceitos (proceso, PCB, planificador, quantum, etc.)
   - Siglas (SO, E/S, CPU, GUI, TLB, etc.)
   - Nomes de estados/algoritmos (Listo, FCFS, Round Robin, etc.)
   - Labels de diagramas, títulos de colunas, termos em atividades
3. Para cada termo, indicar:
   - Slide de primeira aparição
   - Slide de definição inline (deve ser o MESMO)
   - Se já foi definido em aula anterior (não precisa redefinir)

**Formato de saída:**
```
═══════════════════════════════════════════════════════════
PASSO 1 — INVENTÁRIO DE TERMOS
═══════════════════════════════════════════════════════════

Total de termos novos: N

| Termo | 1ª aparição | Definição | Status |
|-------|-------------|-----------|--------|
| Proceso | Slide 3 | Slide 3 | ✓ Definido inline |
| PCB | Slide 4 | — | ✗ NÃO definido |
| Planificador | Slide 5 | Slide 5 | ✓ Definido inline |
| Sistema Operativo | Slide 2 | (Aula 1) | ✓ Já definido antes |

PROBLEMAS ENCONTRADOS:
[CRÍTICO] Slide 4 — PCB usado sem definição inline. 
  → Solução: Adicionar definição: "PCB (Process Control Block): 
     estructura que contiene información del proceso..."
```

**Critério de falha:**
- Termo novo sem definição inline → `[CRÍTICO]`
- Termo em diagrama/tabela sem legenda → `[CRÍTICO]`

---

### PASSO 2 — VERIFICAÇÃO DE ATIVIDADES E EXPERIMENTOS

**Objetivo:** Verificar se atividades e experimentos são resolvíveis em 15min usando apenas conteúdo ensinado e se, no lab, exigem interpretação em vez de mera execução (Regra 6).

**Como fazer:**
1. Localizar todos os slides de atividade
2. Para cada atividade:
   - Verificar se modelo/conceito está especificado no enunciado
   - Listar conhecimentos necessários para resolver
   - Verificar se TODOS foram ensinados ANTES
   - Verificar se há exemplo concreto ANTES do exercício
   - Verificar se slide de resposta usa notação textual plana
   - Se for lab, verificar se há previsão antes da execução
   - Se for lab, verificar se o slide diz claramente o que observar
   - Se for lab, verificar se o estudante precisa explicar, comparar ou interpretar o resultado
   - Se a aula for teórica, de revisão ou integração, verificar se há `Ejercicios para casa` quando fizer sentido pedagógico
   - Estimar tempo de resolução (≤15min)

**Formato de saída:**
```
═══════════════════════════════════════════════════════════
PASSO 2 — VERIFICAÇÃO DE ATIVIDADES E EXPERIMENTOS
═══════════════════════════════════════════════════════════

Total de atividades: N

ATIVIDADE 1 — Slide X: "Transiciones de estados"
  Modelo especificado: ✓ "modelo de 5 estados"
  Conhecimentos necessários:
    - Estados (Nuevo, Listo, Ejecutando, Bloqueado, Terminado) 
      → ✓ Slide 3
    - Transições → ✓ Slide 4
    - Exemplo concreto → ✗ NÃO há exemplo antes
  Notação de resposta: ✓ Textual plana
  Tempo estimado: 10min
  
  PROBLEMAS:
  [IMPORTANTE] Falta exemplo concreto antes da atividade.
    → Solução: Adicionar Slide 9.5 com exemplo de transições
       antes da atividade no Slide 10.

EXPERIMENTO 2 — Slide Y: "Señales entre procesos"
  Previsão antes de executar: ✗ NÃO há
  O que observar: ✓ saída esperada indicada
  Interpretação após executar: ✗ NÃO há
  Tempo estimado: 8min

  PROBLEMAS:
  [EXPERIMENTO MECÂNICO] [CRÍTICO] O estudante só copia e executa.
    → Solução: pedir previsão do comportamento antes de rodar e
       uma explicação curta comparando o observado com a previsão.

CIERRE — Ejercicios para casa
  Presente: ✗ não há
  Tipo de aula: teórica/de integração

  PROBLEMAS:
  [IMPORTANTE] Faltam `Ejercicios para casa` para prolongar o treino.
    → Solução: adicionar 2 a 4 consignas curtas com conteúdo já ensinado.
```

**Critério de falha:**
- Modelo não especificado → `[IMPORTANTE]`
- Falta exemplo antes → `[IMPORTANTE]`
- Conhecimento não ensinado → `[CRÍTICO]` (atividade irresolvível)
- Usa `\xrightarrow{}` → `[CRÍTICO]` (notação proibida)
- Tempo >15min → `[IMPORTANTE]`
- Lab sem previsão/observação/explicação → `[EXPERIMENTO MECÂNICO]` `[CRÍTICO]`
- Consigna centrada em "copie, execute e entregue" → `[EXPERIMENTO MECÂNICO]` `[CRÍTICO]`
- Aula de revisão/integração sem treino extra quando necessário → `[IMPORTANTE]`

---

### PASSO 3 — PROFUNDIDADE (4 perguntas)

**Objetivo:** Verificar se cada conceito novo responde: o que é / para que serve / como funciona / onde aparece (Regra 2).

**Como fazer:**
1. Listar todos os conceitos novos
2. Para cada conceito, verificar as 4 perguntas:
   - **(a) O que é?**
   - **(b) Para que serve?**
   - **(c) Como funciona?**
   - **(d) Onde aparece?**
3. Verificar se a aula distingue corretamente:
   - **conceito nuclear** = abstração central da unidade
   - **mecanismo de apoio** = detalhe que sustenta a abstração
4. Verificar se a distribuição de espaço didático está coerente:
   - a abstração central recebeu mais clareza, exemplos e tempo?
   - o mecanismo foi mantido no tamanho necessário, sem sequestrar a aula?

**Formato de saída:**
```
═══════════════════════════════════════════════════════════
PASSO 3 — PROFUNDIDADE (4 perguntas)
═══════════════════════════════════════════════════════════

Total de conceitos novos: N

CONCEITO: PCB (Process Control Block)
  (a) O que é? → ✓ Slide 4: "estructura de datos..."
  (b) Para que serve? → ✓ Slide 4: "almacenar información..."
  (c) Como funciona? → ✗ NÃO explicado
  (d) Onde aparece? → ✓ Slide 5: "cada proceso tiene su PCB..."
  
  PROBLEMAS:
  [IMPORTANTE] Falta explicar COMO funciona.
    → Solução: Adicionar slide explicando estrutura interna do PCB
       (campos principais: PID, estado, registros, etc.)

PRIORIZAÇÃO DIDÁTICA:
  Conceito nuclear: "espacio de direcciones"
  Mecanismo de apoio: "registro base / registro límite"
  Espaço didático relativo: ✗ mecanismo recebeu mais desenvolvimento do que a abstração

  PROBLEMAS:
  [PRIORIZAÇÃO DIDÁTICA] [IMPORTANTE] A aula detalha demais o mecanismo
    antes de consolidar a abstração central.
    → Solução: expandir a intuição e os exemplos da abstração; compactar o
       mecanismo de apoio ao mínimo necessário.
```

**Critério de falha:**
- Falta 2+ perguntas → `[IMPORTANTE]`
- Conceito usado em atividade mas profundidade insuficiente → `[CRÍTICO]`
- Mecanismo de apoio recebe mais peso que a abstração que sustenta → `[PRIORIZAÇÃO DIDÁTICA]` `[IMPORTANTE]`

---

### PASSO 4 — PROGRESSÃO PEDAGÓGICA

**Objetivo:** Verificar se sequência segue: intuição antes de abstração, exemplo antes de exercício (Regra 3).

**Como fazer:**
1. Ler slides sequencialmente
2. Para cada slide de conteúdo novo:
   - Há preparação (pergunta, situação, conexão)?
   - Definição vem depois da preparação?
   - Há exemplo concreto?
   - Exemplo vem antes de atividade?
   - Há frase-puente conectando com slide anterior?
   - Se houver contraste relacional, o slide diz explicitamente **em relação a quê**?
   - O visual usa base comparável, legenda comum ou contraste suficientemente ancorado?

**Formato de saída:**
```
═══════════════════════════════════════════════════════════
PASSO 4 — PROGRESSÃO PEDAGÓGICA
═══════════════════════════════════════════════════════════

SLIDE 3: "Concepto de proceso"
  Preparação: ✓ "¿Qué pasa cuando abrís una aplicación?"
  Definição após preparação: ✓
  Exemplo concreto: ✓ "Word, Chrome, Spotify"
  OK

SLIDE 5: "Cambio de contexto"
  Preparação: ✗ Começa direto com definição
  Definição após preparação: ✗
  
  PROBLEMAS:
  [PROGRESSÃO QUEBRADA] [CRÍTICO] Definição sem preparação.
    → Solução: Adicionar preparação: "¿Cómo el SO cambia de 
       proceso? ¿Qué información debe guardar?"

SLIDE 10: "Actividad: estados"
SLIDE 11: "Ejemplo: transiciones"
  
  PROBLEMAS:
  [PROGRESSÃO QUEBRADA] [CRÍTICO] Exemplo DEPOIS da atividade.
    → Solução: Inverter ordem — Slide 10 = Exemplo, 
       Slide 11 = Atividade

SLIDES 14-15: "Fragmentación interna" / "Fragmentación externa"
  Referente explícito: ✗ não diz interna a quê / externa a quê
  Base visual comparável: ✗ desenhos não deixam claro o referente comum

  PROBLEMAS:
  [CONTRASTE OPACO] [IMPORTANTE] O contraste aparece sem referente explícito.
    → Solução: nomear o referente no texto e comparar sobre o mesmo mapa
       de particiones ou em diagramas paralelos com legenda comum.
```

**Critério de falha:**
- Definição sem preparação → `[PROGRESSÃO QUEBRADA]` `[CRÍTICO]`
- Exemplo depois de atividade → `[PROGRESSÃO QUEBRADA]` `[CRÍTICO]`
- Conexão não clara → `[SLIDE SEM COESÃO]` `[IMPORTANTE]`
- Contraste relacional sem referente explícito ou sem base visual comparável → `[CONTRASTE OPACO]` `[IMPORTANTE]`

---

### PASSO 5 — FIDELIDADE AO TANENBAUM

**Objetivo:** Verificar alinhamento com o livro: sem omissões críticas, sem distorções, sem contradições.

**Como fazer:**
1. Reler pontos essenciais (Prompt 1, item B)
2. Verificar se TODOS aparecem nos slides
3. Verificar simplificações excessivas
4. Verificar contradições
5. Verificar se figuras do Tanenbaum claramente úteis e utilizáveis foram extraídas para a pasta da aula e incluídas no material final, em vez de deixadas como placeholder

**Formato de saída:**
```
═══════════════════════════════════════════════════════════
PASSO 5 — FIDELIDADE AO TANENBAUM
═══════════════════════════════════════════════════════════

PONTOS ESSENCIAIS (do planejamento):
1. Processo tem 5 estados → ✓ Presente: Slide 3
2. Transições provocadas por eventos → ✓ Presente: Slide 4
3. PCB contém ~10 campos → ✓ Presente: Slide 5
4. Context switch tem custo (overhead) → ✗ OMITIDO

VERIFICAÇÃO DE DISTORÇÕES:
Slide 6: "El PCB solo tiene el PID y el estado"
  → ✗ DISTORÇÃO: Tanenbaum (Sec. 2.1.3) lista ~10 campos

PROBLEMAS:
[OMISSÃO TANENBAUM] [CRÍTICO] Overhead de context switch 
  não mencionado.
  → Solução: Adicionar slide explicando custo do cambio 
     (salvar/carregar registros, TLB flush).

[DISTORÇÃO TANENBAUM] [CRÍTICO] Slide 6 simplifica PCB demais.
  → Solução: Expandir lista de campos: PID, estado, registros,
     prioridad, punteros de memoria, archivos abiertos, etc.

[FIGURA DO LIVRO AUSENTE] [IMPORTANTE] Slide 12 reserva espaço para a Fig. 3-3,
  mas a imagem não foi extraída e o PDF final ficou com placeholder.
  → Solução: recortar a figura do livro, salvar `fig3-3_base_limit.png`
     na pasta da aula e incluir a imagem real no slide final.
```

**Critério de falha:**
- Omissão de ponto essencial → `[OMISSÃO TANENBAUM]` `[CRÍTICO]`
- Distorção que confunde → `[DISTORÇÃO TANENBAUM]` `[CRÍTICO]`
- Contradição → `[DISTORÇÃO TANENBAUM]` `[CRÍTICO]`
- Figura central do livro deixada como placeholder ou não extraída → `[FIGURA DO LIVRO AUSENTE]` `[IMPORTANTE]`

---

### PASSO 6 — QUALIDADE PEDAGÓGICA GERAL, GLOSSÁRIO E COPIABILIDADE DE CÓDIGO

**Objetivo:** Verificar autoexplicatividade, coesão, separação teoria/lab, composição visual, qualidade do glossário e copiabilidade de código.

**Como fazer:**
1. **Autoexplicatividade:** Simular leitura sem fala do professor
2. **Coesão:** Cada slide tem ideia central clara?
3. **Separação teoria/lab:** Teoria tem comandos? Lab tem conceito novo?
4. **Composição visual:** Elemento cortado, ilegível, desequilibrado?
5. **Micro-composição TikZ:** Flechas, labels, espaçamento
6. **Glossário:** verificar se está agrupado por blocos conceituais, com densidade útil boa, títulos descritivos quando ajudarem, colunas equilibradas, sem páginas subocupadas e com visual de slide-resumo em cartões/blocos curtos
7. **Código copiável:** verificar numeração de linhas, codificação quebrada, wrapping nocivo, mistura visual com anotações laterais e, se houver PDF compilado, validar a extração com `pdftotext -layout`
8. **Relação foco x detalhe:** verificar se um mecanismo secundário não tomou o lugar da ideia principal da aula

**Formato de saída:**
```
═══════════════════════════════════════════════════════════
PASSO 6 — QUALIDADE PEDAGÓGICA GERAL, GLOSSÁRIO E COPIABILIDADE DE CÓDIGO
═══════════════════════════════════════════════════════════

AUTOEXPLICATIVIDADE:
Slide 4: Lista de campos do PCB sem explicar para que serve cada um
  → [SLIDE SEM COESÃO] [IMPORTANTE]
  → Solução: Adicionar breve explicação inline para cada campo

SEPARAÇÃO TEORIA/LAB:
Slide 10: Comando "ps aux" em aula teórica
  → [SEPARAÇÃO] [CRÍTICO] Aula teórica não pode ter comandos
  → Solução: Remover comando, mencionar apenas que "en el lab 
     usaremos ps"

COMPOSIÇÃO VISUAL:
Slide 7: Diagrama TikZ com label longo cortado à direita
  → [COMPOSIÇÃO VISUAL] [CRÍTICO] Label muito longo
  → Solução: Encurtar label ou usar \node separado

MICRO-COMPOSIÇÃO TIKZ:
Slide 8: Flecha atravessa texto do nodo
  → [MICROCOMPOSIÇÃO] [IMPORTANTE] Reposicionar flecha
  → Solução: Ajustar coordenadas ou usar bend

GLOSSÁRIO:
Slides 25–28: termos espalhados por páginas quase vazias e sem agrupamento claro
  → [GLOSSÁRIO] [IMPORTANTE] Baixa densidade útil e bloco sem lógica pedagógica
  → Solução: reorganizar por blocos conceituais, balancear colunas e usar cartões curtos com título descritivo

Slides 25–28: glossário em `description` cru, com cara de apostila
  → [GLOSSÁRIO] [IMPORTANTE] O conteúdo cabe, mas o render não parece slide didático
  → Solução: trocar para cartões/blocos curtos com termo em destaque e definição abaixo

Slide 28: glossário só cabe com `shrink=15`
  → [COMPOSIÇÃO VISUAL] [CRÍTICO] Shrink agressivo torna a leitura ruim
  → Solução: encurtar definições, redistribuir itens e dividir em novo bloco se necessário

CÓDIGO COPIÁVEL:
Slide 12: bloco Python com numeração de linhas
  → [CÓDIGO NÃO COPIÁVEL] [CRÍTICO] Números vão junto ao copiar
  → Solução: usar `numbers=none`

Slide 13: comando quebrado em duas linhas no PDF
  → [CÓDIGO NÃO COPIÁVEL] [IMPORTANTE] Quebra prejudica colar no terminal
  → Solução: encurtar linha, separar o exemplo ou usar arquivo-companheiro

FOCO DIDÁTICO:
Slides 9-11: o mecanismo auxiliar recebe três frames, mas a abstração central
fica com uma apresentação breve e pouco visual
  → [PRIORIZAÇÃO DIDÁTICA] [IMPORTANTE] O estudante pode sair lembrando o
     detalhe operacional e não a ideia principal
  → Solução: redistribuir a sequência para que a abstração central tenha mais
     exemplos, comparação e fechamento
```

**Critério de falha:**
- Slide depende de fala oral → `[IMPORTANTE]`
- Lista de fatos sem coesão → `[SLIDE SEM COESÃO]` `[IMPORTANTE]`
- Teoria com comandos → `[SEPARAÇÃO]` `[CRÍTICO]`
- Lab com conceito novo → `[SEPARAÇÃO]` `[CRÍTICO]`
- Elemento cortado/ilegível → `[COMPOSIÇÃO VISUAL]` `[CRÍTICO]`
- TikZ mal resolvido → `[MICROCOMPOSIÇÃO]` `[IMPORTANTE]`
- Glossário sem bloco conceitual claro ou com páginas subocupadas → `[GLOSSÁRIO]` `[IMPORTANTE]`
- Glossário com cara de lista corrida/apostila, mesmo cabendo → `[GLOSSÁRIO]` `[IMPORTANTE]`
- Glossário que depende de `shrink>10` ou fica espremido demais → `[COMPOSIÇÃO VISUAL]` `[CRÍTICO]`
- Numeração de linhas em código copiável → `[CÓDIGO NÃO COPIÁVEL]` `[CRÍTICO]`
- Mojibake/codificação quebrada em código ou comandos → `[CÓDIGO NÃO COPIÁVEL]` `[CRÍTICO]`
- Wrapping que prejudica colar no terminal → `[CÓDIGO NÃO COPIÁVEL]` `[IMPORTANTE]`
- Mecanismo secundário ofusca a abstração central da aula → `[PRIORIZAÇÃO DIDÁTICA]` `[IMPORTANTE]`

---

## RESUMO FINAL OBRIGATÓRIO

Ao final, apresentar resumo consolidado:

```
┌─────────────────────────────────────────────┐
│ RELATÓRIO DE AUDITORIA — Aula {{N}}         │
│                                             │
│ TOTAL DE PROBLEMAS: N                       │
│                                             │
│ [CRÍTICOS] (impedem completar a aula): N    │
│   — Slide X: PCB não definido inline        │
│   — Slide Y: Exemplo após atividade         │
│   — Slide Z: Omissão overhead context switch│
│                                             │
│ [IMPORTANTES] (comprometem qualidade): N    │
│   — Slide A: Falta exemplo antes atividade  │
│   — Slide B: Profundidade insuficiente PCB  │
│                                             │
│ [MENORES] (melhorias desejáveis): N         │
│   — Slide C: Margem excessiva em figura     │
│                                             │
└─────────────────────────────────────────────┘

STATUS: AGUARDANDO APROVAÇÃO PARA CORREÇÃO
```

---

## TAGS DE CLASSIFICAÇÃO

Use estas tags para classificar problemas:

- `[CRÍTICO]` — Impede estudante de completar a aula
- `[IMPORTANTE]` — Compromete qualidade pedagógica
- `[MENOR]` — Melhoria desejável
- `[OMISSÃO TANENBAUM]` — Ponto essencial omitido
- `[DISTORÇÃO TANENBAUM]` — Simplificação excessiva
- `[FIGURA DO LIVRO AUSENTE]` — Figura útil do Tanenbaum prevista, mas não extraída para a aula final
- `[PROGRESSÃO QUEBRADA]` — Sequência pedagógica violada
- `[ANALOGIA PROBLEMÁTICA]` — Analogia imprecisa
- `[SLIDE SEM COESÃO]` — Lista de fatos sem foco
- `[COMPOSIÇÃO VISUAL]` — Cortado/ilegível
- `[MICROCOMPOSIÇÃO]` — TikZ mal resolvido
- `[TÉCNICO LATEX]` — Erro de compilação
- `[SEPARAÇÃO]` — Teoria com comandos, lab com conceito novo
- `[ATIVIDADE IRRESOLVÍVEL]` — Conhecimento não ensinado
- `[EXPERIMENTO MECÂNICO]` — Lab virou execução sem interpretação
- `[GLOSSÁRIO]` — Glossário mal agrupado, subocupado, desequilibrado ou com cara de apostila
- `[CÓDIGO NÃO COPIÁVEL]` — Código ruim para copiar do PDF/terminal
- `[PRIORIZAÇÃO DIDÁTICA]` — Mecanismo de apoio tomou mais espaço do que o conceito nuclear
- `[CONTRASTE OPACO]` — Contraste relacional sem dizer explicitamente "em relação a quê"

---

## NÃO CORRIGIR AINDA

**NÃO corrija nada antes de apresentar o relatório.**

**Aguarde aprovação de Rodrigo.**

---

**Este comando audita a qualidade. Próxima etapa (após aprovação): `/aula-correcao {{N}}`**
