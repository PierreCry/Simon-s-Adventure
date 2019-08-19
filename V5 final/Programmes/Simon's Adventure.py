from tkinter import *
import time
from mes_matrices import*
from mes_textes import*
import pygame

#Ecrit par Superdry(Matthias Ambroise et Pierre Cry) avec Notepad++ et IDLE#


#Partie Audio
pygame.mixer.init()

#Musique de fond
Music = pygame.mixer.music.load("Musiques/Pillars of Eternity- Dyrford Village Music.ogg")
pygame.mixer.music.play()

#Bruitage
ramasse = pygame.mixer.Sound("Bruitages/ramasser.ogg")
épée= pygame.mixer.Sound("Bruitages/épée.ogg")
transit = pygame.mixer.Sound("Bruitages/transition.ogg")
perso=pygame.mixer.Sound("Bruitages/perso.ogg")
boss=pygame.mixer.Sound("Bruitages/boss.ogg")




##Fonctions de mouvement##
def mouvement(a,b):
    global x, y, img, M, cptM, cptV, cptG
    x, y = x + a, y + b
    if collision(x,y)==True: #Si l'endroit n'est pas un mur, faire le mouvement
        can.coords(img, x, y)
        text("")
        cptM, cptV, cptG, cptchoix=0,0,0,0
    else: #Revenir à la place initiale
        x,y=x-a,y-b

def gauche(event):
    global img, x, y
    if x > 82:
        mouvement(-32, 0)
        can.itemconfigure(img, image=fichier_imgg)

def droite(event):
    global img, x, y
    if x < 1138:
        mouvement(32, 0)
        can.itemconfigure(img, image=fichier_imgd)

def haut(event):
    global img, x, y
    if y > 100:
        mouvement(0, -32)

def bas(event):
    global img, x, y
    if y < 529:
        mouvement(0,32)

##Fonction de collision##
def collision(x,y):
    global M, cptmap
    MUR =[8,9,18,19]
    i,j=indices(x,y)
    if M[cptmap][i][j] not in MUR: #Si l'endroit où souhaite aller le joueur n'est pas un mur
        return True



##Création des décors##
def decor(M):
    global d
    for i in range(len(M)): #Parcourt la liste M
        for j in range(len(M[0])): #Parcourt une matrice de la liste M
            can.create_image(50 + 32 * i, 100 + 32 * j, image=d[M[i][j] - 1])


##Fonction qui gère les transitions## 
def transition(event):
    global x, y, cptmap
    X1=[242,114,1042]
    Y1=[420,164,164]
    X2=[210,146,1010]
    Y2=[420,164,164] 
     
    if cptmap == -1: #Menu principal
        carte(1010,452,0)
        can.create_text(1400,350,text="Commandes \nDéplacement : "+
		"Touches Directionnelles \nRamassage : z \nChanger de zone : "+
		"a \nInteragir avec un personnage : p \nDéfier la bête : space", fill="white", font=10)
        transit.play()
    for k in range (1,4): #Transition entre les différentes maps
        if cptmap==0 and (x == X1[k-1] and y == Y1[k-1]): #Transition de la map0 aux différentes maps
            carte(86,324,k)
            transit.play()
        if cptmap==k and (x == 54 and y == 324): #Transition des différentes maps à la map0
            carte(X2[k-1],Y2[k-1],0)
            transit.play()
     
def mapfinjeu(event):	#Fonction qui active la fin du jeu
    global img, x, y, cptmap, M
    Music = pygame.mixer.music.load("Musiques/First Contact Protocol (musique de boss).ogg")
    pygame.mixer.music.play()
    can.delete(img)
    carte(82,132,4)
    text("Magicien : Vas-y Simon, tu y es presque! Appuie sur q pour vaincre la bête")

def carte(g,j,v):	#Permet de charger une map ainsi que son personnage
    global M, L, img, x, y, cptmap
    can.delete(ALL)
    affichage(L)
    cptmap=v
    decor(M[cptmap])
    x=g
    y=j
    img=can.create_image(x,y,image=fichier_imgd)
    

