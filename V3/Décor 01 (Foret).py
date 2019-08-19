## Ecrit sur Notepad++ et éxécuté avec Python 3.6 (64-bit)
## Groupe superdry (Pierre Cry et Matthias Ambroise)

from tkinter import *
from random import *
import time

"""Ce programme consiste à créer le premier niveau, qui se situera sur une plage est une fôret.
Ce code est le squelette du niveau"""

#### Programme de déplacement ####

def mouvement(a,b):
        global x, y, img
        x, y = x+a, y+b
        if Mur(x,y)==True:
                can.coords(img, x, y)
        else:
                x,y=x-a, y-b
				
				
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

def Mur(x,y):
        global M
        i=(x-125)//50
        j=(y-125)//50
        if M[i][j]!= 8 and M[i][j]!=9:
                return True

def dialogue(event):
		global T
		if x==625 and y==325:
			for i in range (len(T)):
				txt1 = can.create_text(75, 60, text=T[i], font="Arial 16 italic", fill="blue")
				time.sleep(3)
				txt1 = can.create_text(75, 60, text=T[i], font="Arial 16 italic", fill="blue")


#### Création de l'environnement ####

fen = Tk()
can = Canvas(fen, height=1000, width=5000)

##### Implémentation du décor #####

d01=PhotoImage(file='Décors/01 (herbe).gif')
d02=PhotoImage(file='Décors/02 (chemin horizontal).gif')
d03=PhotoImage(file='Décors/03 (chemin vertical).gif')
d04=PhotoImage(file='Décors/04 (gauche-bas).gif')
d05=PhotoImage(file='Décors/05 (droite-bas).gif')
d06=PhotoImage(file='Décors/06 (droite-haut).gif')
d07=PhotoImage(file='Décors/07 (gauche-haut).gif')
d08=PhotoImage(file='Décors/08 (arbre).gif')
d09=PhotoImage(file='Décors/09 (eau).gif')
d10=PhotoImage(file='Décors/10 (sable).gif')

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

d=[d01,d02,d03,d04,d05,d06,d07,d08,d09,d10]

for i in range(len(M)):
	for j in range(len(M[0])):
			can.create_image(125+50*i,125+50*j,image=d[M[i][j]-1])

##### Placement des personnages #####

p01=PhotoImage(file='Personnages/Magicien.gif')
img=can.create_image(1425,625,image=p01)
p02=PhotoImage(file='Personnages/Garde.gif')
img=can.create_image(625,325,image=p02)
p03=PhotoImage(file='Personnages/Villageois.gif')
img=can.create_image(1525,225,image=p03)

##### Programme principal #####

T=["salut","sa va"]

x=1625
y=625

#Perso
fichier_imgg=PhotoImage(file='Personnages/Simon 1.gif')
fichier_imgd=PhotoImage(file='Personnages/Simon 2.gif')
	
img=can.create_image(x,y,image=fichier_imgg)
can.pack()

fen.bind("<Left>", gauche)
fen.bind("<Right>", droite)
fen.bind("<Up>", haut)
fen.bind("<Down>", bas)

fen.bind("<a>", dialogue)

fen.mainloop()