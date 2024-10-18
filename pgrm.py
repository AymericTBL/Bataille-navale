"""

BATAILLE NAVALE 

by Aymerico l'asticot


"""
import time

def creer_grille ():
    """fonction qui permet de creer une grille de 10 par 10
    """
    x , y = 10 , 10 # 10 lignes et 10 colonnes
    grille = [['_' for _ in range(x)] for _ in range(y)] # une double boucle pour creer un tableau a double entre
    return grille


def afficher_grille(grille):
    """fonction qui permet d'aficher la grille d'un joueur avec les lettres et les chiffres
    """
    print("  " + " ".join(chr(i) for i in range(ord('A'), ord('A') + len(grille[0]))))  # coordonees des colonnes
    for i in range(len(grille)):
        ligne = grille[i]
        print(f"{i} " + " ".join(ligne))  # affiche les lignes avc les chiffres


def placer_bateaux (x,y,o,grille,bato):
    """fonction qui permet de placer les bateaux a travert la grille de jeu 
    """
    if o == 1 : # si le bateau est oriente horizontalement
        for i in range (bato): # le nbr de cases qu'occupe le bateau 
            grille[x+i][y] = '#' # place le bateau aux coordonees indique
    elif o == 2 : # si le bateau est oriente verticalement
        for i in range (bato): # le nbr de cases qu'occupe le bateau 
            grille[x][y+i] = '#' # place le bateau aux coordonees indique
    return 



def verif_placer_bateau (x,y,o,grille,bato):
    """ fonction qui verifie si le bateau peux etre pose a la posision indique
    """
    if o == 1:  # si le bateau est oriente horizontalement
        if y + bato > 10:  # verifie si le bateau sort de la grille
            return False
        for i in range(bato):
            if grille[x][y + i] == '#':  # verifie si un bateau est deja la
                return False
    elif o == 2:  # si le bateau est oriente verticalement
        if x + bato > 10:  # verifie si le bateau sort de la grille
            return False
        for i in range(bato):
            if grille[x + i][y] == '#':  # verifie si un bateau est deja la 
                return False
    return True  # si tout est valide

    

def attaque (x,y,grille1,grille2):
    """fonction qui permet d'attaque et qui complete la grille en fonction de ce qui etais present sur la grille avant
    """
    if grille1[x][y] == 'O' : # verifie si on a deja jouer sur cette position
        print ('vous avez deja joué sur cette case, rejoué' + attaque(grille1,grille2))
    elif grille2[x][y] == '#' : # verifie si la case selec est un bateau
        grille1[x][y] = 'X'
        return 'touché'
    elif grille2[x][y] == '_' : # verifie 
        grille1[x][y] = 'O'
        return 'coulé'


def bateau_coule(x,y,o,grille,taille):
    """fonction qui verifie si un bateau entier est coule"""
    if o == 1:  # horizontal
        for i in range(taille):
            if grille[x][y + i] != 'X':
                return False
    elif o == 2:  # vertical
        for i in range(taille):
            if grille[x + i][y] != 'X':
                return False
    return True  # le bateau est coule



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Programme principale

bateaux = {
    "PorteAvions" : 5 ,
    "Croiseur" : 4 ,
    "ContreTorpilleur" : 3 ,
    "SousMarin" : 3 ,
    "Torpilleur" : 2
    }

grille_J1 = creer_grille() # initialisation de la grille du joueur 1
grille_J2 = creer_grille() # initialisation de la grille du joueur 2

# me permet plus tard de savoir quant est ce que la game est terminé
nbr_de_bato_J1 = 5 
nbr_de_bato_J2 = 5

# pour savoir a qui est ce que c'est de jouer 
tour_de_jeu = 1

for nom, taille in bateaux.items():
    while True:
        afficher_grille(grille_J1)  # affiche la grille apres chaque placement
        o = int(input('entrez 1 pour orienter le bateau horizontalement ou 2 pour verticalement: '))  # orientation
        x = int(input('dans quelle ligne voulez-vous poser votre bateau ? (0-9): '))  # ligne
        y = int(input('dans quelle colonne voulez-vous poser votre bateau ? (0-9): '))  # colonne

        coordonnees_bateau_J1 = []
        coordonnees_bateau_J1.append(o,x,y)

        if verif_placer_bateau(x, y, o, grille_J1, taille):
            placer_bateaux(x, y, o, grille_J1, taille)
            break  # sort de la boucle si le bateau est place
        else:
            print('Position invalide, rejouez')

