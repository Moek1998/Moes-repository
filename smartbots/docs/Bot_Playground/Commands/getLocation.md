# getLocation - SmartBots Developers Docs

Returns current location of the bot bot.

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |
|     | online | boolean | Bot online flag |
|     | region | string | Bot region name |
|     | position | object | Current bot position, rounded to integer:<br><br>{<br>  x: number; // 100<br>  y: number; // 110<br>  z: number; // 20<br>} |
|     | exactPosition | object | Exact bot position (the same as 'position' but with decimals):<br><br>{<br>  x: number; // 100.01<br>  y: number; // 109.65<br>  z: number; // 20.4<br>} |

## Details

Command returns bot position, mostly in real-time. Use this command to track actual bot position.

Note: [Bot.status()](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/status "Bot Playground/Commands/status") command also returns 'location' but it may be cached for up to 30 seconds.

'position' is just a rounded copy of 'exactPosition'. It has been added for convenience, to avoid clogging code with _Math.round()_ calls.

### Calling when offline

If _getLocation()_ is being called when bot is offline, then:

*   'online' flag is false
*   region is an empty string
*   all coordinates (x, y, z) are _null_

## Examples

const loc \= await Bot.getLocation();
if(loc.region \== "DuoLife") {
  console.log("Wow, I'm in SmartBots region now!");
  console.log(loc);
}

Example output:

{
   "online":true,
   "region":"DuoLife",
   "position":{
      "x":230,
      "y":78,
      "z":32
   },
   "exactPosition":{
      "x":229.6,
      "y":77.69,
      "z":32.1
   }
}
