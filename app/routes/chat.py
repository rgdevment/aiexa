from flask import Blueprint, request
from app.utils.openai import generate_message

chat_blueprint = Blueprint('chat', __name__)

@chat_blueprint.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '')
    response = generate_message(message)
    return {'response': response}