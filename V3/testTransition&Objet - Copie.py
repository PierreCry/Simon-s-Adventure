from tkinter import *
from random import *


##Création des décors##

def decor(M, d):
    for i in range(len(M)):
        for j in range(len(M[0])):
            can.create_image(125 + 50 * i, 125 + 50 * j, image=d[M[i][j] - 1])

def Map1():
    global x,y,img
    #Décor#
    decor(M[0],d)
    #Simon#
    x = 1075
    y = 575
    img = can.create_image(x, y, image=fichier_imgd)
    #Personnages#
    imgp01=can.create_image(1425,625,image=p01)    
    imgp02=can.create_image(625,325,image=p02)
    imgp03=can.create_image(1525,225,image=p03)

def Map2():
    global x,y,img
    can.delete(img)
    #Décor#
    decor(M[1], d)
    #Simon#
    x=125
    y=475
    img = can.create_image(x, y, image=fichier_imgd)
    #Personnages et Objets#
    imgp01=can.create_image(475,475,image=p01)
    imgo01=can.create_image(525,775,image=o01)
    imgo02=can.create_image(975,125,image=o02)
    imgo03=can.create_image(1375,475,image=o03)
    imgo04=can.create_image(275,275,image=o04)
    imgo05=can.create_image(275,675,image=o05)

def Map3():
    global x,y,img
    can.delete(img)
    #Décor#
    decor(M[2], d)
    #Simon#
    x=125
    y=475
    img = can.create_image(x, y, image=fichier_imgd)
    #Objets#
    imgo06=can.create_image(1275,775,image=o06)
    imgo07=can.create_image(1825,475,image=o07)
    imgo08=can.create_image(1475,525,image=o08)
    imgo09=can.create_image(575,325,image=o09) 
    imgo10=can.create_image(1025,475,image=o10)

def Map4():
    global x,y,img
    can.delete(img)
    #Décor#
    decor(M[3], d)
    #Simon#
    x=125
    y=475
    img = can.create_image(x, y, image=fichier_imgd)
    #Objets#
    imgo11=can.create_image(1275,775,image=o11)
    imgo11=can.create_image(1775,325,image=o11)
    imgo11=can.create_image(725,125,image=o11)
    imgo02=can.create_image(575,325,image=o02)
    imgo02=can.create_image(225,775,image=o02)
    imgo02=can.create_image(1225,375,image=o02)


##Fonction qui gère les transitions##
    
def transition(event):
    global x, y, img, cptmap
    if cptmap == -1:
        Map1()
        cptmap = cptmap + 1
    if cptmap == 0 and (x==225 and y==225):
        Map2()
        cptmap = cptmap + 1
    if cptmap == 0 and (x==425 and y==625):
        Map3()
        cptmap = cptmap + 2
    if cptmap == 0 and (x==1675 and y==225):
        Map4()
        cptmap = cptmap + 3
    if cptmap == 2 and x== 275 and y == 475:
        Map1()
        cptmap = 0
    


##Fonctions de mouvement##

def mouvement(a, b):
    global x, y, img, M
    x, y = x + a, y + b
    if collision(x,y)==True:
        can.coords(img, x, y) 
    else:
        x,y=x-a, y-b
        
def gauche(event):
    global img, x, y
    if x > 150:
        mouvement(-50, 0)
        can.itemconfigure(img, image=fichier_imgg)

def droite(event):
    global img, x, y
    if x < 1800:
        mouvement(50, 0)
        can.itemconfigure(img, image=fichier_imgd)

def haut(event):
    global img, x, y
    if y > 150:
        mouvement(0, -50)


def bas(event):
    global img, x, y
    if y < 800:
        mouvement(0, 50)


##Fonction de collision##

def collision(x,y):
        global M, cptmap
        MUR =[8,9,18,19]
        i=(x-125)//50
        j=(y-125)//50
        if M[cptmap][i][j] not in MUR:
            return True

##Matrices des décors##

M=[
        [[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],[9,1,1,1,9,9,9,9,9,9,9,9,9,9,9],
        [9,1,34,1,9,9,9,9,9,9,9,9,9,9,9],[9,8,1,8,9,9,9,9,9,9,9,9,9,9,9],
        [9,8,1,8,9,9,9,9,8,10,10,10,10,8,9],[9,8,1,8,9,9,9,9,8,1,1,1,1,8,9],
        [8,8,1,8,8,8,9,9,8,1,34,1,1,8,9],[8,1,1,1,1,8,9,9,8,8,8,1,1,8,9],
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
        [8,1,1,1,10,9,9,10,10,10,10,10,10,9,9],[8,1,34,1,10,9,9,9,10,10,10,10,10,9,9],
        [8,1,1,1,10,9,9,9,9,9,9,9,9,9,9],[8,1,1,1,10,9,9,9,9,9,9,9,9,9,9],
        [8,8,8,8,8,9,9,9,9,9,9,9,9,9,9]],
        
        [[18, 18, 18, 18, 18, 18, 18, 11, 18, 18, 18, 18, 18, 18, 18], [18, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 18], 
        [18, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 18], [18, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 18], 
        [18, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 18], [18, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 18], 
        [18, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 18], [18, 18, 18, 18, 18, 18, 18, 11, 18, 18, 18, 18, 18, 18, 18], 
        [18, 19, 19, 19, 19, 18, 11, 11, 11, 11, 18, 18, 18, 11, 18], [18, 19, 19, 19, 19, 18, 11, 11, 11, 11, 18, 18, 18, 11, 18], 
        [18, 19, 19, 19, 19, 18, 11, 11, 11, 11, 18, 18, 18, 11, 18], [18, 19, 19, 19, 19, 18, 11, 11, 11, 11, 18, 18, 18, 11, 18], 
        [18, 19, 19, 19, 19, 18, 11, 11, 11, 11, 18, 18, 18, 11, 18], [18, 18, 19, 19, 18, 11, 11, 11, 11, 11, 18, 18, 18, 11, 18], 
        [18, 19, 19, 19, 18, 11, 11, 11, 11, 11, 11, 11, 11, 11, 18], [18, 19, 19, 18, 18, 18, 18, 11, 11, 11, 11, 18, 18, 18, 18], 
        [18, 19, 19, 19, 19, 19, 18, 11, 11, 11, 11, 11, 11, 11, 18], [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 18, 18, 18, 18], 
        [18, 19, 19, 19, 19, 19, 18, 11, 18, 18, 11, 11, 11, 11, 18], [18, 19, 19, 19, 19, 19, 18, 18, 18, 11, 11, 11, 11, 11, 18], 
        [18, 19, 19, 19, 19, 19, 18, 18, 18, 18, 18, 18, 18, 11, 18], [18, 19, 19, 19, 19, 19, 18, 18, 18, 18, 11, 11, 11, 11, 18], 
        [18, 19, 19, 19, 19, 19, 18, 18, 18, 18, 18, 18, 18, 11, 18], [18, 19, 19, 19, 19, 19, 18, 18, 18, 18, 18, 18, 18, 11, 18], 
        [18, 19, 19, 19, 19, 19, 18, 18, 18, 18, 18, 18, 18, 11, 18], [18, 19, 19, 19, 19, 19, 18, 11, 18, 18, 18, 18, 18, 11, 18], 
        [18, 19, 19, 19, 19, 19, 18, 11, 18, 18, 18, 18, 18, 11, 18], [18, 19, 19, 19, 19, 19, 18, 11, 18, 18, 18, 18, 18, 11, 18], 
        [18, 19, 19, 19, 19, 19, 18, 11, 18, 18, 11, 11, 11, 11, 18], [18, 19, 19, 19, 19, 19, 18, 11, 18, 18, 11, 11, 11, 11, 18], 
        [18, 18, 18, 18, 18, 18, 18, 11, 11, 11, 11, 11, 11, 18, 18], [18, 18, 18, 18, 18, 18, 18, 11, 18, 18, 11, 11, 18, 18, 18], 
        [18, 18, 18, 18, 18, 18, 18, 11, 18, 18, 11, 11, 18, 18, 18], [18, 18, 18, 18, 18, 18, 18, 11, 11, 11, 11, 11, 18, 18, 18], 
        [18, 18, 18, 18, 18, 18, 18, 11, 18, 18, 18, 18, 18, 18, 18]],
                
        [[18, 18, 18, 18, 18, 18, 18, 12, 18, 18, 18, 18, 18, 18, 18], [18, 18, 18, 18, 18, 18, 18, 12, 18, 18, 18, 18, 18, 18, 18],
        [18, 18, 18, 18, 18, 18, 18, 12, 18, 18, 15, 13, 13, 16, 18], [18, 12, 18, 18, 15, 13, 13, 17, 18, 18, 12, 18, 18, 12, 18], 
        [18, 12, 18, 18, 12, 18, 18, 18, 18, 18, 12, 18, 18, 12, 18], [18, 26, 13, 13, 29, 13, 13, 13, 13, 13, 17, 18, 18, 12, 18], 
        [18, 12, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 12, 18], [18, 12, 18, 18, 18, 18, 15, 13, 13, 13, 13, 13, 13, 17, 18], 
        [18, 12, 18, 18, 18, 18, 12, 18, 18, 18, 18, 18, 18, 18, 18], [18, 14, 13, 13, 13, 18, 12, 18, 18, 18, 18, 18, 18, 18, 18], 
        [18, 18, 18, 18, 19, 19, 20, 18, 18, 18, 18, 18, 18, 18, 18], [18, 18, 18, 18, 19, 19, 20, 18, 18, 18, 18, 18, 18, 18, 18], 
        [18, 18, 18, 15, 21, 21, 33, 21, 13, 13, 13, 13, 13, 16, 18], [18, 18, 18, 12, 19, 19, 19, 19, 18, 18, 18, 18, 18, 12, 18], 
        [15, 13, 13, 29, 13, 13, 13, 28, 13, 13, 16, 18, 18, 12, 18], [12, 18, 18, 18, 18, 18, 18, 12, 18, 18, 12, 18, 18, 12, 18], 
        [12, 18, 18, 18, 18, 18, 18, 12, 18, 18, 12, 18, 18, 12, 18], [12, 18, 18, 18, 18, 18, 18, 12, 18, 18, 12, 18, 18, 12, 18], 
        [12, 18, 18, 18, 18, 18, 18, 12, 18, 18, 14, 13, 13, 27, 18], [12, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 12, 18], 
        [12, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 12, 18], [12, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 12, 18], 
        [12, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 12, 18], [12, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 12, 18], 
        [14, 13, 21, 21, 32, 21, 21, 23, 18, 18, 18, 18, 18, 18, 18], [18, 18, 19, 19, 20, 19, 19, 24, 21, 21, 21, 23, 18, 18, 18], 
        [18, 18, 19, 19, 20, 19, 19, 19, 19, 19, 19, 20, 18, 18, 18], [18, 18, 19, 19, 30, 21, 21, 21, 21, 19, 19, 20, 18, 18, 18], 
        [18, 18, 19, 19, 20, 19, 19, 19, 19, 19, 19, 20, 18, 18, 18], [18, 18, 19, 19, 20, 19, 19, 19, 19, 19, 19, 20, 18, 18, 18], 
        [18, 18, 19, 19, 20, 19, 19, 19, 19, 19, 19, 20, 18, 18, 18], [18, 18, 18, 18, 18, 18, 18, 15, 21, 21, 21, 25, 18, 18, 18], 
        [18, 18, 18, 18, 18, 18, 18, 12, 18, 18, 18, 18, 18, 18, 18], [18, 18, 18, 18, 18, 18, 18, 12, 18, 18, 18, 18, 18, 18, 18], 
        [18, 18, 18, 18, 18, 18, 18, 12, 18, 18, 18, 18, 18, 18, 18]],
                
        [[18, 18, 18, 18, 18, 18, 18, 12, 18, 18, 18, 18, 18, 18, 18], [18, 18, 18, 18, 18, 18, 18, 12, 18, 18, 18, 18, 18, 18, 18], 
        [18, 15, 13, 13, 16, 18, 18, 14, 13, 13, 16, 18, 18, 12, 18], [18, 12, 18, 18, 12, 18, 18, 18, 18, 18, 12, 18, 18, 12, 18], 
        [18, 12, 18, 18, 12, 18, 18, 18, 18, 18, 12, 18, 18, 12, 18], [18, 26, 13, 13, 29, 13, 13, 13, 28, 13, 17, 18, 18, 12, 18], 
        [18, 12, 18, 18, 18, 18, 18, 18, 12, 18, 18, 18, 18, 12, 18], [18, 12, 18, 18, 18, 18, 15, 13, 29, 13, 13, 13, 13, 17, 18], 
        [18, 12, 18, 18, 18, 18, 12, 18, 18, 18, 18, 18, 18, 18, 18], [18, 14, 13, 13, 13, 18, 12, 18, 18, 18, 18, 18, 18, 18, 18], 
        [18, 18, 18, 18, 19, 19, 14, 13, 13, 13, 13, 13, 16, 18, 18], [18, 19, 19, 19, 19, 19, 19, 19, 18, 18, 18, 18, 12, 18, 18], 
        [12, 19, 19, 19, 19, 19, 19, 19, 15, 13, 13, 13, 17, 18, 18], [12, 19, 19, 19, 19, 19, 19, 19, 12, 18, 18, 18, 18, 12, 18], 
        [12, 19, 19, 19, 19, 19, 19, 19, 14, 13, 16, 18, 18, 12, 18], [12, 19, 19, 19, 19, 19, 19, 19, 18, 18, 12, 18, 18, 12, 18], 
        [12, 18, 18, 18, 19, 19, 18, 18, 18, 18, 12, 18, 18, 12, 18], [12, 18, 12, 18, 12, 18, 12, 18, 12, 18, 12, 18, 18, 12, 18], 
        [26, 13, 29, 28, 29, 28, 29, 28, 29, 28, 29, 13, 13, 27, 18], [12, 18, 18, 12, 18, 12, 18, 12, 18, 12, 18, 18, 18, 12, 18], 
        [12, 18, 18, 12, 18, 12, 18, 12, 18, 12, 18, 18, 18, 12, 18], [12, 18, 18, 12, 18, 12, 18, 12, 18, 12, 18, 18, 18, 12, 18], 
        [12, 18, 18, 12, 18, 12, 18, 12, 18, 12, 18, 18, 18, 12, 18], [12, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 12, 18], 
        [26, 13, 13, 13, 13, 13, 13, 16, 18, 18, 18, 18, 18, 18, 18], [12, 18, 18, 19, 19, 19, 19, 20, 19, 21, 21, 23, 18, 18, 18], 
        [12, 18, 18, 19, 19, 19, 19, 20, 19, 19, 19, 20, 18, 18, 18], [12, 18, 18, 19, 19, 19, 19, 20, 19, 19, 19, 20, 18, 18, 18], 
        [12, 18, 18, 19, 19, 19, 19, 20, 19, 19, 19, 20, 18, 18, 18], [14, 13, 13, 21, 21, 21, 21, 33, 21, 23, 19, 20, 18, 18, 18], 
        [18, 18, 18, 19, 19, 19, 19, 19, 19, 20, 19, 20, 18, 18, 18], [18, 18, 18, 19, 19, 19, 19, 19, 19, 20, 19, 20, 18, 18, 18], 
        [18, 18, 18, 19, 19, 19, 19, 19, 19, 20, 19, 20, 18, 18, 18], [18, 18, 18, 19, 21, 21, 21, 21, 21, 33, 21, 25, 18, 18, 18], 
        [18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18]]
]


