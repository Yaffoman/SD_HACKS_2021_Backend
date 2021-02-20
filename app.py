import pyrebase
from flask import *
import sys
import random
app = Flask(__name__)

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

@app.route("/login_success")
def login_redirected():
    return "You are now logged in"

@app.route("/signup_success")
def signup_redirected():
    return "Successfully signed up"


@app.route('/', methods=['GET', 'POST'])
def login():
    unsuccessful = 'Please check your credentials'
    successful = 'Login successful'
    print(request.method)
    if request.method == 'POST':
        email = request.form['name']
        password = request.form['pass']
        try:
            auth.sign_in_with_email_and_password(email, password)
            #return render_template('new.html', s=successful)
            return redirect('/login_success')
            print("redirecting now")
        except:
            return render_template('new.html', us=unsuccessful)

    return render_template('new.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    email = 'test_email{}@gmail.com'.format(random.randrange(0,100))
    password = 'somepassword12345' 
    print("email: ",email, file=sys.stderr)
    auth.create_user_with_email_and_password(email, password)
    return redirect('/signup_success')


if __name__ == '__main__':
    app.run()




























