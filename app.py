from flask import Flask, request, jsonify
from twilio.rest import Client
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

app = Flask(__name__)

@app.route("/call", methods=["POST"])
def call_number():
    data = request.json
    number = data.get("number")
    script = data.get("script")

    if not number or not script:
        return jsonify({"error": "Missing number or script"}), 400

    # Use environment variables
    account_sid = os.environ.get("TWILIO_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    twilio_number = os.environ.get("TWILIO_NUMBER")

    if not all([account_sid, auth_token, twilio_number]):
        return jsonify({"error": "Twilio credentials not set"}), 500

    try:
        client = Client(account_sid, auth_token)
        call = client.calls.create(
            to=number,
            from_=twilio_number,
            twiml=f'<Response><Say>{script}</Say></Response>'
        )
        return jsonify({"status": "Call initiated", "sid": call.sid})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/leads", methods=["GET"])
def get_leads():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
    sheet = gspread.authorize(creds).open("Rickby Leads").sheet1
    data = sheet.get_all_records()
    return jsonify(data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
