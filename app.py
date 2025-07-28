from flask import Flask, render_template, session
from routes.chat import chat_bp
from routes.history import history_bp
from routes.clear import clear_bp
from routes.pdf_download import pdf_bp
from database import init_db
import uuid

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.before_request
def assign_chat_id():
    if 'chat_id' not in session:
        session['chat_id'] = str(uuid.uuid4())

app.register_blueprint(chat_bp)
app.register_blueprint(history_bp)
app.register_blueprint(clear_bp)
app.register_blueprint(pdf_bp)

init_db()

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
