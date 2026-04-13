# regras_tecnicas_latex.md — Regras técnicas LaTeX (T1 a T9) + estrutura

Estas regras são obrigatórias para garantir compilação sem erros fatais e warnings aceitáveis. Violá-las causa erros de compilação ou problemas visuais graves.

## PROTOCOLO OPERACIONAL DIRETO

Para evitar retrabalho, não aplicar estas regras só "de memória". Use a automação local do projeto:

```bash
python scripts/check_lesson_ready.py --class N
python scripts/check_lesson_ready.py --class N --compile
```

O primeiro comando serve como preflight mecânico ainda na escrita. O segundo centraliza compilação com `latexmk`, leitura de log e validação básica de copiabilidade do PDF.

## PROTOCOLO ANTI-RETRABALHO

Antes de editar um `.tex` já compilável, seguir estas regras operacionais:

1. **Preferir o que já existe**
   - reutilizar cores, macros, estilos TikZ e blocos já definidos no arquivo ou em `layout.tex`
   - não criar cor, macro, pacote ou estilo novo para um ajuste pequeno se o resultado puder ser obtido com elementos já existentes

2. **Se algo novo for inevitável, definir antes de usar**
   - cor nova -> `\definecolor` no preâmbulo no mesmo patch
   - macro nova -> definição no mesmo patch
   - pacote novo -> justificar por que os recursos atuais não bastam

3. **Não confiar em texto quebrado do terminal**
   - se aparecer mojibake (`Ã³`, `Ã±`, etc.), não usar essa renderização como base única para localizar e substituir blocos
   - primeiro conferir o conteúdo real do arquivo com leitura Unicode segura

4. **Compilar cedo após mudança estrutural**
   - se o ajuste tocar preâmbulo, TikZ, cores, macros, colunas ou blocks, rodar compilação logo em seguida
   - não acumular várias mudanças estruturais sem validar no meio

Objetivo: evitar perder tempo e contexto com erros triviais de compilação ou patches aplicados no trecho errado.

---

## REGRA T1 — NÃO USAR \begin{enumerate} EM FRAMES BEAMER

**Problema:** `\begin{enumerate}` dentro de frames Beamer com ambientes aninhados (columns, block, tikzpicture) causa erro fatal:
```
! TeX capacity exceeded, sorry [grouping levels=255].
```

### Padrão PROIBIDO:
```latex
\begin{frame}{Título}
  \begin{enumerate}
    \item Primeiro item
    \item Segundo item
  \end{enumerate}
\end{frame}

% ❌ Causa erro "grouping levels=255"
```

### Padrão CORRETO:
```latex
\begin{frame}{Título}
  \begin{itemize}
    \item[\textbf{1.}] Primeiro item
    \item[\textbf{2.}] Segundo item
  \end{itemize}
\end{frame}

% ✅ Funciona perfeitamente
```

### Quando aplicar:
- **Sempre** substituir `enumerate` por `itemize` com labels manuais
- Mesmo em listas simples sem aninhamento (para manter consistência)

### Critério de auditoria:
- Buscar por `\begin{enumerate}` no arquivo
- Se encontrado → `[TÉCNICO LATEX]` `[CRÍTICO]`

---

## REGRA T2 — NÃO USAR \begin{tikzpicture} COMO WRAPPER DE IMAGEM

**Problema:** Usar `\begin{tikzpicture}` apenas como wrapper decorativo de `\includegraphics` causa erro de compilação e é desnecessário.

### Padrão PROIBIDO:
```latex
\begin{column}{0.5\textwidth}
  \begin{tikzpicture}
    \node {\includegraphics[width=\columnwidth]{figura.png}};
  \end{tikzpicture}
\end{column}

% ❌ tikzpicture desnecessário, causa erro
```

### Padrão CORRETO:
```latex
\begin{column}{0.5\textwidth}
  \includegraphics[width=\columnwidth]{figura.png}
\end{column}

% ✅ Imagem diretamente, sem wrapper
```

