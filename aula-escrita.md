# /aula-escrita
## Uso: `/aula-escrita N`
## Exemplo: `/aula-escrita 7`

---

A estrutura da Aula **{{N}}** foi aprovada. Escreva o arquivo `.tex` completo.

---

## ANTES DE ESCREVER:

### 1. Reler pontos essenciais do Tanenbaum
Releia os **pontos B** do planejamento aprovado (o que o Tanenbaum diz que é essencial).

**Cada um desses pontos DEVE aparecer no material.**

Se algum ficou de fora da estrutura aprovada, **adicione antes de escrever**.

### 2. Reler layout.tex
Leia o arquivo `layout.tex` e siga sua estrutura **exatamente**:
- Paleta de cores (mqred, mqdeepred, mqgray, mqlightgray)
- Footline (3 boxes: 50%-40%-10%)
- Bullets (pifont: ding{228}, ding{51}, ding{55})
- Glosário (padrão fixo: cartões curtos em 2 colunas com `beamercolorbox` e macro tipo `\glosscard`; agrupar por bloco conceitual; usar `description` só se houver justificativa visual clara)

### 3. Reler regras
- `/home/claude/regras_pedagogicas.md` → Regras 1–8
- `/home/claude/regras_visuais.md` → Regras 8–16
- `/home/claude/regras_tecnicas_latex.md` → Regras T1–T9

### 4. Verificar aulas anteriores
Consulte `SO___Unidad_*_Clase_*___2026.tex` para manter **consistência visual e terminológica**.

### 5. Preparar o caminho direto antes de redigir
Antes de sair escrevendo slides, fechar estas decisões operacionais:
- qual é o **arquivo `.tex` final** desta aula
- quais figuras do Tanenbaum serão extraídas **agora** com `scripts/extract_tanenbaum_figure.py`
- quais exemplos de código vão virar **arquivo-companheiro**
- se for lab Linux, confirmar `shell.cloud.google.com` como ambiente padrão

**Objetivo:** escrever uma vez só, já perto da versão final, em vez de depender de placeholders e correções tardias.

### 6. Regra anti-retrabalho antes de editar
- preferir **cores, macros, estilos e blocos já existentes** no arquivo ou em `layout.tex`
- não inventar cor, macro, pacote ou estilo novo para ajuste pequeno se houver equivalente já disponível
- se algo novo for realmente necessário, **definir no mesmo momento em que for usado**
- se o terminal mostrar texto com codificação quebrada, **não confiar nessa renderização** para localizar blocos; conferir o conteúdo real do arquivo primeiro

---

## AO ESCREVER, OBSERVE:

### PROGRESSÃO (Regra 3)
**Comece cada conceito com intuição ou analogia ANTES da definição técnica.**

Nunca abra um slide de conteúdo novo diretamente com uma definição formal.

Sempre prepare o terreno com:
- Pergunta ("¿Qué pasa cuando...?")
- Situação cotidiana ("Cuando abrís una aplicación...")
- Conexão com conhecimento prévio ("Recordemos que en Arquitectura vimos...")

**Padrão PROIBIDO:**
```latex
\begin{frame}{Context switch}
  \textbf{Context switch:} proceso de guardar el estado...
\end{frame}
% ❌ Definição sem preparo
```

**Padrão CORRETO:**
```latex
\begin{frame}{Context switch: ¿cómo el SO cambia de proceso?}
  \textbf{Situación:} el SO necesita pausar un proceso y ejecutar otro.
  
  ¿Qué información debe guardar antes de cambiar?
  
  \vspace{0.3cm}
  
  \textbf{Context switch:} proceso de guardar el estado del proceso 
  saliente y cargar el estado del proceso entrante.
\end{frame}
% ✅ Preparação + definição
```

---

### PROFUNDIDADE (Regra 2)
Para cada conceito novo, o conjunto de slides deve responder:
1. **O que é?**
2. **Para que serve?**
3. **Como funciona?**
4. **Onde aparece na prática?**

**Se um conceito é usado em atividade, inclua exemplo concreto ANTES da atividade, nunca depois.**

### PRIORIZAÇÃO DIDÁTICA OBRIGATÓRIA
Nem todo item importante do capítulo merece o mesmo peso no slide.

Ao escrever, distinguir sempre:
- **conceito nuclear** -> abstração central sem a qual o estudante não entende a unidade
- **mecanismo de apoio** -> detalhe, implementação ou dispositivo que ajuda a sustentar essa abstração

Regra prática:
- o conceito nuclear deve aparecer antes
- o conceito nuclear deve receber mais espaço, mais exemplos e mais clareza visual
- o mecanismo de apoio deve receber apenas o detalhe necessário para sustentar a intuição e a fidelidade ao Tanenbaum

