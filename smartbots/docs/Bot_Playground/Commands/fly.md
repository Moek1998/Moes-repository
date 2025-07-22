# fly - SmartBots Developers Docs

From SmartBots Developers Docs

Jump to: [navigation](#mw-head), [search](#p-search)

Starts or stops flying.

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | enableFlying | yes | boolean, true to start flying, false to stom |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |

## Examples

// Bots Playground script: \[TEST\] Fly (build 1 by Glaznah Gassner)
Bot.fly(true);

// Wait a bit and stop flying
await process.sleep(5\_000);

Bot.fly(false);

// Gracefully exit the test script
process.exit();
