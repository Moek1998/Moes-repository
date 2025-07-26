# Tokens - SmartBots Developers Docs

Token is a "charge" or SmartBots AI, to be utilized by SmartBots AI engine. Think of token as a short word (~4 characters). Longer words may consume more than 1 token.

Calling SmartBots AI consumes tokens of script owner. Thus, when you [sell](https://www.mysmartbots.com/dev/docs/Bot_Playground/Store "Bot Playground/Store") scripts at Bot Store, your buyers would need to fund tokens balance. As of Oct 2023, each user is eligible for 20,000 free tokens.

## Tokens usage

Tokens are consumed for the following parts of a request:

*   User message (what resident says to the bot)
*   Instructions
*   All previous messages (to keep a context)

## Usage example

For example:

1st message from resident

Resident: _"Hello!"_

Request to AI: "Your instructions" + "Hello"

Bot response: _"Hi!"_

Total tokens: 1 (message) + 2 (instructions) + 1 (response)

2nd message

Resident: _"Who are you?"_

Request to AI: "Your instructions + "Hello" (1st message) + "Hi!" (1st response) + "Who are you?" (new message)

Bot response: _"I am a bot"_

Total tokens: 3 (message) + 2 (instructions) + 4 (history) + 4 (response)

Actually the number of tokens will be higher: we also send the bot name, resident name and some system data.

## Tokens report

AI functions (like [Conversation.chat](https://www.mysmartbots.com/dev/docs/Bot_Playground/AI/Conversation.chat "Bot Playground/AI/Conversation.chat")) return tokens usage report, as well as amounts of tokens left. This can be used to warn the script owner about low tokens balance.
