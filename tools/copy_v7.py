"""Aplica el copy de la oferta v7 (Sistema Prueba y Escala) a index.html.

Sustituye listas de datos completas (PAINS, MECH, CMP, SERVICES, STEPS, MODELS, FAQ) y claves del
diccionario I18N en español e inglés. Se puede volver a ejecutar: es idempotente.
Copy fuente: Obsidian 09_Claude_OS/Salidas/2026-10-22 Acceler oferta v7 (Prueba y Escala).md
"""
import re
from pathlib import Path

HTML = Path(__file__).resolve().parent.parent / "index.html"

LISTAS = {
"PAINS": """[
  {h:{es:'Tus anuncios se queman en un mes y hacer nuevos cuesta tiempo y dinero.',en:'Your ads burn out in a month and making new ones costs time and money.'}},
  {h:{es:'Publicas a rachas y por orgánico no te entra ni una conversación.',en:'You post in bursts and organic brings in not a single conversation.'}},
  {h:{es:'Pagas Meta cada mes y no sabes qué anuncio te trajo la última venta.',en:'You pay Meta every month and can\\u2019t tell which ad brought your last sale.'}},
  {h:{es:'Ya probaste una agencia y te quemó.',en:'You already tried an agency and got burned.'}}
]""",
"MECH": """[
  {k:{es:'01 · Publicamos cada día',en:'01 · We publish every day'}, h:{es:'Reel diario, trial reels y carruseles',en:'Daily reel, trial reels and carousels'}, p:{es:'Con todo lo que ya sabe tu negocio y tu forma de hablar. Grabas dos horas cada dos semanas y del resto nos encargamos. Nada sale sin pasar nuestra revisión.',en:'With everything your business already knows and the way you talk. You record two hours every two weeks and we handle the rest. Nothing goes out without our review.'}},
  {k:{es:'02 · Escalamos lo que engancha',en:'02 · We scale what hooks'}, h:{es:'Lo ganador pasa a anuncio',en:'Winners become ads'}, p:{es:'Los ganchos que ya han parado el scroll en orgánico se convierten en anuncios y se multiplican en variaciones. Lo que no vende se apaga.',en:'Hooks that have already stopped the scroll organically become ads and get multiplied into variations. What doesn\\u2019t sell gets switched off.'}, hl:true},
  {k:{es:'03 · Lo convertimos en venta',en:'03 · We turn it into sales'}, h:{es:'Embudo montado y medido',en:'A funnel built and measured'}, p:{es:'Landing, un WhatsApp que contesta al momento y emails para quien aún no compra. Cada semana ves qué anuncio y qué pieza trajo cada venta.',en:'Landing page, a WhatsApp that replies instantly and emails for those not buying yet. Every week you see which ad and which piece brought each sale.'}}
]""",
"CMP": """{
  head:{es:['La forma antigua','La nuestra'],en:['The old way','Ours']},
  rows:[
    {es:['Cuatro piezas al mes, a ver qué pasa','Contenido cada día y ganchos probados antes de pagar por ellos'],en:['Four pieces a month, fingers crossed','Content every day and hooks tested before you pay for them']},
    {es:['Anuncios que se queman y nadie renueva','Creatividades nuevas cada semana, sacadas de lo que ya ha funcionado'],en:['Ads that burn out and nobody replaces','New creatives every week, built from what has already worked']},
    {es:['Un informe de clics e impresiones','Un panel semanal con la venta que trajo cada anuncio'],en:['A report of clicks and impressions','A weekly panel with the sale each ad brought']},
    {es:['Leads que esperan horas a que alguien conteste','Un WhatsApp que contesta al momento y emails que hacen el seguimiento'],en:['Leads waiting hours for a reply','A WhatsApp that replies instantly and emails that follow up']},
    {es:['Si no funciona, pagas igual','Retorno y crecimiento pactados por escrito, o seguimos sin cobrar'],en:['If it doesn\\u2019t work, you pay anyway','Return and growth agreed in writing, or we keep working for free']}
  ]
}""",
"SERVICES": """[
  {num:'01', vis:{type:'phone',img:'iuver-ad1.jpg',alt:{es:'Anuncio de Meta de IUVER Academy en un móvil',en:'IUVER Academy Meta ad on a phone'},a:{es:'Lead cualificado · médica',en:'Qualified lead · doctor'},b:{es:'Matrícula · 7.000 €',en:'Enrolment · 7,000 €'}}, h:{es:'Que te compren.',en:'Get bought.'}, sub:{es:'Anuncios de Meta y el embudo hasta la venta',en:'Meta ads and the funnel down to the sale'},
   c:{es:'<b>IUVER Academy:</b> 24.000 € en anuncios, 210.000 € generados. Primera promoción llena: 30 de 30 plazas.',en:'<b>IUVER Academy:</b> 24,000 € in ads, 210,000 € generated. First intake full: 30 out of 30 places.'}},
  {num:'02', vis:{type:'phone',img:'gla-oro.jpg',alt:{es:'Reel de GLA Patrimonio en un móvil',en:'GLA Patrimonio reel on a phone'},a:{es:'«He visto tu reel, ¿podemos hablar?»',en:'“Saw your reel, can we talk?”'},b:{es:'Llamada reservada',en:'Call booked'}}, h:{es:'Que te sigan.',en:'Get followed.'}, sub:{es:'Contenido diario que hace crecer la cuenta',en:'Daily content that grows the account'},
   c:{es:'<b>Álex Mestres · GLA Patrimonio:</b> reels y carruseles cada semana, con un formato propio que ya reconocen sus seguidores.',en:'<b>Álex Mestres · GLA Patrimonio:</b> reels and carousels every week, in a format his followers already recognise.'}},
  {num:'03', vis:{type:'yt',img:'ms-holding.jpg',alt:{es:'Vídeo de YouTube de Miguel Sierra',en:'Miguel Sierra YouTube video'},a:{es:'+8.000 suscriptores',en:'+8,000 subscribers'},b:{es:'Miguel Sierra · YouTube',en:'Miguel Sierra · YouTube'}}, h:{es:'Que te recuerden.',en:'Get remembered.'}, sub:{es:'YouTube y clips de principio a fin',en:'YouTube and clips from start to finish'},
   c:{es:'<b>Miguel Sierra:</b> 8.000 suscriptores en YouTube en menos de 4 meses y decenas de millones de visualizaciones entre vídeos y reels.',en:'<b>Miguel Sierra:</b> 8,000 YouTube subscribers in under 4 months and tens of millions of views across videos and reels.'}}
]""",
"STEPS": """[
  {when:{es:'Semana 1',en:'Week 1'}, h:{es:'Nos cuentas tu negocio',en:'You tell us about your business'}, p:{es:'Una entrevista de una hora y lo que ya tienes: web, temario, reseñas, vídeos y llamadas. Pactamos por escrito los números de la garantía.',en:'A one-hour interview and what you already have: website, syllabus, reviews, videos and calls. We agree the guarantee numbers in writing.'}, fear:{es:'No tienes que preparar nada.',en:'You don’t have to prepare anything.'}},
  {when:{es:'Semana 2',en:'Week 2'}, h:{es:'Grabamos y montamos el embudo',en:'We record and build the funnel'}, p:{es:'Dos horas de grabación, los primeros reels, anuncios, landing, WhatsApp y emails con tu tono. Apruebas con un clic.',en:'Two hours of recording, the first reels, ads, landing page, WhatsApp and emails in your tone. You approve with one click.'}, fear:{es:'Sin reuniones.',en:'No meetings.'}},
  {when:{es:'Semana 3',en:'Week 3'}, h:{es:'Publicamos cada día y medimos',en:'We publish daily and measure'}, p:{es:'Contenido diario, anuncios en marcha y un panel semanal con lo que trae cada pieza. Lo que vende se escala.',en:'Daily content, ads running and a weekly panel with what each piece brings in. What sells gets scaled.'}, fear:{es:'Pagas por resultados, no por piezas.',en:'You pay for results, not pieces.'}}
]""",
"MODELS": """[
  {k:{es:'Es para ti si',en:'It is for you if'}, h:{es:'Ya vendes y quieres vender más',en:'You already sell and want to sell more'}, p:{es:'Vendes formación, un servicio o un programa de más de 1.000 €, ya tienes clientes que han pagado y puedes invertir al menos 1.500 € al mes en anuncios.',en:'You sell training, a service or a programme above 1,000 €, already have paying clients and can invest at least 1,500 € a month in ads.'}, hl:true},
  {k:{es:'Y además',en:'And also'}, h:{es:'Sales en cámara',en:'You show up on camera'}, p:{es:'Tú o alguien de tu equipo, dos horas cada dos semanas. Del resto nos encargamos nosotros.',en:'You or someone on your team, two hours every two weeks. We handle the rest.'}},
  {k:{es:'No es para ti si',en:'It is not for you if'}, h:{es:'Empiezas de cero o solo quieres «redes»',en:'You start from zero or just want “socials”'}, p:{es:'Tampoco si no quieres enseñarnos cuánto vendes: sin eso no podemos pactar ni medir nada.',en:'Nor if you won\\u2019t show us what you sell: without that we can\\u2019t agree or measure anything.'}}
]""",
"FAQ": """[
  {q:{es:'¿Qué garantizáis exactamente?',en:'What exactly do you guarantee?'}, a:{es:'En la puesta en marcha pactamos por escrito dos números con tus datos: el retorno de tus anuncios (ventas entre inversión) y el crecimiento de tu audiencia. Si a los 90 días no llegamos a los dos, seguimos trabajando sin cobrarte la cuota hasta llegar.',en:'At setup we agree two numbers in writing using your data: your ad return (sales divided by spend) and your audience growth. If we haven\\u2019t hit both by day 90, we keep working without charging the fee until we do.'}},
  {q:{es:'¿Y si no funciona?',en:'What if it doesn\\u2019t work?'}, a:{es:'Lo ves en el panel cada semana, no a los seis meses. Si el día 21 el sistema no está funcionando, te devolvemos la puesta en marcha. Si una semana no publicamos lo pactado, esa semana no la pagas. Y todo lo que hacemos es tuyo, también si te vas.',en:'You see it in the panel every week, not six months later. If the system isn\\u2019t running by day 21, we refund the setup. If one week we don\\u2019t publish what we agreed, you don\\u2019t pay that week. And everything we make is yours, even if you leave.'}},
  {q:{es:'¿Tengo que grabar mucho?',en:'Do I have to record a lot?'}, a:{es:'Dos horas cada dos semanas, con un guion que te damos nosotros. De ahí sale un reel cada día, los trial reels, los carruseles y los anuncios.',en:'Two hours every two weeks, with a script we give you. From that comes a reel every day, the trial reels, the carousels and the ads.'}},
  {q:{es:'¿Qué son los trial reels?',en:'What are trial reels?'}, a:{es:'Reels que Instagram enseña solo a gente que no te sigue. Nos dejan probar cada día ganchos nuevos sin quemar tu cuenta: los que funcionan pasan a tu perfil y a tus anuncios.',en:'Reels Instagram only shows to people who don\\u2019t follow you. They let us test new hooks every day without burning your account: the ones that work go to your profile and your ads.'}},
  {q:{es:'¿Hay permanencia?',en:'Is there a minimum term?'}, a:{es:'Tres meses, que son los 90 días de la garantía: es lo que necesitan los anuncios para aprender y tú para ver con datos qué vende.',en:'Three months, the 90 days of the guarantee: it is what the ads need to learn and what you need to see, with data, what sells.'}},
  {q:{es:'Ya tengo agencia.',en:'I already have an agency.'}, a:{es:'Pregúntale qué anuncio te trajo al último cliente y cuántos ganchos ha probado este mes. Si te lo sabe decir, quédate con ella.',en:'Ask them which ad brought your last client and how many hooks they tested this month. If they can tell you, stay with them.'}},
  {q:{es:'Si la IA lo hace casi gratis, ¿por qué pagaros?',en:'If AI does it almost for free, why pay you?'}, a:{es:'Producir ya cuesta poco. Lo que cuesta es saber qué publicar, qué escalar y qué apagar, y responder por el resultado. Por eso nos jugamos la cuota.',en:'Producing is cheap now. What costs is knowing what to publish, what to scale and what to switch off, and answering for the result. That is why we put our fee on the line.'}}
]""",
}

