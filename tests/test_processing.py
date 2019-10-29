from grandPy.processing import Processing
from constant import LISTE_CORS_GOOGLE, LISTE_MOT_CLES_NON_TROUVE, LISTE_SORS_WIKI
import unittest
import requests
import json
from io import BytesIO
from _pytest.monkeypatch import monkeypatch

questions = {
'no_key_word': "Salut GrandPy ! Est-ce que tu connais d'openclassrooms",
'no_google': "Salut GrandPy ! Est-ce que tu connais l'adresse balsdfasdfsf",
'no_wiki': "Salut GrandPy ! Est-ce que tu connais l'adresse du monument des martyres ?",
'response':"Salut GrandPy ! Est-ce que tu connais l'adresse d'openclassrooms"
}

response_google = {
    'candidates':[{
    'formatted_address': '7 Cité Paradis, 75010 Paris, France', 
    'geometry': {'location': {'lat': 48.8748465, 'lng': 2.3504873},
    'viewport': {'northeast': {'lat': 48.87622362989272, 'lng': 2.351843679892722},
        'southwest': {'lat': 48.87352397010727, 'lng': 2.349144020107278}}}, 
    'name': 'OpenClassrooms', 
    'opening_hours': {'open_now': True}, 
    'rating': 3.3}], 
    'status': 'OK'
    }
response_wiki = {
    'texte': 'La cité Paradis est une voie publique située dans le 10e arrondissement de Paris.== Situation et accès ==La cité Paradis est une voie publique située dans le 10e arrondissement de Paris.'
}


def change_question(question):
    test_question = Processing(question)
    test_question.question_process()
    test_question.google_process()
    data = test_question.wiki_process()
    return data


class Test_Processing():
    
    def test_method_question_process_is_not_ok(self):
        data = change_question(questions['no_key_word'])
        assert data['texte'] in LISTE_MOT_CLES_NON_TROUVE

    def test_method_google_process_is_not_ok(self):
        data = change_question(questions['no_google'])
        assert data['texte'] in LISTE_CORS_GOOGLE

    def test_method_wiki_is_not_ok(self):
        data = change_question(questions['no_wiki'])
        assert data['texte'] in LISTE_SORS_WIKI
    
    def test_method_question_is_ok(self, monkeypatch):
        '''tester le mot cle dans la question '''
        question_test = Processing(questions['response'])
        question_test.question_process()
        monkeypatch.setattr('requests.get', response_google)
        assert question_test.key_word == 'Openclassrooms'

    def test_method_google_is_ok(self, monkeypatch): #  Utiliser le mock 
        '''tester si google api return la bonne reponse  '''
        question_test = change_question(questions['response'])
        monkeypatch.setattr('requests.get', response_google)
        assert question_test['adresse'] == '7 Cité Paradis, 75010 Paris, France'
        
    
    def test_method_wiki_is_ok(self, monkeypatch): #  Utiliser le mock
        '''tester si google api return la bonne reponse  '''
        question_test = change_question(questions['response'])
        question_test['texte'] = question_test['texte'].replace('\n', '')
        monkeypatch.setattr('requests.get', response_wiki)
        assert question_test['texte'] == response_wiki['texte']
