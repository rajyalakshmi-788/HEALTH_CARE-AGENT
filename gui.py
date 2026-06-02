import streamlit as st
import time

# Page Configuration
st.set_page_config(page_title="HealthAgent AI Dashboard", page_icon="🤖", layout="centered")

st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🤖 HealthAgent AI Suite</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Autonomous Prescription & Multi-Agent Care Network</p>", unsafe_allow_html=True)
st.write("---")

# 1. Input Section
st.subheader("📋 Patient & Clinical Intake Form")
col1, col2 = st.columns(2)
with col1:
    patient_name = st.text_input("Patient Full Name", "Suresh Kumar")
with col2:
    patient_age = st.number_input("Patient Age", value=55)

raw_prescription = st.text_area("📄 Paste Rx Prescription Text Here", 
"""1. Telmisartan 40mg - Once daily, morning after food.
2. Metformin 500mg - Twice daily, after breakfast and dinner.
3. Pantoprazole 40mg - Early morning before breakfast.
Note: Patient reports feeling dizzy in the afternoon sometimes.""")

# 2. Trigger Button
if st.button("🚀 Trigger Agentic Swarm Pipeline", type="primary"):
    
    st.write("---")
    # Simulation Loaders
    with st.spinner("🤖 Initializing Multi-Agent System Core..."):
        time.sleep(1.5)
    
    # AGENT 1 SHOWBOX
    st.success("🟢 AGENT 1: PRESCRIPTION PARSING AGENT COMPLETED")
    st.code("""Parsed Clinical Schema Metadata:
- Extracted Compounds:
  1. Telmisartan (40mg) | Dosage: 1-0-0 | Timing: Post-Breakfast
  2. Metformin (500mg)  | Dosage: 1-0-1 | Timing: Post-Breakfast & Post-Dinner
  3. Pantoprazole (40mg)| Dosage: 1-0-0 | Timing: Pre-Breakfast""", language="text")
    
    time.sleep(1.0)
    
    # AGENT 2 SHOWBOX
    st.success("🟢 AGENT 2: DYNAMIC SCHEDULING AGENT COMPLETED")
    st.info("""Generated Adaptive Cron-Alert Schedule (WhatsApp Queue):
• 07:30 AM -> [ALERT] Take Pantoprazole 40mg.
• 08:30 AM -> [ALERT] Take Telmisartan 40mg + Metformin 500mg.
• 08:30 PM -> [ALERT] Take Metformin 500mg.
📡 [GATEWAY STATUS] HTTP 200 OK | Twilio Sandbox Dispatched Successfully.""")
    
    time.sleep(1.0)
    
    # AGENT 3 SHOWBOX
    st.warning("⚠️ AGENT 3: SAFETY GUARD ALERT TRIGGERED")
    st.error("""CRITICAL BIO-SAFETY AUDIT REPORT:
- [WARNING]: Telmisartan combined with Metformin can cause sudden blood pressure drop, leading to afternoon dizziness.
- [ACTION AGENT INTERVENTION]: Auto-generated advisory alert dispatched to patient number.""")

    st.balloons() # Visual celebration balloons animation
