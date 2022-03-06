from tkinter import *
import pygame
import os
import tkinter.font as font
import tkinter as tk


#Creating music player window
window=Tk()
window.geometry("560x630")


#Adding title label
window.title("Audio Player")
title1=PhotoImage(file='C:\\title.png')


#Adding background picture
window.iconphoto(False, title1)
picname=PhotoImage(file='C:\\g.png')
background_label=Label(image=picname)
background_label.place(x=0,y=0)


#Importing pygame.mixer module
pygame.mixer.init()


#Function to receive volume input
def musicvolume(v):
        vol=int(v)/100
        pygame.mixer.music.set_volume(vol)
        print("Volume set to",int(vol*100),'\n')


#Function to loop the audio
def loop():
        pygame.mixer.music.play(-1,0.0)
        print("Audio file is on loop\n")


#Function to fast forward the audio playback
def forward():
        oldtime=pygame.mixer.music.get_pos()
        change=50
        pygame.mixer.music.play(-1,(oldtime+change)/50)        
        print("Audio file fast forwarded")


#Function to add an audio file to the queue to play
def start():
	song_name=songs_listbox.get()
	pygame.mixer.music.load(song_name)
	pygame.mixer.music.play(0)
	print("Audio file has begun playing\nヽ（＾∇＾）ﾉ♪\n ")
	print("Playing:", song_name,'\n')

	
#Function to pause the audio playback
def pause():
        pygame.mixer.music.pause()
        print("Audio file paused! \n(´･_･`)\n")


#Function to unpause the audio playback
def unpause():
        pygame.mixer.music.unpause()
        print("Audio file unpaused! \n°˖✧◝(⁰▿⁰)◜✧˖°\n")


#Function to remove the playing audio file from the queue
def stop():
        pygame.mixer.music.stop()
        print("Audio file stopped\n (´･_･`) \n")


#define font
myFont1=font.Font(family='Bradley Hand ITC',size=15,weight='bold')
myFont2=font.Font(family='Chiller',size=30,weight='bold')
myFont3=font.Font(family='Colonna MT',size=15,weight='bold')


#Adding the player title "AUDIO PLAYER"
titlepic1=PhotoImage(file="C:\\gtitle.png")
l1=Label(window,image=titlepic1)
l1.grid(row=3,column=1,padx=130,pady=20)
l1['font']=myFont2
l1.config(image=titlepic1)

#Adding the next title "Select an auidio file"
titlepic2=PhotoImage(file="C:\\gtitle1.png")
l2=Label(window,image=titlepic2)
l2.grid(row=4,column=1,pady=5)
l2['font']=myFont3
l2.config(image=titlepic2)


#Creating a frame to add the "play audio" button in the player
f1=Frame(window)
f1.grid(column=1, row=6,pady=5)

#Creating a photoimage object to use image
play=PhotoImage(file="C:\\play.png")

#Resizing image to fit on button
tplay=play.subsample(14,13)

def onleave1(event):
        b1['bg']='#d5ebf2'

def onenter1(event):
        b1['activebackground']='#c0e2ed'

b1=Button(f1,image=tplay,bg='#d5ebf2',fg='#2d0636',command=start,relief=GROOVE)
b1.grid(row=0,column=0)
b1.config(image=tplay)
b1.bind('<Leave>',onleave1)
b1.bind('<Enter>',onenter1)

def onleave11(event):
        b11['bg']='#33333d'

def onenter11(event):
        b11['activebackground']='#202024'
        
b11=Button(f1,text='    Click to PLAY SONG     ',bg='#33333d',fg='#ffffff',command=start,relief=GROOVE)
b11['font']=myFont1
b11.grid(row=0,column=1)
b11.bind('<Leave>',onleave11)
b11.bind('<Enter>',onenter11)



#Creating a frame to add the "pause" buttons in the player
f2=Frame(window)
f2.grid(column=1, row=8,pady=5)

#Creating a photoimage object to use image
pause1=PhotoImage(file="C:\\pause.png")

#Resizing image to fit on button
tpause=pause1.subsample(14,13)

def onleave2(event):
        b2['bg']='#dacfe6'

def onenter2(event):
        b2['activebackground']='#cbb6e3'


b2=Button(f2,image=tpause,bg='#dacfe6',fg='#2d0636',command=pause,relief=GROOVE)
b2.grid(row=0,column=0)
b2.config(image=tpause)
b2.bind('<Leave>',onleave2)
b2.bind('<Enter>',onenter2)

def onleave22(event):
        b22['bg']='#33333d'

def onenter22(event):
        b22['activebackground']='#202024'
        
b22=Button(f2,text='        Click to PAUSE          ',bg='#33333d',fg='#ffffff',command=pause,relief=GROOVE)
b22['font']=myFont1
b22.grid(row=0,column=1)
b22.bind('<Leave>',onleave22)
b22.bind('<Enter>',onenter22)



#Creating a frame to add the "unpause" buttons in the player
f3=Frame(window)
f3.grid(column=1, row=10,pady=5)

#Creating a photoimage object to use image
unpause1=PhotoImage(file="C:\\unpause.png")

#Resizing image to fit on button
tunpause=unpause1.subsample(14,13)

def onleave3(event):
        b3['bg']='#f7d5f3'

def onenter3(event):
        b3['activebackground']='#f2b3eb'


