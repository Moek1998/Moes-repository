# Script user settings - SmartBots Developers Docs


The most of scripts are supposed to be configurable for the user. The configurable options could be like group name, various messages and such.

Please note that user's bot name is not a setting. User selects the bot while purchasing your script.

## Configuring settings

[![Store-user-settings-1.png](https://www.mysmartbots.com/dev/docs/images/8/8e/Store-user-settings-1.png)](https://www.mysmartbots.com/dev/docs/File:Store-user-settings-1.png)

There are three values you specify:

*   the setting variable name as your script sees it (see below)
*   the setting "friendly" name as user sees it
*   the optional hint for the user

All settings are string values (if you need a number or UUID you should do a transform in your script).

## Accessing user settings from script

User setting can be accessed from your script using userSettings object:

console.log("Using group: " + userSettings.group\_name);

## Specifying settings while developing scripts

You can specify the settings values for your own script (while in development) on a "Settings" tab:

[![Store-user-settings-2.png](https://www.mysmartbots.com/dev/docs/images/7/77/Store-user-settings-2.png)](https://www.mysmartbots.com/dev/docs/File:Store-user-settings-2.png)

New settings become available here as soon as you add them on "Bot Store > User settings" screen.

## Asking user for settings

User sees the settings right after purchasing the script:

[![Store-user-settings-3.png](https://www.mysmartbots.com/dev/docs/images/f/fc/Store-user-settings-3.png)](https://www.mysmartbots.com/dev/docs/File:Store-user-settings-3.png)

## Settings and releases

When you do a new [release](https://www.mysmartbots.com/dev/docs/index.php?title=Releases&action=edit&redlink=1 "Releases (page does not exist)"), the current settings list is being saved along with the release. Thus, upcoming "User settings" changes won't affect the previous releases:

[![Store-user-settings-4.png](https://www.mysmartbots.com/dev/docs/images/c/cb/Store-user-settings-4.png)](https://www.mysmartbots.com/dev/docs/File:Store-user-settings-4.png)

Thus, you can safely rename, add or remove settings while developing an updated version of the script. Updated/removed settings won't cause already purchased versions to crash.
