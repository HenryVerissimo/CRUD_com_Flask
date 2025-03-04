from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active


config = app_config[app_active]
db = SQLAlchemy()



class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    last_update = db.Column(db.DateTime, onupdate=db.func.now(), nullable=True)
    recovery_code = db.Column(db.String(200), nullable=True)
    active = db.Column(db.Boolean(), default=True, nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id), nullable=False)
    role = db.relationship("Role", back_populates="users")

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.Text(), nullable=False)
    quantity = db.Column(db.Integer, nullable=True, default=0)
    image = db.Column(db.Text(), nullable=True)
    price =db.Column(db.Numeric(10,2), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    last_update = db.Column(db.DateTime, onupdate=db.func.now(), nullable=True)
    status = db.Column(db.Integer, default=1, nullable=True)
    user = db.relationship("User", back_populates="role")


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.Text(), nullable=True)
