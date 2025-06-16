import streamlit as st
import pandas as pd
import random
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Load HR contacts
@st.cache_data
def load_hr_data():
    return pd.read_csv("hr_contacts.csv")

hr_df = load_hr_data()

# Title
st.title("🚀 Internship Cold Email Sender")
if st.button("🌐 Visit My Portfolio"):
    st.markdown("Redirecting...")
    st.markdown("[Click here if not redirected](https://portfolio-n0obcoders-projects.vercel.app/)", unsafe_allow_html=True)


# Form inputs
with st.form("email_form"):
    name = st.text_input("Your Full Name")
    email = st.text_input("Your Gmail Address")
    app_password = st.text_input("Gmail App Password (Get from https://myaccount.google.com/apppasswords)", type="password")

    domain = st.selectbox("Choose Your Internship Role", [
        "Cyber Security Intern", "Graphic Designer Intern", "Frontend Developer Intern",
        "Backend Developer Intern", "Data Science Intern", "DevOps Intern",
        "Machine Learning Intern", "Blockchain Developer Intern", "Cloud Computing Intern",
        "Android Developer Intern", "Web Developer Intern", "Digital Marketing Intern"
    ])

    about = st.text_area("Tell us about yourself")
    resume = st.file_uploader("Upload Your Resume (PDF only)", type=["pdf"])

    submit = st.form_submit_button("Send Emails")

if submit:
    if not all([name, email, app_password, domain, about, resume]):
        st.error("❌ Please fill in all fields and upload your resume.")
    else:
        selected_hrs = hr_df.sample(n=5)

        resume_data = resume.read()

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email, app_password)

            for _, row in selected_hrs.iterrows():
                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = row['Email']
                msg['Subject'] = f"Internship Inquiry: {domain}"

                body = f"""
Dear {row['HR_Name']},

My name is {name}, and I am writing to express my interest in the {domain} position at {row['Company_Name']}.

{about}

Please find my resume attached. I would be grateful for the opportunity to contribute to your team.

Warm regards,
{name}
Email: {email}
"""
                msg.attach(MIMEText(body, 'plain'))

                part = MIMEApplication(resume_data, Name="resume.pdf")
                part['Content-Disposition'] = 'attachment; filename="resume.pdf"'
                msg.attach(part)

                server.sendmail(email, row['Email'], msg.as_string())
                st.success(f"✅ Email sent to {row['HR_Name']} at {row['Company_Name']}")
                
            server.quit()
            st.balloons()

        except smtplib.SMTPAuthenticationError:
            st.error("❌ Authentication failed. Please make sure App Password is correct.")
        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
