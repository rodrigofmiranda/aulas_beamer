# regras_pedagogicas.md — Regras pedagógicas (1 a 8)

Estas regras valem para TODAS as aulas, sem exceção. São obrigatórias e inegociáveis.

---

## REGRA 1 — PROTOCOLO DE PRIMEIRA APARIÇÃO

**Enunciado:** Todo termo técnico deve ser definido em linguagem simples **NO MESMO SLIDE** onde aparece pela primeira vez.

### O que NÃO vale:
- ❌ Estar só no glosário ao final da aula
- ❌ Ter sido mencionado antes sem definição ("veremos isso depois")
- ❌ Nota prometendo definição no próximo slide
- ❌ Definição oral do professor que não está no slide

### Onde se aplica:
- ✅ Labels de diagramas TikZ
- ✅ Títulos de colunas em tabelas
- ✅ Termos em perguntas de repaso
- ✅ Termos em enunciados de atividade
- ✅ Siglas usadas em qualquer contexto (PCB, E/S, GUI, etc.)
- ✅ Nomes de camadas, conceitos, estados, algoritmos

### Como definir inline:
```latex
% CORRETO — definição inline na primeira aparição
\textbf{PCB (Process Control Block):} estrutura de dados 
que contiene toda la información necesaria para administrar 
un proceso: identificador, estado, registros, prioridad, etc.

% CORRETO — parêntesis imediatamente após o termo
El \textbf{quantum} (intervalo de tiempo asignado a cada 
proceso) determina...

% INCORRETO — termo solto sem definição
El quantum determina cuánto tiempo...  % ❌ O que é quantum?
```

### Exceções:
- Termos já definidos em **aula anterior** não precisam ser redefinidos, mas podem aparecer no repaso
- Conceitos de **conhecimento prévio assumido** (ver `CLAUDE.md`) não precisam redefinição

### Critério de auditoria:
- **Inventário obrigatório:** Listar todos os termos técnicos na ordem de primeira aparição
- Para cada termo, indicar: slide de aparição, slide de definição
- Se slide de aparição ≠ slide de definição → `[CRÍTICO]`

---

## REGRA 2 — QUATRO PERGUNTAS MÍNIMAS (profundidade)

**Enunciado:** Para cada conceito novo, o conjunto de slides deve permitir que um estudante principiante responda:

1. **O que é?** — Definição clara e acessível
2. **Para que serve?** — Função, propósito, problema que resolve
3. **Como funciona?** — Mecanismo básico (em linhas gerais, sem todos os detalhes)
4. **Quando ou onde aparece na prática?** — Contexto de uso, exemplos cotidianos

### Implicação importante:
Se um conceito é usado em **atividade**, precisa de **exemplo concreto ANTES** da atividade. Uma definição de uma frase não basta se o exercício exige compreensão mais profunda.

### Hierarquia didática obrigatória: conceito nuclear vs. mecanismo de apoio
Nem todo conceito do capítulo merece o mesmo peso no slide.

- **Conceito nuclear:** é a ideia sem a qual o estudante não entende a unidade.
- **Mecanismo de apoio:** é um detalhe, implementação ou caso simples que ajuda a sustentar a ideia principal.

**Regra prática:**
- o conceito nuclear deve aparecer primeiro e com mais espaço didático;
- o mecanismo de apoio deve receber só o detalhe necessário para sustentar a intuição;
- se o mecanismo puder ser reduzido a um exemplo curto sem perda pedagógica, ele **não** deve virar o centro da aula.

**Exemplo típico em memoria:**
- `espacio de direcciones` / `memoria lógica` = **conceito nuclear**
- `registro base` / `registro límite` = **mecanismo de apoio inicial**

Se a aula gastar mais energia explicando o mecanismo do que a abstração que ele sustenta, há erro de priorização pedagógica.

### Exemplo de profundidade insuficiente:
```latex
% ❌ INSUFICIENTE
\textbf{Round Robin:} algoritmo de planificación que asigna 
un quantum a cada proceso.

% (O que é) ✓  
% (Para que serve) ✗  
% (Como funciona) ✗  
% (Onde aparece) ✗  
% → Estudante não consegue resolver exercício sobre Round Robin
```

