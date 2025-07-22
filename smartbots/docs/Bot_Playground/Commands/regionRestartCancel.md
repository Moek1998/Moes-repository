# regionRestartCancel - SmartBots Developers Docs

From SmartBots Developers Docs

Jump to: [navigation](#mw-head), [search](#p-search)

Cancels pending restart of current region

Bot.regionRestart(delay);

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |

## Permissions

The bot has to be an Estate Manager of the current region.

## Examples

See a [complex region restart script](https://www.mysmartbots.com/dev/docs/Bot_Playground/Examples/Region_restart "Bot Playground/Examples/Region restart") in Examples.
