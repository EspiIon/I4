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
    for _ in range(HAUTEUR_PLATEAU-1):
        tableau.append([VIDE]*LARGEUR_PLATEAU)
    return tableau

def jouer(plateau: "Plateau", colonne: int, pion: "JAUNE|ROUGE") -> None:
    """Fonction qui permet de jouer un pion dans un colonne pas encore remplie (hauteur_colonne(colonne) <= HAUTEUR_PLATEAU)"""
    for i in range(HAUTEUR_PLATEAU-1):
        if plateau[i][colonne-1] == VIDE :
            plateau[i][colonne-1]=pion
            pass

def contenu_case(plateau: "Plateau", colonne: int, ligne:int) -> "Contenu":
    """Fonction qui permet d'obtenir le contenu d'une case du plateau: ROUGE, JAUNE ou VIDE à partir de la colonne (1..LARGEUR_PLATEAU) et de la ligne (1..HAUTEUR_PLATEAU)"""
    return plateau[colonne-1][ligne-1]

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
def _Alignement(plateau,ligne,colonne, pas_x,pas_y):
    x,y=ligne-1,colonne-1
    n=0
    typePion = plateau[ligne][colonne]
    for i in range(colone+pas_x*HAUTEUR_PLATEAU):
        for j in range(LARGEUR_PLATEAU):
            plateau[][]=typePion:
    return n

def nb_pions_alignes_horizontalement(plateau: "Plateau", colonne: int, ligne: int) -> int:
    """Fonction qui permet de savoir combien de pions d'une même couleur sont alignés 
    horizontalement à partir d'une position donnée. Retourne 0 si à 
    cette position la case est vide"""
    
    return -1

    
def nb_pions_alignes_verticalement(plateau: "Plateau", colonne: int, ligne: int) -> int:
    """Fonction qui permet de savoir combien de pions d'une même couleur sont alignés 
    verticalement à partir d'une position donnée. Retourne 0 si à 
    cette position la case est vide"""
    return -1

def nb_pions_alignes_diagonalement_SONE(plateau: "Plateau", colonne: int, ligne: int) -> int:
    """Fonction qui permet de savoir combien de pions d'une même couleur sont alignés 
    diagonalement (du Sud-Ouest au Nord-Est) à partir d'une position donnée. 
    Retourne 0 si à cette position la case est vide"""
    return -1 

def nb_pions_alignes_diagonalement_NOSE(plateau: "Plateau", colonne: int, ligne: int) -> int:
    """Fonction qui permet de savoir combien de pions d'une même couleur sont alignés 
    diagonalement (du Nord-Ouest au Sud-Est) à partir d'une position donnée. 
    Retourne 0 si à cette position la case est vide"""
    return -1

if __name__ == "__main__":
    p = [[ROUGE, JAUNE, JAUNE, JAUNE, ROUGE, ROUGE, VIDE],
         [VIDE, JAUNE, ROUGE, ROUGE, JAUNE, VIDE, VIDE],
         [VIDE, VIDE, ROUGE, JAUNE, ROUGE, VIDE, VIDE],
         [VIDE, VIDE, JAUNE, VIDE, JAUNE, VIDE, VIDE],
         [VIDE, VIDE, VIDE, VIDE, ROUGE, VIDE, VIDE],
         [VIDE, VIDE, VIDE, VIDE, JAUNE, VIDE, VIDE]]
    res = "OK" if contenu_case(p, 1,2) == VIDE else "KO"
    print(f"  contenu_case vide {res}")
    res = "OK" if contenu_case(p, 2,1) == JAUNE else "KO"
    print(f"  contenu_case JAUNE {res}")
    res = "OK" if contenu_case(p, 3,2) == ROUGE else "KO"
    print(f"  contenu_case ROUGE {res}")
    res = "OK" if hauteur_colonne(p, 7) == 0 else "KO"
    print(f"  hauteur_colonne vide {res}")
    res = "OK" if hauteur_colonne(p, 2) == 2 else "KO"
    print(f"  hauteur_colonne non vide {res}")
    res = "OK" if not colonne_remplie(p, 2) else "KO"
    print(f"  colonne_remplie non remplie {res}")
    res = "OK" if colonne_remplie(p, 5) else "KO"
    print(f"  colonne_remplie remplie {res}")
    res = "OK" if not plateau_rempli(p) else "KO"
    print(f"  plateau_rempli non rempli {res}")
    res = "OK" if plateau_rempli([[ROUGE]*LARGEUR_PLATEAU]*HAUTEUR_PLATEAU) else "KO"
    print(f"  plateau_rempli rempli {res}")    
    p = plateau_vide()
    test = [hauteur_colonne(p, colonne) for colonne in range(LARGEUR_PLATEAU)]
    res = "OK" if sum(test) == 0 else "KO"
    print(f"  plateau_vide {res}")
    jouer(p,2,JAUNE)
    jouer(p,2,ROUGE)
    jouer(p,3,JAUNE)
    jouer(p,3,ROUGE)
    jouer(p,3,JAUNE)
    jouer(p,3,ROUGE)
    jouer(p,3,JAUNE)
    jouer(p,3,ROUGE)
    jouer(p,4,JAUNE)
    jouer(p,4,JAUNE)
    jouer(p,4,ROUGE)
    jouer(p,4,ROUGE)
    jouer(p,5,JAUNE)
    jouer(p,5,ROUGE)
    jouer(p,5,JAUNE)    
    res = "OK" if contenu_case(p, 2, 2) == ROUGE else "KO"
    print(f"  jouer {res}")
    res = "OK" if nb_pions_alignes_horizontalement(p, 3,1) == 4 else "KO"
    print(f"  nb_pions_alignes_horizontalement {res}")       
    res = "OK" if nb_pions_alignes_verticalement(p, 4,1) == 2 else "KO"
    print(f"  nb_pions_alignes_verticalement {res}")
    res = "OK" if nb_pions_alignes_diagonalement_SONE(p, 4,3) == 2 else "KO"
    print(f"  nb_pions_alignes_diagonalement_SONE {res}")    
    res = "OK" if nb_pions_alignes_diagonalement_NOSE(p, 4,3) == 3 else "KO"
    print(f"  nb_pions_alignes_diagonalement_NOSE {res}")    
    
