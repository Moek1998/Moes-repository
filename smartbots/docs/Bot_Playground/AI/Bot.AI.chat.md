# Bot.AI.chat - SmartBots Developers Docs

From SmartBots Developers Docs

Jump to: [navigation](#mw-head), [search](#p-search)

Sends a chat message request to bot AI.

Bot.AI.chat(message, senderName\[, options\])

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | message | yes | chat message to the bot |
|     | residentName | yes | The name of the resident sending the message |
|     | options | optional | The name of the resident sending the message Format:<br><br>{<br>     instructions?: string;<br>     // Previous messade ID, if responding to a particular previous AI message of the bot<br>     parentMessageId?: string;<br>     // Maximum number of tokens to generate in response<br>     maxResponseTokens?: number;<br><br>     // Max number of response in bytes. SL IM has a max limit of 1023bytes.<br>     maxResponseBytes?: number;<br>} |
| Output: |     |     |     |
|     | text |     | The response of the bot |
|     | messageId |     | The id of the response message. Can be specified as parentMessageId later |
|     | usage |     | The object which contains Token Usage. Format: The object which contains all groups. Format:<br><br>{<br>// Number of tokens in a request (message + instructions + history)<br>prompt\_tokens: number;<br>// Number of tokens in a response<br>completion\_tokens: number;<br>// Total tokens used<br>total\_tokens: number;<br>// Tokens left on SmartBots AI balance<br>tokens\_left: number;<br>} |

> *   Note: The \`instructions\` and \`maxResponseTokens\` settings are hard-coded in user settings. They do not need to be explicitly created for user settings. Instead, these values should be fetched from \`userSettings.instructions\` and \`userSettings.maxResponseTokens\` and included in the configuration.
> *   In case of error functions throws an error with a message.
