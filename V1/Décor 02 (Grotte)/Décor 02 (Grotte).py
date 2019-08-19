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

#Grotte
fichier_roche=PhotoImage(file='18 (rocher).gif')
fichier_sol=PhotoImage(file='11 (sol rocheux).gif')
fichier_cheminh=PhotoImage(file='12 (chemin horizontal).gif')
fichier_cheminv=PhotoImage(file='13 (chemin vertical).gif')
fichier_eau=PhotoImage(file='19 (eau sombre).gif')
fichier_cheminheau=PhotoImage(file='cheminheau.gif')
fichier_cheminveau=PhotoImage(file='cheminveau.gif')

#Virage
fichier_virgb=PhotoImage(file='14 (gauche-bas).gif')
fichier_virgh=PhotoImage(file='17 (gauche-haut).gif')
fichier_virdb=PhotoImage(file='15 (droite-bas).gif')
fichier_virdh=PhotoImage(file='16 (droite-haut).gif')

fichier_virgbeau=PhotoImage(file='gbeau.gif')
fichier_virgheau=PhotoImage(file='gheau.gif')
fichier_virdbeau=PhotoImage(file='dbeau.gif')
fichier_virdheau=PhotoImage(file='dheau.gif')

fichier_doublevirhbgeau=PhotoImage(file='doublevhbgeau.gif')
fichier_doublevirgdheau=PhotoImage(file='doublevgdheau.gif')
fichier_doublevirhbdeau=PhotoImage(file='doublevhbdeau.gif')
fichier_doublevirgdbeau=PhotoImage(file='doublevgdbeau.gif')

fichier_doublevirhbd=PhotoImage(file='doublevhbd.gif')
fichier_doublevirgdh=PhotoImage(file='doublevgdh.gif')
fichier_doublevirhbg=PhotoImage(file='doublevhbg.gif')
fichier_doublevirgdb=PhotoImage(file='doublevgdb.gif')	
	
#Rocher/Eau
for i in range(35):
	can.create_image(125+50*i,825,image=fichier_roche)

for i in range(3):
	for j in range(7):
		can.create_image(125+50*i,125+50*j,image=fichier_roche)
		can.create_image(1725+50*i,525+50*j,image=fichier_roche)
		
for i in range(5):
	for j in range(12):
		can.create_image(1075+50*i,175+50*j,image=fichier_roche)
		can.create_image(325,375+50*i,image=fichier_roche)
		can.create_image(425,425+50*i,image=fichier_roche)
		
for i in range(4):
	for j in range(7):
		can.create_image(525+50*i,475+50*j,image=fichier_roche)
		can.create_image(1675+50*i,125+50*j,image=fichier_roche)

for i in range(8):
	for j in range(2):
		can.create_image(1325+50*i,725+50*j,image=fichier_roche)
		can.create_image(225+50*i,125,image=fichier_roche)
		can.create_image(825+50*i,675,image=fichier_roche)
		
for i in range(4):
	for j in range(4):
		can.create_image(875+50*i,175+50*j,image=fichier_roche)	
		can.create_image(775,325+50*j,image=fichier_eau)	
		can.create_image(775,525+50*j,image=fichier_roche)	
		
for i in range(2):
	for j in range(6):
		can.create_image(125+50*i,525+50*j,image=fichier_roche)	
		can.create_image(1375+50*j,125+50*i,image=fichier_roche)	
		can.create_image(1375+50*j,225+50*i,image=fichier_eau)	
		
		can.create_image(725+50*i,225,image=fichier_roche)	
		
for i in range(3):
	for j in range(4):
		can.create_image(425+50*i,225+50*j,image=fichier_roche)	
		can.create_image(1525+50*i,475+50*j,image=fichier_eau)	
		can.create_image(775+50*i,725,image=fichier_roche)	
		
for i in range(2):
	for j in range(2):
		can.create_image(275+50*i,225+50*j,image=fichier_roche)	
		can.create_image(225+50*i,525+50*j,image=fichier_roche)	
		can.create_image(625+50*i,325+50*j,image=fichier_eau)	
		can.create_image(925+50*i,675+50*j,image=fichier_roche)		
		can.create_image(1425+50*i,575+50*j,image=fichier_eau)
		can.create_image(625+50*i,225+50*j,image=fichier_roche)	
		can.create_image(1375+50*i,375+50*j,image=fichier_eau)	
		can.create_image(1525+50*i,375+50*j,image=fichier_eau)	

