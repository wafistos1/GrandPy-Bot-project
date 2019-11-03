
#
# Projet7 "Créez GrandPy Bot, le papy-robot"



## Ce programme est un chabot qui répond aux questions posées par l'utilisateur, il va simuler le rôle d'un grand-père qui va raconter une histoire autour d'un endroit, mais agrémentée d'un long récit très intéressant.

## Pour commencer
- Ce programme se compose des éléments suivants

### Partie Tchat(interaction avec l'utilisateur)

- Le programme simule une discussion avec une personne (grand-père) pour trouver l'adresse d'un emplacement(endroit, adresse), l'utilisateur saisi une question et le programme(grand-père) vas donner une réponse avec une image (google map) de l'adresse puis le programme va raconter (si existe) une petite histoire autour de l'adresse.    

### Partie recherchent d'informations.

- Pour la partie recherche d'information le programme va s'appuie sur deux API (google map et WikiMedia).

### Les  différentes réponses.
On peut personnaliser les réponses envoyées a l'utilisateur on ajoutant ou modifiant les phrases qui se trouvent dans le fichier `constant.py`.
On a trois  listes de réponses:
`LISTE_MOT_CLES_NON_TROUVE`: c'est quand le programme ne trouve pas de mot-clé qui sont dans la liste `KEY_WORDS` du fichier `stopWord.py`
`LISTE_CORS_GOOGLE`: c'est quand le programme ne trouve pas de corrspondance on effectuant une recherche sur api google map
`LISTE_SORS_WIKI`: c'est quand le programme ne trouve pas de corrspondance on effectuent une recherche sur api WikiMedia.

### Pré-requis

Ce qu'il est requis pour commencer avec mon programme.

- Installer Python3. 
- Installer les dependances avec le fichier `requirements.txt`.
- Renommer le fichier `api_key.py.exemple` en `api_key.py`  et mettre la API_KEY de google map dedans.

## Démarrage

Pour lancer votre projet
 
- Taper dans un terminal `python3 run.py` 
## Fabriqué avec

Les programmes/logiciels/ressources utilisé pour développer le projet


* [Api google place](https://cloud.google.com/maps-platform/places/?hl=fr)- Recherche une adresse.
* [Wikipedia-API 0.5.2](https://pypi.org/project/Wikipedia-API/)- Recherche des informations.
* [Visual-Studio-code](https://code.visualstudio.com) - Editeur de textes.
* [Heroku](https://www.heroku.com) - Hebergement du programme.



## Auteurs
auteur(s) du projet 
* **Ouafi MAMERI** _WAFI_ [mameri.wafi@gmail.com](https://github.com/wafistos1/Projet7)


_(https://github.com/wafistos1/Projet7 ``/GitHub``)_
_(https://trello.com/b/gByrXXxQ/grandpy ``/Trello``)_
_(https://grandpy1.herokuapp.com ``/Heroku``)_

