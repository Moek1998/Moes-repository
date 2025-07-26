# autopilot\_stuck - SmartBots Developers Docs

Fires when bot autopilot gets stuck and gives up moving further. **Not available for QubicBot yet [(?)](https://www.mysmartbots.com/dev/docs/New_features_and_QubicBot "New features and QubicBot")**

Bot.on("autopilot\_stuck", function(event) { ... });

See [Bot.walkTo()](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/walkTo "Bot Playground/Commands/walkTo") command for autopilot usage.

## Reference

This event comes with the following _event_ object:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| _event_ object properties: |     |     |     |
|     | name |     | The name of the event |
|     | bot\_name |     | The name of the bot teleporting. |
|     | endPoint |     | Bot planned destination point, { X, Y, Z } |
|     | actualPoint |     | Bot actual location, { X, Y, Z } |

## Example

console.log(\`${process.name} started\`);

Bot.on("autopilot\_stuck", (event) \=> {
	console.log(\`Autopilot stuck: ${JSON.stringify(event, null, 2)}\`);
});

/\*
Autopilot stuck: {
  "name": "autopilot\_stuck",
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
