/**
 * SmartBots API Test Script
 * 
 * This script will help us discover what functions are available
 * in the SmartBots JavaScript playground.
 */

console.log("🔍 Testing SmartBots API availability...");

// Test for global functions
const globalFunctions = [
    'walkTo',
    'teleportTo',
    'moveTo',
    'goTo',
    'walk',
    'teleport',
    'move',
    'setPosition',
    'getPosition',
    'getLocation'
];

console.log("\n📋 Testing global functions:");
globalFunctions.forEach(funcName => {
    if (typeof window[funcName] === 'function') {
        console.log(`✅ ${funcName} is available`);
    } else {
        console.log(`❌ ${funcName} is not available`);
    }
});

// Test for bot object
console.log("\n🤖 Testing bot object:");
if (typeof bot !== 'undefined') {
    console.log("✅ bot object exists");
    console.log("📋 Bot object properties:");
    Object.keys(bot).forEach(key => {
        console.log(`  - ${key}: ${typeof bot[key]}`);
    });
} else {
    console.log("❌ bot object not found");
}

// Test for other common objects
const commonObjects = ['client', 'avatar', 'player', 'character'];
console.log("\n🔍 Testing common objects:");
commonObjects.forEach(objName => {
    if (typeof window[objName] !== 'undefined') {
        console.log(`✅ ${objName} object exists`);
        console.log(`  Properties: ${Object.keys(window[objName]).join(', ')}`);
    } else {
        console.log(`❌ ${objName} object not found`);
    }
});

// Test for window object properties
console.log("\n🌐 Testing window object properties:");
const windowProps = Object.keys(window).filter(key => 
    key.toLowerCase().includes('walk') || 
    key.toLowerCase().includes('move') || 
    key.toLowerCase().includes('teleport') ||
    key.toLowerCase().includes('bot') ||
    key.toLowerCase().includes('client')
);
windowProps.forEach(prop => {
    console.log(`  - ${prop}: ${typeof window[prop]}`);
});

// Test basic movement
console.log("\n🚶 Testing basic movement:");
try {
    if (typeof walkTo === 'function') {
        console.log("✅ walkTo function found - testing with sample location");
        walkTo("Sinful/152/88/25");
    } else {
        console.log("❌ walkTo function not found");
    }
} catch (error) {
    console.log(`❌ Error testing walkTo: ${error.message}`);
}

// Test teleport
console.log("\n⚡ Testing teleport:");
try {
    if (typeof teleportTo === 'function') {
        console.log("✅ teleportTo function found - testing with sample location");
        teleportTo("Sinful/152/88/25");
    } else {
        console.log("❌ teleportTo function not found");
    }
} catch (error) {
    console.log(`❌ Error testing teleportTo: ${error.message}`);
}

console.log("\n✅ API testing completed!");
console.log("📝 Check the console output above to see what functions are available.");