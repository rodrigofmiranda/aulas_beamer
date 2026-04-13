# regras_visuais.md — Regras de composição visual (8 a 16)

Estas regras são obrigatórias além das regras pedagógicas e das regras técnicas de compilação. Um slide que compila mas fica cortado, apertado, ilegível ou visualmente desequilibrado está **ERRADO** e deve ser refeito.

---

## REGRA 8 — FIGURA DO LIVRO QUANDO ELA ENSINA MELHOR

**Enunciado:** Use figura do Tanenbaum quando ela comunica visualmente o que texto não consegue. A figura deve **ensinar**, não apenas decorar.

### Quando usar figura do Tanenbaum:
- ✅ Diagramas de estados (processo, memória, arquivo)
- ✅ Estruturas de dados (PCB, tabela de páginas, i-node)
- ✅ Fluxogramas de algoritmos (planificação, paginação)
- ✅ Cronogramas (Gantt, timeline)
- ✅ Arquiteturas (camadas do SO, hierarquia de memória)

### Regra operacional obrigatória:
- Se a figura for **claramente útil e utilizável**, ela deve ser extraída durante a produção da aula
- O PNG recortado deve ficar na **pasta raiz da aula**
- O slide final deve sair **pronto no PDF**, com a figura real incluída
- Placeholder com `IfFileExists` ou bloco "Figura del libro no disponible" só é aceitável como rascunho temporário, nunca na versão final

### Quando NÃO usar figura (texto é melhor):
- ❌ Tabela de dados simples (usar `tabular` com `booktabs`)
- ❌ Lista de itens (usar `itemize`)
- ❌ Definição de termo (texto inline é mais claro)

### Como usar a figura pedagogicamente:
```latex
% ✅ CORRETO — figura + legenda explicativa
\begin{frame}{Modelo de 5 estados}
  \begin{columns}[T]
    \begin{column}{0.6\textwidth}
      \includegraphics[width=\columnwidth]{fig2-2_estados_proceso.png}
    \end{column}
    \begin{column}{0.38\textwidth}
      \textbf{Cómo leer el diagrama:}
      \begin{itemize}\small
        \item Cada círculo es un \textbf{estado}
        \item Las flechas indican \textbf{transiciones}
        \item Los eventos están escritos sobre las flechas
      \end{itemize}
    \end{column}
  \end{columns}
\end{frame}

% ❌ INCORRETO — figura sem explicação
\begin{frame}{Modelo de 5 estados}
  \includegraphics[width=\textwidth]{fig2-2_estados_proceso.png}
\end{frame}
% Estudante não sabe como interpretar o diagrama
```

### Critério de auditoria:
- Verificar se figura tem legenda explicativa ("como ler", "o que mostra", "o que prova")
- Se figura está sem contexto → `[COMPOSIÇÃO VISUAL]` `[IMPORTANTE]`
- Se a aula deixa placeholder no lugar de uma figura central e utilizável do livro → `[FIGURA DO LIVRO AUSENTE]` `[IMPORTANTE]`

---

## REGRA 9 — CROP LIMPO (sem legenda original, sem número, sem margens grandes)

**Enunciado:** Toda figura extraída do Tanenbaum deve ser recortada com detecção automática de conteúdo via PIL e NumPy. NUNCA usar coordenadas manuais.

### Script padrão de recorte (Python):
```python
from PIL import Image
import numpy as np

img = Image.open("figura_original.png").convert("RGB")
arr = np.array(img)

# Máscara: pixels com algum canal abaixo de 230 (detecta conteúdo não-branco)
mask = np.any(arr < 230, axis=2)

rows = np.where(mask.any(axis=1))[0]
cols = np.where(mask.any(axis=0))[0]

# Margem de segurança de 8 pixels em cada lado
top    = max(0, rows[0] - 8)
bottom = min(arr.shape[0], rows[-1] + 9)
left   = max(0, cols[0] - 8)
right  = min(arr.shape[1], cols[-1] + 9)

cropped = img.crop((left, top, right, bottom))
cropped.save("figura_recortada.png")
```

### Nomenclatura padrão:
```
figN-N_descricao.png
Exemplo: fig2-2_estados_proceso.png
```

### Local do arquivo:
- Salvar sempre na **pasta raiz da aula**
- Exemplo:
  `2026-1/SO___Unidad_3_Clase_9___2026/fig3-3_base_limit.png`

