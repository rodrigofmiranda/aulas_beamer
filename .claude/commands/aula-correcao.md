# /aula-correcao
## Uso: `/aula-correcao N`
## Exemplo: `/aula-correcao 7`

---

Este arquivo é um **wrapper fino** para evitar divergência entre o fluxo do Claude e o fluxo canônico do projeto.

## FONTE CANÔNICA DESTA ETAPA

Leia e siga integralmente:

- `CLAUDE.md`
- `aula-correcao.md`
- `aula-auditoria.md`
- `docs/criterio_qualidade.md`

## INSTRUÇÕES

1. Execute o fluxo completo definido em `aula-correcao.md` para a Aula **{{N}}**.
2. Aplique apenas correções aprovadas por Rodrigo.
3. Use as checagens e a compilação pedidas pelo fluxo canônico.
4. Se houver qualquer conflito entre este wrapper e os arquivos canônicos, **vale o arquivo canônico**.
5. Só encerrar quando a aula estiver sem `[CRÍTICOS]` e com compilação estável.

## REGRA DE MANUTENÇÃO

Novas regras desta etapa devem ser adicionadas em `aula-correcao.md`, não aqui.
