import requests

url = "https://background-removal.p.rapidapi.com/remove"

payload = "image_url=http://telegra.ph//file/ed93a3d592491964600b2.jpg"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Host": "background-removal.p.rapidapi.com",
	"X-RapidAPI-Key": "94c5f2655fmshfd1508bf4269d2ap136776jsn6f630f792036"
}


def removeback(img_url):
    payload = f"image_url={img_url}"
    response = requests.request("POST", url, data=payload, headers=headers)
    link = response.json()['response']['image_url']
    return link
print(removeback("http://telegra.ph//file/ed93a3d592491964600b2.jpg"))