### Quando usar tikzpicture:
- ✅ Para desenhar diagramas (nós, setas, formas)
- ❌ Como wrapper de imagem já pronta

### Critério de auditoria:
- Buscar por `\node {\includegraphics`
- Se encontrado → `[TÉCNICO LATEX]` `[CRÍTICO]`

---

## REGRA T2A — FIGURA DO LIVRO DEVE VIRAR ASSET REAL DA AULA

**Problema:** Deixar `IfFileExists` ou alertas de imagem ausente faz o slide compilar, mas entrega um PDF inacabado.

### Padrão CORRETO:
```latex
% arquivo salvo na pasta raiz da aula:
% fig3-3_base_limit.png

\begin{frame}{Registros base y límite}
  \includegraphics[width=0.8\textwidth]{fig3-3_base_limit.png}
\end{frame}
```

### Padrão PROIBIDO na versão final:
```latex
\IfFileExists{fig3-3_base_limit.png}{
  \includegraphics[width=\linewidth]{fig3-3_base_limit.png}
}{
  \begin{alertblock}{Figura del libro no disponible}
    ...
  \end{alertblock}
}
```

### Regra prática:
- Se a figura do livro for central e utilizável, extrair durante a produção da aula
- Salvar o PNG já recortado na pasta raiz da aula
- A versão final da aula deve referenciar o asset real, sem placeholder

### Critério de auditoria:
- `IfFileExists` para figura central na versão final -> `[FIGURA DO LIVRO AUSENTE]` `[IMPORTANTE]`
- Bloco "Figura del libro no disponible" no PDF final -> `[FIGURA DO LIVRO AUSENTE]` `[IMPORTANTE]`

---

## REGRA T3 - GLOSSÁRIO: COMPACTAR COM CRITÉRIO, NÃO ESPALHAR NEM ESMAGAR
**Problema:** Glossário pode falhar de três jeitos: ficar alto demais (`Overfull \vbox`), ficar espalhado demais com páginas subocupadas, ou ficar com cara de lista crua mesmo cabendo.
### Padrão PROIBIDO:
```latex
\begin{frame}[shrink=15]{Glosario}  % shrink>10 = ilegível
  \begin{description}[...]
    \item[Term 1] ...
    ... (10 itens)
  \end{description}
\end{frame}
\begin{frame}[shrink=4]{Glosario (III)}  % página quase vazia
  \begin{description}[...]
    \item[Term 9] ...
    \item[Term 10] ...
  \end{description}
\end{frame}
```
### Padrão CORRETO:
```latex
\setbeamercolor{glossbox}{bg=lightgrayfill,fg=mqgray}
\newcommand{\glosscard}[2]{%
  \begin{beamercolorbox}[wd=\linewidth,sep=0.8ex,rounded=true,vmode]{glossbox}
    {\color{mqdeepred}\textbf{#1}}\par
    \vspace{0.25ex}
    {\footnotesize #2}
  \end{beamercolorbox}
}

\begin{frame}{Glosario | asignación contigua}
  \begin{columns}[T,onlytextwidth]
    \begin{column}{0.485\textwidth}
      \glosscard{Asignación contigua}{...}
      \glosscard{Partición}{...}
      \glosscard{Hueco}{...}
    \end{column}
    \begin{column}{0.485\textwidth}
      \glosscard{Particiones fijas}{...}
      \glosscard{Particiones variables}{...}
      \glosscard{Continuidad}{...}
    \end{column}
  \end{columns}
\end{frame}
```
### Regra prática:
- Agrupar por **blocos conceituais**.
- Usar como padrão **cartões curtos** (`beamercolorbox` + macro como `\glosscard`).
- Preferir **2 colunas** quando as definições forem curtas ou médias.
- Em 1 coluna: usar em geral 4-6 itens.
- Em 2 colunas: usar em geral 6-10 itens totais.
- Evitar `description` cru como formato-padrão do glossário.
- Se sobrar mais de cerca de 1/3 da altura útil, recombinar os itens.
- Se faltar pouco para caber, usar no máximo `shrink=2` a `shrink=4`.
### Critério de auditoria:
- Se `shrink>10` -> `[TÉCNICO LATEX]` `[CRÍTICO]`
- Se houver `Overfull \vbox` real em glossário -> `[COMPOSIÇÃO VISUAL]` `[CRÍTICO]`
- Se o glossário estiver espalhado demais, com baixa densidade útil -> `[GLOSSÁRIO]` `[IMPORTANTE]`
- Se o glossário parecer lista crua/apostila em vez de slide-resumo -> `[GLOSSÁRIO]` `[IMPORTANTE]`
---
## REGRA T4## REGRA T4 — NÃO USAR \colorbox + \parbox PARA TERMINAL

