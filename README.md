# Proyecto ChatGPT

Este proyecto tiene como objetivo proporcionar una interfaz de chat fácil de usar con la API GPT-4 (o el algoritmo que desees) de OpenAI. Permite a los usuarios obtener respuestas generadas por inteligencia artificial a consultas de texto que se basan en una serie de prompts o instrucciones predefinidos, llamados "templates". Esto permite tener un control más preciso sobre el tipo de respuestas que el modelo de IA genera, haciendo que la conversación sea más coherente y útil.

## Funcionalidad Principal

La funcionalidad principal de este proyecto es transformar prompts o instrucciones específicos en respuestas generadas por IA. Cada prompt o instrucción se basa en un "template" que determina la estructura y el estilo de la respuesta generada.

Por ejemplo, si tu template se estructura como un informe diario de trabajo, puedes introducir un texto en bruto que describa tus actividades del día, y la aplicación generará una respuesta que encaje en el formato de un informe diario de trabajo.

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
   curl -X POST -H "Content-Type: application/json" -d '{"message":"Hola Mundo", "template_name":"daily"}' http://127.0.0.1:5000/chat
   ```

4. También puedes interactuar con el chatbot a través de la interfaz gráfica del usuario visitando `http://localhost:5000/gui` en tu navegador.

## Licencia

Este proyecto se encuentra bajo la [licencia MIT](https://opensource.org/licenses/MIT).
