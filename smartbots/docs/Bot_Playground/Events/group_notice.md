# group\_notice - SmartBots Developers Docs

Fires when bot receives a group notice.

Bot.on("group\_notice", function(event) { ... });

## Reference

This event comes with the following _event_ object:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| _event_ object properties: |     |     |     |
|     | name |     | The name of the event in this case group\_notice |
|     | group\_name |     | The name of the group |
|     | group\_uuid |     | The UUID of the group |
|     | speaker\_name |     | The name of the sender |
|     | speaker\_uuid |     | The UUID of the sender |
|     | subject |     | The subject of the notice |
|     | message |     | The message of the notice |
|     | attachment |     | The attachment type of the notice:<br><br>*   Object<br>*   Notecard<br>*   Landmark<br>*   Texture |

## Example

Bot.on("group\_notice", function(event) {
  console.log(event.group\_name + ": " + event.speaker\_name +" sent notice: \\n message: " + event.message + "\\n subject: " + event.subject);
});

console.log("Bot is listening, to group notice.");
