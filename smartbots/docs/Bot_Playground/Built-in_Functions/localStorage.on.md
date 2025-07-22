# localStorage.on - SmartBots Developers Docs

Adds the event callback on localStorage. Also check [localStorage.set()](https://www.mysmartbots.com/dev/docs/Bot_Playground/Built-in_Functions/localStorage.set "Bot Playground/Built-in Functions/localStorage.set").

localStorage.on(eventName, callback);

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | eventName | yes | the name of the event. Currently only supported event is _"update"_ |
|     | callback | yes | the callback function to fire on event, **function(entry, value, script)** where<br><br>*   entry - is the name of the key set<br>*   value - the value<br>*   script - the name of the script which did the change |

## Limitations

See [localStorage.set()](https://www.mysmartbots.com/dev/docs/Bot_Playground/Built-in_Functions/localStorage.set "Bot Playground/Built-in Functions/localStorage.set") for storage limitations.

Use this function if you want to know when other scripts do localStorage.set().

Important: the "update" event _does not_ react on localStorage.set() calls in current script.

## Example

To see how localStorage.on("update") works you'll need two scripts:

The "Listener" script:

localStorage.on("update", function(entry, value, script) {
	console.log("localStorage got updated:", entry, "=", value, "by script", script);

	exit();
});

The "Initiator" script:

localStorage.set("data", "data from 1");
exit();

How to run:

1.  Launch the "Listener" script (it will keep running)
2.  Launch the "Initiator" script (it will run and stop)
3.  Now switch to the "Listener" script and check the runtime logs of "Listener"
