## Ecrit sur Notepad++ et éxécuté avec Python 3.6 (64-bit)
## Groupe superdry (Pierre Cry et Matthias Ambroise)

from tkinter import *
from random import *

"""Ce programme consiste à créer un nouveau niveau, qui se situera dans une grotte.
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
        if M[i][j]!= 108 and M[i][j]!=109:
                return True
				

#### Création de l'environnement ####

fen = Tk()
can = Canvas(fen, height=1000, width=5000)
	
	

##### Implémentation du décor #####

g101=PhotoImage(file='Décors/101 (sol rocheux).gif')
g108=PhotoImage(file='Décors/108 (rocher).gif')
g109=PhotoImage(file='Décors/109 (eau sombre).gif')
g104=PhotoImage(file='Décors/104 (gauche-bas).gif')
g105=PhotoImage(file='Décors/105 (droite-bas).gif')
g106=PhotoImage(file='Décors/106 (droite-haut).gif')
g107=PhotoImage(file='Décors/107 (gauche-haut).gif')
g102=PhotoImage(file='Décors/102 (chemin horizontal).gif')
g103=PhotoImage(file='Décors/103 (chemin vertical).gif')
g110=PhotoImage(file='Décors/110 (chemin horizontal eau).gif')
g111=PhotoImage(file='Décors/111 (chemin vertical eau).gif')
g112=PhotoImage(file='Décors/112 (droite-bas eau).gif')
g113=PhotoImage(file='Décors/113 (droite-haut eau).gif')
g114=PhotoImage(file='Décors/114 (gauche-bas eau).gif')
g115=PhotoImage(file='Décors/115 (gauche-haut eau).gif')
g116=PhotoImage(file='Décors/116 (gauche-bas-droite).gif')
g117=PhotoImage(file='Décors/117 (gauche-haut-droite).gif')
g118=PhotoImage(file='Décors/118 (haut-bas-droite).gif')
g119=PhotoImage(file='Décors/119 (haut-bas-gauche).gif')
g120=PhotoImage(file='Décors/120 (gauche-droite-bas eau).gif')
g121=PhotoImage(file='Décors/121 (gauche-droite-haut eau).gif')
g122=PhotoImage(file='Décors/122 (haut-bas-droite eau).gif')
g123=PhotoImage(file='Décors/123 (haut-bas-gauche eau).gif')





M=[
[108, 108, 108, 108, 108, 108, 108, 102, 108, 108, 108, 108, 108, 108, 108], [108, 108, 108, 108, 108, 108, 108, 102, 108, 108, 108, 108, 108, 108, 108], 
[108, 105, 103, 103, 106, 108, 108, 104, 103, 103, 106, 108, 108, 102, 108], [108, 102, 108, 108, 102, 108, 108, 108, 108, 108, 102, 108, 108, 102, 108], 
[108, 102, 108, 108, 102, 108, 108, 108, 108, 108, 102, 108, 108, 102, 108], [108, 116, 103, 103, 119, 103, 103, 103, 118, 103, 107, 108, 108, 102, 108], 
[108, 102, 108, 108, 108, 108, 108, 108, 102, 108, 108, 108, 108, 102, 108], [108, 102, 108, 108, 108, 108, 105, 103, 119, 103, 103, 103, 103, 107, 108], 
[108, 102, 108, 108, 108, 108, 102, 108, 108, 108, 108, 108, 108, 108, 108], [108, 104, 103, 103, 103, 108, 102, 108, 108, 108, 108, 108, 108, 108, 108], 
[108, 108, 108, 108, 109, 109, 104, 103, 103, 103, 103, 103, 106, 108, 108], [108, 109, 109, 109, 109, 109, 109, 109, 108, 108, 108, 108, 102, 108, 108], 
[102, 109, 109, 109, 109, 109, 109, 109, 105, 103, 103, 103, 107, 108, 108], [102, 109, 109, 109, 109, 109, 109, 109, 102, 108, 108, 108, 108, 102, 108], 
[102, 109, 109, 109, 109, 109, 109, 109, 104, 103, 106, 108, 108, 102, 108], [102, 109, 109, 109, 109, 109, 109, 109, 108, 108, 102, 108, 108, 102, 108], 
[102, 108, 108, 108, 109, 109, 108, 108, 108, 108, 102, 108, 108, 102, 108], [102, 108, 102, 108, 102, 108, 102, 108, 102, 108, 102, 108, 108, 102, 108], 
[116, 103, 119, 118, 119, 118, 119, 118, 119, 118, 119, 103, 103, 117, 108], [102, 108, 108, 102, 108, 102, 108, 102, 108, 102, 108, 108, 108, 102, 108], 
[102, 108, 108, 102, 108, 102, 108, 102, 108, 102, 108, 108, 108, 102, 108], [102, 108, 108, 102, 108, 102, 108, 102, 108, 102, 108, 108, 108, 102, 108], 
[102, 108, 108, 102, 108, 102, 108, 102, 108, 102, 108, 108, 108, 102, 108], [102, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 102, 108], 
[116, 103, 103, 103, 103, 103, 103, 106, 108, 108, 108, 108, 108, 108, 108], [102, 108, 108, 109, 109, 109, 109, 110, 109, 111, 111, 113, 108, 108, 108], 
[102, 108, 108, 109, 109, 109, 109, 110, 109, 109, 109, 110, 108, 108, 108], [102, 108, 108, 109, 109, 109, 109, 110, 109, 109, 109, 110, 108, 108, 108], 
[102, 108, 108, 109, 109, 109, 109, 110, 109, 109, 109, 110, 108, 108, 108], [104, 103, 103, 111, 111, 111, 111, 123, 111, 113, 109, 110, 108, 108, 108], 
[108, 108, 108, 109, 109, 109, 109, 109, 109, 110, 109, 110, 108, 108, 108], [108, 108, 108, 109, 109, 109, 109, 109, 109, 110, 109, 110, 108, 108, 108], 
[108, 108, 108, 109, 109, 109, 109, 109, 109, 110, 109, 110, 108, 108, 108], [108, 108, 108, 109, 111, 111, 111, 111, 111, 123, 111, 115, 108, 108, 108], 
[108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108]]


g=[g101,g102,g103,g104,g105,g106,g107,g108,g109,
g110,g111,g112,g113,g114,g115,g116,g117,g118,g119,
g120,g121,g122,g123]

for i in range(len(M)):
	for j in range(len(M[0])):
			can.create_image(125+50*i,125+50*j,image=g[M[i][j]-101])
			
#### Placement des objets ####

o01=PhotoImage(file='Objets/Note.gif')
img=can.create_image(1275,775,image=o01)
img=can.create_image(1775,325,image=o01)
img=can.create_image(725,125,image=o01)
o02=PhotoImage(file='Objets/Clé.gif')
img=can.create_image(575,325,image=o02)
img=can.create_image(225,775,image=o02)
img=can.create_image(1225,375,image=o02)


##### Programme principal #####

x=125
y=475

#Perso
fichier_imgg=PhotoImage(file='Personnages/Simon 1.gif')
fichier_imgd=PhotoImage(file='Personnages/Simon 2.gif')
	
img=can.create_image(x,y,image=fichier_imgd)
can.pack()

fen.bind("<Left>", gauche)
fen.bind("<Right>", droite)
fen.bind("<Up>", haut)
fen.bind("<Down>", bas)

fen.mainloop()
