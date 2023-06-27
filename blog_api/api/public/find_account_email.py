from typing import Dict
from flask import jsonify, make_response
from flask_restful import Resource
from blog_api.extension import db_session
from blog_api.utils.tools import validate_user
from blog_api.utils.error_messages.users import abort


class GetAccountByEmail(Resource):
    def get(self, user_email):
        session: db_session = db_session
        abort.abort_if_no_username_404(session, user_email)
        find_email = validate_user.get_email(session, user_email)
        response = {
            "Account found": {
                "id": find_email.id,
                "username": find_email.username,
                "email": find_email.email,
            },
            "status": 302,
        }
        response = jsonify(response)
        response.headers["Custom-Headers"] = f"Account found: {find_email.username}"
        return make_response(response, 302)
