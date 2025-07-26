# inventory\_offer - SmartBots Developers Docs

Fires when bot receives a inventory offer

Bot.on("inventory\_offer", function(event) { ... });

## Reference

This event comes with the following _event_ object:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| _event_ object properties: |     |     |     |
|     | name |     | name of the event in this case inventory\_offer |
|     | item\_type |     | type of the inventory item eg:<br><br>*   Notecard,<br>*   Object,<br>*   Landmark... |
|     | folder |     | inventory folder UUID this item goes to |
|     | sender\_type |     | type of the sender AGENT or OBJECT |
|     | sender\_name |     | name of the sender |
|     | sender\_uuid |     | UUID of the sender |
|     | item\_name |     | name of the offered item |
|     | object\_id |     | inventory UUID of the item being offered |
|     | item\_creator |     | The UUID of the creator from the invetory item. |
|     | session |     | Session UUID to accept the item. |

## Example

Bot.on("inventory\_offer", function(event) {
	console.log(event.sender\_name + " send me an " + event.item\_type + " with the name: \\n" + event.item\_name);
});

console.log("Bot is listening to inventory offers");
