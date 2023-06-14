# coding: utf-8
from . import db
from flask_sqlalchemy import SQLAlchemy

class Admin(db.Model):
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(36), nullable=False)
    pwd = db.Column(db.String(36), nullable=False)
    email = db.Column(db.String(36))

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(36), nullable=False)
    pwd = db.Column(db.String(36), nullable=False)
    age = db.Column(db.Integer)
    email = db.Column(db.String(36))
    gender = db.Column(db.Integer, server_default=db.FetchedValue())