for nom, taille in bateaux.items():
    while True:
        afficher_grille(grille_J2)  # affiche la grille apres chaque placement
        o = int(input('entrez 1 pour orienter le bateau horizontalement ou 2 pour verticalement: '))  # orientation
        x = int(input('dans quelle ligne voulez-vous poser votre bateau ? (0-9): '))  # ligne
        y = int(input('dans quelle colonne voulez-vous poser votre bateau ? (0-9): '))  # colonne

        coordonnees_bateau_J2 = []
        coordonnees_bateau_J2.append(o,x,y)

        if verif_placer_bateau(x, y, o, grille_J2, taille):
            placer_bateaux(x, y, o, grille_J2, taille)
            break  # sort de la boucle si le bateau est place
        else:
            print('Position invalide, rejouez')

while nbr_de_bato_J1 != 0 or nbr_de_bato_J2 != 0 :
    if tour_de_jeu == 1 :
        x = int(input('dans quelle ligne voulez-vous attaquer ? (0-9): '))  # ligne
        y = int(input('dans quelle colonne voulez-vous attaquer ? (0-9): '))  # colonne
        attaque(x,y,grille_J1,grille_J2)
        for i in range (nbr_de_bato_J2):
            if bateau_coule (coordonnees_bateau_J2[0],coordonnees_bateau_J2[1],coordonnees_bateau_J2[2],grille_J1,5)  :
                nbr_de_bato_J2 -= 1
            if bateau_coule (coordonnees_bateau_J2[3],coordonnees_bateau_J2[4],coordonnees_bateau_J2[5],grille_J1,4)  :
                nbr_de_bato_J2 -= 1
            if bateau_coule (coordonnees_bateau_J2[6],coordonnees_bateau_J2[7],coordonnees_bateau_J2[8],grille_J1,3)  :
                nbr_de_bato_J2 -= 1
            if bateau_coule (coordonnees_bateau_J2[9],coordonnees_bateau_J2[10],coordonnees_bateau_J2[11],grille_J1,3)  :
                nbr_de_bato_J2 -= 1
            if bateau_coule (coordonnees_bateau_J2[12],coordonnees_bateau_J2[13],coordonnees_bateau_J2[15],grille_J1,2)  :
                nbr_de_bato_J2 -= 1
        tour_de_jeu += 1
        time.sleep(5)
    elif tour_de_jeu == 2 :
        x = int(input('dans quelle ligne voulez-vous attaquer ? (0-9): '))  # ligne
        y = int(input('dans quelle colonne voulez-vous ataquer ? (0-9): '))  # colonne
        attaque(x,y,grille_J2,grille_J1)
        for i in range (nbr_de_bato_J1):
            if bateau_coule (coordonnees_bateau_J1[0],coordonnees_bateau_J1[1],coordonnees_bateau_J1[2],grille_J2,4)  :
                nbr_de_bato_J1 -= 1
            if bateau_coule (coordonnees_bateau_J1[3],coordonnees_bateau_J1[4],coordonnees_bateau_J1[5],grille_J2,4)  :
                nbr_de_bato_J1 -= 1
            if bateau_coule (coordonnees_bateau_J1[6],coordonnees_bateau_J1[7],coordonnees_bateau_J1[8],grille_J2,3)  :
                nbr_de_bato_J1 -= 1
            if bateau_coule (coordonnees_bateau_J1[9],coordonnees_bateau_J1[10],coordonnees_bateau_J1[11],grille_J2,3)  :
                nbr_de_bato_J1 -= 1
            if bateau_coule (coordonnees_bateau_J1[12],coordonnees_bateau_J1[13],coordonnees_bateau_J1[15],grille_J2,2)  :
                nbr_de_bato_J1 -= 1
        tour_de_jeu -= 1
        time.sleep(5)

if nbr_de_bato_J2 == 0 :
    print ('J1 A GAGNE !!')
elif nbr_de_bato_J2 == 0 :
    print ('J2 A GAGNE !!')
            

    
