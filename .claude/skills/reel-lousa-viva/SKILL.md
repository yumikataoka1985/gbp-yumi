---
name: reel-lousa-viva
description: Gera o plano de edição completo (decupagem com tempos, layout, legendas, gráficos, B-roll, efeitos sonoros e CTA) de um Reel do Instituto Yumi Kataoka no estilo "Lousa Viva" (tela dividida rosto + lousa animada, legenda palavra por palavra na linha do meio, ritmo de 1-2s por estímulo). Use quando o usuário pedir "/reel-lousa-viva", "editar reel", "plano de edição", "decupagem do reel", "roteiro de edição", ou mandar um roteiro/transcrição/vídeo bruto para editar.
---

Transforma um roteiro, uma transcrição ou um tema em um **plano de edição pronto para executar
no CapCut** (ou Premiere/Canva), seguindo o estilo "Lousa Viva" que a Yumi escolheu a partir
de reels de referência. A análise detalhada das referências está em
`references/analise-referencias.md` (ler antes da primeira execução da sessão).

A skill não edita o vídeo sozinha: entrega um documento de decupagem que a Yumi (ou o editor)
segue tomada por tomada.

## O estilo Lousa Viva em 10 regras

1. **Tela dividida 50/50 do início ao fim.** Metade = Yumi falando para a câmera (plano médio
   curto, corta no peito). Outra metade = "lousa": fundo da marca + gráficos, prints, B-roll.
2. **Posição padrão:** rosto embaixo, lousa em cima. **Inverter** (rosto em cima) a cada
   8-10 segundos, sempre num ponto de virada da fala, para quebrar a fadiga do olho.
3. **Legenda palavra por palavra**, 1 a 3 palavras por vez, branca, bold, sem serifa
   (Montserrat ExtraBold ou Inter Bold), sombra suave, **cravada na linha divisória** entre as
   metades. Palavra-chave do trecho na cor de destaque.
4. **A lousa nunca fica parada mais de 2-3 segundos.** Novo estímulo (card, ícone, número,
   print, checklist, inversão) a cada 1-2 segundos.
5. **Zero silêncio.** Cortar respirações e pausas. Jump cut com punch-in de 10-15% para
   esconder a emenda (alternar 100% e 112%).
6. **Número falado = número animado.** Todo valor (R$, %, horas, clientes) aparece como
   contador subindo, com som de tick.
7. **Conceito abstrato = metáfora visual.** Ex.: "mapa" = trilha pontilhada com pins;
   "invisível no Google" = card de busca vazio que vai se enchendo; "vender experiência x
   sessão" = dois cards lado a lado com ✓ e ✗; "teto de faturamento" = barra de progresso
   batendo numa linha; "corpo como máquina" = ícone de bateria descarregando.
8. **Todo elemento que entra tem som:** whoosh (entrada de card/troca de lousa), pop/click
   (ícone, selo ✓, botão), digitação (barra de busca, chat, planilha), tick (contador).
9. **Trilha lo-fi/corporativa leve**, uns -24 a -28 dB abaixo da voz, com ducking. Voz limpa:
   redução de ruído + compressão + leve reforço de graves/médios.
