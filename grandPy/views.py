#! /usr/bin/env python
"""Module responsalble de l'affichage des templates
"""
import json
from flask import  Flask, request, render_template
from .processing import Processing
app = Flask(__name__)


@app.route('/')
def index():
    """main template
    """
    return render_template('hello.html')


@app.route('/process', methods=['POST', 'GET'])
def register():
    """main Template
    """
    if request.form:
        question_asked = request.form.get('text')
        question = Processing(question_asked)
        question.question_process()
        question.google_process()
        data = question.wiki_process()
        return json.dumps(data)
    return render_template('hello.html')

@app.errorhandler(404)
def page_not_found():
    """404 error Template
    """
    return render_template('404.html', title='404'), 404
