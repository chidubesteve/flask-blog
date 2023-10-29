from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SECRET_KEY'] = '451687de6cb7eb0d41af6d8f005decd0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///side.db'
db = SQLAlchemy(app)

# this is necessary so as to help the app know where to navigate to
from flaskblog import routes