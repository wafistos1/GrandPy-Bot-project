from grandPy.processing import Processing
from constant import LISTE_CORS_GOOGLE, LISTE_MOT_CLES_NON_TROUVE, LISTE_MOT_CLES_NON_TROUVE
import unittest


questions = {
'no_key_word': "Salut GrandPy ! Est-ce que tu connais d'openclassrooms",
'no_google': "Salut GrandPy ! Est-ce que tu connais l'adresse balsdfasdfsf",
'no_wiki': "Salut GrandPy ! Est-ce que tu connais l'adresse d'openclassrooms",
}

class TestProcessing(unittest.TestCase):
    
    def test_method_question_process_is_ok(self):
        test_question = Processing(questions['no_key_word'])
        test_question.question_process()
        test_question.google_process()
        data = test_question.wiki_process()
        print(data['texte'])
        self.assertIn( data['texte'] , LISTE_MOT_CLES_NON_TROUVE)

    def test_method_google_process_is_ok(self):
        test_question = Processing(questions['no_google'])
        test_question.question_process()
        test_question.google_process()
        data = test_question.wiki_process()
        print(data['texte'])
        self.assertIn( data['texte'] , LISTE_CORS_GOOGLE)