# touchPrim - SmartBots Developers Docs

Touches an in-world object (prim) by its UUID

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | uuid | yes | An UUID of the object to tough. |
| Output: |     |     |     |
|     | result |     | This function does not return anything |

It is important to remember that bot is able to touch objects it "sees":

*   after logging in, give bot about 30 seconds to load surrounding objects,
*   the same after teleporting,
*   nearby objects load faster than distant,
*   if you want bot to touch a distant object (say, another side of the sim), visit it first to "see and remember" it.

## Examples

Touch a special test object in SmartBots office (the object is located at DuoLife/210/151/31):

// SmartBots Playground code start v1.0 (automatic line)
Bot.on("chat\_message", function(event) {
	console.log("Got a message: " + event.message);

	// Teleport home. Please don't leave your bots at DuoLife!
	Bot.teleport("HOME");
});

// Goto to testing object
Bot.teleport("DuoLife/211/152/31");

console.log("Teleported, touching object in 3 seconds...");

setTimeout(function() {
	Bot.touchPrim("a6b4be6c-ca10-398f-846e-ea933cebfda2");
	console.log("Object touched, waiting for object's message...");
}, 3000);

The test object's LSL code is the following:

default {
    touch\_start(integer total\_number) {
        llOwnerSay("touched by "+llDetectedName(0));
        llRegionSayTo(llDetectedKey(0), 0, "I'm touched by " + llDetectedName(0));
    }
}
