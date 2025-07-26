# region\_restart\_cancelled - SmartBots Developers Docs

Fires when bot receives a region restart cancellation notification. **Not available for QubicBot yet [(?)](https://www.mysmartbots.com/dev/docs/New_features_and_QubicBot "New features and QubicBot")**

Bot.on("region\_restart\_cancelled", function(event) { ... });

## Reference

This event comes with the following _event_ object:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| _event_ object properties: |     |     |     |
|     | name |     | The name of the event in this case region\_restart\_cancelled |
|     | bot\_uuid |     | The UUID of the bot which receives the notification. |
|     | message |     | The message of the region\_restart\_cancelled |
|     | region\_name |     | The name of the region. |

## Example

console.log(\`${process.name} started\`);

Bot.on("region\_restart\_cancelled", (event) \=> {
    console.log(\`Region restart cancelled:\`, event);
});

Also see [complex region restart script](https://www.mysmartbots.com/dev/docs/Bot_Playground/Examples/Region_restart "Bot Playground/Examples/Region restart").
