from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config.config import load_config

app = Flask(__name__)

config = load_config("production")

app.config["JWT_SECRET_KEY"] = config.JWT_SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config["ENV"] = config.ENV

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
CORS(app)


from routes.routes import *

if __name__ == "__main__":
    app.config.from_object(config)
    app.run(port=3000)

