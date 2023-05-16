from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .routes import chat as chat_blueprint
    app.register_blueprint(chat_blueprint)

    return app