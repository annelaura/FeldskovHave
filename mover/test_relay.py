import streamlit as st
import requests

# Replace this with the IP address and port of your Raspberry Pi Flask server
pi_url = "http://192.168.1.207:5000"

# Streamlit app
st.title("Relay Test")

st.write("This is meant as a simple relay test, and will be replaced with the real app soon")

# Function to send relay state to Raspberry Pi
def set_relay(relay, state):
    try:
        response = requests.post(f"{pi_url}/set_relay", json={'relay': relay, 'state': state})
        return response.text
    except Exception as e:
        return str(e)

# Relay control checkboxes
relay_states = {}
for i, relay in enumerate([17, 18, 27, 22]):
    relay_states[relay] = st.checkbox(f'Activate Relay {i+1}')
    result = set_relay(relay, 'ON' if relay_states[relay] else 'OFF')
    st.write(f'Relay {i+1} (GPIO Pin {relay}) is {"ON" if relay_states[relay] else "OFF"} - {result}')

# Cleanup message
st.write("Use Ctrl+C in the terminal to stop the app and cleanup GPIO on the Raspberry Pi")
