from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

class WordForm(FlaskForm):
    word = StringField(
        'Word',
        validators = [DataRequired()]
    )

    submit = SubmitField('Search')