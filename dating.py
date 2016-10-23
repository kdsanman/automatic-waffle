import sys, os
import requests
import json
import datetime
import dateutil.parser

payload = {'token': '39be59fc62b2573f516c8ad106d6eed0'}
r = requests.post("http://challenge.code2040.org/api/dating", data=payload)
data = r.json()
datestamp = data["datestamp"]
interval = data["interval"]
print(datestamp)
print(interval)

datestamp = dateutil.parser.parse(datestamp)
tentresult = datestamp + datetime.timedelta(0, interval)
if tentresult.isoformat()[-6:] == "+00:00":
        result = tentresult.isoformat()[:-6] + 'Z'
else:
        result = tentresult.isoformat()

print(result)

payload = {'token': '39be59fc62b2573f516c8ad106d6eed0', 'datestamp': result}
r = requests.post("http://challenge.code2040.org/api/dating/validate", json=payload)
print(r.text)
