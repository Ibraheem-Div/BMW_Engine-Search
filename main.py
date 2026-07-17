#import a library
import csv

#function read data 
def read_data():
    new_data=[]
    with open('Data.csv', mode='r' , encoding='utf-8') as file:
        reader= csv.DictReader(file)
        for row in reader:
            new_data.append(row)
    return new_data
#function take a input user
def take_order():
    user_order=input('What the Engine you search:')
    user_order=user_order.strip().upper()
    return user_order
#function use loop to search in data from user order
def search_engine (engine_list,search_code):
    for engine in engine_list :
        if engine ['EngineName'].strip().upper() == search_code:
            return engine
    return None
#fuction print a result
def output (engine):
    if engine is None :
        print ('Sorry, this engine is not in database')
    else:
        print("--The engine was successfully found--")
        print(f"Name engine: {engine['EngineName']}")
        print(f"Code engine: {engine['EngineCode']}")
        print(f"Engine displacement: {engine['Capacity']}")
        print(f"Cylinders: {engine['Cylinders']}")
        print(f"Aspiration: {engine['Aspiration']}")
        print(f"Max RPM: {engine['RedLine']}")
        print(f"HP: {engine['Power']}")
        print(f"Torque: {engine['EngineTorque']}")
        print(f"Chassis: {engine['Chassis']}")
        print(f"Fuel Type: {engine['FuelType']}")

#link the functions
engine_data=read_data()
user_data=take_order()
matched_engine=search_engine(engine_data,user_data)
output(matched_engine)