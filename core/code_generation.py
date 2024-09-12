# code_generation.py
import openai

class CodeGenerator:
    def __init__(self, api_key):
        # Initialize the code generator with OpenAI API key
        self.api_key = api_key
        openai.api_key = api_key

    def generate_code(self, user_input, language="python"):
        """
        Generates code in the specified programming language based on user input.
        """
        prompt = f"Write {language} code for the following request: {user_input}"

        response = openai.Completion.create(
            engine="code-davinci-002",
            prompt=prompt,
            max_tokens=200,
            temperature=0.2
        )
        
        return response.choices[0].text.strip()

    def generate_function(self, function_name, description, language="python"):
        """
        Generates a specific function based on its name and a description of what it should do.
        """
        prompt = f"Generate a {language} function called {function_name}. {description}"

        response = openai.Completion.create(
            engine="code-davinci-002",
            prompt=prompt,
            max_tokens=150,
            temperature=0.2
        )
        
        return response.choices[0].text.strip()
