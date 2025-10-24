# CLAUDE.md

## Project Overview

This repository contains:
1. **Claude CLI Tool** - A command-line interface for interacting with Claude AI
2. **SmartBots Documentation** - Comprehensive documentation for SmartBots Bots Playground scripting

## SmartBots Bots Playground

SmartBots Bots Playground is a JavaScript sandbox environment for controlling Second Life bots through code. Located in `smartbots/docs/Bot_Playground/`.

### Core Concepts

#### 1. Commands
Commands are JavaScript functions that control bot actions:
```javascript
Bot.im("Avatar Name", "Hello!");
Bot.say("Hello world!");
Bot.teleport("Region Name", 128, 128, 0);
```

#### 2. Events
Events are callback functions that handle bot and world events:
```javascript
Bot.on("instant_message", function(data) {
  console.log("Received message:", data);
});
```

#### 3. AI Integration
SmartBots includes conversational AI capabilities:
```javascript
const conversation = Bot.AI.getConversationByName("Avatar Name");
await conversation.chat("Hello!");
```

### Scripting Environment

- **Language**: JavaScript (NodeJS engine)
- **Async Support**: Modern async/await syntax is FULLY supported and RECOMMENDED
- **ES6**: Limited support (async/await works, but import/export disabled)
- **Limitations**: Cannot include one script into another

### Documentation Structure

```
smartbots/docs/
├── Bot_Playground.md              # Main overview
├── Commands.md                    # Command reference
├── Events.md                      # Event reference
├── SmartBots_AI.md               # AI features
├── Webhooks.md                   # Incoming webhooks
├── Callbacks_and_return_values.md # Async patterns
└── Bot_Playground/
    ├── Scripting_Guide.md        # Comprehensive guide
    ├── Commands/                 # Detailed command docs
    │   ├── im.md
    │   ├── teleport.md
    │   ├── say.md
    │   └── [70+ command files]
    ├── Events/                   # Detailed event docs
    │   ├── instant_message.md
    │   ├── chat_message.md
    │   └── [20+ event files]
    ├── AI/                       # AI-related docs
    │   ├── Bot.AI.chat.md
    │   ├── Conversation.chat.md
    │   └── [6 AI files]
    ├── Built-in_Functions/       # Utility functions
    │   ├── console.log.md
    │   ├── http.get.md
    │   └── [10+ function files]
    └── Examples/                 # Code examples
```

### Key Feature Categories

#### Messaging & Communication
- `Bot.say()` - Local chat
- `Bot.im()` - Instant messages
- `Bot.sendGroupIM()` - Group chat
- `Bot.sendNotice()` - Group notices
- Events: `instant_message`, `chat_message`, `group_im`

#### Movement & Navigation
- `Bot.teleport()` - Teleport to location
- `Bot.walkTo()` - Walk within region
- `Bot.fly()` - Start/stop flying
- `Bot.sit()` - Sit on object
- Events: `autopilot_completed`, `self_position`, `teleport_status`

#### Group Management
- `Bot.activateGroup()` - Activate group
- `Bot.inviteGroup()` - Invite members
- `Bot.ejectGroupMember()` - Eject members
- `Bot.setGroupRole()` - Manage roles
- Events: `group_offer`, `group_im`, `group_notice`

#### Inventory & Items
- `Bot.listInventory()` - List items
- `Bot.giveInventory()` - Give items
- `Bot.acceptInventoryOffer()` - Accept items
- `Bot.wear()` / `Bot.takeoff()` - Manage appearance
- Events: `inventory_offer`

#### World Interaction
- `Bot.touchPrim()` - Touch objects
- `Bot.scanNearbyAvatars()` - Scan region
- `Bot.takeInworldPrim()` - Take objects
- `Bot.replyDialog()` - Respond to dialogs
- Events: `script_dialog`, `region_restart`

#### AI Features
- `Bot.AI.chat()` - Raw AI requests
- `Bot.AI.getConversationByName()` - Get/create conversation
- `Conversation.chat()` - Conversational AI
- `Conversation.configure()` - Configure AI behavior

