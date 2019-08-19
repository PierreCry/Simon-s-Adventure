## Ecrit sur Notepad++ et éxécuté avec Python 3.6 (64-bit)
## Groupe superdry (Pierre Cry et Matthias Ambroise)

from tkinter import *
from random import *

"""Ce programme consiste à créer un personnage (ici, on a pris un exemple en .gif) et le faire
se déplacer dans un environnement vierge sous forme de tableau"""

                #### Programme de déplacement ####

def mouvement(a,b):             ##Fonction de mouvement qui sera appelé pour chaque déplacement
        global x, y, img
        x, y = x+a, y+b
        can.coords(img, x, y)
        objet()
        sortie()
        

def gauche(event): ##Fonction pour le déplacement gauche
        global img
        if x>150:                               ##Condition pour éviter le dépassement
                mouvement(-50,0)
                can.delete(img)
                img=can.create_image(x,y,image=fichier_img) ##Appel de la fonction mouvement
                
def droite(event): ##Fonction pour le déplacement droit
        global img
        if x<550:
                mouvement(50, 0)
                can.delete(img)
                img=can.create_image(x,y,image=fichier_imgd)
def haut(event):          ##Fonction pour le déplacement supérieur
        global img
        if y>150:
                mouvement(0, -50)
                
def bas(event):                ##Fonction pour le déplacement inférieur
        global img
        if y<550:
                mouvement(0, 50)
                

def objet():
        if x == 275 and y == 325:
                can.delete(cle)
                can.create_rectangle(350,400,400,350,fill="green")
                
def sortie():
        if x==375 and y==375:
                #tex1 = Label(fen, text='Gagné', fg='red') ##creation widget
                #tex1.pack() ## on applique une méthode
                b=Button(fen,text="continuer",command=map1())
                b.pack()
def map1():
        global x0,y0,x1,y1,switch1,switch2
        can.delete(ALL)
                ##Création du tableau
        for j in range (n):
                for i in range (n): ## Boucle pour les colonnes
        
                ## Création du carré avec les coordonnées x0, y0, x1, y1 
                        can.create_rectangle(x0, y0, x1, y1, fill="white")
                
                ## Mise à jour des coordonnées sur l'axe des ordonnés
                        y0=y0+50
                        y1=y1+50
        
        ## Mise à jour des coordonées sur l'axe des abscisses
        y0=100
        y1=150
        x0=x0+50
        x1=x1+50
        switch2=switch2+1
        gauche(event)
        bas(event)
        haut(event)
        droite(event)


               
                           
                #### Création de l'environnement ####
                
## Définition des premières variables
x0=100                  
y0=100

x1=150
y1=150

n=10

switch1=0
switch2=0

fen = Tk()
can = Canvas(fen, height=600, width=600)

##Création du tableau
for j in range (n): ## Boucle pour les lignes
        for i in range (n): ## Boucle pour les colonnes
        
                ## Création du carré avec les coordonnées x0, y0, x1, y1 
                can.create_rectangle(x0, y0, x1, y1, fill="white")
                
                ## Mise à jour des coordonnées sur l'axe des ordonnés
                y0=y0+50
                y1=y1+50
        
        ## Mise à jour des coordonées sur l'axe des abscisses
        y0=100
        y1=150
        x0=x0+50
        x1=x1+50
        switch2=switch2+1



                ##### Programme principal #####

x=125
y=125

fichier_img=PhotoImage(file='profil gauche.gif')        #charger l'image depuis un fichier
fichier_imgd=PhotoImage(file='profil droite.gif')
img=can.create_image(x,y,image=fichier_img) #copie l'image sur le canevas 
clé_img=PhotoImage(file="cle.gif")
cle=can.create_image(275,325,image=clé_img)
can.pack()

fen.bind("<Left>", gauche)
fen.bind("<Right>", droite)
fen.bind("<Up>", haut)
fen.bind("<Down>", bas)

fen.mainloop()
