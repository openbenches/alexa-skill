import os
from flask import Flask, render_template, request
from flask_ask import Ask, statement, question, session
import requests, json

app = Flask(__name__)
ask = Ask(app, '/')

headers = {'User-Agent': 'Alexa Skill'}

@ask.launch
def launched():
    return question('Welcome to Open Benches. What would you like to know?')

@ask.intent("AMAZON.FallbackIntent")
def fallback():
    return statement("You can ask for the latest bench, or for a random bench, or find out how many benches there are.")

@ask.intent("LatestBench")
def latest_bench():
    r = requests.get('https://openbenches.org/api/v1.0/alexa.json/?format=raw&latest', headers=headers)
    r.encoding='utf-8-sig'
    j = json.loads(r.text)
    s = j["speech"]
    return statement(s)

@ask.intent("RandomBench")
def random_bench():
    r = requests.get('https://openbenches.org/api/v1.0/alexa.json/?format=raw&random', headers=headers)
    r.encoding='utf-8-sig'
    j = json.loads(r.text)
    s = j["speech"]
    return statement(s)

@ask.intent("HowMany")
def count_bench():
    r = requests.get('https://openbenches.org/api/v1.0/alexa.json/?format=raw&count', headers=headers)
    r.encoding='utf-8-sig'
    j = json.loads(r.text)
    s = j["speech"]
    return statement(s)

@ask.intent("AMAZON.StopIntent")
def stop():
    return statement("Have a nice day!")

@ask.intent("AMAZON.CancelIntent")
def stop():
    return statement("Bye-bye!")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
