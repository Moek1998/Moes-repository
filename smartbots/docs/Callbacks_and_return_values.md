# Callbacks and return values - SmartBots Developers Docs


Javascript is mostly asynchronous language, and Bot Playground too. This means that when you call an operation, it starts at the background immediately, and your program continues running without waiting for the result.

This may cause troubles if you need that result. For example, imagine we want to:

1.  get an UUID of avatar
2.  using that UUID, know the age of avatar
3.  finally, send the age to another avatar.

> **Important update**
>
> As of October 2020, Bots Playground commands support _await_ instruction. It is recommended and makes scripting easier!
>
> See [Async and await](https://www.mysmartbots.com/dev/docs/Bot_Playground/Async_and_await "Bot Playground/Async and await") for examples.

## Starting from scratch

To start, we use _name2key_ bot command:

Bot.name2key("Glaznah Gassner");

Okay, we know how to **ask** the question. How do we get the reply?

## Way 1: Using callbacks

The simplest way is to use callback functions:

var slname \= "Smartbots Resident";

Bot.name2key(slname, function(result) {
  console.log("Got the UUID!", result.slkey);

  // Oh, now the next step, also with a callback
  Bot.avatarProfile(result.slkey, function(result2) {
    console.log("Got the age!", result2.age);

    Bot.im("Glaznah Gassner", "The age of " + slname + " is " + result2.age);
  });
});

console.log("I've asked for UUID and now waiting for answer");

Looks a bit weird. Imagine we want to add the third callback level? This is called a **callback hell**.

## Way 2: Promises

To get rid of callback hell, Bot Playground supports a Promise object. This is how it looks like:

var slname \= "Smartbots Resident";

Bot.name2key(slname)
  .then(function(result) {
    // this code will be called when name2key() get completed
    console.log("Got the UUID!", result.slkey);

    // Oh, now the next step
    return Bot.avatarProfile(result.slkey);
  })
  .then(function(result) {
    // this code will be called when avatarProfile() get completed
    console.log("Got the age!", result2.age);

    Bot.im("Glaznah Gassner", "The age of " + slname + " is " + result2.age);
  });

console.log("I've asked for UUID and now waiting for answer");

Looks a bit easier? Each command (name2key, avatarProfile and others) returns a special object, Promise. You can call its _then()_ function and set your handler. It will be executed as soon as command completed.

Subsequent commands can be chained like example above. Note that we've added a _return Bot.avatarProfile()_ so next _.then()_ get chained to the avatarProfile command.

### Breaking the promise function chain

What if you want to break the chain? Imagine the following code:

var slname \= "Smartbots Resident";
var all\_money \= 0;
var uuid \= "";

// we want to send money to avatar

Bot.name2key(slname)
  .then(function(result) {
    // we know the recipient's UUID now
    uuid \= result.slkey; // <== a potential problem here if we can't find a recipient's UUID
    return Bot.getBalance();
  })
  .then(function(result) {
    // we know our balance now
    all\_money \= result.balance;
    Bot.giveMoney(uuid, all\_money);
  })
  .then(function() {
    // Stop our script
    console.log("Script has been finished");
    exit();
   });

What if we won't find a recipient (an account deleted or name typed wrongfully)? We want to bail our at the very first .then(), right? This is when .catch() helps:

var slname \= "Smartbots Resident";
var all\_money \= 0;
var uuid \= "";

// we want to send money to avatar

Bot.name2key(slname)
  .then(function(result) {
    // Oh-oh, a name mistake!
    if(!result.success) { throw "Unknown recipient!"; }

    // we know the recipient's UUID now
    uuid \= result.slkey;
    return Bot.getBalance();
  })
  .then(function(result) {
    // we know our balance now
    all\_money \= result.balance;
    Bot.giveMoney(uuid, all\_money);
  })

  .catch(function(error) {
    // this code will be called when something wrong happened with a command
    console.log("We've faced an error: " + error);
  })

  .then(function() {
    // Stop our script at any case
    console.log("Script has been finished");
    exit();
   });

We added two pieces of code:

  if(!result.success) { throw "Unknown recipient!"; }

and

  .catch(function(error) {
    // this code will be called when something wrong happened with a command
    console.log("We've faced an error: " + error);
  })

The first line of code throws an error and cancels all further operations **until** the .catch() block (if all operations complete successfully, the .catch() block will be just skipped).

Note that .then() block after a .catch() will be executed at any case - just because it stands **after** the catch.

## More examples

Check Bot [Playground Examples](https://www.mysmartbots.com/dev/docs/Bot_Playground/Examples "Bot Playground/Examples") for more code to play with.
