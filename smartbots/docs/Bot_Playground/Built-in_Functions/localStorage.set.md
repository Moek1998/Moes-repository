# localStorage.set - SmartBots Developers Docs

Puts a string value into a persistent storage. Also check [localStorage.get()](https://www.mysmartbots.com/dev/docs/Bot_Playground/Built-in_Functions/localStorage.get "Bot Playground/Built-in Functions/localStorage.get").

localStorage.set(name, value);

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | name | yes | the name of the persistent value you would like to store |
|     | value | yes | the value you want to save. |
| Output: |     |     |     |
|     | result |     | This function does not return anything |

## Limitations

localStorage is intended to store short key-value pairs. The size of the value is limited to 6144 bytes. If you exceed this size script generates a warning:

 localStorage value is more than 6144 bytes and not persistent

If you store significant amount of data (like dozen of keys, few kilobytes each), consider using your own key-value database using http requests.

This function works similar to browser JavaScript localStorage.set(). It saves value into a persistent storage.

localStorage is shared by all scripts of the same bot. Thus, you can set values in one bot script and retrieve it in another script.

Also note that localStorage supports string values only. To save something more complicated, use JSON.stringify(var).

## Inter-script communication

Executing localStorage.set() will cause [localStorage.on("update")](https://www.mysmartbots.com/dev/docs/Bot_Playground/Built-in_Functions/localStorage.on "Bot Playground/Built-in Functions/localStorage.on") event to fire on _other scripts of this bot_.
