import subprocess, os, sys
V="C:/Users/Alfonso/Documents/claude code/acceler-video-studio/out"
R="C:/Users/Alfonso/remotion-reels"
C="C:/Users/Alfonso/Documents/Evolve Agency/Clientes"
OUT="C:/Users/Alfonso/Documents/claude code/acceler-portfolio"
TMP=OUT+"/tools/reel_tmp"
D=2.5; F=0.5
segs=[
 (V+"/MiguelSierra_yt-0910_v3.mp4",7.5,"h"),
 (R+"/proyectos/GLA_Patrimonio/2026-10-04_40k/out/final.mp4",1.0,"v"),
 (V+"/MiguelSierra_yt-0913_v3.mp4",63.0,"h"),
 (C+"/Iuver Academy (Yiro)/Reels evento 9 oct 2026/IUVER evento - 01 - Lorena - Pinchar es lo fácil. Lo difícil es decidir.mp4",16.0,"v"),
 (V+"/MiguelSierra_3-errores_v1.mp4",47.5,"h"),
 (R+"/pruebas/iuver-subs/out/iuver-v4.mp4",23.0,"v"),
 (V+"/Fixcal_Seleccionarte_v3.mp4",3.5,"h"),
 (C+"/Miguel Sierra/Clipps yt/PRUEBAS pack-video/01 - Misma venta, 270.000 euros de diferencia.mp4",4.0,"v"),
 (V+"/MiguelSierra_fracasaste_v2.mp4",55.5,"h"),
 (C+"/Iuver Academy (Yiro)/Reels evento 9 oct 2026/IUVER evento - 16 - Vicente - Ser un médico normal no basta.mp4",11.5,"v"),
 (R+"/proyectos/GLA_Patrimonio/2026-10-01_oro-cae-6/out/final.mp4",16.0,"v"),
 (R+"/proyectos/IUVER_Academy/clases-master/out/muestra_lorena.mp4",4.0,"h"),
]
H="scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,setsar=1,fps=30,format=yuv420p"
Vf="split=2[a][b];[a]scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,gblur=sigma=28,eq=brightness=-0.22:saturation=1.05[bg];[b]scale=-2:720[fg];[bg][fg]overlay=(W-w)/2:0,setsar=1,fps=30,format=yuv420p"
tmps=[]
for i,(f,ss,m) in enumerate(segs):
    o=f"{TMP}/seg{i:02d}.mp4"; tmps.append(o)
    vf = H if m=="h" else Vf
    cmd=["ffmpeg","-v","error","-y","-ss",str(ss),"-i",f,"-t",str(D),"-an","-filter_complex",f"[0:v]{vf}[out]","-map","[out]","-c:v","libx264","-preset","veryfast","-crf","16",o]
    r=subprocess.run(cmd,capture_output=True,text=True)
    print(i, "ok" if r.returncode==0 else r.stderr[:300], flush=True)
# xfade chain
inputs=[]; 
for t in tmps: inputs+=["-i",t]
n=len(tmps); fc=[]; prev="[0:v]"
for k in range(1,n):
    off=k*(D-F)
    outl=f"[v{k}]" if k<n-1 else "[vout]"
    fc.append(f"{prev}[{k}:v]xfade=transition=fade:duration={F}:offset={off:.2f}{outl}")
    prev=outl
cmd=["ffmpeg","-v","error","-y"]+inputs+["-filter_complex",";".join(fc),"-map","[vout]","-c:v","libx264","-preset","medium","-crf","22","-profile:v","high","-pix_fmt","yuv420p","-movflags","+faststart","-an",OUT+"/assets/videos/showreel.mp4"]
r=subprocess.run(cmd,capture_output=True,text=True)
print("final", "ok" if r.returncode==0 else r.stderr[:500])
if r.returncode==0:
    subprocess.run(["ffmpeg","-v","error","-y","-ss","1","-i",OUT+"/assets/videos/showreel.mp4","-frames:v","1","-q:v","3",OUT+"/assets/posters/showreel.jpg"])
    print(os.path.getsize(OUT+"/assets/videos/showreel.mp4"))
