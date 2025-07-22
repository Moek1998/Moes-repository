# balance\_changed - SmartBots Developers Docs

Fires when bot receives or payd money

Bot.on("balance\_changed", function(event) { ... });

## Reference

This event comes with the following _event_ object:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| _event_ object properties: |     |     |     |
|     | name |     | The name of the event in this case balance\_changed |
|     | amount |     | The amount which was paid or received. |
|     | direction |     | The direction of the money flow, can be:<br><br>INITIAL: bot has logged in, balance is known now  <br>INCOMING: money has arrived  <br>OUTGOING: money has been sent |
|     | source |     | The UUID of the money sender |
|     | destination |     | The UUID of the money receiver |
|     | balance |     | The current balance after the payment |
|     | trx\_type |     | The transaction type |
|     | comment |     | Transaction comment |
|     | transaction |     | Transaction UUID |

## Example

Bot.on("balance\_changed", function(event) {
	console.log("Balance changed, my new balance is: " + event.balance);
});

console.log("Bot is listening to payments");
