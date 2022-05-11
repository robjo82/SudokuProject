#code un jeu de Sudoku
#Auteur: Nicolas FERRERI
#Date: 14/12/2019
#Version: 1.0

def main():
    """
    Fonction principale du jeu de Sudoku
    """
    #initialisation du jeu
    grille = initialisation()
    #affichage du jeu
    affichage(grille)
    #tant que le jeu n'est pas fini
    while not fin(grille):
        #demande de la ligne
        ligne = int(input("Entrez la ligne: "))
        #demande de la colonne
        colonne = int(input("Entrez la colonne: "))
        #demande de la valeur
        valeur = int(input("Entrez la valeur: "))
        #modification de la grille
        grille[ligne][colonne] = valeur
        #affichage du jeu
        affichage(grille)
    #affichage du message de fin
    print("Vous avez gagnez !")

def initialisation():
    """
    Fonction qui initialise le jeu
    """
    #initialisation de la grille
    grille = [[0 for i in range(9)] for j in range(9)]
    #remplissage de la grille
    grille[0][0] = 6
    grille[0][1] = 1
    grille[0][2] = 9
    grille[0][3] = 5
    grille[0][4] = 7
    grille[0][5] = 3
    grille[0][6] = 2
    grille[0][7] = 8
    grille[0][8] = 4
    grille[1][0] = 8
    grille[1][1] = 7
    grille[1][2] = 4
    grille[1][3] = 2
    grille[1][4] = 3
    grille[1][5] = 1
    grille[1][6] = 9
    grille[1][7] = 5
    grille[1][8] = 6
    grille[2][0] = 3
    grille[2][1] = 2
    grille[2][2] = 5
    grille[2][3] = 7
    grille[2][4] = 4
    grille[2][5] = 6
    grille[2][6] = 8
    grille[2][7] = 1
    grille[2][8] = 9
    grille[3][0] = 4
    grille[3][1] = 9
    grille[3][2] = 8
    grille[3][3] = 6
    grille[3][4] = 1
    grille[3][5] = 2
    grille[3][6] = 3
    grille[3][7] = 7
    grille[3][8] = 5
    grille[4][0] = 7
    grille[4][1] = 3
    grille[4][2] = 2
    grille[4][3] = 1
    grille[4][4] = 5
    grille[4][5] = 9
    grille[4][6] = 4
    grille[4][7] = 6
    grille[4][8] = 8
    grille[5][0] = 2
    grille[5][1] = 5
    grille[5][2] = 6
    grille[5][3] = 8
    grille[5][4] = 7
    grille[5][5] = 4
    grille[5][6] = 9
    grille[5][7] = 3
    grille[5][8] = 1
    grille[6][0] = 9
    grille[6][1] = 4
    grille[6][2] = 3
    grille[6][3] = 5
    grille[6][4] = 2
    grille[6][5] = 7
    grille[6][6] = 1
    grille[6][7] = 8
    grille[6][8] = 6
    grille[7][0] = 5
    grille[7][1] = 8
    grille[7][2] = 1
    grille[7][3] = 3
    grille[7][4] = 6
    grille[7][5] = 9
    grille[7][6] = 2
    grille[7][7] = 7
    grille[7][8] = 4
    grille[8][0] = 1
    grille[8][1] = 6
    grille[8][2] = 7
    grille[8][3] = 9
    grille[8][4] = 4
    grille[8][5] = 5
    grille[8][6] = 3
    grille[8][7] = 8
    grille[8][8] = 2
    #retourne la grille
    return grille

def affichage(grille):
    """
    Fonction qui affiche le jeu
    """
    #affichage de la grille
    for i in range(9):
        print(grille[i])

def fin(grille):
    """
    Fonction qui teste si le jeu est fini
    """
    #initialisation de la variable de fin
    fini = True
    #parcours de la grille
    for i in range(9):
        for j in range(9):
            #si une case est vide
            if grille[i][j] == 0:
                #le jeu n'est pas fini
                fini = False
    #retourne la variable de fin
    return fini

