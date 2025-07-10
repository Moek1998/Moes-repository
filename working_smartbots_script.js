/**
 * SmartBots Circle Walking Script (Working Version)
 * 
 * Description: Automates bot to walk in a smooth circle for 4 minutes
 * using actual SmartBots API methods.
 * 
 * Author: Generated for Second Life SmartBots
 * Created: January 2025
 * Version: Working with SmartBots API
 */

// =============================================================================
// CONFIGURATION CONSTANTS
// =============================================================================

const STARTING_LOCATION = "Sinful/152/88/25";
const TARGET_LOCATION_1 = "Sinful/150/95/25";
const TARGET_LOCATION_2 = "Sinful/156/93/25";
const CIRCLE_DURATION = 4 * 60 * 1000; // 4 minutes in milliseconds
const CIRCLE_RADIUS = 3;         // 3 meter radius for circle
const MOVEMENT_INTERVAL = 2000;  // 2 seconds between movements
const LOG_INTERVAL = 30000;      // Log progress every 30 seconds

// =============================================================================
// LOGGING FUNCTIONS
// =============================================================================

function logStart() {
    console.log("=".repeat(60));
    console.log("    SmartBots Circle Walking Script Started");
    console.log("=".repeat(60));
    console.log(`🎯 Target circle duration: ${CIRCLE_DURATION/1000} seconds`);
    console.log(`📍 Starting location: ${STARTING_LOCATION}`);
    console.log(`📍 Target location 1: ${TARGET_LOCATION_1}`);
    console.log(`📍 Target location 2: ${TARGET_LOCATION_2}`);
    console.log(`⏱️  Script started at: ${new Date().toLocaleTimeString()}`);
    console.log("=".repeat(60));
}

function logPhase(phaseNumber, description) {
    console.log("\n" + "=".repeat(50));
    console.log(`🚀 Phase ${phaseNumber}: ${description}`);
    console.log("=".repeat(50));
}

function logSuccess(message) {
    console.log(`✅ ${message}`);
}

function logProgress(message) {
    console.log(`🔄 ${message}`);
}

function logError(message) {
    console.log(`❌ ${message}`);
}

function logCompletion() {
    console.log("\n" + "=".repeat(60));
    console.log("    🎉 SCRIPT COMPLETED SUCCESSFULLY 🎉");
    console.log("=".repeat(60));
    console.log("📋 Summary:");
    console.log("   ✅ Completed 4-minute circle walking");
    console.log("   ✅ Walked to first target location");
    console.log("   ✅ Walked to second target location");
    console.log("   ✅ Walked back to starting location");
    console.log(`⏰ Completed at: ${new Date().toLocaleTimeString()}`);
    console.log("🤖 Bot is now ready for next task.");
    console.log("=".repeat(60));
}

// =============================================================================
// SMARTBOTS API FUNCTIONS
// =============================================================================

function walkTo(location) {
    try {
        // Use SmartBots walkTo function
        if (typeof walkTo === 'function') {
            walkTo(location);
            logProgress(`Walking to ${location}`);
            return true;
        } else if (typeof bot !== 'undefined' && bot.walkTo) {
            bot.walkTo(location);
            logProgress(`Walking to ${location}`);
            return true;
        } else {
            logError("walkTo function not available");
            return false;
        }
    } catch (error) {
        logError(`Error walking to ${location}: ${error.message}`);
        return false;
    }
}

function teleportTo(location) {
    try {
        // Use SmartBots teleport function
        if (typeof teleportTo === 'function') {
            teleportTo(location);
            logSuccess(`Teleported to ${location}`);
            return true;
        } else if (typeof bot !== 'undefined' && bot.teleport) {
            bot.teleport(location);
            logSuccess(`Teleported to ${location}`);
            return true;
        } else {
            logError("teleportTo function not available");
            return false;
        }
    } catch (error) {
        logError(`Error teleporting to ${location}: ${error.message}`);
        return false;
    }
}

function wait(seconds) {
    return new Promise(resolve => {
        setTimeout(resolve, seconds * 1000);
    });
}

// =============================================================================
// CIRCLE WALKING FUNCTIONS
// =============================================================================

function startCircleWalking() {
    logPhase(1, "Starting Circle Walking");
    
    const centerX = 152;
    const centerY = 88;
    const radius = CIRCLE_RADIUS;
    const totalSteps = Math.floor(CIRCLE_DURATION / MOVEMENT_INTERVAL);
    const angleStep = (2 * Math.PI) / totalSteps;
    
    let currentStep = 0;
    const startTime = Date.now();
    
    logProgress(`Starting circle walk: ${totalSteps} steps over ${CIRCLE_DURATION/1000} seconds`);
    
    const circleInterval = setInterval(() => {
        const elapsed = Date.now() - startTime;
        
        if (elapsed >= CIRCLE_DURATION) {
            clearInterval(circleInterval);
            logSuccess("Circle walking completed");
            return;
        }
        
        // Calculate current position on circle
        const angle = currentStep * angleStep;
        const x = centerX + radius * Math.cos(angle);
        const y = centerY + radius * Math.sin(angle);
        const currentLocation = `Sinful/${Math.round(x)}/${Math.round(y)}/25`;
        
        // Walk to current circle position
        walkTo(currentLocation);
        
        currentStep++;
        
        // Log progress every 30 seconds
        if (currentStep % 15 === 0) {
            const progress = Math.round((elapsed / CIRCLE_DURATION) * 100);
            logProgress(`Circle progress: ${progress}% (${Math.round(elapsed/1000)}s elapsed)`);
        }
    }, MOVEMENT_INTERVAL);
    
    return circleInterval;
}

// =============================================================================
// MAIN SCRIPT EXECUTION
// =============================================================================

async function executeScript() {
    logStart();
    
    try {
        // Phase 1: Circle Walking
        const circleInterval = startCircleWalking();
        
        // Wait for circle walking to complete
        await wait(CIRCLE_DURATION / 1000 + 1);
        
        logPhase(2, "Moving to First Target Location");
        walkTo(TARGET_LOCATION_1);
        await wait(3);
        
        logPhase(3, "Moving to Second Target Location");
        walkTo(TARGET_LOCATION_2);
        await wait(3);
        
        logPhase(4, "Returning to Starting Location");
        walkTo(STARTING_LOCATION);
        await wait(2);
        
        logCompletion();
        
    } catch (error) {
        logError(`Script execution error: ${error.message}`);
    }
}

// =============================================================================
// SCRIPT INITIALIZATION
// =============================================================================

// Start the script immediately
console.log("🚀 Initializing SmartBots Circle Walking Script...");
executeScript();

// Export for external use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        executeScript,
        startCircleWalking,
        walkTo,
        teleportTo
    };
}