# acceptGroupOffer - SmartBots Developers Docs

Accept (or reject) a group invitation sent by other avatar.

Bot.on("group\_offer", (event) \=> {
  Bot.acceptGroupOffer(event.avatar\_uuid, event.session\_id, true);
});

See [group\_offer](https://www.mysmartbots.com/dev/docs/index.php?title=Bot_Playground/Commands/acceptGroupOffer/Bot_Playground/Events/group_offer&action=edit&redlink=1 "Bot Playground/Commands/acceptGroupOffer/Bot Playground/Events/group offer (page does not exist)") event for details.

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | avatar\_uuid | yes | sender avatar UUID |
|     | session\_id | yes | session UUID from the event |
|     | accept | yes | true to accept invitation, false to reject. |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |
