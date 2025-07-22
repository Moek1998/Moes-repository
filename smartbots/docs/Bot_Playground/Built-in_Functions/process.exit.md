# process.exit - SmartBots Developers Docs

Ends the execution of the program.

By default, Play programs run forever, waiting for the incoming bot event, timer event etc. You don't need to stop the program in explicit way. However, you may need to terminate your program, like as you press "Stop" command in Bot Playground interface.

### Note

Previously known as bare "exit()".

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | \--- |     | this function does not require any arguments |
| Output: |     |     |     |
|     | result |     | This function does not return anything |

The exit procedure is not immediate. Script terminates in about 1 seconds. However, all event handlers get destroyed immediately after you call _process.exit()_. Thus, you may expect that no more events arrive.

## Examples

Bot.on("instant\_message", function(event) {
  if(event.message \== "secret string") {
    console.log("Received a secret string, program is terminating");
    process.exit();
  }
}