def fin(event):	#Fonction qui affiche les textes à la fin du jeu en fonction des choix
    global M, puissance
    i,j=indices(x,y)
    if M[4][i][j]==56: #Si le joueur se trouve à l'endroit où la bête se situe
        can.delete(ALL)
        if puissance<100: #Mauvaise fin, dépendant de la puissance
            boss.play()
            can.create_text(500,350,text= "Malgré sa détermination, Simon n'était pas prêt "+
			"pour ce combat et maintenant qu'il est mort, plus rien "+
			"ne peut arrêter le dévoreur de monde",fill="white", font=15)
            bouton("Fermer","Recommencer",fermer,recommencer)
            
            
        if 100<puissance<150 : #Fin intermédiaire, dépendant de la puissance
            boss.play()
            can.create_text(700,350, text= "Aucun des deux partis ne prit le dessus sur l'autre alors "+
			"dans un élan de courage, Simon emporta la bête avec lui dans l'au-dela. "+
			"On se souviendra de lui comme d'un héros mort au combat",fill="white", font=15)
            bouton("Fermer","Recommencer",fermer,recommencer)
            
        if puissance>150: #Bonne fin, dépendant de la puissance
            boss.play()
            can.create_text(500,350, text=" La bataille fut rude mais avec la force "+
			"et la détermination des plus grands héros, Simon vainquit "+
			"le Néant et devint le plus grand guerrier du royaume",fill="white", font=15)
            bouton("Fermer","Recommencer",fermer,recommencer)

   
#Dialogue#
def Dialogue(event): #Active les dialogues en pressant la touche définit
    DialogueMag()
    DialogueGard()
    DialogueVill()

def DialogueMag(): #Dialogue avec le magicien
    global M, cptM, fait
    i,j=indices(x,y)
    if M[0][i][j]==48:#Le joueur parle sur la map0 au magicien
        if cptM==0: #Active le son perso
            perso.play()
        if cptM < 2: #Dialogue avant le choix
            text(DiagMag1[cptM])
        if cptM == 2: #Active le choix
            text(DiagMag1[cptM])
            bouton("Oui", "Non",Choix1Mag,Choix2Mag)
        if fait == 1 : #Le joueur a fait le choix
            text(DiagMag1[len(DiagMag1)-1])
            changementdec(10)
            fait=0
    #Le joueur parle pour la deuxième fois au Magicien sur la Map1 après avoir ramassé tous les objets demandé    
    if M[1][i][j]==51 and cptM < len(DiagMag3) and élixir()==True: 
        if cptM==0: #Active le son perso
            perso.play()
        text(DiagMag3[cptM])
        #Lorsque la liste des dialogues est parcourut, le joueur s'apprête à faire les choix moraux
        if cptM == len(DiagMag3)-1: 
            ChoixMor1()   
    else:
        #Le joueur parle pour la première fois au Magicien sur la Map1
        if M[1][i][j]==51 and cptM < len(DiagMag2): 
            if cptM==0:
                perso.play()
            text(DiagMag2[cptM])
    
    cptM=cptM+1 #Après que les conditions dépendant de cptM sont executés, le compteur prend +1

def DialogueGard(): #Dialogue avec le garde
    global M, x, y, cptG,couteau
    i,j=indices(x,y)
    if M[0][i][j]==49 and cptG < len(DiagGard2) and trinité()==True: #Le joueur parle pour la deuxième fois au Garde après avoir ramassé tous les objets demandé
        text(DiagGard2[cptG])
        if cptG==0:
            perso.play()
        if cptG == len(DiagGard2)-1: #Lorsque la liste des dialogues est parcourut, le garde s'en va en laissant un objet à Simon
            inventaire(60)
            changementdec(1)
        
    else:
        if M[0][i][j]==49 and trinité()==False: #Le joueur parle pour la première fois au Garde
            if cptG==0:
                perso.play()
            if fait==0: #Le joueur n'a pas encore fait le choix
                text(DiagGard1[cptG]) 
                if cptG == len(DiagGard1)-1: #Active le choix
                    bouton("L'aider","Le tuer", Choix1Gard, Choix2Gard)
                
            if fait!=0: #Le joueur a fait le choix
                if fait==1: #Si le joueur a fait le premier choix
                    text(Ch1Gard[cptG])
                else: #Si le joueur a fait le second choix
                    text(Ch2Gard[cptG])
                    if cptG == len(Ch2Gard)-1:#Lorsque la liste des dialogues est parcourut, le garde meurt en laissant un objet à Simon
                        épée.play()
                        inventaire(58)
                        changementdec(1)
    
    cptG=cptG+1 #Après que les conditions dépendant de cptG sont executés, le compteur prend +1
    
