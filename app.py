import os
from flask import Flask, render_template, request
from flask_ask import Ask, statement, question, session
import requests


app = Flask(__name__)
ask = Ask(app, '/')

headers = {'User-Agent': 'My User Agent 1.0'}

@ask.launch
def launched():
    return question('Welcome to Open Benches. What would you like to know?')

@ask.intent("AMAZON.FallbackIntent")
def fallback():
    return statement("You can ask for the latest bench, or for a random bench, or find out how many benches there are.")

@ask.intent("LatestBench")
def prescription_cost():
    return statement("The latest bench is...")

@ask.intent("RandomBench")
def prescription_cost():
    r = requests.get('https://test.openbenches.org/api/v1.0/alexa.json/?format=raw&random', headers=headers)
    print(r.text)
    s = r.json()["speech"]
    return statement(s)

@ask.intent("HowMany")
def prescription_cost():
    return statement("Five hundred and fifty five.")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
