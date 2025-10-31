import requests

class ClaudeClient:
    def __init__(self, api_key, api_url="https://api.anthropic.com/v1/messages"):
        self.api_key = api_key
        self.api_url = api_url
        # Create a session for connection reuse
        self.session = requests.Session()
        # Configure session with appropriate timeout and headers
        self.session.headers.update({
            'Content-Type': 'application/json',
            'x-api-key': self.api_key,
            'anthropic-version': '2023-06-01'
        })

    def send_message(self, model, max_tokens, messages, temperature, system_prompt=None):
        data = {
            'model': model,
            'max_tokens': max_tokens,
            'messages': messages,
            'temperature': temperature
        }

        if system_prompt:
            data['system'] = system_prompt

        try:
            # Use session for connection reuse with timeout
            response = self.session.post(
                self.api_url, 
                json=data,
                timeout=(10, 30)  # 10s connect timeout, 30s read timeout
            )
            response.raise_for_status()

            result = response.json()
            # Add defensive checks for response structure
            if 'content' in result and len(result['content']) > 0 and 'text' in result['content'][0]:
                return result['content'][0]['text']
            else:
                print(f"Unexpected response structure: {result}")
                return None

        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response is not None:
                if e.response.status_code == 401:
                    print("❌ API key invalid or expired. Get a new one at: https://console.anthropic.com/")
                elif e.response.status_code == 429:
                    print("⏰ Rate limit reached. Consider upgrading your API plan.")
                else:
                    print(f"Error making request: {e}")
            else:
                print(f"Error making request: {e}")
            return None

        except KeyError as e:
            print(f"Error parsing response: {e}")
            if 'response' in locals():
                print(f"Response: {response.text}")
            return None

    def close(self):
        """Close the session when done"""
        self.session.close()