# friendship\_offer - SmartBots Developers Docs

Fires when bot receives a friendship offer

Bot.on("friendship\_offer", function(event) { ... });

## Reference

This event comes with the following _event_ object:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| _event_ object properties: |     |     |     |
|     | avatar\_name |     | name of the sender |
|     | avatar\_uuid |     | UUID of the sender |
|     | message |     | Text message sent along with the offer |
|     | session\_id |     | Session UUID to accept an offer. |

## See also

Use [acceptFriendshipOffer](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/acceptFriendshipOffer "Bot Playground/Commands/acceptFriendshipOffer") command to accept an offer.

## Example

Bot.on("friendship\_offer", function(event) {
	console.log(\`${event.avatar\_name} offer friendship and says: ${event.message}\`);
});

console.log("Bot is listening to friendship offers");
