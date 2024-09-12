# codegen_model.py
from openai import OpenAI
import torch
import os
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

class CodeGenerationModel:
    def __init__(self, api_key=None, model_name="gpt-3", language="python"):
        """
        Initializes the code generation model, using either OpenAI API or a local model.
        """
        self.language = language
        self.model_name = model_name.lower()

        if self.model_name == "gpt-3" or self.model_name == "codex":
            self.api_key = api_key
            # Initialize OpenAI client here, assuming `openai` is imported and configured
            from openai import OpenAI
            
            client = OpenAI(api_key=self.api_key)
        else:
            from transformers import GPT2Tokenizer, GPT2LMHeadModel
            self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
            self.model = GPT2LMHeadModel.from_pretrained('gpt2')

    def generate_code_openai(self, description):
        """
        Generates code using OpenAI Codex or GPT-3.
        """
        prompt = f"Generate {self.language} code for the following task: {description}"

        response = client.completions.create(model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=200,
        temperature=0.5)
        return response.choices[0].text.strip()

    def generate_code_gpt2(self, description):
        """
        Generates code using a local GPT-2 model.
        """
        # Implementation for generating code using GPT-2
