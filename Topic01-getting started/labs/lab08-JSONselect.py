# Modify the program to only output the current price in Euros
# Author: Finbar Dennehy

import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()
print(data['bpi']['EUR']['rate_float'])