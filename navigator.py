class PhoneTreeNavigator:
    def __init__(self):
        self.flow = {
            "main_menu": {"prompt": "press 1 for billing", "digit": "1"},
            "billing_menu": {"prompt": "press 2 for a representative", "digit": "2"},
            "hold": {"prompt": "waiting for human", "digit": None}
        }
    
    def get_next_step(self, current_state):
        return self.flow.get(current_state, {"prompt": "unknown", "digit": None})

if __name__ == "__main__":
    nav = PhoneTreeNavigator()
    print("Navigator initialized. Current state: main_menu ->", nav.get_next_step("main_menu"))
