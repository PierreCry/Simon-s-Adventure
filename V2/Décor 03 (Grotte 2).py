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

"""x0=0                  
y0=0

x1=50
y1=50

for j in range (35):
        for i in range (15):

                can.create_rectangle(x0, y0, x1, y1, fill="white")
                
                y0=y0+50
                y1=y1+50
				
        y0=100
        y1=150
        x0=x0+50
        x1=x1+50"""
	
	

##### Implémentation du décor #####

#Grotte
g108=PhotoImage(file='108 (rocher).gif')
g101=PhotoImage(file='101 (sol rocheux).gif')
g102=PhotoImage(file='102 (chemin horizontal).gif')
g103=PhotoImage(file='103 (chemin vertical).gif')
g109=PhotoImage(file='109 (eau sombre).gif')
g111=PhotoImage(file='111 (chemin horizontal eau).gif')
g112=PhotoImage(file='112 (chemin vertical eau).gif')

#Virage
g104=PhotoImage(file='104 (gauche-bas).gif')
g107=PhotoImage(file='107 (gauche-haut).gif')
g105=PhotoImage(file='105 (droite-bas).gif')
g106=PhotoImage(file='106 (droite-haut).gif')

g115=PhotoImage(file='115 (gauche-bas eau).gif')
g116=PhotoImage(file='116 (gauche-haut eau).gif')
g113=PhotoImage(file='113 (droite-bas eau).gif')
g114=PhotoImage(file='114 (droite-haut eau).gif')

g125=PhotoImage(file='125 (haut-bas-gauche eau).gif')
g123=PhotoImage(file='123 (gauche-droite-haut eau).gif')
g124=PhotoImage(file='124 (haut-bas-droite eau).gif')
g122=PhotoImage(file='122 (gauche-droite-bas eau).gif')

g119=PhotoImage(file='119 (haut-bas-droite).gif')
g118=PhotoImage(file='118 (gauche-haut-droite).gif')
g121=PhotoImage(file='121 (haut-bas-gauche).gif')
g117=PhotoImage(file='117 (gauche-bas-droite).gif')	



M=[
[108, 108, 108, 108, 108, 108, 108, 102, 108, 108, 108, 108, 108, 108, 108], [108, 108, 108, 108, 108, 108, 108, 102, 108, 108, 108, 108, 108, 108, 108], 
[108, 108, 108, 108, 108, 108, 108, 102, 108, 108, 105, 103, 103, 106, 108], [108, 102, 108, 108, 105, 103, 103, 107, 108, 108, 102, 108, 108, 102, 108], 
[108, 102, 108, 108, 102, 108, 108, 108, 108, 108, 102, 108, 108, 102, 108], [108, 117, 103, 103, 121, 103, 103, 103, 103, 103, 107, 108, 108, 102, 108], 
[108, 102, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 102, 108], [108, 102, 108, 108, 108, 108, 105, 103, 103, 103, 103, 103, 103, 107, 108], 
[108, 102, 108, 108, 108, 108, 102, 108, 108, 108, 108, 108, 108, 108, 108], [108, 104, 103, 103, 103, 108, 102, 108, 108, 108, 108, 108, 108, 108, 108], 
[108, 108, 108, 108, 109, 109, 111, 108, 108, 108, 108, 108, 108, 108, 108], [108, 108, 108, 108, 109, 109, 111, 108, 108, 108, 108, 108, 108, 108, 108], 
[108, 108, 108, 105, 112, 112, 125, 112, 103, 103, 103, 103, 103, 106, 108], [108, 108, 108, 102, 109, 109, 109, 109, 108, 108, 108, 108, 108, 102, 108], 
[105, 103, 103, 121, 103, 103, 103, 119, 103, 103, 106, 108, 108, 102, 108], [102, 108, 108, 108, 108, 108, 108, 102, 108, 108, 102, 108, 108, 102, 108], 
[102, 108, 108, 108, 108, 108, 108, 102, 108, 108, 102, 108, 108, 102, 108], [102, 108, 108, 108, 108, 108, 108, 102, 108, 108, 102, 108, 108, 102, 108], 
[102, 108, 108, 108, 108, 108, 108, 102, 108, 108, 104, 103, 103, 118, 108], [102, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 102, 108], 
[102, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 102, 108], [102, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 102, 108], 
[102, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 102, 108], [102, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 108, 102, 108], 
[104, 103, 112, 112, 124, 112, 112, 114, 108, 108, 108, 108, 108, 108, 108], [108, 108, 109, 109, 111, 109, 109, 115, 112, 112, 112, 114, 108, 108, 108], 
[108, 108, 109, 109, 111, 109, 109, 109, 109, 109, 109, 111, 108, 108, 108], [108, 108, 109, 109, 122, 112, 112, 112, 112, 109, 109, 111, 108, 108, 108], 
[108, 108, 109, 109, 111, 109, 109, 109, 109, 109, 109, 111, 108, 108, 108], [108, 108, 109, 109, 111, 109, 109, 109, 109, 109, 109, 111, 108, 108, 108], 
[108, 108, 109, 109, 111, 109, 109, 109, 109, 109, 109, 111, 108, 108, 108], [108, 108, 108, 108, 108, 108, 108, 105, 112, 112, 112, 116, 108, 108, 108], 
[108, 108, 108, 108, 108, 108, 108, 102, 108, 108, 108, 108, 108, 108, 108], [108, 108, 108, 108, 108, 108, 108, 102, 108, 108, 108, 108, 108, 108, 108], 
[108, 108, 108, 108, 108, 108, 108, 102, 108, 108, 108, 108, 108, 108, 108]]


