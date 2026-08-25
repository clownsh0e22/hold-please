import subprocess
import json

class PhoneTreeNavigator:
    def __init__(self, model_name="deepseek-r1:8b"):
        self.model_name = model_name
        self.current_state = "start"
        self.on_hold = False

    def transition(self, speech_input):
        text = speech_input.lower()
        
        # Hold detection heuristics
        hold_phrases = ["please hold", "stay on the line", "all agents are busy", "your call is important to us"]
        if any(phrase in text for phrase in hold_phrases):
            self.on_hold = True
            return {"action": "wait", "digit": None}

        self.on_hold = False
        prompt = (
            f"An automated phone menu said: '{speech_input}'. "
            "Determine the single numeric key (0-9) to press to navigate this menu effectively. "
            "Respond ONLY with a JSON object containing a single key 'digit' with the string value of the number."
        )
        try:
            result = subprocess.run(
                ["ollama", "run", self.model_name, prompt],
                capture_output=True,
                text=True,
                check=True
            )
            response = json.loads(result.stdout.strip())
            digit = response.get("digit", "0")
            return {"action": "play_digit", "digit": digit}
        except Exception:
            return {"action": "play_digit", "digit": "0"}
