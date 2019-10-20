#! /usr/bin/env python
# Module responsalble de l'affichage des templates
from flask import  Flask,  request,  render_template
from .processing import Processing
import json
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('hello.html')


@app.route('/process', methods=['POST', 'GET'])
def register():
    print(request.form)
    if request.form:
        question_asked = request.form.get('text')
        question = Processing(question_asked)
        question.question_process()
        question.google_process()
        data = question.wiki_process()
        print(data['texte'])
        return json.dumps(data)
    else:
        return ''