b3=Button(f3,image=tunpause,bg='#f7d5f3',fg='#2d0636',command=unpause,relief=GROOVE)
b3.grid(row=0,column=0)
b3.config(image=tunpause)
b3.bind('<Leave>',onleave3)
b3.bind('<Enter>',onenter3)

def onleave33(event):
        b33['bg']='#33333d'

def onenter33(event):
        b33['activebackground']='#202024'

b33=Button(f3,text='      Click to UNPAUSE       ',bg='#33333d',fg='#ffffff',command=unpause,relief=GROOVE)
b33['font']=myFont1
b33.grid(row=0,column=1)
b33.bind('<Leave>',onleave33)
b33.bind('<Enter>',onenter33)



#Creating a frame to add the "stop" buttons in the player
f4=Frame(window)
f4.grid(column=1, row=12,pady=5)


#Creating a photoimage object to use image
stop1=PhotoImage(file="C:\\stop.png")

#Resizing image to fit on button
tstop=stop1.subsample(14,13)

def onleave4(event):
        b4['bg']='#d6d5f5'

def onenter4(event):
        b4['activebackground']='#bebcf5'


b4=Button(f4,image=tstop,bg='#d6d5f5',fg='#2d0636',command=stop,relief=GROOVE)
b4.grid(row=0,column=0)
b4.config(image=tstop)
b4.bind('<Leave>',onleave4)
b4.bind('<Enter>',onenter4)

def onleave44(event):
        b44['bg']='#33333d'

def onenter44(event):
        b44['activebackground']='#202024'

b44=Button(f4,text='         Click to STOP           ',bg='#33333d',fg='#ffffff',command=stop,relief=GROOVE)
b44['font']=myFont1
b44.grid(row=0,column=1)
b44.bind('<Leave>',onleave44)
b44.bind('<Enter>',onenter44)



#Creating a frame to add the "loop" buttons in the player
f5=Frame(window)
f5.grid(column=1, row=14,pady=5)

#Creating a photoimage object to use image
rewind1=PhotoImage(file="C:\\rewind.png")

#Resizing image to fit on button
trewind=rewind1.subsample(14,13)

def onleave5(event):
        b5['bg']='#e6d4fa'

def onenter5(event):
        b5['activebackground']='#ddc3fa'


b5=Button(f5,image=trewind,bg='#e6d4fa',fg='#2d0636',command=loop,relief=GROOVE)
b5.grid(row=0,column=0)
b5.config(image=trewind)
b5.bind('<Leave>',onleave5)
b5.bind('<Enter>',onenter5)

def onleave55(event):
        b55['bg']='#33333d'

def onenter55(event):
        b55['activebackground']='#202024'

b55=Button(f5,text='         Click to LOOP           ',bg='#33333d',fg='#ffffff',command=loop,relief=GROOVE)
b55['font']=myFont1
b55.grid(row=0,column=1)
b55.bind('<Leave>',onleave55)
b55.bind('<Enter>',onenter55)



#Creating a frame to add the "fast forward" buttons in the player
f6=Frame(window)
f6.grid(column=1, row=16,pady=5)

#Creating a photoimage object to use image
forward1=PhotoImage(file="C:\\forward.png")

#Resizing image to fit on button
tforward=forward1.subsample(14,13)

def onleave6(event):
        b6['bg']='#c9c5e8'

def onenter6(event):
        b6['activebackground']='#b7b1e3'

b6=Button(f6,image=tforward,bg='#c9c5e8',fg='#2d0636',command=forward,relief=GROOVE)
b6.grid(row=0,column=0)
b6.config(image=tforward)
b6.bind('<Leave>',onleave6)
b6.bind('<Enter>',onenter6)

def onleave66(event):
        b66['bg']='#33333d'

def onenter66(event):
        b66['activebackground']='#202024'

b66=Button(f6,text='Click to FAST FORWARD ',bg='#33333d',fg='#ffffff',command=forward,relief=GROOVE)
b66['font']=myFont1
b66.grid(row=0,column=1)
b66.bind('<Leave>',onleave66)
b66.bind('<Enter>',onenter66)



#Creating a frame to add the volume ajustment scale in the player
f7=Frame(window)
f7.grid(column=1, row=20,pady=5)

#Creating a photoimage object to use image
vol1=PhotoImage(file="C:\\volume.png")

#Resizing image to fit on button
tvol1=vol1.subsample(15,15)

l3=Label(f7,image=tvol1,bg='#c1b3c9')
l3.grid(row=0,column=0)
l3['font']=myFont3
l3.config(image=tvol1)

scale=Scale(f7,from_=0,to=100,orient=HORIZONTAL,activebackground='#cfc6cc' ,troughcolor='#25212b',cursor="dot",bg='#c1b3c9',fg='#2d0636',length=264,command=musicvolume)
scale.set(50)
scale.grid(row=0,column=1)


#Creating a dropdown list to select songs from
songs_list=os.listdir('C:\\new\\')
songs_listbox=StringVar(window)
songs_listbox.set("     CLICK TO SELECT A SONG FROM THE LIST  ")
menu=OptionMenu(window,songs_listbox,*songs_list)
menu.config(bg='#eddaf0')
menu["menu"].config(bg='#f1ebf5')
menu.grid(row=5,column=1,pady=15)




window.mainloop()
