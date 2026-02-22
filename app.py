import streamlit as st
from resume_processing import extract_and_clean_resume
from model import predict_domain, ats_score, DOMAINS

st.title("Resume Screener")

uploaded_file = st.file_uploader("Upload your resume", type=["txt", "pdf", "png", "jpg", "jpeg"])

if uploaded_file:
    resume_text = extract_and_clean_resume(uploaded_file)
    st.write("Extracted & Cleaned Resume Text:")
    st.write(resume_text)
    predicted_domain = predict_domain(resume_text)
    st.success(f"Predicted Domain: {predicted_domain}")
    # Let user select domain for ATS scoring
    selected_domain = st.selectbox("Select a domain to check ATS score:", DOMAINS, index=DOMAINS.index(predicted_domain) if predicted_domain in DOMAINS else 0)
    score = ats_score(resume_text, selected_domain)
    st.info(f"ATS Score for {selected_domain}: {score} / 100")
