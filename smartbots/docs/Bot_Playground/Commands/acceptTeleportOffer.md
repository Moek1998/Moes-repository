# acceptTeleportOffer - SmartBots Developers Docs

Accept (or reject) a teleport offer sent by other avatar.

Bot.on("teleport\_offer", (event) \=> {
  Bot.acceptTeleportOffer(event.avatar\_uuid, event.session\_id, true);
});

See [teleport\_offer](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/teleport_offer "Bot Playground/Events/teleport offer") event for details.

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | avatar\_uuid | yes | sender avatar UUID |
|     | session\_id | yes | session UUID from the event |
|     | accept | yes | true to accept an offer, false to reject. |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |

## Notes

*   Bot cannot reject teleport offers from Bot Owner.

## Example

Bot.on("teleport\_offer", async function(event) {
  console.log("Got teleport offer from: " + event.avatar\_name + "\\n\\nAccepting now.");
  let response \= await Bot.acceptTeleportOffer(event.avatar\_uuid, event.session\_id, true);
  if(response.success)
  {
    console.log("Accepted the Teleport Offer");
  } else {
    console.log("Rejected the Teleport Offer");
    console.error("Error: " + response.error)
  }
});

console.log("Bot is listening, teleport offers");

[<< return back to Bot commands](https://www.mysmartbots.com/dev/docs/HTTP_API/Bot_Commands "HTTP API/Bot Commands")

_(Miss an API call or parameter? [Submit your request in forum](https://www.mysmartbots.com/dev/forums/forum/developing-with-smartbots-2/http-api/))_
