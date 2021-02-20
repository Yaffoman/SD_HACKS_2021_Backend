#calculate_carbon.pyS
#baseline calculator


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
        
Useful links: https://www.carbonfootprint.com/calculator.aspx 

"""

electricity_rate = 13 #cents/kWh


total_carbon_kgs = 0


class Person:
    def __init__(self, name:str): 
        self.name = name
        self.kg_carbon_footprint = 0
        #household
        self.kWh_factor = 0.4532 

    def add_house(self, occupants: int, electricity_bill: float): #electricity bill is in dollars
        kWh_used = electricity_bill/0.13  #reasoning: avg cost of 1 kWh in america = 12.87 cents
        self.kg_carbon_footprint += (kWh_used * self.kWh_factor) / occupants

    def add_flight(self, num_of_round_trips:int):
        self.kg_carbon_footprint += num_of_round_trips * 1000 #assumption: 13 hour of flight time 
        
    def add_car(self, miles:int, carpool: bool):
        #avg passenger vehicle emits 423g of CO2/mile
        #avg passenger vehicle does 21 miles per gallon
        CO2_permile = 0.423 #kg 
        if carpool: CO2_permile /= 2 
        self.kg_carbon_footprint += miles * CO2_permile 

    def add_motorbike(self, miles:int):
        km_driven = miles * 1.6
        self.kg_carbon_footprint += km_driven * 0.077 

    def print_footprint(self):
        print("carbon footprint:", '%.2f'%self.kg_carbon_footprint, "kgCO2 emission/month")

if __name__ == '__main__':

    abhi = Person("abhi") 
    abhi.add_house(1, 120) #abhi spent $120 on electricity
    abhi.add_flight(2)     #abhi took 2 round trip flights in a month 
    abhi.add_car(5000, False) #abhi drove 5000 miles without carpooling
    abhi.add_motorbike(5000)
    abhi.print_footprint()
