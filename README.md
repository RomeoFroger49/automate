# automate

Le programme Automate permet de  :

- de charger la description d'un automate sous forme d'un fichier texte (json)
- d'afficher l'automate à l'écran ou de générer un fichier image
- d'afficher / lister les états accessibles et co-accessibles
- de compléter l'automate
- de déterminiser l'automate en détaillant les étapes
- de sauvegarder la description d'un automate sous forme d'un fichier texte dont le format respecte celui en lecture


Description technique : 

- Je me suis aidé du package graphviz qui facilite la création et le rendu des descriptions de graphes.

Utilisation : 

- veuillez renseignez vos états dans le dossier .json ainsi que leur lien dans le deuxieme dict
- "->" = lien d'un etat vers un autre / "--" = lien simple entre deux états
- préciser le couple du type de lien en valeur sous forme de liste de 2 
