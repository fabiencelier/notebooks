import time
import requests
while True:
  try:
    request = requests.get("http://localhost:9999/")
    if request.status_code == 200:
      print("URL is ready")
      break
    else:
      print("Waiting for URL, current status is " + str(request.status_code))
  except Exception as e:
    print(e)
    print("Waiting for URL, connexion failed")
  time.sleep(2)
