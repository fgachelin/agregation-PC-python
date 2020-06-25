# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 21:11:55 2019

@author: click
"""

cartes=["Batteleur",
        "Papesse",
        "Impératrice",
        "Empereur",
        "Pape",
        "Amoureux",
        "Chariot",
        "Justice",
        "Ermite",
        "Roue de Fortune",
        "Force",
        "Pendu",
        "Mort",
        "Tempérance",
        "Diable",
        "Maison Dieu",
        "Etoile",
        "Lune",
        "Soleil",
        "Jugement",
        "Monde",
        "Mat"
        ]










cartes_ref=["Batteleur",
        "Papesse",
        "Impératrice",
        "Empereur",
        "Pape",
        "Amoureux",
        "Chariot",
        "Justice",
        "Ermite",
        "Roue de Fortune",
        "Force",
        "Pendu",
        "Mort",
        "Tempérance",
        "Diable",
        "Maison Dieu",
        "Etoile",
        "Lune",
        "Soleil",
        "Jugement",
        "Monde",
        "Mat"
        ]

modes_de_tirage={"2 cartes":[["Situation actuelle","Résultat"]],
                 "3 cartes pour/contre/résultat":[["Pour","Contre","Résultat"]],
                 "3 cartes passé/présent/futur":[["Passé","Présent","Futur"]],
                 "Pyramide":[[" ","Résultat"," "],["Passé","Présent","Futur"]],
                 "Croix":[[" ","Force dominante"," "],["Pour","Synthèse","Contre"],[" ","Résultat"," "]]
                 }

ordre_de_tirage={"2 cartes":["Situation actuelle","Résultat"],
                 "3 cartes pour/contre/résultat":["Pour","Contre","Résultat"],
                 "3 cartes passé/présent/futur":["Passé","Présent","Futur"],
                 "Pyramide":["Passé","Présent","Futur","Résultat"],
                 "Croix":["Pour","Contre","Force dominante","Résultat","Synthèse"]
                 }