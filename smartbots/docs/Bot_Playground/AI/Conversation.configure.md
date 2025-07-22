# Conversation.configure - SmartBots Developers Docs

From SmartBots Developers Docs

Jump to: [navigation](#mw-head), [search](#p-search)


Sets some configuration values for the future usage

Conversation.configure(options)

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | options | yes | configuration directives for the AI engine. Example:<br><br>{<br>     // Main configuration instructions for the AI: role, behavior, response rules etc.<br>     instructions?: string;<br>     <br>     // Maximum number of tokens to generate in response<br>     maxResponseTokens?: number;<br><br>     // The amount of history to retain for the conversation.<br>     maxHistoryMessages?: number;<br>} |
| Output: |     |     |     |
|     | none |     |     |

> *   Note: The \`instructions\` and \`maxResponseTokens\` settings are hard-coded in user settings. They do not need to be explicitly created for user settings. Instead, these values should be fetched from \`userSettings.instructions\` and \`userSettings.maxResponseTokens\` and included in the configuration.
