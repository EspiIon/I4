#!/usr/bin/env python3

""" IA du jeu 2048 utilisant la méthode de Monté Carlo"""
import random
import sys,copy
from jeu_2048 import jouer_une_partie_a_partir_d_une_position, faire_une_partie, deplacer, ajouter_une_valeur,VERS_HAUT,VERS_BAS,VERS_GAUCHE,VERS_DROITE
from grille_2048 import copier
from jeu_2048_ihm_texte import afficher_grille, DIRECTION_VERS_CHAINE
NB_ESSAIS = 100

def obtenir_direction_aleatoire(grille: "Grille2048",
                                score: int,
                                directions_possibles: set) -> "VERS_HAUT|VERS_BAS|VERS_GAUCHE|VERS_DROITE":
    """ Retourne un direction aléatoire """
    return random.choice(list(directions_possibles))

def obtenir_direction(grille: "Grille2048",
                      score: int,
                      directions_possibles: set) -> "VERS_HAUT|VERS_BAS|VERS_GAUCHE|VERS_DROITE":
    """ Retourne un direction 'optimal'"""
    valeursCoups = {VERS_HAUT:0,VERS_BAS:0,VERS_GAUCHE:0,VERS_DROITE:0}
    for direction in directions_possibles:
        scoretot=0
        for _ in range(NB_ESSAIS):
            copygrille = copier(grille)
            score+=deplacer(copygrille,direction)
            score,_=jouer_une_partie_a_partir_d_une_position(copygrille,lambda _1 ,_2:None,obtenir_direction_aleatoire,score)
            scoretot+= score
            score=0
        valeursCoups[direction]=scoretot/NB_ESSAIS
    coupsfinal=max(valeursCoups, key=valeursCoups.get)
    print(f"{valeursCoups=} {coupsfinal=}")
    return coupsfinal

def main():
    """ Programme principal """
    faire_une_partie(afficher_grille, obtenir_direction)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        NB_ESSAIS = int(sys.argv[1])
    main()
