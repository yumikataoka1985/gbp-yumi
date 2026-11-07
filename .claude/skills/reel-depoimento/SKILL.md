---
name: reel-depoimento
description: Gera o plano de edição completo de um Reel de DEPOIMENTO de aluna/mentorada do Instituto Yumi Kataoka (modo depoimento do estilo Lousa Viva) - seleção de falas em 4 atos (gancho, antes, virada, depois), decupagem com tempos, lousa "dossiê" da aluna, legendas, sons, zoom, CTA e legenda do post. Use quando o usuário pedir "/reel-depoimento", "modo depoimento", "editar depoimento", "depoimento da aluna", "vídeo de prova social", ou mandar o vídeo/transcrição de uma aluna falando.
---

# Reel Depoimento (modo depoimento da Lousa Viva)

Transforma o vídeo bruto de uma aluna falando (ou a transcrição dele) num **plano de edição
pronto para o CapCut**. Herda toda a gramática da skill `reel-lousa-viva` (tela dividida
50/50, legenda palavra por palavra na linha do meio, lousa com estímulo novo a cada 1-2s,
zero silêncio, som em todo elemento, CTA com cara de interface, fim em loop). Ler
`.claude/skills/reel-lousa-viva/SKILL.md` e `DNA.md` / `personas.md` antes da primeira
execução da sessão.

A skill não edita o vídeo sozinha: entrega a decupagem que a Yumi (ou o editor) segue.

## As 8 regras do modo depoimento

1. **Quem fala é a aluna.** Metade do rosto = aluna. A Yumi aparece no máximo 2-4s no CTA,
   ou não aparece (CTA só com card).
2. **Nunca reescrever a fala da aluna.** Só cortar, reordenar e limpar ("né", "tipo",
   repetições, pausas). Nunca inventar frase que ela não disse. Se faltar um ato, pular.
3. **Estrutura em 4 atos** montada com as melhores frases do bruto, fora da ordem original
   se preciso:
   - **Gancho (0-3s):** a frase de resultado ou virada mais forte (até 12 palavras).
   - **Antes (3-12s):** a dor, na linguagem dela.
   - **Virada (12-33s):** como chegou na Yumi + 1 a 3 ajustes concretos do Método MAPA +
     o medo que não se confirmou.
   - **Depois (33-50s):** resultado (número ou fato) + sentimento hoje.
   - **Fecho + CTA (50-60s):** recado dela para outra profissional + card de diagnóstico +
     corte seco de volta ao gancho (loop).
4. **A lousa é o "dossiê" da aluna:** etiqueta polaroide "Nome · Profissão · Cidade",
   carimbo vermelho "ANTES" e dourado "DEPOIS", checklist "O que mudou" com ✓, cards ✗/✓,
   contador do número dela, prints reais autorizados (agenda, WhatsApp, avaliação Google,
   tabela de preço).
5. **Inversão do rosto a cada 8-10s**, coincidindo com a troca de ato.
6. **Dois ângulos?** Se houver mais de um bruto da mesma gravação, sincronizar pelo áudio e
   alternar ângulos nos cortes no lugar do punch-in 100%/112%.
7. **Sem promessa (DNA):** o resultado é sempre "dela". Todo número na tela vem com a pílula
   "resultado individual da [Nome]". Nada de "você vai ter".
8. **Autorização de imagem** da aluna confirmada antes de publicar (registrar no
   frontmatter).

## Passo 1 — Material

- **Transcrição (ideal):** CapCut > Legendas > Legendas automáticas, copiar o texto (com
  tempos, se possível). Selecionar as frases reais para cada ato e citar o tempo do bruto.
- **Só o vídeo e não dá para assistir/transcrever:** montar o plano com **frases-alvo**
  (F1 a F10, abaixo), descrevendo o tipo de fala a procurar no bruto. Avisar que as falas
  reais entram depois.
- Perguntar só o que faltar e for essencial: nome, profissão (define a persona), cidade,
  números, autorização. Se o usuário disser "faz com o que tem", seguir com placeholders.

## Passo 2 — Frases-alvo (mapa de seleção)

| # | Ato | O que procurar no bruto |
|---|---|---|
| F1 | Gancho | Resultado concreto ou virada em até 12 palavras |
| F2 | Antes | Como era a rotina / dor principal |
| F3 | Antes | Sentimento de estar travada ou perdida |
| F4 | Virada | Como chegou na Yumi / decisão de entrar |
| F5 | Virada | 1º ajuste concreto (preço, Google, posicionamento, clube) |
| F6 | Virada | 2º ajuste concreto |
| F7 | Virada | Medo que ela tinha e não aconteceu |
| F8 | Depois | Número ou fato do resultado |
| F9 | Depois | Sentimento hoje |
| F10 | Fecho | Recado para outra profissional |

Ícones e metáforas por persona:
- **Massoterapeuta:** agenda lotada, card de busca do Google vazio que se enche, etiqueta
  de preço trocando, barra batendo no "teto".
- **Fisioterapeuta:** bateria descarregando (corpo), "sessão" virando "programa", ticket.
- **Dona de spa:** trilha embaralhada virando mapa (direção), clube de bem-estar,
  cadeira vazia virando equipe.

## Passo 3 — Decupagem padrão (60s, adaptar)

