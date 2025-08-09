import streamlit as st
import joblib
import numpy as np
import pandas as pd

# --------------------
# Load the trained model
# --------------------
@st.cache_resource
def load_model():
    return joblib.load("salary_predictor(2).pkl")

model = load_model()

# --------------------
# App Title
# --------------------
st.set_page_config(page_title="Employee Salary Predictor", page_icon="💼")
st.title("💼 Employee Salary Predictor")
st.write("Predict an employee's **Annual & Monthly Salary** based on their Education, Experience, and Job Title.")

# --------------------
# User Inputs
# --------------------
col1, col2 = st.columns(2)

with col1:
    education_input = st.text_input("🎓 Enter Education Level:")
        
with col2:
    experience_input = st.number_input(
        "⏳ Enter Years of Experience:",
        min_value=0.0, step=0.1
    )

job_title_input = st.text_input("💼 Enter Job Title:")

# --------------------
# Prediction
# --------------------
if st.button("🔮 Predict Salary"):
    if st.button("🔮 Predict Salary"):
     if education_input.strip() == "":
        st.warning("⚠️ Please enter an Education Level before predicting.")
     elif job_title_input.strip() == "":
        st.warning("⚠️ Please enter a Job Title before predicting.")
     else:
        # Match preprocessing from training
        log_experience = np.log1p(experience_input)
        user_input = pd.DataFrame(
            [[education_input, log_experience, job_title_input]],
            columns=['Education', 'Log_Experience', 'Job_Title']
        )

        # Predict
        prediction = model.predict(user_input)
        annual_salary = prediction[0]
        monthly_salary = annual_salary / 12

        st.success(f"📅 Estimated Annual Salary: ₹{annual_salary:,.2f}")
        st.info(f"💰 Estimated Monthly Salary: ₹{monthly_salary:,.2f}")

# --------------------
# Footer
# --------------------
st.markdown("---")

