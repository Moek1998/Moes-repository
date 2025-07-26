# statusExt - SmartBots Developers Docs

Returns the online status of the bot.

const res \= await Bot.statusExt();
console.log("Status:", JSON.stringify(res, null, 2));

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |
|     | status |     | An object which contains various information about bot status. See Details below. |

## Important notes

The subsequent command calls may be cached for up to 60 seconds. Use [status](https://www.mysmartbots.com/dev/docs/index.php?title=Bot_Playground/Commands/statusExt/status&action=edit&redlink=1 "Bot Playground/Commands/statusExt/status (page does not exist)") command to get a faster refresh rate.

## Details

The 'status' field of the response provides a lot of information on bot status:

{
	// Bot name
	"name": "Fashion Firethorn",
	// Bot UUID
	"UUID": "fc417c00-71ae-4427-a9dd-eed32a3e49de"

	// \= Connection status
	// Is bot online
	"online": true,
	// Is bot connecting to Second Life right now
	"connecting": false,

	// In-world status
	// Avatar position
	"position": {
		"Z": 33.377563,
		"X": 234.81233,
		"Y": 111.23107
	},
	// Avatar heading (the view direction), radians
	"heading": \-3.0020456,

	// Current region (sim) name
	"regionName": "DuoLife",
	// Current region ID
	"regionHandle": 849922488517376,
	// Current parcel name
	"parcelName": "SmartBots: Second Life bots for L$79 / Inviter bot + notices",
	// Current parcel ID
	"parcelID": 150,

	// Bot OS version
	"version": "91.00.00"
}
