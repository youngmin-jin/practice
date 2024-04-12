import pandas as pd
import pickle
from flask import Flask, request, jsonify
import joblib

test_file_path = "/home/jin_youngmin_5254/google-deploy/test/test_data.csv"

# load the saved model
with open('/home/jin_youngmin_5254/google-deploy/xg_model.pkl', 'rb') as f:
    model = pickle.load(f)

def prepare_data(file_path):
    df = pd.read_csv(file_path, encoding="utf-8")
    encoder_loaded = joblib.load('/home/jin_youngmin_5254/google-deploy/encoder.joblib')
    df_encoded = encoder_loaded.transform(df)
    return df_encoded

def predict(df):
    predictions = model.predict(df)
    return predictions    


if __name__ == '__main__':
    df = prepare_data(test_file_path)
    predicted_ce = predict(df)
    print(predicted_ce)

