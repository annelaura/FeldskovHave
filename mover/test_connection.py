import streamlit as st
import requests

# Replace this with the IP address and port of your Raspberry Pi Flask server
pi_ip = "192.168.8.100"

# Streamlit app
st.title("Connection Test")

st.write("This app checks the connection to the Raspberry Pi Flask server.")

# Function to check connection to Raspberry Pi
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
ip_address = st.text_input("Enter the IP address of the Raspberry Pi", value=pi_ip)
st.write(f"Your Raspberry Pi is at {ip_address}")

# Button to check connection
if st.button("Check Connection"):
    connection_status = check_connection(ip_address)
    st.write(connection_status)