import pathlib
from pytube import YouTube
import glob
import os
import moviepy.editor as mp 

link=input("Paste the link")
x=int(input("1.ONLY VIDEO 2.BOTH AUDIO AND VIDEO 3.ONLY AUDIO"))
t1=input("Enter start time with colon separated")
t2=input("Enter End time with colon separated")
a = sum(int(x) * 60 ** i for i, x in enumerate(reversed(t1.split(':'))))
b = sum(int(x) * 60 ** i for i, x in enumerate(reversed(t2.split(':'))))

if(x==1):
    try:    
        yt = YouTube(link)  
    except:  
        print("Connection Error")   
    mp4files = yt.streams.filter(adaptive=True).order_by('resolution').desc()
    mp4files[0].download() 
    t=glob.glob("*.mp4")
    t.sort(key=os.path.getmtime,reverse=True)
    print(t)

    input_video_path = t[0]
    output_video_path = 'clip.mp4'

    with mp.VideoFileClip(input_video_path) as video:
        new = video.subclip(a, b)
        new.write_videofile(output_video_path, audio_codec='aac')
    try:
        file_to_rem = pathlib.Path(t[0])
        file_to_rem.unlink()
    except Exception as e:
        pass        
    print('Ready To Edit!') 
if(x==2):
    try:    
        yt = YouTube(link)  
    except:  
        print("Connection Error")   
    mp4files = yt.streams.filter(adaptive=True)
    u=[]
    for i in mp4files:
        u.append(i.resolution)
    print(u)
    e=int(input("selct res index"))
    o=yt.streams.filter(adaptive=True,res=str(u[e]))
    o[0].download()
    yt.streams.filter(only_audio=True).first().download(filename="audio")
    t=glob.glob("*")
    t.sort(key=os.path.getmtime,reverse=True)
    with mp.AudioFileClip(t[0]) as az:
        new=az.subclip(a,b)
        new.write_audiofile('x.mp3')
       
    with mp.VideoFileClip(t[1]) as vid:
        q = vid.subclip(a, b)
        q.write_videofile('y.mp4',fps=60)
    p=glob.glob("*")
    p.sort(key=os.path.getmtime,reverse=True) 
    audi=mp.AudioFileClip(p[1])
    vidi=mp.VideoFileClip(p[0])
    finalclip=vidi.set_audio(audi)
    finalclip.write_videofile('clipping.mp4')
    try:
        file_to_rem = pathlib.Path(t[0])
        file_to_rem.unlink()
        file_to_rem = pathlib.Path(t[1])
        file_to_rem.unlink()
        file_to_rem = pathlib.Path(p[1])
        file_to_rem.unlink()
        file_to_rem = pathlib.Path(p[0])
        file_to_rem.unlink()
    except Exception as e:
        pass        
    print('Ready To play audio and video!') 
if(x==3):
    try:    
        yt = YouTube(link)  
    except:  
        print("Connection Error")   
    mp3files = yt.streams.filter(only_audio=True).all()
    mp3files[0].download() 
    t=glob.glob("*")
    t.sort(key=os.path.getmtime,reverse=True)
    output_video_path="clip.mp3"
    with mp.AudioFileClip(t[0]) as video:
        new = video.subclip(a, b)
        new.write_audiofile(output_video_path)
    try:
        file_to_rem = pathlib.Path(t[0])
        file_to_rem.unlink()
    except Exception as e:
        pass        
    print('Ready For play audio!')     
