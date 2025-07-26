# acceptFriendshipOffer - SmartBots Developers Docs

Accept (or reject) a friendship offer sent by other avatar.

Bot.on("friendship\_offer", (event) \=> {
  Bot.acceptFriendshipOffer(event.avatar\_uuid, event.session\_id, true);
});

See [friendship\_offer](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/friendship_offer "Bot Playground/Events/friendship offer") event for details.

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

## Example

Bot.on("friendship\_offer", async function(event) {
  console.log("Got friendship offer from: " + event.avatar\_name + "\\n\\nAccepting now.");
  let response \= await Bot.acceptFriendshipOffer(event.avatar\_uuid, event.session\_id, true);
  if(response.success)
  {
    console.log("Accepted the friendship Offer");
  } else {
    console.log("Rejected the friendship Offer");
    console.error("Error: " + response.error)
  }
});

console.log("Bot is listening, friendship offers");