### O que remover do crop:
- ❌ Número da figura (ex: "Figure 2-2")
- ❌ Legenda original do livro (caption)
- ❌ Margem branca excessiva ao redor do conteúdo
- ✅ Manter apenas o conteúdo útil da figura + padding de 8px

### Critério de auditoria:
- Verificar se figura tem margem branca excessiva → `[COMPOSIÇÃO VISUAL]` `[MENOR]`
- Verificar se legenda original está incluída → `[COMPOSIÇÃO VISUAL]` `[IMPORTANTE]`
- Verificar se o asset PNG existe de fato na pasta da aula → `[FIGURA DO LIVRO AUSENTE]` `[IMPORTANTE]`

---

## REGRA 10 — TAMANHO ADEQUADO (nem gigante, nem minúscula)

**Enunciado:** Figura deve ser legível na projeção sem zoom, mas não dominar o slide inteiro.

### Tamanhos recomendados:
- **Figura em coluna (0.5\textwidth):** `width=\columnwidth` ou `width=0.9\columnwidth`
- **Figura em largura total:** `width=0.8\textwidth` ou `height=0.5\textheight`
- **Figura pequena inline:** `width=0.4\textwidth`

### Padrão PROIBIDO:
```latex
% ❌ Figura gigante que empurra texto para fora
\includegraphics[width=\textwidth, height=0.8\textheight]{...}

% ❌ Figura minúscula ilegível
\includegraphics[width=3cm]{...}
```

### Padrão CORRETO:
```latex
% ✅ Figura balanceada com texto
\begin{columns}[T]
  \begin{column}{0.55\textwidth}
    ... texto explicativo ...
  \end{column}
  \begin{column}{0.43\textwidth}
    \includegraphics[width=\columnwidth]{...}
  \end{column}
\end{columns}
```

### Teste de legibilidade:
- Todos os labels da figura devem ser legíveis em projeção normal
- Se figura tem texto muito pequeno, considerar reconstruir em TikZ

### Critério de auditoria:
- Simular projeção e verificar se figura é legível sem zoom
- Se ilegível → `[COMPOSIÇÃO VISUAL]` `[IMPORTANTE]`

---

## REGRA 11 — DIAGRAMA DIDÁTICO > DESENHO COMPLICADO

**Enunciado:** Diagramas TikZ devem ser **simples e claros**. Uma seta = uma ideia. Preferir múltiplos diagramas simples a um diagrama complexo.

### Princípios TikZ didáticos:
- ✅ Uma seta por transição/relação
- ✅ Labels curtos (≤5 palavras)
- ✅ Cores distintas por categoria (estados, tipos de memória, etc.)
- ✅ Espaço em branco suficiente entre elementos
- ❌ Múltiplas setas convergindo em um ponto
- ❌ Labels longos colados em setas
- ❌ Texto explicativo dentro do diagrama (mover para fora)

### Exemplo de diagrama simples:
```latex
\begin{tikzpicture}[
  state/.style={circle, draw, minimum size=1.2cm, font=\small},
  arr/.style={->, >=stealth, thick}
]
  \node[state, fill=staterdy] (listo) {Listo};
  \node[state, fill=staterun, right=3cm of listo] (ejecutando) {Ejecutando};
  \node[state, fill=stateblk, below=2cm of ejecutando] (bloqueado) {Bloqueado};
  
  \draw[arr] (listo) -- node[above]{\scriptsize scheduler} (ejecutando);
  \draw[arr] (ejecutando) -- node[right]{\scriptsize solicita E/S} (bloqueado);
  \draw[arr] (bloqueado) to[bend right=30] node[below]{\scriptsize E/S completa} (listo);
\end{tikzpicture}
```

### Quando dividir em dois diagramas:
- Se diagrama tem >6 nós → considerar dividir
- Se setas se cruzam → reorganizar ou dividir
- Se explicação não cabe no slide junto com o diagrama → dividir

### Critério de auditoria:
- Verificar se diagrama é compreendido em <5 segundos
- Se confuso ou sobrecarregado → `[MICROCOMPOSIÇÃO]` `[IMPORTANTE]`

---

## REGRA 12 — TABELAS E SEQUÊNCIAS QUANDO FOR MELHOR QUE TIKZ

