# -*- coding: utf-8 -*-
import os
p=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'index.html')
s=open(p,encoding='utf-8').read(); n=0
def rep(a,b,expect=None):
    global s,n
    c=s.count(a); assert c>0, "NO ENCONTRADO: "+a[:70]
    if expect is not None: assert c==expect, "count %d != %d: %s"%(c,expect,a[:60])
    s=s.replace(a,b); n+=c

# 1. Nombre: Acceler MKT
rep("<title>Acceler · Marketing con IA para marcas personales y empresas</title>","<title>Acceler MKT · Marketing con IA para marcas personales y empresas</title>")
rep('content="Acceler · Marketing con IA para marcas personales y empresas"','content="Acceler MKT · Marketing con IA para marcas personales y empresas"')
rep("'Acceler · Marketing con IA para marcas personales y empresas' : 'Acceler · AI-driven marketing for personal brands and companies'","'Acceler MKT · Marketing con IA para marcas personales y empresas' : 'Acceler MKT · AI-driven marketing for personal brands and companies'")
rep("<span>acceler<b>.</b></span>","<span>acceler mkt<b>.</b></span>",2)
rep('<div class="giant" aria-hidden="true">acceler<b>.</b></div>','<div class="giant" aria-hidden="true">acceler mkt<b>.</b></div>')
rep("<span>© 2026 Acceler</span>","<span>© 2026 Acceler MKT</span>")
rep("he visto la web de Acceler y","he visto la web de Acceler MKT y")
rep("I saw the Acceler site and","I saw the Acceler MKT site and")
rep("Cofundador de Acceler.","Cofundador de Acceler MKT.")
rep("Co-founder of Acceler.","Co-founder of Acceler MKT.")
rep("la plataforma propia de Acceler.","la plataforma propia de Acceler MKT.")
rep("and Acceler’s own platform.","and Acceler MKT’s own platform.")
rep("CRM y automatizaciones propias de Acceler, para","CRM y automatizaciones propias, para")
rep("Acceler’s own CRM and automations, for","Our own CRM and automations, for")
rep("{h:{es:'Acceler',en:'Acceler'}, p:{es:'Un sistema con IA","{h:{es:'Acceler MKT',en:'Acceler MKT'}, p:{es:'Un sistema con IA")

# 2. Hero opción A
rep("Acceler · Marketing con IA · Más de 2 años con marcas personales y empresas","Acceler MKT · Marketing con IA para marcas personales y empresas que ya facturan",2)
rep("Acceler · AI-driven marketing · 2+ years with personal brands and companies","Acceler MKT · AI-driven marketing for personal brands and companies with revenue")
rep("Esto es lo que medimos cada semana: <em>lo que entra en caja.</em></h1>","No tienes marketing. <em>Tienes gastos.</em></h1>")
rep("'hero.h1':'Esto es lo que medimos cada semana: <em>lo que entra en caja.</em>'","'hero.h1':'No tienes marketing. <em>Tienes gastos.</em>'")
rep("'hero.h1':'This is what we measure every week: <em>what reaches the bank.</em>'","'hero.h1':'You don’t have marketing. <em>You have expenses.</em>'")
old_lead_es="Llevamos los anuncios de Meta, el contenido orgánico y el YouTube de marcas personales y empresas que ya facturan. Lo producimos con nuestro propio sistema de IA y lo conectamos con tus ventas. <strong>Si tu marketing te da informes y no clientes, sigue leyendo.</strong>"
new_lead_es="Si no sabes qué anuncio, qué reel o qué vídeo te ha traído el último cliente, eso es lo que te está pasando. <strong>Nosotros llevamos tus anuncios de Meta, tu contenido y tu YouTube, los producimos con nuestro propio sistema de IA y los medimos hasta la venta. Funcionando en 21 días.</strong>"
rep(old_lead_es,new_lead_es,2)
old_lead_en="We run the Meta ads, organic content and YouTube of personal brands and companies with revenue. We produce it with our own AI system and connect it to your sales. <strong>If your marketing gives you reports instead of clients, keep reading.</strong>"
new_lead_en="If you can’t say which ad, reel or video brought your last client, that is what is happening to you. <strong>We run your Meta ads, your content and your YouTube, produce them with our own AI system and measure them down to the sale. Up and running in 21 days.</strong>"
rep(old_lead_en,new_lead_en)
rep('<p class="reassure" data-i18n="hero.reassure">Sin compromiso: en la primera conversación te decimos si encajamos y qué haríamos.</p>',
    '<p class="reassure" data-i18n="hero.reassure">Sin compromiso. Dos plazas por trimestre.</p>')
