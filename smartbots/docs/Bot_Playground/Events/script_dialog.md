# script\_dialog - SmartBots Developers Docs

Fires when bot receives a scripted dialog with a menu buttons

Bot.on("script\_dialog", function(event) { ... });

Use [replyDialog](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/replyDialog "Bot Playground/Commands/replyDialog") to "click" a required menu button.

## Reference

This event comes with the following _event_ object:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| _event_ object properties: |     |     |     |
|     | name |     | The name of the event in this case script\_dialog |
|     | buttons | Array | The selection options (buttons) as array |
|     | channel | integer | The channel on which the dialog listen to. |
|     | owner\_name |     | The owner name from object that sent the dialog. |
|     | text |     | The text in the dialog window |
|     | object\_uuid |     | The UUID of the object that sent the dialog. |
|     | object\_name |     | The name of the object that sent the dialog. |

## Example

Bot.on("script\_dialog", function(event) {
	console.log("Got a dialog:\\n" +
		event.text + "\\n\\n" +
		"channel: " + event.channel + "\\n" +
		"buttons:\\n" + event.buttons.join("\\n"));
});
