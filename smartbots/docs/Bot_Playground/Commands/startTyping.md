# startTyping - SmartBots Developers Docs

From SmartBots Developers Docs

Jump to: [navigation](#mw-head), [search](#p-search)

Sends "typing" in chat to a specific user.

Bot.startTyping(uuid, delay);

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | uuid | yes | The uuid to send the "typing" in chat |
|     | delay | optional | The delay option to determine how long the "typing" in chat stays. Defaults to 15 seconds. |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |

## Examples

Bot.startTyping(1fd5b697\-604c\-4e34\-91f9\-f5c98cc46fa3, "20");
