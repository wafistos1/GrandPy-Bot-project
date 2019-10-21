# Modul for test views
from grandPy.processing import Processing
import json
import urllib.request
from io import BytesIO
from _pytest.monkeypatch import monkeypatch

def test_if_views_return_response():
    ''' tester si la question est un format valide'''
    # mock la question
    mock_data = {'adresse': '7 Cité Paradis, 75010 Paris, France'}
    question_asked = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    question = Processing(question_asked)
    question.question_process()
    question.google_process()
    data = question.wiki_process()
    assert data['adresse'] == mock_data['adresse']