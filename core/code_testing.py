# code_testing.py
import subprocess
import sys
from openai import OpenAI
import os
from dotenv import load_dotenv

class CodeTester:
    def __init__(self, api_key=None):
        """
        Initialize the code generator with OpenAI API key.
        If api_key is provided, it overrides the one from environment variables.
        """
        load_dotenv()

        # Set API key directly in OpenAI's client
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key) if api_key else OpenAI()  # Use provided API key if available, otherwise use default key from environment variables.  # This line ensures that the client's API key is set correctly, even if it's not provided in the constructor.  # It also allows for overriding the API key from environment variables.  # Note: This line will not work if the environment variable is not set, and it will not


    def run_code(self, code, language="python"):
        """
        Runs the code provided in a subprocess and returns the output.
        Currently supports Python code.
        """
        if language == "python":
            try:
                exec_locals = {}
                exec(code, {}, exec_locals)
                return exec_locals
            except Exception as e:
                return str(e)
        else:
            raise NotImplementedError(f"Running code in {language} is not supported yet.")

    def run_tests(self, test_code, language="python"):
        """
        Runs unit tests for the provided test code and returns the results.
        """
        if language == "python":
            try:
                exec(test_code)
                return "All tests passed!"
            except Exception as e:
                return str(e)
        else:
            raise NotImplementedError(f"Running tests in {language} is not supported yet.")

    def run_shell_command(self, command):
        """
        Runs a system-level shell command and returns its output.
        """
        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode("utf-8")
        except subprocess.CalledProcessError as e:
            return e.stderr.decode("utf-8")
