from flask import Flask, request, jsonify
from twilio.rest import Client
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

@app.route("/call", methods=["POST"])
def call_number():
    data = request.json
    number = data.get("number")
    script = data.get("script")

    if not number or not script:
        return jsonify({"error": "Missing number or script"}), 400

    client = Client("TWILIO_SID", "TWILIO_AUTH")
    call = client.calls.create(
        to=number,
        from_="YOUR_TWILIO_NUMBER",
        twiml=f'<Response><Say>{script}</Say></Response>'
    )
    return jsonify({"status": "Call initiated", "sid": call.sid})

@app.route("/leads", methods=["GET"])
def get_leads():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
    sheet = gspread.authorize(creds).open("Rickby Leads").sheet1
    data = sheet.get_all_records()
    return jsonify(data)

if __name__ == "__main__":
    import os

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
