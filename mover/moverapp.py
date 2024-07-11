from flask import Flask, request
import RPi.GPIO as GPIO

app = Flask(__name__)

# GPIO setup
GPIO.setmode(GPIO.BCM)
relays = [17, 18, 27, 22]  # Define your GPIO pins connected to the relays

# Initialize all relays to OFF
for relay in relays:
    GPIO.setup(relay, GPIO.OUT)
    GPIO.output(relay, GPIO.LOW)

@app.route('/set_relay', methods=['POST'])
def set_relay():
    relay = int(request.json['relay'])
    state = GPIO.HIGH if request.json['state'] == 'ON' else GPIO.LOW
    GPIO.output(relays[relay], state)
    return f'Relay {relay + 1} set to {"ON" if state == GPIO.HIGH else "OFF"}', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
