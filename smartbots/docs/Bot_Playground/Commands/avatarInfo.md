# avatarInfo - SmartBots Developers Docs

Returns the Second Life avatar details.

Bot.avatarInfo("0b65a122-8f77-64fe-5b2a-225d4c490d9c").then(function(res) {
	console.log("Avatar info:", res);
});

or using [Async and await](https://www.mysmartbots.com/dev/docs/index.php?title=Async_and_await&action=edit&redlink=1 "Async and await (page does not exist)"):

let res \= await Bot.avatarInfo("0b65a122-8f77-64fe-5b2a-225d4c490d9c");
console.log("Avatar info:", res);

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |
|     | about |     | Profile text |
|     | born |     | SL birth day, MM/DD/YYYY |
|     | identified |     | "1" if avatar has payment info |
|     | image |     | Profile image UUID |
|     | first\_life\_image |     | First life image UUID |
|     | first\_life\_text |     | First life text |
|     | mature |     | "1" if profile is mature |
|     | online |     | "1" if avatar is online |
|     | partner |     | Partner UUID (zero UUID if no partner) |
|     | publish\_web |     | "1" if profile is allowed to be published on web |
|     | transacted |     | "1" if payment info was used |
|     | url |     | Profile URL |

## Details

See [HTTP API avatar\_info](https://www.mysmartbots.com/dev/docs/HTTP_API/Bot_Commands/avatar_info "HTTP API/Bot Commands/avatar info") for more information and limitations.
