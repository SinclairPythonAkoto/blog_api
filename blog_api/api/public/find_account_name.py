from typing import Dict
from flask import jsonify, make_response, request
from flask_restful import Resource
from blog_api.extension import db_session
from blog_api.utils.error_messages.users import abort
from blog_api.utils.tools import validate_user
from blog_api.utils.error_messages.users import abort


class FindAccountName(Resource):
    def get(self, account):
        
        pass