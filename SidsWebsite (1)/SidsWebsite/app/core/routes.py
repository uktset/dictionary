from flask import Blueprint, render_template, request, flash
from .forms import WordForm
from typing import List
import requests

blueprint = Blueprint('core', __name__, template_folder = 'templates')


@blueprint.route('/', methods = ['GET', 'POST'])
def index():
    form = WordForm(request.form)

    if form.validate_on_submit():
        data = lookup_word(form.data.get('word'))

        if data:
            return render_template('index.html', data = data, form = form)

    return render_template('index.html', form = form)


@blueprint.route('/test')
def test():
    word = 'WORLD'

    return f'<h1>HELLO {word}</h1>'


def lookup_word(word: str) -> dict:
    r = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/hi/{word}')
    
    if r.status_code == 200:
        data = r.json()
        return data
    else:
        flash('An error occurred')