def verification(grille):
    """
    Fonction qui verifie la grille
    """
    #initialisation de la variable de verification
    verif = True
    #parcours de la grille
    for i in range(9):
        for j in range(9):
            #si une case est vide
            if grille[i][j] == 0:
                #le jeu n'est pas verifie
                verif = False
            #si une case est deja utilisee
            elif grille[i][j] in grille[i]:
                #le jeu n'est pas verifie
                verif = False
            #si une case est deja utilisee
            elif grille[i][j] in grille[j]:
                #le jeu n'est pas verifie
                verif = False
            #si une case est deja utilisee
            elif grille[i][j] in grille[i//3*3+j//3]:
                #le jeu n'est pas verifie
                verif = False
    #retourne la variable de verification
    return verif

def resolution(grille):
    """
    Fonction qui resoud le jeu
    """
    #initialisation de la variable de resolution
    resolu = False
    #parcours de la grille
    for i in range(9):
        for j in range(9):
            #si une case est vide
            if grille[i][j] == 0:
                #parcours des valeurs
                for k in range(1,10):
                    #si la valeur est possible
                    if k not in grille[i] and k not in grille[j] and k not in grille[i//3*3+j//3]:
                        #remplissage de la case
                        grille[i][j] = k
                        #verification de la grille
                        if verification(grille):
                            #si la grille est verifiee
                            resolu = True
                            #retourne la grille
                            return grille
                        #sinon
                        else:
                            #remise a zero de la case
                            grille[i][j] = 0
    #retourne la grille
    return grille

def resolution_rec(grille):
    """
    Fonction qui resoud le jeu par resolution recursive
    """
    #initialisation de la variable de resolution
    resolu = False
    #parcours de la grille
    for i in range(9):
        for j in range(9):
            #si une case est vide
            if grille[i][j] == 0:
                #parcours des valeurs
                for k in range(1,10):
                    #si la valeur est possible
                    if k not in grille[i] and k not in grille[j] and k not in grille[i//3*3+j//3]:
                        #remplissage de la case
                        grille[i][j] = k
                        #verification de la grille
                        if verification(grille):
                            #si la grille est verifiee
                            resolu = True
                            #retourne la grille
                            return grille
                        #sinon
                        else:
                            #remise a zero de la case
                            grille[i][j] = 0
    #retourne la grille
    return grille

def resolution_iter(grille):
    """
    Fonction qui resoud le jeu par resolution iterative
    """
    #initialisation de la variable de resolution
    resolu = False
    #parcours de la grille
    for i in range(9):
        for j in range(9):
            #si une case est vide
            if grille[i][j] == 0:
                #parcours des valeurs
                for k in range(1,10):
                    #si la valeur est possible
                    if k not in grille[i] and k not in grille[j] and k not in grille[i//3*3+j//3]:
                        #remplissage de la case
                        grille[i][j] = k
                        #verification de la grille
                        if verification(grille):
                            #si la grille est verifiee
                            resolu = True
                            #retourne la grille
                            return grille
                        #sinon
                        else:
                            #remise a zero de la case
                            grille[i][j] = 0
    #retourne la grille
    return grille

def resolution_iter_rec(grille):
    """
    Fonction qui resoud le jeu par resolution iterative recursive
    """
    #initialisation de la variable de resolution
    resolu = False
    #parcours de la grille
    for i in range(9):
        for j in range(9):
            #si une case est vide
            if grille[i][j] == 0:
                #parcours des valeurs
                for k in range(1,10):
                    #si la valeur est possible
                    if k not in grille[i] and k not in grille[j] and k not in grille[i//3*3+j//3]:
                        #remplissage de la case
                        grille[i][j] = k
                        #verification de la grille
                        if verification(grille):
                            #si la grille est verifiee
                            resolu = True
                            #retourne la grille
                            return grille
                        #sinon
                        else:
                            #remise a zero de la case
                            grille[i][j] = 0
    #retourne la grille
    return grille

main()