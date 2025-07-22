# touchAttachment - SmartBots Developers Docs

Touches an attachment of the bot (HUD or wearable object)

Bot.touchAttachment(objectName, linkNumber);

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
|     | objectName | yes | The name of the object to touch. |
|     | linkNumber | yes | The link number of the prim (root prim = 1) |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |

## Return value

*   If object is not found, bot returns _result.success=false_ and error message in _result.error_ (use _.then(function(result)_ to catch this).
*   If linkNumber is wrong (less than 1 or more than number of child prims), function returns a success but no touch happens.

Remember that bot have to load all objects from SL before touching them. So:

*   after logging in, give bot about 30 seconds to load surrounding objects,
*   the same after teleporting.

### Determining the link number

The root prim is always 1 (so, linkNumber=1 for 1-prim objects too).

To get the link number of the specific child prim use Phoenix Firestorm viewer:

![Get object linknum.jpg](https://www.mysmartbots.com/dev/docs/images/4/4c/Get_object_linknum.jpg)

1.  Start editing your object
2.  Check "Edit linked" option
3.  Select required child prim
4.  See the "Link number" value

## Examples

Touch a special test attachment object (contact SmartBots support to get it):

// Touch the button of the "Touch tester v2.0" object:
Bot.touchAttachment("Touch tester v2.0", 2);

// Gracefully exit since we're done
exit();
