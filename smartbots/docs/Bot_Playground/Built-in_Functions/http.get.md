# http.get - SmartBots Developers Docs

Retrieves data from a HTTP source.

http.get(url, query)
	.then(function(response) {
		...
	});

or with [await](https://www.mysmartbots.com/dev/docs/Bot_Playground/Async_and_await "Bot Playground/Async and await"):

var response \= await http.get(url, query);

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | url | yes | the URL to retrieve |
|     | query | optional | (object) the optional URL query string params |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |
|     | statusCode |     | (on success) The HTTP status code |
|     | headers |     | (on success) The array with HTTP headers |
|     | body |     | (on success) The string body of the reply |

This function makes an HTTP GET request to the specified URL. The query string may be added to the URL (**example.com/?param1=1&param2=2**) or passes as a **query** object (**{ param1: 1, param2: 2 }**).

### Limitations

The length of the body is limited to 4096 bytes.

### Example

console.log("Doing http request...");

http.get("https://mysmartbots.com")
	.then(function(response) {
		console.log("http result:", response.body);
	})

	.then(function() {
		// Gracefully stop the test script
		exit();
	});

A bit more complex example which provides the error handling:

console.log("Doing http request...");

http.get("https://mysmartbots.com")
	.then(function(result) {
		if(!result.success) {
			// On error display the error message and stop the processing
			console.log("HTTP error:", result.error);
			throw "";
		}

		console.log("http result:", result.body);
	})

	.catch(function(err) {
		// This block allows cancelling the processing chain with throw ""
		if(err != "") { throw err; }
	})
	.then(function() {
		// Gracefully stop the test script
		exit();
	});