**Problema:** Blocos de terminal com `\colorbox{...}{\parbox{...}{...}}` são difíceis de controlar e causam Overfull \hbox.

### Padrão PROIBIDO:
```latex
\colorbox{termbg}{\parbox{\dimexpr\linewidth-12pt}{
  \color{termfg}\ttfamily 
  $ ps aux | grep python
  user  1234  0.5  1.2  ...
}}

% ❌ Causa Overfull \hbox, difícil ajustar largura
```

### Padrão CORRETO (usar tcolorbox):
```latex
\usepackage{tcolorbox}  % no preâmbulo

\begin{tcolorbox}[colback=termbg, colframe=termbg,
  boxrule=0pt, arc=3pt,
  left=4pt, right=4pt, top=3pt, bottom=3pt]
  \color{termfg}\ttfamily\footnotesize
  \$ ps aux | grep python\\
  user  1234  0.5  1.2  ...
\end{tcolorbox}

% ✅ Controle fino de padding, sem Overfull
```

### Definir cores no preâmbulo:
```latex
\definecolor{termbg}{RGB}{40,40,40}    % fundo escuro
\definecolor{termfg}{RGB}{220,220,220}  % texto claro
```

### Critério de auditoria:
- Buscar por `\colorbox{.*}{\parbox`
- Se encontrado → `[TÉCNICO LATEX]` `[IMPORTANTE]`

---

## REGRA T5 — \\ DENTRO DE \node EM \draw

**Problema:** Usar `\\` para quebrar linha dentro de um `\node` que está dentro de um comando `\draw` causa erro:
```
! Missing \item inserted.
```

### Padrão PROIBIDO:
```latex
\draw[arr] (a) -- node[above]{Linha 1 \\ Linha 2} (b);

% ❌ Causa "Missing \item"
```

### Padrão CORRETO (opção 1 — node separado com align=center):
```latex
\node[align=center] at ($(a)!0.5!(b)+(0,0.4)$)
  {Linha 1\\Linha 2};
\draw[arr] (a) -- (b);

% ✅ node separado, pode usar \\
```

### Padrão CORRETO (opção 2 — texto em uma linha, preferível):
```latex
\draw[arr] (a) -- node[above]{\small Texto curto} (b);

% ✅ Texto em uma linha só, sem \\
```

### Quando usar cada opção:
- **Opção 1:** Quando label PRECISA ser multilinha (raro)
- **Opção 2:** Sempre que possível (preferível) — usar label curto

### Critério de auditoria:
- Buscar por `\draw.*node.*\\` (regex)
- Se encontrado → `[TÉCNICO LATEX]` `[CRÍTICO]`

---

## REGRA T6 — BABEL NO TEX LIVE 2023+

**Problema:** `\usepackage[spanish]{babel}` causa erro em TeX Live 2023 e posteriores:
```
! Package babel Error: Unknown option 'spanish'
```

### Padrão PROIBIDO:
```latex
\usepackage[spanish]{babel}

% ❌ Erro em TeX Live 2023+
```

