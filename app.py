import os
from flask import Flask, render_template, request
from flask_ask import Ask, statement, question, session
import json, urllib.request


app = Flask(__name__)
ask = Ask(app, '/')

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
    return statement("Some Bench details")

@ask.intent("HowMany")
def prescription_cost():
    return statement("Five hundred and fifty five.")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
