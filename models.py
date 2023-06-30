# coding: utf-8
from . import db
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import LONGTEXT, TINYINT

from .lib import UserType


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
    auth = db.Column(db.Integer, nullable=False)

    @property
    def user_type(self):
        if self.auth == 0:
            return UserType.CUSTOM
        elif self.auth == 1:
            return UserType.ADMIN


class ProductDetail(db.Model):
    __tablename__ = "product_detail"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(36), nullable=False)
    intro = db.Column(db.Text, nullable=False)
    content = db.Column(LONGTEXT, nullable=True)
    price = db.Column(db.String(36), nullable=False)
    mask = db.Column(db.SmallInteger, nullable=True)


class Feedback(db.Model):
    __tablename__ = "feedback"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    email = db.Column(db.String(36), nullable=False)
    comment = db.Column(db.String(500), nullable=False)


class Bill(db.Model):
    __tablename__ = "bill"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    fname = db.Column(db.String(36), nullable=False)
    lname = db.Column(db.String(36), nullable=False)
    cname = db.Column(db.String(36), nullable=False)

    zipcode = db.Column(db.String(8), nullable=False)
    email = db.Column(db.String(36), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    city = db.Column(db.String(36), nullable=False)
    address = db.Column(db.String(36), nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    pay_method = db.Column(db.String(8), nullable=False)
    unit = db.Column(TINYINT, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    start_time = db.Column()