### Padrão CORRETO:
```latex
\usepackage[spanish,provide=*]{babel}

% ✅ Funciona em todas as versões
```

### Critério de auditoria:
- Verificar linha de `\usepackage{babel}`
- Se falta `provide=*` → `[TÉCNICO LATEX]` `[CRÍTICO]`

---

## REGRA T7 — COMPILAÇÃO E VERIFICAÇÃO DE OVERFULL

**Enunciado:** Sempre compilar DUAS vezes para TOC correto. Critério de aceitação: zero erros fatais, zero Overfull \hbox ou \vbox > 5pt (exceto falsos positivos de imagem ausente).

### Comando de compilação:
```bash
python scripts/check_lesson_ready.py --class N --compile
```

### Critério de aceitação:
- ✅ Zero erros fatais (`! TeX capacity exceeded`, `! Missing \item`, etc.)
- ✅ Zero Overfull \hbox reais (qualquer valor)
- ✅ Zero Overfull \vbox reais (qualquer valor)
- ✅ Número de páginas estável entre 2ª e 3ª compilação

### Overfull \vbox — Como lidar:
- **Qualquer valor real:** Não usar shrink como solução primária. Resolver a causa: reduzir texto, eliminar `\vspace` entre blocos, simplificar conteúdo.
- Se após redução de conteúdo ainda sobrar ≤ 10pt: `[shrink=2]` a `[shrink=4]` como último recurso.
- Se > 10pt após redução de conteúdo: dividir em dois frames.
- **`\vspace` entre blocos é proibido.** A sombra do bloco Beamer já fornece separação visual suficiente. Remover qualquer `\vspace{Npt}` entre `\end{block}` e `\begin{block}`.

### Overfull \hbox — Como lidar:
- **Qualquer valor real:** Localizar frame e verificar:
  - `\colorbox + \parbox` → aplicar Regra T4 (tcolorbox)
  - Linha de código longa → quebrar com comentário
  - Outro texto longo → reformular com `\small`

### Distinção IMPORTANTE — Overfull de imagem ausente vs. real:
Quando uma imagem não é encontrada, o LaTeX substitui por caixa "draft" com dimensões fixas que não correspondem à imagem real. Isso gera Overfull \vbox grandes (>50pt) que **DESAPARECEM automaticamente** quando os arquivos de imagem estão presentes.

**Como identificar:**
Verificar se o log contém `File 'nome.png' not found: using draft setting` próximo ao número de linha do Overfull.
- Se SIM: falso positivo de layout — NÃO corrigir o .tex por causa do Overfull
  mas verificar separadamente se a imagem ausente era uma figura esperada da aula
- Se NÃO: Overfull real — corrigir conforme critérios acima

### Critério de auditoria:
- Compilar 2x e verificar log
- Se erro fatal → `[TÉCNICO LATEX]` `[CRÍTICO]`
- Se Overfull real >5pt → classificar por tipo e aplicar correção apropriada

---

## ESTRUTURA MÍNIMA DE CADA AULA

Todo arquivo `.tex` deve seguir esta estrutura:

### 1. Preâmbulo (baseado em layout.tex)
```latex
\documentclass[xcolor=svgnames]{beamer}

% Codificação e idioma
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[spanish,provide=*]{babel}  % REGRA T6

% Gráficos, colores e diagramas
\usepackage{xcolor}
\usepackage{graphicx}
\usepackage{tikz}

% Hyperlinks e ajustes de layout
\usepackage{hyperref}
\hypersetup{colorlinks=true, linkcolor=blue}
\usepackage{adjustbox}
\usepackage{calc}

% Símbolos
\usepackage{pifont}
\usepackage{enumitem}
\setbeamertemplate{frametitle continuation}{\relax}

% tcolorbox (se houver blocos de terminal)
\usepackage{tcolorbox}

% booktabs (se houver tabelas)
\usepackage{booktabs}
```

