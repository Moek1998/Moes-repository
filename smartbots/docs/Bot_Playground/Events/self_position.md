# self\_position - SmartBots Developers Docs

Fires when bot in-world location, position or heading changes. **Not available for QubicBot yet [(?)](https://www.mysmartbots.com/dev/docs/New_features_and_QubicBot "New features and QubicBot")**

Bot.on("self\_position", function(event) { ... });

## Reference

This event comes with the following _event_ object:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| _event_ object properties: |     |     |     |
|     | name |     | The name of the event in this case region\_restart |
|     | region |     | The name of the region the bot is at. |
|     | heading |     | The direction in degrees where the bot is facing. |
|     | bot\_uuid |     | The UUID of the bot. |
|     | active\_group |     | The active group uuid of the bot. |
|     | position |     | The current position of the bot.<br><br>Position Format:<br><br>*   X<br>*   Y<br>*   Z |

The event fires when bot's position and/or view direction changes. The view direction change threshold is 5 degrees (thus, you won't get a notification if bot turns for less than 5 degrees).

The event is usually sent real time but can be postponed to avoid flooding your script with self\_position event.

## Example

console.log(\`${process.name} started\`);

Bot.on("self\_position", (event) \=> {
    console.log(\`self position event:\`, event);
});
