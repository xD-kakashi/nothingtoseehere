from flask import Flask, render_template, redirect
import requests
import threading

URL = "https://umisc.club/"

app = Flask(__name__)

def hit_http():
    url_request = requests.get(url = URL)
    threading.Timer(890.0,hit_http).start()
    print(url_request)

threading.Timer(1,hit_http).start()

@app.route("/")
def index():
    return render_template('index.html')