# wear - SmartBots Developers Docs

From SmartBots Developers Docs

Jump to: [navigation](#mw-head), [search](#p-search)

Commands bot to wear a clothing item, body part or attach an object.

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| wear: |     |     |     |
|     | uuid | yes | The inventory UUID of the item. Use the [Personal Bot Control Panel](http://www.mysmartbots.com/docs/Personal_Bot_Control_Panel) to get this UUID. |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |
