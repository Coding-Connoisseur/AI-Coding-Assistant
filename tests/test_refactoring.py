# test_refactoring.py
import unittest
from unittest.mock import patch
from core.code_refactoring import CodeRefactor

class TestCodeRefactoring(unittest.TestCase):

    @patch('core.code_refactoring.openai.Completion.create')
    def test_refactor_code(self, mock_openai_create):
        mock_openai_create.return_value.choices = [type('', (), {'text': 'def calculator():\n    pass'})]
        
        code_refactor = CodeRefactor(api_key="fake_api_key")
        original_code = 'def calc():\n    return 42'
        refactored_code = code_refactor.refactor_code(original_code)

        self.assertIn('def calculator', refactored_code)
        mock_openai_create.assert_called_once()

    @patch('core.code_refactoring.openai.Completion.create')
    def test_improve_performance(self, mock_openai_create):
        mock_openai_create.return_value.choices = [type('', (), {'text': 'Improved performance code'})]

        code_refactor = CodeRefactor(api_key="fake_api_key")
        original_code = 'for i in range(100):\n    print(i)'
        improved_code = code_refactor.improve_performance(original_code)

        self.assertIn('Improved performance', improved_code)
        mock_openai_create.assert_called_once()

if __name__ == '__main__':
    unittest.main()
