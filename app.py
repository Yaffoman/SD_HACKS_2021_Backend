# flask and other web required frameworks
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from random import randint

app = Flask(__name__)
CORS(app)
# # #
# # # # ROUTES
# # # # # # # # #

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/login")
def login_user():
    return "Under development"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
