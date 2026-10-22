"""Genera propiedad.html (oferta de lanzamiento «Marketing en propiedad») con el <head> y el CSS de index.html.

Uso: python tools/pagina_propiedad.py
Copy aprobado en Obsidian: 09_Claude_OS/Salidas/2026-10-22 Acceler oferta Marketing en propiedad (lanzamiento).md
Página pública: sin el caso IUVER (solo se usa en privado) y sin precio.
"""
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
idx = (RAIZ / "index.html").read_text(encoding="utf-8")
head = idx[:idx.index("</head>")]
simbolo_wa = re.search(r'<svg width="0" height="0".*?</svg>', idx, re.S).group(0)
logo_svg = re.search(r'<a class="logo" href="#top"[^>]*>(<svg.*?</svg>)', idx, re.S).group(1)

TITULO = "Marketing en propiedad · Acceler MKT"
DESC = ("Tu propio departamento de marketing, instalado en tu empresa en 30 días: anuncios y contenido nuevos cada "
        "semana y una medición que dice qué anuncio trajo cada venta. Sin permanencia. Y es tuyo.")
head = re.sub(r"<title>.*?</title>", f"<title>{TITULO}</title>", head, flags=re.S)
head = re.sub(r'(<meta name="description" content=")[^"]*', rf"\g<1>{DESC}", head)
head = re.sub(r'(<meta property="og:description" content=")[^"]*', rf"\g<1>{DESC}", head)
head = re.sub(r'(<meta name="twitter:description" content=")[^"]*', rf"\g<1>{DESC}", head)
head = re.sub(r'(<meta property="og:title" content=")[^"]*', rf"\g<1>{TITULO}", head)
head = re.sub(r'(<meta name="twitter:title" content=")[^"]*', rf"\g<1>{TITULO}", head)
head = head.replace('href="https://acceler-mkt.github.io/"', 'href="https://acceler-mkt.github.io/propiedad.html"')
head = head.replace('content="https://acceler-mkt.github.io/"', 'content="https://acceler-mkt.github.io/propiedad.html"')
head = re.sub(r'<script type="application/ld\+json">.*?</script>', "", head, flags=re.S)
head += """<style>
.p-hero{padding:150px 0 clamp(56px,7vw,96px);position:relative;overflow:hidden}
.p-hero::before{content:"";position:absolute;inset:-30% -20% auto auto;width:70vw;aspect-ratio:1;border-radius:50%;background:radial-gradient(circle,rgba(222,98,98,.35),rgba(232,160,72,.12) 40%,transparent 68%);filter:blur(20px);pointer-events:none}
.p-hero .wrap{position:relative}
.p-hero h1{font-size:clamp(38px,6vw,88px);max-width:18ch;margin:22px 0 24px}
.cards4{display:grid;gap:14px}
@media(min-width:760px){.cards4{grid-template-columns:repeat(2,minmax(0,1fr))}}
.extras{display:grid;gap:14px;margin-top:14px}
@media(min-width:900px){.extras{grid-template-columns:repeat(3,minmax(0,1fr))}}
.extras .pain h3{font-size:clamp(19px,1.7vw,22px)}
.obien{margin-top:clamp(28px,4vw,48px);display:grid;gap:12px;max-width:62ch}
.obien p{font-size:clamp(19px,1.8vw,24px);line-height:1.45;letter-spacing:-.02em}
.obien p em{font-family:var(--serif);font-style:italic;color:var(--gold)}
.nofor{display:grid;gap:10px;margin-top:8px}
.nofor li{list-style:none;color:var(--mute);font-size:17px;padding-left:26px;position:relative}
.nofor li::before{content:"✕";position:absolute;left:0;color:var(--coral);font-family:var(--mono)}
.ftr{padding:40px 0;border-top:1px solid var(--line2);color:var(--mute);font-size:14px}
.ftr .wrap{display:flex;flex-wrap:wrap;gap:16px 28px;justify-content:space-between;align-items:center}
</style>
"""

WA = "Hola Alfonso, quiero información sobre una de las 5 plazas de Marketing en propiedad. Mi empresa es: "

