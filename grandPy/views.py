#! /usr/bin/env python
from flask import  Flask,  request, jsonify, render_template
from .processing import Processing
import json
app = Flask(__name__)
app.config.from_object('config')
app.config['SECRET_KEY'] = 'bc5eedbdc41a5742e6ee2c0a8f34376f'

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/process', methods=['POST', 'GET'])
def register():
    print(request.form)
    if request.form:
        question = request.form.get('text')
        question = Processing(question)
        question.question_process()
        question.google_process()
        data = question.wiki_process()

        

        return json.dumps(data)
    else:
        return ''
    # traiter les donnees recues
        # affiicher : "Bonjour mon enfant"