def DialogueVill(): #Dialogue avec le Villageois
    global M, x, y, cptV, cptenig
    i,j=indices(x,y)
    if M[0][i][j]==50 and cptV < len(DiagVill2) and clénote()==True: #Le joueur parle pour la deuxième fois au Villageois après avoir ramassé tous les objets demandé
        text(DiagVill2[cptV])
        if cptV==0:
            perso.play()
        if cptV == len(DiagVill2)-1 and cptenig < len(EnigVillQ): #Lorsque la liste des dialogues est parcourut, le joueur commence les énigmes
            Enigme()
        
    else:
        if M[0][i][j]==50 and cptV < len(DiagVill1) and clénote()==False: #Le joueur parle pour la première fois au Villageois
            text(DiagVill1[cptV])
            if cptV==0:
                perso.play()
    cptV=cptV+1 #Après que les conditions dépendant de cptV sont executés, le compteur prend +1


#Choix#

#Fonctions qui gère les choix du Magicien
    
def Choix1Mag(): #Le joueur a effectué la première réponse au choix du Magicien
    global cptchoix, fait
    text(Ch1Mag[cptchoix])
    inventaire(57)
    bouton("","",NONE,NONE)
    fait = 1

def Choix2Mag(): #Le joueur a effectué la deuxième réponse au choix du Magicien
    global cptchoix, fait
    text(Ch2Mag[cptchoix])
    bouton("","",NONE,NONE)
    fait = 1

#Fonctions qui gère les choix du Garde
    
def Choix1Gard(): #Le joueur a effectué la première réponse au choix du Garde
    global fait, cptG
    fait=1
    cptG=0
    bouton("","",NONE,NONE)

def Choix2Gard(): #Le joueur a effectué la deuxième réponse au choix du Garde
    global fait, cptG
    fait=-1
    cptG=0
    bouton("","",NONE,NONE)       


#Fonctions qui gère les choix moraux
def ChoixMor1(): 
    global cptchoix
    for k in range(3):
        if cptchoix==k: #Le joueur effectue le k-ème Choix Moraux
            text(ChMorauxQ[k])
            bouton(ChMorauxRC[k],ChMorauxRP[k],Concilliant,Pragmatique)
    if cptchoix==3: #Le joueur a effectué tous les choix moraux
        MorauxFin()
        changementdec(11)

def Concilliant(): #Concilliant amène à ajouter 1 au moral
    global moral,cptchoix
    moral=moral+1
    cptchoix=cptchoix+1
    ChoixMor1()

def Pragmatique(): #Pragmatique amène à enlever 1 au moral
    global moral,cptchoix
    moral=moral-1
    cptchoix=cptchoix+1
    ChoixMor1()

def MorauxFin(): #Annonce le côté Pragmatique ou Concilliant du joueur
    global moral
    if moral>0: #Joueur Conciliant
        text(ChMorauxFin[0])
        inventaire(38)
        changementdec(11)
        bouton("","",NONE,NONE)
    else: #Joueur Pragmatique
        text(ChMorauxFin[1])
        inventaire(39)
        changementdec(11)
        bouton("","",NONE,NONE)


#Enigme#
def Enigme():	#Fonction qui assure le déroulement des énigmes
    global cptenig
    ButtonEnig.config(text="Valider", command=verif)
    if cptenig<len(EnigVillQ):
        text(EnigVillQ[cptenig])
        