#### Built-in Functions
- `console.log()` / `console.error()` - Logging
- `http.get()` / `http.post()` - HTTP requests
- `http.requestWebhook()` - Webhook endpoints
- `localStorage.get()` / `localStorage.set()` - Data persistence
- `process.sleep()` - Delay execution

### Best Practices for SmartBots Scripts

#### 1. Always Use async/await (CRITICAL)
```javascript
// ✅ CORRECT - Modern approach
async function sendMessage(name, message) {
  const result = await Bot.name2key(name);
  if (result.success) {
    await Bot.im(name, message);
  }
}

// ❌ AVOID - Old callback hell
Bot.name2key(name, function(result) {
  Bot.im(name, message);
});
```

#### 2. Log Liberally
```javascript
console.log("Script started");
console.log("Looking up UUID for:", avatarName);
console.log("Profile result:", profileData);
```

#### 3. Handle Errors Properly
```javascript
async function safeOperation() {
  try {
    const result = await Bot.someCommand();
    if (!result.success) {
      console.error("Operation failed:", result.error);
      return;
    }
    // Continue processing
  } catch (error) {
    console.error("Exception occurred:", error);
  }
}
```

#### 4. Modularize with Functions
```javascript
async function getAvatarAge(name) {
  const keyResult = await Bot.name2key(name);
  if (!keyResult.success) throw new Error("Avatar not found");

  const profile = await Bot.avatarProfile(keyResult.slkey);
  return profile.age;
}
```

#### 5. Use Webhooks for External Integration
```javascript
// Set up webhook
Bot.on("playground_webhook", function(event) {
  console.log("Received webhook:", event.payload);
});

const webhook = await http.requestWebhook();
console.log("Webhook URL:", webhook.url);
console.log("Token:", webhook.token);
```

### Common Patterns

#### Event-Driven Bot
```javascript
// Respond to instant messages
Bot.on("instant_message", async function(data) {
  if (data.name === "Some Avatar") {
    await Bot.im(data.name, "Hello back!");
  }
});

// Handle friendship offers
Bot.on("friendship_offer", async function(data) {
  await Bot.acceptFriendshipOffer(data.name, true);
});
```

#### Conversational AI Bot
```javascript
Bot.AI.configure({
  instructions: "You are a helpful Second Life assistant."
});

Bot.on("instant_message", async function(data) {
  const conversation = Bot.AI.getConversationByName(data.name);
  const response = await conversation.chat(data.message);
  await Bot.im(data.name, response.reply);
});
```

#### Automated Group Manager
```javascript
Bot.on("group_offer", async function(data) {
  console.log("Group invite from:", data.from);
  // Auto-accept or reject based on criteria
});

Bot.on("instant_message", async function(data) {
  if (data.message.startsWith("!invite")) {
    const target = data.message.split(" ")[1];
    await Bot.inviteGroup("group-uuid", target);
  }
});
```

### Important Notes

1. **Asynchronous Nature**: Almost all Bot commands are asynchronous - ALWAYS use `await`
2. **Token Usage**: AI features consume tokens - monitor usage
3. **Rate Limits**: Be mindful of command frequency
4. **Persistence**: Use `localStorage` for data that needs to survive script restarts
5. **Webhooks**: Webhook URLs/tokens change on script restart
6. **QubicBot**: Some features are not yet available for QubicBot (check docs)

### Reference Documentation

- Main Guide: `smartbots/docs/Bot_Playground/Scripting_Guide.md`
- Commands: `smartbots/docs/Commands.md`
- Events: `smartbots/docs/Events.md`
- AI: `smartbots/docs/SmartBots_AI.md`
- Webhooks: `smartbots/docs/Webhooks.md`
- Examples: `smartbots/docs/Bot_Playground/Examples/`

## Claude CLI Tool

### Core Bash Commands
- `pip install -r src/requirements.txt` - Install Python dependencies

### Code Style
- Follow PEP 8 for Python code
- Use descriptive variable names
- Add comments for complex logic

### Branching
- Use `feature/*` for new features
- Use `bugfix/*` for bug fixes
- Use `docs/*` for documentation updates

### PR Etiquette
- Always link to relevant issue
- Tag at least one reviewer
- Include clear description of changes
- Test thoroughly before submitting
