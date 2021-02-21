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

@app.route('/get_dummy_users_ranked', methods= ['GET'])
def dummy_users_ranked():
    global dum1
    global dum2
    global dum3
    global dum4
    global dum5

    tuple_list = [(dum1.name, dum1.kg_carbon_footprint),
                  (dum2.name, dum2.kg_carbon_footprint),
                  (dum3.name, dum3.kg_carbon_footprint), 
                  (dum4.name, dum4.kg_carbon_footprint),
                  (dum5.name, dum5.kg_carbon_footprint),  
                  ]
    
    tuple_list.sort(key=lambda tup: tup[1])
    response = jsonify(tuple_list) 
    return response


@app.route('/get_dummy_user_emission',methods=['GET'])
def dummy_emission_breakdown():
    global dum1
    global dum2
    global dum3
    global dum4
    global dum5

    dum1 = {
                 "carbon_footprint": dum1.kg_carbon_footprint,
                 "house_emission": dum1.house_emissions,
                 "flight_emissions": dum1.flight_emissions,
                 "car_emissions": dum1.car_emissions,
                 "motorbike_emissions": dum1.motorbike_emissions,
                 "bus_emissions": dum1.bus_emissions,
                 "train_emissions": dum1.train_emissions,
                 "subway_emissions": dum1.subway_emissions,
                 "food_emissions": dum1.food_emissions,
                 "electricity_tips": dum1.electricity_tips,
                 "car_tips": dum1.car_tips,
                 "food_tips": dum1.food_tips
                 }

    dum2 = {
                 "carbon_footprint": dum2.kg_carbon_footprint,
                 "house_emission": dum2.house_emissions,
                 "flight_emissions": dum2.flight_emissions,
                 "car_emissions": dum2.car_emissions,
                 "motorbike_emissions": dum2.motorbike_emissions,
                 "bus_emissions": dum2.bus_emissions,
                 "train_emissions": dum2.train_emissions,
                 "subway_emissions": dum2.subway_emissions,
                 "food_emissions": dum2.food_emissions,
                 "electricity_tips": dum2.electricity_tips,
                 "car_tips": dum2.car_tips,
                 "food_tips": dum2.food_tips
                 }

    dum3 = {
                 "carbon_footprint": dum3.kg_carbon_footprint,
                 "house_emission": dum3.house_emissions,
                 "flight_emissions": dum3.flight_emissions,
                 "car_emissions": dum3.car_emissions,
                 "motorbike_emissions": dum3.motorbike_emissions,
                 "bus_emissions": dum3.bus_emissions,
                 "train_emissions": dum3.train_emissions,
                 "subway_emissions": dum3.subway_emissions,
                 "food_emissions": dum3.food_emissions,
                 "electricity_tips": dum3.electricity_tips,
                 "car_tips": dum3.car_tips,
                 "food_tips": dum3.food_tips
                 }

    dum4 = {
                 "carbon_footprint": dum4.kg_carbon_footprint,
                 "house_emission": dum4.house_emissions,
                 "flight_emissions": dum4.flight_emissions,
                 "car_emissions": dum4.car_emissions,
                 "motorbike_emissions": dum4.motorbike_emissions,
                 "bus_emissions": dum4.bus_emissions,
                 "train_emissions": dum4.train_emissions,
                 "subway_emissions": dum4.subway_emissions,
                 "food_emissions": dum4.food_emissions,
                 "electricity_tips": dum4.electricity_tips,
                 "car_tips": dum4.car_tips,
                 "food_tips": dum4.food_tips
                 }


    dum5 = {
                 "carbon_footprint": dum5.kg_carbon_footprint,
                 "house_emission": dum5.house_emissions,
                 "flight_emissions": dum5.flight_emissions,
                 "car_emissions": dum5.car_emissions,
                 "motorbike_emissions": dum5.motorbike_emissions,
                 "bus_emissions": dum5.bus_emissions,
                 "train_emissions": dum5.train_emissions,
                 "subway_emissions": dum5.subway_emissions,
                 "food_emissions": dum5.food_emissions,
                 "electricity_tips": dum5.electricity_tips,
                 "car_tips": dum5.car_tips,
                 "food_tips": dum5.food_tips
                 }

    dummy_data = {
                "dum1": dum1,
                "dum2": dum2,
                "dum3": dum3,
                "dum4": dum4,
                "dum5": dum5
    }

    response = jsonify(dummy_data)
    return response

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
    global dum1
    global dum2
    global dum3
    global dum4
    global dum5
    dum1 = create_dummy_data('jason', 'light_meat', True) 
    dum2 = create_dummy_data('walter', 'heavy_meat', False) 
    dum3 = create_dummy_data('nathan', 'vegan', True) 
    dum4 = create_dummy_data('kaler', 'pescatarian', False) 
    dum5 = create_dummy_data('tiffani', 'vegetarian', False) 
    dum1.print_footprint()
    dum2.print_footprint()
    dum3.print_footprint()
    dum4.print_footprint()
    dum5.print_footprint()

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




























