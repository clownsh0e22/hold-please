import subprocess
import json

class PhoneTreeNavigator:
    def __init__(self, model_name="deepseek-r1:8b"):
        self.model_name = model_name
        self.current_state = "start"

    def transition(self, speech_input):
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
            return response.get("digit", "0")
        except Exception:
            return "0"