rep('<div class="hero-cta">\n          <a class="btn btn-wa wa-link"','<p class="qual" data-i18n="hero.qual">Para marcas personales y empresas que ya facturan. Si empiezas de cero, no somos para ti.</p>\n        <div class="hero-cta">\n          <a class="btn btn-wa wa-link"')
rep("'hero.reassure':'Sin compromiso: en la primera conversación te decimos si encajamos y qué haríamos.',","'hero.reassure':'Sin compromiso. Dos plazas por trimestre.','hero.qual':'Para marcas personales y empresas que ya facturan. Si empiezas de cero, no somos para ti.',")
rep("'hero.reassure':'No strings: in the first conversation we tell you whether we fit and what we would do.',","'hero.reassure':'No strings. Two spots per quarter.','hero.qual':'For personal brands and companies with revenue. If you are starting from zero, we are not for you.',")
rep(".reassure{font-family:var(--mono);font-size:12px;letter-spacing:.06em;color:var(--mute);margin-top:14px}",".reassure{font-family:var(--mono);font-size:12px;letter-spacing:.06em;color:var(--mute);margin-top:14px}\n.qual{margin-top:18px;font-size:15px;color:var(--ink);border-left:2px solid var(--coral);padding-left:12px;max-width:52ch}")
rep("gsap.from('.hero .lead, .hero-cta, .hero .reassure, .proof'","gsap.from('.hero .lead, .hero .qual, .hero-cta, .hero .reassure, .proof'")

# 3. Tesis
rep("El marketing de las marcas que facturan lo llevan agencias de posts bonitos o freelances que <em>desaparecen en agosto.</em>","Hasta ahora tenías dos opciones: una agencia de posts bonitos <em>o un freelance que desaparece en agosto.</em>",2)
rep("Marketing for brands with revenue is run by pretty-posts agencies or freelancers who <em>vanish in August.</em>","Until now you had two options: a pretty-posts agency <em>or a freelancer who vanishes in August.</em>")
rep("Las dos cobran por piezas y reportan impresiones. Ninguna se juega nada en tus ventas. Acceler existe para lo contrario:","Las dos cobran por piezas y reportan impresiones. Ninguna se juega nada en tus ventas. Acceler MKT existe para lo contrario:",2)
rep("Both charge per piece and report impressions. Neither has anything riding on your sales. Acceler exists for the opposite:","Both charge per piece and report impressions. Neither has anything riding on your sales. Acceler MKT exists for the opposite:")

# 4. Tabla: textos y nuevo render
rep("{es:['Una creatividad nueva cada trimestre','30 o 40 creatividades al mes'],en:['One new creative per quarter','30 to 40 creatives a month']}","{es:['Unas pocas creatividades al mes, a ver qué pasa','30 o 40 creatividades al mes, y se apaga lo que no vende'],en:['A handful of creatives a month, fingers crossed','30 to 40 creatives a month, and what doesn’t sell gets switched off']}")
old_cmp_render="""  document.getElementById('cmp').innerHTML = `<div class="cmp-row"><div>${esc(CMP.head[lang][0])}</div><div>${esc(CMP.head[lang][1])}</div></div>` + CMP.rows.map(r=>`<div class="cmp-row"><div>${esc(r[lang][0])}</div><div>${esc(r[lang][1])}</div></div>`).join('');"""
new_cmp_render="""  document.getElementById('cmp').innerHTML = `<div class="cmp-old"><div class="cmp-h">${esc(CMP.head[lang][0])}</div><ul>${CMP.rows.map(r=>`<li><i>✕</i><span>${esc(r[lang][0])}</span></li>`).join('')}</ul></div>
    <div class="cmp-new"><div class="sweep"></div><div class="cmp-h">${MARK}<span>acceler mkt<b>.</b></span><em>${esc(CMP.head[lang][1])}</em></div><ul>${CMP.rows.map((r,i)=>`<li style="--i:${i}"><i>→</i><span>${esc(r[lang][1])}</span></li>`).join('')}</ul></div>`;"""
