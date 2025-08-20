# -*- coding: utf-8 -*-
import streamlit as st

# ---------- App Title ----------
st.title("📱 Digital Stress Scale Web App")
st.write("""
**Developer:** Amna Khan – Clinical Psychologist, Researcher, and Data Analyst

Welcome! This bilingual (Urdu + English) app will help you assess your digital stress level.
Please complete the payment to unlock the full assessment.
""")

# ---------- Introduction ----------
st.markdown("""
### Introduction
This tool is based on the **Multidimensional Digital Stressor Scale (MDSS)**.
It is designed **only** for individuals aged **18 to 30 years**.
It diagnoses the **level of digital stress** you may be experiencing due to usage of devices such as mobile phones, laptops, and social media.

⚠️ **Important Notes:**
- This tool specifically measures **digital stress**, not other types of stress.
- It does **not** assess professional or work-related stress caused by using devices for your job or study.
- Please answer all questions honestly based on your experience in the **past 7 days**.
- While it is a diagnostic tool for digital stress, it should be used for **awareness and guidance**, not as a substitute for professional medical or psychological evaluation.
""")

# ---------- Part 1: Sample Questions ----------
st.subheader("Sample Questions")
sample_items = [
    ("Most of my friends approve of me being constantly available online",
     "میرے زیادہ تر دوست میرے مسلسل آن لائن رہنے سے متفق ہیں"),
    ("I feel a social obligation to be constantly available online",
     "مسلسل آن لائن رہنا مجھے ایک سماجی ذمہ داری محسوس ہوتا ہے")
]
scale_labels = ["0 - Strongly Disagree", "1 - Disagree", "2 - Neutral", "3 - Agree", "4 - Strongly Agree"]

for idx, item in enumerate(sample_items, 1):
    st.markdown(f"**Q{idx}. {item[0]}**  \n_{item[1]}_")
    st.radio("", scale_labels, key=f"sample_{idx}")

# ---------- Payment Verification ----------
if 'payment_verified' not in st.session_state:
    st.session_state['payment_verified'] = False

st.subheader("💳 Payment Verification")
st.write("Enter the transaction code you received after payment:")

transaction_code = st.text_input("Transaction Code")

if st.button("Verify Payment"):
    # Simulate verification
    if transaction_code == "EASY1234":  # replace with your actual code for demo
        st.session_state['payment_verified'] = True
        st.success("✅ Payment Verified Successfully! You can now take the full assessment.")
    else:
        st.error("❌ Invalid transaction code. Please try again.")

# ---------- Full Assessment ----------
if st.session_state['payment_verified']:
    st.subheader("📝 Full Digital Stress Assessment")
    
    digital_stress_items = [
        {"id": 1, "en_text": "Most of my friends approve of me being constantly available online", "ur_text": "میرے زیادہ تر دوست میرے مسلسل آن لائن رہنے سے متفق ہیں"},
        {"id": 2, "en_text": "I feel a social obligation to be constantly available online", "ur_text": "مسلسل آن لائن رہنا مجھے ایک سماجی ذمہ داری محسوس ہوتا ہے"},
        {"id": 3, "en_text": "I am nervous about how people will respond to my posts and photos", "ur_text": "میں پریشان ہوتا ہوں کہ لوگ میرے پوسٹ اور تصویر کا کس طرح سے جواب دیں گے؟"},
        {"id": 4, "en_text": "I feel anxious about how others will respond when I share a new photo on social media", "ur_text": "میری طرف سے سوشل میڈیا پر کوئی نئی تصویر شیئر کی جاتی ہے تو مجھے بیچینی ہوتی ہے کہ دوسرے کیسے جواب دیں گے؟"},
        # ... add more questions ...
    ]

    responses = []
    for item in digital_stress_items:
        st.markdown(f"**Q{item['id']}. {item['en_text']}**  \n_{item['ur_text']}_")
        score = st.radio("", scale_labels, key=f"q{item['id']}")
        responses.append(int(score.split(" - ")[0]))

    if st.button("Submit Full Assessment"):
        total_score = sum(responses)
        st.write(f"**Your total digital stress score is: {total_score}**")
        
        if total_score <= 21:
            st.info("Low digital stress")
        elif total_score <= 44:
            st.info("Moderate digital stress")
        elif total_score <= 66:
            st.warning("Elevated digital stress")
        else:
            st.error("High digital stress")
else:
    st.info("🔒 Full assessment is locked. Complete payment to unlock it.")
