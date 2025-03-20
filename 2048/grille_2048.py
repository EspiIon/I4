#!/usr/bin/env python3
""" Module permettant de manipuler une grille du jeu 2048 """

from typing import Tuple
import random
import copy
import itertools

random.seed()

def grille_vide() -> "Grille2048":
    """ Obtention d'une grille du jeu 2048 vide """
    return [[0]*4 for i in range(4)]

def case_vide(grille: "Grille2048",
             colonne : "1..4", ligne : "1..4") -> bool:
    """ Permet de savoir si une case d'une grille est vide """
    return grille[ligne-1][colonne-1] == 0

def obtenir_valeur(grille: "Grille2048",
                   colonne : "1..4", ligne : "1..4") -> int:
    """ Permet d'obtenir la valeur d'une case non vide d'une grille"""
    return grille[ligne-1][colonne-1]

def fixer_valeur(grille: "Grille2048",
                 colonne : "1..4", ligne : "1..4",
                 valeur : int) -> None:
    """ Permet d'obtenir la valeur d'une case d'une grille"""
    grille[ligne-1][colonne-1] = valeur

def vider_case(grille: "Grille2048",
               colonne : "1..4", ligne : "1..4") -> None:
    grille[ligne-1][colonne-1] = 0
    
def remplie(grille: "Grille2048") -> bool:
    """ Permet de savoir si une gille est totalement remplie"""
    for col in range(1,5):
        for lig in range(1,5):
            if case_vide(grille, col, lig):
                return False
    return True

def obtenir_case_vide(grille: "Grille2048") -> Tuple[int, int]:
    """ Permet d'obtenir les coordonnées (colonne, ligne)
    d'une case vide d'une grille non totalement remplie"""
    cases_vides = [(col, lig) for col, lig in itertools.product(range(1,5), range(1,5))
                   if case_vide(grille, col, lig)]
    return random.choice(cases_vides)

def grille_en_chaine(grille: "Grille2048") -> str:
    taille_case = 6
    res = ""
    for lig in range(1,5):
        res += ("+"+"-"*taille_case)*4+"+\n"
        for i in range(taille_case // 4):
            res += ("|"+" "*taille_case)*4+"|\n"
        for col  in range(1,5):
            res += "|" + f"{obtenir_valeur(grille, col, lig):^6}" if not case_vide(grille, col, lig) else "|" + " "*taille_case
        res += "|\n"
        for i in range(taille_case // 4):
            res += ("|"+" "*taille_case)*4+"|\n"
    res += ("+"+"-"*taille_case)*4+"+\n"
    return res

def copier(grille: "Grille2048") -> "Grille2048":
    return copy.deepcopy(grille)

def tests():
    g = grille_vide()
    fixer_valeur(g, 2, 3, 2)
    print(grille_en_chaine(g))

if __name__ == "__main__":
    tests()
