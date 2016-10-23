import requests
payload = {'token': '39be59fc62b2573f516c8ad106d6eed0'}
r = requests.post("http://challenge.code2040.org/api/reverse", data=payload)
print(r.text)
r = r.text
r = r[::-1]
print(r)
payload = {'token': '39be59fc62b2573f516c8ad106d6eed0', 'string': r} 
r = requests.post("http://challenge.code2040.org/api/reverse/validate", data=payload)
print(r.text)
