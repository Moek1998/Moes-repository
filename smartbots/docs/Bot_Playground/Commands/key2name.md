# key2name - SmartBots Developers Docs

From SmartBots Developers Docs

Jump to: [navigation](#mw-head), [search](#p-search)

Returns avatar Second Life name by UUID. The command works in opposition to [name2key](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/name2key "Bot Playground/Commands/name2key").

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | key | yes | the UUID of the avatar |
| Output: |     |     |     |
|     | slname |     | Second Life name of the avatar |

## Examples

var slname \= "Glaznah Gassner";

Bot.name2key(slname)
.then(function(result) {
  if(result.success) {
    console.log("The UUID of " + slname + " is " + result.slkey);
  } else {
    console.log("Error executing name2key: " + result.error);
  }

  return Bot.key2name(result.slkey);
})
.then(function(result) {
  console.log("Backward key2name check. Name: " + result.slname);
});
