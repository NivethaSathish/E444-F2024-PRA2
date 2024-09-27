'''from flask import Flask

app = Flask(__name__)

@app.route('/') 

def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>') 

def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)'''

from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your UofT email address?', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():

        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data

        old_email = session.get('email')
        if old_email is not None and old_email != form.email.data:
            flash('Looks like you have changed your email!')
        session['email'] = form.email.data

        # Check if the email contains '@'
        if "@" not in session['email']:
            flash('Please include an @ in the email address. ' + session['email'] + " is missing an @.")
            session['missing_at'] = True
            session['uoft_email'] = None
        else:
            session['missing_at'] = False
            # If the email contains '@', check if it's a UofT email
            if session['email'].endswith("utoronto.ca"):
                session['uoft_email'] = session['email']
            else:
                session['uoft_email'] = None  # Not a UofT email

        '''if "@" in session['email'] and "utoronto" in session['email']:
            session['uoft_email'] = form.email.data
            session['missing_at'] = False
        elif "@" in session['email']:
            session['missing_at'] = True
            session['uoft_email'] = None
        else:
            flash('Please include an @ in the email address. ' + session['email'] + " is missing an @.")
            session['uoft_email'] = None
            session['missing_at'] = False'''

        return redirect(url_for('index'))

    return render_template('index.html', form=form, name=session.get('name'), uoft_email=session.get('uoft_email'), missing_at=session.get('missing_at'), current_time=datetime.utcnow())

'''@app.route('/') 
def index():
    return render_template('index.html', current_time=datetime.utcnow())'''

@app.route('/user/<name>') 

def user(name):
    return render_template('user.html', name=name, current_time=datetime.utcnow())




