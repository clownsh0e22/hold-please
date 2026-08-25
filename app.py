from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather
from navigator import PhoneTreeNavigator

app = Flask(__name__)
sessions = {}

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    resp = VoiceResponse()
    call_sid = request.values.get('CallSid', 'default')
    speech_result = request.values.get('SpeechResult', '')

    if call_sid not in sessions:
        sessions[call_sid] = PhoneTreeNavigator()

    navigator = sessions[call_sid]

    if speech_result:
        res = navigator.transition(speech_result)
        if res["action"] == "play_digit" and res["digit"]:
            resp.play(digits=res["digit"])
        elif res["action"] == "wait":
            resp.pause(length=5)

    gather = Gather(input='speech', action='/voice', method='POST', timeout=5)
    gather.say("Please state the menu option or speak to navigate.")
    resp.append(gather)

    return str(resp)

if __name__ == '__main__':
    app.run(port=5000)
