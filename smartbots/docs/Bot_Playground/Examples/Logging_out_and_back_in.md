# Logging out and back in


This example script logs bot out, waits for 30 seconds and then logs back in. To track the procedure, we set event handlers: before\_logout, before\_login and after\_login.

P.S. Note that you can chain Bot.on() function calls as shown below.

Bot
	.on("before\_logout", function(event) {
		console.log("Event: Bot is logging out");
	})
	.on("before\_login", function(event) {
		console.log("Event: Bot is logging in");
	})
	.on("after\_login", function(event) {
		console.log("Event: Bot has logged in");
	});

// Logout bot in few seconds (otherwise bot may not notice the events we just set)
setTimeout(function() {
	console.log("Logging out the bot...");
	Bot.logout();
}, 5 \* 1000);

// Then wait 30 second and login back
setTimeout(function() {
	console.log("Starting log in sequence...");

	Bot.login();
}, 30 \* 1000);
