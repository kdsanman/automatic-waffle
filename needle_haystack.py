import sys, os
import requests
import json


payload = {'token': '39be59fc62b2573f516c8ad106d6eed0'}
r = requests.post("http://challenge.code2040.org/api/haystack", data=payload)
data = r.json()
haystack = data["haystack"]
needle = data["needle"]

for i in range(0, len(haystack)):
    if needle == haystack[i]:
        payload = {'token': '39be59fc62b2573f516c8ad106d6eed0', 'needle': i}
        r = requests.post("http://challenge.code2040.org/api/haystack/validate", data=payload)

