# mock_gpio.py

class MockGPIO:
    BCM = "BCM"
    OUT = "OUT"
    HIGH = "HIGH"
    LOW = "LOW"

    def setmode(self, mode):
        pass

    def setup(self, pin, mode):
        pass

    def output(self, pin, state):
        pass

    def cleanup(self):
        pass

GPIO = MockGPIO()
