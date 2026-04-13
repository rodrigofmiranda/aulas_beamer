# /aula-cruzada
## Uso: `/aula-cruzada N M`
## Exemplo: `/aula-cruzada 6 7`

---

Analise as Aulas **{{N}}** e **{{M}}** em conjunto para verificar **consistência, continuidade e separação teoria/lab**.

Localização dos arquivos:
- o `.tex` da Aula {{N}} em `2026-1/`
- o `.tex` da Aula {{M}} em `2026-1/`

---

## OBJETIVO DA AUDITORIA CRUZADA

Verificar que as duas aulas **formam uma sequência pedagógica coerente**, sem:
- Inconsistências terminológicas
- Quebras de continuidade
- Violação de separação teoria/lab
- Termos duplicados em glosários

---

## 4 VERIFICAÇÕES OBRIGATÓRIAS

### 1. CONSISTÊNCIA DE TERMINOLOGIA

**Objetivo:** Os mesmos termos são usados da mesma forma nas duas aulas?

**Como fazer:**
1. Listar todos os termos técnicos usados em ambas as aulas
2. Verificar se há termos definidos de uma forma na Aula {{N}} e usados de forma diferente (ou com nome diferente) na Aula {{M}}

**Formato de saída:**
```
═══════════════════════════════════════════════════════════
1. CONSISTÊNCIA DE TERMINOLOGIA
═══════════════════════════════════════════════════════════

TERMO: Planificador
  Aula {{N}}: "componente del SO que asigna CPU"
  Aula {{M}}: "algoritmo que decide qué proceso ejecutar"
  
  PROBLEMA:
  [CONSISTÊNCIA] Definições diferentes — Aula {{N}} diz 
  "componente", Aula {{M}} diz "algoritmo".
  → Solução: Padronizar como "componente del SO" em ambas.

TERMO: Quantum
  Aula {{N}}: "intervalo de tiempo asignado"
  Aula {{M}}: "intervalo de tiempo asignado"
  
  OK — Consistente
```

**Critério de falha:**
- Termo definido diferente → `[CONSISTÊNCIA]` `[IMPORTANTE]`
- Termo com nome diferente (ex: "cambio de contexto" vs "context switch") → `[CONSISTÊNCIA]` `[IMPORTANTE]`

---

### 2. CONTINUIDADE PEDAGÓGICA

**Objetivo:** A sequência entre as aulas é natural e bem conectada?

**Como fazer:**
1. Verificar se o **slide de síntese da Aula {{N}}** anuncia corretamente o que a **Aula {{M}}** vai ensinar
2. Verificar se o **slide de repaso da Aula {{M}}** retoma corretamente o que foi ensinado na **Aula {{N}}**
3. Verificar se há algum conceito usado na Aula {{M}} que deveria ter sido introduzido na Aula {{N}} mas não foi

**Formato de saída:**
```
═══════════════════════════════════════════════════════════
2. CONTINUIDADE PEDAGÓGICA
═══════════════════════════════════════════════════════════

SÍNTESE DA AULA {{N}} (último slide):
  "Próxima clase: comunicación entre procesos"
  
  AULA {{M}} (tema):
  "Comunicación entre procesos y sincronización"
  
  OK — Anuncia corretamente

REPASO DA AULA {{M}} (slide 3):
  Retoma: estados de proceso, PCB, context switch
  
  AULA {{N}} (conteúdo):
  Ensinou: estados, PCB, context switch ✓
  
  OK — Retoma corretamente

CONCEITO USADO NA AULA {{M}} SEM BASE NA AULA {{N}}:
  Aula {{M}}, Slide 8: usa "sección crítica" sem ter introduzido
  
  PROBLEMA:
  [CONTINUIDADE] [CRÍTICO] Aula {{M}} usa conceito não visto antes.
  → Solução: Adicionar slide na Aula {{M}} definindo "sección 
     crítica" ANTES de usar, OU adicionar ao final da Aula {{N}}.
```

**Critério de falha:**
- Síntese não anuncia próxima aula → `[CONTINUIDADE]` `[MENOR]`
- Repaso não retoma aula anterior → `[CONTINUIDADE]` `[IMPORTANTE]`
- Conceito usado sem ter sido introduzido → `[CONTINUIDADE]` `[CRÍTICO]`

---

### 3. SEPARAÇÃO TEORIA/LAB

**Objetivo:** Se {{N}} é teórica e {{M}} é lab (ou vice-versa), verificar que a separação está correta.

**Como fazer:**
1. Verificar tipo de cada aula (Clase / Lab. Inf)
2. Se {{N}} é teórica e {{M}} é lab:
   - **Todo o conteúdo prático do lab** tem base teórica na Aula {{N}}?
   - Aula {{N}} não tem comandos/terminal/código?
