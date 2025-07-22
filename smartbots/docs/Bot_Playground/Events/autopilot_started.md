# autopilot\_started - SmartBots Developers Docs

Fires when bot autopilot starts. **Not available for QubicBot yet [(?)](https://www.mysmartbots.com/dev/docs/New_features_and_QubicBot "New features and QubicBot")**

Bot.on("autopilot\_started", function(event) { ... });

See [Bot.walkTo()](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/walkTo "Bot Playground/Commands/walkTo") command for autopilot usage.

## Reference

This event comes with the following _event_ object:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| _event_ object properties: |     |     |     |
|     | name |     | The name of the event |
|     | bot\_name |     | The name of the bot teleporting. |
|     | currentPoint |     | Bot current location, { X, Y, Z } |
|     | endPoint |     | Bot destination point, { X, Y, Z } |

## Example

console.log(\`${process.name} started\`);

Bot.on("autopilot\_started", (event) \=> {
	console.log(\`Autopilot started: ${JSON.stringify(event, null, 2)}\`);
});

/\*
Autopilot started: {
  "name": "autopilot\_started",
  "bot\_slname": "DakotahRaine Resident",
  "bot\_uuid": "4f6b8999-14a0-4f50-882d-a764ee913daa",
  "endPoint": {
    "X": 212,
    "Y": 25,
    "Z": 93
  },
  "currentPoint": {
    "X": 203.21446,
    "Y": 36.776222,
    "Z": 93.68485
  }
}
\*/
