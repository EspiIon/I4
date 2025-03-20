#!/usr/bin/env python3
""" Logique métier du jeu 2048 """
from typing import List, Tuple
import random
from grille_2048 import grille_vide, case_vide, obtenir_valeur, fixer_valeur, \
    vider_case, obtenir_case_vide, grille_en_chaine, copier


VERS_HAUT = 1
VERS_BAS = 2
VERS_GAUCHE = 3
VERS_DROITE = 4

def ajouter_une_valeur(grille: "Grille2048",
                       score):
    """ Ajoute une valeur (2 ou 4) sur une case vide d'une grille
    non totalement remplie"""
    col, lig = obtenir_case_vide(grille)
    if score < 1000:
        fixer_valeur(grille, col, lig, 2)
    else:
        fixer_valeur(grille, col, lig, 2 if random.randrange(100) > min(50, score // 100) else 4)

def deplacer(grille: "Grille2048",
             direction: "VERS_HAUT|VERS_BAS|VERS_GAUCHE|VERS_DROITE") -> int:
    """ Fonction qui rélise un mouvement
    La valeur retournée correspond au gain lié à ce déplacement """

    def ligne(grille: "Grille2048", lig: int) -> List[int]:
        return [obtenir_valeur(grille, col, lig) if not case_vide(grille, col, lig) else 0
                for col in range(1,5)]

    def colonne(grille: "Grille2048", col: int) -> List[int]:
        return [obtenir_valeur(grille, col, lig) if not case_vide(grille, col, lig) else 0
                for lig in range(1,5)]

    def deplacer_gauche(valeurs: List[int]):
        nonlocal score
        temp = [valeur for valeur in valeurs if valeur != 0]
        for i in range(len(temp)-1):
            if temp[i] == temp[i+1]:
                temp[i] = temp[i] + temp[i+1]
                temp[i+1] = 0
                score = score + temp[i]
        temp = [valeur for valeur in temp if valeur != 0]
        return temp + [0] * (4-len(temp))

    score = 0
    if direction in (VERS_GAUCHE, VERS_DROITE):
        for lig in range(1,5):
            temp = ligne(grille, lig)
            if direction == VERS_DROITE:
                temp.reverse()
            temp = deplacer_gauche(temp)
            if direction == VERS_DROITE:
                temp.reverse()
            for col in range(1, 5):
                if col > len(temp) or temp[col-1] == 0:
                    vider_case(grille, col, lig)
                else:
                    fixer_valeur(grille, col, lig, temp[col-1])
    if direction in (VERS_HAUT, VERS_BAS):
        for col in range(1,5):
            temp = colonne(grille, col)
            if direction == VERS_BAS:
                temp.reverse()
            temp = deplacer_gauche(temp)
            if direction == VERS_BAS:
                temp.reverse()
            for lig in range(1, 5):
                if lig > len(temp) or temp[lig-1] == 0:
                    vider_case(grille, col, lig)
                else:
                    fixer_valeur(grille, col, lig, temp[lig-1])
    return score

def directions_possibles(grille : "Grille2048") -> set:
    """ Fonction qui retourne tous les directions possibles pour une grille donnée"""
    res = set()
    for dep in (VERS_HAUT, VERS_BAS, VERS_GAUCHE, VERS_DROITE):
        temp = copier(grille)
        deplacer(temp, dep)
        if grille != temp:
            res.add(dep)
    return res

def grille_de_depart() -> "Grille2048":
    """ Fonction qui retourne une grille initialisée avec deux 2
    positionnés aléatoirement"""
    grille = grille_vide()
    ajouter_une_valeur(grille, 0)
    ajouter_une_valeur(grille, 0)
    return grille

def jouer_une_partie_a_partir_d_une_position(grille: "Grille2048",
                                             afficher_grille: "Fonction(Grille2048, int) -> None",
                                             obtenir_direction_choisi: "Fonction(Grille2048, int, set) -> VERS_HAUT|VERS_BAS|VERS_GAUCHE|VERS_DROITE",
                                             score_initial: int) -> Tuple[int, int]:
    """ Fonction qui permet de jouer entièrement à partir d'une certaine position de la grille"""
    nbcoups=0
    partiefini =False
    gain=0
    while (gain<2048) and directions_possibles(grille):
        afficher_grille(grille,score_initial)
        direction=obtenir_direction_choisi(grille,score_initial,directions_possibles(grille))
        gain=deplacer(grille,direction)
        nbcoups+=1
        score_initial+=gain
        ajouter_une_valeur(grille,score_initial)
    afficher_grille(grille,score_initial)    
    return score_initial,nbcoups

def faire_une_partie(afficher_grille: "Fonction(Grille2048, int) -> None",
                     obtenir_direction_choisi: "Fonction(Grille2048, int, set) -> VERS_HAUT|VERS_BAS|VERS_GAUCHE|VERS_DROITE") -> Tuple[int, int]:
    """ Fonction qui permet de jouer une partie entière """

    grille = grille_de_depart()
    return jouer_une_partie_a_partir_d_une_position(grille, afficher_grille,  obtenir_direction_choisi, 0)

def tests():
    """ Des tests """
    grille = grille_vide()
    fixer_valeur(grille, 1, 2, 2)
    fixer_valeur(grille, 3, 2, 2)
    fixer_valeur(grille, 1, 1, 2)
    fixer_valeur(grille, 2, 3, 2)
    fixer_valeur(grille, 3, 3, 2)
    fixer_valeur(grille, 4, 3, 2)
    print(grille_en_chaine(grille))
    print(directions_possibles(grille))
    deplacer(grille, VERS_GAUCHE)
    print(grille_en_chaine(grille))

if __name__ == "__main__":
    tests()
