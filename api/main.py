import requests
from flask import Flask, jsonify, make_response, request
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import cross_origin
from datetime import datetime

app = Flask(__name__)
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blogapi.sqlite3"
app.config["TRACK_MODIFICATIONS"] = False

db = SQLAlchemy()
db.init_app(app)

# create db models
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(35), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)

# create all db models
with app.app_context():
    db.create_all()

# allows cross domain with Angular
@app.after_request

def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response

# put arguments (to create blog)
create_user_put_args = reqparse.RequestParser()
create_user_put_args.add_argument("user", type=str, help="A username is required.", required=True)
create_user_put_args.add_argument("password", type=str, help="A password is required.", required=True)
create_user_put_args.add_argument("email", type=str, help="An email is required.", required=True)

def validate_email(email: str) -> bool:
    response = db.session.query(
        db.session.query(Users).filter_by(email=email).exists()
    ).scalar()
    return response

class HelloWorld(Resource):
    def get(self):
        response = jsonify({"note": "Hello World"})

        # create headers
        response.headers["Custom-Header"] = "Hello World resource"

        return response

class CreateUser(Resource):
    def put(self):
        data = request.get_json()
        print(data)
        new_user = Users(
            username=data.get("user").get("user"),
            password=data.get("user").get("password"),
            email=data.get("user").get("email")
        )
        db.session.add(new_user)
        db.session.commit()
        # create json response 
        response = {
            "id": new_user.id,
            "username": new_user.username,
            "password": new_user.password
        }
        response = jsonify(response)
        response.headers["Custom-Header"] = f"A new user has been created - {data.get('user')}:{data.get('email')}"
        return make_response(response, 201)

class GetUserByEmail(Resource):
    def get(self, user_email):
        # check if email is in db
        validated_email = validate_email(user_email)
        if validated_email is False:
            abort(404, message="Email not found.")
        find_blog = db.session.query(Users).filter_by(email=user_email).first()
        # create json response
        response = {
            "status": 302,
            "id": find_blog.id,
            "username": find_blog.username,
            "email": find_blog.email,
        }
        response = jsonify(response)
        response.headers["Custom-Header"] = f"User {find_blog.username} found."
        return make_response(response, 302)

api.add_resource(HelloWorld, "/helloworld")
api.add_resource(CreateUser, "/new/user")
api.add_resource(GetUserByEmail, "/user/<string:user_email>")

if __name__ == "__main__":
    app.run(debug=True, port=5000)