### Exemplo de profundidade adequada:
```latex
% ✅ ADEQUADO
\textbf{Round Robin:} algoritmo de planificación apropiativa 
que asigna un quantum (intervalo fijo de tiempo) a cada proceso.

\textbf{Para qué sirve:} garantizar que todos los procesos 
reciban tiempo de CPU de forma justa, sin que ninguno monopolice 
el procesador.

\textbf{Cómo funciona:} la cola de procesos listos funciona en 
forma circular. Cada proceso recibe un quantum; si no termina, 
vuelve al final de la cola.

\textbf{Ejemplo:} sistemas interactivos (Linux, Windows) usan 
variantes de Round Robin para atender múltiples usuarios.

% Ahora sí: estudiante puede resolver ejercicio pedindo para 
% aplicar Round Robin en un conjunto de procesos
```

### Critério de auditoria:
- Para cada conceito novo, verificar se as 4 perguntas são respondidas
- Se conceito é usado em atividade mas não tem exemplo antes → `[IMPORTANTE]`
- Se definição é puramente enciclopédica (só "o que é") sem contexto → `[IMPORTANTE]`

---

## REGRA 3 — PROGRESSÃO NARRATIVA (analogia antes de abstração)

**Enunciado:** Nenhum conceito cai do nada. Sequência obrigatória: situação concreta → problema → conceito → exemplo → síntese.

### Estrutura pedagógica de cada slide de conteúdo novo:
1. **Preparação:** Pergunta, situação cotidiana ou conexão com conhecimento prévio
2. **Problema:** Por que esse conceito existe? Que problema resolve?
3. **Conceito:** Definição técnica (após preparação)
4. **Exemplo:** Caso concreto que ilustra o conceito
5. **Síntese:** Fechamento que conecta com o próximo passo

### Padrão PROIBIDO:
```latex
% ❌ Slide começa direto com definição formal, sem preparo
\begin{frame}{Interrupción}
  \textbf{Interrupción:} señal que la CPU recibe de un 
  dispositivo de hardware...
```

### Padrão CORRETO:
```latex
% ✅ Slide prepara terreno antes da definição
\begin{frame}{Interrupciones: ¿cómo el SO atiende dispositivos?}
  \textbf{Situación:} estás escribiendo en Word y llega un 
  correo. ¿Cómo el sistema operativo detecta que llegó el correo 
  sin estar revisando el email constantemente?
  
  \vspace{0.3cm}
  
  \textbf{Solución:} el dispositivo de red envía una 
  \textbf{interrupción} — señal que alerta a la CPU de que 
  hay un evento pendiente.
  
  \textbf{Interrupción:} señal que la CPU recibe de un 
  dispositivo, indicando que necesita atención inmediata.
```

### Frase-puente:
Se a conexão entre dois slides não for óbvia, usar **frase-puente** explícita:
```latex
% ✅ Transição explícita
...
\vspace{0.3cm}
\textbf{Ahora bien,} para que el planificador pueda funcionar, 
necesita información sobre cada proceso. Esta información se 
almacena en el \textbf{PCB}...
```

### Nota off-slide em comentário LaTeX:
Se a fluidez depender da fala do professor, deixar **nota em comentário**:
```latex
% NOTA PARA O PROFESSOR: Perguntar aos estudantes: 
% "¿Qué creen que pasa si el quantum es muy pequeño?"
% Esperar respostas antes de revelar o próximo slide.
```

### Contrastes relacionais precisam dizer “em relação a quê”
Quando um conceito depende de uma relação espacial ou lógica, o slide deve nomear explicitamente o referente.

Exemplos:
- `fragmentación interna` = desperdício **dentro da partición asignada**
- `fragmentación externa` = huecos **fora dos bloques ya ocupados**, espalhados entre particiones/procesos
- `memoria lógica` = vista **do processo**
- `memoria física` = RAM **real da máquina**

**Padrão proibido:**
- dizer apenas “interna” e “externa” sem responder “interna a quê?” / “externa a quê?”
- mostrar dois desenhos separados sem uma legenda que explicite o referente comum

