# Proyecto Yitipi

¡Hola! Aunque no soy un programador de Python, decidí sumergirme en esta aventura como un nuevo hobby para mantenerme activo y aprender algo nuevo. Es mi primer contacto con el lenguaje y, aunque aún estoy aprendiendo, si este proyecto ayuda aunque sea a una persona, me sentiré más que satisfecho.

Yitipi es una aventura que he iniciado con el objetivo de desarrollar una API que pueda dialogar con otro proyecto en proceso, llamado "Aiexa". Aiexa está diseñado para trabajar con ChatGPT en Alexa. Sin embargo, como Aiexa aún está en las primeras etapas de desarrollo, Yitipi no se queda de brazos cruzados.

En su versión actual, Yitipi es una interfaz de chat fácil de usar con la API GPT-3.5 (o cualquier otro algoritmo que prefieras) de OpenAI. Permite a los usuarios obtener respuestas generadas a partir de consultas de texto, que se basan en una serie de instrucciones o "prompts" predefinidos, a los que nos referimos como "templates". Así, puedes tener un control más preciso sobre el tipo de respuestas que genera el modelo de IA, manteniendo la conversación coherente y útil.

## Funcionalidad Principal

El corazón de este proyecto es convertir prompts específicos en respuestas generadas por IA. Cada prompt se basa en un "template" que moldea la estructura y el estilo de la respuesta generada.

Para poner un ejemplo sencillo, digamos que tienes un template estructurado como un informe diario de trabajo. Si introduces un texto en bruto que describe tus actividades del día, la aplicación generará una respuesta que se ajuste al formato de dicho informe. ¡Así de fácil!

## Requisitos

- Python 3.6+
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [OpenAI Python](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_generate_text_with_GPT3_or_Davinci_Codex.md)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

Estas dependencias se pueden instalar ejecutando:

```bash
pip install -r requirements.txt
```

## Configuración

1. Clona este repositorio en tu máquina local.
2. Crea un archivo `.env` en el directorio raíz del proyecto y añade tu clave de API de OpenAI. Debería verse algo así:

   ```
   OPENAI_KEY=your-openai-key-here
   ```

## Uso

1. Inicia la aplicación Flask ejecutando `python run.py`.
2. La aplicación estará disponible en `http://localhost:5000`.
3. Para enviar una solicitud de chat a la API, realiza una solicitud POST a `http://localhost:5000/chat` con un cuerpo JSON que contenga un campo `message` y un campo `template_name`. Por ejemplo:

   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"message":"Una idea para un buen template", "template_name":"daily"}' http://127.0.0.1:5000/chat
   ```

4. También puedes interactuar con el chatbot a través de la interfaz gráfica del usuario visitando `http://localhost:5000/guy` en tu navegador.