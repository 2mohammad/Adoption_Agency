from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import InputRequired, Email, Optional


class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[
        InputRequired(message="Pet Name can't be blank")
    ])
    species = StringField("Species", validators=[
        InputRequired(message="Species Field can't be blank")
    ])
    photo_url = StringField("Photo Url")
    age = IntegerField("Age")
    notes = TextAreaField("Notes")
    available = BooleanField("Avialable")

