from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# 1. Send Prompt to AI (/api/chat)
@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'prompt' not in data:
        return jsonify({"status": "error", "message": "Missing prompt"}), 400
    
    user_prompt = data.get('prompt')
    
    # Mock AI response logic
    ai_response = f"This is a mock AI response to your prompt: '{user_prompt}'"
    
    return jsonify({
        "status": "success",
        "response": ai_response,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }), 200

# 2. Retrieve Conversations (/api/history)
@app.route('/api/history', methods=['GET'])
def history():
    return jsonify({
        "user_id": "user_12345",
        "history": [
            {"role": "user", "text": "Hello!"},
            {"role": "assistant", "text": "Hi there! How can I help you today?"}
        ]
    }), 200

# 3. Fetch User Information (/api/users)
@app.route('/api/users', methods=['GET'])
def users():
    return jsonify({
        "user_id": "user_12345",
        "username": "lokarepreethi2",
        "email": "preethi@example.com"
    }), 200

# 4. Store Ratings (/api/feedback)
@app.route('/api/feedback', methods=['POST'])
def feedback():
    return jsonify({
        "status": "feedback_saved",
        "message": "Thank you for your rating."
    }), 201

# 5. Health Check (/api/health)
@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "services": {
            "database": "connected",
            "ai_engine": "operational"
        }
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
s
