from flask import Blueprint, jsonify, session
from database import get_history

history_bp = Blueprint('history', __name__)

@history_bp.route('/history', methods=['GET'])
def history():
    history = get_history(session['chat_id'])
    return jsonify(history)
