# sendGroupIM - SmartBots Developers Docs

From SmartBots Developers Docs

Jump to: [navigation](#mw-head), [search](#p-search)

Sends a message to group chat.

Bot.sendGroupIM(groupuuid, message);

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | groupuuid | yes | the UUID of the group |
|     | message | yes | the text to send (can contain international characters) |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |

1.  This command does not return FAIL if your bot has no "Join Group Chat" ability. Pay attention to the bot's group permissions while using this command.
2.  The message delivery is guaranteed even if bot is offline (the message will be sent when bot comes online)
