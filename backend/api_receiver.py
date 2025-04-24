# api_receiver.py

from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] Received data: {data}")
    
    # TODO: Add code to save data to a database or file

    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
