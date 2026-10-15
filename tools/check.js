const fs=require('fs');
const s=fs.readFileSync('index.html','utf8');
const m=s.match(/<script>([\s\S]*)<\/script>/);
try{ new Function(m[1]); console.log('JS syntax OK'); }catch(e){ console.log('JS ERR', e.message); process.exitCode=1; }
const hrefs=[...s.matchAll(/href="([^"]+)"/g)].map(x=>x[1]);
const ids=new Set([...s.matchAll(/id="([^"]+)"/g)].map(x=>x[1]));
const bad=[];
for(const h of hrefs){
  if(h.startsWith('#')){ if(h.length>1 && !ids.has(h.slice(1))) bad.push(h); }
  else if(!/^https?:|^data:|^mailto:/.test(h)){ const f=h.split('#')[0]; if(f && !fs.existsSync(f)) bad.push(h); }
}
console.log('enlaces internos rotos:', bad.length ? bad : 'ninguno');
const srcs=[...s.matchAll(/(?:src|poster)="(assets\/[^"]+)"/g)].map(x=>x[1]).filter(x=>!x.includes('${'));
const miss=srcs.filter(f=>!fs.existsSync(f));
console.log('assets estáticos que faltan:', miss.length ? miss : 'ninguno');
for(const f of ['favicon.svg','favicon-32.png','apple-touch-icon.png','robots.txt','sitemap.xml','404.html','legal.html','assets/img/og.jpg','assets/videos/showreel-bg.mp4']) console.log(f, fs.existsSync(f)?'ok':'FALTA');
