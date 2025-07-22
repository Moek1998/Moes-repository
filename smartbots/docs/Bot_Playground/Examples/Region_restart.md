# Bot Playground/Examples/Region restart - SmartBots Developers Docs

From SmartBots Developers Docs

Jump to: [navigation](#mw-head), [search](#p-search)

The following script uses commands and events to work with region restarts:

1.  It restarts region
2.  Sleeps for 10 seconds
3.  Then cancels restart
4.  All restart events are being logged as well

## Code

console.log(\`${process.name} started\`);

Bot.on("region\_restart", (event) \=> {
	console.log(\`region\_restart:\`, event);
});

Bot.on("region\_restart\_cancelled", (event) \=> {
	console.log(\`region\_restart\_cancelled:\`, event);
});

Bot.regionRestart(240);
console.log("Region restart requested");

await sleep(10 \* 1000);

Bot.regionRestartCancel();
console.log("Region restart cancelled");
