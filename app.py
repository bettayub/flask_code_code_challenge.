


#creating instance
app = Flask(__name__)


#creating database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emp.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'FALSE'

# Initialize SQLAlchemy with 'app' for database connection.
db = SQLAlchemy(app)


#Adding classe pizzas
class Pizzas(db.Model):
    id = db.Column(db.Integer,primary_key =True)
    name = db.Column(db.String(255),nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow())
                            
                
#Adding class Restaurants
class Restaurant_pizzas(db.Model):
    id = db.Column(db.Integer,primary_key =True)
    pizza_id = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    price = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow())
         

