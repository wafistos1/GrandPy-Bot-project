from grandPy.processing import Processing
from constant import LISTE_CORS_GOOGLE, LISTE_MOT_CLES_NON_TROUVE, LISTE_SORS_WIKI
import unittest
import urllib.request
import json
from io import BytesIO
from _pytest.monkeypatch import monkeypatch
questions = {
'no_key_word': "Salut GrandPy ! Est-ce que tu connais d'openclassrooms",
'no_google': "Salut GrandPy ! Est-ce que tu connais l'adresse balsdfasdfsf",
'no_wiki': "Salut GrandPy ! Est-ce que tu connais l'adresse du monument des martyres ?",
'response':"Salut GrandPy ! Est-ce que tu connais l'adresse d'openclassrooms"
}


def change_question(question):
    test_question = Processing(question)
    test_question.question_process()
    test_question.google_process()
    data = test_question.wiki_process()
    return data


class TestProcessing(unittest.TestCase):
    
    def test_method_question_process_is_not_ok(self):
        data = change_question(questions['no_key_word'])
        self.assertIn(data['texte'], LISTE_MOT_CLES_NON_TROUVE)

    def test_method_google_process_is_not_ok(self):
        data = change_question(questions['no_google'])
        self.assertIn(data['texte'], LISTE_CORS_GOOGLE)

    def test_method_wiki_is_not_ok(self):
        data = change_question(questions['no_wiki'])
        self.assertIn(data['texte'], LISTE_SORS_WIKI)
    
    def test_method_question_is_ok(self): # Utiliser le mock
        '''tester le mot cle dans la question '''
        result = 'openclassrooms'
        question = Processing(questions['response'])
        mot = question.key_word
        def mockreturn(request):
            return result
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert mot == result
            
    
    def test_method_google_is_ok(self): #  Utiliser le mock
        '''tester si google api return la bonne reponse  '''
        return ''
    
    def test_method_wiki_is_ok(self): #  Utiliser le mock
        '''tester si google api return la bonne reponse  '''
        return ''
