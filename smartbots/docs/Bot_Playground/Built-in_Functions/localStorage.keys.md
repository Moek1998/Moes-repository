# localStorage.keys - SmartBots Developers Docs

Returns the list of the available keys in a persistent storage. Also check [localStorage.set()](https://www.mysmartbots.com/dev/docs/Bot_Playground/Built-in_Functions/localStorage.set "Bot Playground/Built-in Functions/localStorage.set").

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
| Output: |     |     |     |
|     | value |     | The array of strings, key names |

Use this if you need to know the keys in your localStorage.

## Example

console.log("the localStorage keeps keys ", localStorage.keys());

exit();

Or with forEach:

localStorage.keys().forEach(function(key) {
  console.log(key, "=", localStorage.get(key));
});

exit();
