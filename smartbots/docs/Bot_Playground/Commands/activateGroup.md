# activateGroup - SmartBots Developers Docs

Activates a specific group (for example, to get build rights on the parcel).

Bot.activateGroup(groupuuid);

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | groupuuid | yes | the UUID of the group to activate<br><br>**Special values:**<br><br>*   _LAND_ - set the group to the current parcel's group (see examples)<br>*   _00000000-0000-0000-0000-000000000000_ - remove active group<br><br>Obliviously, the bot has to be a member of the group already to activate it. |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |

## Examples

1\. Set the active group to match current parcel's group. This can be used to get rights to rez items.

Bot.activateGroup("LAND");

2\. Remove active group from the bot (sets the active group to none):

Bot.activateGroup("00000000-0000-0000-0000-000000000000");
