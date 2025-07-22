# group\_im - SmartBots Developers Docs

From SmartBots Developers Docs

Jump to: [navigation](#mw-head), [search](#p-search)

Fires when bot receives a group chat message.

Bot.on("group\_im", function(event) { ... });

## Reference

This event comes with the following _event_ object:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| _event_ object properties: |     |     |     |
|     | name |     | The name of the event in this case group\_im |
|     | group\_name |     | The same of the group |
|     | group\_uuid |     | The UUUID of the group |
|     | speaker\_name |     | The name of the sender |
|     | speaker\_uuid |     | The UUID of the sender |
|     | message |     | The text of the message |

## Example

Bot.on("group\_im", function(event) {
  console.log(event.group\_name + ": " + event.speaker\_name +" says: \\n" + event.message);
});

console.log("Bot is listening to group chat.");