Se o mecanismo puder ser resumido em um exemplo curto sem perda pedagógica, ele **não deve virar sequência longa de slides**.

Exemplo de aplicação:
- `espacio de direcciones` / `memoria lógica` -> foco principal
- `registro base` / `registro límite` -> mecanismo inicial para mostrar deslocamento e proteção; não deixar esse mecanismo ocupar mais energia didática do que a própria abstração

---

### FLUIDEZ
Cada slide deve ter uma **razão clara de existir** e deve conduzir naturalmente ao próximo.

Evite slides que parecem **listas de fatos isolados** — cada item deve estar conectado aos demais por uma **ideia central explícita**.

**Use frase-puente** se a conexão não for óbvia:
```latex
\textbf{Ahora bien,} para que el planificador pueda funcionar, 
necesita información sobre cada proceso...
```

### CONTRASTES RELACIONAIS DEVEM DIZER "EM RELAÇÃO A QUÊ"
Sempre que o conteúdo usar pares como:
- `interna` / `externa`
- `lógica` / `física`
- `local` / `global`
- `usuario` / `kernel`

o slide precisa responder explicitamente qual é o referente do contraste.

Exemplos obrigatórios de clareza:
- `fragmentación interna` = espaço desperdiçado **dentro da partición ya asignada**
- `fragmentación externa` = huecos livres **fuera de los bloques ocupados, entre particiones/procesos**
- `memoria lógica` = endereços **vistos pelo processo**
- `memoria física` = posições **reais da RAM**

Regra visual:
- preferir a mesma base de desenho comparada lado a lado
- ou mapas paralelos com legenda comum
- evitar dois desenhos soltos sem dizer o que muda em cada um

Frase de fechamento recomendada quando houver contraste:
- `Interna = sobra dentro de una partición ya asignada; externa = huecos libres entre particiones.`

---

### ATIVIDADES E EXPERIMENTOS (Regra 6)
- **Especifique no enunciado qual modelo usar**: "Usando el modelo de 5 estados...", "Aplique el algoritmo FCFS..."
- **Slides de resposta:** notação textual plana apenas
  - ✅ `Estado --etiqueta--> Estado`
  - ❌ NUNCA `\xrightarrow{etiqueta}`
- **Resolúvel em 15 minutos máximo**
- **Conceitos necessários devem ter sido ensinados ANTES**
- **Em labs, a atividade deve ser um experimento guiado**, não uma execução mecânica
  - ✅ pedir previsão antes de rodar
  - ✅ dizer exatamente o que observar
  - ✅ pedir explicação, comparação ou interpretação depois
  - ❌ evitar consignas do tipo "copie, execute e envie captura" como núcleo pedagógico
- **O foco é o conceito de SO**, não a sintaxe do script
- **Se houver entregas múltiplas**, deixar explícito o que observar e o que entregar em cada experimento
- **Em aulas teóricas, de revisão ou integração, prever `Ejercicios para casa` quando fizer sentido**
  - preferir **2 a 4 consignas**
  - usar apenas conteúdo já ensinado
  - servir como treino adicional, não como teoria nova
  - colocar em slide final ou penúltimo com título claro

### CÓDIGO COPIÁVEL PARA LAB
- Todo código que o estudante deve copiar precisa ser preparado para **colar direto do PDF/Cloud Shell sem retrabalho**
- **Nunca usar numeração de linhas** em blocos copiáveis
- **Evitar caracteres e comentários que quebrem a cópia** quando houver alternativa equivalente mais simples
- **Preferir linhas curtas** e evitar wrapping que misture indentação ou junte comandos
- **Se o código for central ou mais longo, preferir arquivo-companheiro** (`.py`, `.sh`) com `\lstinputlisting`
- **Não confiar em shrink agressivo** para "fazer caber" código copiável; se apertou, virar slide de largura total ou separar em outro frame
- Assumir como cenário padrão de uso o aluno copiando do PDF para `shell.cloud.google.com`