##Programme principal##
fen = Tk()
can = Canvas(fen, height=1000, width=5000)

##Déclaration des images des décors##

d01 = PhotoImage(file='Décors/01 (herbe).gif')
d02 = PhotoImage(file='Décors/02 (chemin horizontal).gif')
d03 = PhotoImage(file='Décors/03 (chemin vertical).gif')
d04 = PhotoImage(file='Décors/04 (gauche-bas).gif')
d05 = PhotoImage(file='Décors/05 (droite-bas).gif')
d06 = PhotoImage(file='Décors/06 (droite-haut).gif')
d07 = PhotoImage(file='Décors/07 (gauche-haut).gif')
d08 = PhotoImage(file='Décors/08 (arbre).gif')
d09 = PhotoImage(file='Décors/09 (eau).gif')
d10 = PhotoImage(file='Décors/10 (sable).gif')
d11 = PhotoImage(file='Décors/11 (sol rocheux).gif')
d18 = PhotoImage(file='Décors/18 (rocher).gif')
d19 = PhotoImage(file='Décors/19 (eau sombre).gif')
d14 = PhotoImage(file='Décors/14 (gauche-bas).gif')
d15 = PhotoImage(file='Décors/15 (droite-bas).gif')
d16 = PhotoImage(file='Décors/16 (droite-haut).gif')
d17 = PhotoImage(file='Décors/17 (gauche-haut).gif')
d12 = PhotoImage(file='Décors/12 (chemin horizontal).gif')
d13 = PhotoImage(file='Décors/13 (chemin vertical).gif')
d20 = PhotoImage(file='Décors/20 (chemin horizontal eau).gif')
d21 = PhotoImage(file='Décors/21 (chemin vertical eau).gif')
d22 = PhotoImage(file='Décors/22 (droite-bas eau).gif')
d23 = PhotoImage(file='Décors/23 (droite-haut eau).gif')
d24 = PhotoImage(file='Décors/24 (gauche-bas eau).gif')
d25 = PhotoImage(file='Décors/25 (gauche-haut eau).gif')
d26 = PhotoImage(file='Décors/26 (gauche-bas-droite).gif')
d27 = PhotoImage(file='Décors/27 (gauche-haut-droite).gif')
d28 = PhotoImage(file='Décors/28 (haut-bas-droite).gif')
d29 = PhotoImage(file='Décors/29 (haut-bas-gauche).gif')
d30 = PhotoImage(file='Décors/30 (gauche-droite-bas eau).gif')
d31 = PhotoImage(file='Décors/31 (gauche-droite-haut eau).gif')
d32 = PhotoImage(file='Décors/32 (haut-bas-droite eau).gif')
d33 = PhotoImage(file='Décors/33 (haut-bas-gauche eau).gif')
d34=PhotoImage(file='34 - Entrée.gif')

