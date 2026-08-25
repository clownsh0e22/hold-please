class PhoneTreeNavigator:
    def __init__(self):
        self.current_state = "start"

    def transition(self, speech_input):
        if "password" in speech_input.lower():
            self.current_state = "password_reset"
            return "1"
        elif "bill" in speech_input.lower():
            self.current_state = "billing"
            return "2"
        else:
            return "0"
