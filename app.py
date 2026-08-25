from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather
from navigator import PhoneTreeNavigator

app = Flask(__name__)
navigator = PhoneTreeNavigator()

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    resp = VoiceResponse()
    speech_result = request.values.get('SpeechResult', '')

    if speech_result:
        digit = navigator.transition(speech_result)
        resp.play(digits=digit)

    gather = Gather(input='speech', action='/voice', method='POST', timeout=3)
    gather.say("Please state the menu option or speak to navigate.")
    resp.append(gather)

    return str(resp)

if __name__ == '__main__':
    app.run(port=5000)
