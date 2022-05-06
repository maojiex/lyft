from flask import Flask
import requests

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def index():
    return "<h2>welcome to the index page</h2>"

@app.route("/lyftTest/<input>", methods = ['GET', 'POST'])
def lyft(input):
    res = requests.post('https://lyft-interview-test.glitch.me/test', json={"string_to_cut": input})
    if res.ok:
        return res.json()
    else:
        return "fail"


# https://lyft-interview-test.glitch.me/test

