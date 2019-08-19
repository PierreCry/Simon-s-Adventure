## Ecrit sur Notepad++ et éxécuté avec Python 3.6 (64-bit)
## Groupe superdry (Pierre Cry et Matthias Ambroise)

from tkinter import *

"""Ce programme consiste à créer un personnage (ici, on a pris un exemple en .gif) et le faire
se déplacer dans un environnement vierge sous forme de tableau"""

		#### Programme de déplacement ####

def mouvement(a,b):		##Fonction de mouvement qui sera appelé pour chaque déplacement
	global x, y, img
	x, y = x+a, y+b
	can.coords(img, x, y)
	

def gauche(event):				##Fonction pour le déplacement gauche
	if x>150:				##Condition pour éviter le dépassement
		mouvement(-50,0)	##Appel de la fonction mouvement
		
def droite(event):				##Fonction pour le déplacement droit
	if x<550:
		mouvement(50, 0)
		
def haut(event):				##Fonction pour le déplacement supérieur
	if y>150:
		mouvement(0, -50)
		
def bas(event):					##Fonction pour le déplacement inférieur
	if y<550:
		mouvement(0, 50)
		

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
can = Canvas(fen, height=700, width=700)

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

fichier_img=PhotoImage(file='test.gif') #charger l'image depuis un fichier
img=can.create_image(x,y,image=fichier_img) #copie l'image sur le canevas 
can.pack()

fen.bind("<Left>", gauche)
fen.bind("<Right>", droite)
fen.bind("<Up>", haut)
fen.bind("<Down>", bas)

fen.mainloop()
