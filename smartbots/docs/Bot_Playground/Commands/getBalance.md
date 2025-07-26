# getBalance - SmartBots Developers Docs

From SmartBots Developers Docs

Jump to: [navigation](#mw-head), [search](#p-search)

Retrieves the current bot's L$ balance.

Bot.getBalance(function(result) {
  console.log("I have L$" + result.balance);
});

or using a Promise:

Bot.getBalance()
  .then(function(result) {
    console.log("I have L$" + result.balance);
  });

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| getBalance: |     |     |     |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |

## Examples

For a comprehensive balance management script check the [code in Examples section](https://www.mysmartbots.com/dev/docs/Bot_Playground/Examples/Working_with_bot_money_balance "Bot Playground/Examples/Working with bot money balance").

## See also

*   [giveMoney()](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/giveMoney "Bot Playground/Commands/giveMoney")
