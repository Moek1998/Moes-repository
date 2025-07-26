# isMyOwner - SmartBots Developers Docs

From SmartBots Developers Docs

Jump to: [navigation](#mw-head), [search](#p-search)

Returns if the bot is owned by the avatar.

const res \= await Bot.isMyOwner("slnameOrUUID");
console.log("Is Bot Owner:", res);

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | slName or UUID | yes | The Avatar SL Name or UUID |
| Output: |     |     |     |
|     | return value | boolean | true if resident is the owner of the bot |

## Examples

Bot.on("chat\_message", async function (event) {
	let isOwner \= await Bot.isMyOwner(event.speaker\_name);
	if(isOwner) {
		console.log(\`Message from Owner\`);
	}
}
