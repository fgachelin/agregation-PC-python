# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 20:28:44 2019

@author: click
"""

print("------------------------------------\n")
print("|         Tarow WineDot 2019       |\n")
print("------------------------------------\n\n")


from random import randint

from oracleAmoi import *

def choix_methode_tirage():
    global emplacements,mode,tas,tirage
    print("Modes de tirages possibles:")
    modes=list(modes_de_tirage.keys())
    for i in range(len(modes)):
        print(i+1," -> ",modes[i])
    choix=int(input("Choix numéro "))-1
    mode=modes[choix]
    tas=modes_de_tirage[mode] 
    tirage={}
    for ligne in tas:
        for colonne in ligne:
            if colonne!=" ":
                tirage[colonne]=[]
    emplacements=ordre_de_tirage[mode]
    print("++++++++++++++++++++++++++++++++++++\n")
    
choix_methode_tirage()
    

def tirage_aleatoire_carte(cartes,tirage,emplacement):
    """
    tirage aleatoire d une carte dans le tableau cartes 
    puis insertion dans tirage à l'emplacement
    """
    if len(cartes)>0:
        if emplacement!="Synthèse":
            numero_carte=randint(0,len(cartes)-1)
            carte_tiree=cartes[numero_carte]
            tirage[emplacement].append(carte_tiree)
            del cartes[numero_carte]
            print("------------------------------------\n")
            print("Carte tirée: ",carte_tiree)
            print("------------------------------------\n")
        else:
            valeur=valeur_de_synthese()
            tirage[emplacement].append(valeur)
            numero_carte=int(cartes.index(valeur))
            del cartes[numero_carte]
    else:
        print("\nPlus de cartes !\n")

def valeur_de_synthese():
    somme=0
    for i in range(4):
        somme=somme+1+cartes_ref.index(tirage[emplacements[i]][-1])
    if somme>22:
        somme=str(somme)
        somme=int(somme[0])+int(somme[1])
    return cartes_ref[somme-1]


def affiche_tirage(tas,tirage):
    print("------------------------------------\nTirage ",mode,"\n")
    for ligne in tas:
        for carte in ligne:
            if carte!=" ":
                print(carte)
                print("  |  ",end="")
                for i in tirage[carte]:
                    print(i,end="  |  ")
                print()


def propose_tirage(cartes,tas,tirage):
    print("------------------------------------\n")
    print("Dans quel tas voulez-vous ajouter une carte?")
    liste_tas=list(tirage.keys())
    for t in range(len(tirage)):
        print(t+1," -> ",liste_tas[t])
    tas_choisi=int(input("Je choisis le numéro: "))
    tirage_aleatoire_carte(cartes,tirage,liste_tas[tas_choisi-1])
    affiche_tirage(tas,tirage)
    propose_tirage(cartes,tas,tirage)


def fait_un_tirage():
    global cartes,cartes_ref
    for emplacement in ordre_de_tirage[mode]:
        print(emplacement)
        tirage_aleatoire_carte(cartes,tirage,emplacement)
    affiche_tirage(tas,tirage)
    print("------------------------------------\n")
    print("Choix 1: Continuer le tirage")
    print("Choix 2: Faire un autre tirage")
    print("Choix 3: Quitter")
    tirage_suivant=input("Votre choix: ")
    print("------------------------------------\n")
    if tirage_suivant=="1":
        fait_un_tirage()
    if tirage_suivant=="2":
        cartes=cartes_ref.copy()
        choix_methode_tirage()
        fait_un_tirage()
    

#propose_tirage(cartes,tas,tirage)
fait_un_tirage()