| Tempo | Rosto | Lousa | Legenda | Som | Zoom |
|---|---|---|---|---|---|
| 0:00-0:01 | embaixo | carimbo "DEPOIS" + contador de F1 | F1 início | whoosh + tick | 100% |
| 0:01-0:03 | embaixo | etiqueta polaroide da aluna | F1 final, **palavra do resultado** | pop | 112% |
| 0:03-0:09 | embaixo | carimbo "ANTES" + 2 ícones da dor (persona) | F2 | whoosh, pops | alterna |
| 0:09-0:12 | **em cima** | trilha embaralhada com "?" | F3 | whoosh | 100% |
| 0:12-0:16 | em cima | trilha vira mapa "Método MAPA" + etiqueta Yumi mentora | F4 | whoosh + ding | alterna |
| 0:16-0:18 | em cima | checklist vazio "O que mudou" | ponte | click | 100% |
| 0:18-0:27 | **embaixo** | ✓1 (F5), ✓2 (F6), ✓3 ou print | F5, F6 | pop + ding por ✓ | alterna |
| 0:27-0:33 | **em cima** | ✗ medo × ✓ realidade | F7 | whoosh + click | alterna |
| 0:33-0:43 | **embaixo** | "DEPOIS" + contador de F8 + pílula "resultado individual" + barra passando o teto | F8 | tick + ding | 100%→112% |
| 0:43-0:50 | embaixo → **em cima** | ícone de leveza + print autorizado | F9 | pop | alterna |
| 0:50-0:54 | em cima | F10 em pílula dourada | F10 | whoosh | 100% |
| 0:54-0:58 | em cima / Yumi | card perfil + "DIAGNÓSTICO GRATUITO" + "link na bio" + seta | CTA | pop + click | 100% |
| 0:58-1:00 | frame de F1 | carimbo "DEPOIS" (loop) | F1, 1 palavra | whoosh | 112% |

Material curto: cortar ✓3 e o bloco da barra. F8 sem número: trocar contador por cards ✓.

## Passo 4 — Escrever o arquivo

Criar `reels/AAAA-MM-DD-depoimento-<nome>.md` com frontmatter:

```yaml
data: AAAA-MM-DD
estilo: lousa-viva (modo depoimento)
persona: massoterapeuta | fisioterapeuta | dona-de-spa
aluna: "Nome"
duracao_alvo: "45-75s"
gancho: "..."
cta: "Quer o mesmo caminho? Diagnóstico gratuito, link na bio / WhatsApp (11) 98560-4140"
cor_destaque: "dourado quente"
brutos: [links]
autorizacao_imagem: "sim/não + data"
status: "falas reais | frases-alvo"
```

Seções: Roteiro (falas reais com tempo do bruto, ou tabela F1-F10), Decupagem, Lista de
assets, Ficha técnica, Passo a passo no CapCut, Legenda do post + capa.

**Ficha técnica padrão:** trilha lo-fi acolhedora 80-95 BPM a -26 dB com ducking e fade
nos 2s finais; legenda Montserrat ExtraBold branca, sombra, 1-3 palavras, linha do meio,
destaque dourado (vermelho só em "ANTES"/✗); lousa em gradiente verde-petróleo ou vinho com
pontinhos animados; voz com redução de ruído + aprimorar voz + compressão (usar o melhor
áudio entre os brutos).

**Passo a passo no CapCut:** 1) projeto 9:16 1080x1920, importar brutos, sincronizar áudio
se forem ângulos; 2) legendas automáticas e marcadores em F1-F10; 3) montar na ordem dos
atos, gancho primeiro, cortar pausas; 4) lousa 1080x960 em cima, aluna embaixo, inversões
nas trocas de ato; 5) alternar ângulo ou 100%/112% nos cortes; 6) etiqueta, carimbos,
checklist, contadores, prints com Pop/Deslizar 0,2-0,3s; 7) legendas 1-3 palavras, revisar;
8) sons -10 a -15 dB, trilha -26 dB; 9) CTA + loop; 10) exportar 1080p 30fps e conferir no
celular sem som.

**Legenda do post:** "A [Nome] chegou [dor dela]. Hoje [resultado dela]. O que mudou foi o
caminho, não a técnica. Se você se viu na fala dela, o diagnóstico gratuito está no link da
bio." + 3-5 hashtags de nicho. **Capa:** frame da aluna sorrindo + "ANTES x DEPOIS da
[Nome]".

## Passo 5 — Validar

- [ ] Nenhuma fala inventada; só cortes e reordenação.
- [ ] Gancho com resultado em até 3s e etiqueta da aluna até 0:03.
- [ ] 4 atos presentes (ou ato ausente pulado, não inventado).
- [ ] Inversão a cada 8-10s; lousa nunca parada mais de 3s.
- [ ] Todo número com contador + pílula "resultado individual".
- [ ] Nenhum travessão em texto na tela, legenda ou post.
- [ ] Autorização de imagem registrada.
- [ ] CTA com interface e fim em loop.

## Passo 6 — Entregar

Salvar o arquivo, mostrar roteiro e decupagem na resposta, listar os assets, e commitar só
o novo arquivo em `reels/` com `reel-depoimento: <nome>` e push na branch atual.
