from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
from navigator import PhoneTreeNavigator
from fx_agent import FXAgent

app = Flask(__name__)
navigator = PhoneTreeNavigator()
fx_agent = FXAgent()

@app.route("/voice", methods=['POST'])
def voice():
    response = VoiceResponse()
    speech_input = request.values.get('SpeechResult', '')
    
    if not speech_input:
        response.say("Welcome to the hold bot agent. Initializing interactive voice response system.")
        response.pause(length=2)
        response.say("Navigating menu options.")
    else:
        digit = navigator.transition(speech_input)
        response.play(digits=digit)
        response.say(f"Pressed digit {digit} based on navigation state.")

    return str(response)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
