# Random Group Tag Activator - SmartBots Developers Docs

From SmartBots Developers Docs

Jump to: [navigation](#mw-head), [search](#p-search)

The following code requests the groups list using [listGroups()](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/listGroups "Bot Playground/Commands/listGroups"), selects the very first group and activates it using [activateGroup()](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/activateGroup "Bot Playground/Commands/activateGroup"):

Bot.listGroups()
.then(function(result) {
	// We don't use Object.keys() below because it is was not
	// supported in early versions of Bots Playground
	var cnt \= 0;
	var uuid \= "";
	for(k in result.groups) {
		cnt++;

		// Activate the very first group in list
		if(uuid \== "") { uuid \= k; }
	}

	console.log("Got groups. I'm a member of " + cnt + " group(s)" + "\\n" +
							"I will activate this group tag: " + result.groups\[uuid\]);

	// We use Promise here. See Bot Playground docs
	return Bot.activateGroup(uuid);
})
.then(function(result) {
	console.log("group activated successfully: " + result.success);

	exit();
});
