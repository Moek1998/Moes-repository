# instant\_message - SmartBots Developers Docs

Fires when bot receives a message from another avatar or in-world object.

Bot.on("instant\_message", function(event) { ... });

## Reference

This event comes with the following _event_ object:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| _event_ object properties: |     |     |     |
|     | name |     | The name of the event in this case instant\_message |
|     | speaker\_type |     | The sender of the message. Can be AVATAR or OBJECT |
|     | speaker\_name |     | The name of the sender |
|     | speaker\_uuid |     | The UUID of the sender |
|     | message |     | The text of the message |

## Example

Bot.on("instant\_message", function(event) {
	console.log(event.speaker\_name + " says: \\n" + event.message);
});

console.log("Bot is listening, IM something");