**Padrão correto:**
- usar o mesmo mapa base ou dois mapas paralelos comparáveis
- nomear explicitamente o referente no texto do slide
- idealmente fechar com uma frase-contraste:
  `interna = sobra dentro de una partición ya asignada; externa = huecos libres entre particiones`

### Critério de auditoria:
- Verificar se cada conceito novo tem preparação antes da definição
- Se slide começa com definição sem contexto → `[PROGRESSÃO QUEBRADA]` `[CRÍTICO]`
- Se conexão entre slides não é clara → `[SLIDE SEM COESÃO]` `[IMPORTANTE]`

---

## REGRA 4 — AUTOEXPLICATIVIDADE

**Enunciado:** O slide deve fazer sentido sem improvisação oral. O professor aprofunda, não salva slide mal conectado.

### Implicação:
- Estudante que lê o slide sozinho, sem assistir à aula, deve entender o conteúdo
- Professor pode (e deve) adicionar exemplos, perguntas e discussão oral, mas o slide **não depende** disso para ser compreensível

### Padrão PROIBIDO:
```latex
% ❌ Slide depende da fala do professor para fazer sentido
\begin{frame}{Estados}
  \begin{itemize}
    \item Nuevo
    \item Listo
    \item Ejecutando
    \item Bloqueado
    \item Terminado
  \end{itemize}
\end{frame}

% Problema: estudante não sabe o que esses termos significam 
% apenas lendo essa lista
```

### Padrão CORRETO:
```latex
% ✅ Slide é autoexplicativo
\begin{frame}{Estados de un proceso}
  Un proceso puede estar en uno de estos cinco estados:
  \begin{itemize}
    \item \textbf{Nuevo:} el proceso fue creado, pero aún no 
      está listo para ejecutar.
    \item \textbf{Listo:} esperando ser asignado a la CPU.
    \item \textbf{Ejecutando:} usando la CPU en este momento.
    \item \textbf{Bloqueado:} esperando un evento externo 
      (ej.: lectura de disco).
    \item \textbf{Terminado:} finalizó su ejecución.
  \end{itemize}
\end{frame}

% Agora: estudante entende os estados sem fala do professor
% Professor pode adicionar: "¿Cuántos procesos pueden estar 
% Ejecutando al mismo tiempo en una CPU de un núcleo?"
```

### Critério de auditoria:
- Simular leitura do slide sem contexto oral
- Se slide tem lista de termos sem explicação → `[SLIDE SEM COESÃO]` `[IMPORTANTE]`
- Se slide tem diagrama sem legenda → `[COMPOSIÇÃO VISUAL]` `[IMPORTANTE]`

---

## REGRA 5 — SEPARAÇÃO TEORIA vs LAB

**Enunciado:** Aulas teóricas = zero comandos/terminal/configuração. Aulas de lab = zero conceito novo que não apareceu na teoria.

### Aulas teóricas (tipo "Clase"):
- ❌ Comandos Linux (`ps`, `top`, `kill`, etc.)
- ❌ Código C, Python ou qualquer linguagem
- ❌ Instruções de terminal (`cd`, `ls`, `chmod`)
- ❌ Configuração de sistema (`/etc/fstab`, `systemd`)
- ✅ Conceitos e modelos apenas
- ✅ Pseudocódigo (se necessário para explicar algoritmo)
- ✅ Exemplos narrativos ("un proceso que lee un archivo")

### Aulas de laboratório (tipo "Lab. Inf"):
- ❌ Conceito teórico novo que não foi introduzido em aula teórica anterior
- ❌ Definições formais pela primeira vez
- ❌ Atividade reduzida a copiar, colar e executar sem interpretação
- ✅ Aplicação prática de conceitos já vistos
- ✅ Comandos, código, terminal
- ✅ Exercícios integrados (ECs)
- ✅ Observação de comportamento do sistema
- ✅ Experimentos curtos com previsão, execução, observação e explicação

### Exceção permitida:
- Em aula teórica, pode-se **mencionar** que "en el laboratorio veremos el comando `ps`", mas sem ensinar como usá-lo. Apenas como preview.

