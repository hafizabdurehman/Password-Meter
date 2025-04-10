import streamlit as st
import re
import random
import string

def check_password_strength(password):

    score = 0

    feedback = []
    
    # Length Check

    if len(password) >= 8:

        score += 1

    else:

        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):

        score += 1

    else:

        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check

    if re.search(r"\d", password):

        score += 1

    else:

        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check

    if re.search(r"[!@#$%^&*]", password):

        score += 1

    else:

        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Common password check

    common_passwords = ["password", "123456", "qwerty", "admin", "welcome", "password123"]

    if password.lower() in common_passwords:

        score = 0

        feedback.append("❌ This is a commonly used password and is very insecure!")
    
    # Strength Determination

    strength = ""

    if score == 4:

        strength = "Strong"

        feedback = ["✅ Strong Password!"]

    elif score == 3:

        strength = "Moderate"

        feedback.append("⚠️ Moderate Password - Consider adding more security features.")

    else:

        strength = "Weak"

        feedback.append("❌ Weak Password - Improve it using the suggestions above.")
        
    return score, strength, feedback

def generate_strong_password():

    # Generate a strong password

    length = random.randint(12, 16)
    
    # Ensure all character types are included

    lowercase = random.choice(string.ascii_lowercase)

    uppercase = random.choice(string.ascii_uppercase)

    digit = random.choice(string.digits)

    special_char = random.choice("!@#$%^&*")
    
    # Fill the rest of the password with random characters

    remaining_length = length - 4

    remaining_chars = ''.join(random.choices(

        string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*",
        k=remaining_length
    ))
    
    # Combine all parts and shuffle

    all_chars = lowercase + uppercase + digit + special_char + remaining_chars

    password_chars = list(all_chars)

    random.shuffle(password_chars)
    
    return ''.join(password_chars)

# Setup Streamlit UI

st.set_page_config(

    page_title="Password Strength Meter",

    page_icon="🔐",

    layout="centered"
)

# Application title

st.title("🔐 Password Strength Meter")

st.markdown("Check how strong your password is and get suggestions to improve it.")

# Input field for password

password = st.text_input("Enter your password:", type="password", key="password_input")

# Create placeholder for results that will update in real-time

results_placeholder = st.empty()

# Generate password button

if st.button("Generate Strong Password"):

    suggested_password = generate_strong_password()

    st.code(suggested_password, language=None)

    st.info("Copy this password and use it for better security!")

# Real-time password checking

if password:

    score, strength, feedback = check_password_strength(password)
    
    # Update the placeholder with current results

    with results_placeholder.container():

        # Display score visually

        st.subheader("Password Strength:")
        
        # Create a colored progress bar based on the strength

        if strength == "Strong":

            st.progress(1.0)

            st.success(f"Strength: {strength} (Score: {score}/4)")

        elif strength == "Moderate":

            st.progress(0.75)

            st.warning(f"Strength: {strength} (Score: {score}/4)")

        else:

            st.progress(0.4)

            st.error(f"Strength: {strength} (Score: {score}/4)")
        
        # Display feedback

        st.subheader("Feedback:")

        for item in feedback:

            st.markdown(item)
            
        # Requirements reminder

        if strength != "Strong":
            
            st.subheader("Requirements for a Strong Password:")
            st.markdown("✅ At least 8 characters long")
            st.markdown("✅ Contains uppercase & lowercase letters")
            st.markdown("✅ Includes at least one digit (0-9)")
            st.markdown("✅ Has one special character (!@#$%^&*)")

# Display password criteria

with st.expander("See Password Guidelines"):

    st.markdown("""
    ## Password Strength Criteria
    A strong password should:
    - Be at least 8 characters long
    - Contain uppercase & lowercase letters
    - Include at least one digit (0-9)
    - Have one special character (!@#$%^&*)
    """)

# Footer
st.markdown("---")

st.markdown("*Made by Tayyab Aziz*")