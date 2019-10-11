# Modul ......
import wikipedia
import requests
import random
from constant import LISTE_CORS_GOOGLE, LISTE_MOT_CLES_NON_TROUVE, LISTE_SORS_WIKI
from stopWord import DIC_STOPWORDS, KEY_WORDS
from api_key import KEY_API_GOOGLE

class Processing:
    def __init__(self, question):
        self.question = question
        self.key_word = ''
        self.answer_question = {}

    def question_process(self):
        """Method recovers a question and filters the keywords and then returns this word
        """
        self.question = self.question.replace("'", " ")
        self.question = self.question.split(' ')

        for ele in DIC_STOPWORDS:
            if ele in self.question:
                self.question.remove(ele)
        
        for i in range(len(self.question) - 1):
            if self.question[i] in KEY_WORDS:
                self.key_word = self.question[i + 1]
                
        
    def google_process(self):
        """Method receives a keyword and then  search on google map to return the address of this place
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
            Json_data['candidates'][0]['name']
        except IndexError as err:
            self.answer_question['texte'] = random.choice(LISTE_MOT_CLES_NON_TROUVE)
            print(f"erreur: {err}")
            # Sortir directement de la methode //todo
        nom = Json_data['candidates'][0]['name']
        adresse = Json_data['candidates'][0]['formatted_address']
        photo = Json_data['candidates'][0]['geometry']['location']
        self.answer_question['nom'] = nom
        self.answer_question['adresse'] = adresse
        self.answer_question['photo'] = photo


    def wiki_process(self):
        """A method that collects an address and then returns information about the address if it exists 
        """
        try:
            self.answer_question['texte'] = wikipedia.summary((lambda s: s.split(",")[0])(adresse), sentences=2)
        except:
            self.answer_question['texte'] = random.choice(LISTE_SORS_WIKI)   # Cas Corp pas de mot cle trouve
            print('Aucun corespondance trouvee dans API WikiMedia.')

