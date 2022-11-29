import requests
from jsonExtract import jsonExtract

from pprint import pprint as print

city='navoi'

url = f"https://api.pray.zone/v2/times/today.json?city={city}"

r = requests.get(url)
# print(r.status_code)
res = r.json()
# res['results']['datetime'][0]['times']
# print(res)
while True:
    
    namoz_vaqti = input("Namoz mahalini yozing ('Fajr', 'Sunrise', 'Dhuhr', 'Asr', 'Maghrib', 'Isha'): \n>>> ")
    
    
    print(jsonExtract(res, namoz_vaqti.title()))
    
    if namoz_vaqti == 'quit':
        break
