# from requests import post  # Import only the 'post' function from requests for making HTTP POST requests

class ClaudeClient:
    def __init__(self, api_key, api_url="https://api.anthropic.com/v1/messages"):

class ClaudeClient:
    def __init__(self, api_key, api_url="https://api.anthropic.com/v1/messages"):
        self.api_key = api_key
        self.api_url = api_url

    def send_message(self, model, max_tokens, messages, temperature, system_prompt=None):
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
return result['content'][0]['text']

        except requests.exceptions.RequestException as e:
            # import logging
            if "unauthorized" in str(e).lower():
                logging.error("❌ API key invalid or expired. Get a new one at: https://console.anthropic.com/")
            elif "rate_limit" in str(e).lower():
                logging.warning("⏰ Rate limit reached. Consider upgrading your API plan.")
            else:
                logging.error(f"Error making request: {e}")
            return None
        except KeyError as e:
            logging.error(f"Error parsing response: {e}")
            logging.error(f"Response: {response.text}")
            return None
            return None
        except KeyError as e:
            print(f"Error parsing response: {e}")
except requests.exceptions.RequestException as e:
            if "unauthorized" in str(e).lower():
                logging.error("❌ API key invalid or expired. Get a new one at: https://console.anthropic.com/")
            elif "rate_limit" in str(e).lower():
                logging.warning("⏰ Rate limit reached. Consider upgrading your API plan.")
            else:
                logging.error(f"Error making request: {e}")
            return None
        except KeyError as e:
            logging.error(f"Error parsing response: {e}")
            logging.debug(f"Response: {response.text}")
            return None

# Import logging at the top of the file
# import logging
# logging.basicConfig(level=logging.INFO)
            return None
