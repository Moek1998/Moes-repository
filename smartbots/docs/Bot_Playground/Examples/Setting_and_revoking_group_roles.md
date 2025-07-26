# Setting and revoking group roles


This script demonstrates how to set and revoke the group roles (see [setGroupRole](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/setGroupRole "Bot Playground/Commands/setGroupRole") and [revokeGroupRole](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/revokeGroupRole "Bot Playground/Commands/revokeGroupRole") functions).

var operation \= "SET"; // SET or REVOKE

var AVATAR \= "042536ca-dc19-45ef-bd3c-2f3c829d4e56";
var GROUP \= "6c9ecdd2-dcd8-384d-00bc-57a5dc3e7396";
var ROLE \= "ff37ff6a-595f-eff4-6ae2-6a5ec9ade464";

var promise;

console.log("The goal is to " + operation + " the group role");

switch(operation) {
	case "SET":
		promise \= Bot.setGroupRole(AVATAR, GROUP, ROLE);

		break;

	case "REVOKE":
		promise \= Bot.revokeGroupRole(AVATAR, GROUP, ROLE);
		break;
}

promise.then(function(result) {
		console.log("Command result: " + JSON.stringify(result));
});

// Gracefully exit. We don't need to run anymore.
setTimeout(function() {
	exit();
}, 1000);