**Enunciado:** Para comparações, cronogramas lineares e tabelas de dados, usar tabular com booktabs em vez de TikZ complexo.

### Quando usar tabular:
- ✅ Tabela de comparação de algoritmos (FCFS vs SJF vs RR)
- ✅ Cronograma Gantt simples (processo × tempo)
- ✅ Tabela de campos de estrutura (PCB, i-node)
- ✅ Lista de chamadas ao sistema

### Quando usar TikZ:
- ✅ Diagrama de estados
- ✅ Árvore de processos (hierarquia)
- ✅ Fluxo de controle (setas, decisões)
- ✅ Arquitetura em camadas

### Exemplo de tabela bem feita:
```latex
\begin{table}\small
  \begin{tabular}{lccc}
    \toprule
    \textbf{Algoritmo} & \textbf{Apropiativo} & \textbf{Complejidad} & \textbf{Uso} \\
    \midrule
    FCFS     & No  & O(1) & Lote \\
    SJF      & No  & O(n log n) & Lote \\
    SRTN     & Sí  & O(n log n) & Tiempo compartido \\
    RR       & Sí  & O(1) & Interactivo \\
    \bottomrule
  \end{tabular}
\end{table}
```

### Critério de auditoria:
- Se tabela simples foi convertida em TikZ desnecessariamente → `[MENOR]`
- Se TikZ complexo seria mais claro como tabela → `[COMPOSIÇÃO VISUAL]` `[IMPORTANTE]`

---

## REGRA 13 — NADA FORA DA ÁREA VISÍVEL

**Enunciado:** Nenhum elemento pode ultrapassar a área visível do frame: texto, blocos, imagens, diagramas TikZ, legendas, eixos, setas, labels.

### Áreas proibidas:
- ❌ Footline (barra inferior com autor/título/página)
- ❌ Margem direita
- ❌ Margem inferior
- ❌ Margem superior (menos crítico, mas evitar)

### Como verificar:
1. Compilar PDF
2. Visualizar slide em tela cheia
3. Verificar se todos os elementos estão inteiros e visíveis

### Se algo está cortado:
- **Opção 1:** Dividir em dois slides
- **Opção 2:** Trocar colunas por largura total
- **Opção 3:** Simplificar TikZ
- **Opção 4:** Mover explicação textual para outro slide
- **Última opção:** `[shrink=N]` (N≤10) apenas se N pequeno

### Critério de auditoria:
- Verificar visualmente cada slide no PDF renderizado
- Se algo está cortado → `[COMPOSIÇÃO VISUAL]` `[CRÍTICO]`

---

## REGRA 14 — TEXTO DENTRO DE NODOS DEVE CABER COM PADDING

**Enunciado:** Nodos TikZ devem ter `minimum size` e `inner sep` adequados para o texto não ficar espremido.

### Padrão PROIBIDO:
```latex
% ❌ Texto espremido, sem padding
\node[circle, draw] (n) {Texto muito longo aqui};
```

### Padrão CORRETO:
```latex
% ✅ Nodo com tamanho mínimo e padding
\node[circle, draw, minimum size=1.5cm, inner sep=3pt, font=\small] (n) 
  {Texto};

% ✅ Se texto é longo, usar retângulo em vez de círculo
\node[rectangle, draw, minimum width=2.5cm, minimum height=0.8cm, 
  inner sep=4pt, font=\footnotesize] (n) 
  {Texto mais longo};
```

### Critério de auditoria:
- Verificar se texto dentro de nodos está legível e não espremido
- Se espremido → `[MICROCOMPOSIÇÃO]` `[IMPORTANTE]`

---

## REGRA 15 — LABELS LONGOS NÃO PODEM SAIR DA ÁREA ÚTIL

**Enunciado:** Labels de setas TikZ devem ser curtos (≤5 palavras). Se frase é longa, mover para texto do slide.

### Padrão PROIBIDO:
```latex
% ❌ Label longo colado na seta
\draw[arr] (a) -- node[above]{El proceso solicita leer archivo 
  y queda esperando} (b);
```

### Padrão CORRETO:
```latex
% ✅ Label curto na seta, explicação no texto
\draw[arr] (a) -- node[above]{\scriptsize solicita E/S} (b);

% No texto do slide:
\textbf{Transición:} cuando el proceso solicita leer un archivo, 
pasa al estado Bloqueado y queda esperando hasta que termine 
la operación de E/S.
```