### GLOSÁRIO COMPACTO
- O glossário deve ser organizado **pelo render**, não por uma contagem fixa de itens por página
- O glossário deve ser organizado também por **blocos conceituais**, não por “sobrou termo, abre página”
- Objetivo: **nem estourar nem sobrar um slide vazio demais**
- **Padrão fixo:** usar cartões curtos com termo em destaque e definição logo abaixo
- O padrão preferido é `beamercolorbox` + macro reutilizável, por exemplo `\glosscard{Término}{Definición}`
- Preferir títulos de bloco como `Glosario | memoria y protección` quando isso ajudar a leitura
- Se as definições forem curtas ou médias, **preferir 2 colunas de cartões** antes de abrir páginas extras
- Em **1 coluna**, usar em geral **4–6 itens** quando as definições ocuparem 2–3 linhas
- Em **2 colunas**, usar em geral **6–10 itens totais**, balanceados entre as colunas, quando as definições couberem em 1–2 linhas
- Se um frame de glossário deixar **mais de cerca de 1/3 da altura útil em branco**, recombinar os itens
- Evitar visual de **lista corrida / apostila / dicionário bruto**; o slide precisa parecer resumo visual, não folha impressa
- `shrink` no glossário é **último recurso**, não padrão automático
- `description` cru em duas colunas não é mais o padrão do projeto

---

### DIAGRAMAS TIKZ
**Acompanhe cada diagrama de legenda textual** explicando como lê-lo.

Para diagramas de estados, explique **cada estado e cada transição** antes ou no mesmo slide.

**Exemplo:**
```latex
\begin{frame}{Modelo de 5 estados}
  \begin{columns}[T]
    \begin{column}{0.55\textwidth}
      \begin{tikzpicture}[...]
        % diagrama
      \end{tikzpicture}
    \end{column}
    \begin{column}{0.43\textwidth}
      \textbf{Cómo leer el diagrama:}
      \begin{itemize}\small
        \item Cada círculo es un \textbf{estado}
        \item Las flechas indican \textbf{transiciones}
        \item Los eventos están sobre las flechas
      \end{itemize}
    \end{column}
  \end{columns}
\end{frame}
```

---

## VALIDAÇÃO VISUAL OBRIGATÓRIA POR FRAME

**Antes de considerar um slide terminado, verifique não apenas o conteúdo, mas também a composição visual.**

### VALIDAÇÃO ESTRUTURAL RÁPIDA
Se a mudança mexer em:
- preâmbulo
- cores
- macros
- TikZ
- colunas
- blocks

rode compilação logo após esse grupo de mudanças, antes de continuar editando outras partes. Isso evita acumular erros triviais e correções em cascata.

Pergunte obrigatoriamente para cada frame:
- ☑️ Algum elemento ficou cortado à direita, embaixo ou sobre a footline?
- ☑️ A figura inteira aparece?
- ☑️ Todos os labels e setas estão legíveis sem zoom?
- ☑️ A legenda da figura está inteira?
- ☑️ Há equilíbrio entre as colunas ou uma coluna ficou pesada demais?
- ☑️ Este frame precisaria virar dois slides para ensinar melhor?

**Se a resposta indicar aperto, corte ou ilegibilidade, NÃO mantenha o slide. Refaça a composição.**

### Trocas obrigatórias preferenciais:
1. **Dividir em dois frames**
2. **Trocar colunas por largura total**
3. **Simplificar o TikZ**
4. **Mover a explicação textual para outro slide**
5. **Reduzir blocos** — NUNCA "esmagar" com shrink agressivo

---

## REGRAS ESPECÍFICAS PARA FIGURAS E TIKZ

### Figuras em colunas
- **Figura em coluna só é permitida se continuar legível**
- Figura com muitos labels ou nota sob a imagem deve ir em **slide de largura total** ou virar **dois frames**

### Slides sobrecarregados (PROIBIDOS)
- **Nunca combinar, no mesmo frame:**
  - Texto corrido longo
  - + Dois blocos
  - + Figura detalhada
- Se precisa de tudo isso, **dividir em dois slides**

### Explicação de figuras
- Se a figura precisa de "como ler", essa explicação deve ficar **no mesmo slide de modo legível** ou em um **slide imediatamente anterior**

---

## MICRO-AUDITORIA VISUAL OBRIGATÓRIA PARA TIKZ

Se um frame tiver diagrama TikZ, não basta dizer que "compila" ou que "não ficou cortado".

**Antes de entregar, faça uma auditoria visual fina do render** e responda internamente:

- ☑️ Alguma flecha atravessa texto?
- ☑️ Alguma flecha termina de forma imprecisa?
- ☑️ Algum label parece solto ou ambíguo?
- ☑️ Há texto explicativo longo demais colado em seta?
- ☑️ Dois labels ficaram visualmente competindo?
- ☑️ O diagrama é entendido em menos de 5 segundos?
- ☑️ O fluxo visual principal está óbvio?
- ☑️ Há espaço em branco suficiente entre labels, setas e caixas?

**Se qualquer resposta for problemática:**
- Simplificar o diagrama
- Encurtar os labels
- Mover frases longas para o texto do slide
- Reposicionar elementos
- Ou dividir o conteúdo em dois frames

