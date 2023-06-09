from flask import Blueprint, request, jsonify, render_template
from app.utils.openai import generate_message
from app.utils.templates import load_template

chat_blueprint = Blueprint('chat', __name__)

@chat_blueprint.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        data = request.get_json()
        if data is None:
            data = request.form

        if 'template' not in data or 'message' not in data:
            return jsonify({'error': 'La solicitud debe incluir un nombre de plantilla y un mensaje'}), 400

        template_name = data.get('template')
        template_text = load_template(template_name)
        if "error" in template_text:
            return jsonify({'error': f'Error al cargar la plantilla: {template_text}'}), 500

        message = data.get('message')
        try:
            response = generate_message(template_text + " " + message)
            if request.is_json:
                return {'response': response}
            else:
                return render_template('chat.html', response=response)

        except Exception as exception:
            return jsonify({'error': 'Error al generar la respuesta: ' + str(exception)}), 500

    else:
        return render_template('chat.html')

@chat_blueprint.route('/guy', methods=['GET'])
def gui():
    return render_template('chat.html')