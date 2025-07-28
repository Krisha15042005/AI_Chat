from flask import Blueprint, send_file, session
from database import get_history
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

pdf_bp = Blueprint('pdf', __name__)

@pdf_bp.route('/download', methods=['GET'])
def download_pdf():
    history = get_history(session['chat_id'])
    filepath = "chat_history.pdf"
    c = canvas.Canvas(filepath, pagesize=letter)
    width, height = letter
    y = height - 50

    for item in history:
        c.drawString(30, y, f"User: {item['prompt']}")
        y -= 20
        c.drawString(30, y, f"Bot: {item['response']}")
        y -= 30
        if y < 50:
            c.showPage()
            y = height - 50

    c.save()
    return send_file(filepath, as_attachment=True)
