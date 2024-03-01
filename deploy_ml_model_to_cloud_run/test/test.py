import requests

resp = requests.post("https://127.... something", files={'file':open('/home/jin_youngmin_5254/google-deploy/test/test_data.csv', 'rb')})
# resp = requests.post("https://getprediction-g3ozk66igq-ue.a.run.app", files={'file':open('/home/jin_youngmin_5254/google-deploy/test/test_data.csv', 'rb')})
print(resp.json())
