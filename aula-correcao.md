# /aula-correcao
## Uso: `/aula-correcao N`
## Exemplo: `/aula-correcao 7`

---

Aplique TODAS as correções do relatório aprovado da Aula **{{N}}**.

---

## REGRA OPERACIONAL ANTI-RETRABALHO

Durante correções:

1. **Corrigir com delta mínimo**
   - preferir reaproveitar cores, macros, estilos TikZ, blocks e estruturas já existentes
   - não criar elemento novo para ajuste pequeno se o problema puder ser resolvido com o vocabulário visual já presente

2. **Se algo novo for inevitável, criar antes de usar**
   - cor nova -> definir no preâmbulo no mesmo patch
   - macro nova -> definir no mesmo patch
   - pacote novo -> só quando os recursos atuais realmente não bastarem

3. **Não confiar em texto quebrado do terminal**
   - se aparecer mojibake (`Ã¡`, `Ã±`, etc.), verificar o conteúdo real do arquivo antes de montar a substituição

4. **Compilar cedo**
   - se a correção tocar preâmbulo, TikZ, cores, macros, colunas ou blocks, compilar logo após essa correção, antes de continuar para a próxima

Objetivo: evitar erros triviais de compilação e economizar retrabalho durante a fase de correção.

---

## PARA CADA CORREÇÃO, APRESENTE:

1. **Frame e problema original**
2. **Trecho ANTES da correção**
3. **Trecho DEPOIS da correção**
4. **Uma frase explicando por que resolve o problema**

---

## CRITÉRIOS POR TIPO DE CORREÇÃO

### [PROFUNDIDADE INSUFICIENTE]
**Solução:** Adicionar slide dedicado ou expandir com exemplo concreto.

**Importante:** Uma frase a mais NÃO resolve profundidade. Se o conceito merecia mais espaço, dê espaço.

**Exemplo de correção:**
```
PROBLEMA: Slide 5 — PCB com profundidade insuficiente
  Falta responder "como funciona"

ANTES:
\begin{frame}{PCB (Process Control Block)}
  \textbf{PCB:} estructura que contiene información del proceso.
\end{frame}

DEPOIS:
\begin{frame}{PCB: ¿qué información almacena?}
  \textbf{PCB (Process Control Block):} estructura que contiene 
  toda la información necesaria para administrar un proceso.
  
  \textbf{Campos principales:}
  \begin{itemize}
    \item \textbf{PID:} identificador único del proceso
    \item \textbf{Estado:} Nuevo, Listo, Ejecutando, etc.
    \item \textbf{Registros:} contenido de registros de CPU
    \item \textbf{Prioridad:} importancia relativa del proceso
    \item \textbf{Memoria:} punteros a espacio de direcciones
  \end{itemize}
\end{frame}

EXPLICAÇÃO: Agora responde "o que é" + "como funciona" 
(quais campos) + "para que serve" (administrar proceso).
```

---

### [ATIVIDADE IRRESOLVÍVEL]
**Solução:** Ajustar enunciado para especificar o modelo, OU adicionar o conteúdo necessário antes da atividade.

**Exemplo de correção:**
```
PROBLEMA: Slide 10 — Atividade sem modelo especificado

ANTES:
\textbf{Ejercicio:} Describe las transiciones que ocurren...

DEPOIS:
\textbf{Ejercicio:} Usando el modelo de 5 estados (Nuevo, 
Listo, Ejecutando, Bloqueado, Terminado), describe las 
transiciones que ocurren...

EXPLICAÇÃO: Agora estudante sabe qual modelo usar.
```

---

### [RESPOSTA ILEGÍVEL]
**Solução:** Substituir por notação textual plana.

**Exemplo de correção:**
```
PROBLEMA: Slide 11 — Resposta usa notação proibida

ANTES:
Nuevo $\xrightarrow{\text{admitted}}$ Listo

DEPOIS:
El proceso pasa de Nuevo --admitted--> Listo cuando el 
planificador lo acepta en memoria principal.

EXPLICAÇÃO: Notação textual plana + explicação do que aconteceu.
```

---

### [TÉCNICO LATEX]
**Solução:** Consultar `/home/claude/regras_tecnicas_latex.md` (Regras T1–T7) e aplicar o padrão CORRETO correspondente.

