# move - SmartBots Developers Docs

Start or stop bot movement and rotations.

Bot.move(instruction, state);

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | instruction | yes | The movement instruction. One of the following:<br><br>*   FORWARD - start/stop the forward movement<br>*   BACKWARD - start/stop the backward movement<br>*   LEFT - start/stop turning to the left<br>*   RIGHT - start/stop turning to the right<br>*   FLY - start/stop flying<br>*   STOP - stops all movements |
|     | state | yes | value which controls the "instruction" completion:<br><br>*   START - starts "instruction"<br>*   STOP - stops "instruction" |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |

## Details

This function allows establishing a direct control over bot's movement.

This function may be a bit laggy, and you might find [Bot.walkTo()](https://www.mysmartbots.com/dev/docs/index.php?title=Bot_Playground/Command/walkTo&action=edit&redlink=1 "Bot Playground/Command/walkTo (page does not exist)") command to be more precise. However, use this command if you want a direct control over the bot's movement.

Related events:

*   [self\_position](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/self_position "Bot Playground/Events/self position") event will deliver you the bot position while it changes

## Examples

Bot.move("FORWARD", "START");

// Walk forward for 2 seconds
await process.sleep(2\_000);

Bot.move("FORWARD", "STOP");
