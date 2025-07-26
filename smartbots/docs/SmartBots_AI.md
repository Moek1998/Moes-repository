# SmartBots AI - SmartBots Developers Docs

[SmartBots AI](https://www.mysmartbots.com/docs/SmartBots_AI) is a conversation-based AI which can be used with Playground scripts in order to create AI conversations.

## SmartBots AI for developers

The most convenient way to access SmartBots AI is to use conversations.

You can send "raw" requests to the AI but conversations give you the way to keep track of context (previous messages and responses.

*   You create a conversation by calling **Bot.AI.getConversationByName(residentName)**. The resulting object may be reused for further communications with AI.
*   SmartBots AI keeps track of a context within a conversation.
*   Conversation options can be adjusted separately for each conversation.
*   Conversations are system-wide, tied to script + bot + specific resident.

## Main concepts

Instructions

The rules for the bot: how to react, how to role-play, what to know. [Check instructions examples](https://www.mysmartbots.com/docs/SmartBots_AI/Instructions)

Token

Each request to SmartBots AI consumes tokens. [Read more here](https://www.mysmartbots.com/dev/docs/Bot_Playground/AI/Tokens "Bot Playground/AI/Tokens") about tokens usage.

## AI commands reference

| Command | Description |
| --- | --- |
| ### Commands |     |     |
| [Bot.AI.chat](https://www.mysmartbots.com/dev/docs/Bot_Playground/AI/Bot.AI.chat "Bot Playground/AI/Bot.AI.chat") | Sends a chat message request to bot AI. |
| [Bot.AI.configure](https://www.mysmartbots.com/dev/docs/Bot_Playground/AI/Bot.AI.configure "Bot Playground/AI/Bot.AI.configure") | Configures AI options to be used in all further communications within the current script. |
| [Bot.AI.getConversationByName](https://www.mysmartbots.com/dev/docs/Bot_Playground/AI/Bot.AI.getConversationByName "Bot Playground/AI/Bot.AI.getConversationByName") | Get/create conversation with a specific resident. If conversation doesn't exist yet, creates it. |
| [Bot.AI.forgetConversation](https://www.mysmartbots.com/dev/docs/Bot_Playground/AI/Bot.AI.forgetConversation "Bot Playground/AI/Bot.AI.forgetConversation") | Forget (cancel) conversation of a bot with a specific resident. |
| [Conversation.chat](https://www.mysmartbots.com/dev/docs/Bot_Playground/AI/Conversation.chat "Bot Playground/AI/Conversation.chat") | Sends a chat message request to bot AI within a conversation with a specific resident. |
| [Conversation.configure](https://www.mysmartbots.com/dev/docs/Bot_Playground/AI/Conversation.configure "Bot Playground/AI/Conversation.configure") | Sets some configuration values for the future usage |
