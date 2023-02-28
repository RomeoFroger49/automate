import graphviz
import json

# Charger le contenu du fichier JSON en tant qu'objet Python
with open('fichier.json',"r") as f:
    data = json.load(f)

# Convertir les données JSON en dictionnaire
etape= []

for etapes in data[0]:
    etape += [etapes]

dictionnaire = {}

for element in data[0]:
    dictionnaire[element] = data[0][element]

print(dictionnaire)

dot = graphviz.Graph("automate")

etat_ecris = []

#creation des etats initiaux
for etat_init in dictionnaire[etape[2]]:
    dot.edge(etat_init, etat_init)
    etat_ecris += etat_init

#creation des etats finaux
for etat_final in dictionnaire[etape[3]]:
    dot.attr('node', shape='doublecircle')
    dot.node(etat_final)
    etat_ecris += etat_final
    dot.attr('node', shape='circle')

nb_etat_ecris = len(etat_ecris)

#creation des etats restants
for etat_restant in dictionnaire[etape[1]]:
    nb_etat = 0
    for etat in etat_ecris:
        if etat_restant != etat:
            nb_etat += 1
    if nb_etat == nb_etat_ecris:
        dot.node(etat_restant)
        nb_noeud = 0
    else:
        nb_noeud = 0



# Affichage du graphe
dot.view()