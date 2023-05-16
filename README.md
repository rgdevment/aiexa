
# IN PROGRESS
This project is still a baby. It sprouted from a spark of an idea, providing just a basic template and simple communication for now. We have heaps of development and growth ahead, so some things might not be quite up to speed yet. But with every change we make, we're taking one step closer to our goal. So, thanks for your patience and feedback! Together, we're going to help this little project grow up and reach its full potential.

# ChatGPT API with Alexa

This project integrates OpenAI's GPT-3 model with an Alexa Skill to create an interactive and engaging conversational agent. The application is written in Python using Flask for the API and the OpenAI API to interface with GPT-3.

## Getting Started

### Prerequisites

- Python 3.8 or later
- Conda package manager
- OpenAI API key

### Installation

1. Clone the repository
2. Navigate to the project directory and create a new Conda environment: conda create --name myenv python=3.8
3. Activate the Conda environment: conda activate myenv
4. Install the required dependencies: pip install -r requirements.txt
5. move a `.env.dist` file to `.env` and add your OpenAI API key: OPENAI_KEY=YOUR-KEY_OPENIA

## Running the Application

To run the application, execute the following command in the root of your project: `python run.py` 

The Flask server will start and listen for incoming connections. You can now use the API endpoint (`http://localhost:5000/chat`) to communicate with the GPT-3 model.

## Author

Mario Hidalgo G.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details