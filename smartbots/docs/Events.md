# Events - SmartBots Developers Docs

Event is a callback function which is invoked when something happens with your bot or surrounding world.

Callbacks are set using a special _on()_ function:

Bot.on("instant\_message", function(data) {
  console.log("bot got a message:", data);
});

## Events reference

| Command | Description |
| --- | --- |
| ### Messaging |     |     |
| [chat\_message](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/chat_message "Bot Playground/Events/chat message") | Fires when bot receives a message in the local chat |
| [instant\_message](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/instant_message "Bot Playground/Events/instant message") | Fires when bot receives a message from another avatar or in-world object. |
| [start\_typing](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/start_typing "Bot Playground/Events/start typing") | Fires when another avatar starts typing in IM to the bot. **Not available for QubicBot yet [(?)](https://www.mysmartbots.com/dev/docs/New_features_and_QubicBot "New features and QubicBot")** |
| [stop\_typing](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/stop_typing "Bot Playground/Events/stop typing") | Fires when another avatar stops typing in IM to the bot. **Not available for QubicBot yet [(?)](https://www.mysmartbots.com/dev/docs/New_features_and_QubicBot "New features and QubicBot")** |
| [teleport\_offer](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/teleport_offer "Bot Playground/Events/teleport offer") | Fires when bot receives a teleport offer from another avatar. |
| ### Group Messaging |     |     |
| [group\_offer](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/group_offer "Bot Playground/Events/group offer") | Fires when bot receives a group invite |
| [group\_im](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/group_im "Bot Playground/Events/group im") | Fires when bot receives a group chat message. |
| [group\_notice](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/group_notice "Bot Playground/Events/group notice") | Fires when bot receives a group notice. |
| ### Inventory |     |     |
| [inventory\_offer](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/inventory_offer "Bot Playground/Events/inventory offer") | Fires when bot receives a inventory offer |
| [balance\_changed](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/balance_changed "Bot Playground/Events/balance changed") | Fires when bot receives or payd money |
| ### Friendship |     |     |
| [friendship\_offer](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/friendship_offer "Bot Playground/Events/friendship offer") | Fires when bot receives a friendship offer |
| ### Movement |     |     |
| [autopilot\_completed](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/autopilot_completed "Bot Playground/Events/autopilot completed") | Fires when bot autopilot successfully completes its journey. **Not available for QubicBot yet [(?)](https://www.mysmartbots.com/dev/docs/New_features_and_QubicBot "New features and QubicBot")** |
| [autopilot\_started](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/autopilot_started "Bot Playground/Events/autopilot started") | Fires when bot autopilot starts. **Not available for QubicBot yet [(?)](https://www.mysmartbots.com/dev/docs/New_features_and_QubicBot "New features and QubicBot")** |
| [autopilot\_stuck](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/autopilot_stuck "Bot Playground/Events/autopilot stuck") | Fires when bot autopilot gets stuck and gives up moving further. **Not available for QubicBot yet [(?)](https://www.mysmartbots.com/dev/docs/New_features_and_QubicBot "New features and QubicBot")** |
| [self\_position](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/self_position "Bot Playground/Events/self position") | Fires when bot in-world location, position or heading changes. **Not available for QubicBot yet [(?)](https://www.mysmartbots.com/dev/docs/New_features_and_QubicBot "New features and QubicBot")** |
| [sit](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/sit "Bot Playground/Events/sit") | Fires when bot sits on the object |
| [teleport\_status](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/teleport_status "Bot Playground/Events/teleport status") | Fires when bot teleports, indicating various stages of the teleport. **Not available for QubicBot yet [(?)](https://www.mysmartbots.com/dev/docs/New_features_and_QubicBot "New features and QubicBot")** |
| ### World |     |     |
| [region\_restart](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/region_restart "Bot Playground/Events/region restart") | Fires when bot receives a region restart notification. **Not available for QubicBot yet [(?)](https://www.mysmartbots.com/dev/docs/New_features_and_QubicBot "New features and QubicBot")** |
| [region\_restart\_cancelled](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/region_restart_cancelled "Bot Playground/Events/region restart cancelled") | Fires when bot receives a region restart cancellation notification. **Not available for QubicBot yet [(?)](https://www.mysmartbots.com/dev/docs/New_features_and_QubicBot "New features and QubicBot")** |
| [script\_dialog](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/script_dialog "Bot Playground/Events/script dialog") | Fires when bot receives a scripted dialog with a menu buttons |
| ### Online status |     |     |
| [before\_login](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/before_login "Bot Playground/Events/before login") | Fires when bot is going to login to Second Life. |
| [after\_login](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/after_login "Bot Playground/Events/after login") | Fires when bot successfully logged to Second Life. |
| [before\_logout](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/before_logout "Bot Playground/Events/before logout") | Fires when bot is going offline. |
| [after\_logout](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/after_logout "Bot Playground/Events/after logout") | Fires after bot goes offline. **Not available for QubicBot yet [(?)](https://www.mysmartbots.com/dev/docs/New_features_and_QubicBot "New features and QubicBot")** |
| [login\_error](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/login_error "Bot Playground/Events/login error") | Fires when bot is unable to login to Second Life. **Not available for QubicBot yet [(?)](https://www.mysmartbots.com/dev/docs/New_features_and_QubicBot "New features and QubicBot")** |
| ### Webhooks | | |
| [playground_webhook](./Webhooks.md) | Fires when the script’s webhook receives an HTTP request from your server. See [Webhooks](./Webhooks.md) for more information. |
