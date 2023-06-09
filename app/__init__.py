from flask import Flask
from .routes.chat import chat_blueprint

def create_app():
    app = Flask(__name__, template_folder='views')
    app.register_blueprint(chat_blueprint)

    return app
