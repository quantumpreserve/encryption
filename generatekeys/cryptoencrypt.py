from flask import Flask, request, jsonify
from cryptography.fernet import Fernet

app = Flask(__name__)

# Function to generate a Fernet key (simulation of quantum key)
def generate_key():
    return Fernet.generate_key().decode()

# Simulated encryption
def encrypt(file_content, key):
    cipher = Fernet(key.encode())
    return cipher.encrypt(file_content.encode()).decode()

# Simulated decryption
def decrypt(encrypted_content, key):
    cipher = Fernet(key.encode())
    return cipher.decrypt(encrypted_content.encode()).decode()

@app.route('/generate-key', methods=['GET'])
def generate_key_endpoint():
    key = generate_key()
    return jsonify({"key": key})

@app.route('/encrypt', methods=['POST'])
def encrypt_file():
    try:
        data = request.json
        if 'file_content' not in data or 'key' not in data:
            return jsonify({"error": "Missing required fields: 'file_content' and 'key'"}), 400
        encrypted_data = encrypt(data['file_content'], data['key'])
        return jsonify({"encrypted_data": encrypted_data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/decrypt', methods=['POST'])
def decrypt_file():
    try:
        data = request.json
        if 'encrypted_content' not in data or 'key' not in data:
            return jsonify({"error": "Missing required fields: 'encrypted_content' and 'key'"}), 400
        decrypted_data = decrypt(data['encrypted_content'], data['key'])
        return jsonify({"decrypted_data": decrypted_data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
