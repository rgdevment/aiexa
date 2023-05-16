from flask import request, jsonify
from . import chat
from ..utils.openai import generate_message

@chat.route('/chat', methods=['POST'])
def chat():
    message = request.json.get('message', '')
    response = generate_message(message)
    return jsonify(response=response)