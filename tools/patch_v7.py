# -*- coding: utf-8 -*-
# Muro de clientes como cuentas de Instagram (avatar + nombre + @usuario, enlazadas).
import os
p=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'index.html')
s=open(p,encoding='utf-8').read(); n=0
def rep(a,b,expect=None):
    global s,n
    c=s.count(a); assert c>0, "NO ENCONTRADO: "+a[:70]
    if expect is not None: assert c==expect, "count %d != %d: %s"%(c,expect,a[:60])
    s=s.replace(a,b); n+=c

i0=s.index("const FACES = ["); i1=s.index("];",i0)+2
new_faces="""const FACES = [
  {img:'f-miguel-sierra.jpg', n:'Miguel Sierra', h:'miguelsierrag'},
  {img:'f-fixcal.jpg', n:'Fixcal', h:'fixcal.asesores'},
  {img:'f-alex-mestres.jpg', n:'Álex Mestres', h:'alexsmestres'},
  {img:'f-gla.jpg', n:'GLA Patrimonio', h:'glapatrimonio'},
  {img:'f-iuver.jpg', n:'IUVER Academy', h:'iuver_academy'},
  {img:'f-dna.jpg', n:'DNA Formación', h:'dnaformacion'},
  {img:'f-liberfy.jpg', n:'Liberfy', h:'liberfy.es'},
  {img:'f-vas.jpg', n:'Zapatos VAS', h:'vas_bootsandshoes'},
  {img:'f-edtuhogar.jpg', n:'ED Tu Hogar', h:'edtuhogar'},
  {img:'f-cesar-rivero.jpg', n:'César Rivero', h:'cesarriveroo'},
  {img:'f-angel-aparicio.jpg', n:'Ángel Aparicio', h:'angelapa_ia'},
  {img:'f-simon.jpg', n:'Simón Hernangómez', h:'simon.hernangomez'},
  {img:'f-miguel-rms.jpg', n:'Miguel RMS', h:'miguelrms'},
  {img:'f-pedro-redes.jpg', n:'Pedro Redes', yt:'https://www.youtube.com/channel/UCnyTiZXykfkpyKa5Vs9jZpw', r:{es:'YouTube',en:'YouTube'}},
  {img:'f-josep-baixas.jpg', n:'Josep Baixas', r:{es:'Coach de montaña',en:'Mountain coach'}}
];"""
s=s[:i0]+new_faces+s[i1:]; n+=1
rep("""  document.getElementById('faces').innerHTML = FACES.map(f=>`<div class="face"><img src="assets/img/${f.img}" alt="${esc(f.n)}" loading="lazy"><div class="n">${esc(f.n)}</div><div class="r">${esc(L(f.r))}</div></div>`).join('');""",
    """  document.getElementById('faces').innerHTML = FACES.map(f=>{
    const inner=`<img src="assets/img/${f.img}" alt="${esc(f.n)}" loading="lazy"><div class="n">${esc(f.n)}</div><div class="r">${f.h?'@'+esc(f.h):esc(L(f.r))}</div>`;
    const url=f.h?`https://www.instagram.com/${f.h}/`:(f.yt||'');
    return url?`<a class="face" href="${url}" target="_blank" rel="noopener">${inner}</a>`:`<div class="face">${inner}</div>`;
  }).join('');""")
rep(".face{display:grid;justify-items:center;gap:10px;width:118px;text-align:center}",
    ".face{display:grid;justify-items:center;gap:8px;width:118px;text-align:center;text-decoration:none;color:inherit}")
rep(".face .r{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;color:var(--mute);line-height:1.3}",
    ".face .r{font-family:var(--mono);font-size:10.5px;letter-spacing:.02em;color:var(--gold);line-height:1.3;word-break:break-all}\n.face img{background:#1b1917}")
rep("'wall.cap':'Con quién trabajamos y hemos trabajado',","'wall.cap':'Cuentas con las que trabajamos y hemos trabajado',")
rep("'wall.cap':'Who we work and have worked with',","'wall.cap':'Accounts we work and have worked with',")
rep('<div class="cap" data-i18n="wall.cap">Con quién trabajamos y hemos trabajado</div>','<div class="cap" data-i18n="wall.cap">Cuentas con las que trabajamos y hemos trabajado</div>')
open(p,'w',encoding='utf-8').write(s); print('reemplazos ok:',n)
