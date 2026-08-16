import requests

api_key = 'd9f30835cc2348b9a1da8aa95ca30440'
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2026-07-16&sortBy=publishedAt&apiKey="
       "d9f30835cc2348b9a1da8aa95ca30440")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and descriptions
for article in content["articles"]:
    print(article["title"])
    print(article["descriptions"])