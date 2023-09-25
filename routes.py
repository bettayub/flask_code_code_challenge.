
from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Restaurant, Pizza, RestaurantPizza
from app import app

# Setting the SQLAlchemy database Uniform Resource Identifier
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emp.db'
db = SQLAlchemy(app)