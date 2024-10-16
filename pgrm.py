
# BATAILLE NAVALE 

# by Aymerico l'asticot

import time

def creer_grille ():
    x , y = 10 , 10 
    grille = [['_' for _ in range(x)] for _ in range(y)]
    return grille


def placer_bateaux (grille,bato):
    o = int (input('entré 1 pour orienter le bateau horizontalement ou bien 2 pour jouer verticalement'))
    x = int (input('Dans quelle ligne voulez-vous poser votre bateau ?'))
    y = int (input('Dans quelle colonne voulez-vous poser votre bateau ?'))
    if x + len(bato) <= 9 and y - len(bato) >= 0:
        if o == 1 :
            for i in range (len(bato)):
                grille[x][y] = '#'
                x += 1
        elif o == 2 :
            for i in range (len(bato)):
                grille[x][y] = '#'
                y -= 1
    else :
        print ('le bateau sort de la grille, rejoué')
        return placer_bateaux(grille,bato)
    return grille

def verif_placer_bateau (x,y,o,grille,bato):
    if o == 1 :
        if x + len(bato) > 9 :
    for i in range (len(bato)):
        if o == 1 :
            if grille[x][y] == '#' :
                return False
            x += 1
        elif o == 2 :
            if grille[x][y] == '#':
                return False
            y -= 1
    





def attaque (x,y,grille1,grille2):
    x = int (input('Dans quelle ligne voulez-vous jouer ?'))
    y = int (input('Dans quelle colonne voulez-vous jouer ?'))
    if grille1[x][y] == 'O' :
        print ('vous avez deja joué sur cette case, rejoué' + attaque(grille1,grille2))
    elif grille2[x][y] == '#' :
        grille1[x][y] == 'X'
        return 'touché'
    elif grille2[x][y] != '#' :
        grille1[x][y] == 'O'
        return 'coulé'
    

def jeu():
    bato1 = ['#','#','#']
    bato2 = ['#','#','#','#']
    bato3 = ['#','#','#','#']
    bato4 = ['#','#','#','#','#']

    grille_J1 = creer_grille()
    grille_J2 = creer_grille()


    for a in grille_J1:
        print ("".join(a))
    placer_bateaux(grille_J1,bato1)

    for a in grille_J1:
        print ("".join(a))
    placer_bateaux(grille_J1,bato2)

    for a in grille_J1:
        print ("".join(a))
    placer_bateaux(grille_J1,bato3)

    for a in grille_J1:
        print ("".join(a))
    placer_bateaux(grille_J1,bato4)

    
    for i in range (time.sleep(10)):
        print (i-1)



print (jeu())
