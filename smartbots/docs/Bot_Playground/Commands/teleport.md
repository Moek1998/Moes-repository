# teleport - SmartBots Developers Docs

Teleports bot to specific location.

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| teleport: |     |     |     |
|     | location | yes | address of the new location<br><br>Format: _Region name/X/Y/Z_<br><br>Use _HOME_ instead of location to send the bot home (see examples below). |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |

## Examples

Teleport bot to SmartBots office:

Bot.teleport("DuoLife/128/128/20");

Teleport bot to its home location:
