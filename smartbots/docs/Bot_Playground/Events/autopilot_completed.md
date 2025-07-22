# autopilot\_completed - SmartBots Developers Docs

Fires when bot autopilot successfully completes its journey. **Not available for QubicBot yet [(?)](https://www.mysmartbots.com/dev/docs/New_features_and_QubicBot "New features and QubicBot")**

Bot.on("autopilot\_completed", function(event) { ... });

See [Bot.walkTo()](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/walkTo "Bot Playground/Commands/walkTo") command for autopilot usage.

## Reference

This event comes with the following _event_ object:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| _event_ object properties: |     |     |     |
|     | name |     | The name of the event |
|     | bot\_name |     | The name of the bot teleporting. |
|     | endPoint |     | Bot destination point, { X, Y, Z } |
|     | actualPoint |     | Bot actual location, { X, Y, Z } |

## Example

console.log(\`${process.name} started\`);

Bot.on("autopilot\_completed", (event) \=> {
	console.log(\`Autopilot started: ${JSON.stringify(event, null, 2)}\`);
});

/\*
Autopilot completed: {
  "name": "autopilot\_completed",
  "bot\_slname": "DakotahRaine Resident",
  "bot\_uuid": "4f6b8999-14a0-4f50-882d-a764ee913daa",
  "endPoint": {
    "X": 212,
    "Y": 25,
    "Z": 93
  },
  "actualPoint": {
    "X": 203.21446,
    "Y": 36.776222,
    "Z": 93.68485
  }
}
\*/
