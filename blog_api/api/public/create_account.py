from typing import Dict, List
from flask import jsonify, make_response, request
from flask_restful import Resource
from blog_api.extension import db_session
from blog_api.utils.tools import validate_user
from blog_api.utils.api_arguments import create_account_put
from blog_api.utils.tools.create_new_account import create_account

class CreateNewAccount(Resource):
    def put(self):
        data = request.get_json()
        username: data = data["user"]["user"]
        email: data = data["user"]["email"]
        user_password: data = data["user"]["password"]
        session = db_session()

        find_user: validate_user = validate_user.get_username(session, username)
        find_email: validate_user = validate_user.get_email(session, email)
        # validate if username already exists, if so abort
        validate_user.abort_if_username_already_exists_409(session, username)
        # validate if email already exists, if so abort
        validate_user.abort_if_email_already_exists_409(session, email)
        # create a new user account
        if not find_user and not find_email:
            create_new_account = create_account(
                session=session,
                username=username,
                email=email,
                password=user_password
            )
            # create response 
            response: Dict = {
                "New account created": {
                    "id": create_new_account.id,
                    "username": create_new_account.username,
                    "email": create_new_account.email,
                    "password": create_new_account.password
                },
                "status": 201,
            }
            response = jsonify(response)
            response.headers["Custom-Header"] = f"New user created: {create_new_account.username}"
            return make_response(response, 201)