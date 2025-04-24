# send_to_backend.py

import requests
import time
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)  # Adjust port as needed

def send_data(moisture_value):
    payload = {
        "moisture": moisture_value,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    response = requests.post("http://localhost:5000/api/data", json=payload)
    print(f"Data sent, response: {response.status_code}")

while True:
    if ser.in_waiting:
        moisture = ser.readline().decode().strip()
        print("Sending:", moisture)
        send_data(moisture)
        time.sleep(5)
