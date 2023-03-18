import requests

# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/e9e06dc1b6a5afe193e7b803/pair/USD/UZS'

# Making our request
response = requests.get(url)

jsondata = response.json()
# Your JSON object
kurs = response.json()['conversion_rate']
print(f"Bugungi kurs: \n1 AQSH dollari = {kurs} sum")
