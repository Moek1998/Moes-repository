# takeInworldPrim - SmartBots Developers Docs

Takes (de-rezzes) or copies in-world prim into bot's inventory. **Not available for QubicBot yet [(?)](https://www.mysmartbots.com/dev/docs/New_features_and_QubicBot "New features and QubicBot")**

Bot.takeInworldPrim(operation, objectUUID, folderUUID);

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | operation | yes | one of the following values:<br><br>*   take - to take object from the world completely<br>*   copy - to take a copy of the object |
|     | objectUUID | yes | the UUID of the in-world object |
|     | folderUUID | yes | (optional) UUID of the folder to put object to. "Objects" folder will be used if not specified. |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |

## Return value

**Important:** the command does not checks for the operation success.

Your bot has to have rights to grab the object specified (own it, or have permissions an owner's friend).

## Examples

Touch a special test attachment object (contact SmartBots support to get it):

// Take (de-rez) in-world object to the default ("Objects") folder
Bot.takeInworldPrim("take", "bd36c29f-8a14-4350-b648-3e0f50b6d32a");
