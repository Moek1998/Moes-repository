# giveMoney - SmartBots Developers Docs

From SmartBots Developers Docs

Jump to: [navigation](#mw-head), [search](#p-search)

Commands bot to send money (L$) to specific avatar.

Bot.giveMoney(avatar, amount, comment);

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| giveMoney: |     |     |     |
|     | avatar | yes | The avatar UUID. |
|     | amount | yes | The amount of money to give. |
|     | comment | (optional) | Text comment for the money transaction. |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |

## Examples

For a comprehensive balance management script check the [code in Examples section](https://www.mysmartbots.com/dev/docs/Bot_Playground/Examples/Working_with_bot_money_balance "Bot Playground/Examples/Working with bot money balance").

## See also

*   [getBalance()](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/getBalance "Bot Playground/Commands/getBalance")
*   [giveInventory()](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/giveInventory "Bot Playground/Commands/giveInventory")
