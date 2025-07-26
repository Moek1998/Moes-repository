# Bot.AI.configure - SmartBots Developers Docs

From SmartBots Developers Docs

Jump to: [navigation](#mw-head), [search](#p-search)


Configures AI options to be used in all further communications within the current script.

Bot.AI.configure(options)

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | options | yes | configuration directives for the AI engine. Format:<br><br>{<br>     // Main configuration instructions for the AI: role, behavior, response rules etc.<br>     instructions?: string;<br><br>     // If responding to a particular previous AI message of the bot<br>     parentMessageId?: string;<br><br>     // Maximum number of tokens to generate in response<br>     maxResponseTokens?: number;<br><br>     // The unique conversation id. Usually generated automatically based<br>     // on the sender and bot name.<br>     conversationId?: string;<br><br>     // The amount of history to retain for the conversation.<br>     maxHistoryMessages?: number;<br><br>} |
| Output: |     |     |     |
|     | result |     | This function does not return anything |

> *   Note: The \`instructions\` and \`maxResponseTokens\` settings are hard-coded in user settings. They do not need to be explicitly created for user settings. Instead, these values should be fetched from \`userSettings.instructions\` and \`userSettings.maxResponseTokens\` and included in the configuration.
