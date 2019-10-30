
"""Module that contains Processing class that will answer the user's question
"""
import random
import os
import wikipedia
import requests
from constant import LISTE_CORS_GOOGLE, LISTE_MOT_CLES_NON_TROUVE, LISTE_SORS_WIKI
from .stopWord import DIC_STOPWORDS, KEY_WORDS
KEY_API_GOOGLE = os.environ['KEY_API_GOOGLE']

class Processing:
    """Class that receives a string question and will return the address
    """
    def __init__(self, question):
        self.question = question
        self.key_word = ''
        self.answer_question = {}

    def question_process(self):
        """Method recovers a question and filters the keywords and then returns this word
        """
        self.question = self.question.replace("'", " ")
        self.question = self.question.split(' ')
        # Enleve les stopwords de la question
        for ele in DIC_STOPWORDS:
            if ele in self.question:
                self.question.remove(ele)
        # Chercher le mots cle puis trouver les mots nessaicere pour la recherch google
        for i, quest in enumerate(self.question):
            if self.question[i] in KEY_WORDS:
                try:
                    self.key_word = self.question[i+1] + ' ' + self.question[i+2]
                    print(f'Key Word: {self.key_word}')
                    break
                except IndexError:
                    pass
                try:
                    self.key_word = self.question[i+1]
                    print(f'Key Word: {self.key_word}')
                except IndexError:
                    print(f'Mot de localisation trouvé : " {self.question[i]}" mais aucun destination')
        if self.key_word == '':
            self.answer_question['texte'] = random.choice(LISTE_MOT_CLES_NON_TROUVE)

    def google_process(self):
        """Method receives a keyword and then  search on google map to
            return the address of this place
        """
        api_search = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'
        payload = {
            'input': self.key_word,
            'inputtype': 'textquery',
            'fields': 'photos,formatted_address,name,rating,opening_hours,geometry',
            'key': KEY_API_GOOGLE,
            }
        Json_data = requests.get(api_search, params=payload).json()
        try:
            nom = Json_data['candidates'][0]['name']
            adresse = Json_data['candidates'][0]['formatted_address']
            self.answer_question['nom'] = nom
            self.answer_question['adresse'] = adresse
            self.answer_question['map'] = "https://www.google.com/maps/embed/v1/place?key=" \
            + KEY_API_GOOGLE + "&q=$"+ nom + adresse
        except IndexError as err:
            if 'texte' not in self.answer_question:
                self.answer_question['texte'] = random.choice(LISTE_CORS_GOOGLE)
                print(f'erreur google ne trouve aucun corespandance: {err}')

    def wiki_process(self):
        """A method that collects an address and then returns
            information about the address if it exists
        """
        wikipedia.set_lang("fr")
        try:
            if self.answer_question['nom']:
                self.answer_question['texte'] = wikipedia.summary(
                    (lambda s: s.split(",")[0])(self.answer_question['adresse']), sentences=2)
                return self.answer_question
        except:
            if 'texte' not in self.answer_question:
                self.answer_question['texte'] = random.choice(LISTE_SORS_WIKI)
                print('Erreur: Aucun corespondance trouvee dans API WikiMedia.')
                return self.answer_question
            return self.answer_question
