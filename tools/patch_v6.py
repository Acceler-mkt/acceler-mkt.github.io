# -*- coding: utf-8 -*-
# Mínimos técnicos (reel de millocreador.ia): metas, OG, favicon, legal, 404, contraste, alt, hero ligero.
import os
p=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'index.html')
s=open(p,encoding='utf-8').read(); n=0
def rep(a,b,expect=None):
    global s,n
    c=s.count(a); assert c>0, "NO ENCONTRADO: "+a[:70]
    if expect is not None: assert c==expect, "count %d != %d: %s"%(c,expect,a[:60])
    s=s.replace(a,b); n+=c

# metas
rep('<meta name="description" content="Anuncios de Meta, contenido orgánico y YouTube para marcas personales y empresas que ya facturan, producidos con nuestro sistema de IA y medidos en ventas. Con 10.000 € en anuncios, IUVER Academy facturó 165.000 €.">',
    '<meta name="description" content="Anuncios de Meta, contenido y YouTube para marcas personales y empresas que ya facturan, producidos con IA y medidos hasta la venta. Con 10.000 € en anuncios, IUVER Academy facturó 165.000 €.">\n<meta name="robots" content="index,follow">')
rep('<meta property="og:title" content="Acceler MKT · Marketing con IA para marcas personales y empresas">',
    '<meta property="og:url" content="https://acceler-mkt.github.io/">\n<meta property="og:site_name" content="Acceler MKT">\n<meta property="og:locale" content="es_ES">\n<meta property="og:title" content="Acceler MKT · No tienes marketing. Tienes gastos.">')
rep('<meta property="og:description" content="Esto es lo que medimos cada semana: lo que entra en caja. Con 10.000 € en anuncios, IUVER Academy facturó 165.000 €.">',
    '<meta property="og:description" content="Anuncios, contenido y YouTube producidos con IA y medidos hasta la venta. Con 10.000 € en anuncios, IUVER Academy facturó 165.000 €.">')
rep('<meta property="og:image" content="https://acceler-mkt.github.io/assets/posters/showreel.jpg">',
    '<meta property="og:image" content="https://acceler-mkt.github.io/assets/img/og.jpg">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:title" content="Acceler MKT · No tienes marketing. Tienes gastos.">\n<meta name="twitter:description" content="Anuncios, contenido y YouTube producidos con IA y medidos hasta la venta.">\n<meta name="twitter:image" content="https://acceler-mkt.github.io/assets/img/og.jpg">')
# favicon real
i0=s.index('<link rel="icon" href="data:image/svg+xml'); i1=s.index('>',i0)+1
s=s[:i0]+'<link rel="icon" href="favicon.svg" type="image/svg+xml">\n<link rel="icon" href="favicon-32.png" sizes="32x32" type="image/png">\n<link rel="apple-touch-icon" href="apple-touch-icon.png">'+s[i1:]; n+=1
# JSON-LD + hueco de analítica
rep('<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">\n<style>',
    '<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">\n<script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization","name":"Acceler MKT","url":"https://acceler-mkt.github.io/","logo":"https://acceler-mkt.github.io/apple-touch-icon.png","description":"Marketing con IA para marcas personales y empresas: anuncios de Meta, contenido orgánico y YouTube medidos hasta la venta.","address":{"@type":"PostalAddress","addressRegion":"Santa Cruz de Tenerife","addressCountry":"ES"},"contactPoint":{"@type":"ContactPoint","telephone":"+34647829854","contactType":"sales","availableLanguage":["es","en"]}}</script>\n<!-- ANALÍTICA: pendiente de ID (GA4 o Meta Pixel). Si se añade, hace falta banner de consentimiento. -->\n<style>')
# hero: vídeo de fondo ligero
rep('<video id="heroVideo" autoplay muted loop playsinline preload="auto" poster="assets/posters/showreel.jpg">\n      <source src="assets/videos/showreel.mp4" type="video/mp4">',
    '<video id="heroVideo" autoplay muted loop playsinline preload="auto" poster="assets/posters/showreel-bg.jpg" aria-hidden="true">\n      <source src="assets/videos/showreel-bg.mp4" type="video/mp4">')
# contraste del gris pequeño
rep("--mute:#a39d94;--mute2:#6f6961;","--mute:#a39d94;--mute2:#8a847c;")
# alt en los visuales de resultados
rep("""? `<div class="vis"><div class="ph"><img src="assets/posters/${v.img}" alt="" loading="lazy"></div>""","""? `<div class="vis"><div class="ph"><img src="assets/posters/${v.img}" alt="${esc(L(v.alt))}" loading="lazy"></div>""")
rep("""    : `<div class="vis"><div class="yt"><img src="assets/posters/${v.img}" alt="" loading="lazy"><i></i></div>""","""    : `<div class="vis"><div class="yt"><img src="assets/posters/${v.img}" alt="${esc(L(v.alt))}" loading="lazy"><i></i></div>""")
rep("vis:{type:'phone',img:'iuver-ad1.jpg',","vis:{type:'phone',img:'iuver-ad1.jpg',alt:{es:'Anuncio de Meta de IUVER Academy en un móvil',en:'IUVER Academy Meta ad on a phone'},")
rep("vis:{type:'phone',img:'gla-oro.jpg',","vis:{type:'phone',img:'gla-oro.jpg',alt:{es:'Reel de GLA Patrimonio en un móvil',en:'GLA Patrimonio reel on a phone'},")
rep("vis:{type:'yt',img:'ms-holding.jpg',","vis:{type:'yt',img:'ms-holding.jpg',alt:{es:'Vídeo de YouTube de Miguel Sierra',en:'Miguel Sierra YouTube video'},")
rep('<div class="showreel reveal"><video autoplay muted loop playsinline preload="metadata" poster="assets/posters/showreel.jpg" src="assets/videos/showreel.mp4"></video>',
    '<div class="showreel reveal"><video autoplay muted loop playsinline preload="metadata" poster="assets/posters/showreel.jpg" src="assets/videos/showreel.mp4" aria-label="Showreel de Acceler MKT"></video>')
# footer: enlaces legales
rep('<span data-i18n="ftr.tag">Marketing con IA · Tenerife, España</span>\n    <span>© 2026 Acceler MKT</span>',
    '<span data-i18n="ftr.tag">Marketing con IA · Tenerife, España</span>\n    <span><a href="legal.html" data-i18n="ftr.legal">Aviso legal y privacidad</a> · <a href="legal.html#cookies">Cookies</a> · © 2026 Acceler MKT</span>')
rep("'ftr.tag':'Marketing con IA · Tenerife, España','lb.yt':'Ver completo en YouTube'","'ftr.tag':'Marketing con IA · Tenerife, España','ftr.legal':'Aviso legal y privacidad','lb.yt':'Ver completo en YouTube'")
rep("'ftr.tag':'AI-driven marketing · Tenerife, Spain','lb.yt':'Watch the full video on YouTube'","'ftr.tag':'AI-driven marketing · Tenerife, Spain','ftr.legal':'Legal notice and privacy','lb.yt':'Watch the full video on YouTube'")
rep(".ftr .wrap{display:flex;flex-wrap:wrap;gap:20px;justify-content:space-between;align-items:center}",".ftr .wrap{display:flex;flex-wrap:wrap;gap:20px;justify-content:space-between;align-items:center}\n.ftr a{color:var(--mute);text-decoration:none;border-bottom:1px solid var(--line)}\n.ftr a:hover{color:var(--ink)}")
open(p,'w',encoding='utf-8').write(s); print('reemplazos ok:',n)
