# cli_integration.py
import argparse
from core import nlp_processing, code_generation, code_refactoring, code_testing

class CLIIntegration:
    def __init__(self, api_key):
        self.nlp_processor = nlp_processing.NLPProcessor(api_key)
        self.code_generator = code_generation.CodeGenerator(api_key)
        self.code_refactor = code_refactoring.CodeRefactor(api_key)
        self.code_tester = code_testing.CodeTester()

    def run_cli(self):
        """
        Main entry point for the CLI. Parses commands and executes actions.
        """
        parser = argparse.ArgumentParser(description="AI Assistant CLI for Code Generation and Refactoring")
        
        subparsers = parser.add_subparsers(dest="command", help="Available commands")

        # Generate code
        gen_parser = subparsers.add_parser("generate", help="Generate code based on input")
        gen_parser.add_argument("language", help="Programming language")
        gen_parser.add_argument("description", help="Description of what the code should do")

        # Refactor code
        ref_parser = subparsers.add_parser("refactor", help="Refactor code for improvement")
        ref_parser.add_argument("code", help="Code to refactor")

        # Test code
        test_parser = subparsers.add_parser("test", help="Test code")
        test_parser.add_argument("code", help="Code to run tests on")

        args = parser.parse_args()

        if args.command == "generate":
            print(self.handle_generate(args.language, args.description))
        elif args.command == "refactor":
            print(self.handle_refactor(args.code))
        elif args.command == "test":
            print(self.handle_test(args.code))
        else:
            parser.print_help()

    def handle_generate(self, language, description):
        """
        Handles the code generation command.
        """
        return self.code_generator.generate_code(description, language)

    def handle_refactor(self, code):
        """
        Handles the code refactoring command.
        """
        return self.code_refactor.refactor_code(code)

    def handle_test(self, code):
        """
        Handles the code testing command.
        """
        return self.code_tester.run_code(code)
