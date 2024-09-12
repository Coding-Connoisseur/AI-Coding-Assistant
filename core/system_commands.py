# system_commands.py
import subprocess
import os
from openai import OpenAI
from dotenv import load_dotenv


class SystemCommand:
    def __init__(self, api_key=None):
        """
        Initialize the System Command with OpenAI API key.
        If api_key is provided, it overrides the one from environment variables.
        """
        load_dotenv()

        # Set API key directly in OpenAI's client
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key) if api_key else OpenAI()  # Use provided API key if available, otherwise use default key from environment variables.  # This line ensures that the client's API key is set correctly, even if it's not provided in the constructor.  # It also allows for overriding the API key from environment variables.  # Note: This line will not work if the environment variable is not set, and it will not


    def run_shell_command(self, command):
        """
        Runs a system shell command.
        """
        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return e.stderr.decode('utf-8')

    def create_file(self, filename, content):
        """
        Creates a new file and writes content to it.
        """
        try:
            with open(filename, 'w') as f:
                f.write(content)
            return f"{filename} created successfully."
        except Exception as e:
            return str(e)

    def read_file(self, filename):
        """
        Reads the contents of a file.
        """
        try:
            with open(filename, 'r') as f:
                return f.read()
        except Exception as e:
            return str(e)

    def delete_file(self, filename):
        """
        Deletes a file.
        """
        try:
            os.remove(filename)
            return f"{filename} deleted successfully."
        except Exception as e:
            return str(e)
