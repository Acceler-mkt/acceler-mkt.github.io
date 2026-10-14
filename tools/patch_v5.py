# -*- coding: utf-8 -*-
# Dieta de texto: menos palabras por bloque, fuera "alternativas", hero más corto.
import os, re
p=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'index.html')
s=open(p,encoding='utf-8').read(); n=0
def rep(a,b,expect=None):
    global s,n
    c=s.count(a); assert c>0, "NO ENCONTRADO: "+a[:70]
    if expect is not None: assert c==expect, "count %d != %d: %s"%(c,expect,a[:60])
    s=s.replace(a,b); n+=c

# ---------- HERO ----------
rep("Acceler MKT · Marketing con IA para marcas personales y empresas que ya facturan","Acceler MKT · Marketing con IA · Más de 2 años",2)
rep("Acceler MKT · AI-driven marketing for personal brands and companies with revenue","Acceler MKT · AI-driven marketing · 2+ years")
old_lead_es="Si no sabes qué anuncio, qué reel o qué vídeo te ha traído el último cliente, eso es lo que te está pasando. <strong>Nosotros llevamos tus anuncios de Meta, tu contenido y tu YouTube, los producimos con nuestro propio sistema de IA y los medimos hasta la venta. Funcionando en 21 días.</strong>"
new_lead_es="Si no sabes qué anuncio te trajo el último cliente, es esto. <strong>Llevamos tus anuncios, tu contenido y tu YouTube con nuestro sistema de IA, medidos hasta la venta. Funcionando en 21 días.</strong>"
rep(old_lead_es,new_lead_es,2)
old_lead_en="If you can’t say which ad, reel or video brought your last client, that is what is happening to you. <strong>We run your Meta ads, your content and your YouTube, produce them with our own AI system and measure them down to the sale. Up and running in 21 days.</strong>"
new_lead_en="If you can’t say which ad brought your last client, this is it. <strong>We run your ads, your content and your YouTube with our AI system, measured down to the sale. Running in 21 days.</strong>"
rep(old_lead_en,new_lead_en)
rep('<p class="qual" data-i18n="hero.qual">Para marcas personales y empresas que ya facturan. Si empiezas de cero, no somos para ti.</p>\n        ','')
rep('<p class="reassure" data-i18n="hero.reassure">Sin compromiso. Dos plazas por trimestre.</p>','<p class="reassure" data-i18n="hero.reassure">Sin compromiso · Dos plazas por trimestre · Solo marcas que ya facturan</p>')
rep("'hero.reassure':'Sin compromiso. Dos plazas por trimestre.','hero.qual':'Para marcas personales y empresas que ya facturan. Si empiezas de cero, no somos para ti.',","'hero.reassure':'Sin compromiso · Dos plazas por trimestre · Solo marcas que ya facturan',")
rep("'hero.reassure':'No strings. Two spots per quarter.','hero.qual':'For personal brands and companies with revenue. If you are starting from zero, we are not for you.',","'hero.reassure':'No strings · Two spots per quarter · Only brands with revenue',")
rep("gsap.from('.hero .lead, .hero .qual, .hero-cta, .hero .reassure, .proof'","gsap.from('.hero .lead, .hero-cta, .hero .reassure, .proof'")
# fuera las dos mini tarjetas del hero
old_mini="""        <div class="mini">
          <div class="proof-card"><div class="k" data-i18n="proof.k2">En el mercado</div><div class="v" data-i18n="proof.v2">+2 años</div></div>
          <div class="proof-card"><div class="k" data-i18n="proof.k3">Marcas</div><div class="v">13</div></div>
        </div>
"""
rep(old_mini,"")

# ---------- ¿TE SUENA?: solo titulares ----------
rep("""  document.getElementById('pains').innerHTML = PAINS.map((p,i)=>`<div class="pain reveal"><div class="x">0${i+1}</div><h3>${esc(L(p.h))}</h3><p>${esc(L(p.p))}</p></div>`).join('');""",
    """  document.getElementById('pains').innerHTML = PAINS.map((p,i)=>`<div class="pain reveal"><div class="x">0${i+1}</div><h3>${esc(L(p.h))}</h3></div>`).join('');""")