### Critério de auditoria:
- Verificar se labels de setas têm ≤5 palavras
- Se muito longo → `[MICROCOMPOSIÇÃO]` `[IMPORTANTE]`

---

## REGRA 16 - GLOSSÁRIO POR RENDER, BLOCOS CONCEITUAIS E CARTÕES
**Enunciado:** Glossário deve ser organizado por **blocos conceituais** e ajustado pelo **render real do slide**, não por uma contagem fixa. O padrão visual fixo do projeto é **cartão curto**: termo em destaque e definição logo abaixo. `shrink` só entra como último recurso leve.
### Estrutura recomendada:
```latex
\setbeamercolor{glossbox}{bg=lightgrayfill,fg=mqgray}
\newcommand{\glosscard}[2]{%
  \begin{beamercolorbox}[wd=\linewidth,sep=0.8ex,rounded=true,vmode]{glossbox}
    {\color{mqdeepred}\textbf{#1}}\par
    \vspace{0.25ex}
    {\footnotesize #2}
  \end{beamercolorbox}
}

\begin{frame}{Glosario | memoria y protección}
  \begin{columns}[T,onlytextwidth]
    \begin{column}{0.485\textwidth}
      \glosscard{Término 1}{Definición breve...}
      \glosscard{Término 2}{Definición breve...}
      \glosscard{Término 3}{Definición breve...}
    \end{column}
    \begin{column}{0.485\textwidth}
      \glosscard{Término 4}{Definición breve...}
      \glosscard{Término 5}{Definición breve...}
      \glosscard{Término 6}{Definición breve...}
    \end{column}
  \end{columns}
\end{frame}
```
### Critérios de composição:
- Agrupar termos por sentido pedagógico.
  Ex.: `memoria y protección`, `asignación contigua`, `fragmentación y gestión`.
- Preferir títulos descritivos em vez de `Glosario (I)`, `Glosario (II)` quando isso ajudar a leitura.
- Preferir **2 colunas de cartões** quando as definições couberem em 1-2 linhas e isso evitar abrir páginas extras.
- Em **1 coluna**, usar em geral **4-6 itens**.
- Em **2 colunas**, usar em geral **6-10 itens totais**, balanceados entre as colunas.
- Manter o termo como entrada visual forte e a definição logo abaixo.
- Evitar aparência de **lista corrida, apostila ou dicionário bruto**.
- Se sobrar **mais de cerca de 1/3 da altura útil** do frame, recombinar os itens antes de criar nova página.
- Se apertar um pouco no final, usar no máximo `shrink=2` a `shrink=4`.
### Se não cabe:
- **Nunca** usar `shrink>10` para forçar.
- Primeiro: reequilibrar as colunas.
- Depois: encurtar definições redundantes.
- Depois: dividir em mais um bloco conceitual.
- Só por último: aplicar shrink leve.
### Critério de auditoria:
- Verificar se o glossário está agrupado por sentido pedagógico, não só por sobra de termos.
- Verificar se há excesso de páginas com muito espaço em branco.
- Verificar se há equilíbrio entre as colunas.
- Verificar se o visual é de slide-resumo e não de lista impressa crua.
- Se o glossário estiver espalhado demais ou com baixa densidade útil -> `[GLOSSÁRIO]` `[IMPORTANTE]`
- Se o glossário estiver com cara de lista corrida/bruta, mesmo sem overflow -> `[GLOSSÁRIO]` `[IMPORTANTE]`
- Se `shrink>10` -> `[COMPOSIÇÃO VISUAL]` `[CRÍTICO]`
---
## VERIFICA??O VISUAL OBRIGAT?RIA POR FRAME

Antes de considerar um slide terminado, verificar:
- ☑️ Algum elemento ficou cortado à direita, embaixo ou sobre a footline?
- ☑️ A figura inteira aparece?
- ☑️ Todos os labels e setas estão legíveis sem zoom?
- ☑️ A legenda da figura está inteira?
- ☑️ Há equilíbrio entre as colunas ou uma coluna ficou pesada demais?
- ☑️ Este frame precisaria virar dois slides para ensinar melhor?

Se **qualquer resposta indicar problema**, NÃO manter o slide. Refazer a composição.

---

## MICRO-AUDITORIA VISUAL OBRIGATÓRIA PARA TIKZ

