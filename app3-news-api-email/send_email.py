import smtplib, ssl
from email.message import EmailMessage


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "dowsha12345@gmail.com"
    password = "favetnttcoxgorsc"
    receiver = "dowsha12345@gmail.com"

    msg = EmailMessage()
    msg["Subject"] = "Newest articles"
    msg["From"] = username
    msg["To"] = receiver

    msg.set_content(message, subtype="html", charset="utf-8")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.send_message(msg)