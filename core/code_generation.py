from openai import OpenAI
import os
from dotenv import load_dotenv



class CodeGenerator:
    def __init__(self, api_key=None):
        """
        Initialize the code generator with OpenAI API key.
        If api_key is provided, it overrides the one from environment variables.
        """
        load_dotenv()

        # Set API key directly in OpenAI's client
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key) if api_key else OpenAI()  # Use provided API key if available, otherwise use default key from environment variables.  # This line ensures that the client's API key is set correctly, even if it's not provided in the constructor.  # It also allows for overriding the API key from environment variables.  # Note: This line will not work if the environment variable is not set, and it will not


    def generate_function(self, function_name, description, language="python"):
        """
        Generates a specific function based on its name and a description of what it should do.
        """
        prompt = f"Generate a {language} function called {function_name}. {description}"

        response = self.client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful coding assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.2)

        return response.choices[0].message.content.strip()
    
    def generate_class(self, class_name, description, language="python"):
        """
        Generates a specific class based on its name and a description of what it should do.
        """
        prompt = f"Generate a {language} class called {class_name}. {description}"

        response = self.client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful coding assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.2)

        return response.choices[0].message.content.strip()
    
    def generate_method(self, method_name, description, language="python"):
        """
        Generates a specific method based on its name and a description of what it should do.
        """
        prompt = f"Generate a {language} method called {method_name}. {description}"

        response = self.client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful coding assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.2)

        return response.choices[0].message.content.strip()
    
    def generate_variable(self, variable_name, description, language="python"):
        """
        Generates a specific variable based on its name and a description of what it should do.
        """
        prompt = f"Generate a {language} variable called {variable_name}. {description}"

        response = self.client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful coding assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.2)

        return response.choices[0].message.content.strip()
    
    def generate_loop(self, loop_type, description, language="python"):
        """
        Generates a specific loop based on its type and a description of what it should do.
        """
        prompt = f"Generate a {language} {loop_type} loop. {description}"

        response = self.client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful coding assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.2)

        return response.choices[0].message.content.strip()
    
    def generate_condition(self, condition_type, description, language="python"):
        """
        Generates a specific condition based on its type and a description of what it should do.
        """
        prompt = f"Generate a {language} {condition_type} condition. {description}"

        response = self.client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful coding assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.2)

        return response.choices[0].message.content.strip()
    
    def generate_if_statement(self, condition_type, description, language="python"):
        """
        Generates a specific if statement based on its type and a description of what it should do.
        """
        prompt = f"Generate a {language} if statement with {condition_type} condition. {description}"

        response = self.client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful coding assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.2)

        return response.choices[0].message.content.strip()
    
    def generate_else_statement(self, description, language="python"):  # This method generates an else statement based on a description of what it should do.
        """
        Generates a specific else statement based on a description of what it should do.
        """
        prompt = f"Generate a {language} else statement. {description}"

        response = self.client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful coding assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.2)

        return response.choices[0].message.content.strip()

    def generate_switch_statement(self, description, language="python"):  # This method generates a switch statement based on a description of what it should do.
        """
        Generates a specific switch statement based on a description of what it should do.
        """
        prompt = f"Generate a {language} switch statement. {description}"

        response = self.client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful coding assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.2)

        return response.choices[0].message.content.strip()
    
    def generate_return_statement(self, description, language="python"):  # This method generates a return statement based on a description of what it should do.
        """
        Generates a specific return statement based on a description of what it should do.
        """
        prompt = f"Generate a {language} return statement. {description}"

        response = self.client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful coding assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.2)

        return response.choices[0].message.content.strip()
    
    def generate_code(self, user_input, language="python"):
        """
        Generates code in the specified programming language based on user input.
        """
        prompt = f"Write {language} code for the following request: {user_input}"

        response = self.client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful coding assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200,
        temperature=0.2)

        return response.choices[0].message.content.strip()

    def generate_function(self, function_name, description, language="python"):
        """
        Generates a specific function based on its name and a description of what it should do.
        """
        prompt = f"Generate a {language} function called {function_name}. {description}"

        response = self.client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful coding assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.2)

        return response.choices[0].message.content.strip()

# Example usage
if __name__ == "__main__":
    generator = CodeGenerator()
    user_input = "a function that sorts an array"
    print(generator.generate_code(user_input))

    function_name = "sort_array"
    description = "This function sorts an array using the bubble sort algorithm."
    print(generator.generate_function(function_name, description))