def verif():	#Fonction qui permet de vérifier les réponse aux énigmes
    global cptenig,faux
    for i in range(3):
        if cptenig==i: #Le joueurs effectue la i-ème énigme 
            if EntryEnig.get()==EnigVillR[i]:
                cptenig=cptenig+1
                EntryEnig.delete(0,END)
                Enigme()       
            else:
                faux=faux+1 #Compteur du nombre d'erreur
                if faux == 5: #Nombre d'erreur limité
                    text(EnigVillF[1])
                    changementdec(1)
                    EntryEnig.config(state = DISABLED)
                    ButtonEnig.config(text="", command=NONE)
        if cptenig==3: #Compteur exprimant le sans faute du joueur
            text(EnigVillF[0])
            inventaire(59)
            changementdec(1)
            EntryEnig.config(state = DISABLED)
            ButtonEnig.config(text="", command=NONE)
            

#Fonction pour configurer les labels et les boutons#
def bouton(text1, text2, command1, command2):
    ButtonCh1.config(text=text1, command=command1)
    ButtonCh1.pack(side=LEFT)
    ButtonCh2.config(text=text2, command=command2)
    ButtonCh2.pack(side=RIGHT)

def text(text):
    LabelDiag.config(text = text)
    LabelDiag.pack()


#Puissance#     
def power():	#Fonction qui permet de mettre à jour la puissance du joueur
    global puissance,T
    pt50 = [38,39,59,60]
    pt10 = [45,46,47]
    pt5  = [35,36,57,58]
    for k in range(len(T)): #On parcourt la liste des objets          
        if T[k] in pt50:
            puissance = puissance + 50
        if T[k] in pt10:
            puissance = puissance + 10
        if T[k] in pt5:
            puissance = puissance + 5

##Ramassage#
def ramasser(event): 	#Fonction qui permet de ramasser un objet
    global cptmap,M,x,y,son
    objet=[35,36,37,38,39,40,41,42,43,44,45,46,47,52,53,54,55]
    i,j=indices(x,y)
    if M[cptmap][i][j] in objet:
        power()
        inventaire(M[cptmap][i][j])
        changementdec(11)
        ramasse.play()
        
        
def inventaire(x):	#Fonction qui permet de mettre a jour l'inventaire
    global L,T
    T.append(x)
    L.append(d[x-1])
    affichage(L)
    
def affichage(L):	#Fonction qui permet l'affichage des objets dans l'inventaire
    for k in range(len(L)):
        can.create_image((120+50*k),30,image=L[k])

#Fonctions qui permet de vérifier la présence d'objets
        
def trinité():	#Les cristaux de la trinité	
    global T
    if 45 in T and 46 in T and 47 in T:
        return True
    return False

def élixir():	#Les élixirs
    global T
    if 40 in T and 41 in T and 42 in T and 43 in T:
        return True
    return False

def clénote():	#Les clés et les notes
    global T
    if 37 in T and 44 in T and 52 in T and 53 in T and 54 in T:
        return True
    return False

#Fonction qui parmet d'appeler les indices i et j
def indices(x,y): 
    i=(x-50)//32
    j=(y-100)//32
    return i,j

#Fonction permettant de remplacer une image par une autre dans la matrice
def changementdec(f): 
    global cptmap,img,x,y
    i,j=indices(x,y)
    M[cptmap][i][j]=f
    decor(M[cptmap])
    img=can.create_image(x,y,image=fichier_imgd)

def fermer(): #Fonction permettant de fermer la fenêtre à la fin du jeu
    pygame.mixer.music.stop()
    fen.destroy()
 
def recommencer(): #Fonction permettant de recommencer le jeu
    global cptmap, puissance, L,T,cptM,cptG,cptV,cptchoix,cptenig,moral,fait,faux,d,N,M
    can.delete(ALL)
    text("Tu veux recommencer ? Très bien, appuies sur le bouton a")
    cptmap = -1
    puissance=0
    L=[]
    T=[]
    cptM=0
    cptG=0
    cptV=0
    cptchoix=0
    cptenig=0
    moral=0
    fait=0
    faux=0
    M=N
    sic = pygame.mixer.music.load("Musiques/Pillars of Eternity- Dyrford Village Music.ogg")
    pygame.mixer.music.play()
    bouton("","",NONE,NONE)
    