### Critério de auditoria:
- Verificar tipo da aula (Clase vs Lab. Inf)
- Se aula teórica contém comandos → `[SEPARAÇÃO]` `[CRÍTICO]`
- Se aula de lab introduz conceito novo não visto na teoria → `[SEPARAÇÃO]` `[CRÍTICO]`
- Se aula de lab vira execução mecânica sem interpretação → `[EXPERIMENTO MECÂNICO]` `[CRÍTICO]`

---

## REGRA 6 — PROTOCOLO DE ATIVIDADES E EXPERIMENTOS

**Enunciado:** O enunciado deve especificar EXPLICITAMENTE qual modelo ou conceito usar. Respostas em notação textual plana. Tempo máximo: 15 minutos.

### Especificação obrigatória no enunciado:
```latex
% ✅ CORRETO — modelo especificado
\textbf{Ejercicio:} Usando el modelo de 5 estados (Nuevo, 
Listo, Ejecutando, Bloqueado, Terminado), describe las 
transiciones que ocurren cuando...

% ❌ INCORRETO — modelo não especificado
\textbf{Ejercicio:} Describe las transiciones que ocurren 
cuando... 
% Estudante não sabe qual modelo usar
```

### Notação de respostas esperadas:
```latex
% ✅ CORRETO — notação textual plana
Estado --etiqueta--> Estado
Ejemplo: Listo --scheduler asigna CPU--> Ejecutando

% ❌ PROIBIDO — notação matemática de flechas
\xrightarrow{scheduler asigna CPU}
% Causa erro de compilação e é ilegível para principiantes
```

### Resolubilidade:
- Toda atividade deve ser **resolúvel em 15 minutos máximo**
- Deve usar **apenas conteúdo ensinado nesta aula** (ou em aulas anteriores)
- Se atividade exige conhecimento não ensinado ainda → `[ATIVIDADE IRRESOLVÍVEL]` `[CRÍTICO]`

### Em laboratório, atividade = experimento didático
Todo experimento de lab deve conter estes quatro movimentos:
1. **Prever:** o estudante antecipa o que espera observar
2. **Executar:** roda o código/comando
3. **Observar:** registra a evidência relevante
4. **Explicar ou comparar:** relaciona o observado com o conceito visto

### Ejercicios para casa
Além das atividades feitas em sala, a aula pode e deve fechar com uma pequena bateria de
**ejercicios para casa** quando isso ajudar a consolidar o conteúdo.

**Regra prática:**
- em aulas teóricas, de revisão ou de integração, preferir **2 a 4 ejercicios para casa**
- devem usar apenas **conceitos e modelos já ensinados**
- devem servir como treino adicional, não como introdução de conteúdo novo
- podem misturar identificação/classificação, aplicação de modelo, comparação, justificativa e leitura de diagramas/mapas

**Formato recomendado:**
- 1 slide final ou penúltimo com título `Ejercicios para casa`
- 2 a 4 consignas curtas, claras e independentes
- sem exigir software extra, ambiente especial ou teoria não vista

### Padrão PROIBIDO em lab:
```latex
% ❌ Mecânico demais
\textbf{Tarea:} Copiá el código, ejecutalo y subí una captura.
```

### Padrão CORRETO em lab:
```latex
% ✅ Experimento guiado
\textbf{Predicción:} Antes de ejecutar, indicá qué señal creés
que recibirá cada proceso y en qué orden.

\textbf{Ejecución:} Ejecutá el script.

\textbf{Observación:} Anotá qué salida apareció realmente.

\textbf{Explicación:} Compará el resultado con tu predicción.
```

### Estrutura de atividade (2 slides obrigatórios):
1. **Slide de enunciado:** Especificar modelo, dar contexto, tempo sugerido
2. **Slide de respostas esperadas:** Solução completa usando notação já ensinada

### Observação importante
`Ejercicios para casa` **não substituem** a atividade principal da aula quando ela for necessária.
Eles entram como extensão de treino, especialmente em aulas de revisão, integração ou fechamento.

