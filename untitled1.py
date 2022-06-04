# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 20:23:46 2022

@author: bekir
"""

import os
os.path.isdir("")

if os.path.exists('./logo.ic')==True:
    pass
    
else:
    pass


if os.path.isdir('./sorular')==True:
    pass
else:
    pass
    
if os.path.exists('./logo.ic')==True and os.path.exists('./sorular/1.mp3')==True and os.path.exists('./sorular/2.mp3')==True and os.path.exists('./sorular/3.mp3')==True and os.path.exists('./sorular/4.mp3')==True and os.path.exists('./sorular/arka.gif')==True and os.path.exists('./sorular/start.mp3')==True:
    h=0
else:
    print(" klasor yok")
    h=input("entere bas")

if os.path.exists('./logo.ico')==True:
    print("logo klasor var")

if os.path.exists('./sorular/1.mp3')==True:
    print("1 var")


if os.path.exists('./sorular/start.mp3')==True:
    print(" klasor var")
else:
    print(" klasor yok")
    