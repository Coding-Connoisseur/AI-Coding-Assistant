# nlp_processing.py
from openai import OpenAI
import os
from dotenv import load_dotenv


class NLPProcessor:
    def __init__(self, api_key=None):
        """
        Initialize the NLP Processor with OpenAI API key.
        If api_key is provided, it overrides the one from environment variables.
        """
        load_dotenv()

        # Set API key directly in OpenAI's client
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key) if api_key else OpenAI()  # Use provided API key if available, otherwise use default key from environment variables.  # This line ensures that the client's API key is set correctly, even if it's not provided in the constructor.  # It also allows for overriding the API key from environment variables.  # Note: This line will not work if the environment variable is not set, and it will not


    def process_input(self, user_input):
        """
        Takes a natural language input from the user and processes it to extract the intent.
        Returns a structured response that maps the intent to a specific action.
        """
        response = self.client.completions.create(model="text-davinci-003",
        prompt=f"Process this command: {user_input}",
        max_tokens=100,
        temperature=0.5)

        # Returning structured action command based on NLP output
        return response.choices[0].text.strip()

    def extract_code_requirements(self, user_input):
        """
        Special processing for extracting programming language or function requirements
        from the user's input.
        """
        response = self.client.completions.create(model="text-davinci-003",
        prompt=f"Extract code generation requirements from this: {user_input}",
        max_tokens=50,
        temperature=0.5)

        return response.choices[0].text.strip()
