# after\_logout - SmartBots Developers Docs

Fires after bot goes offline. **Not available for QubicBot yet [(?)](https://www.mysmartbots.com/dev/docs/New_features_and_QubicBot "New features and QubicBot")**

Bot.on("after\_logout", function(event) { ... });

## Reference

This event comes with the following _event_ object:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| _event_ object properties: |     |     |     |
|     | \-- none -- |     | Event has no properties |

This event fires after a bot goes offline.

## Example

Bot.on("after\_logout", function(event) {
	console.log("I went offline. See you later.");
});

More complex example can be found here: [Logging out and back in](https://www.mysmartbots.com/dev/docs/Bot_Playground/Examples/Logging_out_and_back_in "Bot Playground/Examples/Logging out and back in")
