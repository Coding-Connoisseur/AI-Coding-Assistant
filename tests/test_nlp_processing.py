# test_nlp_processing.py
import unittest
from unittest.mock import patch
from core.nlp_processing import NLPProcessor

class TestNLPProcessing(unittest.TestCase):

    @patch('core.nlp_processing.openai.Completion.create')
    def test_process_input(self, mock_openai_create):
        mock_openai_create.return_value.choices = [type('', (), {'text': 'Generate Python code'})]
        
        nlp_processor = NLPProcessor(api_key="fake_api_key")
        result = nlp_processor.process_input("Generate Python code for a calculator")

        self.assertEqual(result, "Generate Python code")
        mock_openai_create.assert_called_once()

    @patch('core.nlp_processing.openai.Completion.create')
    def test_extract_code_requirements(self, mock_openai_create):
        mock_openai_create.return_value.choices = [type('', (), {'text': 'Python, calculator'})]
        
        nlp_processor = NLPProcessor(api_key="fake_api_key")
        result = nlp_processor.extract_code_requirements("Generate Python code for a calculator")

        self.assertEqual(result, "Python, calculator")
        mock_openai_create.assert_called_once()

if __name__ == '__main__':
    unittest.main()
