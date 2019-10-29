# Modul for test views 
from grandPy import app
from grandPy.processing import Processing
import requests

def test_if_views_return_response():
    ''' tester si la question est un format valide'''
    adresse = {'adresse': '7 Cité Paradis, 75010 Paris, France'}
    nom = {'nom': 'OpenClassrooms'}
    text = {'texte': 'La cité Paradis est une voie publique située dans le 10e arrondissement de Paris.\n\n\n== Situation et accès ==\nLa cité Paradis est une voie publique située dans le 10e arrondissement de Paris.'}
    
    question_asked = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    question = Processing(question_asked)
    question.question_process()
    question.google_process()
    data = question.wiki_process()
    assert data['adresse'] == adresse['adresse']
    assert data['nom'] == nom['nom']
    assert data['texte'] == text['texte']

def test_register(app):
    url = '/'
    resp = app.post(url)
    assert resp.status_code == 200 
