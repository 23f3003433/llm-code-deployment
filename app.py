from flask import Flask, request, jsonify
import os

app = Flask(__name__)
MY_SECRET = os.getenv('SECRET', 'default_secret')

@app.route('/')
def home():
    return "LLM Code Deployment API is running!"

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/api-endpoint', methods=['POST'])
def handle_request():
    data = request.json
    
    # Verify secret
    if data.get('secret') != MY_SECRET:
        return jsonify({"error": "Invalid secret"}), 400

    try:
        email = data.get('email')
        task = data.get('task')
        brief = data.get('brief')
        
        # Simple response
        response = {
            "status": "success", 
            "message": "Request received successfully",
            "email": email,
            "task": task,
            "round": data.get('round', 1)
        }
        
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860, debug=False)