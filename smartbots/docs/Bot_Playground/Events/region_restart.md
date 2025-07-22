# region\_restart - SmartBots Developers Docs

Fires when bot receives a region restart notification. **Not available for QubicBot yet [(?)](https://www.mysmartbots.com/dev/docs/New_features_and_QubicBot "New features and QubicBot")**

Bot.on("region\_restart", function(event) { ... });

## Reference

This event comes with the following _event_ object:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| _event_ object properties: |     |     |     |
|     | name |     | The name of the event in this case region\_restart |
|     | message |     | The message of the region\_restart |
|     | bot\_uuid |     | The UUID of the bot which receives the notification. |
|     | region\_name |     | The name of the region going to restart. |
|     | time\_units |     | Unit of Time in which region is going to restart:<br><br>*   Seconds<br>*   Minutes |
|     | time\_left |     | Amount of time till region restart based on time\_units. |
|     | seconds\_left |     | Amount of time till region restart in seconds. |

*   time\_left contains time till restart in time\_units
*   time\_units are “Seconds”, “Minutes” - Unknown is sent when anything other is received.
*   seconds\_left is time till restart in seconds

## Example

console.log(\`${process.name} started\`);

Bot.on("region\_restart", (event) \=> {
    console.log(\`Region restart event:\`, event);
});

Also see a [complex region restart script](https://www.mysmartbots.com/dev/docs/Bot_Playground/Examples/Region_restart "Bot Playground/Examples/Region restart") in Examples.
