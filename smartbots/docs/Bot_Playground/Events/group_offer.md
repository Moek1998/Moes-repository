# group\_offer - SmartBots Developers Docs

Fires when bot receives a group invite

Bot.on("group\_offer", function(event) { ... });

## Reference

This event comes with the following _event_ object:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| _event_ object properties: |     |     |     |
|     | name |     | The name of the event in this case group\_offer |
|     | avatar\_name |     | The name of the sender |
|     | avatar\_uuid |     | Sender's UUID |
|     | group\_name |     | The name of the group |
|     | group\_uuid |     | The UUID of the group |
|     | session\_id |     | Session ID to accept invitation |
|     | system\_message |     | SL system message |

## Example

Bot.on("group\_offer", function(event) {
	console.log(event.avatar\_name + " invited me to group: \\n" + event.group\_name);
});

console.log("Bot is listening, group invites");
