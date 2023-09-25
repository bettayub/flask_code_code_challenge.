# from flask import Flask, request, jsonify, make_response  #web application functionality.
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
# from sqlalchemy import CheckConstraint



# #creating instance
# app = Flask(__name__)


# #creating database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myrestaurant.db'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'FALSE'

# #mapping
# # db = SQLAlchemy(app)

# #Adding classes
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

# db = SQLAlchemy()

# class Restaurant(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False, unique=True)
#     address = db.Column(db.String(70), nullable=False)
#     restaurant_pizzas = db.relationship('RestaurantPizza', backref='restaurant', lazy=True)

# class Pizza(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False)
#     ingredients = db.Column(db.String(200), nullable=False)
#     restaurant_pizzas = db.relationship('RestaurantPizza', backref='pizza', lazy=True)
    
    
# class RestaurantPizza(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
#     restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
#     price = db.Column(db.Float, nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow())
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow())

#     # Adding a CheckConstraint for the price range
#     __table_args__ = (
#         db.CheckConstraint('price >= 1 AND price <= 30', name='check_price_range'),
#     )

# with app.app_context():
#     db.create_all()


from flask import Flask
from models import db
from routes import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myrestaurant.db'

# Initialize SQLAlchemy with the Flask app
db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
