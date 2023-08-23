import os
import sys
from pathlib import Path
import json
from flask import Flask, jsonify, request
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
import pickle
sys.path.append(str(Path.cwd().parent))
from settings.params import (DATA_DIR_INPUT,
                             DATA_DIR_OUTPUT,
                             MODEL_PARAMS,
                             REPORT_DIR,
                             TIMEZONE,
                            HOME_DIR 
                            )

app = Flask(__name__)



def newFeatures(df):
  df['Date'] = pd.to_datetime(df['Open Date'],format='%m/%d/%Y')
  df['Year'] = df['Date'].dt.year
  df['Month'] = df['Date'].dt.month
  df['Years Old'] = pd.to_datetime('23-03-2015', dayfirst=True).year - df['Date'].dt.year
  df = df.drop(['Open Date','Date'],axis=1)
  return df

def catFea(df):
  labelEncoding = LabelEncoder()
  df['City Group'] = labelEncoding.fit_transform(df['City Group'].astype('str'))
  df['Type'] = labelEncoding.fit_transform(df['Type'].astype('str'))
  return df

def reorderingCols(test_data):
    test = test_data[['Id','City','City Group','Type','Year','Month','Years Old','P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','P11','P12','P13','P14','P15','P16','P17','P18','P19','P20','P21','P22','P23','P24','P25','P26','P27','P28','P29','P30','P31','P32','P33','P34','P35','P36','P37']]
    return test

def split_X_y(test_data):
    X_test = test_data.drop(['Id','City'],axis=1)
    return X_test

scaler = StandardScaler()
# transform data
def scaling(X_test):
    X_test_scale = scaler.transform(X_test)
    return X_test_scale

def featureEngineering(test):

    #generating new features
    if 'Open Date' in test:
        test = newFeatures(test)
    
    #Reordering columns
    test = reorderingCols(test)
    

    #Handling numerical features
    dropnum = ['P12', 'P17', 'P18', 'P25', 'P28', 'P34']
    test = test.drop(dropnum,axis=1)


    #Handling categorical features
    test = catFea(test)  

    #Split X & y
    X_test = split_X_y(test)

    #Standard Scaling
   # X_test_scale = scaling(X_test)

    return X_test

def predict_single_row(objet):      
    x = pd.DataFrame(np.empty((0,42)))
    column = MODEL_PARAMS['FEATURES']
    x.columns = column
    x.loc[len(x)] = 0
    
    for key , value in objet.items() :
        if key in column :
            x[key] = value


    #x = catFea(x) 
    X_test_scale = featureEngineering(x)
    # Get the path to the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the model file within the container
    model_path = os.path.join(script_dir, '..', 'models', 'bestmodel.pkl')

# Load the model
    model = pickle.load(open(model_path, 'rb'))
    # model = pickle.load(open(str(HOME_DIR) + '/models/bestmodel.pkl', 'rb'))
    return model.predict(X_test_scale)

@app.route('/predict', methods=['POST'])
def question_answers():

    data = json.loads(request.data)
    print(type(data))
    
    
    answer = predict_single_row(data)
    return jsonify({"revenue" : float(answer[0]) }), 200

@app.route('/test', methods=['GET'])
def get_tests():
 return jsonify({ 'message': "test message"}), 200


if __name__ == '__main__':
    # app.run(port=5000, use_reloader=True)
    app.run(host='0.0.0.0', port = 5000, use_reloader=True)