DOLORES = [
    ("01", "Pagas cada mes y no sabes qué anuncio te trajo la última venta."),
    ("02", "Tus anuncios funcionan un mes y después se queman."),
    ("03", "Te escriben curiosos que no saben ni lo que cuesta lo que vendes."),
    ("04", "Tu agencia te ata un año y lo que hace en tu nombre no es tuyo."),
]
INSTALAMOS = [
    ("El Cerebro del Negocio", "Una IA cargada con tu web, tu temario o tus servicios, tus reseñas y lo que te pregunta tu "
     "cliente en las llamadas. Por eso lo que produce suena a ti y no a una plantilla."),
    ("Motor de anuncios", "Anuncios nuevos cada semana: estáticos, vídeos animados y vídeos editados con tu material. "
     "Lo que vende se repite y lo que no, se apaga."),
    ("Motor de contenido", "Carruseles, reels editados con lo que tu equipo graba con el móvil y vídeos animados, "
     "para publicar todas las semanas sin pensar qué subir."),
    ("Embudo y medición", "Landing, guion del VSL y emails de seguimiento, conectados con tus ventas para que cada "
     "semana veas qué anuncio y qué pieza trajeron cada una."),
]
PASOS = [
    ("01 · Semana 1", "Cargamos tu negocio", "Nos das acceso a lo que ya tienes y lo convertimos en tu Cerebro del "
     "Negocio. Esa misma semana tienes los 10 primeros anuncios."),
    ("02 · Semanas 1 a 3", "Lo ponemos a producir", "Anuncios, contenido y embudo hechos con tu cerebro. Nosotros "
     "revisamos todo antes de que salga."),
    ("03 · Semana 4", "Lo dejamos funcionando contigo", "Medimos qué anuncio trae cada venta y formamos a tu equipo. "
     "Decides si lo lleva él o seguimos nosotros."),
]
EXTRAS = [
    ("Primera tanda en 7 días", "Si los 10 primeros anuncios no llegan en la primera semana, no pagas el resto."),
    ("Sin permanencia", "Después de la instalación, te quedas mientras te sirva."),
    ("Todo es tuyo", "El cerebro, las piezas, las plantillas, la landing y la medición. Si te vas, te lo llevas."),
]
FAQ = [
    ("¿Cuánto cuesta?", "Depende de cuánto material tengáis ya y de si tenéis CRM. Te damos un número cerrado en una "
     "llamada de 20 minutos. Las 5 primeras empresas tienen precio de fundador."),
    ("¿Tengo que grabar mucho?", "No. Con 20 minutos a la semana con el móvil basta, o empezamos con lo que ya "
     "tenéis grabado. Nosotros no grabamos: editamos y producimos."),
    ("¿Qué pasa si dejo de trabajar con vosotros?", "Te quedas con todo: el Cerebro del Negocio vive en tu cuenta, y "
     "las piezas, las plantillas, la landing y la medición son tuyas."),
    ("La IA hace cosas genéricas, ¿no?", "Las hace cuando no sabe nada de ti. Por eso lo primero es cargarla con tu "
     "negocio, y por eso ves los 10 primeros anuncios antes de seguir."),
]


def tarjetas(items, numeradas=True):
    return "".join(f'<div class="pain"><div class="x">{n}</div><h3>{t}</h3></div>' if numeradas else
                   f'<div class="pain"><h3>{n}</h3><p>{t}</p></div>' for n, t in items)


