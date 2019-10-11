import wikipedia
import requests
import random
from constant import LISTE_CORS_GOOGLE, LISTE_MOT_CLES_NON_TROUVE, LISTE_SORS_WIKI


# Function that searches for a keyword in the list mot_cla_chaine and return it
def touver_place(chaine):
    

    for i in range(len(chaine) - 1):
        if chaine[i] in mot_cle_chaine:
            return chaine[i + 1]


# a function that looks for the location of an address and return it
def search(place):
   
    
   
    Json_data = requests.get(api_search, params=payload).json()

    try:
        Json_data['candidates'][0]['name']
    except(IndexError):
        reponse_question['texte'] = random.choice(LISTE_MOT_CLES_NON_TROUVE)  # Cas Corp pas de mot cle trouver
        print('Aucun corespondance au mot cle')
        return reponse_question
    nom = Json_data['candidates'][0]['name']
    adresse = Json_data['candidates'][0]['formatted_address']
    photo = Json_data['candidates'][0]['geometry']['location']
    print(photo)
    reponse_question['nom'] = nom
    reponse_question['adresse'] = adresse
    reponse_question['photo'] = photo
    # to do // ajouter lien et pour le frame 

    """ Wikipedia API recive addresse element from dic ( reponse_question) and return all data (dic { 'nom', 'adresse',
        'text'}) 
    """

    wikipedia.set_lang("fr")
    try:
        reponse_question['texte'] = wikipedia.summary((lambda s: s.split(",")[0])(adresse), sentences=2)
    except:
        reponse_question['texte'] = random.choice(LISTE_SORS_WIKI)   # Cas Corp pas de mot cle trouve
        return reponse_question
    return reponse_question

# function that cuts a sentence into several words and eliminates unnecessary words and return list
def chaine_formated(chaine):
    chaine = chaine.replace("'", " ")
    chaine = chaine.split(' ')
    

    for ele in chaine1:
        if ele in chaine:
            chaine.remove(ele)
    return search(touver_place(chaine))



