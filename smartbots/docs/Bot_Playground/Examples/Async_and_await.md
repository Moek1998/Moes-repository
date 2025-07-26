# Async and await - SmartBots Developers Docs

## TL;DR

This is how async/await Playground script looks like:

const AVATAR \= "Smartbots Resident";

console.log("The age is:", await getAge(AVATAR);

async function getAge(slname) {
  const res1 \= await Bot.name2key(slname);
  const res2 \= await Bot.avatarProfile(res1.slkey);
  return res2.age;
}

console.log("This log appears only after all calculations are complete");

## A long story

Async/await is the JavaScript modern approach to the asynchronous programming. The concept may be hard to understand at the very beginning, but you'll find async functions extremely useful once you get used to them.

Let's take an example from [Callbacks and return values](https://www.mysmartbots.com/dev/docs/Bot_Playground/Callbacks_and_return_values "Bot Playground/Callbacks and return values") page:

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

After rewriting using _await_ the code looks this way:

const slname \= "Smartbots Resident";

const res1 \= await Bot.name2key(slname);
// this code will be called when name2key() get completed
console.log("Got the UUID!", res1.slkey);

const res2 \= await Bot.avatarProfile(res1.slkey);
// this code will be called when avatarProfile() get completed
console.log("Got the age!", res2.age);

await Bot.im("Glaznah Gassner", \`The age of ${slname} is ${res2.age}\`);

console.log("The script has been completed");

Looks much simpler and easier!

## Notes

Remember that _await_ may appear in _async_ functions only (see [JavaScript reference](https://javascript.info/async-await) and various tutorials for understanding). Thus, you may need to convert all your functions to async:

const AVATAR \= "Smartbots Resident";

console.log("The age is:", await getAge(AVATAR);

async function getAge(slname) {
  const res1 \= await Bot.name2key(slname);
  const res2 \= await Bot.avatarProfile(res1.slkey);
  return res2.age;
}

## More examples

Check Bot [Playground Examples](https://www.mysmartbots.com/dev/docs/Bot_Playground/Examples "Bot Playground/Examples") for more code to play with.
