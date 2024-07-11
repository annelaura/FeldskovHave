import streamlit as st
import requests

# Replace this with the IP address of your Raspberry Pi
pi_url = "http://192.168.1.207:5000"

# Streamlit app
st.title("Relay Test")

# Function to set relay state
def set_relay(relay, state):
    try:
        response = requests.post(f"{pi_url}/set_relay", json={'relay': relay, 'state': state})
        return response.text
    except Exception as e:
        return str(e)

# Relay control checkboxes
relay_states = {}
for i, relay in enumerate([17, 18, 27, 22]):
    relay_states[i] = st.checkbox(f'Activate Relay {i+1}')
    result = set_relay(i, 'ON' if relay_states[i] else 'OFF')
    st.write(f'Relay {i+1} is {"ON" if relay_states[i] else "OFF"} - {result}')

st.write("Use Ctrl+C in the terminal to stop the app and cleanup GPIO on the Raspberry Pi")
