import unittest
from unittest.mock import patch, Mock
from src.cli import main

class TestCLI(unittest.TestCase):

    @patch('src.cli.ClaudeCLI')
    def test_main_interactive(self, MockClaudeCLI):
        """
        Test that the CLI runs in interactive mode when invoked with the '-i' flag.
        """
        instance = MockClaudeCLI.return_value
        with patch('sys.argv', ['claude', '-i']):
            main()
        instance.interactive_mode.assert_called_once()

    @patch('src.cli.ClaudeCLI')
    def test_main_squad(self, MockClaudeCLI):
        """
        Test that the main function calls simulate_squad_features when the '--squad' flag is provided.
        """
        instance = MockClaudeCLI.return_value
        with patch('sys.argv', ['claude', '--squad']):
            main()
        instance.simulate_squad_features.assert_called_once()

    @patch('src.cli.ClaudeCLI')
    def test_main_code(self, MockClaudeCLI):
        """
        Test that the CLI invokes simulate_code_features when the --code flag is provided.
        """
        instance = MockClaudeCLI.return_value
        with patch('sys.argv', ['claude', '--code']):
            main()
        instance.simulate_code_features.assert_called_once()

    @patch('src.cli.ClaudeCLI')
    def test_main_message(self, MockClaudeCLI):
        """
        Test that the CLI calls the chat method with the correct arguments when a message is provided as a command-line argument.
        """
        instance = MockClaudeCLI.return_value
        instance.chat.return_value = "response"
        with patch('sys.argv', ['claude', 'hello']):
            main()
        instance.chat.assert_called_once_with('hello', None, None)

if __name__ == '__main__':
    unittest.main()
