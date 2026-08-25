# PROJECT_STATE.md — Hold-Bot-Agent Recovery & Direction File

## Core Directives & Hard Constraints
- DO NOT USE NGROK UNDER ANY CIRCUMSTANCES. IT REQUIRES A PAID SUBSCRIPTION. DO NOT SUGGEST IT.
- Hardware/Environment: macOS Apple M5 Pro, 48 GB RAM, Python virtual environment (`venv`).
- Ollama: Local model integration via `navigator.py`.
- Workflows: Designated terminal windows (1st, 2nd, 3rd window). Single-step terminal instructions with verification checks unless user requests batch operations.

---

## Completed Architecture & Progress

1. **Repository & Dependencies**
   - Repository initialized and tracked on GitHub: `clownsh0e22/hold-please.git`.
   - `requirements.txt` updated with pinned environment dependencies.

2. **State Machine & Hold Detection (`navigator.py`)**
   - Implemented `PhoneTreeNavigator`.
   - Integrated local Ollama model to process speech input and derive menu navigation decisions/digits.
   - Added hold detection heuristics (detecting hold music/phrases) to trigger pause actions.

3. **Flask Voice Webhook & Session Management (`app.py`)**
   - Exposed `/voice` route supporting `GET` and `POST`.
   - Integrated `PhoneTreeNavigator` to parse incoming Twilio `SpeechResult`.
   - Multi-turn session tracking per `CallSid`.
   - Generates TwiML output using `<Gather>`, `<Play digits="...">`, and `<Pause length="5" />`.

4. **Testing Suite (`test_sim.py`)**
   - Unit tests written using `unittest` and Flask `test_client`.
   - Asserts navigation (`<Play digits=>`) and hold detection (`<Pause length="5" />`).
   - All tests passing verified via `python test_sim.py`.

5. **Commit History Snapshot**
   - Includes implementation of dynamic hold detection and DTMF handling.

---

## Remaining Roadmap

1. **Local Tunneling (Free Alternatives Only)**
   - STRICT RULE: DO NOT USE NGROK.
   - Setup free local tunnel exposure using `cloudflared` (Cloudflare Tunnel) or `localtunnel` to expose local port 5000 to Twilio.

2. **End-to-End Live Integration Test**
   - Start Flask server, launch free tunnel, point Twilio webhook to public URL, and execute live call test.