**Exemplo de correção (enumerate → itemize):**
```
PROBLEMA: Slide 8 — Uso de \begin{enumerate} causa erro fatal

ANTES:
\begin{enumerate}
  \item Primeiro item
  \item Segundo item
\end{enumerate}

DEPOIS:
\begin{itemize}
  \item[\textbf{1.}] Primeiro item
  \item[\textbf{2.}] Segundo item
\end{itemize}

EXPLICAÇÃO: Regra T1 — enumerate causa "grouping levels=255". 
Substituir por itemize com labels manuais.
```

---

### [OMISSÃO TANENBAUM]
**Solução:** Adicionar o conteúdo ausente como slide novo ou expansão de slide existente.

**Importante:** Manter tom adaptado para principiantes — não copiar do livro, reescrever.

**Exemplo de correção:**
```
PROBLEMA: Slide — Overhead de context switch omitido

SOLUÇÃO: Adicionar novo Slide 8.5

\begin{frame}{Context switch: ¿tiene costo?}
  \textbf{Overhead (costo) del cambio de contexto:}
  \begin{itemize}
    \item Guardar registros del proceso saliente en su PCB
    \item Cargar registros del proceso entrante desde su PCB
    \item Invalidar TLB (Translation Lookaside Buffer)
    \item Actualizar punteros de memoria
  \end{itemize}
  
  \vspace{0.3cm}
  
  \textbf{Implicación:} el SO debe minimizar cambios de contexto 
  innecesarios para no desperdiciar tiempo de CPU.
\end{frame}

EXPLICAÇÃO: Conceito de overhead agora presente, adaptado 
para nivel principiante.
```

---

### [DISTORÇÃO TANENBAUM]
**Solução:** Corrigir a simplificação preservando a acessibilidade.

**Importante:** Se o conceito correto é mais complexo, usar analogia melhor em vez de simplificar demais.

**Exemplo de correção:**
```
PROBLEMA: Slide 6 — PCB simplificado demais ("solo PID y estado")

ANTES:
El PCB contiene el PID y el estado del proceso.

DEPOIS:
El PCB contiene toda la información necesaria para administrar 
el proceso:
\begin{itemize}\small
  \item \textbf{Identificación:} PID, usuario
  \item \textbf{Estado:} Nuevo, Listo, Ejecutando, etc.
  \item \textbf{CPU:} registros, contador de programa
  \item \textbf{Memoria:} punteros, tabla de páginas
  \item \textbf{E/S:} archivos abiertos, dispositivos
  \item \textbf{Planificación:} prioridad, tiempos de CPU
\end{itemize}

EXPLICAÇÃO: Lista ampliada mas ainda acessível. Tanenbaum 
lista ~10 campos, não 2.
```

---

### [PROGRESSÃO QUEBRADA]
**Solução:** Reordenar os slides OU adicionar slide de transição.

**Importante:** Se exemplo precisa vir antes de exercício, mova-o — nunca deixe exercício sem exemplo que o prepara.

**Exemplo de correção:**
```
PROBLEMA: Exemplo DEPOIS da atividade

ANTES:
Slide 10: Atividade
Slide 11: Exemplo

DEPOIS:
Slide 10: Exemplo
Slide 11: Atividade

EXPLICAÇÃO: Exemplo agora vem ANTES, preparando o estudante 
para resolver a atividade.
```

---

### [ANALOGIA PROBLEMÁTICA]
**Solução:** Substituir por analogia mais precisa OU adicionar frase que corrija impressão errada.

**Exemplo de correção:**
```
PROBLEMA: Analogia de "proceso como programa pausado" 
  sugere que só há um processo

ANTES:
Proceso es como un programa que está pausado.

DEPOIS:
Proceso es un programa en ejecución. En un instante dado, 
puede estar usando la CPU (Ejecutando), esperando su turno 
(Listo), o esperando un evento (Bloqueado). Múltiples procesos 
coexisten en memoria al mismo tiempo.

EXPLICAÇÃO: Analogia corrigida para evitar impressão de que 
só há um processo.
```

---

### [SLIDE SEM COESÃO]
**Solução:** Identificar a ideia central do slide e reescrever os itens para que todos sustentem essa ideia.

**Importante:** Se há mais de dois conceitos novos, dividir em dois slides.

**Exemplo de correção:**
```
PROBLEMA: Slide 7 — Lista de fatos sem ideia central

ANTES:
\begin{frame}{Varios conceptos}
  \begin{itemize}
    \item PCB almacena información
    \item Context switch tiene costo
    \item Los procesos tienen prioridad
  \end{itemize}
\end{frame}

DEPOIS:
% Dividir em dois slides com foco claro

\begin{frame}{PCB: toda la información del proceso}
  \textbf{PCB:} estructura que contiene toda la información...
  (explicação focada em PCB)
\end{frame}

\begin{frame}{Context switch: cambiar de proceso tiene costo}
  \textbf{Context switch:} cuando el SO cambia de proceso...
  (explicação focada em overhead)
\end{frame}

EXPLICAÇÃO: Slides agora têm foco claro, um conceito por slide.
```

