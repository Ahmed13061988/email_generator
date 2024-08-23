import requests
from send_email import send_email

topic = "tesla"

api_key = "2ca2e4fc76d6437ba40dae617fe02fab"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2024-07-23&sortBy=publishedAt" \
      "&apiKey=2ca2e4fc76d6437ba40dae617fe02fab" \
      "&language=en"

request = requests.get(url)
content = request.json()

body = "Subject: Today's News" + "\n"

for article in content["articles"][:10]:
    if article["title"] is not None and article["description"] is not None:
        body = body + article["title"] + "\n" + \
               article["description"] + "\n" + \
               article["url"] + 2 * "\n"

body = body.encode("utf-8")

send_email(body)

