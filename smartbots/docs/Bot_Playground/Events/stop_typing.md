# stop\_typing - SmartBots Developers Docs

Fires when another avatar stops typing in IM to the bot. **Not available for QubicBot yet [(?)](https://www.mysmartbots.com/dev/docs/New_features_and_QubicBot "New features and QubicBot")**

Bot.on("stop\_typing", function(event) { ... });

## Reference

This event comes with the following _event_ object:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| _event_ object properties: |     |     |     |
|     | name |     | The name of the event in this case stop\_typing |
|     | speaker\_name |     | The name of the sender |
|     | speaker\_uuid |     | The UUID of the sender |
|     | bot\_slname |     | The name of the bot |
|     | bot\_uuid |     | The uuid of the bot |

## Example

Bot.on("stop\_typing", event \=> {
  console.log(\`${event.speaker\_name} stopped typing\`);
});

console.log("Bot is listening, IM something");
