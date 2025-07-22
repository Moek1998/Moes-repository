# isMyManager - SmartBots Developers Docs

From SmartBots Developers Docs

Jump to: [navigation](#mw-head), [search](#p-search)

Returns if the avatar is a Trusted Manager for the bot.

const res \= await Bot.isMyManager("slnameOrUUID");
console.log("Is Bot Manager:", res);

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | slName or UUID | yes | The Avatar SL Name or UUID |
| Output: |     |     |     |
|     | return value | boolean | true if resident is the trusted manager of the bot |

## Examples

Bot.on("chat\_message", async function (event) {
	let isManager \= await Bot.isMyManager(event.speaker\_name);
	if(isManager) {
		console.log(\`Message from Trusted Manager\`);
	}
}
