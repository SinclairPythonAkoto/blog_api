from typing import Dict, List
from flask import jsonify, make_response
from flask_restful import Resource


class HelloWorld(Resource):
    def get(self) -> List[Dict]:
        response: jsonify = jsonify({"note": "hello world"})
        # create header
        response.headers["Custom-Header"] = "Hello World Resource"
        return make_response(response, 200)
