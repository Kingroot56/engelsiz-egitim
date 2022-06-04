# -*- coding: utf-8 -*-
from tkinter import Label, Tk 
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import time
from colorama import Fore,Back 
import random
from gtts import gTTS
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
r = sr.Recognizer()
from PIL.ImageTk import PhotoImage
import pygame
import os
try:
    import nin_nin
except:
    pass

pencere = Tk()
pygame.init()
pygame.mixer.init()
pencere.title("ENGELSİZ EĞİTİM")
pencere.iconbitmap("logo.ico")
pencere.geometry("300x150")
text_font= ("Boulder", 15, 'bold')
border_width = 30
b=1
ogrncicevap=[]
text_font_1= ("Boulder", 25, 'bold')
background_1 = "#f2e750"
foreground_1= "#363529"
border_width_1 = 60
dak=20
saniye=60

def varlik():
    if os.path.exists('./logo.ic')==True:
        print("var")
    else:
        print("yok")


    if os.path.isdir('./sorular')==True:
        print("var")
    else:
        print("yok")
        

def digital_clock():
    global dak,saniye,label,bildirim
    saniye-=1
    pencere.after(1000,digital_clock)
    if saniye!=0 and dak > -1:
        label = Label(pencere, font=text_font_1, bg=background_1,text=str(dak)+" : "+str(saniye)).grid(row=0, column=1)
        print(bildirim)
        print("Yapımcı github linki:https://github.com/Kingroot56")
    elif saniye==0:
        print("Kullandığınız için teşekkurler")
        dak-=1
        label = Label(pencere, font=text_font_1, bg=background_1,text=str(dak)+" : "+str(saniye)).grid(row=0, column=1)
        saniye=60
    elif dak==-1:
        label = Label(pencere, font=text_font_1, bg=background_1,text="SÜRENİZ BİTTİ").grid(row=0, column=1)
def girr(a):
     global digital_clock,sayac,img,text_font,img,border_width,label,cevap
     anahtar=["a","b","c"]
     pencere.resizable(width=FALSE, height=FALSE)
     pencere.state("zoomed")
     sorular=["""1.Mitoz bölünme sonrasında oluşan hücrelerle ana\nhücre arasında,verilenlerden hangisi mutasyonun olduğuna \ndair kesin kanıt oluşturur?""",
      """2.Mitoz bölünmede kalıtsal çeşitlilik oluşmamasının temel nedeni seçeneklerin\n hangisinde belirtilmiştir?""",
      """3.verilen canlılardan hangisinde rejenerasyonla çoğalma gözlenir?""",
      """4.Partenogenezle çoğalma aşağıda verilen canlılardan hangisinde görülmez?"""]
     cevap=["""A) Sitoplazma miktarının farklı olması\n
    B) Hücre büyüklüklerinin farklı olması\n
    C) Organel sayılarının farklı olması\n
    D) Aktif genlerin farklı olması\n""",
    """A) Sitokinez sonrasında iki hücrenin oluşması
    B) Profaz evresinde kromozomların iğ ipliklerine tutunması
    C) İnterfaz evresinde replikasyon ile DNA miktarının iki katına çıkması
    D) Anafaz evresinde kardeş kromatitlerin birbirinden ayrılması""",
    """A) Uğur böceği	 B)Kertenkele   C)Planarya    D)Ahtapot  """]
     img=PhotoImage(file="sorular/arka.gif")
     labelarka=Label(image=img).place(relx="0",rely="0")
     if a=="1":
         sor=Button(font=text_font,
                    text=sorular[0]+"\n"+cevap[0],
                    bd=border_width,
                    width=128,
                    height=34,
                    command=lambda:ses(a,35)).place(relx="0",rely="0")
     elif a=="2":
         sor=Button(font=text_font,
                    text=sorular[1]+"\n"+cevap[1],
                    bd=border_width,
                    width=128,
                    height=34,
                    command=lambda:ses(a,42)).place(relx="0",rely="0")
     elif a=="3":
         sor=Button(font=text_font,
                    text=sorular[2]+"\n"+cevap[2],
                    bd=border_width,
                    width=128,
                    height=34,
                    command=lambda:ses(a,17)).place(relx="0",rely="0")
     elif a=="4":
         dogru=0
         yanlis=0
         sayac=0
         for i in ogrncicevap:
             dogrusayisi="Hesaplanmadı"
             print(i)
             if i=="be":
                 if anahtar[sayac]=="b":
                     dogru+=1
                 else :
                     yanlis=1
             elif i=="ce":
                 if anahtar[sayac]=="c":
                     dogru+=1
                 else :
                     yanlis=1
             elif i=="de":
                 if anahtar[sayac]=="d":
                     dogru+=1
                 else :
                     yanlis=1
             elif i==anahtar[sayac]:
                 dogru+=1
             else:
                 yanlis+=1
             sayac+=1
         sor=Button(font=text_font,text="Sınavınız Bitti\n"+"Doğru Sayınız : "+str(dogru)+"\nYanlış Sayınız : "+str(yanlis),
                    bd=border_width,
                    width=128,
                    height=34).place(relx="0",rely="0")
r = sr.Recognizer()
def record(x,b,ask=False):
    global ogrncicevap
    time.sleep(int(b))
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice= r.recognize_google(audio, language='tr-Tr')
            print(voice)
            if voice=="a" or voice=="a" or voice=="be" or voice=="b" or voice=="c" or voice=="ce" or voice=="d" or voice=="de":    
                ogrncicevap.append(voice)
                b=int(x)+1
                print(ogrncicevap)
                
                girr(str(b))
            else:
                time.sleep(1)
                print("\a")
                time.sleep(1)
        except :
            print("ses yakalanamdı\a")
            time.sleep(1)
            print("\a")
            time.sleep(1)
            print("\a")
            time.sleep(1)
def close():
    global pencere
    if messagebox.askokcancel("DİKKAT", "Uygulama kapatılacak"):
        pencere.destroy()
def ses(s,b):
    if s=="1":
        pygame.mixer.music.load("sorular/1.mp3")
        pygame.mixer.music.play()
        record(s,b)
    if s=="2":
        pygame.mixer.music.load("sorular/2.mp3")
        pygame.mixer.music.play()
        record(s,b)
    if s=="3":
        pygame.mixer.music.load("sorular/3.mp3")
        pygame.mixer.music.play()
        record(s,b)
    if s=="4":
        pygame.mixer.music.load("sorular/4.mp3")
        pygame.mixer.music.play()
        record(s,b)    

girr(str(1))
pencere.after(1000,digital_clock)
pencere.protocol("WM_DELETE_WINDOW", close)
pencere.mainloop()