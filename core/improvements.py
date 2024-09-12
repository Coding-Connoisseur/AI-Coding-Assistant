# improvements.py
from openai import OpenAI
import os
from dotenv import load_dotenv


class CodeImprover:
    def __init__(self, api_key=None):
        """
        Initialize the code generator with OpenAI API key.
        If api_key is provided, it overrides the one from environment variables.
        """
        load_dotenv()

        # Set API key directly in OpenAI's client
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key) if api_key else OpenAI()  # Use provided API key if available, otherwise use default key from environment variables.  # This line ensures that the client's API key is set correctly, even if it's not provided in the constructor.  # It also allows for overriding the API key from environment variables.  # Note: This line will not work if the environment variable is not set, and it will not


    def suggest_improvements(self, code):
        """
        Suggest improvements to the provided code based on efficiency and best practices.
        """
        prompt = f"Suggest improvements for the following code:\n{code}"

        response = self.client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a code assistant."},
                  {"role": "user", "content": prompt}],
        max_tokens=200,
        temperature=0.2)
        return response.choices[0].message.content.strip()

    def analyze_complexity(self, code):
        """
        Analyzes the time and space complexity of the given code and suggests optimizations.
        """
        prompt = f"Analyze the time and space complexity of this code and suggest improvements:\n{code}"

        response = self.client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a code assistant."},
                  {"role": "user", "content": prompt}],
        max_tokens=150,
        temperature=0.2)
        return response.choices[0].message.content.strip()

    def optimize_algorithm(self, code):
        """
        Suggests optimizations to improve algorithm efficiency based on known data structures and algorithms.
        """
        prompt = f"Optimize the algorithm for better performance:\n{code}"

        response = self.client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a code assistant."},
                  {"role": "user", "content": prompt}],
        max_tokens=200,
        temperature=0.2)
        return response.choices[0].message.content.strip()

# Example usage
if __name__ == "__main__":
    api_key = os.getenv("OPENAI_API_KEY")
    improver = CodeImprover(api_key)
    code = "def sort_array(arr): for i in range(len(arr)): for j in range(i+1, len(arr)): if arr[i] > arr[j]: arr[i], arr[j] = arr[j], arr[i]"
    print(improver.suggest_improvements(code))
    print(improver.analyze_complexity(code))
    print(improver.optimize_algorithm(code))
