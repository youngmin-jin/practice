import pandas as pd
import pickle
from flask import Flask, request, jsonify
import joblib

# load the saved model
with open('xg_model.pkl', 'rb') as f:
    model = pickle.load(f)

def transform_data(df):
    encoder_loaded = joblib.load('encoder.joblib')
    df_encoded = encoder_loaded.transform(df)
    return df_encoded

def predict_ce(df):
    predictions = model.predict(df)
    return predictions    

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def predict():
    if request.method == "POST":
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({"error":"no file"})
        
        try:
            # df = pd.read_csv(request.files.get('file'))
            df = pd.read_csv(file, encoding='utf-8')
            df = transform_data(df)
            predictions = predict_ce(df)
            return jsonify({"predictions":predictions.tolist()})
            
        except Exception as e:
            return jsonify({"error":str(e)})
    
    return "OK"


if __name__ == '__main__':
    app.run(debug=True)    
