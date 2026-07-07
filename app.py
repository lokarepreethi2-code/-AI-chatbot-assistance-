import os
from flask import Flask, request, jsonify
from datetime import datetime
from anthropic import Anthropic

app = Flask(__name__)
# Task 5: Store conversation history
conversation_history = []

# --- AI Model client setup ---
# Reads the API key from an environment variable (never hardcode keys in code!)
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
AI_MODEL = "claude-sonnet-4-6"


# 1. Send Prompt to AI (/api/chat)
@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'prompt' not in data:
        return jsonify({"status": "error", "message": "Missing prompt"}), 400

    user_prompt = data.get('prompt')

    try:
        # --- Real AI Model call (replaces the old mock logic) ---
        message = client.messages.create(
            model=AI_MODEL,
            max_tokens=1000,
            messages=[
                {"role": "user", "content": user_prompt}
            ]
        )
        ai_response = message.content[0].text
        # Task 5: Save prompt and response to history
        chat_turn = {
            "question": user_prompt,
            "answer": ai_response
        }
        conversation_history.append(chat_turn)

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"AI model request failed: {str(e)}"
        }), 502

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
    ai_status = "operational" if os.environ.get("ANTHROPIC_API_KEY") else "not_configured"
    return jsonify({
        "status": "healthy",
        "services": {
            "database": "connected",
            "ai_engine": ai_status
        }
    }), 200
# Task 5: Endpoint to retrieve conversation history
@app.route('/api/history', methods=['GET'])
def get_history():
    return jsonify({
        "status": "success",
        "history": conversation_history
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
