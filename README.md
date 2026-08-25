# Local Webhook Setup

## Architecture
- Flask Application running locally on http://127.0.0.1:5000
- Cloudflare Tunnel routing public HTTPS traffic to local port 5000

## Active Tunnel Specs
- Transport Protocol: HTTP/2 (Fallback applied for UDP/QUIC port 7844 blocking)
- Process Execution: Background logger (`tunnel.log`)
- Public Endpoint: https://occupational-treasure-aka-boxed.trycloudflare.com
- Twilio Webhook Target: https://occupational-treasure-aka-boxed.trycloudflare.com/voice

## Status & Verification
- Connectivity test returned HTTP/2 200 OK via `curl -I`.
- Initial POST simulation to `/voice` returned valid `<Gather>` TwiML XML.
- Speech payload simulation (`SpeechResult=customer service`) returned valid `<Play digits="0" />` TwiML XML.
- Ready for Twilio console integration once account reactivation completes.
