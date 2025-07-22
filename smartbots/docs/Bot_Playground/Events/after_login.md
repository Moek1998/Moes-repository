# after\_login - SmartBots Developers Docs

Fires when bot successfully logged to Second Life.

Bot.on("after\_login", function(event) { ... });

## Reference

This event comes with the following _event_ object:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| _event_ object properties: |     |     |     |
|     | \-- none -- |     | Event has no properties |

This event fires after bot logged into Second Life. This is a pair for a [before\_login](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/before_login "Bot Playground/Events/before login") event.

## Example

Bot.on("after\_login", function(event) {
	console.log("Bot is successfully logged in!");
});

More complex example can be found here: [Logging out and back in](https://www.mysmartbots.com/dev/docs/Bot_Playground/Examples/Logging_out_and_back_in "Bot Playground/Examples/Logging out and back in")
