# localStorage.get - SmartBots Developers Docs

Restores a string value from a persistent storage. Also check [localStorage.set()](https://www.mysmartbots.com/dev/docs/Bot_Playground/Built-in_Functions/localStorage.set "Bot Playground/Built-in Functions/localStorage.set").

var data \= localStorage.get("old\_data");

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | name | yes | the name of the persistent value you would like to get. |
| Output: |     |     |     |
|     | value |     | The value you've stored in a persistent storage. |

This function works similar to browser JavaScript localStorage.get(). It retrieves value from a persistent storage.

localStorage is shared by all scripts of the same bot. Thus, you can set values in one bot script and retrieve it in another script.