rep(old_cmp_render,new_cmp_render)
rep("function esc(s){","const MARK='<svg viewBox=\"0 0 136 136\" aria-hidden=\"true\"><circle cx=\"68\" cy=\"68\" r=\"60\" fill=\"#7a2a2a\"/><circle cx=\"86\" cy=\"50\" r=\"48\" fill=\"#e8a048\"/><circle cx=\"78\" cy=\"62\" r=\"40\" fill=\"#c24a4a\"/><circle cx=\"88\" cy=\"56\" r=\"30\" fill=\"#de6262\"/><circle cx=\"95\" cy=\"52\" r=\"18\" fill=\"#f1b76f\"/></svg>';\nfunction esc(s){")
i0=s.index("/* comparison table */"); i1=s.index("/* services */")
new_cmp_css="""/* comparison */
.cmp{display:grid;gap:14px}
@media(min-width:860px){.cmp{grid-template-columns:.9fr 1.1fr;align-items:stretch}}
.cmp ul{list-style:none}
.cmp li{display:flex;gap:12px;align-items:flex-start;padding:15px 0;border-top:1px solid var(--lined);font-size:15.5px;line-height:1.45}
.cmp li i{font-style:normal;font-family:var(--mono);flex:none;width:18px;text-align:center;transition:transform .3s}
.cmp-h{font-family:var(--mono);font-size:11.5px;letter-spacing:.12em;text-transform:uppercase;padding-bottom:14px}
.cmp-old{background:#fff;border:1px solid var(--lined);border-radius:24px;padding:24px 26px;color:var(--greyw)}
.cmp-old .cmp-h{color:var(--greyw)}
.cmp-old li i{color:#b9b2a8}
.cmp-new{position:relative;overflow:hidden;border-radius:24px;padding:24px 26px;background:var(--inkd);color:var(--ink);border:1px solid rgba(222,98,98,.45);box-shadow:0 40px 90px -40px rgba(222,98,98,.55),0 0 0 1px rgba(222,98,98,.08) inset}
.cmp-new::before{content:"";position:absolute;inset:auto -35% -55% auto;width:85%;aspect-ratio:1;border-radius:50%;background:radial-gradient(circle,rgba(222,98,98,.55),rgba(232,160,72,.22) 40%,transparent 68%);filter:blur(12px);animation:breathe 4.5s ease-in-out infinite}
.cmp-new::after{content:"";position:absolute;inset:-40% auto auto -30%;width:60%;aspect-ratio:1;border-radius:50%;background:radial-gradient(circle,rgba(232,160,72,.25),transparent 65%);filter:blur(14px);animation:breathe 6s ease-in-out infinite reverse}
.cmp-new .sweep{position:absolute;inset:0;background:linear-gradient(105deg,transparent 35%,rgba(246,245,244,.12) 50%,transparent 65%);transform:translateX(-120%);animation:sweep 5.5s cubic-bezier(.6,0,.2,1) infinite;pointer-events:none}
.cmp-new>*{position:relative}
.cmp-new .cmp-h{display:flex;align-items:center;gap:10px;color:var(--ink);border-bottom:1px solid rgba(246,245,244,.12)}
.cmp-new .cmp-h svg{width:22px;height:22px}
.cmp-new .cmp-h span{font-family:"Inter",var(--sans);font-weight:700;font-size:18px;letter-spacing:-.04em;text-transform:none}
.cmp-new .cmp-h span b{color:var(--coral)}
.cmp-new .cmp-h em{margin-left:auto;font-style:normal;font-family:var(--mono);color:var(--gold)}
.cmp-new li{border-top-color:rgba(246,245,244,.1);color:var(--ink);font-weight:500;animation:rowin .9s cubic-bezier(.2,.8,.2,1) both;animation-delay:calc(.12s * var(--i))}
.cmp-new li i{color:var(--coral);text-shadow:0 0 12px rgba(222,98,98,.8)}
.cmp-new li:hover{color:#fff}
.cmp-new li:hover i{transform:translateX(3px)}
@keyframes breathe{0%,100%{transform:scale(1);opacity:.85}50%{transform:scale(1.18);opacity:1}}
@keyframes sweep{0%,55%{transform:translateX(-120%)}100%{transform:translateX(120%)}}
@keyframes rowin{from{opacity:0;transform:translateX(-14px)}to{opacity:1;transform:none}}
@media(prefers-reduced-motion:reduce){.cmp-new::before,.cmp-new::after,.cmp-new .sweep,.cmp-new li{animation:none}}

"""
s=s[:i0]+new_cmp_css+s[i1:]; n+=1

