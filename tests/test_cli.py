import unittest
from unittest.mock import patch, Mock
from src.cli import main

class TestCLI(unittest.TestCase):

    @patch('src.cli.ClaudeCLI')
    def test_main_interactive(self, MockClaudeCLI):
        instance = MockClaudeCLI.return_value
        with patch('sys.argv', ['claude', '-i']):
            main()
        instance.interactive_mode.assert_called_once()

    @patch('src.cli.ClaudeCLI')
    def test_main_squad(self, MockClaudeCLI):
        instance = MockClaudeCLI.return_value
        with patch('sys.argv', ['claude', '--squad']):
            main()
        instance.simulate_squad_features.assert_called_once()

    @patch('src.cli.ClaudeCLI')
    def test_main_code(self, MockClaudeCLI):
        instance = MockClaudeCLI.return_value
        with patch('sys.argv', ['claude', '--code']):
            main()
        instance.simulate_code_features.assert_called_once()

    @patch('src.cli.ClaudeCLI')
    def test_main_message(self, MockClaudeCLI):
        instance = MockClaudeCLI.return_value
        instance.chat.return_value = "response"
        with patch('sys.argv', ['claude', 'hello']):
            main()
        instance.chat.assert_called_once_with('hello', None, None)

if __name__ == '__main__':
    unittest.main()
