# setGroupRole - SmartBots Developers Docs

Puts member of a group in a specific role. Also see a [revokeGroupRole](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/revokeGroupRole "Bot Playground/Commands/revokeGroupRole") function.

Bot.setGroupRole(avatar\_uuid, group\_uuid, role\_uuid)
  .then(function(result) {
    if(result.success) { console.log("Role revoked"); }
  });

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | avatar\_uuid | yes | The UUID of the avatar which should be moved to the specific role |
|     | group\_uuid | yes | The UUID of the group |
|     | role\_uuid | yes | The UUID of the group role. "Everyone" role is 00000000-0000-0000-0000-000000000000 |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |

Make sure your bot has sufficient rights to assign/revoke members from group roles.

Check the [complex example](https://www.mysmartbots.com/dev/docs/Bot_Playground/Setting_and_revoking_group_roles "Bot Playground/Setting and revoking group roles") for function usage.
