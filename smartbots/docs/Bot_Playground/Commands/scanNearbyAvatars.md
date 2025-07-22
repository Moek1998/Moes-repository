# scanNearbyAvatars - SmartBots Developers Docs

Scans current region for other avatars.

const result \= await Bot.scanNearbyAvatars();

## Reference

This command accepts the following parameters:

| Variable |     | Required | Description |
| --- | --- | --- | --- |
| Input: |     |     |     |
| Output: |     |     |     |
|     | Function returns a [Promise](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") with the following data: |     |     |
|     | success | bool | _true_ if command completed successfully |
|     | error | string | error string if command has failed |
|     | avatars | Array | An array containing avatars on sim. See "Response details" for more info. |

## Response details

'avatars' field of the response is an array and contains the list of avatars our bot sees:

{
  // Avatar name
  "name": "GrrrillaBongo Resident",
  // Avatar UUID
  "UUID": "d8e20552-ca84-4c42-b8d3-e8fa5fbdcc6b",

  // The parcel this avatar currently in
  "parcelID": 177,

  // If avatar is sitting on something
  "sitting": false,

  // Position of avatar in-world
  "position": {
    "X": 110,
    "Y": 75,
    "Z": 32
  },
  // Local position. If avatar is sitting this position is relative to sit parent
  "localPosition": {
    "X": 110,
    "Z": 32,
    "Y": 75
  },
  // Avatar heading (the view direction)
  "heading": 0,
  // Local heading (for sitting avatars)
  "localHeading": 0,

  // The distance to this avatar
  "distance": 129.97195,

  // When we seen this avatar for first time (see Details)
  "seenSince": "2022-10-18T12:36:58.2626463Z",
  // How much seconds do we see this avatar
  "seenSeconds": 123,
}

## Details

'SeenSince' value shows when we saw the specific avatar for the first time _when running scanNearbyAvatars_. For example:

1.  Bot logs on. Time passes (say, 1 hour).
2.  Script sends 'scanNearbyAvatars' command
3.  Bot sees one avatar, Guest1 and sets SeenSince to current time (say, "2022-10-18 13:00")
4.  5 minutes passes
5.  Script sends 'scanNearbyAvatars' again
6.  Now bot sees that another avatar arrived - Guest2. Its SeenSince will be "2022-10-18 13:05"

Thus, all further calls to 'scanNearbyAvatars' will return:

*   Guest1: SeenSince = "2022-10-18 13:00"
*   Guest2: SeenSince = "2022-10-18 13:05"

SeenSeconds shows the number of seconds we see avatar (Now - SeenSince).

## Throttling

The maximum rate of calling scanNearbyAvatars is 2 calls per 10 seconds. Excessive calls will return "Frequent API requests throttled" error.

## Data size

The amount of data returned by this command can be pretty large (up to 10kb and more). Remember [console.log](https://www.mysmartbots.com/dev/docs/Bot_Playground/Built-in_Functions/console.log "Bot Playground/Built-in Functions/console.log") is unable to log more than 4kbytes.

If you need to trace scanNearbyAvatars response, use for(...of...) loop (as used in Examples below).

## Examples

See the \[[nearby avatars](https://www.mysmartbots.com/dev/docs/Bot_Playground/Examples/Scan_nearby_avatars%7CScan)\] scripts in our Playground Examples section.
