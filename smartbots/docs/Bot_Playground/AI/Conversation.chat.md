# Conversation.chat - SmartBots Developers Docs

From SmartBots Developers Docs

Jump to: [navigation](#mw-head), [search](#p-search)


Sends a chat message request to bot AI within a conversation with a specific resident.

Conversation.chat(message\[, options\])

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | message | yes | chat message to the bot |
|     | options | optional | configuration directives for the AI engine. Example:<br><br>{<br>     // Main configuration instructions for the AI: role, behavior, response rules etc.<br>     instructions?: string;<br>     <br>     // Maximum number of tokens to generate in response<br>     maxResponseTokens?: number;<br><br>     // Max number of response in bytes. SL IM has a max limit of 1023bytes.<br>     maxResponseBytes?: number;<br>} |
| Output: |     |     |     |
|     | same value as Bot.AI.chat(...) |     | This command returns the same value as Bot.AI.chat(...) |

> *   Note: The \`instructions\` and \`maxResponseTokens\` settings are hard-coded in user settings. They do not need to be explicitly created for user settings. Instead, these values should be fetched from \`userSettings.instructions\` and \`userSettings.maxResponseTokens\` and included in the configuration.
