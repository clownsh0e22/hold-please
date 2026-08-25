# Hold Please (Hold Bot Agent)

A Flask-based Twilio voice bot integration designed to intelligently navigate interactive voice response (IVR) phone trees using speech-to-intent mapping and automated state machines.

## Features
- **Twilio Voice Webhook Integration:** Handles incoming voice requests and responds with dynamic TwiML instructions.
- **State Machine Navigation:** Maps user speech input (e.g., password reset, billing inquiries) to the correct downstream IVR navigation paths.
- **Local Simulation Tools:** Includes testing utilities to simulate Twilio webhooks locally.

## Setup & Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/clownsh0e22/hold-please.git
   cd hold-please
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```
