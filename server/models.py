# from flask.ext.login import UserMixin, AnonymousUserMixin
from server import db
from werkzeug.security import generate_password_hash, check_password_hash
# from datetime import datetime


class UserAccount(db.Model):
    __tablename__ = 'user_accounts'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Survey(db.Model):
    __tablename__ = 'surveys'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)


class QuestionType(db.Model):
    __tablename__ = 'question_types'
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(80), unique=True)


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80), unique=True)


class Answer(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80), unique=True)
    question = db.relationship('Question',
                               backref=db.backref('posts', lazy='dynamic'))

class Response(db.Model):
    __tablename__ = 'responses'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80), unique=True)
    user = db.relationship('UserAccount',
                           backref=db.backref('posts', lazy='dynamic'))
    answer = db.relationship('Answer',
                             backref=db.backref('posts', lazy='dynamic'))