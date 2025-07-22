# AI IM Autoresponder - SmartBots Developers Docs

## AI IM Autoresponder

This is a source code of simple AI autoresponder by SmartBots, available in [Bot Store](https://www.mysmartbots.com/store/item/100/ai_gpt_im_autoresponder/).

Script listens for incoming IMs, sends them to SmartBots AI engine and responds the result back.

// Bots Playground script: Test (build 1 by Glaznah Gassner)

const aiSettings \= {
	instructions: "You are a bot in Second Life. Act like a greater, be polite and friendly. Answer any question you can.",
};

// Init default settings
Object.assign(aiSettings, userSettings);

if(aiSettings.maxResponseTokens) {
	aiSettings.maxResponseTokens \= Number(aiSettings.maxResponseTokens);
}

// console.log("AI settings:", aiSettings);

// Init AI
Bot.AI.configure(aiSettings);

// Listen for IMs
Bot.on("instant\_message", (event) \=> {
	if(event.speaker\_type != "AVATAR") { return; }

	processMessage(event.speaker\_name, event.speaker\_uuid, event.message);
});

console.log(process.name + " is running");

async function processMessage(senderName, senderUUID, message) {
	console.log(\`\[IM\] ${senderName}: ${message}\`);

	Bot.startTyping(senderUUID);

	try {
		const convo \= Bot.AI.getConversationByName(senderName);
		let res;

		try {
			res \= await convo.chat(message, { featureEmptyResponse: true });
		} catch(e) {
			console.error(\`AI error: ${e.message}\`);
			return;
		}

		if(!res.text) {
			console.log(\`\[AI\] ${Bot.name}: response empty, ${res.emptyTextReason}\`);
			return;
		}

		console.log(\`\[AI\] ${Bot.name}: ${res.text}\`);
		Bot.im(senderUUID, res.text);
	} finally {
		Bot.stopTyping(senderUUID);
	}
}
