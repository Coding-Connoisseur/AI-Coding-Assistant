# test_code_generation.py
import unittest
from unittest.mock import patch
from core.code_generation import CodeGenerator

class TestCodeGeneration(unittest.TestCase):

    @patch('core.code_generation.openai.Completion.create')
    def test_generate_code(self, mock_openai_create):
        mock_openai_create.return_value.choices = [type('', (), {'text': 'def calculator():\n    return "code" '})]

        code_generator = CodeGenerator(api_key="fake_api_key")
        result = code_generator.generate_code("Create a Python calculator", language="python")

        self.assertIn("def calculator", result)
        mock_openai_create.assert_called_once()

    @patch('core.code_generation.openai.Completion.create')
    def test_generate_function(self, mock_openai_create):
        mock_openai_create.return_value.choices = [type('', (), {'text': 'def add(a, b): return a + b'})]

        code_generator = CodeGenerator(api_key="fake_api_key")
        result = code_generator.generate_function("add", "adds two numbers", language="python")

        self.assertIn("def add", result)
        mock_openai_create.assert_called_once()

if __name__ == '__main__':
    unittest.main()
