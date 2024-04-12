import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import cross_val_score, KFold
from xgboost import XGBRegressor
import pickle
import joblib
from category_encoders import *

# file path
file_path = "/home/jin_youngmin_5254/google-deploy/test/carbon_emission2.csv"

def prepare_data(file_path):
    df = pd.read_csv(file_path, encoding="utf-8")
    
    # fill null vehicle_type
    df.loc[(df['Vehicle Type'].isnull()) & (df['CarbonEmission']<=1934), 'Vehicle Type'] = 'electric'
    df.loc[(df['Vehicle Type'].isnull()) & ((df['CarbonEmission']>1934) & (df['CarbonEmission']<=2775)), 'Vehicle Type'] = 'hybrid'
    df.loc[(df['Vehicle Type'].isnull()) & ((df['CarbonEmission']>2775) & (df['CarbonEmission']<=3312)), 'Vehicle Type'] = 'diesel'
    df.loc[(df['Vehicle Type'].isnull()) & ((df['CarbonEmission']>3312) & (df['CarbonEmission']<=3438)), 'Vehicle Type'] = 'lpg'
    df.loc[(df['Vehicle Type'].isnull()) & (df['CarbonEmission']>3438), 'Vehicle Type'] = 'petrol'
    
    return df  

def split_data(df):
    x_train, x_test, y_train, y_test = train_test_split(df.drop('CarbonEmission', axis=1), df[['CarbonEmission']], train_size=0.7)
    
    # one hot encoding and save an encoder
    encoder = OrdinalEncoder().fit(x_train)
    x_train_encoded = encoder.transform(x_train)
    x_test_encoded = encoder.transform(x_test)
    joblib.dump(encoder, '/home/jin_youngmin_5254/google-deploy/encoder.joblib')

    return x_train_encoded, x_test_encoded, y_train, y_test

def print_r2_mae(model, x_test, y_test):
    y_predicted = model.predict(x_test)
    y_actual = np.array(y_test['CarbonEmission'])
    r2 = r2_score(y_actual, y_predicted)
    mae = mean_absolute_error(y_actual, y_predicted)
    print("r2:", r2, "mae:", mae)

def xg_model(x_train, y_train):
    xg = XGBRegressor()
    xg_folds = KFold(n_splits=5, shuffle=True, random_state=100)
    xg_scores = cross_val_score(xg, x_train.to_numpy(), y_train.to_numpy(), scoring='r2', cv=xg_folds)
    xg_model = xg.fit(x_train.to_numpy(), y_train.to_numpy())
    return xg_model


if __name__ == "__main__":
    # prepare data
    df = prepare_data(file_path)
    
    # split data
    x_train, x_test, y_train, y_test = split_data(df)

    # create xg model 
    xg_model = xg_model(x_train, y_train)

    # print r2 and mae score
    print_r2_mae(xg_model, x_test, y_test)

    # save model as pickle
    with open('/home/jin_youngmin_5254/google-deploy/xg_model.pkl', 'wb') as f:
        pickle.dump(xg_model, f)


    
    
