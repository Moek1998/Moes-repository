# groupInfo - SmartBots Developers Docs

From SmartBots Developers Docs

Jump to: [navigation](#mw-head), [search](#p-search)

Returns the Second Life group details.

Bot.groupInfo("0b65a122-8f77-64fe-5b2a-225d4c490d9c").then(function(res) {
	console.log("Group info:", res);
});

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |
|     | charter |     | Group text |
|     | insignia |     | Group profile image UUID |
|     | fee |     | Group join fee |
|     | founder |     | Founder avatar UUID |
|     | mature |     | "1" if group has a Mature flag |
|     | members |     | The number of members |
|     | member\_title |     | The default member tag |
|     | name |     | Group name |
|     | open |     | "1" if group is open to join |
|     | uuid |     | Group UUID |

## Details

See [HTTP API group\_info](https://www.mysmartbots.com/dev/docs/HTTP_API/Bot_Commands/group_info "HTTP API/Bot Commands/group info") for more information and limitations.
