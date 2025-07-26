# status - SmartBots Developers Docs

Returns the online status of the bot.

Check [Bot.getLocation()](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/getLocation "Bot Playground/Commands/getLocation") command if you are looking for bot location (region and/or coordinates).

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |
|     | status |     | Current online status of the bot (see "Details") |
|     | online |     | "1" if bot is online, "0" otherwise |
|     | slname |     | Full SL name of the bot |
|     | uuid |     | Bot avatar UUID |
|     | location |     | Current bot location if bot is online ("Region/X/Y/Z") - legacy see "Bot location" below |

## Important notes

The subsequent 'status' calls may be cached up to 30 seconds.

## Bot location

_Bot.status()_ returns bot location ('location') just for compatibility reasons.

We recommend using [Bot.getLocation()](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/getLocation "Bot Playground/Commands/getLocation") command to retrieve real-time bot location. _Bot.status()_ result may be cached (see notes above).

## Details

The following statuses can be returned:

*   ONLINE - the bot is online
*   PRE-CONNECTING - the bot is going to log in and waits for a SL login server response
*   CONNECTING - SL login server logs the bot in
*   LOGGED OUT - bot is logged out now (gracefully, by the owner's command)
*   OFFLINE - bot can not be contacted. This is an unexpected behavior and usually happens while SmartBots servers are restarting

## Examples

const status \= await Bot.status()
console.log("My status is:", res);