### 2. Tema e paleta (NUNCA DESVIAR)
```latex
\usetheme{Madrid}

\definecolor{mqred}{RGB}{166, 25, 46}
\definecolor{mqdeepred}{RGB}{118, 35, 47}
\definecolor{mqgray}{RGB}{55, 58, 54}
\definecolor{mqlightgray}{RGB}{237, 235, 229}

\usecolortheme[named=mqred]{structure}
\setbeamercolor{title in head/foot}{bg=mqlightgray, fg=mqgray}
\setbeamercolor{author in head/foot}{bg=mqdeepred}
\setbeamercolor{page number in head/foot}{bg=mqdeepred, fg=mqlightgray}
```

### 3. Footline personalizado (3 boxes: 50%-40%-10%)
```latex
\makeatletter
\setbeamertemplate{footline}{
  \leavevmode%
  \hbox{%
    \begin{beamercolorbox}[wd=.5\paperwidth,ht=2.25ex,dp=1ex,center]{author in head/foot}%
      \usebeamerfont{author in head/foot}\insertshortauthor\expandafter\ifblank\expandafter{\beamer@shortinstitute}{}{~~(\insertshortinstitute)}
    \end{beamercolorbox}%
    \begin{beamercolorbox}[wd=.4\paperwidth,ht=2.25ex,dp=1ex,center]{title in head/foot}%
      \usebeamerfont{title in head/foot}\insertshorttitle
    \end{beamercolorbox}%
    \begin{beamercolorbox}[wd=.1\paperwidth,ht=2.25ex,dp=1ex,center]{page number in head/foot}%
      \usebeamerfont{page number in head/foot}\insertframenumber{} / \inserttotalframenumber
    \end{beamercolorbox}%
  }%
  \vskip0pt%
}
\makeatother
\beamertemplatenavigationsymbolsempty
```

### 4. Comandos para imagens
```latex
\newcommand{\imgfill}[1]{%
  \begin{center}
    \adjustbox{max height=0.5\textheight, keepaspectratio}{%
      \includegraphics{#1}%
    }%
  \end{center}
}
```

### 5. Cores adicionais (se necessário)
```latex
% Estados de processo
\definecolor{staterun}{RGB}{39,139,70}    % Ejecutando
\definecolor{staterdy}{RGB}{52,101,164}   % Listo
\definecolor{stateblk}{RGB}{166,25,46}    % Bloqueado
\definecolor{statenew}{RGB}{106,60,140}   % Nuevo
\definecolor{stateend}{RGB}{100,100,100}  % Terminado

% PCB (campos por categoria)
\definecolor{pcbblue}{RGB}{52,101,164}    % gestão de processo
\definecolor{pcbgreen}{RGB}{39,139,70}    % gestão de memória
\definecolor{pcbyellow}{RGB}{180,120,10}  % gestão de arquivos

% Terminal
\definecolor{termbg}{RGB}{40,40,40}       % fundo escuro
\definecolor{termfg}{RGB}{220,220,220}    % texto claro
```

### 6. Metadados
```latex
\title[SO — Unidad N]{\textbf{Sistemas Operativos} \\ 
  \textit{Unidad N, Clase M: Título da aula}}
\author[Rodrigo Fuchs Miranda]{Rodrigo Fuchs Miranda}
\institute[Lic.\ en Ing.\ de Datos e IA]{Licenciatura en 
  Ingeniería de Datos e Inteligencia Artificial}
\date{Dia de mês de 2026}
```