CLAVES = {
"es": {
 "hero.eyebrow": "Para formación, servicios y marcas personales que ya venden",
 "hero.h1": "Contenido cada día. <em>Anuncios que se pagan solos.</em>",
 "hero.lead": "Publicamos cada día para descubrir qué engancha a tus clientes, convertimos lo que funciona en anuncios y lo llevamos hasta la venta con un embudo montado. <strong>En marcha en 21 días. Retorno y crecimiento pactados por escrito, o seguimos sin cobrar.</strong>",
 "hero.cta1": "Quiero mi diagnóstico gratis",
 "hero.reassure": "Gratis: revisamos tus anuncios y te mandamos 3 creatividades · Una empresa nueva por semana",
 "proof.k": "Caso real · Meta Ads",
 "proof.who": "<strong>IUVER Academy</strong> · máster de medicina estética. Primera promoción llena: 30 de 30 plazas.",
 "proof.k2": "Miguel Sierra · YouTube",
 "proof.v2": "+8.000 suscriptores en menos de 4 meses",
 "res.eyebrow": "Resultados",
 "res.h2": "Lo que pasa cuando el contenido <em>alimenta los anuncios.</em>",
 "pain.eyebrow": "¿Te suena?",
 "pain.h2": "No tienes marketing. <em>Tienes gastos.</em>",
 "tesis.h3": "Meta funciona y lo que vendes se vende. <em>El problema es que pruebas demasiado poco.</em>",
 "tesis.p": "Una agencia te hace cuatro piezas al mes y espera a ver qué pasa. Así se tarda un año en dar con el anuncio que vende. <strong>Nosotros publicamos cada día y probamos ganchos sin parar</strong>, con todo lo que ya sabe tu negocio: tu web, tu temario, tus reseñas y lo que te preguntan tus clientes. Con IA, el volumen deja de ser un coste.",
 "mech.eyebrow": "El Sistema Prueba y Escala",
 "mech.h2": "Publicamos cada día. <em>Escalamos lo que vende.</em>",
 "mech.lead": "Tres movimientos con nuestro sistema de IA y el criterio de dos personas que deciden qué sale.",
 "svc.h2": "Tres resultados, <em>con nombre y número.</em>",
 "svc.lead": "Que te compren, que te sigan y que te recuerden. Así se ve en cuentas reales.",
 "how.h2": "De tu negocio a ventas, <em>en tres semanas.</em>",
 "g.k": "días",
 "g.p": "<strong>Pactamos por escrito el retorno de tus anuncios y el crecimiento de tu audiencia. Si a los 90 días no llegamos, seguimos trabajando sin cobrarte la cuota hasta llegar.</strong> Además: si el día 21 el sistema no está funcionando, te devolvemos la puesta en marcha; si una semana no publicamos lo pactado, esa semana no la pagas; y todo lo que hacemos es tuyo, también si te vas.",
 "models.h2": "Para negocios que ya venden <em>y quieren escalar.</em>",
 "cta.lead": "Escríbenos qué vendes. Te contesta Alfonso en persona y, si encajamos, te manda un vídeo con lo que cambiaría en tus anuncios y 3 creatividades hechas para tu negocio. Si no encajamos, te lo dice.",
 "cta.btn": "Quiero mi diagnóstico gratis",
 "cta.fit": "Gratis y sin compromiso · Una empresa nueva por semana",
},
"en": {
 "hero.eyebrow": "For training, service and personal brands that already sell",
 "hero.h1": "Content every day. <em>Ads that pay for themselves.</em>",
 "hero.lead": "We publish every day to find out what hooks your clients, turn what works into ads and take it all the way to the sale with a funnel built in. <strong>Running in 21 days. Return and growth agreed in writing, or we keep working for free.</strong>",
 "hero.cta1": "Get my free diagnosis",
 "hero.reassure": "Free: we review your ads and send you 3 creatives · One new company per week",
 "proof.k": "Real case · Meta Ads",
 "proof.who": "<strong>IUVER Academy</strong> · aesthetic medicine master’s. First intake full: 30 out of 30 places.",
 "proof.k2": "Miguel Sierra · YouTube",
 "proof.v2": "+8,000 subscribers in under 4 months",
 "res.eyebrow": "Results",
 "res.h2": "What happens when content <em>feeds the ads.</em>",
 "pain.eyebrow": "Sound familiar?",
 "pain.h2": "You don’t have marketing. <em>You have expenses.</em>",
 "tesis.h3": "Meta works and what you sell sells. <em>The problem is you test too little.</em>",
 "tesis.p": "An agency makes you four pieces a month and waits to see what happens. That way it takes a year to find the ad that sells. <strong>We publish every day and test hooks non-stop</strong>, with everything your business already knows: your website, syllabus, reviews and what your clients ask. With AI, volume stops being a cost.",
 "mech.eyebrow": "The Test & Scale System",
 "mech.h2": "We publish every day. <em>We scale what sells.</em>",
 "mech.lead": "Three moves, with our AI system and the judgement of two people who decide what goes out.",
 "svc.h2": "Three results, <em>with a name and a number.</em>",
 "svc.lead": "Get bought, get followed and get remembered. This is how it looks on real accounts.",
 "how.h2": "From your business to sales, <em>in three weeks.</em>",
 "g.k": "days",
 "g.p": "<strong>We agree in writing your ad return and your audience growth. If we haven’t hit them by day 90, we keep working without charging the fee until we do.</strong> Also: if the system isn’t running by day 21, we refund the setup; if one week we don’t publish what we agreed, you don’t pay that week; and everything we make is yours, even if you leave.",
 "models.h2": "For businesses that already sell <em>and want to scale.</em>",
 "cta.lead": "Tell us what you sell. Alfonso replies in person and, if we’re a fit, sends you a video with what he would change in your ads and 3 creatives made for your business. If we’re not, he’ll tell you.",
 "cta.btn": "Get my free diagnosis",
 "cta.fit": "Free, no strings · One new company per week",
},
}