##Déclaration des objets##

p01=PhotoImage(file='Personnages/Magicien.gif')
p02=PhotoImage(file='Personnages/Garde.gif')
p03=PhotoImage(file='Personnages/Villageois.gif')

o01=PhotoImage(file='Objets/Fiole Bleu.gif')
o02=PhotoImage(file='Objets/Fiole Jaune.gif')
o03=PhotoImage(file='Objets/Fiole Verte.gif')
o04=PhotoImage(file='Objets/Epée angélique.gif')
o05=PhotoImage(file='Objets/Epée diabolique.gif')
o06=PhotoImage(file='Objets/Trinité cyan.gif')
o07=PhotoImage(file='Objets/Trinité violet.gif')
o08=PhotoImage(file='Objets/Trinité jaune.gif')
o09=PhotoImage(file='Objets/Casque.gif')
o10=PhotoImage(file='Objets/Bouclier.gif')
o11=PhotoImage(file='Objets/Note.gif')

d = [d01, d02, d03, d04, d05, d06, d07, d08, d09, d10, d11, d12, d13, d14, d15, d16, d17, d18,
     d19, d20, d21, d22, d23, d24, d25, d26, d27, d28, d29, d30, d31, d32, d33, d34,p01,p02,p03]

fichier_imgg = PhotoImage(file='Personnages/Simon 1.gif')
fichier_imgd = PhotoImage(file='Personnages/Simon 2.gif')

cptmap=-1

can.pack()

fen.bind("<Left>", gauche)
fen.bind("<Right>", droite)
fen.bind("<Up>", haut)
fen.bind("<Down>", bas)
fen.bind_all("<a>",transition)

fen.mainloop()
