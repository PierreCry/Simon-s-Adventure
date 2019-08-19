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
                
def dialogue(event):
        global cpt, txt1, var_choix
        
        if x==275 and y==325:
                can.delete(txt1)
                txt1 = can.create_text(75, 60, text=D1[cpt], font="Arial 16 italic", fill="blue")
                cpt=cpt+1

        if cpt==3:
                b1 = button(fen, text="Rouge", command=var_choix==1)
                b2 = button(fen, text="Vert", command=var_choix==2)
                
                choix_rouge.pack()
                choix_vert.pack()
               
                if var_choix==1:
                        txt1 = can.create_text(75, 60, text="tg", font="Arial 16 italic", fill="blue")
                else:
                        txt1 = can.create_text(75, 60, text="lol", font="Arial 16 italic", fill="blue")
                

        
#### Création de l'environnement ####

fen = Tk()
can = Canvas(fen, height=400, width=400)

x0=100
y0=100

x1=150
y1=150

for j in range (10):
        for i in range (10):

                can.create_rectangle(x0, y0, x1, y1, fill="white")
                
                y0=y0+50
                y1=y1+50
				
        y0=100
        y1=150
        x0=x0+50
        x1=x1+50


##### Programme principal #####

p01=PhotoImage(file='Personnages/Magicien.gif')
img=can.create_image(275,325,image=p01)

x=125
y=125

#Perso
fichier_imgg=PhotoImage(file='Personnages/Simon 1.gif')
fichier_imgd=PhotoImage(file='Personnages/Simon 2.gif')

img=can.create_image(x,y,image=fichier_imgd)
can.pack()

D1=["Magicien: Tu es l'élu Simon",
"Simon: Quoi? Qu'est ce que se passe ici? Et je suis où là?",
"Magicien: Tu as été choisie pour vaincre le mal sans nom, le maitre de la"+ 
"mort! Le roi des cavaliers de l'apocalypse. Es-tu prêt pour une aventure"]
cpt=0
txt1=""

var_choix=0

fen.bind("<q>", gauche)
fen.bind("<d>", droite)
fen.bind("<z>", haut)
fen.bind("<s>", bas)

fen.bind("<a>", dialogue)

fen.mainloop()
