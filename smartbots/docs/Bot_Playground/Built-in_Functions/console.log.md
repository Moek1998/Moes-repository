# console.log - SmartBots Developers Docs

Logs data to the runtime log. Read more about [runtime logs](https://www.mysmartbots.com/dev/docs/Bot_Playground/Logging "Bot Playground/Logging").

console.log(...arguments);

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | ...arguments | yes | any number of arguments to be logged to the log. Objects can be translated to a string using JSON.stringify() |
| Output: |     |     |     |
|     | result |     | This function does not return anything |

## Important notice

Since logs are being saved in asynchronous way, **consecutive** console.log() may shuffle:

console.log("line 1");
console.log("line 2");

may generate the following under a heavy load:

13/6/2016 22:25:50
line 2

13/6/2016 22:25:50
line 1

## Limitations

The amount of data is limited to somewhat between 4kb and 8kb of raw string data. If output data buffer is too big then 'console.log' call will be silently discarded.
