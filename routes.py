
from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Restaurant, Pizza, RestaurantPizza
from app import app

# Setting the SQLAlchemy database Uniform Resource Identifier
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emp.db'
db = SQLAlchemy(app)


# model routes function for Restaurants 

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurant_list = []
    for restaurant in restaurants:
        restaurant_data = {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address
        }
        restaurant_list.append(restaurant_data)
    return jsonify(restaurant_list)