### 7. Corpo do documento
```latex
\begin{document}

% Portada
\begin{frame}
  \titlepage
  \begin{center}
  \vspace{-10pt}
    \includegraphics[height=3.5cm]{logo.jpg}  % ou 2.2cm (decisão pendente)
  \end{center}
\end{frame}

% Índice
\begin{frame}{¿Qué vemos hoy?}
  \tableofcontents
\end{frame}

% Repaso (se aula >1)
\section{Repaso de la clase anterior}
\begin{frame}{Repaso}
  ...
\end{frame}

% Conteúdo principal
\section{Título da seção 1}
\begin{frame}{Título do slide}
  ...
\end{frame}

% Atividade (se houver)
\section{Actividad}
\begin{frame}{Actividad: ...}
  ...
\end{frame}
\begin{frame}{Actividad: respuestas esperadas}
  ...
\end{frame}

% Síntese
\section{Cierre y síntesis}
\begin{frame}{Cierre y síntesis de la clase}
  ...
\end{frame}

% Glosário
\section{Glosario de términos}
\setbeamercolor{glossbox}{bg=lightgrayfill,fg=mqgray}
\newcommand{\glosscard}[2]{%
  \begin{beamercolorbox}[wd=\linewidth,sep=0.8ex,rounded=true,vmode]{glossbox}
    {\color{mqdeepred}\textbf{#1}}\par
    {\footnotesize #2}
  \end{beamercolorbox}
}
\begin{frame}{Glosario | bloque conceptual}
  \begin{columns}[T,onlytextwidth]
    \begin{column}{0.485\textwidth}
      \glosscard{Término 1}{...}
      \glosscard{Término 2}{...}
    \end{column}
    \begin{column}{0.485\textwidth}
      \glosscard{Término 3}{...}
      \glosscard{Término 4}{...}
    \end{column}
  \end{columns}
\end{frame}

\end{document}
```

---

## BULLETS (SEMPRE USAR ESTES)

```latex
% Point (bolinha)
\item[\textcolor{mqred}{\ding{228}}] Texto do item

% Check (correto)
\item[\textcolor{mqred}{\ding{51}}] Texto do item

% X (incorreto/não)
\item[\textcolor{mqred}{\ding{55}}] Texto do item

% Numeração manual (substituir enumerate)
\item[\textbf{1.}] Primeiro item
\item[\textbf{2.}] Segundo item
```

---

## LIMITAÇÕES CONHECIDAS

### allowframebreaks não funciona com block/columns/tabular
```latex
\begin{frame}[allowframebreaks]{Título}
  \begin{block}{Bloco}  % ❌ Não funciona
    ...
  \end{block}
\end{frame}
```

**Solução:** Nunca usar `allowframebreaks`. Dividir manualmente em dois frames.

### \onslide<N->{} acumula conteúdo
Se usar `\onslide<1->` e `\onslide<2->` no mesmo slide, o conteúdo de <1-> permanece visível em <2->.

**Solução:** Usar `\only<N>{...}` para conteúdo mutuamente exclusivo.

---

## PROTOCOLO DE DIAGNÓSTICO DE COMPILAÇÃO

Seguir esta sequência exata ao interpretar resultado da compilação. Não tentar corrigir antes de terminar o diagnóstico completo.

### PASSO D1 — Verificar erro fatal
Se o log contém "Fatal error" ou "TeX capacity exceeded":
1. Localizar linha com `l.N \end{frame}` — esse é o frame com problema
2. Ler o frame que TERMINA nessa linha
3. Verificar nesta ordem:
   - Há `\begin{enumerate}`? → aplicar Regra T1
   - Há `\begin{tikzpicture}` como wrapper de imagem? → aplicar Regra T2
   - Há `\\` dentro de `\node` em `\draw`? → aplicar Regra T5
4. Corrigir e recompilar antes de continuar

### PASSO D2 — Classificar Overfull \vbox
Para cada "Overfull \vbox (Xpt too high) detected at line N":
1. Verificar se log contém `File 'nome.png' not found` próximo à linha N
   - SE SIM: falso positivo de layout — NÃO corrigir por Overfull
     mas auditar se a imagem ausente deveria existir como asset final
   - SE NÃO: Overfull real — continuar
