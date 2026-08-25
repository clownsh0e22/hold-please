from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=['POST'])
def voice():
    response = VoiceResponse()
    response.say("Welcome to the hold bot agent. Initializing interactive voice response system.")
    response.pause(length=2)
    response.say("Navigating menu options.")
    return str(response)

if __name__ == "__main__":
    app.run(port=5000)
