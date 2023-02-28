import graphviz
import json

# Charger le contenu du fichier JSON en tant qu'objet Python
with open('fichier.json',"r") as f:
    data = json.load(f)

# Recueil des différentes clés du dictionnaire 1 du fichier json
etape= []

for etapes in data[0]:
    etape += [etapes]

# Recueil des différentes clés du dictionnaire 2 du fichier json
lien = []

for liens in data[1]:
    lien += [liens]
    
# transformation du dict 1 l'objet json en dict python 
dictionnaire = {}

for element in data[0]:
    dictionnaire[element] = data[0][element]

print(dictionnaire)

# transformation du dict 2 l'objet json en dict python
dictionnaire_1 = dict()

for element in data[1]:
    dictionnaire_1[element] = data[1][element]

# création du graphe
dot = graphviz.Graph("automate")

# liste qui repertorie les etats ecris
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


#liens entre etats

#lien --
for couple in dictionnaire_1[lien[0]]:
    dot.edge(couple[0], couple[1])

#lien ->
for couple in dictionnaire_1[lien[1]]:
    dot.edge(couple[0], couple[1], dir="forward")

#lien <->
for couple in dictionnaire_1[lien[2]]:
    dot.edge(couple[0], couple[1], dir="both")

# Affichage du graphe
dot.view()