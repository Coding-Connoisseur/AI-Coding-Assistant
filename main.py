# main.py
from flask import Flask, request, jsonify
from core.nlp_processing import NLPProcessor
from core.code_generation import CodeGenerator
from core.code_refactoring import CodeRefactor
from integrations.cli_integration import CLIIntegration
from integrations.api_integration import APIIntegration
from config.settings import Settings
import os
import argparse

app = Flask(__name__)

# Initialize components with OpenAI API Key from environment variables
api_key = os.getenv("OPENAI_API_KEY", "your_openai_api_key")
nlp_processor = NLPProcessor(api_key)
code_generator = CodeGenerator(api_key)
code_refactor = CodeRefactor(api_key)
settings = Settings()

# CLI Integration
cli_integration = CLIIntegration(api_key)

@app.route('/')
def home():
    return "Welcome to the AI Coding Assistant API"

@app.route('/generate_code', methods=['POST'])
def generate_code():
    """
    Endpoint to generate code based on user input.
    Expected payload: { "description": "Create a function to add two numbers", "language": "python" }
    """
    data = request.json
    description = data.get("description", "")
    language = data.get("language", "python")
    code = code_generator.generate_code(description, language)
    return jsonify({"code": code})

@app.route('/refactor_code', methods=['POST'])
def refactor_code():
    """
    Endpoint to refactor the provided code for optimization and readability.
    Expected payload: { "code": "original_code_string" }
    """
    data = request.json
    original_code = data.get("code", "")
    refactored_code = code_refactor.refactor_code(original_code)
    return jsonify({"refactored_code": refactored_code})

@app.route('/test_code', methods=['POST'])
def test_code():
    """
    Endpoint to run the provided code and return the output or any errors.
    Expected payload: { "code": "code_to_test" }
    """
    data = request.json
    test_code = data.get("code", "")
    try:
        exec_globals = {}
        exec(test_code, {}, exec_globals)
        result = exec_globals
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Coding Assistant")
    subparsers = parser.add_subparsers(dest="command")

    # Subparser for the generate command
    generate_parser = subparsers.add_parser("generate", help="Generate code")
    generate_parser.add_argument("description", type=str, help="Description of the code to generate")
    generate_parser.add_argument("language", type=str, help="Programming language", default="python")

    # Subparser for the refactor command
    refactor_parser = subparsers.add_parser("refactor", help="Refactor code")
    refactor_parser.add_argument("code", type=str, help="Code to refactor")

    # Subparser for the test command
    test_parser = subparsers.add_parser("test", help="Test code")
    test_parser.add_argument("code", type=str, help="Code to test")

    args = parser.parse_args()

    if args.command == "generate":
        description = args.description
        language = args.language
        code = code_generator.generate_code(description, language)
        print(code)
    elif args.command == "refactor":
        original_code = args.code
        refactored_code = code_refactor.refactor_code(original_code)
        print(refactored_code)
    elif args.command == "test":
        test_code = args.code
        try:
            exec_globals = {}
            exec(test_code, {}, exec_globals)
            result = exec_globals
            print(result)
        except Exception as e:
            print(f"Error: {str(e)}")
    else:
        # Run the Flask API server
        app.run(host="0.0.0.0", port=5000)
