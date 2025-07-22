# checkScriptedAgent - SmartBots Developers Docs

Returns if the resident is scripted agents known by SmartBots. It included all SmartBots bots, and other residents our system considers bot or scripted agent.

const res \= await Bot.checkScriptedAgent("slnameOrUUID");
console.log("Is Bot Scripted Agent:", res);

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | slName or UUID | yes | The Avatar SL Name or UUID |
| Output: |     |     |     |
|     | return value | boolean | true if resident is the bot |

## Examples

Bot.on("chat\_message", async function (event) {
	let isBot \= await Bot.checkScriptedAgent(event.speaker\_name);
	if(isBot) {
		console.log(\`Message from Bot\`);
	}
}
