from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import os


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__.split('.')[0])
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/survey/<int:survey_id>/')
def show_survey(survey_id):
    return 'Hello World!'


@app.route('/login/oauth/')
def login_oauth():
    return 'Hello World!'


@app.route('/login/local/')
def login_local():
    return 'Hello World!'
