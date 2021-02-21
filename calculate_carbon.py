#calculate_carbon.py

"""
IMPORTANT ASSUMPTION: every measurement is monthly 
0) House electricity
1) Transport mode: car, bus, train, carpool, motorbike, bicycle, e-scooter, walk
2) journey time 
3) Major flights  
    3.1) 1-2 per year (low) 
    3.2) 3-6 per year (moderate) 
    3.3) 1 flight per month (high)
4) Cruise
    4.1) 1 cruise a year
    4.2) 2 or more cruise a year
5) bus
6) train
7) Food types: 
Useful link: https://www.carbonfootprint.com/calculator.aspx 
"""

electricity_rate = 13 #cents/kWh
total_carbon_kgs = 0

# "heavy_meat"  = $100 spent/month = 730kgCO2/month 
#               = $1   spent/month = 7.3kgCO2/month

# "medium_meat" = $100 spent/month = 570kgCO2/month
#               = $1   spent/month = 5.3kgCO2/month

# "low_meat"    = $100 spent/month = 470kgCO2/month
#               = $1   spent/month = 4.7kgCO2/month

# "pescatarian" = $100 spent/month = 400kgCO2/month
#               = $1   spent/month = 4.0kgCO2/month

# "vegetarian"  = $100 spent/month = 390kgCO2/month
#               = $1   spent/month = 3.9kgCO2/month

# "vegan"       = $100 spent/month = 290kgCO2/month
#               = $1   spent/month = 2.9kgCO2/month 

class Person:
    def __init__(self, name:str, food_choice:str): 
        self.name = name
        self.kg_carbon_footprint = 0
        #household
        self.kWh_factor = 0.4532 
        self.food_choice = food_choice
        self.food_dict= {
                            "heavy_meat"  : 7.3,
                            "medium_meat" : 5.3,
                            "low_meat"    : 4.7,
                            "pescatarian" : 4.0,
                            "vegetarian"  : 3.9,
                            "vegan"       : 2.9
                        }
        self.house_emissions = 0
        self.flight_emissions = 0
        self.car_emissions = 0
        self.motorbike_emissions = 0
        self.bus_emissions = 0
        self.train_emissions = 0
        self.subway_emissions = 0
        self.food_emissions = 0

    def add_house(self, occupants: int, electricity_bill: float): #electricity bill is in dollars
        kWh_used = electricity_bill/0.13  #reasoning: avg cost of 1 kWh in america = 12.87 cents
        self.house_emissions +=  (kWh_used * self.kWh_factor) / occupants
        self.kg_carbon_footprint += (kWh_used * self.kWh_factor) / occupants

    def add_flight(self, num_of_round_trips:int):
        self.flight_emissions += num_of_round_trips * 1000 #assumption: 13 hour of flight time 
        self.kg_carbon_footprint += num_of_round_trips * 1000 
        
    def add_car(self, miles:int, carpool: bool):
        #avg passenger vehicle emits 423g of CO2/mile
        #avg passenger vehicle does 21 miles per gallon
        CO2_permile = 0.423 #kg 
        if carpool: CO2_permile /= 2 
        self.car_emissions += miles * CO2_permile 
        self.kg_carbon_footprint += miles * CO2_permile 

    def add_motorbike(self, miles:int):
        km_driven = miles * 1.6
        CO2_permile = 0.077
        self.motorbike_emissions += km_driven * CO2_permile 
        self.kg_carbon_footprint += km_driven * CO2_permile 

    def add_bus(self, miles: int): 
        km_dirven = miles * 1.6
        CO2_permile = 0.053 #kg
        self.bus_emissions += miles * CO2_permile
        self.kg_carbon_footprint += miles * CO2_permile

    def add_train(self, miles: int):
        CO2_permile = 0.148
        self.train_emissions += miles * CO2_permile
        self.kg_carbon_footprint += miles * CO2_permile

    def add_subway(self, miles: int): 
        CO2_permile = 0.099
        self.subway_emissions += miles * CO2_permile
        self.kg_carbon_footprint += miles * CO2_permile

    def add_food(self, monthly_money_spent: int):
        self.food_emissions += self.food_dict[self.food_choice] * monthly_money_spent
        self.kg_carbon_footprint += self.food_dict[self.food_choice] * monthly_money_spent 

    def print_footprint(self):
        print("carbon footprint:", '%.2f'%self.kg_carbon_footprint, "kgCO2 emission/month")
    def print_report(self):
        print("house emissions: ", self.house_emissions, "\nflight emissions: ",self.flight_emissions, 
        "\ncar emissions: ", self.car_emissions, "\nmotorbike emissions: ", self.motorbike_emissions,
        "\nbus emissions: ", self.bus_emissions, "\ntrain emissions: ", self.train_emissions,
        "\nsubway emissions: ", self.subway_emissions, "\nfood emissions: ", self.food_emissions)

