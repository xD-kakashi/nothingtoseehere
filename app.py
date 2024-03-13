from flask import Flask, render_template, request, redirect
import requests
import threading

URL = "https://umisc.club/"

app = Flask(__name__)

def hit_http():
    url_request = requests.get(url = URL)
    print(url_request)

threading.Timer(900.0,hit_http).start()

@app.route("/")
def index():
    return render_template('index.html')