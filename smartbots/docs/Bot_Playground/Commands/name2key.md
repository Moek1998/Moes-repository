# name2key - SmartBots Developers Docs

Returns the UUID of the given resident by name.

Bot.name2key(slname, function(result) { ... });

or using promises:

Bot.name2key(slname)
  .then(function(result) { ... });

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | slname | yes | The name of the resident.<br><br>Important: this value has to contain a full name: "FirstName LastName", or "FirstName Resident". |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |
|     | slkey |     | The UUID of the avatar |

## Examples

var AVATAR \= "Glaznah Gassner";

Bot.name2key(AVATAR)
	.then(function(result) {
		console.log("The uuid using promises is " + result.slkey);
		exit();
	});

Bot.name2key(AVATAR, function(result) {
	console.log("The uuid using callback is " + result.slkey);
	exit();
});
