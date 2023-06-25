import os
from blog_api import app, api
import requests
from flask import Flask, jsonify, make_response, request, session
from blog_api.extension import init_db, SessionLocal
from blog_api.api.public.helloworld import HelloWorld
from dotenv import load_dotenv

load_dotenv()

# config your db
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["BLOG_DB"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initialise db models
with app.app_context():
    init_db()

# allow cross domain with Angular FE
@app.after_request

def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response

# add api resource here

api.add_resource(HelloWorld, "/helloworld")

if __name__ == "__main__":
    app.run(debug=True, port=os.environ["BLOG_PORT"])