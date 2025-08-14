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
### ✅ on June 3, 2025

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


#!/bin/bash

# Create department directories
mkdir /Engineering /Sales /IS

# Create groups
groupadd engineering
groupadd sales
groupadd is

# Create users for Engineering
useradd -m -s /bin/bash -g engineering eng_admin
useradd -m -s /bin/bash -g engineering eng_user1
useradd -m -s /bin/bash -g engineering eng_user2

# Create users for Sales
useradd -m -s /bin/bash -g sales sales_admin
useradd -m -s /bin/bash -g sales sales_user1
useradd -m -s /bin/bash -g sales sales_user2

# Create users for IS
useradd -m -s /bin/bash -g is is_admin
useradd -m -s /bin/bash -g is is_user1
useradd -m -s /bin/bash -g is is_user2

# Set ownership and permissions for Engineering
chown eng_admin:engineering /Engineering
chmod 2770 /Engineering

# Set ownership and permissions for Sales
chown sales_admin:sales /Sales
chmod 2770 /Sales

# Set ownership and permissions for IS
chown is_admin:is /IS
chmod 2770 /IS

# Create confidential file for Engineering
echo "This file contains confidential information for the department." > /Engineering/confidential.txt
chown eng_admin:engineering /Engineering/confidential.txt
chmod 640 /Engineering/confidential.txt

# Create confidential file for Sales
echo "This file contains confidential information for the department." > /Sales/confidential.txt
chown sales_admin:sales /Sales/confidential.txt
chmod 640 /Sales/confidential.txt

# Create confidential file for IS
echo "This file contains confidential information for the department." > /IS/confidential.txt
chown is_admin:is /IS/confidential.txt
chmod 640 /IS/confidential.txt

# Verification commands
echo "Verifying users and groups..."
getent passwd eng_admin
getent group engineering
id eng_user1

echo "Verifying directory permissions..."
ls -ld /Engineering /Sales /IS

echo "Verifying confidential files..."
ls -l /Engineering/confidential.txt
ls -l /Sales/confidential.txt
ls -l /IS/confidential.txt


**************

# Question 1: Create directories
mkdir ../Exam
mkdir ../Exam/business
mkdir ../Exam/tunes
mkdir ../Exam/book
mkdir ../Exam/temp

# Question 2: Create files
touch ../Exam/tunes/music.mp3
touch ../Exam/tunes/tunes.wav
touch ../Exam/book/sueletters.txt
touch ../Exam/book/list.txt

# Question 3: Copy and move files
cp ../Exam/book/sueletters.txt ../Exam/business/
cp ../Exam/book/list.txt ../Exam/business/
mv ../Exam/tunes/*.mp3 ../Exam/business/
mv ../Exam/tunes/*.wav ../Exam/business/

# Question 4: Copy and remove files
cp ../Exam/business/* ../Exam/temp/
rm ../Exam/temp/*.txt

# Question 5: Rename a file
mv ../Exam/temp/music.mp3 ../Exam/temp/sue.mp3

# Question 6: Move a directory
mv ../Exam/business ../Exam/book/

# Question 7: Use grep to find lines
grep 'false$' /etc/passwd

# Question 8: Bash script to archive a file
#!/bin/bash

# Prompt for the file name
echo "Enter the name of the file:"
read filename

# Check if the file exists
if [ ! -f "$filename" ]; then
    echo "no such file $filename, end of line"
    exit 3
fi

# Get the current date
current_date=$(date +%F)

# Create the archive file name
archive_name="${filename}-${current_date}.tar.gz"

# Create the compressed tar archive
tar -czf "$archive_name" "$filename"

# Print a success message
echo "Job complete"
