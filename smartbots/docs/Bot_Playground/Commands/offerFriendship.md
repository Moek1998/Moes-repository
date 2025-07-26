# offerFriendship - SmartBots Developers Docs

From SmartBots Developers Docs

Jump to: [navigation](#mw-head), [search](#p-search)

Offers friendship to a resident.

Bot.offerFriendship(avatar, message);

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| offerFriendship: |     |     |     |
|     | avatar | yes | the UUID of the resident |
|     | message |     | optional message to send |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |
