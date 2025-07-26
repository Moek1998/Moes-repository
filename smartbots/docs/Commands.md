# Commands - SmartBots Developers Docs

Commands are being sent to the bot by calling the javascript method of _Bot_:

Bot.im("Glaznah Gassner", "Hello there!");

## Commands reference

| Command | Description |
| --- | --- |
| ### Access Rights |     |     |
| [isMyOwner](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/isMyOwner "Bot Playground/Commands/isMyOwner") | Returns if the bot is owned by the avatar. |
| [isMyManager](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/isMyManager "Bot Playground/Commands/isMyManager") | Returns if the avatar is a Trusted Manager for the bot. |
| [isOnline](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/isOnline "Bot Playground/Commands/isOnline") | Returns true/false if the bot is online. |
| ### Avatar Info |     |     |
| [avatarInfo](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/avatarInfo "Bot Playground/Commands/avatarInfo") | Returns the Second Life avatar details. |
| [checkScriptedAgent](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/checkScriptedAgent "Bot Playground/Commands/checkScriptedAgent") | Returns if the resident is scripted agents known by SmartBots. It included all SmartBots bots, and other residents our system considers bot or scripted agent. |
| ### Status |     |     |
| [status](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/status "Bot Playground/Commands/status") | Returns the online status of the bot. |
| [statusExt](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/statusExt "Bot Playground/Commands/statusExt") | Returns the online status of the bot. |
| [login](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/login "Bot Playground/Commands/login") | Initiates bot login sequence. |
| [logout](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/logout "Bot Playground/Commands/logout") | Initiates bot logout sequence. |
| ### Messaging |     |     |
| [say](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/say "Bot Playground/Commands/say") | Says message over a specific chat channel. |
| [im](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/im "Bot Playground/Commands/im") | Sends Instant Message to specific avatar. |
| [replyDialog](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/replyDialog "Bot Playground/Commands/replyDialog") | Virtually "presses" a pop-up dialog button (which was displayed by an in-world script). |
| [startTyping](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/startTyping "Bot Playground/Commands/startTyping") | Sends "typing" in chat to a specific user. |
| [stopTyping](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/stopTyping "Bot Playground/Commands/stopTyping") | Stops sending "typing" in chat to a specific user. |
| ### Friendship |     |     |
| [acceptFriendshipOffer](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/acceptFriendshipOffer "Bot Playground/Commands/acceptFriendshipOffer") | Accept (or reject) a friendship offer sent by other avatar. |
| [offerFriendship](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/offerFriendship "Bot Playground/Commands/offerFriendship") | Offers friendship to a resident. |
| ### Group Control |     |     |
| [acceptGroupOffer](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/acceptGroupOffer "Bot Playground/Commands/acceptGroupOffer") | Accept (or reject) a group invitation sent by other avatar. |
| [activateGroup](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/activateGroup "Bot Playground/Commands/activateGroup") | Activates a specific group (for example, to get build rights on the parcel). |
| [groupInfo](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/groupInfo "Bot Playground/Commands/groupInfo") | Returns the Second Life group details. |
| [joinGroup](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/joinGroup "Bot Playground/Commands/joinGroup") | Tries to join a group by UUID. |
| [leaveGroup](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/leaveGroup "Bot Playground/Commands/leaveGroup") | Commands bot to leave the group specified by a UUID. |
| [listGroups](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/listGroups "Bot Playground/Commands/listGroups") | Returns a list of the Second Life groups the bot is member of. |
| [revokeGroupRole](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/revokeGroupRole "Bot Playground/Commands/revokeGroupRole") | Removes a group member from a specific role. |
| [sendGroupIM](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/sendGroupIM "Bot Playground/Commands/sendGroupIM") | Sends a message to group chat. |
| [sendNotice](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/sendNotice "Bot Playground/Commands/sendNotice") | Sends a notice to the group. |
| [setGroupRole](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/setGroupRole "Bot Playground/Commands/setGroupRole") | Puts member of a group in a specific role. |
| ### Group Members Control |     |     |
| [ejectGroupMember](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/ejectGroupMember "Bot Playground/Commands/ejectGroupMember") | Ejects residents from the group. |
| [inviteGroup](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/inviteGroup "Bot Playground/Commands/inviteGroup") | Sends a group invitation to a specific resident. |
| ### Inventory |     |     |
| [acceptInventoryOffer](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/acceptInventoryOffer "Bot Playground/Commands/acceptInventoryOffer") | Accept (or reject) an inventory offer sent by other avatar or in-world script. |
| [listInventory](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/listInventory "Bot Playground/Commands/listInventory") | Returns a list of the Second Life groups the bot is member of. |
| [giveInventory](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/giveInventory "Bot Playground/Commands/giveInventory") | Commands bot to send an inventory item or folder to specific avatar. |
| ### Appearance |     |     |
| [takeoff](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/takeoff "Bot Playground/Commands/takeoff") | Removes a clothing item, body part or attachment (the opposite of the [wear](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/wear "Bot Playground/Commands/wear") command). |
| [wear](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/wear "Bot Playground/Commands/wear") | Commands bot to wear a clothing item, body part or attach an object. |
| ### Money |     |     |
| [getBalance](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/getBalance "Bot Playground/Commands/getBalance") | Retrieves the current bot's L$ balance. |
| [giveMoney](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/giveMoney "Bot Playground/Commands/giveMoney") | Commands bot to send money (L$) to specific avatar. |
| ### Movement |     |     |
| [fly](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/fly "Bot Playground/Commands/fly") | Starts or stops flying. |
| [getLocation](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/getLocation "Bot Playground/Commands/getLocation") | Returns current location of the bot bot. |
| [move](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/move "Bot Playground/Commands/move") | Start or stop bot movement and rotations. |
| [sit](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/sit "Bot Playground/Commands/sit") | Commands bot to sit on a specific prim. Allows saving this object as a permanent location. |
| [teleport](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/teleport "Bot Playground/Commands/teleport") | Teleports bot to specific location. |
| [walkTo](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/walkTo "Bot Playground/Commands/walkTo") | Walk to a position within the current region. |
| ### Other avatars interaction |     |     |
| [key2name](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/key2name "Bot Playground/Commands/key2name") | Returns avatar Second Life name by UUID. |
| [name2key](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/name2key "Bot Playground/Commands/name2key") | Returns the UUID of the given resident by name. |
| [offerTeleport](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/offerTeleport "Bot Playground/Commands/offerTeleport") | Sends a teleport offer to the resident. |
| [acceptTeleportOffer](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/acceptTeleportOffer "Bot Playground/Commands/acceptTeleportOffer") | Accept (or reject) a teleport offer sent by other avatar. |
| ### World interaction |     |     |
| [scanNearbyAvatars](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/scanNearbyAvatars "Bot Playground/Commands/scanNearbyAvatars") | Scans current region for other avatars. |
| [takeInworldPrim](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/takeInworldPrim "Bot Playground/Commands/takeInworldPrim") | Takes (de-rezzes) or copies in-world prim into bot's inventory. **Not available for QubicBot yet [(?)](https://www.mysmartbots.com/dev/docs/New_features_and_QubicBot "New features and QubicBot")** |
| [touchAttachment](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/touchAttachment "Bot Playground/Commands/touchAttachment") | Touches an attachment of the bot (HUD or wearable object) |
| [touchPrim](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/touchPrim "Bot Playground/Commands/touchPrim") | Touches an in-world object (prim) by its UUID |
| ### Region (sim) control |     |     |
| [regionRestart](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/regionRestart "Bot Playground/Commands/regionRestart") | Queries to restart current region of the bot |
| [regionRestartCancel](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/regionRestartCancel "Bot Playground/Commands/regionRestartCancel") | Cancels pending restart of current region |

## If you already using SmartBots HTTP API

If you already using SmartBots HTTP API, you may notice that these commands roughly correspond to [HTTP API bot commands](https://www.mysmartbots.com/dev/docs/HTTP_API/Bot_Commands "HTTP API/Bot Commands").
