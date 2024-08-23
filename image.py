import requests

url = "https://awoiaf.westeros.org/images/2/23/Marc_Simonetti_Damon_Prince-VillainII.jpg"

response = requests.get(url)

with open("image.png", "wb") as file:
    file.write(response.content)
