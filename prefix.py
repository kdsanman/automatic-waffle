import sys, os
import requests
import json

payload = {'token': '39be59fc62b2573f516c8ad106d6eed0'}
r = requests.post("http://challenge.code2040.org/api/prefix", data=payload)
data = r.json()
prefix = data["prefix"]
array = data["array"]
print(prefix)
print(array)
n = len(prefix)
list = []
for i in range(0, len(array)):
    if not array[i].startswith(prefix):
       list.append(array[i])
       
payload = {'token': '39be59fc62b2573f516c8ad106d6eed0', 'array': list}
r2 = requests.post("http://challenge.code2040.org/api/prefix/validate", json=payload)
print(r2.text) 