Se um frame tiver diagrama TikZ, antes de entregar, fazer auditoria visual fina:
- ☑️ Alguma flecha atravessa texto?
- ☑️ Alguma flecha termina de forma imprecisa?
- ☑️ Algum label parece solto ou ambíguo?
- ☑️ Há texto explicativo longo demais colado em seta?
- ☑️ Dois labels ficaram visualmente competindo?
- ☑️ O diagrama é entendido em menos de 5 segundos?
- ☑️ O fluxo visual principal está óbvio?
- ☑️ Há espaço em branco suficiente entre labels, setas e caixas?

Se **qualquer resposta for problemática:**
- Simplificar o diagrama
- Encurtar os labels
- Mover frases longas para o texto do slide
- Reposicionar elementos
- Ou dividir o conteúdo em dois frames

### Regra prática:
**Em diagramas pequenos, a flecha leva a ideia principal; o texto do slide leva a explicação completa.** Não sobrecarregue a flecha com frase longa.

---

## SLIDES DUPLOS PARA DIAGRAMAS PRINCIPAIS (Regra F2 da instrução do projeto)

Todo diagrama principal de uma aula (diagrama de estados, PCB, Gantt, hierarquia de processos, etc.) deve aparecer em **DOIS slides consecutivos**:
1. **Versão imagem** — Figura do Tanenbaum recortada
2. **Versão diagrama TikZ** — Reconstruído nas cores UTEC-SO

O professor elimina um dos dois antes de projetar, dependendo do contexto.

### Modelo de slides duplos:
```latex
% [VERSÃO IMAGEM] — eliminá este slide se preferís el diagrama TikZ
\begin{frame}{Modelo de 5 estados
  \textmd{\small--- versión imagen (Tanenbaum Fig.~2-2)}}
  \includegraphics[width=0.8\textwidth]{fig2-2_estados_proceso.png}
  ...
\end{frame}

% [VERSÃO DIAGRAMA TikZ] — eliminá este slide se preferís a imagem
\begin{frame}{Modelo de 5 estados
  \textmd{\small--- versión diagrama}}
  \begin{tikzpicture}[...]
    % diagrama reconstruído nas cores mqred, staterun, etc.
  \end{tikzpicture}
  ...
\end{frame}
```

### Cores por tipo de elemento (já definidas no projeto):
```latex
% Estados de processo
staterun   RGB(39,139,70)    — Ejecutando
staterdy   RGB(52,101,164)   — Listo
stateblk   RGB(166,25,46)    — Bloqueado
statenew   RGB(106,60,140)   — Nuevo
stateend   RGB(100,100,100)  — Terminado

% Estrutura geral
mqred       RGB(166,25,46)
mqdeepred   RGB(118,35,47)
mqgray      RGB(55,58,54)
mqlightgray RGB(237,235,229)

% PCB (campos por categoria)
pcbblue    RGB(52,101,164)   — gestão de processo
pcbgreen   RGB(39,139,70)    — gestão de memória
pcbyellow  RGB(180,120,10)   — gestão de arquivos
```

---

## RESUMO DAS REGRAS VISUAIS

| # | Regra | Critério de falha | Gravidade |
|---|-------|-------------------|-----------|
| 8 | **Figura ensina** | Figura sem legenda ou contexto | `[IMPORTANTE]` |
| 9 | **Crop limpo** | Margem excessiva, legenda original incluída | `[MENOR]` a `[IMPORTANTE]` |
| 10 | **Tamanho adequado** | Figura ilegível ou dominando slide | `[IMPORTANTE]` |
| 11 | **Diagrama didático** | TikZ confuso, sobrecarregado | `[IMPORTANTE]` |
| 12 | **Tabela vs TikZ** | Escolha inadequada de formato | `[MENOR]` a `[IMPORTANTE]` |
| 13 | **Área visível** | Elemento cortado | `[CRÍTICO]` |
| 14 | **Texto em nodos** | Texto espremido | `[IMPORTANTE]` |
| 15 | **Labels curtos** | Label >5 palavras | `[IMPORTANTE]` |
| 16 | **Glossário** | Bloco arbitrário, página subocupada ou `shrink>10` | `[IMPORTANTE]` a `[CRÍTICO]` |

---

**Estas regras garantem que slides não apenas compilem, mas sejam legíveis, equilibrados e pedagogicamente eficazes na projeção.**
