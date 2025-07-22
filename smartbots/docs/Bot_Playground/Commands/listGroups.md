# listGroups - SmartBots Developers Docs

Returns a list of the Second Life groups the bot is member of.

Bot.listGroups().then(function(result) { ... });

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | \-- none -- |     |     |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |
|     | groups |     | The object which contains all groups. Format:<br><br>{<br>  "uuid-1": "group-name-1",<br>  "uuid-2": "group-name-2",<br>  ...<br>}<br><br>See "Examples" section below for details.<br><br>**Important:** groups list order is always random. |

## Examples

### List all groups

Print all bot groups:

Bot.listGroups()
.then(function(result) {
	var list \= "";

	for(var k in result.groups) {
		list \= list + k + ": " + result.groups\[k\] + "\\n";
	}

	console.log(list);

	exit();
});

Output:

022df06c-b616-d400-fd94-8ccc523c5ae2: Get Paid in Second Life
9590cad7-3b63-88d6-0d06-d75b04698ec1: PicMe Poses
0ec6f039-1a39-339c-3c68-e31ed2dc703f: Earn2Life.com Discount Shops

### Random Group Tag Activator

See this example [here](https://www.mysmartbots.com/dev/docs/Bot_Playground/Examples/Random_Group_Tag_Activator "Bot Playground/Examples/Random Group Tag Activator").