rep(".pain{border:1px solid var(--line2);background:var(--bg2);border-radius:22px;padding:28px 26px;display:grid;gap:12px;align-content:start}",
    ".pain{border:1px solid var(--line2);background:var(--bg2);border-radius:22px;padding:24px 24px;display:grid;gap:10px;align-content:start}")

# ---------- TESIS: dos frases ----------
rep("Las dos cobran por piezas y reportan impresiones. Ninguna se juega nada en tus ventas. Acceler MKT existe para lo contrario: <strong>un sistema de producción con IA que conoce tu negocio, publica cada semana y se mide en lo que entra en caja.</strong> La IA hace el volumen. Nosotros decidimos qué se publica, qué se escala y qué se mata.",
    "Las dos cobran por piezas y reportan impresiones. Acceler MKT existe para lo contrario: <strong>un sistema con IA que conoce tu negocio, publica cada semana y se mide en lo que entra en caja.</strong>",2)
rep("Both charge per piece and report impressions. Neither has anything riding on your sales. Acceler MKT exists for the opposite: <strong>an AI production system that knows your business, publishes every week and is measured by what reaches the bank.</strong> The AI does the volume. We decide what gets published, scaled or killed.",
    "Both charge per piece and report impressions. Acceler MKT exists for the opposite: <strong>an AI system that knows your business, publishes every week and is measured by what reaches the bank.</strong>")

# ---------- RESULTADOS: caso en una línea, sin "qué incluye" ----------
rep("c:{es:'<b>IUVER Academy:</b> 10.000 € en anuncios, 165.000 € facturados en matrículas de un máster de 7.000 €.',en:'<b>IUVER Academy:</b> 10,000 € in ads, 165,000 € billed in enrolments for a 7,000 € master’s.'}",
    "c:{es:'<b>IUVER Academy:</b> 10.000 € en anuncios, 165.000 € facturados.',en:'<b>IUVER Academy:</b> 10,000 € in ads, 165,000 € billed.'}")
rep("c:{es:'<b>GLA Patrimonio:</b> siete piezas a la semana entre Álex y Laura con un formato propio, documentado y repetible.',en:'<b>GLA Patrimonio:</b> seven pieces a week between Álex and Laura in a format of their own, documented and repeatable.'}",
    "c:{es:'<b>GLA Patrimonio:</b> siete piezas a la semana con un formato propio.',en:'<b>GLA Patrimonio:</b> seven pieces a week in a format of their own.'}")
rep("c:{es:'<b>Miguel Sierra:</b> dos vídeos a la semana desde hace años, con sus clips verticales, sin que él toque un programa de edición.',en:'<b>Miguel Sierra:</b> two videos a week for years, vertical clips included, without him touching an editing app.'}",
    "c:{es:'<b>Miguel Sierra:</b> dos vídeos a la semana desde hace años.',en:'<b>Miguel Sierra:</b> two videos a week for years.'}")
rep("""<div class="case">${L(s.c)}</div><div class="inc"><span>${tr('svc.inc')}</span>${esc(L(s.inc))}</div></div>`).join('');""",
    """<div class="case">${L(s.c)}</div></div>`).join('');""")
rep("'svc.lead':'Anuncios, contenido y YouTube trabajando juntos. Cada uno con un caso real detrás; si no hay número, no lo publicamos.',","'svc.lead':'Cada uno con un caso real detrás. Si no hay número, no lo publicamos.',")
rep("'svc.lead':'Ads, content and YouTube working together. Each one with a real case behind it; no number, no publishing.',","'svc.lead':'Each one with a real case behind it. No number, no publishing.',")
rep('<p class="lead reveal" data-i18n="svc.lead">Anuncios, contenido y YouTube trabajando juntos. Cada uno con un caso real detrás; si no hay número, no lo publicamos.</p>','<p class="lead reveal" data-i18n="svc.lead">Cada uno con un caso real detrás. Si no hay número, no lo publicamos.</p>')

# ---------- TRABAJO: 3 piezas a la vista (las largas), el resto en "ver más" ----------
for id_ in ['iuver-ad1','gla-oro','iuver-pinchar','ms-clip-270k','gla-40k']:
    s=re.sub(r"(\{id:'%s'[^\n]*?), first:true"%re.escape(id_), r"\1", s, count=1); n+=1
