# ejectGroupMember - SmartBots Developers Docs

From SmartBots Developers Docs

Jump to: [navigation](#mw-head), [search](#p-search)

Ejects residents from the group.

Bot.ejectGroupMember(avatar, groupuuid);

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | avatar | yes | The UUID of the resident |
|     | groupuuid | yes | The UUID of the group |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |

## Important

If you are using a custom role (other than "Everyone") you need an additional abilities for your bot. [Read this for details](https://www.mysmartbots.com/dev/docs/Inviting_and_ejecting_from_custom_role "Inviting and ejecting from custom role").
