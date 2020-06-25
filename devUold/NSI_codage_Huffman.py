# -*- coding: utf-8 -*-



def sequence_to_occurrences(seq):
    d={}
    for i in range(len(seq)):
        try:
            d[seq[i]]=d[seq[i]]+1
        except:
            d[seq[i]]=1
    e={}
    for k,v in sorted(d.items(),key=lambda x: x[1],reverse=True):
        e[k]=v
    return e
    

    
src = '''La Cigale et la Fourmi

La Cigale, ayant chanté
Tout l'été,
Se trouva fort dépourvue
Quand la bise fut venue :
Pas un seul petit morceau
De mouche ou de vermisseau.
Elle alla crier famine
Chez la Fourmi sa voisine,
La priant de lui prêter
Quelque grain pour subsister
Jusqu'à la saison nouvelle.
Je vous paierai, lui dit-elle,
Avant l'Oût, foi d'animal,
Intérêt et principal. 
La Fourmi n'est pas prêteuse :
C'est là son moindre défaut.
Que faisiez-vous au temps chaud ?
Dit-elle à cette emprunteuse.
Nuit et jour à tout venant
Je chantais, ne vous déplaise.
Vous chantiez ? j'en suis fort aise.
Eh bien! dansez maintenant.
'''    
    

dico=sequence_to_occurrences(src)

def complete(binary_str):
    reste=len(binary_str)%8
    binary_str=binary_str+"1"
    while len(binary_str)%8!=0:
        binary_str=binary_str+"0"
    return binary_str
    
b="0110001010110010"
b=complete(b)
