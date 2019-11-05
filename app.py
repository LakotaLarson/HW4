from flask import Flask
from flask import render_template, redirect, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app=Flask(__name__)
app.config['SECRET_KEY']='SecretKey'

class larson_dogs(db.Model):
    dogId = db.Column(db.Integer, primary_key=True)
    dogName = db.Column(db.String(255))
    age = db.Column(db.Integer)
    sex =db.Column(db.String(1))
    breed =db.Column(db.String(255))

def __repr__(self):
    return "ID: {0} | Name: {1} | Age: {2} | Sex:{3} | Breed:{4}".format(self.Dogid, self.dogName, self.age, self.sex, self.breed)


class DogForm(FlaskForm):
    dogName = StringField('First Name:', validators=[DataRequired()])
    age = StringField('Age:', validators=[DataRequired()])
    sex = StringField('Sex:', validators=[DataRequired()])
    breed = StringField('Breed:', validators=[DataRequired()])

@app.route('/')
def index():
    return render_template(index.html, pageTitle='Lakota\'s Dogs')

@app.route('/add_dog', methods=['GET', 'POST'])
def add_dog():
    form = DogForm()
    if form.validate_on_submit():
        return "<h2> My dog's name is {0}".format(form.dogName)
    return render_template('add_dog.html', form=form, pageTitle='Add A New Dog')


if __name__ =='__main__':
    app.run(debug=True)
