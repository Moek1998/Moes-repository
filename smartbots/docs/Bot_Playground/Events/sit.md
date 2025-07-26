# sit - SmartBots Developers Docs

Fires when bot sits on the object

Bot.on("sit", function(event) { ... });

## Reference

This event comes with the following _event_ object:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| _event_ object properties: |     |     |     |
|     | sitting | boolean | \[boolean\] true if bot seated on the object, false if it stands |
|     | object\_uuid |     | the UUID of the object bot is sitting on. NULL\_KEY if bot is standing. |
|     | position | object { x, y, z } | the sitting position (offset). Empty object if _sitting==false_ |

## Example

Bot.on("sit", function(event) {
	if(event.sitting) {
		console.log("I'm sitting on the object ", event.object\_uuid);
	} else {
		console.log("I'm standing now");
	}
});
