import os
import requests
from dotenv import load_dotenv

load_dotenv()

DOMAIN = os.getenv("MAILGUN_DOMAIN")


def send_simple_message(to, subject, body):
    domain = os.getenv("MAILGUN_DOMAIN")
    requests.post(
  	    f"https://api.mailgun.net/v3/{domain}/messages",
  		auth=("api", os.getenv('API_KEY', os.getenv("MAILGUN_API_KEY"))),
  		data={"from": "Mailgun Sandbox <postmaster@{domain}",
			"to": [to],
  			"subject": [subject],
  			"text": [body]})