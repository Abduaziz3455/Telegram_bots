import requests
# from jsonExtract import jsonExtract

from pprint import pprint as print

app_id = "a9c6bbd6"
app_key = "f00be5039289fef3f6cc7dd732a2a2ee"
language = "en-gb"

word_id = "earth"
url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()

r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})

print(r.status_code)
res = r.json()
# print(res)

print(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
print(res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile'])