##Programme principal##
fen = Tk()
fen.title("Simon\'s Adventure")

can = Canvas(fen, height=1000, width=1750,bg="black")

#Menu
label = Label(fen, text="Simon's Adventure by Superdry")
label.pack()

menu=PhotoImage(file='Décors/menu.gif')

can.create_text(500,50,text="«Dans les sombres contrées d’Alveyshik, où la lumière elle-même refuse de pénétrer, un nouveau mal va émerger. Né de la mort et du sang, \n"+
        "cette sombre entité n’est animée que par la colère, la haine et le feu qui le brûle de l’intérieur. "+
        "Personne dans la vallée ne se doute que leur fin est proche. Tous… Sauf un…» ",fill="white")
		
can.create_image(750, 300, image=menu)

can.create_text(500,550,text="L’objectif du jeu est de contrôler le héros Simon qui doit récupérer des éléments de son "+
		"armure ainsi que des armes afin de vaincre le mal.\nLe jeu est scindé en quatre niveaux. Un niveau global qui, en l’explorant, permet d’accéder aux trois "+
		"autres niveaux.\nLe joueur devra interagir avec des objets et d’autres personnages. Il aura également accès à des énigmes \nafin de récupérer "+
        "les différents éléments qui lui permettront de vaincre le mal. Chaque objets que le joueur acquiert augmente sa puissance. \nC’est en "+
        "fonction de la valeur de la puissance du joueur à la fin du jeu que les fins seront sélectionnées. \nQuand vous êtes prêt, appuyez sur a pour commencer l'aventure." ,fill="white")

#Interface de jeu

#Frame principale
Interface = Frame(fen, width=1650, height=220, pady=20)
Interface.pack(side=TOP)

#Frame qui contient les dialogues
FrameDiag = LabelFrame(Interface, text="Dialogue", bg="green", width=550, height=120)
FrameDiag.pack(side = LEFT)
FrameDiag.pack_propagate(False)

#Label qui affiche les dialogues
LabelDiag = Label(FrameDiag, text="", fg="white", bg="green")
LabelDiag.pack()

#Frame qui contient les choix
FrameCh = LabelFrame(Interface, text="Choix", bg="purple", width=550, height=120)
FrameCh.pack(side = LEFT)
FrameCh.pack_propagate(False)

#Bouttons utilisés dans le système de choix
ButtonCh1 = Radiobutton(FrameCh, text="", indicatoron=0, width=30, height=30, command=NONE)
ButtonCh1.pack(side=LEFT)
ButtonCh2 = Radiobutton(FrameCh, text="", indicatoron=0, width=30, height=30, command=NONE)
ButtonCh2.pack(side=RIGHT)

#Frame qui contient les enigmes
FrameEnig = LabelFrame(Interface, text="Enigme", bg="green", width=550, height=120)
FrameEnig.pack(side = LEFT)
FrameEnig.pack_propagate(False)

#Label, Bouton et Entry qui gère le système d'enigme
enig = StringVar()
LabelEnig = Label(FrameEnig, text="Entrez votre réponse à l'énigme \n Un mot, minuscule, 5 tentatives", bg="green", fg="white", font="5")
LabelEnig.pack(side=TOP)
ButtonEnig = Button(FrameEnig)
ButtonEnig.pack(side=BOTTOM)
EntryEnig = Entry(FrameEnig, textvariable=enig)
EntryEnig.pack(side=BOTTOM)

fichier_imgg = PhotoImage(file='Personnages/Simon 1.gif')
fichier_imgd = PhotoImage(file='Personnages/Simon 2.gif')

