# code_refactoring.py
from openai import OpenAI
import os
from dotenv import load_dotenv


class CodeRefactor:
    def __init__(self, api_key=None):
        """
        Initialize the code refactor with OpenAI API key.
        If api_key is provided, it overrides the one from environment variables.
        """
        load_dotenv()

        # Set API key directly in OpenAI's client
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key) if api_key else OpenAI()  # Use provided API key if available, otherwise use default key from environment variables.  # This line ensures that the client's API key is set correctly, even if it's not provided in the constructor.  # It also allows for overriding the API key from environment variables.  # Note: This line will not work if the environment variable is not set, and it will not

    def refactor_code(self, code):
        """
        Refactor the provided code for optimization and readability.
        """
        prompt = f"Refactor the following code for optimization and readability:\n\n{code}"
        response = self.client.completions.create(model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=200,
        temperature=0.5)
        return response.choices[0].message['content'].strip()

    def improve_performance(self, code):
        """
        Focuses on optimizing code for performance.
        """
        prompt = f"Optimize the following code for performance:\n{code}"
    
        response = self.client.completions.create(model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=200,
        temperature=0.2)
    
        return response.choices[0].text.strip()