cuerpo = f"""<body>
{simbolo_wa}
<header class="hdr" id="top">
  <div class="wrap">
    <a class="logo" href="index.html" aria-label="Acceler MKT">{logo_svg}<span>acceler mkt<b>.</b></span></a>
    <div class="hdr-right"><a class="btn btn-wa wa-link" href="#" target="_blank" rel="noopener"><svg><use href="#wa"/></svg><span>Hablar por WhatsApp</span></a></div>
  </div>
</header>

<section class="p-hero">
  <div class="wrap">
    <span class="eyebrow">Lanzamiento · 5 plazas con precio de fundador</span>
    <h1>Tu propio departamento de marketing. <em>Instalado en tu empresa en 30 días.</em></h1>
    <p class="lead">Anuncios y contenido nuevos cada semana, hechos con todo lo que sabe tu negocio, y una medición que te dice qué anuncio trajo cada venta. <strong>Sin permanencia. Y es tuyo.</strong></p>
    <div class="hero-cta">
      <a class="btn btn-wa wa-link" href="#" target="_blank" rel="noopener"><svg><use href="#wa"/></svg><span>Quiero una de las 5 plazas</span></a>
      <a class="btn btn-ghost" href="#como">Ver cómo funciona</a>
    </div>
    <p class="reassure">Para negocios de formación, servicios y programas de ticket alto que ya invierten en anuncios</p>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head"><div><span class="eyebrow">¿Te suena?</span><h2>No tienes marketing. <em>Tienes gastos.</em></h2></div></div>
    <div class="pains">{tarjetas(DOLORES)}</div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">Qué instalamos</span><h2>Un departamento de marketing <em>que se queda en tu empresa.</em></h2></div>
      <p class="lead">Una agencia te alquila su trabajo mientras le pagas. Esto se queda contigo.</p>
    </div>
    <div class="cards4">{tarjetas(INSTALAMOS, numeradas=False)}</div>
  </div>
</section>

<section class="section" id="como" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head"><div><span class="eyebrow">Cómo funciona</span><h2>Tres pasos, <em>treinta días.</em></h2></div></div>
    <div class="models">{"".join(f'<div class="model{" hl" if i == 1 else ""}"><div class="k">{k}</div><h3>{h}</h3><p>{p}</p></div>' for i, (k, h, p) in enumerate(PASOS))}</div>
    <div class="guarantee" style="margin-top:clamp(28px,4vw,48px)">
      <div class="d">30<small>Garantía Día 30</small></div>
      <p><strong>Si el día 30 el sistema no está produciendo anuncios y contenido cada semana, te devolvemos la instalación entera.</strong> Solo pedimos los accesos y el material en la primera semana. Va en el contrato.</p>
    </div>
    <div class="extras">{tarjetas(EXTRAS, numeradas=False)}</div>
    <div class="obien">
      <p>O bien en 30 días tienes tu propio departamento de marketing funcionando y sabiendo qué vende, o bien recuperas la instalación <em>y te quedas con todo lo producido.</em></p>
      <p style="color:var(--mute);font-size:clamp(17px,1.5vw,20px)">Piensa en esto como un departamento de marketing entero que no se va de vacaciones, no se lleva lo que sabe cuando se marcha y no te pide un año de permanencia.</p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">Lo que ya hacemos</span><h2>Mira el trabajo <em>antes de hablar.</em></h2></div>
      <p class="lead">Miguel Sierra: 8.000 suscriptores en YouTube en menos de cuatro meses. Carruseles, vídeos y anuncios de las cuentas que llevamos, en nuestra web.</p>
    </div>
    <a class="btn btn-ghost" href="index.html#trabajo">Ver trabajos</a>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head"><div><span class="eyebrow">Para quién no es</span><h2>Mejor decírtelo <em>ahora.</em></h2></div></div>
    <ul class="nofor">
      <li>Negocios que empiezan de cero o que todavía no venden.</li>
      <li>Quien no invierte en anuncios ni quiere hacerlo.</li>
      <li>Quien no quiere enseñarnos sus ventas: sin eso no se puede medir nada.</li>
      <li>Quien busca el más barato o alguien que le suba posts.</li>
    </ul>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head"><div><span class="eyebrow">Preguntas</span><h2>Lo que preguntarías <em>en la llamada.</em></h2></div></div>
    <div class="faq">{"".join(f'<details><summary>{q}</summary><div class="a">{a}</div></details>' for q, a in FAQ)}</div>
  </div>
</section>

<section class="section cta" id="contacto">
  <div class="wrap">
    <div class="box">
      <span class="eyebrow">5 plazas de lanzamiento</span>
      <h2>Tu marketing, <em>en tu casa.</em></h2>
      <p class="lead">Escríbenos qué vendes. Si encajamos, te mandamos un vídeo con lo que cambiaríamos en tus anuncios y tres anuncios nuevos hechos con tu web. Si no encajamos, te lo decimos.</p>
      <div class="cta-row"><a class="btn btn-wa wa-link" href="#" target="_blank" rel="noopener" style="padding:20px 30px;font-size:17px"><svg><use href="#wa"/></svg><span>Quiero una de las 5 plazas</span></a><span class="num">+34 647 82 98 54</span></div>
      <p class="reassure">Las 5 primeras empresas tienen precio de fundador a cambio de poder contar su caso</p>
    </div>
  </div>
</section>

<footer class="ftr"><div class="wrap"><span>acceler mkt<b style="color:var(--coral)">.</b> · Marketing con IA · Tenerife, España</span><span><a href="legal.html">Aviso legal y privacidad</a> · © 2026 Acceler MKT</span></div></footer>
<a class="wa-float wa-link" href="#" target="_blank" rel="noopener" aria-label="WhatsApp"><svg><use href="#wa"/></svg></a>
<script>
(function(){{
  var url = 'https://wa.me/34647829854?text=' + encodeURIComponent({WA!r});
  document.querySelectorAll('.wa-link').forEach(function(a){{ a.href = url; }});
  var hdr = document.querySelector('.hdr');
  addEventListener('scroll', function(){{ hdr.classList.toggle('scrolled', scrollY > 40); }}, {{passive:true}});
}})();
</script>
</body>
</html>
"""
(RAIZ / "propiedad.html").write_text(head + "</head>\n" + cuerpo, encoding="utf-8")
print("propiedad.html generada")