### Exemplo completo:
```latex
% Slide 1 — Enunciado
\begin{frame}{Actividad: transiciones de estados}
  \textbf{Contexto:} Un proceso está Ejecutando y solicita 
  leer un archivo del disco.
  
  \textbf{Tarea:} Usando el modelo de 5 estados, describe:
  \begin{itemize}
    \item ¿A qué estado pasa el proceso?
    \item ¿Qué evento provoca el retorno al estado Listo?
  \end{itemize}
  
  \textbf{Tiempo:} 10 minutos
\end{frame}

% Slide 2 — Respuestas esperadas
\begin{frame}{Actividad: respuestas esperadas}
  \textbf{Transiciones:}
  \begin{itemize}
    \item El proceso pasa de Ejecutando --solicita E/S--> Bloqueado
    \item Cuando termina la lectura del disco, pasa de 
      Bloqueado --E/S completa--> Listo
    \item Luego, el planificador puede asignarlo nuevamente: 
      Listo --scheduler asigna CPU--> Ejecutando
  \end{itemize}
\end{frame}
```

### Critério de auditoria:
- Verificar se modelo está especificado no enunciado
- Verificar se slide de resposta usa notação textual plana (não `\xrightarrow`)
- Verificar se atividade é resolúvel em 15min com conteúdo ensinado
- Se falta especificação → `[ATIVIDADE IRRESOLVÍVEL]` `[IMPORTANTE]`
- Se usa notação proibida → `[TÉCNICO LATEX]` `[CRÍTICO]`
- Em lab, verificar se há previsão, observação e explicação
- Se a tarefa se resume a copiar/executar/entregar → `[EXPERIMENTO MECÂNICO]` `[CRÍTICO]`

---

## REGRA 7 — CONTEXTO LIDIA (conexões com a carreira)

**Enunciado:** Quando houver conexão natural com a carreira LIDIA (Ingeniería de Datos e IA), mencionar sem forçar.

### Conexões naturais:
- **Processos CPU-bound:** Treinamento de modelos de ML, processamento de datasets grandes
- **Processos I/O-bound:** Leitura de datasets de disco, requisições a APIs externas
- **Memória:** Datasets carregados em RAM, modelos em memória
- **Sistemas de arquivos:** Armazenamento de datasets, checkpoints de treinamento
- **Virtualização:** Ambientes de treinamento em cloud (AWS, GCP, Azure)
- **Contenedores:** Docker para deployment de modelos

### Exemplo de menção natural:
```latex
% ✅ Conexão natural
\textbf{Ejemplo CPU-bound:} entrenar un modelo de deep learning 
con millones de parámetros. El proceso usa la CPU (o GPU) de 
forma continua durante horas.

% ❌ Conexão forçada (evitar)
\textbf{Ejemplo:} entrenar un modelo de deep learning... 
(quando o contexto é sobre gerenciamento de disco e não tem 
relação com CPU-bound)
```

### Quando NÃO forçar:
- Se o exemplo cotidiano for mais claro que o exemplo de IA/dados, usar o cotidiano
- Nunca inventar conexão artificial só para mencionar LIDIA

### Critério de auditoria:
- Verificar se há oportunidades claras de conexão não aproveitadas → `[MENOR]`
- Verificar se há conexão forçada que confunde → `[ANALOGIA PROBLEMÁTICA]` `[IMPORTANTE]`

---

## ESTRUTURA OBRIGATÓRIA DE CADA AULA

Toda aula deve seguir esta sequência:

1. **Portada** — Título, docente, data, logo UTEC
2. **Índice** — `\tableofcontents` (gerado automaticamente)
3. **Repaso** — APENAS termos de aulas anteriores, nenhum termo novo
4. **Conteúdo principal** — Vários slides com progressão lógica (Regra 3)
5. **Atividade** (se houver) — Enunciado + slide de respostas esperadas (Regra 6)
6. **Síntese da aula** — Fechamento que recapitula o que foi visto
7. **Glosário** — Um slide por cada 4–7 termos novos (nunca >7 itens em um slide)

---

## REGRA 8 — GOOGLE CLOUD SHELL COMO AMBIENTE LINUX BASE NOS LABS