2. Identificar frame que termina na linha N
3. Se X ≤ 30pt: adicionar `[shrink=N]` ao frame, N entre 2 e 10
4. Se X > 30pt OU shrink=10 não resolver: dividir em dois frames
5. Glosários: verificar bloco conceitual, densidade útil, estilo em cartões e aplicar Regra T3

### PASSO D3 — Classificar Overfull \hbox
Para cada "Overfull \hbox (Xpt too wide)":
1. Localizar frame e verificar (qualquer valor é para corrigir):
   - `\colorbox + \parbox`? → aplicar Regra T4 (tcolorbox)
   - Linha de código longa? → quebrar com comentário
   - Outro texto longo? → reformular com `\small`

### PASSO D4 — Verificação final
Após resolver todos os itens reais:
1. Recompilar uma terceira vez
2. Verificar número de páginas estável entre 2ª e 3ª compilação
3. Confirmar: zero erros fatais, zero Overfull reais (qualquer valor)

---

## REGRA T8 — CÓDIGO COPIÁVEL: SEM NUMERAÇÃO, SEM QUEBRAS NOCIVAS, SEM CODIFICAÇÃO QUEBRADA

**Problema:** O estudante copia do PDF para o terminal. Se houver numeração de linhas, mojibake, quebra ruim de linha ou mistura visual com outros elementos, o código deixa de funcionar mesmo estando "certo" no slide.

### Padrão PROIBIDO:
```latex
\lstset{
  numbers=left,          % ❌ Gera numeração que vai junto ao copiar
  numberstyle=\tiny\color{mqgray},
  numbersep=6pt,
}
```

### Padrão CORRETO:
```latex
\lstset{
  numbers=none,          % ✅ Sem numeração — código limpo para copiar
}
```

### Quando aplicar:
- **Sempre** em blocos de código que os estudantes devem executar (Python, bash, etc.)
- O estilo `terminal` já usa `numbers=none` — manter assim
- Preferir **ASCII no código** quando isso evitar problemas de cópia sem perda pedagógica
- Evitar linhas longas que quebrem no PDF e prejudiquem a indentação ou o comando
- Se o código for central ou longo, preferir **arquivo-companheiro** com `\lstinputlisting`
- Para código copiável, preferir **slide de largura total** e evitar colunas com texto explicativo ao lado

### Critério de auditoria:
- Verificar `\lstset` no preâmbulo: se `numbers=left` ou `numbers=right` → `[CÓDIGO NÃO COPIÁVEL]` `[CRÍTICO]`
- Verificar cada `\begin{lstlisting}[...]`: se incluir `numbers=left` individualmente → `[CÓDIGO NÃO COPIÁVEL]` `[CRÍTICO]`
- Verificar se há caracteres quebrados ou extração ruim no PDF → `[CÓDIGO NÃO COPIÁVEL]` `[CRÍTICO]`
- Verificar se há wrapping que atrapalha copiar/colar → `[CÓDIGO NÃO COPIÁVEL]` `[IMPORTANTE]`

---

## REGRA T9 — CÓDIGO COM ANOTAÇÃO PEDAGÓGICA: USAR DUAS COLUNAS

**Problema:** Quando um slide de código usa comentários `#` inline para explicar o que cada trecho faz, linhas curtas (ex: `seguir = True`, `signal.pause()`) deixam ~40% da largura do slide sem uso. Comentários inline também são visualmente inferiores: são cinzas, pequenos e se confundem com o código.

### Padrão PROIBIDO — inline comments como anotação pedagógica:
```latex
\begin{frame}[fragile]{Título}
\begin{lstlisting}[language=Python]
import os       # para obtener el PID
seguir = True   # controla el bucle
signal.pause()  # bloquea sin gastar CPU
\end{lstlisting}
\end{frame}

% ❌ Linhas curtas deixam grande espaço em branco à direita
% ❌ Comentários cinzas são menos legíveis que blocos formatados
```

