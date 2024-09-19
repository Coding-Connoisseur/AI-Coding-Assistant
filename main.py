# main.py
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from core.nlp_processing import NLPProcessor
from core.code_generation import CodeGenerator
from core.code_refactoring import CodeRefactor
from integrations.cli_integration import CLIIntegration
from integrations.api_integration import APIIntegration
from config.settings import Settings
import os
import re
import sys
import io


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback_key_for_dev')
socketio = SocketIO(app)

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
    return render_template('index.html')  # Rendering the frontend page

def clean_code_response(response_text):
    """
    Extract code from the response by looking for code blocks or stripping explanations.
    """
    # Regex to capture everything inside a Python code block or other language code block.
    code_match = re.search(r"```(?:\w+)?\n([\s\S]+?)\n```", response_text)

    if code_match:
        # If there's a match, return the code part only
        return code_match.group(1).strip()

    # If no code block found, assume the whole response is code (fallback)
    return response_text.strip()

# In your Flask API (when generating code)
@app.route('/generate_code', methods=['POST'])
def generate_code():
    data = request.json
    description = data.get("description", "")
    language = data.get("language", "python")

    # Generate code using your AI model (replace this with actual call to your model)
    raw_response = code_generator.generate_code(description, language)
    
    # Clean the raw response to extract only the code
    clean_code = clean_code_response(raw_response)

    return jsonify({"code": clean_code})


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
    data = request.json
    test_code = data.get("code", "")
    
    # Set up capturing of stdout
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    
    try:
        # Execute the code
        exec_globals = {}
        exec(test_code, {}, exec_globals)
        
        # Capture the output and return it
        output = new_stdout.getvalue()  # The captured output
        sys.stdout = old_stdout  # Restore original stdout
        return jsonify({"result": output.strip()})  # Return captured output as result
    
    except Exception as e:
        sys.stdout = old_stdout  # Restore original stdout even in case of error
        return jsonify({"error": str(e)})

# WebSocket for real-time code testing
@socketio.on('test_code')
def handle_test_code(data):
    """
    WebSocket handler for testing code live in real-time.
    """
    code = data.get("code", "")
    try:
        exec_globals = {}
        exec(code, {}, exec_globals)
        result = exec_globals
        emit('test_result', {"result": result})
    except Exception as e:
        emit('test_result', {"error": str(e)})

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
