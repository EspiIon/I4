#!/usr/bin/env python3
""" Script permettant à un humain de jouer au jeu 2048 en mode texte"""
from jeu_2048 import faire_une_partie,  \
    VERS_HAUT, VERS_BAS, VERS_GAUCHE,VERS_DROITE
from grille_2048 import grille_en_chaine

DIRECTION_VERS_CHAINE = {
    VERS_HAUT : "8 (Haut)",
    VERS_BAS : "2 (Bas)",
    VERS_GAUCHE : "4 (Gauche)",
    VERS_DROITE : "6 (Droite)"
}

CHAINE_EN_DIRECTION = {
    "8" : VERS_HAUT,
    "2" : VERS_BAS,
    "4" : VERS_GAUCHE,
    "6" : VERS_DROITE
}

def afficher_grille(grille: "Grille2048", score: int) -> None:
    """ Affichage d'une grille """
    print(grille_en_chaine(grille))
    print(f"Score : {score}")

def obtenir_direction(grille: "Grille2048", score: int, directions_possibles: set) -> "VERS_HAUT|VERS_BAS|VERS_GAUCHE|VERS_DROITE":
    """ Saisie d'une direction par l'utilisateur """
    def saisie_ok(chaine):
        nonlocal deplacements
        if chaine in CHAINE_EN_DIRECTION:
            if CHAINE_EN_DIRECTION[res] in deplacements:
                return True
        return False

    deplacements = directions_possibles
    texte = "Direction(s) possible(s) : "
    for dep in deplacements:
        texte += DIRECTION_VERS_CHAINE[dep] + " "
    print(texte)
    res = input()
    while not saisie_ok(res):
        res = input()
    return CHAINE_EN_DIRECTION[res]

def main():
    """ Programme principal """
    faire_une_partie(afficher_grille, obtenir_direction)

if __name__ == "__main__":
    main()
