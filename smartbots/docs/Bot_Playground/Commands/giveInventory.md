# giveInventory - SmartBots Developers Docs

Commands bot to send an inventory item or folder to specific avatar.

Bot.giveInventory(avatar, object);

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| giveInventory: |     |     |     |
|     | avatar | yes | The avatar UUID. |
|     | object | yes | The inventory or folder UUID of the item. Use the [Personal Bot Control Panel](http://www.mysmartbots.com/docs/Personal_Bot_Control_Panel) to get this UUID. |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |

## Error messages

Bot checks the permissions of the item before doing the delivery. The following error message is being returned if object is no-trans:

_transfer permission not set_

This does **not** apply for folders. Empty folder is being delivered if no transferable items found.

1.  The inventory is loading each time your bot restarts. Allow about 60 seconds for inventory to completely load.
2.  Bot automatically recognizes the inventory folders and delivers them accordingly.
3.  The commands freezes for about 15 seconds if object UUID is not exists in bot's inventory. To avoid this make sure you are using correct UUIDs.

## Examples

Bot.giveInventory(avatar, object)
.then(function(result) {
  if(result.success) {
    console.log("The inventory item was send.");
  } else {
    console.log("Error executing giveInventory: " + result.error);
  }
});
