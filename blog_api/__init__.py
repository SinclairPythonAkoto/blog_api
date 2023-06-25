import os
from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv

load_dotenv()

def create_app() -> Flask:
    app: Flask = Flask(__name__)
    # add app configurations here
    return app

app: Flask = create_app()

api: Api = Api(app)