 
from flask import Flask, jsonify, request
import time

app = Flask(__name__)  # Creating a Flask app

# Blockchain Data Storage (Temporary)
blockchain = []

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Secure IoT Blockchain API!"})

@app.route('/add_iot_data', methods=['POST'])
def add_iot_data():
    data = request.get_json()
    
    if not data or "device_id" not in data or "sensor_data" not in data:
        return jsonify({"message": "Invalid data"}), 400

    transaction = {
        "device_id": data["device_id"],
        "sensor_data": data["sensor_data"],
        "timestamp": time.time()
    }

    blockchain.append(transaction)

    return jsonify({"message": "IoT Data added to blockchain", "data": transaction}), 201

@app.route('/get_chain', methods=['GET'])
def get_chain():
    return jsonify({"chain": blockchain, "length": len(blockchain)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
