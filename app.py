# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 11:17:00 2021

@author: sidkadam
"""

import uvicorn 
from fastapi import FastAPI
from model_names import model_names
import numpy as np
import pickle
import pandas as pd

app= FastAPI()
pickle_in = open("classification.pkl","rb")
classification=pickle.load(pickle_in)

@app.get('/')
def index():
    return{"message": "Hello guys"}

@app.get('/{name}')
def get_name(name: str):
    return{f'{name}':"You have deployed your model using fast API"}

@app.post("/predict")
def predict_class(data:model_names):
    data=data.dict()
    Number_of_Man = data['MAN(x1)']
    Number_of_Women = data['WOMAN(x1)']
    Age_between_15_to_25 = data['INW_1524(x1)']  
    Age_between_25_to_45 = data['INW_2544(x1)']
    Dutch_achtergond=data=['P_NL_ACHTG(%)']
    Western_migration_background=['P_NW_MIG_A(%)']
    Single= data['TOTHH_EENP(x1)']
    Total= data['WONING(x1)']
    Born_between_1975_to_1985=data['WON_7584(x1)']
    Meergezins = data['WON_MRGEZ(x1)']
    Persons_with_unemployment_benefits=data['UITKMINAOW(x1)']
    address=data['OAD(adressen/km2)']
    
    prediction=classification.predict([[Number_of_Man,Number_of_Women, Age_between_15_to_25, Age_between_25_to_45,
                                        Dutch_achtergond, Western_migration_background, Single, Total,Born_between_1975_to_1985,
                                        Meergezins, Persons_with_unemployment_benefits,address ]])
    if (prediction==1):
        prediction="It belongs to Urbanity One"
    elif(prediction==2):
        prediction="It belongs to Urbanity two"
    elif(prediction==3):
        prediction="It belongs to Urbanity three"
    elif(prediction==4):
        prediction="It belongs to Urbanity four"
    else:
        prediction="It belongs to Urbanity Five"
    return {
        "prediction":prediction
        }

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1',port=8000)