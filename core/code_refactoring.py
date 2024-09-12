# code_refactoring.py
import openai

class CodeRefactor:
    def __init__(self, api_key):
        # Initialize the refactor class with OpenAI API key
        self.api_key = api_key
        openai.api_key = api_key

    def refactor_code(self, code):
        """
        Refactors the provided code to make it cleaner, more efficient, and more readable.
        """
        prompt = f"Refactor the following code for readability and efficiency:\n{code}"

        response = openai.Completion.create(
            engine="code-davinci-002",
            prompt=prompt,
            max_tokens=200,
            temperature=0.2
        )
        
        return response.choices[0].text.strip()

    def improve_performance(self, code):
        """
        Focuses on optimizing code for performance.
        """
        prompt = f"Optimize the following code for performance:\n{code}"

        response = openai.Completion.create(
            engine="code-davinci-002",
            prompt=prompt,
            max_tokens=200,
            temperature=0.2
        )
        
        return response.choices[0].text.strip()
