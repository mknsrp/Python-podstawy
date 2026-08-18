import requests
import send_email

topic = "tesla"

api_key = 'd9f30835cc2348b9a1da8aa95ca30440'
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2026-07-18&"
       "sortBy=publishedAt&"
       "apiKey=d9f30835cc2348b9a1da8aa95ca30440&"
       "language=pl")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and descriptions
email_body = ""
for article in content["articles"][:20]:
    title = (article["title"])
    description = (article["description"])

    email_body += f"""
    <h2>{title}</h2>
    <p>{description}</p>
    <p>{article["url"]}</p>
    <hr>
    """
print(email_body)
send_email.send_email(email_body)