d = [PhotoImage(file='Décors/01 (herbe).gif'), PhotoImage(file='Décors/02 (chemin horizontal).gif'), PhotoImage(file='Décors/03 (chemin vertical).gif'),
     PhotoImage(file='Décors/04 (gauche-bas).gif'), PhotoImage(file='Décors/05 (droite-bas).gif'), PhotoImage(file='Décors/06 (droite-haut).gif'),
     PhotoImage(file='Décors/07 (gauche-haut).gif'), PhotoImage(file='Décors/08 (arbre).gif'), PhotoImage(file='Décors/09 (eau).gif'),
     PhotoImage(file='Décors/10 (sable).gif'), PhotoImage(file='Décors/11 (sol rocheux).gif'), PhotoImage(file='Décors/12 (chemin horizontal).gif'),
     PhotoImage(file='Décors/13 (chemin vertical).gif'), PhotoImage(file='Décors/14 (gauche-bas).gif'), PhotoImage(file='Décors/15 (droite-bas).gif'),
     PhotoImage(file='Décors/16 (droite-haut).gif'), PhotoImage(file='Décors/17 (gauche-haut).gif'), PhotoImage(file='Décors/18 (rocher).gif'),
     PhotoImage(file='Décors/19 (eau sombre).gif'), PhotoImage(file='Décors/20 (chemin horizontal eau).gif'), PhotoImage(file='Décors/21 (chemin vertical eau).gif'),
     PhotoImage(file='Décors/22 (droite-bas eau).gif'), PhotoImage(file='Décors/23 (droite-haut eau).gif'), PhotoImage(file='Décors/24 (gauche-bas eau).gif'),
     PhotoImage(file='Décors/25 (gauche-haut eau).gif'), PhotoImage(file='Décors/26 (gauche-bas-droite).gif'), PhotoImage(file='Décors/27 (gauche-haut-droite).gif'),
     PhotoImage(file='Décors/28 (haut-bas-droite).gif'), PhotoImage(file='Décors/29 (haut-bas-gauche).gif'), PhotoImage(file='Décors/30 (gauche-droite-bas eau).gif'),
     PhotoImage(file='Décors/31 (gauche-droite-haut eau).gif'), PhotoImage(file='Décors/32 (haut-bas-droite eau).gif'), PhotoImage(file='Décors/33 (haut-bas-gauche eau).gif'),
     PhotoImage(file='Décors/34 (entrée).gif'), PhotoImage(file='Décors/35 Bouclier.gif'), PhotoImage(file='Décors/36 Casque.gif'),
     PhotoImage(file='Décors/37 Clé.gif'), PhotoImage(file='Décors/38 Epée angélique.gif'), PhotoImage(file='Décors/39 Epée diabolique.gif'),
     PhotoImage(file='Décors/40 Fiole Bleu.gif'), PhotoImage(file='Décors/41 Fiole Jaune.gif'), PhotoImage(file='Décors/42 Fiole Verte.gif'),
     PhotoImage(file='Décors/43 Fiole Rouge.gif'), PhotoImage(file='Décors/44 Note.gif'), PhotoImage(file='Décors/45 Trinité cyan.gif'),
     PhotoImage(file='Décors/46 Trinité violet.gif'), PhotoImage(file='Décors/47 Trinité jaune.gif'), PhotoImage(file='Décors/48 Magicien.gif'),
     PhotoImage(file='Décors/49 Garde.gif'), PhotoImage(file='Décors/50 Villageois.gif'), PhotoImage(file='Décors/51 Magicien.gif'),
     PhotoImage(file='Décors/52 Note2.gif'), PhotoImage(file='Décors/53 Note3.gif'), PhotoImage(file='Décors/54 Clé2.gif'),
     PhotoImage(file='Décors/55 Clé3.gif'), PhotoImage(file='Décors/56 (Néant).gif'), PhotoImage(file='Décors/57 Bottes.gif'),
     PhotoImage(file='Décors/58 Gantelet.gif'), PhotoImage(file='Décors/59 Plastron.gif'), PhotoImage(file='Décors/60 Trident.gif')]

#Définition des variables
cptmap = -1
puissance=0
L=[]
T=[]
cptM=0
cptG=0
cptV=0
cptchoix=0
cptenig=0
moral=0
fait=0
faux=0

can.pack()


#Définition des contrôles
fen.bind("<Left>", gauche)
fen.bind("<Right>", droite)
fen.bind("<Up>", haut)
fen.bind("<Down>", bas)
fen.bind("<a>", transition)
fen.bind("<p>", Dialogue)
fen.bind("<z>", ramasser)
fen.bind("<space>", mapfinjeu)
fen.bind("<q>", fin)

fen.mainloop()
