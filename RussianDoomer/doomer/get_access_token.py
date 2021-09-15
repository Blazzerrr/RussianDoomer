
from flask import Flask, redirect
from donationalerts_api import DonationAlertsApi

client = Flask(__name__)
api = DonationAlertsApi("{{client_id}}", "{{client_secret}}", "http://127.0.0.1:5000/login", "oauth-donation-index")


@client.route("/", methods = ["get"])
def index():
    return redirect(api.login())


@client.route("/login", methods = ["get"])
def login():
    code = api.get_code()
    token = api.get_access_token(code)

    return token


if __name__ == "__main__":
    client.run()

