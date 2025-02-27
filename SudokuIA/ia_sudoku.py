#!/usr/bin/env python3

from grille_sudoku import coordonnee, obtenir_colonne, obtenir_ligne, obtenir_carre, \
    grille_vide, listes_chiffres_en_lignes_en_grille, \
    case_vide, obtenir_chiffre, fixer_chiffre, vider_case, grille_en_chaine

def grille_remplie(grille: "GrilleSudoku") -> bool:
    for colonne in range(1,10):
        for ligne in range(1, 10):
            if case_vide(grille, coordonnee(colonne, ligne)):
                return False
    return True

def obtenir_chiffres_d_une_ligne(grille: "GrilleSudoku", ligne: int) -> set:
    ensemble=set()
    for i in range(len(grille[ligne])):
        coord=coordonnee(i,ligne)
        if not case_vide(grille,coord):
            ensemble.add(obtenir_chiffre(grille,coord))
    return ensemble

def obtenir_chiffres_d_une_colonne(grille: "GrilleSudoku", colonne: int) -> set:
    ensemble=set()
    for i in range(len(grille)):
        coord=coordonnee(colonne,i)
        if not case_vide(grille,coord):
            ensemble.add(obtenir_chiffre(grille,coord))
    return ensemble

def obtenir_chiffres_d_un_carre(grille: "GrilleSudoku", carre: int) -> set:
    colonne_dep = 3 * (carre % 3 - 1) + 1
    ligne_dep = 3 * ((carre - 1) // 3) + 1
    return {obtenir_chiffre(grille, coordonnee(colonne, ligne))
            for colonne in range(colonne_dep, colonne_dep+3)
            for ligne in range(ligne_dep, ligne_dep+3)
            if not case_vide(grille, coordonnee(colonne, ligne))}

def est_chiffre_valable(grille: "GrilleSudoku",
                        coord : "Coordonnee",
                        chiffre: int) -> bool:
    ChiffresLigne=obtenir_chiffres_d_une_ligne(grille,obtenir_ligne(coord))
    ChiffresColonne=obtenir_chiffres_d_une_colonne(grille,obtenir_colonne(coord))
    ChiffreCarre = obtenir_chiffres_d_un_carre(grille,obtenir_carre(coord))
    if not((chiffre in ChiffresColonne | ChiffresLigne | ChiffreCarre)):
        return True
    return False


def obtenir_solutions_possibles(grille: "GrilleSudoku",
                                coord : "Coordonnee") -> set:
    solutions =set()
    for i in range(8):
        if est_chiffre_valable(grille,coord,i+1):
            solutions.add(i+1)
    return solutions

def _trouver_case_vide(grille):
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            coord =coordonnee(i,j)
            if case_vide(grille,coord):
                return coord
    return coord
def resoudre_sudoku(grille: "GrilleSudoku") -> bool:
    if grille_remplie(grille):
        return True
    else:
        coord=_trouver_case_vide(grille)
        solutions=obtenir_solutions_possibles(grille,coord)
        print(coord)
        for i in solutions:
            print(i)
            fixer_chiffre(grille,coord,i)
            print(solutions)
            resoudre_sudoku(grille)
    return False

def main():
    print("Tests unitaires :")
    la_grille = grille_vide()
    fixer_chiffre(la_grille, coordonnee(5, 1), 3)
    fixer_chiffre(la_grille, coordonnee(6, 1), 5)
    fixer_chiffre(la_grille, coordonnee(2, 2), 2)
    fixer_chiffre(la_grille, coordonnee(3, 2), 3)
    fixer_chiffre(la_grille, coordonnee(3, 3), 9)
    fixer_chiffre(la_grille, coordonnee(8, 3), 6)
    fixer_chiffre(la_grille, coordonnee(9, 3), 7)
    fixer_chiffre(la_grille, coordonnee(2, 5), 9)
    fixer_chiffre(la_grille, coordonnee(4, 5), 7)
    fixer_chiffre(la_grille, coordonnee(7, 5), 1)
    fixer_chiffre(la_grille, coordonnee(1, 6), 6)
    fixer_chiffre(la_grille, coordonnee(2, 6), 2)
    fixer_chiffre(la_grille, coordonnee(6, 6), 3)
    fixer_chiffre(la_grille, coordonnee(8, 6), 9)
    fixer_chiffre(la_grille, coordonnee(2, 7), 3)
    fixer_chiffre(la_grille, coordonnee(3, 7), 8)
    fixer_chiffre(la_grille, coordonnee(4, 7), 9)
    fixer_chiffre(la_grille, coordonnee(2, 8), 5)
    fixer_chiffre(la_grille, coordonnee(5, 8), 4)
    fixer_chiffre(la_grille, coordonnee(7, 8), 2)
    fixer_chiffre(la_grille, coordonnee(9, 8), 8)
    fixer_chiffre(la_grille, coordonnee(3, 9), 4)
    fixer_chiffre(la_grille, coordonnee(5, 9), 2)
    fixer_chiffre(la_grille, coordonnee(7, 9), 6)
    print("Grille de référence")
    print(grille_en_chaine(la_grille))
    res = "OK" if not grille_remplie(la_grille) else "KO"
    print(f"  grille_remplie {res}")
    chiffres = obtenir_chiffres_d_une_ligne(la_grille,6)
    res = "OK" if chiffres == {6,2,3,9} else "KO"
    print(f"  obtenir_chiffres_d_une_ligne {res}")
    chiffres = obtenir_chiffres_d_une_colonne(la_grille,3)
    res = "OK" if chiffres == {3,9,8,4} else "KO"
    print(f"  obtenir_chiffres_d_une_colonne {res}")
    chiffres = obtenir_chiffres_d_un_carre(la_grille,4)
    res = "OK" if chiffres == {9,6,2} else "KO"
    print(f"  obtenir_chiffres_d_un_carre {res}")   
    res = "OK" if est_chiffre_valable(la_grille, coordonnee(5,6), 1) else "KO"
    print(f"  est_chiffre_valable valable {res}")
    res = "OK" if not est_chiffre_valable(la_grille, coordonnee(5,6), 2) else "KO"
    print(f"  est_chiffre_valable non valable {res}")  
    res = "OK" if obtenir_solutions_possibles(la_grille, coordonnee(5,6)) == {1,5,8} else "KO"
    print(f"  obtenir_solutions_possibles {res}")
    print("\nResolution")
    print(" Grille à résoudre")
    from exemples_grilles import SIMPLE
    la_grille = listes_chiffres_en_lignes_en_grille(SIMPLE)
    print(grille_en_chaine(la_grille))
    if resoudre_sudoku(la_grille):
        print(" Grille résolue")
        print(grille_en_chaine(la_grille))

if __name__ == "__main__":
    main()
