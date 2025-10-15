# SmartBots Playground Scripting Guide

This guide provides a comprehensive overview of how to write scripts for the SmartBots Bots Playground. It covers the scripting environment, logging, functions, and the modern approach to handling asynchronous operations using `async/await`.

## Introduction to SmartBots Scripting

The SmartBots Bots Playground is a sandbox environment that runs your scripts to control your Second Life bot. The scripting language is JavaScript, running on a NodeJS engine.

### Key Concepts

- **Commands**: These are functions you call in your script to make your bot perform actions (e.g., `Bot.say("Hello!")`).
- **Events**: These are callbacks you define in your script to react to things that happen in Second Life (e.g., receiving a chat message).

### Environment Limitations

- **ECMAScript 6 (ES6) is not fully supported**: While modern features like `async/await` are available, some other ES6 features may not be.
- **`import`/`export` is disabled**: You cannot include one script into another. All your code must be in a single file.

## Logging

Logging is essential for debugging your scripts. The Playground provides two types of logs:

- **Error Log**: Automatically logs any errors that occur during script execution.
- **Runtime Log**: You can write to this log yourself using the `console.log()` function.

### Using `console.log()`

You can use `console.log()` to print messages, variables, or object contents to the runtime log to track your script's execution.

```javascript
console.log("Starting the script...");
const myVariable = "test";
console.log("The value of myVariable is:", myVariable);
```

## Functions

You can and should organize your code into functions, just like in any other JavaScript program. This makes your code more readable, reusable, and easier to debug.

```javascript
function greet(name) {
  Bot.say("Hello, " + name + "!");
}

// Call the function
greet("Smartbots Resident");
```

## Asynchronous Operations with async/await

Many bot commands (like getting an avatar's UUID or profile information) are **asynchronous**. This means they don't return a result immediately. Your script starts the command and continues running without waiting. To handle this, the Playground supports the modern `async/await` syntax, which is the recommended approach.

### What is `async/await`?

`async/await` is a special syntax that lets you write asynchronous code as if it were synchronous.

- `async`: You declare a function as `async` to indicate that it will contain asynchronous operations.
- `await`: You use the `await` keyword before a call to an asynchronous function (like a `Bot` command). This pauses the execution of your `async` function until the command completes and returns a result.

**Important**: The `await` keyword can only be used inside a function marked as `async`.

### Example: From Callbacks to `async/await`

Let's look at a common task: getting an avatar's age and sending it in an IM.

**The old way (with Promises):**

```javascript
var slname = "Smartbots Resident";

Bot.name2key(slname)
  .then(function(result) {
    return Bot.avatarProfile(result.slkey);
  })
  .then(function(result) {
    Bot.im("Glaznah Gassner", "The age of " + slname + " is " + result.age);
  });
```

**The new, better way (with `async/await`):**

This code is much cleaner and easier to read.

```javascript
// We wrap our logic in an async function
async function sendAvatarAge(targetAvatar, recipientAvatar) {
  console.log("Looking up UUID for:", targetAvatar);
  const name2keyResult = await Bot.name2key(targetAvatar);

  if (!name2keyResult.success) {
    console.log("Could not find avatar:", targetAvatar);
    return;
  }

  console.log("Getting profile for UUID:", name2keyResult.slkey);
  const profileResult = await Bot.avatarProfile(name2keyResult.slkey);

  const message = "The age of " + targetAvatar + " is " + profileResult.age;
  console.log("Sending IM:", message);
  await Bot.im(recipientAvatar, message);

  console.log("Script finished.");
}

// Call our main async function
sendAvatarAge("Smartbots Resident", "Glaznah Gassner");
```

## A Complete Scripting Example

Here is a full script that demonstrates logging, functions, and `async/await` to get the age of a specified avatar.

```javascript
const AVATAR_TO_LOOKUP = "Smartbots Resident";

console.log("Script started. Looking up age for:", AVATAR_TO_LOOKUP);

// Call our main async function and handle any potential errors
getAge(AVATAR_TO_LOOKUP)
  .then(age => {
    console.log("Successfully retrieved age:", age);
  })
  .catch(error => {
    console.log("An error occurred:", error);
  });

/**
 * Gets the age of a Second Life avatar.
 * @param {string} slname - The name of the avatar.
 * @returns {Promise<number>} - The age of the avatar.
 */
async function getAge(slname) {
  // Get the avatar's UUID from their name
  const res1 = await Bot.name2key(slname);
  if (!res1.success) {
    // Throw an error if the avatar is not found
    throw new Error("Avatar not found: " + slname);
  }

  // Get the avatar's profile information from their UUID
  const res2 = await Bot.avatarProfile(res1.slkey);

  // Return the age from the profile
  return res2.age;
}
```

## Best Practices

- **Always use `async/await`**: For any bot command that performs an action and might take time, use `await`. This prevents race conditions and makes your code's logic flow predictably.
- **Log Liberally**: Use `console.log()` to track the state of your script. It's the primary way to debug.
- **Modularize with Functions**: Break your code into smaller, single-purpose functions (preferably `async` functions) to keep it organized.
- **Handle Errors**: Asynchronous operations can fail. Use `try...catch` blocks within your `async` functions or `.catch()` on the final promise to handle errors gracefully.
