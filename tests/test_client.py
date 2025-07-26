import unittest
from unittest.mock import patch, Mock
import requests
from src.client import ClaudeClient

class TestClaudeClient(unittest.TestCase):

    def setUp(self):
        self.client = ClaudeClient(api_key="test_api_key")

    @patch('requests.post')
    def test_send_message_success(self, mock_post):
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "content": [{"text": "Hello, world!"}]
        }
        mock_post.return_value = mock_response

        response = self.client.send_message(
            model="claude-3-5-sonnet-20241022",
            max_tokens=10,
            messages=[{"role": "user", "content": "Hello"}],
            temperature=0.7
        )

        self.assertEqual(response, "Hello, world!")
        mock_post.assert_called_once()

    @patch('requests.post')
    def test_send_message_unauthorized(self, mock_post):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.RequestException("unauthorized")
        mock_post.return_value = mock_response

        response = self.client.send_message(
            model="claude-3-5-sonnet-20241022",
            max_tokens=10,
            messages=[{"role": "user", "content": "Hello"}],
            temperature=0.7
        )

        self.assertIsNone(response)

    @patch('requests.post')
    def test_send_message_rate_limit(self, mock_post):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.RequestException("rate_limit")
        mock_post.return_value = mock_response

        response = self.client.send_message(
            model="claude-3-5-sonnet-20241022",
            max_tokens=10,
            messages=[{"role": "user", "content": "Hello"}],
            temperature=0.7
        )

        self.assertIsNone(response)

if __name__ == '__main__':
    unittest.main()
