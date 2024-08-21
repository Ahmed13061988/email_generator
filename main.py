import plistlib
import requests
from send_email import send_email

api_key = "2ca2e4fc76d6437ba40dae617fe02fab"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-07-21&sortBy=publishedAt" \
      "&apiKey=2ca2e4fc76d6437ba40dae617fe02fab"

request = requests.get(url)
content = request.json()

body = ""

for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2 * "\n"

body = body.encode("utf-8")

send_email(body)