for i in range(len(M)):
	for j in range(len(M[0])):
		
		if M[i][j]==102:
			can.create_image(125+50*i,125+50*j,image=g102)
		if M[i][j]==103:
			can.create_image(125+50*i,125+50*j,image=g103)
		if M[i][j]==104:
			can.create_image(125+50*i,125+50*j,image=g104)
		if M[i][j]==105:
			can.create_image(125+50*i,125+50*j,image=g105)
		if M[i][j]==106:
			can.create_image(125+50*i,125+50*j,image=g106)
		if M[i][j]==107:
			can.create_image(125+50*i,125+50*j,image=g107)
		if M[i][j]==108:
			can.create_image(125+50*i,125+50*j,image=g108)
		if M[i][j]==109:
			can.create_image(125+50*i,125+50*j,image=g109)
		if M[i][j]==111:
			can.create_image(125+50*i,125+50*j,image=g111)
		if M[i][j]==112:
			can.create_image(125+50*i,125+50*j,image=g112)
		if M[i][j]==113:
			can.create_image(125+50*i,125+50*j,image=g113)
		if M[i][j]==114:
			can.create_image(125+50*i,125+50*j,image=g114)
		if M[i][j]==115:
			can.create_image(125+50*i,125+50*j,image=g115)
		if M[i][j]==116:
			can.create_image(125+50*i,125+50*j,image=g116)
		if M[i][j]==117:
			can.create_image(125+50*i,125+50*j,image=g117)
		if M[i][j]==118:
			can.create_image(125+50*i,125+50*j,image=g118)
		if M[i][j]==119:
			can.create_image(125+50*i,125+50*j,image=g119)
		if M[i][j]==121:
			can.create_image(125+50*i,125+50*j,image=g121)
		if M[i][j]==122:
			can.create_image(125+50*i,125+50*j,image=g122)	
		if M[i][j]==123:
			can.create_image(125+50*i,125+50*j,image=g123)
		if M[i][j]==124:
			can.create_image(125+50*i,125+50*j,image=g124)
		if M[i][j]==125:
			can.create_image(125+50*i,125+50*j,image=g125)
			


	
##### Programme principal #####

x=125
y=475



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
