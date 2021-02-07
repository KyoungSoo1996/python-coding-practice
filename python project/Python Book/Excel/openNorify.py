import requests
import json

url = "http://api.open-notify.org/iss-now.json"
r = requests.get(url)
print(r.text)