rep("'work.lead':'Anuncios, reels, vídeos de YouTube y vídeos de venta. Pasa el ratón para verlos en movimiento y haz clic para oírlos.',","'work.lead':'Pasa el ratón para verlos en movimiento y haz clic para oírlos.',")
rep("'work.lead':'Ads, reels, YouTube videos and sales videos. Hover to see them move, click to hear them.',","'work.lead':'Hover to see them move, click to hear them.',")
rep('<p class="lead reveal" data-i18n="work.lead">Anuncios, reels, vídeos de YouTube y vídeos de venta. Pasa el ratón para verlos en movimiento y haz clic para oírlos.</p>','<p class="lead reveal" data-i18n="work.lead">Pasa el ratón para verlos en movimiento y haz clic para oírlos.</p>')

# ---------- CÓMO TRABAJAMOS: una frase por paso + garantía en una línea ----------
rep("p:{es:'Una llamada y tus materiales. Sacamos el contexto: qué vendes, a quién, qué objeciones oyes, qué ha funcionado.',en:'One call and your materials. We extract the context: what you sell, to whom, which objections you hear, what has worked.'}",
    "p:{es:'Una llamada y tus materiales. Sacamos el contexto de tu negocio.',en:'One call and your materials. We extract your business context.'}")
rep("p:{es:'Anuncios, contenido y vídeo salen de nuestro sistema con tu tono y tu marca. Tú apruebas en un calendario, con un clic.',en:'Ads, content and video come out of our system with your tone and your brand. You approve in a calendar, with one click.'}",
    "p:{es:'Anuncios, contenido y vídeo con tu tono. Tú apruebas con un clic.',en:'Ads, content and video in your tone. You approve with one click.'}")
rep("p:{es:'Todo en marcha y un panel semanal con lo que ha traído cada pieza. Lo que no vende se apaga.',en:'Everything running and a weekly panel with what each piece brought in. What doesn’t sell gets switched off.'}",
    "p:{es:'Un panel semanal con lo que trae cada pieza. Lo que no vende se apaga.',en:'A weekly panel with what each piece brings in. What doesn’t sell gets switched off.'}")
rep("fear:{es:'No pagas por piezas: pagas por un sistema que mejora cada semana.',en:'You don’t pay per piece: you pay for a system that improves every week.'}","fear:{es:'Pagas por un sistema, no por piezas.',en:'You pay for a system, not per piece.'}")
rep('<p data-i18n-html="g.p"><strong>Si el día 21 el sistema no está funcionando, te devolvemos la puesta en marcha.</strong> Lo decimos en la web porque lo cumplimos en el contrato.</p>','<p data-i18n-html="g.p"><strong>Si el día 21 el sistema no está funcionando, te devolvemos la puesta en marcha.</strong></p>')
rep("'g.p':'<strong>Si el día 21 el sistema no está funcionando, te devolvemos la puesta en marcha.</strong> Lo decimos en la web porque lo cumplimos en el contrato.',","'g.p':'<strong>Si el día 21 el sistema no está funcionando, te devolvemos la puesta en marcha.</strong>',")
rep("'g.p':'<strong>If the system isn’t running by day 21, we refund the setup.</strong> We say it on the site because it is in the contract.',","'g.p':'<strong>If the system isn’t running by day 21, we refund the setup.</strong>',")
rep('<p class="lead reveal" data-i18n="how.lead">Sin reuniones de tres horas ni calendarios que nadie mira. Cada paso quita un miedo.</p>','<p class="lead reveal" data-i18n="how.lead">Sin reuniones de tres horas.</p>')
rep("'how.lead':'Sin reuniones de tres horas ni calendarios que nadie mira. Cada paso quita un miedo.',","'how.lead':'Sin reuniones de tres horas.',")
rep("'how.lead':'No three-hour meetings, no calendars nobody reads. Every step removes a fear.',","'how.lead':'No three-hour meetings.',")

