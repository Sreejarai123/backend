import requests
import json
from flask import Blueprint, jsonify
from flask_restful import Api, Resource # used for REST API building
from flask import Flask, request
import flask
import json
from flask_cors import CORS

app = Flask(__name__)

brawl_api = Blueprint('brawl_api', __name__)
api = Api(brawl_api)

class BrawlAPI:
    class _Brawl(Resource):
        def post(self): 
            body = request.get_json()
            tag = body.get("tag")
            url = f"https://api.brawlstars.com/v1/players/%23{tag}"
            api_token = ""

            headers = {
                "Accept": "application/json",
                "Authorization": f"Bearer {api_token}"
            }

            response = requests.get(url, headers=headers)

            return json.dumps(response.json())
        def get(self):
            message = "GET METHOD"
            return message
    api.add_resource(_Brawl, '/api/brawl')