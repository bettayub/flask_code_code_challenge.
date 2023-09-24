


#creating instance
app = Flask(__name__)


#creating database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emp.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'FALSE'
