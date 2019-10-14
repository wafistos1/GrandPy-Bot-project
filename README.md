
#
# Projet5 "Créez GrandPy Bot, le papy-robot"



## Ce programme va créer un robot qui vous répondrait comme votre grand-père ! Si vous lui demandez l'adresse d'un lieu, il vous la donnera, certes, mais agrémentée d'un long récit très intéressant.

## Pour commencer
- Ce programme ce compose des elements suivants

### Partie Tchat

- Le programme simule une discution avec une personne (grand-pere) pour trouver l'adresse d'un enplacement, l'utilisateur saisie une question et le programme(grand-pere) vas donner une reponse avec une images (google map) de l'adresse puis le programme va raconte (si existe) une petite histoire autour de l'adresse.    

### Partie recherche d'informations.

- Pour la partie recherche d'informations le programme va s'appuier sur deux API (google map et WikiMedia).

### Les differentes reponses.
On peut personnaliser les reponses envoye a l'utilisateur on ajoutant ou modifiant les phrases qui se trouves dans le fichier `constant.py`.
On a trois  listes de reponses:
`LISTE_MOT_CLES_NON_TROUVE`: c'est quand le programme ne trouve pas de mot cle qui sont dans la liste `KEY_WORDS` du fichier `stopWord.py`
`LISTE_CORS_GOOGLE`: c'est quand le programme ne trouve pas de corspondance on effectuant une recherche sur api google map
`LISTE_SORS_WIKI`: c'est quand le programme ne trouve pas de corspondance on effectuant une recherche sur api WikiMedia.

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
