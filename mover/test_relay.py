import streamlit as st
import time

# Try importing the RPi.GPIO library, and fallback to mock GPIO if not available
try:
    import RPi.GPIO as GPIO
except (ImportError, RuntimeError):
    from mock_gpio import GPIO

# GPIO setup
GPIO.setmode(GPIO.BCM)
relays = [17, 18, 27, 22]  # Define your GPIO pins connected to the relays

# Initialize all relays to OFF
for relay in relays:
    GPIO.setup(relay, GPIO.OUT)
    GPIO.output(relay, GPIO.LOW)

# Streamlit app
st.title("Relay Test")

# Function to set relay state
def set_relay(relay, state):
    GPIO.output(relay, state)

# Relay control checkboxes
relay_states = {}
for i, relay in enumerate(relays):
    relay_states[i] = st.checkbox(f'Activate Relay {i+1}')
    set_relay(relay, GPIO.HIGH if relay_states[i] else GPIO.LOW)
    st.write(f'Relay {i+1} is {"ON" if relay_states[i] else "OFF"}')

# Cleanup on exit
st.write("Use Ctrl+C in the terminal to stop the app and cleanup GPIO")
try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