### Padrão CORRETO — duas colunas: código limpo + blocos de anotação:
```latex
\begin{frame}[fragile]{Título}
  \begin{columns}[T]
    \begin{column}{0.60\textwidth}
      \textbf{Guardalo como:} \texttt{arquivo.py}
\begin{lstlisting}[language=Python, basicstyle=\ttfamily\scriptsize]
import os
import signal

seguir = True

def handler(num, frame):
    global seguir
    seguir = False

signal.signal(signal.SIGTERM, handler)
while seguir:
    signal.pause()
\end{lstlisting}
    \end{column}
    \begin{column}{0.38\textwidth}
      \begin{block}{Importar}
        \scriptsize
        \texttt{os}: obtener PID.\\
        \texttt{signal}: handlers y bloqueo.
      \end{block}
      \begin{block}{Variable de control}
        \scriptsize
        \texttt{seguir = True}: el bucle corre mientras sea verdadero.
      \end{block}
      \begin{block}{Registrar y esperar}
        \scriptsize
        \texttt{signal.signal()}: conecta señal con handler.\\
        \texttt{signal.pause()}: bloquea sin gastar CPU.
      \end{block}
    \end{column}
  \end{columns}
\end{frame}

% ✅ Toda a largura usada: código à esquerda, anotações formatadas à direita
% ✅ Blocos coloridos são muito mais legíveis que comentários cinzas
```

### Quando aplicar:
- Código que o professor explica em aula mas que **NÃO precisa ser copiado** → duas colunas (código esquerda + anotação direita)
- Código que **os estudantes devem copiar e executar** → slide dedicado largura total, sem colunas. Anotações vão no slide SEGUINTE separado.
- Código de terminal → largura total, sem anotações inline

**Razão:** O layout de colunas em PDF dificulta a cópia limpa do código (indentação pode misturar com o texto do lado direito). Para código copiável, slide dedicado é inegociável.

### Proporções recomendadas:
- Coluna código: `0.60\textwidth`
- Coluna anotações: `0.38\textwidth`
- (Soma 0.98, deixando 0.02 de gap entre colunas)

### Comentários `#` inline: apenas para notas técnicas brevíssimas:
```latex
# ✅ Aceitável — uma palavra, nota técnica:
import os      # PID

# ❌ Não usar — use um bloco de anotação à direita:
import os      # para obtener el PID de este proceso y enviarlo al usuario
```

### Critério de auditoria:
- Slide de código com comentários `#` longos (> 3 palavras) e espaço visível em branco à direita → `[COMPOSIÇÃO VISUAL]` `[IMPORTANTE]`
- Slide de código pedagógico sem anotação alguma → `[PROFUNDIDADE INSUFICIENTE]` `[IMPORTANTE]`

---

## RESUMO DAS REGRAS TÉCNICAS

| # | Regra | Problema | Solução |
|---|-------|----------|---------|
| T1 | **enumerate** | grouping levels=255 | `itemize` com labels manuais |
| T2 | **tikzpicture wrapper** | Erro de compilação | `\includegraphics` direto |
| T3 | **Glosário** | Overfull \vbox, slide-apostila ou páginas vazias | Reorganizar em cartões por bloco conceitual |
| T4 | **Terminal** | Overfull \hbox | `tcolorbox` |
| T5 | **\\ em node** | Missing \item | `node` separado com `align=center` |
| T6 | **babel** | Unknown option | `[spanish,provide=*]` |
| T7 | **Compilação** | Overfull, TOC | 2+ compilações, zero erros reais |
| T8 | **código copiável** | Numeração, mojibake ou quebra ruim | `numbers=none`, linhas seguras e arquivo-companheiro se preciso |
| T9 | **inline comments pedagógicos** | Espaço desperdiçado à direita | Duas colunas: código + blocos de anotação |

---

**Estas regras garantem compilação limpa e saída visual correta. Toda auditoria técnica deve verificá-las sistematicamente.**
