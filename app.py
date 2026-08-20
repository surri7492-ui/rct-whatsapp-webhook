from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "RCT2026Webhook"


@app.route("/", methods=["GET"])
def home():
    return "RCT WhatsApp Webhook is running!"


@app.route("/webhook", methods=["GET"])
def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    print("=== WEBHOOK VERIFICATION ===")
    print("Mode:", mode)
    print("Token:", token)
    print("Challenge:", challenge)

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("VERIFICATION SUCCESS")
        return challenge, 200

    print("VERIFICATION FAILED")
    return "Forbidden", 403


@app.route("/webhook", methods=["POST"])
def receive_webhook():
    print("\n==============================")
    print("NEW WEBHOOK POST RECEIVED")
    print("==============================")

    print("Headers:")
    print(dict(request.headers))

    print("\nRaw body:")
    print(request.get_data(as_text=True))

    print("\nJSON:")
    print(request.get_json(silent=True))

    print("==============================\n")

    return "EVENT_RECEIVED", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