# ---------- EQUIPO: una línea ----------
rep("p:{es:'Lleva la estrategia, el copy y el criterio, y da la cara en cada llamada. Cofundador de Acceler MKT.',en:'Runs strategy, copy and judgement, and is on every call. Co-founder of Acceler MKT.'}",
    "p:{es:'Estrategia, copy y criterio. Da la cara en cada llamada.',en:'Strategy, copy and judgement. On every call.'}")
rep("p:{es:'Construye los sistemas, las automatizaciones y la plataforma propia. Cofundador y socio técnico.',en:'Builds the systems, the automations and our own platform. Co-founder and technical partner.'}",
    "p:{es:'Sistemas, automatizaciones y la plataforma propia.',en:'Systems, automations and our own platform.'}")
rep("p:{es:'El tercer miembro del equipo. Pone el volumen: anuncios, reels, carruseles y vídeos con tu contexto. Lo que se publica lo decidimos nosotros.',en:'The third team member. Brings the volume: ads, reels, carousels and videos with your context. What gets published is our call.'}",
    "p:{es:'Pone el volumen. Lo que se publica lo decidimos nosotros.',en:'Brings the volume. What gets published is our call.'}")
rep('<p class="lead reveal" data-i18n="team.lead">Nadie te vende al senior para entregarte al becario. Hablas con quien decide y con quien produce.</p>','<p class="lead reveal" data-i18n="team.lead">Nadie te vende al senior para entregarte al becario.</p>')
rep("'team.lead':'Nadie te vende al senior para entregarte al becario. Hablas con quien decide y con quien produce.',","'team.lead':'Nadie te vende al senior para entregarte al becario.',")
rep("'team.lead':'Nobody sells you the senior and hands you the intern. You talk to whoever decides and whoever produces.',","'team.lead':'Nobody sells you the senior and hands you the intern.',")

# ---------- MODELOS: una línea, sin "para quién" ----------
rep("p:{es:'Anuncios, contenido y YouTube, medido en ventas. Un sistema vivo dentro de tu negocio.',en:'Ads, content and YouTube, measured in sales. A living system inside your business.'}","p:{es:'Anuncios, contenido y YouTube, medido en ventas.',en:'Ads, content and YouTube, measured in sales.'}")
rep("p:{es:'Entramos en la pata que te falta y la conectamos con lo que ya tienes.',en:'We take the leg you are missing and connect it to what you already have.'}","p:{es:'Entramos en la pata que te falta.',en:'We take the leg you are missing.'}")
rep("p:{es:'CRM y automatizaciones propias, para cuando el marketing ya funciona y el cuello de botella está dentro.',en:'Our own CRM and automations, for when marketing already works and the bottleneck is inside.'}","p:{es:'CRM y automatizaciones propias, para cuando el cuello de botella está dentro.',en:'Our own CRM and automations, for when the bottleneck is inside.'}")
rep("""<p>${esc(L(m.p))}</p><div class="for"><span>${tr('models.for')}</span>${esc(L(m.f))}</div></div>`).join('');""","""<p>${esc(L(m.p))}</p></div>`).join('');""")
rep('<p class="lead reveal" data-i18n="models.lead">El precio no está en la web: te lo decimos en la primera conversación, con tu caso delante. Abrimos dos plazas por trimestre.</p>','<p class="lead reveal" data-i18n="models.lead">Sin precio en la web: te lo decimos en la primera conversación. Dos plazas por trimestre.</p>')
rep("'models.lead':'El precio no está en la web: te lo decimos en la primera conversación, con tu caso delante. Abrimos dos plazas por trimestre.',","'models.lead':'Sin precio en la web: te lo decimos en la primera conversación. Dos plazas por trimestre.',")
rep("'models.lead':'Pricing is not on the site: we tell you in the first conversation, with your case in front of us. We open two spots per quarter.',","'models.lead':'No pricing on the site: we tell you in the first conversation. Two spots per quarter.',")

# ---------- ALTERNATIVAS: fuera ----------
old_alts_html="""
    <div class="sec-head" style="margin-top:clamp(56px,7vw,96px)">
      <div>
        <span class="eyebrow" data-i18n="alts.eyebrow">Qué harías si no nos contratas</span>
        <h2 class="reveal" data-i18n-html="alts.h2">Las alternativas, <em>sin trampa.</em></h2>
      </div>
    </div>
    <div class="alts reveal" id="alts"></div>
"""
rep(old_alts_html,"\n")
rep("""  document.getElementById('alts').innerHTML = ALTS.map(a=>`<div class="alt${a.us?' us':''}"><h3>${esc(L(a.h))}</h3><p>${L(a.p)}</p></div>`).join('');\n""","")