# 5. Servicios con visual encima
rep("  {num:'01', h:{es:'Que te compren.',en:'Get bought.'}, sub:","  {num:'01', vis:{type:'phone',img:'iuver-ad1.jpg',a:{es:'Lead cualificado · médica',en:'Qualified lead · doctor'},b:{es:'Matrícula · 7.000 €',en:'Enrolment · 7,000 €'}}, h:{es:'Que te compren.',en:'Get bought.'}, sub:")
rep("  {num:'02', h:{es:'Que te crean.',en:'Get believed.'}, sub:","  {num:'02', vis:{type:'phone',img:'gla-oro.jpg',a:{es:'«He visto tu reel, ¿podemos hablar?»',en:'“Saw your reel, can we talk?”'},b:{es:'Llamada reservada',en:'Call booked'}}, h:{es:'Que te crean.',en:'Get believed.'}, sub:")
rep("  {num:'03', h:{es:'Que te recuerden.',en:'Get remembered.'}, sub:","  {num:'03', vis:{type:'yt',img:'ms-holding.jpg',a:{es:'2 vídeos a la semana',en:'2 videos a week'},b:{es:'Miguel Sierra · 12:55',en:'Miguel Sierra · 12:55'}}, h:{es:'Que te recuerden.',en:'Get remembered.'}, sub:")
old_svc_render="""  document.getElementById('services').innerHTML = SERVICES.map(s=>`<div class="service reveal"><div class="num">${s.num}</div><h3>"""
new_svc_render="""  const visHTML = v => v.type==='phone'
    ? `<div class="vis"><div class="ph"><img src="assets/posters/${v.img}" alt="" loading="lazy"></div><span class="chip c1">${esc(L(v.a))}</span><span class="chip c2">${esc(L(v.b))}</span></div>`
    : `<div class="vis"><div class="yt"><img src="assets/posters/${v.img}" alt="" loading="lazy"><i></i></div><span class="chip c1">${esc(L(v.a))}</span><span class="chip c3">${esc(L(v.b))}</span></div>`;
  document.getElementById('services').innerHTML = SERVICES.map(s=>`<div class="service reveal">${visHTML(s.vis)}<div class="num">${s.num}</div><h3>"""
rep(old_svc_render,new_svc_render)
rep(".service{background:#fff;border:1px solid var(--lined);border-radius:24px;padding:30px 28px;display:grid;gap:14px;align-content:start;transition:transform .5s cubic-bezier(.2,.8,.2,1),box-shadow .5s}",
""".service{background:#fff;border:1px solid var(--lined);border-radius:24px;padding:0 28px 30px;display:grid;gap:14px;align-content:start;overflow:hidden;transition:transform .5s cubic-bezier(.2,.8,.2,1),box-shadow .5s}
.vis{position:relative;height:230px;margin:0 -28px 14px;background:radial-gradient(80% 70% at 50% 110%,rgba(222,98,98,.22),transparent 70%),linear-gradient(180deg,#eceae5,#f5f3f0);border-bottom:1px solid var(--lined);overflow:hidden}
.vis .ph{position:absolute;left:50%;top:24px;transform:translateX(-50%);width:124px;aspect-ratio:9/16;border-radius:18px;overflow:hidden;border:4px solid #1b1a18;box-shadow:0 24px 50px -20px rgba(27,26,24,.6);background:#000}
.vis .ph img{width:100%;height:100%;object-fit:cover}
.vis .yt{position:absolute;left:28px;right:28px;top:26px;aspect-ratio:16/9;border-radius:14px;overflow:hidden;box-shadow:0 24px 50px -20px rgba(27,26,24,.6);background:#000}
.vis .yt img{width:100%;height:100%;object-fit:cover}
.vis .yt i{position:absolute;left:50%;top:50%;width:54px;height:36px;transform:translate(-50%,-50%);background:#ff0033;border-radius:10px}
.vis .yt i::after{content:"";position:absolute;left:55%;top:50%;transform:translate(-50%,-50%);border-left:14px solid #fff;border-top:9px solid transparent;border-bottom:9px solid transparent}
.vis .chip{position:absolute;background:#fff;color:var(--inkd);border-radius:999px;padding:9px 13px;font-size:12.5px;font-weight:500;box-shadow:0 14px 30px -14px rgba(27,26,24,.5);border:1px solid var(--lined);white-space:nowrap;max-width:46%;overflow:hidden;text-overflow:ellipsis}
.vis .chip::before{content:"";display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--coral);margin-right:8px;vertical-align:middle}
.vis .c1{left:18px;top:52px;animation:floaty 5s ease-in-out infinite}
.vis .c2{right:18px;bottom:36px;animation:floaty 6s ease-in-out infinite reverse}
.vis .c3{right:18px;bottom:22px;animation:floaty 6s ease-in-out infinite reverse}
@keyframes floaty{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
@media(prefers-reduced-motion:reduce){.vis .chip{animation:none}}""")

