# Formação em Thai Massagem Clínica · página de vendas

Página estática (HTML + CSS + um pouco de JavaScript, sem build), no mesmo formato de arquivo
único da landing anterior. As imagens ficam em `assets/img/`.

- `index.html`: a página.
- `assets/img/`: fotos reais do workshop de 18/10/2026 (frames das câmeras e foto RAW da turma),
  retrato e logotipo da Yumi, otimizados em WebP (600/900 px verticais, 800/1350-1600 px horizontais).
- `PENDENCIAS.md`: informações que faltam para fechar a oferta (uso interno).

## Ver localmente

```sh
cd formacao-thai
python3 -m http.server 8000
# abrir http://localhost:8000
```

## Contatos e mensagens do WhatsApp

Todos os botões usam `data-wa` e recebem o texto pronto no script do fim do arquivo:
`geral`, `iniciante` (Trilha B), `profissional` (Trilha A) e `turma` (investimento/calendário).
Para trocar o número ou as mensagens, editar o objeto `msgs` no fim do `index.html`.

## Paleta

Vinho `#3B010E` (fundo principal), off-white `#FAF7F0` (faixas de leitura e topo), dourado
`#BB913A` (botões, divisórias, destaques). Em fundo claro, textos dourados usam `#8A6420` para
manter contraste.
