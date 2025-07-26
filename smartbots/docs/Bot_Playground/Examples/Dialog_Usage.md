# Dialog Usage - SmartBots Developers Docs


This script displays the basic usage of [Bot\_Playground/Events/script\_dialog](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events/script_dialog "Bot Playground/Events/script dialog") and [Bot\_Playground/Commands/replyDialog](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/replyDialog "Bot Playground/Commands/replyDialog") functions.

With this script you will receive an Instant Message outlining the options each time your bot receives a dialog menu, you can respond to the Instant Message with the option you want your bot to click.

// You should put your avatar name here to ensure you receive dialog options via. IM and be able to respond to them.
var ownerName \= "YourName Resident";

var channel;
var objUuid;
var options;
var index;

Bot.on("script\_dialog", function(event) {
  channel \= event.channel;
  objUuid \= event.object\_uuid;
  options \= event.buttons;
  Bot.im(ownerName, "I just received a dialog, respond to me with the option I should choose:\\n\\nChannel:"+channel+"\\n\\nMessage:\\n"+event.text+"\\n\\nOptions:\\n"+options.join("\\n")+"\\nIgnore - Ignores the dialog\\n\\n(The options are CaSe SeNsItIvE)");
});

Bot.on("instant\_message", function(event) {
  if (Array.isArray(options)) {
    if (event.speaker\_name \== ownerName) {
      if (event.message.toLowerCase() \== "ignore") {
        channel \= objUuid \= options \= index \= "";
        Bot.im(ownerName, "Dialog ignored successfully.");
      } else {
        index \= options.indexOf(event.message);
        if (index != "-1") {
            Bot.replyDialog(channel, objUuid, options\[index\]);
        } else Bot.im(ownerName, "Invalid option received. Please choose one of the following options:\\n\\n"+options.join("\\n")+"\\nIgnore - Ignores the dialog\\n\\n(The options are CaSe SeNsItIvE)");
      }
    }
  }
});