# ---------- FAQ: corta y con "¿por qué no una agencia?" ----------
i0=s.index("const FAQ = ["); i1=s.index("];",i0)+2
new_faq="""const FAQ = [
  {q:{es:'¿Qué no hacéis?',en:'What don’t you do?'}, a:{es:'Redes por llevarlas, bodas, vídeo institucional y negocios que empiezan de cero.',en:'Social media for its own sake, weddings, corporate films and businesses starting from zero.'}},
  {q:{es:'¿Cuánto tiempo me va a costar a mí?',en:'How much of my time will it take?'}, a:{es:'Una llamada al principio, grabar cuando toca y unos minutos a la semana para aprobar.',en:'One call at the start, recording when it is due and a few minutes a week to approve.'}},
  {q:{es:'¿La IA no hace contenido genérico?',en:'Doesn’t AI make generic content?'}, a:{es:'Lo hace cuando no sabe nada de ti. Nuestro sistema trabaja con tu contexto y el criterio es nuestro.',en:'It does when it knows nothing about you. Ours works with your context, and the judgement is ours.'}},
  {q:{es:'¿Y si no funciona?',en:'What if it doesn’t work?'}, a:{es:'Lo ves en el panel semanal, no a los seis meses. Y si el día 21 no está funcionando, te devolvemos la puesta en marcha.',en:'You see it in the weekly panel, not six months later. And if it isn’t running by day 21, we refund the setup.'}},
  {q:{es:'¿Por qué no un freelance o una agencia?',en:'Why not a freelancer or an agency?'}, a:{es:'Los dos cobran por piezas. Nosotros llevamos un sistema que produce, publica y mide, y no desaparece en agosto.',en:'Both charge per piece. We run a system that produces, publishes and measures, and it doesn’t vanish in August.'}},
  {q:{es:'¿Enseñáis el precio?',en:'Do you show prices?'}, a:{es:'En la primera conversación, con tu caso delante.',en:'In the first conversation, with your case in front of us.'}}
];"""
s=s[:i0]+new_faq+s[i1:]; n+=1

# ---------- CIERRE: una frase ----------
rep('<p class="lead reveal" data-i18n="cta.lead">Cuéntanos qué vendes y qué estás haciendo ahora. Te decimos por WhatsApp si encajamos, qué haríamos y cuándo empezaríamos.</p>','<p class="lead reveal" data-i18n="cta.lead">Cuéntanos qué vendes y te decimos por WhatsApp si encajamos y qué haríamos.</p>')
rep("'cta.lead':'Cuéntanos qué vendes y qué estás haciendo ahora. Te decimos por WhatsApp si encajamos, qué haríamos y cuándo empezaríamos.',","'cta.lead':'Cuéntanos qué vendes y te decimos por WhatsApp si encajamos y qué haríamos.',")
rep("'cta.lead':'Tell us what you sell and what you are doing now. We reply on WhatsApp with whether we fit, what we would do and when we would start.',","'cta.lead':'Tell us what you sell and we reply on WhatsApp with whether we fit and what we would do.',")
rep('<p class="reassure reveal" data-i18n="cta.fit">Sin compromiso. Para marcas personales y empresas que ya facturan. Marketing completo o solo vídeo: dinos qué necesitas.</p>','<p class="reassure reveal" data-i18n="cta.fit">Sin compromiso · Marketing completo o solo vídeo</p>')
rep("'cta.fit':'Sin compromiso. Para marcas personales y empresas que ya facturan. Marketing completo o solo vídeo: dinos qué necesitas.',","'cta.fit':'Sin compromiso · Marketing completo o solo vídeo',")
rep("'cta.fit':'No strings. For personal brands and companies with revenue. Full marketing or video only: tell us what you need.',","'cta.fit':'No strings · Full marketing or video only',")

open(p,'w',encoding='utf-8').write(s); print('reemplazos ok:',n)