10. **CTA com cara de interface:** card que imita perfil/botão ("DIAGNÓSTICO", "Chama no
    WhatsApp", "link na bio") enquanto a Yumi aponta. Fim seco, sem tela preta, última frase
    que puxa de volta pro começo (loop).

## Identidade visual da lousa (adaptada para a Yumi)

As referências usam Dark UI (preto + verde neon / amarelo). Para a Yumi, manter a gramática e
trocar a pele:

- **Fundo da lousa:** gradiente escuro (verde-petróleo profundo ou berinjela/vinho, conforme a
  paleta do Instagram @yumikataoka) com textura sutil de pontinhos animada bem devagar.
- **1 cor de destaque só** (ex.: dourado quente ou verde-sálvia vivo) para sublinhados,
  selos ✓, botões e palavra-chave da legenda. Vermelho só para "erro"/✗/carimbo de alerta.
- **Cards:** retângulos escuros translúcidos, cantos bem arredondados, borda fina clara, ícone
  à esquerda. Textos de apoio em pílulas.
- **Fotos e prints** com crédito discreto no canto superior direito quando não forem da Yumi.
- Se a Yumi já tiver um kit de marca definido, ele vence estas sugestões.

## Passo 1 — Ler o contexto

Ler `DNA.md` e `personas.md` na raiz do projeto (tom de voz, Método MAPA, 3 personas, frases
-chave, proibição de travessão). O reel fala **com a profissional** (massoterapeuta,
fisioterapeuta ou dona de spa), nunca com cliente final de massagem. Ler
`references/analise-referencias.md`.

## Passo 2 — Entender o material

O usuário pode mandar:
- **Roteiro ou transcrição** → usar o texto como fala (ajustar só o que quebrar as regras).
- **Só um tema** → escrever o roteiro primeiro (60-110 segundos, ~150-260 palavras faladas),
  com gancho de contraste, 3 blocos de conteúdo e CTA, no tom do DNA. Mostrar o roteiro e
  seguir com o plano de edição na mesma resposta.
- **Vídeo bruto** → se não der para assistir, pedir a transcrição (o CapCut gera
  automaticamente em Legendas > Legendas automáticas).

Definir: persona-alvo, promessa do gancho, a única ideia central, o CTA (padrão: diagnóstico
gratuito / WhatsApp (11) 98560-4140 / link na bio).

## Passo 3 — Montar o gancho (0-3s)

O gancho precisa de **contraste + prova visual** na lousa já no primeiro frame:
- Contador ("R$ 2 mil → R$ 10 mil", "0 clientes do Google → 23 por mês"), ou
- Manchete/print real (avaliação do Google, agenda vazia x agenda cheia, notificação de
  WhatsApp), ou
- Dois cards opostos ✗/✓.

A fala do gancho tem no máximo 12 palavras. Nada de "oi, gente" ou apresentação.

## Passo 4 — Decupar

Quebrar a fala em trechos de 1-3 segundos e, para cada trecho, decidir: posição do rosto
(embaixo/em cima), o que entra na lousa, legenda e palavra destacada, som, zoom. Marcar uma
inversão a cada 8-10s. Garantir pelo menos 1 contador, 1 metáfora visual e 1 checklist ou
comparação ✓/✗ ao longo do vídeo.

## Passo 5 — Escrever o arquivo

Criar `reels/AAAA-MM-DD-slug.md`:

```markdown
---
data: AAAA-MM-DD
estilo: lousa-viva
persona: massoterapeuta | fisioterapeuta | dona-de-spa
duracao_alvo: "XXs"
gancho: "..."
cta: "..."
cor_destaque: "..."
---

## Roteiro (fala)
<texto corrido, sem travessão>

## Decupagem

| Tempo | Rosto | Lousa (gráfico / B-roll / print) | Legenda (destaque em **negrito**) | Som | Zoom |
|---|---|---|---|---|---|
| 0:00-0:01 | embaixo | contador "R$ 2 mil" subindo... | VOCÊ **ATENDE** | tick + whoosh | 100% |
| ... | | | | | |

## Lista de assets para preparar
- Prints / fotos / ícones / cards que precisam ser criados antes de editar.

## Ficha técnica
- Trilha sugerida (estilo + BPM), volume, ducking.
- Fonte, tamanho e cor da legenda; cor de destaque; fundo da lousa.

## Passo a passo no CapCut
<o roteiro de montagem abaixo, ajustado a este vídeo>

## Legenda do post + capa
- Texto do post (curto, sem travessão, 1 CTA), 3-5 hashtags de nicho.
- Capa: frame do gancho com título de até 5 palavras na metade da lousa.
```

## Passo a passo padrão no CapCut (incluir adaptado em cada plano)

1. Projeto 9:16 (1080x1920). Importar o vídeo bruto.
2. Cortar silêncios: *Editar > Remover pausas* (ou cortar à mão), depois revisar.
3. Áudio: *Redução de ruído* ligada, *Aprimorar voz*, volume da voz em 0 dB.
4. Criar a lousa: camada de fundo 1080x960 (imagem/vídeo de fundo da marca) na metade de
   cima; o vídeo da Yumi como sobreposição 1080x960 na metade de baixo (escala ~100-112% e
   corte para enquadrar o peito pra cima).
5. Inversões: nos tempos marcados, dividir o clipe e mover rosto para cima / lousa para baixo
   (duplicar o keyframe de posição, sem transição, corte seco).
6. Jump cuts: em cada emenda, alternar escala 100% e 112%.
7. Gráficos da lousa: textos, stickers, formas e prints como sobreposições, animação de
   entrada "Pop", "Deslizar para cima" ou "Zoom in" (0,2-0,3s). Contadores: texto com animação
   de números, ou 3-4 textos trocando rápido.
8. Legendas: *Legendas automáticas* → estilo bold branco com sombra, 1-3 palavras por bloco
   (dividir os blocos longos), posição Y na linha do meio, palavra-chave na cor de destaque.
   Revisar a ortografia de cada bloco.
9. Sons: biblioteca *Efeitos sonoros* (whoosh, pop, click, typing, tick) alinhados ao frame
   exato da entrada de cada elemento, volume -10 a -15 dB.
10. Trilha: lo-fi/corporate, -24 a -28 dB, fade out nos 2 últimos segundos, sem ultrapassar a
    voz.
11. CTA: card de interface + seta/dedo apontando, entra com pop + click.
12. Exportar 1080p, 30 fps, taxa de bits alta. Conferir no celular com o som desligado (a
    legenda sozinha precisa contar a história).

## Passo 6 — Validar

- [ ] Uma persona só, falando com a profissional (nunca cliente final).
- [ ] Gancho em até 3s com prova visual na lousa.
- [ ] Nenhum trecho da lousa parado mais de 3s; inversão a cada 8-10s.
- [ ] Legenda de 1-3 palavras na linha do meio, sem travessão em nenhum texto na tela.
- [ ] Todo número falado vira contador; pelo menos 1 metáfora visual e 1 ✓/✗ ou checklist.
- [ ] Som em todo elemento que entra; trilha baixa com ducking.
- [ ] Sem promessa de resultado garantido (DNA).
- [ ] CTA com elemento de interface e fim em loop.

## Passo 7 — Entregar

1. Salvar `reels/AAAA-MM-DD-slug.md`.
2. Mostrar o roteiro e a tabela de decupagem na resposta.
3. Listar os assets a preparar antes de abrir o CapCut.
4. Se o usuário quiser guardar o plano no repositório, commitar só o novo arquivo em `reels/`
   com mensagem `reel-lousa-viva: <título>` e dar push na branch atual.
