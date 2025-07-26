# isOnline - SmartBots Developers Docs

From SmartBots Developers Docs

Jump to: [navigation](#mw-head), [search](#p-search)

Returns true/false if the bot is online.

const res \= await Bot.isOnline();
console.log("Is Bot Online:", res);

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Output: |     |     |     |
|     | return value | boolean | true/false if bot online |

## Examples

	let isOnline \= await Bot.isOnline();
	if(isOnline) {
		console.log(\`Bot is Online\`);
	} else {
		console.log(\`Bot is Offline\`);
	}