3. Se {{N}} é lab e {{M}} é teórica:
   - Lab não introduziu inadvertidamente **terminologia nova** que vai confundir a Aula {{M}}?

**Formato de saída:**
```
═══════════════════════════════════════════════════════════
3. SEPARAÇÃO TEORIA/LAB
═══════════════════════════════════════════════════════════

Aula {{N}}: Clase teórica
Aula {{M}}: Lab. Inf

VERIFICAÇÃO 1: Lab usa conceitos vistos na teoria?
  Conceitos usados no lab:
    - fork() → ✓ Visto na teoria (Aula {{N}}, Slide 5)
    - PID → ✓ Visto na teoria (Aula {{N}}, Slide 6)
    - Jerarquía → ✓ Visto na teoria (Aula {{N}}, Slide 8)
  
  OK — Todo conceito tem base teórica

VERIFICAÇÃO 2: Teoria não tem comandos?
  Aula {{N}}, Slide 10: menciona "ps aux"
  
  PROBLEMA:
  [SEPARAÇÃO] [CRÍTICO] Aula teórica não pode ter comandos.
  → Solução: Remover comando, apenas mencionar "herramientas 
     como ps" sem ensinar sintaxe.
```

**Critério de falha:**
- Lab usa conceito não visto na teoria → `[SEPARAÇÃO]` `[CRÍTICO]`
- Teoria tem comandos → `[SEPARAÇÃO]` `[CRÍTICO]`
- Lab introduz terminologia nova → `[SEPARAÇÃO]` `[IMPORTANTE]`

---

### 4. GLOSÁRIOS

**Objetivo:** Verificar que termos não estão duplicados e estão no glosário correto.

**Como fazer:**
1. Listar todos os termos nos glosários de ambas as aulas
2. Verificar se há termos duplicados
3. Verificar se termos estão no glosário da aula onde foram introduzidos

**Formato de saída:**
```
═══════════════════════════════════════════════════════════
4. GLOSÁRIOS
═══════════════════════════════════════════════════════════

TERMO: Proceso
  Aula {{N}}, Glosario: ✓ Presente
  Aula {{M}}, Glosario: ✓ Presente
  
  PROBLEMA:
  [GLOSÁRIO] [MENOR] Termo duplicado — "Proceso" já estava 
  no glosário da Aula {{N}}.
  → Solução: Remover de Aula {{M}} (termo já visto antes, 
     não precisa redefinir).

TERMO: Sección crítica
  Aula {{N}}, Glosario: — Ausente
  Aula {{M}}, Glosario: ✓ Presente
  Primeiro uso: Aula {{M}}, Slide 7
  
  OK — Termo no glosário correto (aula onde foi introduzido)

TERMO: Context switch
  Aula {{N}}, Glosario: — Ausente
  Aula {{M}}, Glosario: — Ausente
  Primeiro uso: Aula {{N}}, Slide 9
  
  PROBLEMA:
  [GLOSÁRIO] [IMPORTANTE] Termo introduzido na Aula {{N}} 
  mas não está em nenhum glosário.
  → Solução: Adicionar ao glosário da Aula {{N}}.
```

**Critério de falha:**
- Termo duplicado → `[GLOSÁRIO]` `[MENOR]`
- Termo no glosário errado → `[GLOSÁRIO]` `[IMPORTANTE]`
- Termo faltando no glosário → `[GLOSÁRIO]` `[IMPORTANTE]`

---

## FORMATO DE SAÍDA

Use o mesmo formato de tags do Prompt 3, mas com tipos específicos de auditoria cruzada:
- `[CONSISTÊNCIA]` — Terminologia inconsistente
- `[CONTINUIDADE]` — Conexão entre aulas quebrada
- `[SEPARAÇÃO]` — Violação teoria vs lab
- `[GLOSÁRIO]` — Termo duplicado ou mal posicionado

---

## RESUMO FINAL

```
┌─────────────────────────────────────────────┐
│ AUDITORIA CRUZADA — Aulas {{N}} e {{M}}     │
│                                             │
│ TOTAL DE PROBLEMAS: N                       │
│                                             │
│ [CRÍTICOS]: N                               │
│   — ...                                     │
│                                             │
│ [IMPORTANTES]: N                            │
│   — ...                                     │
│                                             │
│ [MENORES]: N                                │
│   — ...                                     │
│                                             │
└─────────────────────────────────────────────┘

STATUS: AGUARDANDO APROVAÇÃO PARA CORREÇÃO
```

---

## AGUARDAR APROVAÇÃO

**NÃO corrija nada antes de apresentar o relatório.**

**Aguarde aprovação de Rodrigo.**

---

**Este comando verifica a coerência entre aulas consecutivas. Use após concluir duas aulas sequenciais.**
