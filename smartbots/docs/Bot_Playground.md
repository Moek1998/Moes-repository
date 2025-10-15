# SmartBots Bots Playground - SmartBots Developers Docs

SmartBots Bots Playground is a JavaScript sandbox to run your own programs to control your Second Life bot.

The Bots Playground is available here: [play.mysmartbots.com/](https://play.mysmartbots.com/)

## Controlling bots with JavaScript

![Bots Playground screenshot-2.png](https://www.mysmartbots.com/dev/docs/images/2/2b/Bots_Playground_screenshot-2.png)

Playground runs programs written JavaScript. The pure javascript: with callbacks, functions, arrays and objects. The underlying javascript engine is NodeJS.

There are some limitations applied yet:

*   We do not support ECMAScript 6
*   import/export is disabled
*   you can't include one script into another (yet)

## Interacting with your bot

Your program runs in a sandbox and sends commands to the bot. Events come from the bots to your program.

This two-way communication is tied directly into javascript program routines:

*   [bot commands](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands "Bot Playground/Commands") are functions you call
*   [events](https://www.mysmartbots.com/dev/docs/Bot_Playground/Events "Bot Playground/Events") are callback functions you specify

Refer to [Examples](https://www.mysmartbots.com/dev/docs/Bot_Playground/Examples "Bot Playground/Examples") page for more info.

## Read more

*   [Comprehensive Scripting Guide](./Bot_Playground/Scripting_Guide.md)
*   [Playground FAQ](https://www.mysmartbots.com/dev/docs/Bot_Playground/Faq "Bot Playground/Faq")
*   [Webhooks](./Webhooks.md)
*   [Bug Hunter program](https://www.mysmartbots.com/dev/docs/Bot_Playground/Bug_Hunter_program "Bot Playground/Bug Hunter program")
*   [Create and sell Playground scripts](https://www.mysmartbots.com/dev/docs/Bot_Playground/Store "Bot Playground/Store")
