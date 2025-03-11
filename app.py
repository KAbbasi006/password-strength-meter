import re
import random
import string
import streamlit as st


# 🎯 Blacklisted Common Passwords
BLACKLISTED_PASSWORDS = {
    "password", "password123", "123456", "12345678", "qwerty", 
    "abc123", "letmein", "welcome", "admin", "iloveyou"
}

# 🎯 Generate a Strong Random Password
def generate_strong_password(length=12):
    """Generates a strong password with uppercase, lowercase, digits, and special characters."""
    all_characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# 🎯 Password Strength Checker
def check_password_strength(password):
    score = 0
    feedback = []

    # ❌ Reject Blacklisted Passwords
    if password.lower() in BLACKLISTED_PASSWORDS:
        return "❌ **This password is too common! Please choose a stronger one.**", feedback

    # ✅ Length Check
    if len(password) >= 12:
        score += 2  # Higher weight for longer passwords
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # ✅ Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 2
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # ✅ Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # ✅ Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 2
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # 🔥 Strength Rating Based on Custom Weights
    if score >= 6:
        return "✅ **Strong Password!** 💪", feedback
    elif score >= 4:
        return "⚠️ **Moderate Password - Consider adding more security features.**", feedback
    else:
        return "❌ **Weak Password - Improve it using the suggestions below.**", feedback

# 🌟 Streamlit 
st.set_page_config(page_title = "Password Strength Meter", layout= "centered")
st.title("🔐 Password Strength Meter")
st.write("Enter a password below to check its strength or generate a strong one.")

password = st.text_input("Enter Password:", type="password")

# 🔘 Check Password Strength
if password:
    result, suggestions = check_password_strength(password)
    st.markdown(result)
    
    if suggestions:
        st.subheader("💡 Suggestions to Improve:")
        for suggestion in suggestions:
            st.write("- " + suggestion)

# 🔘 Generate a Strong Password
if st.button("🔄 Generate a Strong Password"):
    new_password = generate_strong_password()
    st.success(f"💡 **Suggested Password:** `{new_password}`")
