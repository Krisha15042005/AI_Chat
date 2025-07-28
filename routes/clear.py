from flask import Blueprint, session
from database import clear_history

clear_bp = Blueprint('clear', __name__)

@clear_bp.route('/clear', methods=['POST'])
def clear():
    clear_history(session['chat_id'])
    return {'message': 'Chat history cleared'}
