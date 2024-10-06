# Write a program to print this JSON to the console: https://api.coindesk.com/v1/bpi/currentprice.json
# Author: Finbar Dennehy

import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()
print(data)