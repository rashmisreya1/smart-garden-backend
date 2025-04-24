# smart-garden-backend
Backend for Automatic Garden System with Soil Moisture Monitoring
## 📁 Backend Setup

### 1. API Receiver (Flask)
File: `backend/api_receiver.py`

- Runs a server on port 5000 to receive moisture data
- Stores or processes data as needed

### 2. Data Sender
File: `backend/send_to_backend.py`

- Reads moisture values from serial (Arduino/Raspberry Pi)
- Sends it to the Flask API every 5 seconds

