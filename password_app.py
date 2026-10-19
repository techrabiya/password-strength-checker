import streamlit as st
import re

st.title("🔒 Password Strength Checker")

password = st.text_input("Enter your password", type="password")

if password:
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r"[@$!%*?&]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (@$!%*?&).")

    if score == 4:
        st.success("Strong Password! 🟢")
    elif score >= 2:
        st.warning("Moderate Password. 🟡 Consider making it stronger.")
    else:
        st.error("Weak Password. 🔴 Please follow the suggestions below:")

    for item in feedback:
        st.write(f"- {item}")
