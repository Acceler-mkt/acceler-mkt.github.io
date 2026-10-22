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

TITULO = "Tu Cerebro de Marketing en 7 días · Acceler MKT"
DESC = ("En 7 días instalamos en tu empresa una IA cargada con todo lo que sabe tu negocio, que escribe tus anuncios "
        "como tú, y te entregamos 10 anuncios nuevos hechos con ella. Es tuya. Si no la tienes en 7 días, te devolvemos el dinero.")
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

WA = "Hola Alfonso, quiero mi Cerebro de Marketing. Mi empresa es: "

DOLORES = [
    ("01", "Pagas cada mes y no sabes qué anuncio te trajo la última venta."),
    ("02", "Tus anuncios funcionan un mes y después se queman."),
    ("03", "Te escriben curiosos que no saben ni lo que cuesta lo que vendes."),
    ("04", "Tu agencia te ata un año y lo que hace en tu nombre no es tuyo."),
]
RECIBES = [
    ("Tu Cerebro del Negocio", "Una IA instalada en tu cuenta de Claude, cargada con tu web, tus servicios, tus reseñas "
     "y lo que te preguntan tus clientes. Escribe tus anuncios y tu contenido como lo harías tú."),
    ("10 anuncios nuevos", "Siete estáticos y tres vídeos animados hechos con tu cerebro, con sus textos, listos para "
     "subir a Meta."),
    ("30 minutos contigo", "Repasamos los anuncios y te enseñamos a sacar tú solo textos, guiones y anuncios con tu "
     "cerebro cuando los necesites."),
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
    ("01 · Días 1 y 2", "Cargamos tu negocio", "Nos pasas tu web, tus reseñas, tu material y lo que más te preguntan. "
     "Lo convertimos en tu cerebro y lo dejamos instalado en tu cuenta."),
    ("02 · Días 3 a 6", "Hacemos tus 10 anuncios", "Con tu cerebro sacamos los textos y producimos los estáticos y los "
     "vídeos animados. Nosotros revisamos todo antes de entregártelo."),
    ("03 · Día 7", "Te enseñamos a usarlo", "En 30 minutos repasamos los anuncios y te enseñamos a sacar más tú solo. "
     "Desde ese día, el cerebro trabaja para ti."),
]
EXTRAS = [
    ("Es tuyo desde el día 1", "El cerebro vive en tu cuenta. Aunque no vuelvas a hablar con nosotros, sigue funcionando."),
    ("Sin permanencia", "Es una entrega de 7 días, no una cuota. Si quieres más, lo hablamos después."),
    ("Si sigues, se descuenta", "Si después quieres el departamento completo, lo que pagaste por el cerebro se descuenta."),
]
COMPLETO = [
    ("Anuncios cada semana", "Unos 30 anuncios en el primer mes, probados y renovados cada semana."),
    ("Contenido del mes", "Carruseles, reels editados con lo que grabe tu equipo con el móvil y vídeos animados."),
    ("Embudo", "Una landing, el guion y la edición de un VSL, y emails de seguimiento."),
    ("Medición", "Conectada a tus ventas: cada semana ves qué anuncio trajo cada una."),
]
EXTRAS_COMPLETO = [
    ("Garantía Día 30", "Si el día 30 el sistema no está produciendo cada semana, te devolvemos la instalación."),
    ("Sin permanencia", "Después, te quedas mientras te sirva."),
    ("Todo es tuyo", "Las piezas, las plantillas, la landing y la medición. Si te vas, te lo llevas."),
]
FAQ = [
    ("¿Cuánto cuesta?", "La primera fase es pequeña y la ves funcionar en una semana. Te decimos el número exacto en "
     "una llamada de 20 minutos, cuando sepamos qué material tenéis."),
    ("¿Qué necesito para empezar?", "Tu material en las primeras 48 horas y una cuenta de Claude Pro (unos 20 € al mes). "
     "Si no la tienes, la abrimos contigo."),
    ("¿Tengo que grabar mucho?", "No. Con 20 minutos a la semana con el móvil basta, o empezamos con lo que ya "
     "tenéis grabado. Nosotros no grabamos: editamos y producimos."),
    ("¿Qué pasa si no seguimos después?", "Te quedas con todo: el cerebro vive en tu cuenta y los 10 anuncios son "
     "tuyos."),
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
    <span class="eyebrow">Para negocios que ya invierten en anuncios</span>
    <h1>Tu Cerebro de Marketing. <em>Instalado en tu empresa en 7 días.</em></h1>
    <p class="lead">Una IA cargada con todo lo que sabe tu negocio, que escribe tus anuncios y tu contenido como tú, y 10 anuncios nuevos hechos con ella. <strong>Es tuya. Y si no la tienes en 7 días, te devolvemos el dinero.</strong></p>
    <div class="hero-cta">
      <a class="btn btn-wa wa-link" href="#" target="_blank" rel="noopener"><svg><use href="#wa"/></svg><span>Quiero mi cerebro</span></a>
      <a class="btn btn-ghost" href="#como">Ver cómo funciona</a>
    </div>
    <p class="reassure">Formación, servicios y programas de ticket alto · Sin permanencia</p>
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
      <div><span class="eyebrow">Qué recibes en 7 días</span><h2>Algo que es tuyo <em>y que trabaja desde el primer día.</em></h2></div>
      <p class="lead">Una agencia te alquila su trabajo mientras le pagas. Esto se queda contigo.</p>
    </div>
    <div class="models">{"".join(f'<div class="model"><h3>{h}</h3><p>{p}</p></div>' for h, p in RECIBES)}</div>
  </div>
</section>

<section class="section" id="como" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head"><div><span class="eyebrow">Cómo funciona</span><h2>Tres pasos, <em>siete días.</em></h2></div></div>
    <div class="models">{"".join(f'<div class="model{" hl" if i == 1 else ""}"><div class="k">{k}</div><h3>{h}</h3><p>{p}</p></div>' for i, (k, h, p) in enumerate(PASOS))}</div>
    <div class="guarantee" style="margin-top:clamp(28px,4vw,48px)">
      <div class="d">7<small>días o te devolvemos el dinero</small></div>
      <p><strong>Si en 7 días no tienes tu cerebro funcionando y los 10 anuncios, te devolvemos lo que pagaste.</strong> Solo pedimos tu material en las primeras 48 horas.</p>
    </div>
    <div class="extras">{tarjetas(EXTRAS, numeradas=False)}</div>
    <div class="obien">
      <p>O bien en una semana tienes un sistema tuyo que escribe tus anuncios y 10 anuncios nuevos para probar, <em>o bien recuperas lo que pagaste.</em></p>
      <p style="color:var(--mute);font-size:clamp(17px,1.5vw,20px)">Piensa en esto como contratar a alguien que se ha leído todo tu negocio, escribe como tú y no se va cuando deja de cobrar.</p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">Y si quieres más</span><h2>Tu departamento de marketing, <em>en tu empresa en 30 días.</em></h2></div>
      <p class="lead">Con tu cerebro ya funcionando, montamos el resto: anuncios cada semana, el contenido del mes, el embudo y una medición que dice qué anuncio trajo cada venta. Lo que pagaste por el cerebro se descuenta, y las 5 primeras empresas tienen precio de fundador.</p>
    </div>
    <div class="cards4">{tarjetas(COMPLETO, numeradas=False)}</div>
    <div class="extras">{tarjetas(EXTRAS_COMPLETO, numeradas=False)}</div>
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
      <span class="eyebrow">Empieza por el cerebro</span>
      <h2>Tu marketing, <em>en tu casa.</em></h2>
      <p class="lead">Escríbenos qué vendes. Si encajamos, te mandamos un vídeo con lo que cambiaríamos en tus anuncios y tres anuncios nuevos hechos con tu web. Si no encajamos, te lo decimos.</p>
      <div class="cta-row"><a class="btn btn-wa wa-link" href="#" target="_blank" rel="noopener" style="padding:20px 30px;font-size:17px"><svg><use href="#wa"/></svg><span>Quiero mi cerebro</span></a><span class="num">+34 647 82 98 54</span></div>
      <p class="reassure">7 días · 10 anuncios · Es tuyo · Si no llega, te devolvemos el dinero</p>
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
