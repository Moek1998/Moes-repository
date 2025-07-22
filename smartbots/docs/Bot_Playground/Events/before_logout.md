# before\_logout - SmartBots Developers Docs

Fires when bot is going offline.

Bot.on("before\_login", function(event) { ... });

## Reference

This event comes with the following _event_ object:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| _event_ object properties: |     |     |     |
|     | \-- none -- |     | Event has no properties |

This event fires right before bot goes offline. Actually, the logout process starts immediately, so you can't interact with Second Life (e.g. send IMs) within this event. However, you can use [console.log()](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/console.log "Bot Playground/Commands/console.log") and all Bots Playground functionality.

## Example

Bot.on("before\_logout", function(event) {
	console.log("I'm going offline. See you later.");
});

More complex example can be found here: [Logging out and back in](https://www.mysmartbots.com/dev/docs/Bot_Playground/Examples/Logging_out_and_back_in "Bot Playground/Examples/Logging out and back in")
