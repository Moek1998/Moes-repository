# chat\_message - SmartBots Developers Docs

Fires when bot receives a message in the local chat

Bot.on("chat\_message", function(event) { ... });

## Reference

This event comes with the following _event_ object:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| _event_ object properties: |     |     |     |
|     | name |     | The name of the event |
|     | speaker\_type |     | The sender of the message. Can be AGENT or OBJECT |
|     | speaker\_name |     | The name of the sender |
|     | speaker\_uuid |     | The UUID of the sender |
|     | speaker\_owner |     | The UUID of the owner of the sender object. |
|     | message |     | The text of the message |
|     | chat\_type |     | One of the following: Normal, Whisper, Shout, OwnerSay |
|     | own\_message |     | If this message has been said by the bot itself |

## Important note

Bot DOES hear what it says, so you will get a _chat\_message_ event when bot says something in local chat.

Make sure to ignore bot's own messages (especially for auto-responders)! See the example below.

## Example

Bot.on("chat\_message", function(event) {
	// Ignore own messages
	if(event.own\_message) { return; }

	console.log(event.speaker\_name + " says: \\n" + event.message);
});

console.log("Bot is listening for local chat");
