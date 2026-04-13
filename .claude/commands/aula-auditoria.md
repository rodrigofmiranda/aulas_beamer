# /aula-auditoria
## Uso: `/aula-auditoria N`
## Exemplo: `/aula-auditoria 7`

---

Este arquivo é um **wrapper fino** para evitar divergência entre o fluxo do Claude e o fluxo canônico do projeto.

## FONTE CANÔNICA DESTA ETAPA

Leia e siga integralmente:

- `CLAUDE.md`
- `aula-auditoria.md`
- `docs/criterio_qualidade.md`
- `memoria_projeto.md` (quando existir)

## INSTRUÇÕES

1. Execute o fluxo completo definido em `aula-auditoria.md` para a Aula **{{N}}**.
2. Rode as checagens mecânicas pedidas no fluxo canônico antes da auditoria humana.
3. Se houver qualquer conflito entre este wrapper e os arquivos canônicos, **vale o arquivo canônico**.
4. Entregue o relatório consolidado com tags e severidade.
5. Não corrigir ainda; finalize em **"aguardando aprovação para correção"**.

## REGRA DE MANUTENÇÃO

Novas regras desta etapa devem ser adicionadas em `aula-auditoria.md`, não aqui.
