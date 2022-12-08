import json
import pickle
import numpy as np
__locations = None
__data_columns = None
__model = None

def predict_price(location,sqft,bath,room):    
    try:
        loc_index =__data_columns.index(location.lower())
    except:
        loc_index=-1
        
    X = np.zeros(len(__data_columns))
    X[0] = sqft
    X[1] = bath
    X[2] = room
    if loc_index >= 0:
        X[loc_index] = 1
    return __model.predict([X])[0]




def load_saved_artifacts():
    print("load saved arifacts...start")
    global __data_columns
    global __model
    global __locations

    with open("./artifacts/columns.json","r") as f:
        __data_columns = json.load(f)["data_columns"]
        __locations=__data_columns[3:]
        
    with open("./artifacts/banglore_home_prices_model.pickle","rb") as f:
        __model=pickle.load(f)

def get_locations_name():
    return __locations

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_locations_name())