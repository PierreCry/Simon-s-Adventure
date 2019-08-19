## Ecrit sur Notepad++ et éxécuté avec Python 3.6 (64-bit)
## Groupe superdry (Pierre Cry et Matthias Ambroise)

from tkinter import *

#### Programme de déplacement ####

def mouvement(a,b):		##Fonction de mouvement qui sera appelé pour chaque déplacement
	global x, y, img
	x, y = x+a, y+b
	can.coords(img, x, y)
	

def gauche(event):				##Fonction pour le déplacement gauche
	if x>50:				##Condition pour éviter le dépassement
		mouvement(-10,0)	##Appel de la fonction mouvement
		
def droite(event):				##Fonction pour le déplacement gauche
	if x<450:
		mouvement(10, 0)
		
def haut(event):				##Fonction pour le déplacement gauche
	if y>50:
		mouvement(0, -10)
		
def bas(event):					##Fonction pour le déplacement gauche
	if y<450:
		mouvement(0, 10)


##### Programme principal #####

fen = Tk()
can = Canvas(fen, height=500, width=500)

x=50
y=50

fichier_img=PhotoImage(file='test.gif') #charger l'image depuis un fichier
img=can.create_image(x,y,image=fichier_img) #copie l'image sur le canevas 
can.pack()

fen.bind("<Left>", gauche)
fen.bind("<Right>", droite)
fen.bind("<Up>", haut)
fen.bind("<Down>", bas)

fen.mainloop()
