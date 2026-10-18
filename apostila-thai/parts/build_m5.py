"""Gera as páginas do Módulo 5 (manobras da aula) dentro de apostila.html,
entre os marcadores <!-- M5-START --> e <!-- M5-END -->."""
import html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from manobras import SECOES

APOSTILA = os.path.join(HERE, '..', 'apostila.html')
PRINTS = os.path.join(HERE, '..', 'prints')
TEMPOS = os.path.join(HERE, 'tempos.json')  # {"01": "12:34", ...} opcional

FOOT = '  <div class="foot"><span>Módulo 05 · Manobras</span><b class="pn"></b></div>\n</section>\n'
e = html.escape


def card(no, pos, m, tempos):
    nome, tc, cli, ter, reg, fer, obj, cui, passos = m
    tc = tempos.get(no, tc)
    img = f'prints/manobra-{no}.jpg'
    foto = (f'<img src="{img}" alt="{e(nome)}">' if os.path.exists(os.path.join(PRINTS, f'manobra-{no}.jpg'))
            else ('Foto da manobra' if tc.startswith('Livro') else 'Print do vídeo'))
    tag = tc if tc.startswith('Livro') else (f'Vídeo {tc}' if tc != '--:--' else 'Aula ao vivo')
    li = ''.join(f'<li>{e(p)}</li>' for p in passos)
    return f'''  <div class="mv">
    <div class="mv-head"><span class="no">{no}</span><span class="nm"><small>{e(pos)}</small>{e(nome)}</span><span class="tc">{tag}</span></div>
    <div class="mv-body">
      <div class="mv-photo">{foto}</div>
      <div class="mv-info">
        <dl>
          <dt>Cliente</dt><dd>{e(cli)}</dd>
          <dt>Terapeuta</dt><dd>{e(ter)}</dd>
          <dt>Região</dt><dd>{e(reg)}</dd>
          <dt>Ferramenta</dt><dd>{e(fer)}</dd>
          <dt>Objetivo</dt><dd>{e(obj)}</dd>
          <dt>Cuidados</dt><dd>{e(cui)}</dd>
        </dl>
      </div>
      <div class="mv-steps"><span class="tag">Passo a passo</span><ol>{li}</ol></div>
    </div>
  </div>
'''


def build():
    tempos = json.load(open(TEMPOS)) if os.path.exists(TEMPOS) else {}
    out = [open(os.path.join(HERE, 'm5_intro.html')).read()]
    n = 0
    for _key, titulo, desc, manobras in SECOES:
        cards = []
        for m in manobras:
            n += 1
            cards.append(card(f'{n:02d}', titulo, m, tempos))
        # abertura da seção + primeira ficha na mesma página
        lista = ''.join(f'<li><strong>{i:02d}</strong> {e(m[0])}</li>'
                        for i, m in enumerate(manobras, start=n - len(manobras) + 1))
        out.append(f'''<section class="page">
  <div class="kicker">Módulo 05 · Manobras · {e(titulo)}</div>
  <h2 style="margin-top:0">{e(titulo)}</h2>
  <p>{e(desc)}</p>
  <ul class="clean cols-list">{lista}</ul>
{cards[0]}{FOOT}''')
        for i in range(1, len(cards), 2):
            out.append(f'<section class="page">\n  <div class="kicker">Módulo 05 · Manobras · {e(titulo)}</div>\n'
                       + ''.join(cards[i:i + 2]) + FOOT)
    s = open(APOSTILA).read()
    a, b = '<!-- M5-START -->', '<!-- M5-END -->'
    s = s[:s.index(a) + len(a)] + '\n' + '\n'.join(out) + s[s.index(b):]
    open(APOSTILA, 'w').write(s)
    print('fichas:', n)


if __name__ == '__main__':
    build()
