import plistlib
import requests

api_key = "2ca2e4fc76d6437ba40dae617fe02fab"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-07-21&sortBy=publishedAt" \
      "&apiKey=2ca2e4fc76d6437ba40dae617fe02fab"

request = requests.get(url)
content = request.json()


for i in content["articles"]:
    print(i)


