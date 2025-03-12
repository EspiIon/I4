#!/usr/bin/env python3
"""Module permettant de manipuler un plateau de Puissance 4"""

VIDE = 0
JAUNE = 1
ROUGE = 2

LARGEUR_PLATEAU = 7
HAUTEUR_PLATEAU = 6


def plateau_vide() -> "Plateau":
    """Fonction qui permet d'obtenir un plateau vide de LARGEUR_PLATEAU colonnes (1..LARGEUR_PLATEAU) chaque colonne étant de hauteur HAUTEUR_PLATEAU"""
    tableau = []
    for _ in range(HAUTEUR_PLATEAU):
        tableau.append([VIDE]*LARGEUR_PLATEAU)
    return tableau

def jouer(plateau: "Plateau", colonne: int, pion: "JAUNE|ROUGE") -> None:
    """Fonction qui permet de jouer un pion dans un colonne pas encore remplie (hauteur_colonne(colonne) <= HAUTEUR_PLATEAU)"""
    for i in range(HAUTEUR_PLATEAU-1):
        if plateau[i][colonne-1] == VIDE :
            plateau[i][colonne-1]=pion
            return
def contenu_case(plateau: "Plateau", colonne: int, ligne:int) -> "Contenu":
    """Fonction qui permet d'obtenir le contenu d'une case du plateau: ROUGE, JAUNE ou VIDE à partir de la colonne (1..LARGEUR_PLATEAU) et de la ligne (1..HAUTEUR_PLATEAU)"""
    return plateau[ligne-1][colonne-1]

def hauteur_colonne(plateau: "Plateau", colonne: int) -> int:
    """Fonction qui permet d'obtenir la hauteur d'une colonne (1..LARGEUR_PLATEAU)"""
    n=0
    for i in range(HAUTEUR_PLATEAU-1):
        if plateau[i][colonne-1]:
            n+=1
    return n

def colonne_remplie(plateau: "Plateau", colonne: int) -> bool:
    """Fonction qui permet de savoir si une colonne (1..LARGEUR_PLATEAU) est remplie"""
    if hauteur_colonne(plateau,colonne) == HAUTEUR_PLATEAU-1:
        return True
    return False

def plateau_rempli(plateau: "Plateau") -> bool:
    """Fonction qui permet de savoir si le plateau est rempli"""
    for i in range(HAUTEUR_PLATEAU):
        if not hauteur_colonne(plateau,i):
            return False
    return True
def _Alignement(plateau,colonne,ligne, pas_x,pas_y):
    x,y=ligne-1,colonne-1
    n=0
    inrange=True
    typePion = plateau[x][y]
    if (x<0 or x>HAUTEUR_PLATEAU-1) or (y<0 or y>LARGEUR_PLATEAU-1):
        inrange=False
    while plateau[x][y]==typePion and inrange:
        x+=pas_x
        y+=pas_y
        n+=1
        if x<0 or x>=HAUTEUR_PLATEAU or y<0 or y>=LARGEUR_PLATEAU:
            inrange=False
    return n

def nb_pions_alignes_horizontalement(plateau: "Plateau", colonne: int, ligne: int) -> int:
    """Fonction qui permet de savoir combien de pions d'une même couleur sont alignés 
    horizontalement à partir d'une position donnée. Retourne 0 si à 
    cette position la case est vide"""
    n=_Alignement(plateau,colonne,ligne,0,1)
    n+=_Alignement(plateau,colonne,ligne,0,-1)-1
    return n

    
def nb_pions_alignes_verticalement(plateau: "Plateau", colonne: int, ligne: int) -> int:
    """Fonction qui permet de savoir combien de pions d'une même couleur sont alignés 
    verticalement à partir d'une position donnée. Retourne 0 si à 
    cette position la case est vide"""
    n=_Alignement(plateau,colonne,ligne,1,0)
    n+=_Alignement(plateau,colonne,ligne,-1,0)-1
    return n

def nb_pions_alignes_diagonalement_SONE(plateau: "Plateau", colonne: int, ligne: int) -> int:
    """Fonction qui permet de savoir combien de pions d'une même couleur sont alignés 
    diagonalement (du Sud-Ouest au Nord-Est) à partir d'une position donnée. 
    Retourne 0 si à cette position la case est vide"""
    n=_Alignement(plateau,colonne,ligne,-1,-1)
    n+=_Alignement(plateau,colonne,ligne,1,1)-1
    return n

def nb_pions_alignes_diagonalement_NOSE(plateau: "Plateau", colonne: int, ligne: int) -> int:
    """Fonction qui permet de savoir combien de pions d'une même couleur sont alignés 
    diagonalement (du Nord-Ouest au Sud-Est) à partir d'une position donnée. 
    Retourne 0 si à cette position la case est vide"""
    n=_Alignement(plateau,colonne,ligne,1,-1)
    n+=_Alignement(plateau,colonne,ligne,-1,1)-1
    return n 