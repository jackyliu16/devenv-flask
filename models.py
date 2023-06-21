# coding: utf-8
from . import db
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from enum import Enum


class UserType(Enum):
    NONE = 0
    ADMIN = 1
    CUSTOM = 2


class User:
    user_type = UserType.NONE


class Admin(User, UserMixin, db.Model):
    __tablename__ = "admin"
    user_type = UserType.ADMIN

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(36), nullable=False)
    pwd = db.Column(db.String(88), nullable=False)
    email = db.Column(db.String(36), nullable=False, unique=True)


class Customer(User, UserMixin, db.Model):
    __tablename__ = "customer"
    user_type = UserType.CUSTOM

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(36), nullable=False)
    lastname = db.Column(db.String(36), nullable=True)
    name = db.Column(db.String(36), nullable=False)
    pwd = db.Column(db.String(88), nullable=False)
    age = db.Column(db.Integer)
    email = db.Column(db.String(36))
    gender = db.Column(db.Integer, server_default=db.FetchedValue())
