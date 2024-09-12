# nlp_model.py
from openai import OpenAI
import os
import torch
from transformers import GPT2Tokenizer, GPT2Model
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

class NLPModel:
    def __init__(self, api_key=None, model_name="gpt-3"):
        """
        Initializes the NLP model, either using OpenAI API (GPT-3) or a local transformer model like GPT-2.
        """
        self.model_name = model_name.lower()

        if self.model_type == "bert":
            # Initialize BERT model
            from transformers import BertTokenizer, BertModel
            self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
            self.model = BertModel.from_pretrained('bert-base-uncased')
        else:
            # Initialize a different model, e.g., GPT-2
            from transformers import GPT2Tokenizer, GPT2LMHeadModel
            self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
            self.model = GPT2LMHeadModel.from_pretrained('gpt2')

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt")
        outputs = self.model(**inputs)
        return outputs 


    def process_text_openai(self, text):
        """
        Uses OpenAI's GPT-3 model to process text and generate a response.
        """
        response = client.completions.create(model="text-davinci-003",
        prompt=text,
        max_tokens=150,
        temperature=0.7)
        return response.choices[0].text.strip()

    def process_text_gpt2(self, text):
        """
        Uses a local GPT-2 model to process text and generate a response.
        """
        inputs = self.tokenizer(text, return_tensors="pt")
        outputs = self.model(**inputs)
        return outputs.last_hidden_state

    def process_text(self, text):
        """
        Routes text processing to the appropriate model (GPT-3 or GPT-2).
        """
        if self.model_name == "gpt-3":
            return self.process_text_openai(text)
        else:
            return self.process_text_gpt2(text)

    def extract_intent(self, text):
        """
        Extracts intent from the text using NLP model.
        For example: "Generate Python code for a calculator" -> intent: "code_generation"
        """
        prompt = f"Extract the intent from the following text: {text}"
        return self.process_text(prompt)