def reemplazar_lista(t: str, nombre: str, nuevo: str) -> str:
    ini = t.index(f"const {nombre} = ")
    i = ini + len(f"const {nombre} = ")
    abre = t[i]; cierra = {"[": "]", "{": "}"}[abre]
    prof, j, en_str, q = 0, i, False, ""
    while True:  # busca el cierre equilibrado respetando cadenas
        c = t[j]
        if en_str:
            if c == "\\": j += 2; continue
            if c == q: en_str = False
        elif c in "'\"`": en_str, q = True, c
        elif c == abre: prof += 1
        elif c == cierra:
            prof -= 1
            if prof == 0: break
        j += 1
    return t[:i] + nuevo + t[j + 1:]


def reemplazar_clave(bloque: str, clave: str, valor: str) -> str:
    v = valor.replace("\\", "\\\\").replace("'", "\\'")
    patron = re.compile(r"'" + re.escape(clave) + r"':'(?:[^'\\]|\\.)*'")
    if patron.search(bloque):
        return patron.sub(lambda m: f"'{clave}':'{v}'", bloque, count=1)
    cierre = bloque.rindex("}")  # clave nueva justo antes de la llave que cierra el idioma
    return bloque[:cierre].rstrip() + f",\n    '{clave}':'{v}'\n  " + bloque[cierre:]


def main():
    t = HTML.read_text(encoding="utf-8")
    for nombre, nuevo in LISTAS.items():
        t = reemplazar_lista(t, nombre, nuevo)
    ini = t.index("const I18N = {")
    es_i = t.index("es:{", ini); en_i = t.index("en:{", es_i); fin = t.index("\n};", en_i)
    es_b, en_b = t[es_i:en_i], t[en_i:fin]
    for k, v in CLAVES["es"].items():
        es_b = reemplazar_clave(es_b, k, v)
    for k, v in CLAVES["en"].items():
        en_b = reemplazar_clave(en_b, k, v)
    t = t[:es_i] + es_b + t[en_i:en_i] + en_b + t[fin:]
    t = t.replace("Unos 7.800 € al mes y tres meses de contratación", "Unos 9.000-10.000 € al mes y tres meses de contratación")
    t = t.replace("Around 7,800 € a month and three months of hiring", "Around 9,000-10,000 € a month and three months of hiring")
    HTML.write_text(t, encoding="utf-8")
    print("copy v7 aplicado")


if __name__ == "__main__":
    main()
