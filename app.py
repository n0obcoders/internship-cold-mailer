import streamlit as st

st.title("🚀 Internship Cold Email Sender")
if st.button("🌐 Visit My Portfolio"):
    st.markdown("Redirecting...")
    st.markdown("[Click here if not redirected](https://portfolio-n0obcoders-projects.vercel.app/)", unsafe_allow_html=True)

name = st.text_input("Enter your full name")
email = st.text_input("Enter your Gmail ID")
password = st.text_input("Enter your Gmail App Password", type="password")

domain = st.selectbox("Choose your internship domain", [
    "Cyber Security Intern", "Graphic Designer Intern", "Frontend Developer Intern",
    "Backend Developer Intern", "Data Science Intern", "DevOps Intern",
    "Machine Learning Intern", "Blockchain Developer Intern", "Cloud Computing Intern",
    "Android Developer Intern", "Web Developer Intern", "Digital Marketing Intern"
])

about_you = st.text_area("Tell us about yourself")
resume = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
if st.checkbox("Preview email"):
    st.write(f"**To:** Random HRs\n\n**Subject:** Internship Inquiry: {domain}\n\nDear HR,\n\nMy name is {name}...")
if st.button("Send Emails"):
    if all([name, email, password, about_you, resume]):
        # Process and send emails
        st.success("✅ Emails sent to 5 HRs!")
    else:
        st.warning("Please fill all fields and upload your resume.")
