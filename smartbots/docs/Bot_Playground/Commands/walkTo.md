# walkTo - SmartBots Developers Docs

Walk to a position within the current region.

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | x   | yes | The X coordinate of the destination point |
|     | y   | yes | The Y coordinate of the destination point |
|     | z   | yes | The Z coordinate of the destination point |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |

## Details

Bot does not "navigate" to the point. Instead, it walks straight to the specified point, pushing into all obstacles on the way. Just like you keep pressing "arrow up" button on your keyboard.

If bot gets stuck for 2 seconds (for example, hitting the wall), the autopiloting ends.

You can use [fly](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/fly "Bot Playground/Commands/fly") command to start flying and reach the higher destination point.

These events deliver the autopilot status:

*   [autopilot\_started](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/autopilot_started "Bot Playground/Events/autopilot started") - autopilot started
*   [autopilot\_completed](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/autopilot_completed "Bot Playground/Events/autopilot completed") - autopilot reached destination point
*   [autopilot\_stuck](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/autopilot_stuck "Bot Playground/Events/autopilot stuck") - autopilot got stuck (and stopped)

## Examples

// Bots Playground script: \[TEST\] Autopilot events (build 1 by Glaznah Gassner)
Bot.on("autopilot\_completed", (event) \=> {
	console.log(\`Autopilot completed: ${JSON.stringify(event, null, 2)}\`);
});

Bot.on("autopilot\_stuck", (event) \=> {
	console.log(\`Autopilot stuck: ${JSON.stringify(event, null, 2)}\`);
});

console.log("Script is running, waiting for autopilot events");

// Start autopilot
Bot.walkTo(203, 37, 93);

// Gracefully end test script in 10 seconds
setTimeout(() \=> process.exit(), 10\_000);

/\*
clear
07/12/2023 13:28:39
Script is running, waiting for autopilot events

07/12/2023 13:28:42
Autopilot completed: {
  "name": "autopilot\_completed",
  "bot\_slname": "DakotahRaine Resident",
  "bot\_uuid": "4f6b8999-14a0-4f50-882d-a764ee913daa",
  "endPoint": {
    "X": 203,
    "Y": 37,
    "Z": 93
  },
  "actualPoint": {
    "X": 203.21898,
    "Y": 36.799942,
    "Z": 93
  }
}
\*/
