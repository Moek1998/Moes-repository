# Working with bot money balance

From SmartBots Developers Docs

Jump to: [navigation](#mw-head), [search](#p-search)


The following script allows sending AMOUNT\_TO\_SEND of money to RECIPIENT. Script does this by:

1.  calling [name2key()](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/name2key "Bot Playground/Commands/name2key") function to get a RECIPIENT's uuid
2.  checking available balance using [getBalance()](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/getBalance "Bot Playground/Commands/getBalance")
3.  sending money using [giveMoney()](https://www.mysmartbots.com/dev/docs/Bot_Playground/Commands/giveMoney "Bot Playground/Commands/giveMoney")

var RECIPIENT \= "Glaznah Gassner";
var AMOUNT\_TO\_SEND \= 1;

var uuid \= "";
var balance;

Bot
	// 1. First, request the UUID of the recipient
	.name2key(RECIPIENT)

	// 2. Save UUID, then check our balance
	.then(function(result) {
		uuid \= result.slkey;
		if(!result.success) {
			throw "Can't resolve recipient UUID";
		} else {
			console.log("The recipient's UUID is " + uuid);
		}

		return Bot.getBalance();
	})

	// 3. Save balance (for a future check) and send money
	.then(function(result) {
		balance \= result.balance;
		console.log("My balance is " + balance);

		if(balance < AMOUNT\_TO\_SEND) { throw "I have not enough money to deliver"; }

		return Bot.giveMoney(uuid, AMOUNT\_TO\_SEND, "Playground test");
	})

	// 4. Check the operation result and check our balance again
	.then(function(result) {
		console.log("giveMoney successful: " + (result.success? "yes": "no"));

		return Bot.getBalance();
	})

	// 5. Compare with expected balance
	.then(function(result) {
		console.log("New balance: " + result.balance + "\\n" +
								"expected balance: " + (balance \- AMOUNT\_TO\_SEND));
	})

	// 6. We will fall here in case of any error
	.catch(function(error) {
		console.log("Script error: " + error);
	})

	// 7. Exit - we don't need this script running forever
	.then(function() {
		exit();
	});
