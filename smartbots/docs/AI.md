# AI - SmartBots Developers Docs

## AI Chat Examples

The following example shows a conversation being started and continued with the AI by creating an Async Function.

const chatOptions \= {
    instructions: "You are a metal guardian support bot in Second Life. You freeze every few words."
};

const SENDER \= "Glaznah Gassner";
// Start from scratch (to avoid previous message to mess)
Bot.AI.forgetConversation(SENDER);
Bot.AI.configure(chatOptions);

await processMessage(SENDER, "Hello!");

await sleep(5);

await processMessage(SENDER, "Do you know my name?");
process.exit();

async function processMessage(sender, message) {
    console.log(\`\[IM\] ${sender}: ${message}\`);
    const convo \= Bot.AI.getConversationByName(sender);
    const res \= await convo.chat(message);
    console.log(\`\[AI\] ${Bot.name}: ${res.text}\`);
}

* * *

The below example shows a continued conversation using the parentMessageId to relate to the last message for the AI to continue the chat.

const SENDER \= "Glaznah Gassner";

const chatOptions \= {
    instructions: "You are a fictional robot which skips all letters 'o' and replaces all 'o' with apostrophe.Respond like this robot."
};

Bot.AI.configure(chatOptions)

const res \= await Bot.AI.chat("Hello!", SENDER);

console.log("AI response:", res.text);

await sleep(5);

const res2 \= await Bot.AI.chat("Are you sure?", SENDER, {
    parentMessageId: res.messageId
});

console.log("AI response:", res2.text);

process.exit();
