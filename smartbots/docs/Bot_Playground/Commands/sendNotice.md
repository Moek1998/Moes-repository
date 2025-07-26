# sendNotice - SmartBots Developers Docs

Sends a notice to the group.

Bot.sendNotice(groupuuid, subject, text, attachment);

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | groupuuid | yes | the UUID of the group |
|     | subject | yes | the subject of the notice (can't contain international characters) |
|     | text | yes | the text of the notice (can contain international characters) |
|     | attachment | optional | inventory UUID of the attachment (see below) |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |

1.  This command does not return FAIL if your bot has no "Send Group Notice" ability. Pay attention to bot's group permissions while using this command.
2.  The notice delivery is guaranteed even if the bot is offline (the invitation will be sent after bot comes online)

## Attachments

The notice attachment can be taken from the bot's inventory. To make an attachment, proceed with the following steps:

1.  Set copy+transfer permissions to the object (so bot can give it with notice)
2.  Drop object to the bot in Second Life
3.  Open SmartBots account, click "manage bot":
4.  Open bot's inventory browser:
5.  Copy the "inventory UUID" of the required inventory item.
