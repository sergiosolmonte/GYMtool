from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64),nullable=True)
    lastname = db.Column(db.String(64),nullable=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    birthdate = db.Column(db.DateTime, nullable=True)
    height = db.Column(db.Integer, nullable=True)
    weight = db.Column(db.Float, nullable=True)
    neck = db.Column(db.Integer, nullable=True)
    waist = db.Column(db.Integer, nullable=True)


    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class UserInterest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    interest_id = db.Column(db.Integer, db.ForeignKey('interest.id'))


class Interest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)


class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    train = db.relationship('Training', backref='exercise', lazy=True)
    description = db.Column(db.Text,nullable=True)
    category = db.Column(db.Integer, db.ForeignKey('category.id'))


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)


class Training(db.Model):
    id = db.Column(db.Integer, primary_key=True)  #Sostituire con tupla
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'))
    program_id = db.Column(db.Integer, db.ForeignKey('program.id'))
    set = db.Column(db.Integer)
    reps = db.Column(db.String)
    time = db.Column(db.String)
    day = db.Column(db.Integer)
    exNum = db.Column(db.Integer)  #Numero dell'esercizio nel giorno


class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(64), nullable=True)
    share = db.Column(db.Boolean)
    train = db.relationship('Training', backref='program', lazy=True)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

