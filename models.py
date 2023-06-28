# coding: utf-8
from . import db
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from enum import Enum


class UserType(Enum):
    NONE = 0
    ADMIN = 1
    CUSTOM = 2


class User(UserMixin, db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(36), nullable=False)
    lastname = db.Column(db.String(36), nullable=True)
    name = db.Column(db.String(36), nullable=False)
    pwd = db.Column(db.String(88), nullable=False)
    age = db.Column(db.Integer)
    email = db.Column(db.String(36))
    gender = db.Column(db.Integer, server_default=db.FetchedValue())
    auth = db.Column(db.Integer)

    @property
    def user_type(self):
        if self.auth == 0:
            return UserType.CUSTOM
        elif self.auth == 1:
            return UserType.ADMIN


class Feedback(db.Model):
    __tablename__ = "feedback"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    email = db.Column(db.String(36), nullable=False)
    comment = db.Column(db.String(500), nullable=False)
