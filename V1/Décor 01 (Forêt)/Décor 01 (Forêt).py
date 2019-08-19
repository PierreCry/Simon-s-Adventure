## Ecrit sur Notepad++ et éxécuté avec Python 3.6 (64-bit)
## Groupe superdry (Pierre Cry et Matthias Ambroise)

from tkinter import *
from random import *

"""Ce programme consiste à créer le premier niveau, qui se situera sur une plage et une forêt.
Ce code est le squelette du niveau"""

#### Programme de déplacement ####

def mouvement(a,b):
        global x, y, img
        x, y = x+a, y+b
        can.coords(img, x, y)
        

def gauche(event):
        global img
        if x>150:
                mouvement(-50,0)
                can.delete(img)
                img=can.create_image(x,y,image=fichier_imgg)
                
def droite(event):
        global img
        if x<1800:
                mouvement(50,0)
                can.delete(img)
                img=can.create_image(x,y,image=fichier_imgd)
def haut(event):
        global img
        if y>150:
                mouvement(0,-50)
                
def bas(event):
        global img
        if y<800:
                mouvement(0,50)
				

#### Création de l'environnement ####

fen = Tk()
can = Canvas(fen, height=1000, width=5000)

x0=100                  
y0=100

x1=150
y1=150

for j in range (35):
        for i in range (15):

                can.create_rectangle(x0, y0, x1, y1, fill="white")
                
                y0=y0+50
                y1=y1+50
				
        y0=100
        y1=150
        x0=x0+50
        x1=x1+50

##### Implémentation du décor #####

d01=PhotoImage(file='01 (herbe).gif')
d02=PhotoImage(file='02 (chemin horizontal).gif')
d03=PhotoImage(file='03 (chemin vertical).gif')
d04=PhotoImage(file='04 (gauche-bas).gif')
d05=PhotoImage(file='05 (droite-bas).gif')
d06=PhotoImage(file='06 (droite-haut).gif')
d07=PhotoImage(file='07 (gauche-haut).gif')
d08=PhotoImage(file='08 (arbre).gif')
d09=PhotoImage(file='09 (eau).gif')
d10=PhotoImage(file='10 (sable).gif')

## eau ##

for i in range(35):
	for j in range(15):
		can.create_image(125+50*i,125+50*j,image=d09)

## Plage de départ ##

for i in range(5):
	for j in range(3):
		can.create_image(1475+50*i,575+50*j,image=d10)

can.create_image(1475,525,image=d10)
can.create_image(1525,525,image=d10)
can.create_image(1625,525,image=d10)
can.create_image(1675,525,image=d10)
can.create_image(1625,475,image=d10)
can.create_image(1575,725,image=d10)
can.create_image(1625,725,image=d10)
can.create_image(1675,725,image=d10)
can.create_image(1425,625,image=d10)

for i in range(2):
	for j in range(2):
		can.create_image(1325+50*i,575+50*j,image=d10)
		
## chemin ##

for i in range(8):
	for j in range(2):
		can.create_image(925+50*i,575+50*j,image=d01)

for i in range(2):
	for j in range(7):
		can.create_image(825+50*i,425+50*j,image=d01)

for i in range(3):
	can.create_image(675+50*i,425,image=d02)

for j in range(5):
	can.create_image(825,475+50*j,image=d03)
	
can.create_image(825,425,image=d04)
can.create_image(625,425,image=d06)
can.create_image(625,375,image=d03)
can.create_image(825,725,image=d03)
can.create_image(825,775,image=d07)
can.create_image(575,775,image=d06)

for i in range(4):
	can.create_image(625+50*i,775,image=d02)

## fin du niveau ##

for i in range(4):
	for j in range(2):
		can.create_image(475+50*i,675+50*j,image=d01)

for i in range(2):
	for j in range(4):
		can.create_image(375+50*i,575+50*j,image=d01)
		
for j in range (4):
	can.create_image(325,575+50*j,image=d10)


## île ##

for i in range(7):
	can.create_image(1475+50*i,125,image=d08)
	
for j in range(5):
	can.create_image(1825,125+50*j,image=d08)
	
for i in range(7):
	for j in range(4):
		can.create_image(1475+50*i,175+50*j,image=d01)
	
for i in range(7):
	can.create_image(1475+50*i,325,image=d10)

## village ##

for i in range(15):
	for j in range(4):
		can.create_image(475+50*i,175+50*j,image=d01)
		
for i in range(2):
	for j in range(3):
		can.create_image(175+50*i,175+50*j,image=d01)
	
for i in range(4):
	can.create_image(275+50*i,225,image=d01)
	
for i in range(5):
	can.create_image(1225+50*i,275,image=d01)

## arbres ##

for i in range(9):
	can.create_image(925+50*i,525,image=d08)

for i in range(9):
	can.create_image(925+50*i,675,image=d08)
	
for i in range(12):
	can.create_image(675+50*i,375,image=d08)

for i in range(4):
	can.create_image(425+50*i,375,image=d08)
	
for i in range(17):
	can.create_image(425+50*i,125,image=d08)

for i in range(4):
	can.create_image(275+50*i,175,image=d08)
	
for i in range(4):
	can.create_image(275+50*i,275,image=d08)

for i in range(5):
	can.create_image(1225+50*i,325,image=d08)

for i in range(5):
	can.create_image(1225+50*i,225,image=d08)
	
for i in range(4):
	can.create_image(325+50*i,525,image=d08)
	
for i in range(5):
	can.create_image(475+50*i,625,image=d08)
	
for i in range(3):
	can.create_image(675+50*i,725,image=d08)

for i in range(5):
	can.create_image(325+50*i,775,image=d08)

for j in range(2):
	can.create_image(1425,125+50*j,image=d08)

for j in range(5):
	can.create_image(775,475+50*j,image=d08)
	
for j in range(3):
	can.create_image(875,425+50*j,image=d08)

can.create_image(425,325,image=d08)
can.create_image(1225,175,image=d08)
can.create_image(475,575,image=d08)
can.create_image(675,675,image=d08)
can.create_image(875,775,image=d08)
can.create_image(925,725,image=d08)

##### Programme principal #####

x=1625
y=625

#Perso
fichier_imgg=PhotoImage(file='profil gauche.gif')
fichier_imgd=PhotoImage(file='profil droite.gif')
	
img=can.create_image(x,y,image=fichier_imgd)
can.pack()

fen.bind("<Left>", gauche)
fen.bind("<Right>", droite)
fen.bind("<Up>", haut)
fen.bind("<Down>", bas)

fen.mainloop()