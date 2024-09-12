# api_integration.py
from flask import Flask, request, jsonify
from core import nlp_processing, code_generation, code_refactoring

app = Flask(__name__)

class APIIntegration:
    def __init__(self, api_key):
        self.nlp_processor = nlp_processing.NLPProcessor(api_key)
        self.code_generator = code_generation.CodeGenerator(api_key)
        self.code_refactor = code_refactoring.CodeRefactor(api_key)

    def setup_routes(self):
        """
        Sets up API routes for external services to use the AI assistant.
        """

        @app.route("/generate_code", methods=["POST"])
        def generate_code():
            """
            API endpoint to generate code based on a description.
            Input: { "description": "description of the code", "language": "python" }
            """
            data = request.json
            description = data.get("description", "")
            language = data.get("language", "python")
            code = self.code_generator.generate_code(description, language)
            return jsonify({"code": code})

        @app.route("/refactor_code", methods=["POST"])
        def refactor_code():
            """
            API endpoint to refactor existing code.
            Input: { "code": "existing code to refactor" }
            """
            data = request.json
            code = data.get("code", "")
            refactored_code = self.code_refactor.refactor_code(code)
            return jsonify({"refactored_code": refactored_code})

    def run_api(self):
        """
        Runs the Flask API server to expose endpoints for the AI assistant.
        """
        self.setup_routes()
        app.run(host="0.0.0.0", port=5000)

# Initialize the APIIntegration with your OpenAI API key and start the API
if __name__ == "__main__":
    api_integration = APIIntegration(api_key="your_openai_api_key")
    api_integration.run_api()
