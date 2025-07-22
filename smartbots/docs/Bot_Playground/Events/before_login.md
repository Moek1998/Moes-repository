# before\_login - SmartBots Developers Docs

Fires when bot is going to login to Second Life.

Bot.on("before\_login", function(event) { ... });

## Reference

This event comes with the following _event_ object:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| _event_ object properties: |     |     |     |
|     | \-- none -- |     | Event has no properties |

This event fires right before bot tries to login to Second Life. This is a pair for [after\_login](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/after_login "Bot Playground/Events/after login") event, but they are not the same: remember that login procedure may fail (for example, because of wrong password).

## Example

Bot.on("before\_login", function(event) {
	console.log("Bot is going to login. Lets see if password is right!");
});

More complex example can be found here: [Logging out and back in](https://www.mysmartbots.com/dev/docs/Bot_Playground/Examples/Logging_out_and_back_in "Bot Playground/Examples/Logging out and back in")
