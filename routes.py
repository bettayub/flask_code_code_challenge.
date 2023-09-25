
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


@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        pizzas = []
        for restaurant_pizza in restaurant.restaurant_pizzas:
            pizzas = Pizza.query.get(restaurant_pizza.pizza_id)
            if pizzas:
                pizza_data = {
                    'id': pizzas.id,
                    'name': pizzas.name,
                    'ingredients': pizzas.ingredients
                }
                pizzas.append(pizza_data)
        restaurant_data = {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address,
            'pizzas': pizzas
        }
        return jsonify(restaurant_data)
    else:
        return jsonify({'error': 'Restaurant not found'}), 404


@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        # Delete associated RestaurantPizzas first
        RestaurantPizza.query.filter_by(restaurant_id=id).delete()
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    else:
        return jsonify({'error': 'Restaurant not found'}), 404



# model routes function for Pizzas 

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    pizza_list = []
    for pizza in pizzas:
        pizza_data = {
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        }
        pizza_list.append(pizza_data)
    return jsonify(pizza_list)

# model routes function for restaurants_Pizzas

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.json
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')
    price = data.get('price')

    if not pizza_id or not restaurant_id or not price:
        return jsonify({'errors': ['validation errors']}), 400

    # Check if the Pizza and Restaurant exist
    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    if not pizza or not restaurant:
        return jsonify({'errors': ['validation errors']}), 400

    # Create a new RestaurantPizza
    new_restaurant_pizza = RestaurantPizza(
        pizza_id=pizza_id,
        restaurant_id=restaurant_id,
        price=price
    )

    db.session.add(new_restaurant_pizza)
    db.session.commit()
    
    
    # Return the pizza details
    return jsonify({
        'id': pizza.id,
        'name': pizza.name,
        'ingredients': pizza.ingredients
    })
    
    
#starting  the Flask development server in debug mode
if __name__ == '__main__':
    app.run(debug=True)
