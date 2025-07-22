# Scan nearby avatars - SmartBots Developers Docs


Script scans for nearby avatars and logs them. Since console.log is limited to 4kb, avatars are logged one by one.

// Bots Playground script: \[TEST\] nearbyAvatars (build 1 by Glaznah Gassner)
console.log(\`${process.name} started\`);

const result \= await Bot.scanNearbyAvatars();
console.log(\`Avatars arrived: (${JSON.stringify(result).length} bytes)\`);

if(JSON.stringify(result).length < 1024) {
	console.log("Raw response:", result);
}

if(!result.success) {
	console.log("Error scanning avatars: " + result.error);
}

if(!result.avatars) {
	console.log(\`No avatars found in command result\`);
} else {
	for(const avatar of result.avatars) {
		// Uncomment below or raw output
		// console.log(JSON.stringify(avatar, null, 2));

		console.log(\`${avatar.name}: seen for ${avatar.seenSeconds} seconds\`);
	}
}

process.exit();