# 6. Cómo trabajamos sin el "día 21" en el titular
rep("Tres pasos y un día: <em>el 21.</em>","De tu grabación a clientes, <em>en tres pasos.</em>",2)
rep("'how.h2':'Three steps and one day: <em>day 21.</em>'","'how.h2':'From your footage to clients, <em>in three steps.</em>'")
rep("{when:{es:'Día 21',en:'Day 21'}, h:{es:'Publicas y medimos',en:'You publish, we measure'}","{when:{es:'Semana 3',en:'Week 3'}, h:{es:'Publicas y medimos',en:'You publish, we measure'}")

# 7. Equipo con fotos y logo como tercer miembro
old_team="""const TEAM = [
  {r:{es:'Estrategia y criterio',en:'Strategy and judgement'}, h:'Alfonso Aparicio', p:{es:'Lleva la estrategia, el copy y el criterio, y da la cara en cada llamada. Cofundador de Acceler MKT.',en:'Runs strategy, copy and judgement, and is on every call. Co-founder of Acceler MKT.'}},
  {r:{es:'Sistemas y plataforma',en:'Systems and platform'}, h:{es:'Su socio técnico',en:'His technical partner'}, p:{es:'Construye los sistemas, las automatizaciones y la plataforma propia de Acceler MKT.',en:'Builds the systems, the automations and Acceler MKT’s own platform.'}},
  {r:{es:'Producción',en:'Production'}, h:{es:'El sistema de producción con IA',en:'The AI production system'}, p:{es:'Pone el volumen: anuncios, reels, carruseles y vídeos con tu contexto. Lo que se publica lo decidimos nosotros.',en:'Brings the volume: ads, reels, carousels and videos with your context. What gets published is our call.'}}
];"""
new_team="""const TEAM = [
  {img:'t-alfonso.jpg', r:{es:'Estrategia y criterio',en:'Strategy and judgement'}, h:'Alfonso Aparicio', p:{es:'Lleva la estrategia, el copy y el criterio, y da la cara en cada llamada. Cofundador de Acceler MKT.',en:'Runs strategy, copy and judgement, and is on every call. Co-founder of Acceler MKT.'}},
  {img:'t-winslet.jpg', r:{es:'Sistemas y plataforma',en:'Systems and platform'}, h:'Winslet Mateus', p:{es:'Construye los sistemas, las automatizaciones y la plataforma propia. Cofundador y socio técnico.',en:'Builds the systems, the automations and our own platform. Co-founder and technical partner.'}},
  {logo:true, r:{es:'Producción',en:'Production'}, h:{es:'El sistema de producción con IA',en:'The AI production system'}, p:{es:'El tercer miembro del equipo. Pone el volumen: anuncios, reels, carruseles y vídeos con tu contexto. Lo que se publica lo decidimos nosotros.',en:'The third team member. Brings the volume: ads, reels, carousels and videos with your context. What gets published is our call.'}}
];"""
rep(old_team,new_team)
rep("""  document.getElementById('team').innerHTML = TEAM.map(t=>`<div class="who reveal"><div class="r">""","""  document.getElementById('team').innerHTML = TEAM.map(t=>`<div class="who reveal">${t.logo?`<div class="tphoto tlogo">${MARK}</div>`:`<div class="tphoto"><img src="assets/img/${t.img}" alt="${esc(L(t.h))}" loading="lazy"></div>`}<div class="r">""")
rep(".team .who{background:#fff;border:1px solid var(--lined);border-radius:22px;padding:26px 24px;display:grid;gap:8px;align-content:start}",
""".team .who{background:#fff;border:1px solid var(--lined);border-radius:22px;padding:18px 18px 24px;display:grid;gap:8px;align-content:start}
.tphoto{aspect-ratio:4/5;border-radius:16px;overflow:hidden;background:#dcd8d2;margin-bottom:10px;display:grid;place-items:center}
.tphoto img{width:100%;height:100%;object-fit:cover;filter:grayscale(1) contrast(1.05)}
.tlogo{background:var(--inkd);position:relative}
.tlogo::before{content:"";position:absolute;inset:auto -30% -40% auto;width:80%;aspect-ratio:1;border-radius:50%;background:radial-gradient(circle,rgba(222,98,98,.5),rgba(232,160,72,.2) 45%,transparent 70%);filter:blur(12px)}
.tlogo svg{position:relative;width:46%;height:auto;filter:drop-shadow(0 20px 40px rgba(222,98,98,.5))}""")
rep("@media(min-width:900px){.team{grid-template-columns:1.2fr .9fr .9fr}}","@media(min-width:900px){.team{grid-template-columns:repeat(3,1fr)}}")
open(p,'w',encoding='utf-8').write(s); print('reemplazos ok:',n)