def smart_tips(person: Person):
    #global electricity_tips
    electricity_tips = []
    car_tips = []
    food_tips = []

    if person.house_emissions > 400: 
        more_than_avg = person.house_emissions - 400
        percentage_above_avg = (more_than_avg / 400)*100
        electricity_tips.append("You are generating {}% more CO2 than an average household".format(round(percentage_above_avg,2)))
        electricity_tips.append("Unplug unused electronics: Standby power can account for 10% of an average household's annual electricity use")  
        electricity_tips.append("Use natural light: A single south-facing window can illuminate 20 to 100 times its area. Turning off one 60-watt bulb for four hours a day is a $9 saving over a year.") 
        electricity_tips.append("Manage your thermostat: If you have electric heat, lower your thermostat by two degrees to save 5% on your heating bill. Lowering it five degrees could save 10%.")
        electricity_tips.append("Be strategic with window coverings: Promote airflow through your home and block the afternoon sun. You could save you up to $10 (2 fans) or $45 (1 window unit AC) during the summer.")
    if person.car_emissions > 383: 
        more_than_avg = person.car_emissions - 383
        percentage_above_avg = (more_than_avg/383) * 100
        car_tips.append("You are generating {}% more CO2 than an average emissions of a typical passenger vehicle".format(round(percentage_above_avg,2)))
        car_tips.append("Drive less: Walk or bike when you can, take public transit when possible, use ride-sharing services, or work from home periodically if your job allows it.")
        car_tips.append("Drive effciently: Go easy on the gas pedal and brakes")
        car_tips.append("Maintain your car: Get regular tune-ups, check tyre pressure frequently, follow the manufacturer’s maintenance schedule, and use the recommended motor oil.")
        print("car_tips: ", car_tips)

    if person.food_emissions  > 2000:
        more_than_avg = person.food_emissions - 2000
        percentage_above_avg = (more_than_avg/2000) *100
        food_tips.append("Your food consumption is generating {}% more carbond dioxide than the average".format(round(percentage_above_avg,2)))
        food_tips.append("Do not waste food: Throwing away 3kg of edible food results in greenhouse gases equivalent to 23kg of carbon dioxide being emitted into the atmosphere.")
        food_tips.append("Diversify your protien sources: The carbon footprint of beef is four times higher than port and poultry.")
        food_tips.append("Compost: Putting any scraps or unusable leftovers into compost can reduce the amount of methane released into the atmosphere.")
        print()
        print("food_tips:", food_tips)
        
if __name__ == '__main__':
    global tips
    abhi = Person("abhi", "low_meat") 
    abhi.add_house(1, 120)    #abhi spent $120 on electricity
    abhi.add_flight(2)        #abhi took 2 round trip flights in a month 
    abhi.add_car(1100, False) #abhi drove 1100 miles without carpooling
    abhi.add_motorbike(5000)  #abhi drove 5000 miles on a motorbike
    abhi.add_food(500)        #abhi spent 400 dollars on food/month
    abhi.add_subway(100)
    abhi.add_bus(300)
    abhi.add_train(1000)
    abhi.print_footprint()
    abhi.print_report()
    smart_tips(abhi)
