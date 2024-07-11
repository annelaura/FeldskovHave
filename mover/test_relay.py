import streamlit as st
import requests

# Replace this with the IP address and port of your Raspberry Pi Flask server
pi_url = "http://192.168.8.102:5000"
pi_ip = "192.168.8.102"

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
        response = requests.get(f"http://{ip_address}/status")
        if response.status_code == 200:
            print("Successfully connected to the remote server.")
        else:
            print("Failed to connect to the remote server.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace '192.168.1.100' with the actual IP address
check_connection(pi_ip)

# Cleanup message
st.write("Use Ctrl+C in the terminal to stop the app and cleanup GPIO on the Raspberry Pi")