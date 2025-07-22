# process.sleep - SmartBots Developers Docs

Pauses a program execution.

await process.sleep(timeMs);

### Note

Previously known as bare "sleep()".

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | timeMs | yes | sleep time, ms |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |

~This function can be used to delay the code execution for a specific time. Note that this function is asynchronous (like the most of javascript), so can't write "doSomething(); process.sleep(1000); doAfterDelay;". See the examples below.~

The process.sleep() function immediately returns a Promise. You can use [async/await](https://www.mysmartbots.com/dev/docs/Bot_Playground/Async_and_await "Bot Playground/Async and await") to pause your script (see examples below).

## Examples

The function can be used in three ways:

1\. Async/await (recommended)

console.log("one1");

await process.sleep(2000);

console.log("two2");

2\. Standalone:

console.log("one1");

process.sleep(2000)
	.then(function() {
		console.log("two2");
	});

3\. Within the chain:

// SmartBots Playground code start v1.0 (automatic line)
http.get("https://mysmartbots.com")
	.then(function() {
		console.log("one");

	return process.sleep(2000);
	})
	.then(function() {
		console.log("two");
	})

	.then(function() {
		// Gracefully stop the test script
		exit();
	});
