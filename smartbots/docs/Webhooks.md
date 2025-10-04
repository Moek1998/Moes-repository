# Webhooks

Incoming webhooks are available at Bots Playground, giving your scripts an ability to receive data directly from your servers.

This addition opens up a wide range of possibilities:
- receive remote commands,
- integrate with third-party services (like Discord),
- create two-way communication bridges between your servers and Second Life.

## How it works

The update introduces a new function `http.requestWebhook()` and a new event: `playground_webhook`.

### `http.requestWebhook()`

Allocates a new, per-run webhook URL and authorization token for the current script instance.

**Reference**
```javascript
const webhook = await http.requestWebhook();
```

**Output:**

Function returns a `Promise` with the following data:

| Variable  | Type   | Description                                                     |
|-----------|--------|-----------------------------------------------------------------|
| `success` | bool   | `true` if command completed successfully                        |
| `error`   | string | error string if command has failed                              |
| `url`     | string | Endpoint that accepts your server’s POST requests.              |
| `token`   | string | Bearer token you must include in the Authorization header.      |

**Comments**

- It is good practice to register the the event first: Put `Bot.on("playground_webhook", …)` before `http.requestWebhook()` to avoid missing early responses.
- Hook URL and token change ("release") on every script restart. Make sure to deliver them to your remote server.
- The consequent calls to `requestWebhook()` return the same url/token. These values persist while the script is running. There's no system-wide limits on the number of webhooks.

### `playground_webhook` event

Fires when the script’s webhook receives an HTTP request from your server.

**Reference**
```javascript
Bot.on("playground_webhook", function(event) { ... });
```

**Event Object:**

| Variable        | Type   | Description                                               |
|-----------------|--------|-----------------------------------------------------------|
| `name`          | string | The name of the event                                     |
| `bot_slname`    | string | Your bot’s Second Life name (e.g. "smartbots Resident").  |
| `hookId`        | string | Identifier of the current webhook.                        |
| `correlationId` | string | A unique identifier for this request.                     |
| `payload`       | object | Parsed JSON data from the request.                        |

**Important notes**

1. If the payload on the request is not valid JSON, the `payload` object will come through as an empty object.
2. To send a string payload set `"Content-Type: text/plain"` on a remote server.
3. It is best practice to place the event above the `http.requestWebhook()` command, to catch any early requests.

### Sending a request from a remote server

Sending a POST request to the webhook URL, and including the `Authorization` and `Content-Type` headers. The payload is JSON.

```bash
curl --location 'https://gate07.play.mysmartbots.com/userhook/ca4687a9-db28-43ee-9bb8-cf80100t41cf' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer PBubZ9CbPd9PWUm2n6L5ygfHkhCOUf8V' \
  --data '{"exampleData": 123456}'

# Use --header 'Content-Type: text/plain' to send string payload instead of JSON
```

**Example response:**
```json
{
    "success": true,
    "correlationId": "bb980f2e-b3e0-4eee-acd0-f5041af6a449"
}
```

**Example `playground_webhook` event:**
```json
{
  "name": "playground_webhook",
  "bot_slname": "smartbot Resident",
  "hookId": "ca4687a9-db28-43ee-9bb8-cf80100t41cf",
  "correlationId": "bb980f2e-b3e0-4eee-acd0-f5041af6a449",
  "payload": {
    "exampleData": 123456
  }
}
```