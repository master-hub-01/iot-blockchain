from flask import request
import hashlib

# IoT Data Storage in Blockchain
@app.route('/add_iot_data', methods=['POST'])
def add_iot_data():
    data = request.json
    if not data or 'device_id' not in data or 'sensor_data' not in data:
        return jsonify({'message': 'Invalid IoT data'}), 400

    # Encrypt data using SHA-256 (or implement AES for stronger encryption)
    encrypted_data = hashlib.sha256(str(data).encode()).hexdigest()

    # Add the data as a transaction to blockchain
    previous_block = blockchain.get_previous_block()
    new_block = blockchain.create_block(proof=1, previous_hash=previous_block['hash'])
    new_block['data'] = encrypted_data

    return jsonify({'message': 'IoT Data added to Blockchain', 'block': new_block}), 201

