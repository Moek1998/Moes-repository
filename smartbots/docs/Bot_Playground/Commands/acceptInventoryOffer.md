# acceptInventoryOffer - SmartBots Developers Docs

Accept (or reject) an inventory offer sent by other avatar or in-world script.

Bot.on("inventory\_offer", (event) \=> {
  Bot.acceptInventoryOffer(
    event.sender\_type,
    event.object\_id,
    event.sender\_uuid,
    event.folder,
    event.session,
    true
  );
});

See [inventory\_offer](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/inventory_offer "Bot Playground/Events/inventory offer") event for details.

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | sender\_type | yes | who sent us an inventory (agent or in-world script) |
|     | object\_id | yes | inventory UUID of the item being offered |
|     | sender\_uuid | yes | UUID of the sender |
|     | folder | yes | inventory folder UUID this item goes to |
|     | session | yes | session UUID from the event |
|     | accept | yes | true to accept item, false to reject. |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |
