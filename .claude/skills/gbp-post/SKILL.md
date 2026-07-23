---
name: gbp-post
description: Gera um rascunho de post para o Google Business Profile (Perfil da Empresa no Google) do Instituto Yumi Kataoka, pronto para colar no painel do Google. Use quando o usuário pedir "/gbp-post", "rascunho de post do Google", "post do Google Meu Negócio", "novo post do perfil da empresa", com tema opcional como argumento.
---

Gera **um rascunho** de post do Google Business Profile por execução. Não publica sozinho:
não há API de publicação conectada neste projeto, então a entrega é sempre um arquivo pronto
para o usuário copiar e colar manualmente no painel do Google (Perfil da Empresa > Postagens).

## Passo 1 — Ler a estratégia

Ler `../../DNA.md` (ou `DNA.md` na raiz do projeto) por inteiro: tom de voz, público
(massoterapeuta, não cliente final), regras específicas do Google Business Profile (tamanho,
tipos de post, CTA, imagem, sem link no corpo), pilares de conteúdo e checklist final.

## Passo 2 — Escolher o tema

Listar os arquivos em `../../posts/` (ou `posts/` na raiz) ordenados por data e olhar os
**2 últimos** publicados: não repetir o mesmo pilar de conteúdo do DNA.md em seguida. Se o
usuário passou um tema/argumento, usar esse tema ajustado ao DNA. Senão, escolher o próximo
pilar da lista seguindo o rodízio. Definir: tipo de post (Novidade/Oferta/Evento), palavra-chave
de intenção, CTA e botão.

## Passo 3 — Escrever o rascunho

Criar `posts/AAAA-MM-DD-slug.md` com esta estrutura:

```markdown
---
data: AAAA-MM-DD
tipo: Novidade | Oferta | Evento
palavra_chave: "..."
cta_botao: "Saiba mais | Ligar agora | Reservar | Comprar | Cadastre-se"
cta_destino: "WhatsApp (11) 98560-4140" ou URL do site
pilar: "<qual dos 6 pilares do DNA>"
---

<corpo do post, 150-300 palavras, seguindo tom de voz do DNA>

---
**Briefing de imagem:** <1-2 linhas descrevendo o que a foto/arte deveria mostrar, proporção 4:3>
```

## Passo 4 — Humanizar

Reler o corpo e eliminar: travessão (proibido no DNA), linguagem de vendedor genérico,
vocabulário de IA ("no cenário atual", "vale ressaltar", "em suma", "desbloqueie", "eleve"),
paralelismos do tipo "não é só X, é Y", promessas de resultado garantido. Variar o tamanho das
frases. O texto deve soar como a Yumi falando com uma colega de profissão.

## Passo 5 — Validar

Conferir contra o checklist do final do DNA.md: 1 palavra-chave só, sem travessão, 150-300
palavras (máx 1500 caracteres), fala com a massoterapeuta (não com cliente de massagem), CTA
claro, tipo de post definido, briefing de imagem presente, pilar diferente dos 2 últimos posts.
Se algo não bater, corrigir antes de entregar.

## Passo 6 — Entregar

Não existe publicação automática configurada. Entregar sempre assim:

1. Confirmar que o arquivo `posts/AAAA-MM-DD-slug.md` foi salvo.
2. Mostrar o corpo do post pronto para copiar.
3. Lembrar o usuário: colar no painel do Google Business Profile em Postagens, escolher o
   tipo de post e o botão de CTA indicados no frontmatter, subir a foto conforme o briefing.
4. Resumir: tema/pilar escolhido, palavra-chave, tipo de post e caminho do arquivo.

Se no futuro uma ferramenta de publicação para Google Business Profile for conectada (API
oficial ou um agregador como Windsor.ai/Metricool), este Passo 6 deve ser atualizado para
publicar direto, mas até lá a entrega é sempre o arquivo de rascunho.
