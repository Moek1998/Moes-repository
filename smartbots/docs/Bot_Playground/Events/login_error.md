# login\_error - SmartBots Developers Docs

Fires when bot is unable to login to Second Life. **Not available for QubicBot yet [(?)](https://www.mysmartbots.com/dev/docs/New_features_and_QubicBot "New features and QubicBot")**

Bot.on("login\_error", function(event) { ... });

## Reference

This event comes with the following _event_ object:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| _event_ object properties: |     |     |     |
|     | reason |     | The login error text from Second Life servers |

If bot logs in for the first time (or because of some other reasons) the bot\_uuid field may have zero UUID.

## Example

Bot.on("login\_error", (event) \=> {
  console.log("Error logging in:", event.reason);
});

Bot.on("after\_login", (event) \=> {
  console.log("Bot is successfully logged in!");
});

console.log("Waiting for bot to log in");
