import requests

url = 'http://192.168.11.3:8000/food'
data = {'data':1}
h=requests.post(url, json=data)
print(h.text)



