import pyrebase
from flask import *
import sys
import random
from random import randrange
from flask_cors import CORS
from calculate_carbon import Person, smart_tips
app = Flask(__name__)
cors = CORS(app)

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



#{'firstName': 'Jesse', 'lastName': 'Pinkman', 'username': 'bitch', 'email': 'jessemethdealer@gmail.com', 'password': 'bitchbitchbitch', 
# 'confirmPassword': 'bitchbitchbitch', 'flights_per_year': '2', 'Car': '1110', 'carpool': True, 'diet': 'medium_meat',
# 'occupants': 0, 'electricity': 0, 'naturalGas': 0, 'fuelOil': 0, 'propane': 0}

def create_dummy_data(first_name: str, diet:str, carpool:bool):
    dummy_user = Person(first_name, diet)
    dummy_user.add_house(randrange(0,5), randrange(90, 200))
    dummy_user.add_flight(randrange(1,4))
    dummy_user.add_car(randrange(500,1500),carpool) 
    dummy_user.add_motorbike(randrange(1,600))
    dummy_user.add_food(randrange(300,700))
    dummy_user.add_subway(randrange(50,500))
    dummy_user.add_bus(randrange(0,300))
    dummy_user.add_train(randrange(0,2000))
    return dummy_user

def create_user(data):
    print("inside create_user")
    print(data)
    user = Person (data["firstName"],data["diet"])
    user.add_house(int(data["occupants"]), int(data["electricity"]))
    user.add_flight(int(data["flights_per_year"]))
    user.add_car(int(data["Car"]), data["carpool"])
    user.add_food(int(data["monthly_food_spending"]))
    user.print_report()
    user.print_footprint()
    user.print_tips()
    smart_tips(user)
    return user

@app.route('/get_dummy_user_emission',methods=['GET'])
def dummy_emission_breakdown():
    pass


@app.route('/user_emission',methods=['GET'])
def emission_breakdown():
    global user
    user_data = {
                 "carbon_footprint": user.kg_carbon_footprint,
                 "house_emission": user.house_emissions,
                 "flight_emissions": user.flight_emissions,
                 "car_emissions": user.car_emissions,
                 "motorbike_emissions": user.motorbike_emissions,
                 "bus_emissions": user.bus_emissions,
                 "train_emissions": user.train_emissions,
                 "subway_emissions": user.subway_emissions,
                 "food_emissions": user.food_emissions,
                 "electricity_tips": user.electricity_tips,
                 "car_tips": user.car_tips,
                 "food_tips": user.food_tips
                        }
    response = jsonify(user_data)
    return response

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        request_data = request.get_json()
        print(request_data)
        email = request_data["email"]
        password = request_data["password"]
        try:
            auth.sign_in_with_email_and_password(email, password)
        except:
            print("firebase login failed")
    response = jsonify(message="Success")
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

@app.route('/signup', methods=['GET', 'POST'])
#@flask_cors.cross_origin(origins="**")
def signup():
    global user
    dum = create_dummy_data('jason', 'light_meat', True) 
    dum1 = create_dummy_data('walter', 'heavy_meat', False) 
    dum2 = create_dummy_data('nathan', 'vegan', True) 
    dum3 = create_dummy_data('kaler', 'pescatarian', False) 
    dum4 = create_dummy_data('tiffani', 'vegetarian', False) 
    dum.print_footprint()
    dum1.print_footprint()
    dum2.print_footprint()
    dum3.print_footprint()
    dum4.print_footprint()

    print(request.method)
    if request.method == 'POST':
        request_data = request.get_json()
        print(request_data)
        email = request_data["email"]
        password = request_data["password"]
        try:
            auth.create_user_with_email_and_password(email, password)
        except:
            print("firebase signup failed")
    user = create_user(request_data)
    response = jsonify(message="Success")
    response.headers.add("Access-Control-Allow-Origin","*")
    return response
if __name__ == '__main__':
    app.run()




























