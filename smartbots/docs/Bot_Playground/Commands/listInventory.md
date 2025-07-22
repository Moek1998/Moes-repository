# listInventory - SmartBots Developers Docs

Returns a list of the Second Life groups the bot is member of.

Bot.listGroups(folderUUID).then(function(result) { ... });

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | uuid | yes | The UUID of the folder. Leave blank for root folder contents. |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |
|     | list | Array | An array containing selected folder items. Each array item is:<br><br>{<br> type: _item type (see below)_,<br> name: _inventory item name_,<br> inventoryUUID: _the UUID of the inventory item_,<br> assetUUID: _this asset UUID (unique id of the object in SL, see below)_,<br> flags: _WORN - item is being worn_,<br> permissions: _permission object (see below)_,<br> nextPermissions: _next owner permissions, similar to above_<br>}<br><br>**Item type:**  <br>a string which shows what kind of item is it: "folder", "object", "notecard", "clothing" etc.<br><br>**Permissions object format:**<br><br>{<br> mod: _true/false_,<br> copy: _true/false_,<br> transfer: _true/false_<br>} |

### Useful folders

If you need to know what your bot is currently wearing, find the "Current Outfit" folder in a root of the inventory.

### Inventory-ID vs Asset-ID

There's a huge difference between "inventory ID" and "asset ID":

*   "Inventory ID" is an id of the object in **avatar's personal** inventory.
*   "Asset ID" is a **global id** of the item within SL database ("asset server").

Therefore, you may have two identical textures in the bots inventory: they will have a different Inventory-ID but the same Asset-ID (because they point to the same image on the SL server).

So, the rules are:

*   When you rez an item from **inventory**, you need to pick up an object by Inventory-ID. You rez specific object.
*   When the script sets a texture to a face, it uses Asset-ID (because scripts have no access to your inventory! It just tells SL to fetch a specific image from the global database)

## Examples

See the [Currently worn items](https://www.mysmartbots.com/dev/docs/Bot_Playground/Examples/Listing_worn_items "Bot Playground/Examples/Listing worn items") scripts in our Playground Examples section.
