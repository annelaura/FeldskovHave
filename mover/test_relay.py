import streamlit as st
import requests

# Replace this with the IP address and port of your Raspberry Pi Flask server
pi_url = "http://192.168.8.102:5000"

# Streamlit app
st.title("Relay Test")

st.write("This is meant as a simple relay test, and will be replaced with the real app soon TEST")

# Function to send relay state to Raspberry Pi
def set_relay(relay, state):
    try:
        response = requests.post(f"{pi_url}/set_relay", json={'relay': relay, 'state': state})
        return response.text
    except Exception as e:
        return str(e)

# Function to check connection to Raspberry Pi
def check_connection(ip_address):
    try:
        response = requests.get(f"http://{ip_address}/status")
        if response.status_code == 200:
            return "Successfully connected to the remote server."
        else:
            return "Failed to connect to the remote server."
    except Exception as e:
        return f"An error occurred: {e}"

# Define GPIO pins connected to the relays
relay_pins = [17, 18, 27, 22]

# Relay control buttons
for i, pin in enumerate(relay_pins):
    if st.button(f'Activate Relay {i+1}'):
        result = set_relay(pin, 'ON')
        st.write(f'Relay {i+1} (GPIO Pin {pin}) is ON - {result}')
    else:
        result = set_relay(pin, 'OFF')
        st.write(f'Relay {i+1} (GPIO Pin {pin}) is OFF - {result}')

# Input for IP address
ip_address = st.text_input("Enter the IP address of the Raspberry Pi", value="192.168.8.102")

# Button to check connection
if st.button("Check Connection"):
    connection_status = check_connection(ip_address)
    st.write(connection_status)

# Cleanup message
st.write("Use Ctrl+C in the terminal to stop the app and cleanup GPIO on the Raspberry Pi")
