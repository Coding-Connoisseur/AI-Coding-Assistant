# nlp_processing.py
import openai

class NLPProcessor:
    def __init__(self, api_key):
        # Initialize the NLP processor with the OpenAI API key
        self.api_key = api_key
        openai.api_key = api_key

    def process_input(self, user_input):
        """
        Takes a natural language input from the user and processes it to extract the intent.
        Returns a structured response that maps the intent to a specific action.
        """
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Process this command: {user_input}",
            max_tokens=100,
            temperature=0.5
        )
        
        # Returning structured action command based on NLP output
        return response.choices[0].text.strip()

    def extract_code_requirements(self, user_input):
        """
        Special processing for extracting programming language or function requirements
        from the user's input.
        """
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Extract code generation requirements from this: {user_input}",
            max_tokens=50,
            temperature=0.5
        )
        
        return response.choices[0].text.strip()
