import streamlit as st
import pywhatkit as kit
import webbrowser as web
# Title for the Streamlit app
st.title("PyWhatKit Integration with Streamlit")

# Get user input for WhatsApp message
message = st.text_input("Enter the message you want to send on WhatsApp")

# Get user input for phone number
phone_number = st.text_input("Enter the phone number (with country code)")

# Get user input for time (optional)
hour = st.number_input("Enter the hour", min_value=0, max_value=23)
minute = st.number_input("Enter the minute", min_value=0, max_value=59)

# Button to send WhatsApp message
if st.button("Send WhatsApp Message"):
    # Send WhatsApp message using PyWhatKit
    kit.sendwhatmsg(phone_number, message, hour, minute)
    st.success("WhatsApp message sent successfully!")
