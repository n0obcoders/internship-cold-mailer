# 📬 Internship Cold Email Sender (Streamlit App)

A web-based tool built with Streamlit to automate sending personalized cold emails for internship opportunities. You can select your desired domain, upload your resume, and instantly send internship requests to 5 random HRs from a verified list.

---

## 🔧 Features

- Choose from 12 internship domains (e.g., Cyber Security, Graphic Design, etc.)
- Automatically sends emails to 5 HRs at a time
- Upload and attach your resume (PDF)
- Fully customizable with your name, message, and credentials
- Uses Gmail App Password for secure sending

---

## 🖥 How to Run Locally (One-Time Setup)

### 📦 1. Clone the Repository

```bash
git clone https://github.com/n0obcoders/internship-cold-mailer.git
cd internship-cold-mailer
pip install -r requirements.txt
streamlit run app.py
Open your browser and visit: http://localhost:8501
🔐 Gmail App Password Instructions
To send emails from your Gmail securely:

Enable 2-Step Verification in your Google account

Go to: https://myaccount.google.com/apppasswords

Generate an App Password for “Mail” > “Other (Python Script)”

Use this app password in the tool (not your Gmail login password)

🙌 Credits
Developed by Nitin Shukla
Inspired by the need to help freshers automate professional outreach.
