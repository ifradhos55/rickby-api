# Rickby → Rick The Bot Yapper

## Project Function:
**Rickby is a General AI Agent designed to perform a variety of telephone operations.**  
Primary use cases include:
- Telemarketing & Sales
- Customer Service (Refunds, Complaints, Reviews)
- Customer Troubleshooting & Follow-ups

The agent is designed to operate semi-autonomously, placing and managing calls from a centralized list or database, adapting to tone and case type where needed.

---

## Step-by-Step Build Process

---
###✅ Achieved on June 3, 2025

### Step 1: Core Call Functionality
**Purpose:** Establish basic outbound call capabilities using Twilio

1. Create a Python-based script using Twilio to:
   - Call a number
   - Read a scripted message using Text-to-Speech
   - Hang up after 3–5 rings if unanswered
   - Move on to the next number in the queue

2. Support lead/script input from a CSV file

---

### Step 2: Voicemail Detection & Sheets Integration
**Purpose:** Enhance call realism and lead sourcing

1. Integrate **Answering Machine Detection (AMD)** using Twilio  
   → Automatically detect voicemail and deliver a scripted message

2. Access phone numbers and scripts from a **Google Sheet**  
   → Use the `gspread` + Google API with a service account

---

### Step 3: Deploy Rickby as a Public API
**Purpose:** Enable remote usage via web or GPT

1. Wrap the Python logic in a **Flask API**
2. Create two endpoints:
   - `POST /call` → Makes a call with a phone number and script
   - `GET /leads` → Fetches list of leads from Google Sheets

3. Deploy the API on **Render**  
   → Live URL: [https://rickby.onrender.com](https://rickby.onrender.com)

---

### Step 4: GPT Integration via Actions
**Purpose:** Control Rickby from within a custom GPT

1. Manually define GPT actions for `/call` and `/leads`
2. Test commands like:
   - “Call this number and say this script…”
   - “Get the next 3 leads from the list”

---

## Remaining Development Steps

---

### Step 5: Voicemail Script Management
**Goal:** Leave a pre-recorded or TTS message when voicemail is detected

1. Create fallback voicemail scripts (TTS or MP3)
2. Ensure logic branches depending on AMD result

---

### Step 6: Adaptive Tone & Case-Type Response
**Goal:** Allow Rickby to handle refunds, complaints, and reviews in different tones

1. Create categories of case types (e.g., refund, complaint, product info)
2. Dynamically adjust the script based on:
   - Sentiment or intent (manual for now, future: LLM classification)
   - Customer profile

---

### Step 7: Call Logging and State Tracking
**Goal:** Track call outcomes and statuses

1. Add a `status` flag to each lead (e.g., success, failed, voicemail, no answer)
2. Optionally write back to Google Sheets or store in Firebase/MongoDB

---

### Step 8: Queue Management & Retries
**Goal:** Handle large lead batches intelligently

1. Implement retry logic for failed or missed calls
2. Option to pause/resume queue

---

### Step 9: Dashboard for Monitoring
**Goal:** Provide a visual interface for monitoring call status

1. Build a lightweight dashboard (React or Streamlit)
2. Display:
   - Current call queue
   - Live status updates
   - Lead history and logs

---

### Step 10: Speech Input & Customer Interaction (Phase 2)
**Goal:** Move beyond 1-way calling into responsive dialog

1. Add speech recognition using Twilio or Deepgram
2. Capture user replies and process basic intents (e.g., "Yes", "No", "Refund", "Stop calling")
3. Use OpenAI API or GPT function calls for reply generation (future phase)

---

## Status
- **Version:** 0.0.0
- **Live API:** [https://rickby.onrender.com](https://rickby.onrender.com)
- **Integration:** CSV, Google Sheets, Custom GPT
- **In Development:** Voicemail, Adaptive Tone, Logging, Dashboard, Smart Retry

---

## License
This project is experimental and currently in active development. Contributions are welcome.
