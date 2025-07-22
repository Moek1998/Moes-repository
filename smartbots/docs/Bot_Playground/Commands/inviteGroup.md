# inviteGroup - SmartBots Developers Docs

Sends a group invitation to a specific resident.

Bot.inviteGroup(avatar, groupuuid, roleuuid, check\_membership);

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | avatar | yes | The UUID of the resident |
|     | groupuuid | yes | The UUID of the group |
|     | roleuuid | yes | The UUID of the group role (NULL\_KEY for "Everyone") |
|     | check\_membership | optional | set to 1 if you want to ignore existing group members (see "Comments" below) |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |

### Ignoring existing group members

It is possible to ignore existing group members and do not invite them: set _check\_membership_ parameter to 1.

**Important notice:** bot reloads the list of the group members every 10 minutes. Thus, if resident (1) exits from the group and then (2) tries to join back immediately, bot will think that resident still in the group: the invitation will be discarded.
