import requests

class ClaudeClient:
    def __init__(self, api_key, api_url="https://api.anthropic.com/v1/messages"):
        """
        Initialize a ClaudeClient instance with the provided API key and optional API URL.
        
        Parameters:
            api_key (str): The API key used for authenticating requests to the Claude API.
            api_url (str, optional): The endpoint URL for the Claude API. Defaults to "https://api.anthropic.com/v1/messages".
        """
        self.api_key = api_key
        self.api_url = api_url

    def send_message(self, model, max_tokens, messages, temperature, system_prompt=None):
        """
        Send a message to the Anthropic Claude API and return the generated response text.
        
        Parameters:
            model (str): The Claude model to use.
            max_tokens (int): Maximum number of tokens to generate in the response.
            messages (list): List of message objects representing the conversation history.
            temperature (float): Sampling temperature for response generation.
            system_prompt (str, optional): Optional system prompt to guide the model's behavior.
        
        Returns:
            str or None: The generated response text from Claude, or None if an error occurs.
        """
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': self.api_key,
            'anthropic-version': '2023-06-01'
        }

        data = {
            'model': model,
            'max_tokens': max_tokens,
            'messages': messages,
            'temperature': temperature
        }

        if system_prompt:
            data['system'] = system_prompt

        try:
            response = requests.post(self.api_url, headers=headers, json=data)
            response.raise_for_status()

            result = response.json()
            return result['content'][0]['text']

        except requests.exceptions.RequestException as e:
            if "unauthorized" in str(e).lower():
                print("❌ API key invalid or expired. Get a new one at: https://console.anthropic.com/")
            elif "rate_limit" in str(e).lower():
                print("⏰ Rate limit reached. Consider upgrading your API plan.")
            else:
                print(f"Error making request: {e}")
            return None
        except KeyError as e:
            print(f"Error parsing response: {e}")
            print(f"Response: {response.text}")
            return None
