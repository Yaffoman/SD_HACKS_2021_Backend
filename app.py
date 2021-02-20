# flask and other web required frameworks
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json
from random import randint
import pyrebase

config = {
    "apiKey": "AIzaSyAn8HjyDpn4dZW5-kPQh9DfqiHeTTt7rE4",
    "authDomain": "carbon-tracker-60db3.firebaseapp.com",
    "databaseURL": "https://carbon-tracker-60db3.firebaseio.com",
    "projectId": "carbon-tracker-60db3",
    "storageBucket": "carbon-tracker-60db3.appspot.com",
    "messagingSenderId": "550886715542",
    "appId": "1:550886715542:web:938237ae0c85ffbf3a52b7",
    "measurementId": "G-NCVPXEC72N"
};

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()



app = Flask(__name__)
CORS(app)
# # #
# # # # ROUTES
# # # # # # # # #

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/login", methods=['GET', 'POST'])
def login():
	unsuccessful = 'Please check your credentials'
	successful = 'Login successful'
	if request.method == 'POST':
		email = request.form['name']
		password = request.form['pass']
		try:
			auth.sign_in_with_email_and_password(email, password)
			return render_template('login.html', s=successful)
		except:
			return render_template('login.html', us=unsuccessful)

	return render_template('login.html')

@app.route("/signup")
def signup():
    return "Under development"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
