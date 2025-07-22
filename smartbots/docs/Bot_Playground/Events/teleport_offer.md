# teleport\_offer - SmartBots Developers Docs

Fires when bot receives a teleport offer from another avatar.

Bot.on("teleport\_offer", function(event) { ... });

Use [acceptTeleportOffer](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/acceptTeleportOffer "Bot Playground/Commands/acceptTeleportOffer") to "accept/reject" a teleport offer.

## Reference

This event comes with the following _event_ object:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| _event_ object properties: |     |     |     |
|     | avatar\_name |     | Sender's SL name |
|     | avatar\_uuid |     | The UUID of the sender |
|     | message |     | Teleport offer message |
|     | slurl |     | The teleport location |

## Example

Bot.on("teleport\_offer", function(event) {
      console.log("Got teleport offer from: " + event.avatar\_name);
});

console.log("Bot is listening, teleport offers");
