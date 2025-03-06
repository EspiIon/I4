#!/usr/bin/env python3

from plateau_puissance4 import plateau_rempli, contenu_case, \
    hauteur_colonne, colonne_remplie, jouer,\
    nb_pions_alignes_horizontalement, nb_pions_alignes_verticalement, \
    nb_pions_alignes_diagonalement_SONE, nb_pions_alignes_diagonalement_NOSE,plateau_vide,\
    HAUTEUR_PLATEAU, LARGEUR_PLATEAU, JAUNE, ROUGE,VIDE

import random

def obtenir_meilleur_coup(plateau: "Plateau", couleur: "JAUNE|ROUGE") -> int:
    """Fonction qui sera redéveloppée dans le deuxième TP sur le puissance 4
Pour l'instant le choix du coup est aléatoire"""
    coup_trouve = False
    while not coup_trouve:
        colonne_choisie = random.randrange(1, LARGEUR_PLATEAU)
        coup_trouve = not colonne_remplie(plateau, colonne_choisie)
    return colonne_choisie

def obtenir_coups_possible(plateau) -> set[int]:
    """Retourne un ensemble de numero qui correspond aux colonne jouable"""
    colonnes_Libre = set()
    for i in range(1,LARGEUR_PLATEAU+1):
        if not colonne_remplie(plateau,i):
            colonnes_Libre.add(i)
    return colonnes_Libre

def autre_couleur(couleur):
    """Retourne la couleur du joueur adverse"""
    if couleur == JAUNE:
        return ROUGE
    else:
        return JAUNE
def score(plateau,couleur):
    score=0
    for i in range(HAUTEUR_PLATEAU):
        for j in range(LARGEUR_PLATEAU):
            if plateau[i][j]==couleur:
                if (nb_pions_alignes_horizontalement(plateau,j,i)) ==1:
                    score+=1
                elif (nb_pions_alignes_horizontalement(plateau,j,i)) ==2:
                    score+=5
                elif (nb_pions_alignes_horizontalement(plateau,j,i)) ==3:
                    score+=10
                elif (nb_pions_alignes_horizontalement(plateau,j,i)) ==4:
                    score+=10000

                if (nb_pions_alignes_verticalement(plateau,j,i)) ==1:
                    score+=1
                elif (nb_pions_alignes_verticalement(plateau,j,i)) ==2:
                    score+=5
                elif (nb_pions_alignes_verticalement(plateau,j,i)) ==3:
                    score+=10
                elif (nb_pions_alignes_verticalement(plateau,j,i)) ==4:
                    score+=10000

                score+= 10**(nb_pions_alignes_diagonalement_NOSE(plateau,j,i))
                score+= 10**(nb_pions_alignes_diagonalement_SONE(plateau,j,i))
    return score


def evaluer(plateau: "Plateau", couleur: "JAUNE|ROUGE") -> int:
    return score(plateau,couleur)-score(plateau,autre_couleur(couleur))

p = plateau_vide()
jouer(p,1,ROUGE)
jouer(p,1,ROUGE)
jouer(p,1,JAUNE)
jouer(p,1,ROUGE)
res = "OK" if obtenir_coups_possible(p) == {1,3,4,7} else "KO"
print("Obtenir coups: ",res)

print(evaluer(p,ROUGE))
print(score(p,JAUNE))
