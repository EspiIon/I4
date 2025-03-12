#!/usr/bin/env python3
"""Module proposant des fonctions de manipulations de grille de Sudoku
"""
def coordonnee(colonne: int, ligne: int) -> "Coordonnee":
    """fonction permettant d'avoir une coordonnée d'une grille de Sudoku à partir d'une colonne (1..9) et d'une ligne (1..9)"""
    return (colonne, ligne)

def obtenir_colonne(coordonnee: "Coordonnee") -> int:
    """fonction permettant d'obtenir la colonne d'une coordonnée"""
    return coordonnee[0]

def obtenir_ligne(coordonnee: "Coordonnee") -> int:
    """fonction permettant d'obtenir la ligne d'une coordonnée"""
    return coordonnee[1]












def obtenir_carre(coordonnee: "Coordonnee") -> int:
    """fonction permettant d'obtenir la carré d'une coordonnée"""
    return 3 * ((obtenir_ligne(coordonnee) - 1) // 3) +\
        ((obtenir_colonne(coordonnee) - 1) // 3) + 1

def grille_vide() -> "GrilleSudoku":
    """fonction permettant d'obtenir une grille vide"""
    grille=[]
    for _ in range(8):
        grille.append([None]*9)
    return grille

def listes_chiffres_en_lignes_en_grille(lignes: list) -> "GrilleSudoku":
    """fonction permettant d'obtenir une grille à partir d'une liste de 9 lignes contenant 9 chiffres, 0 représentant une case vide"""
    return [[chiffre if chiffre>=1 else None for chiffre in ligne] for ligne in lignes]

def case_vide(grille: "GrilleSudoku", coordonnee: "Coordonnee") -> bool:
    """fonction qui permet de savoir si une case est vide"""
    vide= False
    ligne= obtenir_ligne(coordonnee)
    colonne=obtenir_colonne(coordonnee)
    vide = (grille[ligne][colonne] ==  None)
    return vide

def obtenir_chiffre(grille: "GrilleSudoku", coordonnee: "Coordonnee") -> int:
    """fonction qui permet d'obtenir le chiffre d'une case non vide"""
    chiffre = grille[obtenir_ligne(coordonnee)][obtenir_colonne(coordonnee)] 
    if chiffre != None:
        return chiffre
    return None
    
def fixer_chiffre(grille: "GrilleSudoku", coordonnee: "Coordonnee", chiffre: int) -> None:
    """fonction qui permet de mettre un chiffre dans une case vide"""
    if grille[obtenir_ligne(coordonnee)][obtenir_colonne(coordonnee)] == None:
        grille[obtenir_ligne(coordonnee)][obtenir_colonne(coordonnee)] = chiffre
    pass

def vider_case(grille: "GrilleSudoku", coordonnee: "Coordonnee") -> None:
    """fonction qui permet de vider une case"""
    grille[obtenir_ligne(coordonnee)][obtenir_colonne(coordonnee)] = None
    pass

def grille_en_chaine(grille: "GrilleSudoku") -> str:
    """fonction qui permet d'obtenir une représentation textuelle d'une grille"""
    chaine = ""
    for i in range(9):
        if i%3 == 0:
            for a in range(25):
                if a%8 == 0:
                    chaine = chaine + "+"
                else:
                    chaine = chaine + "-"
            chaine = chaine + "\n"
        chaine = chaine + "| "
        for j in range(9):
            if grille[i][j]==None:
                chaine= chaine + "  "
            else:
                chaine = chaine + str(grille[i][j])
                chaine= chaine + " "
            if j%3 == 2:
                chaine = chaine + "| "
        chaine = chaine + "\n"
        
    for a in range(25):
                if a%8 == 0:
                    chaine = chaine + "+"
                else:
                    chaine = chaine + "-"
    return chaine
                

if __name__ == "__main__":
    print("Tests unitaires :")
    
    print(" Coordonnee :")
    c = coordonnee(4,5)
    res = "OK" if obtenir_colonne(c) == 4 else "KO"
    print(f"  obtenir_colonne {res}")
    res = "OK" if obtenir_ligne(c) == 5 else "KO"
    print(f"  obtenir_ligne {res}")    
    res = "OK" if obtenir_carre(c) == 5 else "KO"
    print(f"  obtenir_ligne {res}")

    print(" GrilleSudoku :")
    g = grille_vide()
    res = "OK" if case_vide(g, c) else "KO"
    print(f"  case_vide vide {res}")
    fixer_chiffre(g, c, 5)
    res = "OK" if not case_vide(g, c) else "KO"
    print(f"  case_vide non vide {res}")    
    res = "OK" if obtenir_chiffre(g, c) == 5 else "KO" 
    print(f"  fixer_chiffre et obtenir_chiffre {res}")
    vider_case(g,c)
    res = "OK" if case_vide(g, c) else "KO"
    print(f"  vider_case {res}")

    print("Affichage d'une grille")
    from exemples_grilles import SIMPLE
    g = listes_chiffres_en_lignes_en_grille(SIMPLE)
    print(grille_en_chaine(g))