for i in range(4):
	for j in range(2):
		can.create_image(625+50*i,125+50*j,image=fichier_roche)	
		can.create_image(275+50*i,675+50*j,image=fichier_roche)	
		can.create_image(875+50*i,525+50*j,image=fichier_roche)	
		can.create_image(1325,525+50*i,image=fichier_roche)	
		can.create_image(1425,475+50*j,image=fichier_eau)	
		can.create_image(1625,375+50*j,image=fichier_eau)	
		can.create_image(875+50*i,375+50*j,image=fichier_roche)
		
#Chemin
for i in range(3):
	can.create_image(125+50*i,475,image=fichier_cheminh)
	can.create_image(425+50*i,175,image=fichier_cheminh)
	can.create_image(875+50*i,625,image=fichier_cheminh)
	can.create_image(825,325+50*i,image=fichier_cheminv)
	can.create_image(1725+50*i,475,image=fichier_cheminh)	
	can.create_image(1375,525+50*i,image=fichier_cheminveau)	
	can.create_image(1525+50*i,325,image=fichier_cheminheau)
	can.create_image(1675,525+50*i,image=fichier_cheminveau)
	
for i in range(2):
	can.create_image(275,375+50*i,image=fichier_cheminv)
	can.create_image(375,225+50*i,image=fichier_cheminv)	
	can.create_image(275+50*i,625,image=fichier_cheminh)
	can.create_image(275+50*i,175,image=fichier_cheminh)
	can.create_image(225,675+50*i,image=fichier_cheminv)
	can.create_image(525+50*i,425,image=fichier_cheminh)
	can.create_image(625+50*i,425,image=fichier_cheminheau)
	can.create_image(725,325+50*i,image=fichier_cheminveau)
	can.create_image(825,175+50*i,image=fichier_cheminv)
	can.create_image(825,525+50*i,image=fichier_cheminv)
	can.create_image(1025,675+50*i,image=fichier_cheminv)
	can.create_image(1325,225+50*i,image=fichier_cheminveau)
	can.create_image(1325,375+50*i,image=fichier_cheminveau)
	can.create_image(1375+50*i,325,image=fichier_cheminheau)
		
for i in range(5):
	can.create_image(375,375+50*i,image=fichier_cheminv)
	can.create_image(725,525+50*i,image=fichier_cheminv)
	can.create_image(775+50*i,775,image=fichier_cheminh)
	can.create_image(1425+50*i,675,image=fichier_cheminheau)
	can.create_image(1075+50*i,775,image=fichier_cheminh)
	
for i in range(4):
	can.create_image(275+50*i,775,image=fichier_cheminh)
	can.create_image(875+50*i,475,image=fichier_cheminh)
	can.create_image(1475,375+50*i,image=fichier_cheminveau)
	can.create_image(575,225+50*i,image=fichier_cheminv)
	
for i in range(6):
	can.create_image(475,475+50*i,image=fichier_cheminv)
	
for i in range (9):
	can.create_image(875+50*i,125,image=fichier_cheminh)


can.create_image(275,475,image=fichier_virgh)
can.create_image(275,325,image=fichier_virdb)
can.create_image(325,325,image=fichier_cheminh)
can.create_image(375,325,image=fichier_doublevirhbg)
can.create_image(375,175,image=fichier_doublevirgdb)
can.create_image(575,175,image=fichier_virgb)
can.create_image(375,625,image=fichier_virgh)
can.create_image(225,625,image=fichier_virdb)
can.create_image(225,775,image=fichier_virdh)
can.create_image(475,775,image=fichier_virgh)
can.create_image(475,425,image=fichier_virdb)
can.create_image(725,425,image=fichier_doublevirhbgeau)
can.create_image(725,275,image=fichier_virdb)
can.create_image(775,275,image=fichier_cheminh)
can.create_image(825,275,image=fichier_doublevirhbg)
can.create_image(725,475,image=fichier_cheminveau)
can.create_image(725,775,image=fichier_virdh)
can.create_image(1025,775,image=fichier_doublevirgdh)
can.create_image(1025,625,image=fichier_virgb)
can.create_image(825,475,image=fichier_doublevirhbd)
can.create_image(825,625,image=fichier_virdh)
can.create_image(825,125,image=fichier_virdb)
can.create_image(1325,125,image=fichier_virgb)
can.create_image(1325,175,image=fichier_cheminv)
can.create_image(1325,325,image=fichier_doublevirhbdeau)
can.create_image(1325,475,image=fichier_virdheau)
can.create_image(1375,475,image=fichier_virgbeau)
can.create_image(1375,675,image=fichier_virdheau)
can.create_image(1475,325,image=fichier_doublevirgdbeau)
can.create_image(1675,675,image=fichier_virgheau)
can.create_image(1675,475,image=fichier_virdbeau)

##### Programme principal #####

x=125
y=475

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