# Examples - SmartBots Developers Docs

From SmartBots Developers Docs

Jump to: [navigation](#mw-head), [search](#p-search)

This section contains example scripts we've written to test Bots Playground features, and to demonstrate them.

We just started writing example scripts, and here's what we have already:

## Webhook Example

The following example demonstrates the use of a webhook:
1. creating a webhook,
2. displaying webhook details,
3. sending data from a remote server,
4. receiving these data in a script.

### Playground script
```javascript
Bot.on("playground_webhook", (event) => {
  console.log("Webhook received:", event);
});

// 1. Create a webhook
const webhook = await http.requestWebhook(); // Requests the webhook URL and token

// 2. Display its data
// (You probably send this to your server but we just display the data)
console.log("Webhook details:", webhook);
```

**Example output:**
```
Webhook details:
{
  url: "https://gate07.play.mysmartbots.com/userhook/ca4687a9-db28-43ee-9bb8-cf80100t41cf",
  token: "PBubZ9CbPd9PWUm2n6L5ygfHkhCOUf8V"
}
```

### Remote server simulation (curl)
```bash
curl --location 'https://gate07.play.mysmartbots.com/userhook/ca4687a9-db28-43ee-9bb8-cf80100t41cf' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: 'Bearer PBubZ9CbPd9PWUm2n6L5ygfHkhCOUf8V'' \
  --data '{"exampleData": 123456}'
```

**Example output:**
```json
{
    "success": true,
    "correlationId": "bb980f2e-b3e0-4eee-acd0-f5041af6a449"
}
```

### Playground webhook output
```
Webhook received:
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