---

## APÓS TODAS AS CORREÇÕES: COMPILAR

### Comando de compilação:
```bash
# Executar a partir da raiz do projeto
python scripts/check_lesson_ready.py --class {{N}} --compile
```

**Observação:** esse comando já compila com `latexmk`, revisa o log e reaproveita a checagem automática de placeholders, assets ausentes e copiabilidade básica do PDF. Se precisar depurar manualmente, usar `latexmk -pdf -interaction=nonstopmode -halt-on-error arquivo.tex`.

---

## PROTOCOLO DE DIAGNÓSTICO DE COMPILAÇÃO

Seguir sequência exata ao interpretar o resultado.

### PASSO D1 — Verificar erro fatal
Se log contém "Fatal error" ou "TeX capacity exceeded":
1. Localizar linha com `l.N \end{frame}`
2. Ler frame que TERMINA nessa linha
3. Verificar nesta ordem:
   - `\begin{enumerate}` → Regra T1
   - `\begin{tikzpicture}` wrapper → Regra T2
   - `\\` em `\node` dentro de `\draw` → Regra T5
4. Corrigir e recompilar antes de continuar

### PASSO D2 — Classificar Overfull \vbox
Para cada "Overfull \vbox (Xpt too high)":
1. Verificar se log contém `File 'nome.png' not found` próximo
   - SE SIM: falso positivo — NÃO corrigir
   - SE NÃO: Overfull real
2. Se X ≤ 30pt: `[shrink=N]`, N entre 2 e 10
3. Se X > 30pt OU shrink=10 não resolver: dividir em dois frames

### PASSO D3 — Classificar Overfull \hbox
Para cada "Overfull \hbox (Xpt too wide)":
1. Se X ≤ 5pt: aceitável — não corrigir
2. Se X > 5pt:
   - `\colorbox + \parbox` → Regra T4 (tcolorbox)
   - Linha de código longa → quebrar
   - Outro texto longo → `\small`

### PASSO D4 — Verificação final
1. Recompilar uma terceira vez
2. Verificar número de páginas estável
3. Confirmar: zero erros fatais, zero Overfull reais > 5pt
4. Confirmar que `python scripts/check_lesson_ready.py --class {{N}} --compile` não retorna erros mecânicos

---

## CRITÉRIOS DE ACEITAÇÃO FINAL

- ✅ Zero erros fatais
- ✅ Zero Overfull \hbox reais > 5pt
- ✅ Zero Overfull \vbox reais > 5pt (exceto falsos positivos de imagem ausente)
- ✅ Zero erros em `python scripts/check_lesson_ready.py --class {{N}} --compile`
- ✅ PDF gerado com número de páginas estável

---

## ENTREGUE:

1. **Lista de todas as correções de conteúdo** (antes/depois)
2. **Lista de todas as correções pedagógicas** (antes/depois)
3. **Lista de todas as correções técnicas** com Regra T usada
4. **Resultado da compilação final:** warnings reais, nº páginas
5. **O `.tex` corrigido completo**
6. **Status:** "zero warnings reais, N páginas" OU lista de problemas restantes com classificação D1/D2/D3

---

## APÓS A ENTREGA: SEGUNDA AUDITORIA AUTOMÁTICA

**Execute `/aula-auditoria {{N}}` novamente sobre o arquivo corrigido.**

O processo está completo **apenas quando** a segunda auditoria retornar **zero `[CRÍTICOS]`** em todos os seis passos.

Se ainda houver `[CRÍTICOS]`, repita `/aula-correcao {{N}}` até eliminá-los.

---

## ATUALIZAR MEMORIA DO PROJETO

Ao concluir (zero `[CRÍTICOS]` + compilação limpa), atualizar `/home/claude/memoria_projeto.md`:

- Adicionar linha na tabela "Aulas concluídas"
- Registrar novos termos padronizados (se houver)
- Registrar erros encontrados e corrigidos (se padrão novo)
- Adicionar notas livres relevantes (decisões, aprendizados)

---

**Este comando fecha o ciclo. Aula concluída quando zero `[CRÍTICOS]` + compilação limpa + memoria atualizada.**
