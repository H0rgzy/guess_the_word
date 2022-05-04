from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'A_Top_Secret_Key_For_Me'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)