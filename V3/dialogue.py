## Ecrit sur Notepad++ et éxécuté avec Python 3.6 (64-bit)
## Groupe superdry (Pierre Cry et Matthias Ambroise)

from tkinter import *
from tkinter.filedialog import *
from random import *


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
        global txt, D1, cptd1, bouton1, bouton2
        can.delete(txt, bouton1, bouton2)
        
        if 0<=cptd1<3:
            txt=can.create_text(300,50, text=D1[cptd1])
        
        if cptd1==3:            
            bouton1 = Button(fen, text="Oui", command=choix1)
            bouton2 = Button(fen, text="Non", command=choix2)
            
            bouton1.pack()
            bouton2.pack()
            
        cptd1 = cptd1+1

def choix1():
    txt=can.create_text(300,50, text="lol")

def choix2():
    txt=can.create_text(300,50, text="mdr")

def enigme(event):
    global entree
    entree = Entry(fen)
    entree.pack()
        
    bou1 = Button(fen, text = 'valider', command = juste)
    bou1.pack()
    
def juste():
    global liste, entree
    liste.append(entree)
    if liste[0]==lol[0]:
        print("juste")
    else:
        print("fausse")
    
#### Création de l'environnement ####

fen = Tk()
can = Canvas(fen, height=500, width=500)

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

#Dialogue

txt=can.create_text(300,50, text="")
bouton1=Button(fen, text="")
bouton2=Button(fen, text="")
D1 = ["Bonjour", "Salut", "Yo"]
cptd1 = 0
var_texte = StringVar()
lol = [2]
liste=[]
entree=0
#Perso

fichier_imgg=PhotoImage(file='Personnages/Simon 1.gif')
fichier_imgd=PhotoImage(file='Personnages/Simon 2.gif')

img=can.create_image(x,y,image=fichier_imgd)
can.pack()

fen.bind("<q>", gauche)
fen.bind("<d>", droite)
fen.bind("<z>", haut)
fen.bind("<s>", bas)

fen.bind("<a>", dialogue)
fen.bind("<r>", enigme)

fen.mainloop()