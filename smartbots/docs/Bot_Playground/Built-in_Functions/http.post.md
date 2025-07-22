# http.post - SmartBots Developers Docs

Retrieves data from a HTTP source using the POST method.

const queryData \= { f: "123" };

http.post(url, queryData, "json")
	.then(function(response) {
		...
	});

// or with await:
const response \= await http.post(url, queryData, "json");

or with [await](https://www.mysmartbots.com/dev/docs/Bot_Playground/Async_and_await "Bot Playground/Async and await"):

var response \= await http.post(url, query);

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | url | yes | the URL to retrieve |
|     | queryData | optional | (object) the optional POST parameters, object |
|     | contentType | optional | (string) the optional content type (see below) |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |
|     | statusCode |     | (on success) The HTTP status code |
|     | headers |     | (on success) The array with HTTP headers |
|     | body |     | (on success) The string body of the reply |

This function makes an HTTP POST request to the specified URL. The query parameters may be added to the URL as a **query** object (**{ param1: 1, param2: 2 }**).

You can use [https://ptsv2.com](https://ptsv2.com/) to test your POST requests.

### Limitations

The length of the response body is limited to 4096 bytes.

### Content type

By default the request is being sent as an old plain POST. This is the string composed of key=value pairs (also known as "application/x-www-form-urlencoded").

http.post(url, queryString);
// or, the same
http.post(url, queryString, "form");

You can change the request to send JSON by specifying "json" as contentType argument (this way is also known as "application/json"):

http.post(url, queryData, "json")

### Example

A simple POST request using await:

console.log("Doing http request...");

var response \= await http.post("https://ptsv2.com/t/h6rf5-1631886515/post", { param1: 1, param2: 2})
console.log("http result:", response.body);

// Gracefully stop the test script
exit();

A bit more complex example which provides the error handling (uses Promises but can be rewritten to use [await](https://www.mysmartbots.com/dev/docs/Bot_Playground/Async_and_await "Bot Playground/Async and await")):

console.log("Doing http request...");

http.post("https://ptsv2.com/t/h6rf5-1631886515/post", { param1: 1, param2: 2})
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
