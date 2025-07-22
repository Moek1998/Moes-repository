# replyDialog - SmartBots Developers Docs

Virtually "presses" a pop-up dialog button (which was displayed by an in-world script).

Bot.replyDialog(channel, object, button);

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | channel | yes | The dialog channel (either positive or negative value) |
|     | object | yes | UUID of the object which sent us the dialog |
|     | button | yes | The text of the dialog button to press |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |

## Examples

Bot.on("script\_dialog", function(event) {
	Bot.replyDialog(event.channel, event.object\_uuid, event.buttons\[0\]);
	console.log("Got an dialog and answered with the first button: " + event.buttons\[0\]);
});
