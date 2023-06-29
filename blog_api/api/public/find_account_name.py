from typing import Dict
from flask import jsonify, make_response, request
from flask_restful import Resource
from blog_api.extension import db_session
from blog_api.utils.error_messages.users import abort
from blog_api.utils.tools import validate_user
from blog_api.utils.error_messages.users import abort


class FindAccountName(Resource):
    def get(self, user: str):
        session: db_session = db_session
        abort.abort_if_username_not_found_404(session, user)
        find_user: validate_user = validate_user.get_username(session, user)
        response: Dict = {
            "Account found": {
                "id": find_user.id,
                "username": find_user.username,
                "email": find_user.email,
            },
            "status": 200,
        }
        response: jsonify = jsonify(response)
        response.headers["Custom-Header"] = f"Account found: {find_user.username}"
        return make_response(response, 200)