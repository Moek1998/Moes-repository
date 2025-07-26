# Basic localStorage usage - SmartBots Developers Docs

From SmartBots Developers Docs

Jump to: [navigation](#mw-head), [search](#p-search)


This script displays the basic usage of [localStorage.set()](https://www.mysmartbots.com/dev/docs/Bot_Playground/Built-in_Functions/localStorage.set "Bot Playground/Built-in Functions/localStorage.set") and [localStorage.get()](https://www.mysmartbots.com/dev/docs/Bot_Playground/Built-in_Functions/localStorage.get "Bot Playground/Built-in Functions/localStorage.get") functions.

var CONFIG \= {};

restoreConfig();

CONFIG.runs++;
console.log("This script is starting for " + CONFIG.runs + " time");

saveConfig();

function restoreConfig() {
	var cnf \= localStorage.get("my\_config");
	CONFIG \= { runs: 0 };

	if(typeof(cnf) != "undefined" && cnf != "") {
		CONFIG \= JSON.parse(cnf);
	}
}

function saveConfig() {
	localStorage.set("my\_config", JSON.stringify(CONFIG));
}
