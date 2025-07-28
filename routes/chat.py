from flask import Blueprint, request, jsonify, session
from cohere_handler import generate_with_cohere
from database import save_message

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    response = generate_with_cohere(prompt)
    save_message(session['chat_id'], prompt, response)
    return jsonify({'response': response})
