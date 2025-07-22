# teleport\_status - SmartBots Developers Docs

Fires when bot teleports, indicating various stages of the teleport. **Not available for QubicBot yet [(?)](https://www.mysmartbots.com/dev/docs/New_features_and_QubicBot "New features and QubicBot")**

Bot.on("teleport\_status", function(event) { ... });

## Reference

This event comes with the following _event_ object:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| _event_ object properties: |     |     |     |
|     | name |     | The name of the event in this case teleport\_status |
|     | bot\_name |     | The name of the bot teleporting. |
|     | message |     | The status message of the teleport |
|     | status |     | The status of the teleport. (Start/Progress/Finished) |
|     | bot\_uuid |     | The UUID of the bot teleporting. |
|     | location |     | The current location of the bot. |

## Example

console.log(\`${process.name} started\`);

Bot.on("teleport\_status", (event) \=> {
    console.log(\`teleport status event: \`, event);
});
