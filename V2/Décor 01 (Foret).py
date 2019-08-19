## Ecrit sur Notepad++ et éxécuté avec Python 3.6 (64-bit)
## Groupe superdry (Pierre Cry et Matthias Ambroise)

from tkinter import *
from random import *

"""Ce programme consiste à créer le premier niveau, qui se situera sur une plage est une fôret.
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
                can.itemconfigure(img,image=fichier_imgg)
        
                
def droite(event):
        global img
        if x<1800:
                mouvement(50,0)
                can.itemconfigure(img,image=fichier_imgd)
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

M=[
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],[9,1,1,1,9,9,9,9,9,9,9,9,9,9,9],
[9,1,1,1,9,9,9,9,9,9,9,9,9,9,9],[9,8,1,8,9,9,9,9,9,9,9,9,9,9,9],
[9,8,1,8,9,9,9,9,8,10,10,10,10,8,9],[9,8,1,8,9,9,9,9,8,1,1,1,1,8,9],
[8,8,1,8,8,8,9,9,8,1,1,1,1,8,9],[8,1,1,1,1,8,9,9,8,8,8,1,1,8,9],
[8,1,1,1,1,8,9,9,9,9,8,1,1,8,9],[8,1,1,1,1,8,9,9,9,9,8,1,1,6,9],
[8,1,1,1,1,3,6,9,9,9,8,1,1,2,9],[8,1,1,1,1,8,2,9,9,9,8,8,8,2,9],
[8,1,1,1,1,8,2,9,9,9,9,9,8,2,9],[8,1,1,1,1,8,2,8,8,8,8,8,8,2,9],
[8,1,1,1,1,8,4,3,3,3,3,3,3,7,9],[8,1,1,1,1,8,8,8,8,1,1,1,1,8,9],
[8,1,1,1,1,8,9,9,8,1,1,8,8,9,9],[8,1,1,1,1,8,9,9,8,1,1,8,9,9,9],
[8,1,1,1,1,8,9,9,8,1,1,8,9,9,9],[8,1,1,1,1,8,9,9,8,1,1,8,9,9,9],
[8,1,1,1,1,8,9,9,8,1,1,8,9,9,9],[8,1,1,1,1,8,9,9,8,1,1,8,9,9,9],
[8,8,8,1,8,8,9,9,8,1,1,8,9,9,9],[9,9,8,1,8,9,9,9,8,1,1,8,9,9,9],
[9,9,8,1,8,9,9,9,8,10,10,8,9,9,9],[9,9,8,1,8,9,9,9,9,10,10,9,9,9,9],
[8,8,8,1,8,9,9,9,9,9,10,9,9,9,9],[8,1,1,1,10,9,9,9,10,10,10,10,9,9,9],
[8,1,1,1,10,9,9,9,10,10,10,10,9,9,9],[8,1,1,1,10,9,9,9,9,10,10,10,10,9,9],
[8,1,1,1,10,9,9,10,10,10,10,10,10,9,9],[8,1,1,1,10,9,9,9,10,10,10,10,10,9,9],
[8,1,1,1,10,9,9,9,9,9,9,9,9,9,9],[8,1,1,1,10,9,9,9,9,9,9,9,9,9,9],
[8,8,8,8,8,9,9,9,9,9,9,9,9,9,9]
]

for i in range(len(M)):
	for j in range(len(M[0])):
		if M[i][j]==1:
			can.create_image(125+50*i,125+50*j,image=d01)
		if M[i][j]==2:
			can.create_image(125+50*i,125+50*j,image=d02)
		if M[i][j]==3:
			can.create_image(125+50*i,125+50*j,image=d03)
		if M[i][j]==4:
			can.create_image(125+50*i,125+50*j,image=d04)
		if M[i][j]==5:
			can.create_image(125+50*i,125+50*j,image=d05)
		if M[i][j]==6:
			can.create_image(125+50*i,125+50*j,image=d06)
		if M[i][j]==7:
			can.create_image(125+50*i,125+50*j,image=d07)
		if M[i][j]==8:
			can.create_image(125+50*i,125+50*j,image=d08)
		if M[i][j]==9:
			can.create_image(125+50*i,125+50*j,image=d09)
		if M[i][j]==10:
			can.create_image(125+50*i,125+50*j,image=d10)



##### Programme principal #####

x=1625
y=625

#Perso
fichier_imgg=PhotoImage(file='Simon 1.gif')
fichier_imgd=PhotoImage(file='Simon 2.gif')
	
img=can.create_image(x,y,image=fichier_imgd)
can.pack()

fen.bind("<Left>", gauche)
fen.bind("<Right>", droite)
fen.bind("<Up>", haut)
fen.bind("<Down>", bas)

fen.mainloop()
