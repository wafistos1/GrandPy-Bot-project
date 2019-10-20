# Modul for test views
from grandPy.processing import Processing
import json


def test_if_views_return_response():
    ''' tester si la question est un format valide'''
    # mock la question
    mock_data = {'status': 'OK'}
    question_asked = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    question = Processing(question_asked)
    question.question_process()
    question.google_process()
    data = question.wiki_process()
    assert data['status'] == mock_data['status']