### REGRA PRÁTICA:
**Em diagramas pequenos, a flecha leva a ideia principal; o texto do slide leva a explicação completa.**

Não sobrecarregue a flecha com frase longa.

---

## SLIDES DUPLOS PARA DIAGRAMAS PRINCIPAIS

Todo diagrama principal (estados, PCB, Gantt, hierarquia) deve aparecer em **DOIS slides consecutivos**:
1. **Versão imagem** — Figura do Tanenbaum recortada
2. **Versão TikZ** — Reconstruído nas cores UTEC-SO

O professor elimina um dos dois antes de projetar.

**Regra operacional obrigatória:**
- Se a figura do livro for claramente útil e utilizável, ela deve ser **extraída na hora**, não deixada como tarefa futura
- O arquivo deve ficar na **pasta raiz da aula** (`2026-1/.../figN-N_descricao.png`)
- A versão final do `.tex` deve apontar para o arquivo real com `\includegraphics`
- `IfFileExists` + alertas do tipo "Figura do livro no disponible" só podem existir como rascunho temporário, nunca no entregável final

**Modelo:**
```latex
% [VERSÃO IMAGEM]
\begin{frame}{Modelo de 5 estados
  \textmd{\small--- versión imagen (Tanenbaum Fig.~2-2)}}
  \includegraphics[width=0.8\textwidth]{fig2-2_estados_proceso.png}
  ...
\end{frame}

% [VERSÃO TIKZ]
\begin{frame}{Modelo de 5 estados
  \textmd{\small--- versión diagrama}}
  \begin{tikzpicture}[...]
    % diagrama nas cores mqred, staterun, etc.
  \end{tikzpicture}
  ...
\end{frame}
```

**Cores por tipo de elemento** (já definidas):
```latex
% Estados de processo
staterun   RGB(39,139,70)    — Ejecutando
staterdy   RGB(52,101,164)   — Listo
stateblk   RGB(166,25,46)    — Bloqueado
statenew   RGB(106,60,140)   — Nuevo
stateend   RGB(100,100,100)  — Terminado

% PCB
pcbblue    RGB(52,101,164)   — gestão de processo
pcbgreen   RGB(39,139,70)    — gestão de memória
pcbyellow  RGB(180,120,10)   — gestão de arquivos
```

---

## CRITÉRIOS DE QUALIDADE FINAL

Ao terminar, releia o arquivo `.tex` completo e verifique:

1. ✅ **REGRA 1 (Primeira aparição):** Todo termo técnico definido inline na 1ª aparição?
2. ✅ **REGRA 2 (Profundidade):** Conceitos respondem: o que é / para que / como / onde?
3. ✅ **REGRA 3 (Progressão):** Intuição antes de abstração, exemplo antes de exercício?
4. ✅ **Priorização didática:** O conceito nuclear recebeu mais espaço e clareza do que o mecanismo de apoio?
5. ✅ **Contrastes relacionais:** Todo `interna/externa`, `lógica/física` etc. responde explicitamente "em relação a quê" no texto e no visual?
6. ✅ **REGRA 5 (Separação):** Teoria sem comandos, lab sem conceito novo?
7. ✅ **REGRA 6 (Atividades):** Modelo especificado, notação textual plana, ≤15min?
8. ✅ **Didática de lab:** Experimentos pedem previsão, observação e explicação, em vez de só copiar/executar?
9. ✅ **Treino extra:** Quando a aula pedir mais fixação, há `Ejercicios para casa` coerentes com o conteúdo?
10. ✅ **Código copiável:** Blocos executáveis estão sem numeração, sem codificação quebrada e com layout seguro para copiar?
11. ✅ **Fidelidade Tanenbaum:** Pontos essenciais presentes, sem distorções?
12. ✅ **Composição visual:** Nenhum elemento cortado, ilegível ou desequilibrado?
13. ✅ **Preflight mecânico:** `python scripts/check_lesson_ready.py --class {{N}}` roda sem erros?

### PRÉ-ENTREGA OBRIGATÓRIA

Antes de encerrar a escrita, rode:

```bash
python scripts/check_lesson_ready.py --class {{N}}
```

Se aparecer erro mecânico conhecido (placeholder de figura, numeração de linhas, asset ausente, etc.), corrigir **antes** de entregar a escrita para auditoria.

---

## NÃO COMPILAR AINDA

**NÃO compile o arquivo `.tex` nesta etapa.**

A compilação será feita no **Passo 4** (correção), após auditoria aprovada.

**Aguarde auditoria.**

---

**Este comando produz o `.tex` completo. Próxima etapa: `/aula-auditoria {{N}} CAPX`**
