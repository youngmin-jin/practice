# Deploy ML model to Google Cloud Run
Ref: https://github.com/patrickloeber/ml-deployment/tree/main/google-cloud-run 
<br/><br/>

## Write Codes
1. Write [train.py](https://github.com/youngmin-jin/practice/blob/main/deploy_ml_model_to_cloud_run/test/train.py, "train.py") code that creates ML model
   - save encoder and model

2. Write [load.py](https://github.com/youngmin-jin/practice/blob/main/deploy_ml_model_to_cloud_run/test/test.py](https://github.com/youngmin-jin/practice/blob/main/deploy_ml_model_to_cloud_run/test/load.py)https://github.com/youngmin-jin/practice/blob/main/deploy_ml_model_to_cloud_run/test/load.py, "load.py") to test if the saved model works fine with another data
   - load the saved encoder and model

3. Write [main.py](https://github.com/youngmin-jin/practice/blob/main/gcp_cloud_run_deploy_ml_model/main.py, "main.py") app using Flask
   - load the saved encoder and model
   - use Flask app
     ```
      app = Flask(__name__)
      
      @app.route("/", methods=["GET","POST"])
      def predict():
          if request.method == "POST":
      ...
     ```

4. Write [test.py](https://github.com/youngmin-jin/practice/blob/main/deploy_ml_model_to_cloud_run/test/test.py, "test.py") to test if main.py works fine using localhost
   ```
    resp = requests.post("https://127.... something", files={'file':open('/home/jin_youngmin_5254/google-deploy/test/test_data.csv', 'rb')})
   ``` 

## Setup Google Cloud
- In GCP, activate Cloud Run API and Cloud Build API <br/><br/>

## Containerize App using Docker
- [Dockerfile](https://github.com/youngmin-jin/practice/blob/main/deploy_ml_model_to_cloud_run/Dockerfile, "Dockerfile")
- [requirements.txt](https://github.com/youngmin-jin/practice/blob/main/deploy_ml_model_to_cloud_run/requirements.txt, "requirements.txt")
- [.dockerignore](https://github.com/youngmin-jin/practice/blob/main/deploy_ml_model_to_cloud_run/.dockerignore, ".dockerignore") <br/><br/>

- Open GCP cloud shell and make an alignment like below <br/>
   -> train.py, test.py, and load.py files in the test folder <br/>
   -> Dockerfile, requirements.txt, .dockerignore, main.py, encoder, and model in the google-deploy folder <br/>
    > ![image](https://github.com/youngmin-jin/practice/assets/135728064/e2bcf68f-f31e-408a-a2a7-37b39de3afbb) 

## Cloud Build and Deploy
- Build cloud (predict -> named after @app.route~ in main.py)
  > gcloud builds submit --tag gcr.io/gothic-imprint-407506/predict 

- Deploy app
  > gcloud run deploy --image gcr.io/gothic-imprint-407506/predict --platform managed <br/><br/>
  >   -> Service name: getprediction <br/>
  >   -> Region: 33

- Modify test.py and test if it is successfully deployed
  ```
  resp = requests.post("https://getprediction-g3ozk66igq-ue.a.run.app", files={'file':open('/home/jin_youngmin_5254/google-deploy/test/test_data.csv', 'rb')})
  ```














