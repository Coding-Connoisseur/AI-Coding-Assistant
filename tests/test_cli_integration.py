# test_cli_integration.py
import unittest
from unittest.mock import patch
import sys
from io import StringIO
from integrations.cli_integration import CLIIntegration

class TestCLIIntegration(unittest.TestCase):

    @patch('core.code_generation.CodeGenerator.generate_code')
    @patch('core.nlp_processing.NLPProcessor.extract_code_requirements')
    def test_generate_command(self, mock_extract_code, mock_generate_code):
        mock_extract_code.return_value = "Python"
        mock_generate_code.return_value = 'def calculator(): pass'

        cli_integration = CLIIntegration(api_key="fake_api_key")
        test_args = ["prog", "generate", "python", "Create a calculator function"]

        with patch.object(sys, 'argv', test_args):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                cli_integration.run_cli()
                self.assertIn('def calculator', fake_out.getvalue())

    @patch('core.code_refactoring.CodeRefactor.refactor_code')
    def test_refactor_command(self, mock_refactor_code):
        mock_refactor_code.return_value = 'def refactored_code(): pass'

        cli_integration = CLIIntegration(api_key="fake_api_key")
        test_args = ["prog", "refactor", "def code(): pass"]

        with patch.object(sys, 'argv', test_args):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                cli_integration.run_cli()
                self.assertIn('def refactored_code', fake_out.getvalue())

if __name__ == '__main__':
    unittest.main()