**Enunciado:** Em aulas de laboratório que requerem acesso a Linux, usar **Google Cloud Shell** (`shell.cloud.google.com`) como ambiente padrão, pois os estudantes não têm acesso garantido a um Linux nativo.

### Por que esta ferramenta:
- Fornece um Linux real (Debian) acessível direto do navegador
- Python 3 já instalado, sem configuração
- Suporta múltiplas abas de terminal no mesmo ambiente
- Requer apenas conta Gmail e conexão à internet

### Slide obrigatório de setup (todo lab Linux):
Todo lab que usa Linux deve ter um slide de acesso ao Cloud Shell seguindo este padrão:

```latex
\begin{frame}{¿Cómo accedemos al entorno Linux hoy?}
  \begin{columns}[T]
    \begin{column}{0.54\textwidth}
      \small
      \textbf{Usaremos Google Cloud Shell}, una terminal Linux 
      accesible desde el navegador.\\[6pt]
      \begin{block}{Pasos para entrar}
        \small
        \begin{itemize}\setlength\itemsep{4pt}
          \item[\textcolor{mqred}{\textbf{1.}}] Abrí el navegador.
          \item[\textcolor{mqred}{\textbf{2.}}] Ingresá a: 
            \texttt{\textbf{shell.cloud.google.com}}
          \item[\textcolor{mqred}{\textbf{3.}}] Iniciá sesión con 
            tu cuenta Gmail.
          \item[\textcolor{mqred}{\textbf{4.}}] Hacé clic en 
            \textbf{``Start Cloud Shell''}.
          \item[\textcolor{mqred}{\textbf{5.}}] Esperá a que 
            aparezca la terminal.
        \end{itemize}
      \end{block}
    \end{column}
    \begin{column}{0.42\textwidth}
      \begin{exampleblock}{¿Por qué Cloud Shell?}
        \small
        Nos da un Linux real con Python~3 ya instalado,
        sin necesidad de configurar nada.
      \end{exampleblock}
      \vspace{5pt}
      \begin{alertblock}{Necesitás}
        \small
        Conexión a internet \ding{228} Cuenta Gmail 
        \ding{228} Navegador actualizado
      \end{alertblock}
    \end{column}
  \end{columns}
\end{frame}
```

### Referência a múltiplas terminais:
Quando o lab precisar de 2 terminais simultâneos (ex: labs de sinais, semáforos, processos):
- Mencionar explicitamente que "en Google Cloud Shell podés abrir una segunda pestaña desde el menú superior"
- Pode ser no mesmo slide de setup ou em slide separado

### Padrão PROIBIDO:
```latex
% ❌ Vago e inacessível sem Linux nativo
Vamos a usar un Linux real con Python 3.
```

### Critério de auditoria:
- Lab Linux sem slide de setup com `shell.cloud.google.com` → `[SEPARAÇÃO]` `[IMPORTANTE]`
- Lab com "Linux real" sem especificar a ferramenta → `[IMPORTANTE]`

---

## RESUMO DAS 8 REGRAS

| # | Regra | Critério de falha | Gravidade |
|---|-------|-------------------|-----------|
| 1 | **Primeira aparição** | Termo técnico sem definição inline | `[CRÍTICO]` |
| 2 | **Quatro perguntas** | Conceito não responde o que é / para que / como / onde | `[IMPORTANTE]` |
| 3 | **Progressão narrativa** | Definição sem preparo, exemplo após exercício, contraste relacional sem referente explícito | `[CRÍTICO]` |
| 4 | **Autoexplicatividade** | Slide depende de improvisação oral | `[IMPORTANTE]` |
| 5 | **Separação teoria/lab** | Teoria com comandos, lab com conceito novo | `[CRÍTICO]` |
| 6 | **Protocolo de atividades** | Modelo não especificado, notação proibida, >15min | `[CRÍTICO]` |
| 7 | **Contexto LIDIA** | Oportunidade perdida ou conexão forçada | `[MENOR]` |
| 8 | **Google Cloud Shell** | Lab Linux sem slide `shell.cloud.google.com` | `[IMPORTANTE]` |

---

**Estas regras são a espinha dorsal pedagógica do projeto. Toda auditoria começa por verificar o cumprimento delas.**
