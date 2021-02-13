from flask import Flask, request, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

from models import db, connect_db, Pet
from forms import AddPetForm


app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)


with app.app_context():
    
    db.create_all()

@app.route("/home")
def home():
    pets = Pet.query.all()
    return render_template("home.html",pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """ Renders add pet form """
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        add_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(add_pet)
        db.session.commit()
        return redirect('/home')
    else:
        return render_template('add_pet.html', form=form)

@app.route('/edit/<int:id>', methods=["GET", "POST"])
def edit_pet(id):
    pet = Pet.query.get_or_404(id)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/home')
    else:
        return render_template("edit_pet.html", form=form)
            