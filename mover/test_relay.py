import streamlit as st
import requests

# Replace this with the IP address and port of your Raspberry Pi Flask server
pi_url = "http://192.168.8.100:5000"

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

# Define GPIO pins connected to the relays
relay_pins = [17, 18, 27, 22]

# Relay control checkboxes
relay_states = {}
for i, pin in enumerate(relay_pins):
    relay_states[pin] = st.checkbox(f'Activate Relay {i+1}')
    result = set_relay(pin, 'ON' if relay_states[pin] else 'OFF')
    st.write(f'Relay {i+1} (GPIO Pin {pin}) is {"ON" if relay_states[pin] else "OFF"} - {result}')

def check_connection(ip_address):
    try:
        response = requests.get(f"http://{ip_address}:5000/status")
        if response.status_code == 200:
            return "Successfully connected to the remote server."
        else:
            return "Failed to connect to the remote server."
    except Exception as e:
        return f"An error occurred: {e}"

# Input for IP address
ip_address = st.text_input("Enter the IP address of the Raspberry Pi", value="192.168.8.100")

# Button to check connection
if st.button("Check Connection To Pi"):
    connection_status = check_connection(ip_address)
    st.write(connection_status)

# Cleanup message
st.write("Use Ctrl+C in the terminal to stop the app and cleanup GPIO on the Raspberry Pi")
