/**
 * SmartBots Circle Walking and Teleportation Script (Corrected)
 * 
 * Description: Automates bot to walk in a smooth circle for 4 minutes at a specific location,
 * then teleport to another location, and finally return to the original position.
 * 
 * Locations:
 * - Starting/Circle location: Sinful/152/88/25
 * - Target location: Sinful/143/94/25
 * 
 * Author: Generated for Second Life SmartBots
 * Created: January 2025
 * Fixed: Continuous movement without constant starting/stopping
 */

// =============================================================================
// CONFIGURATION CONSTANTS
// =============================================================================

const STARTING_LOCATION = "Sinful/152/88/25";
const TARGET_LOCATION_1 = "Sinful/150/95/25";
const TARGET_LOCATION_2 = "Sinful/156/93/25";
const CIRCLE_DURATION = 4 * 60 * 1000; // 4 minutes in milliseconds
const CIRCLE_RADIUS = 3;         // 3 meter radius for circle
const SMOOTH_MOVEMENT_INTERVAL = 100; // 100ms for smooth movement
const LOG_INTERVAL = 30000;      // Log progress every 30 seconds

// =============================================================================
// LOGGING FUNCTIONS
// =============================================================================

function logStart() {
    console.log("=".repeat(60));
    console.log("    SmartBots Circle Walking Script Started (Corrected)");
    console.log("=".repeat(60));
    console.log(`🎯 Target circle duration: ${CIRCLE_DURATION/1000} seconds (${CIRCLE_DURATION/60000} minutes)`);
    console.log(`📍 Starting location: ${STARTING_LOCATION}`);
    console.log(`📍 Target location 1: ${TARGET_LOCATION_1}`);
    console.log(`📍 Target location 2: ${TARGET_LOCATION_2}`);
    console.log(`⏱️  Script started at: ${new Date().toLocaleTimeString()}`);
    console.log(`🔄 Smooth movement interval: ${SMOOTH_MOVEMENT_INTERVAL}ms`);
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
    console.log("   ✅ Completed 4-minute smooth circle walking");
    console.log("   ✅ Walked to first target location");
    console.log("   ✅ Walked to second target location");
    console.log("   ✅ Walked back to starting location");
    console.log(`⏰ Completed at: ${new Date().toLocaleTimeString()}`);
    console.log("🤖 Bot is now ready for next task.");
    console.log("=".repeat(60));
}

// =============================================================================
// SMOOTH MOVEMENT FUNCTIONS
// =============================================================================

function startSmoothMovement() {
    // Initialize smooth movement system
    if (typeof bot !== 'undefined' && bot.startSmoothMovement) {
        bot.startSmoothMovement();
        logSuccess("Smooth movement system initialized");
    } else {
        logError("Smooth movement system not available");
    }
}

function stopSmoothMovement() {
    // Stop smooth movement system
    if (typeof bot !== 'undefined' && bot.stopSmoothMovement) {
        bot.stopSmoothMovement();
        logSuccess("Smooth movement system stopped");
    }
}

function moveToLocation(location, speed = 1.0) {
    // Use smooth movement to location
    if (typeof bot !== 'undefined' && bot.moveTo) {
        bot.moveTo(location, speed);
        logProgress(`Moving to ${location} at speed ${speed}`);
        return true;
    } else {
        logError("Movement system not available");
        return false;
    }
}

function teleportToLocation(location) {
    // Instant teleport to location
    if (typeof bot !== 'undefined' && bot.teleport) {
        bot.teleport(location);
        logSuccess(`Teleported to ${location}`);
        return true;
    } else {
        logError("Teleport system not available");
        return false;
    }
}

// =============================================================================
// CIRCLE WALKING FUNCTIONS
// =============================================================================

function startCircleWalking() {
    logPhase(1, "Starting Smooth Circle Walking");
    
    // Initialize smooth movement
    startSmoothMovement();
    
    // Calculate circle parameters
    const centerX = 152;
    const centerY = 88;
    const radius = CIRCLE_RADIUS;
    const totalSteps = Math.floor(CIRCLE_DURATION / SMOOTH_MOVEMENT_INTERVAL);
    const angleStep = (2 * Math.PI) / totalSteps;
    
    let currentStep = 0;
    const startTime = Date.now();
    
    logProgress(`Starting circle walk: ${totalSteps} steps over ${CIRCLE_DURATION/1000} seconds`);
    
    const circleInterval = setInterval(() => {
        const elapsed = Date.now() - startTime;
        
        if (elapsed >= CIRCLE_DURATION) {
            clearInterval(circleInterval);
            stopSmoothMovement();
            logSuccess("Circle walking completed");
            return;
        }
        
        // Calculate current position on circle
        const angle = currentStep * angleStep;
        const x = centerX + radius * Math.cos(angle);
        const y = centerY + radius * Math.sin(angle);
        const currentLocation = `Sinful/${Math.round(x)}/${Math.round(y)}/25`;
        
        // Move to current circle position
        moveToLocation(currentLocation, 0.8); // Slower speed for smooth circle
        
        currentStep++;
        
        // Log progress every 30 seconds
        if (currentStep % 300 === 0) {
            const progress = Math.round((elapsed / CIRCLE_DURATION) * 100);
            logProgress(`Circle progress: ${progress}% (${Math.round(elapsed/1000)}s elapsed)`);
        }
    }, SMOOTH_MOVEMENT_INTERVAL);
    
    return circleInterval;
}

// =============================================================================
// MAIN SCRIPT EXECUTION
// =============================================================================

function executeScript() {
    logStart();
    
    // Phase 1: Circle Walking
    const circleInterval = startCircleWalking();
    
    // Wait for circle walking to complete
    setTimeout(() => {
        logPhase(2, "Moving to First Target Location");
        
        // Phase 2: Move to first target
        if (moveToLocation(TARGET_LOCATION_1, 1.0)) {
            setTimeout(() => {
                logPhase(3, "Moving to Second Target Location");
                
                // Phase 3: Move to second target
                if (moveToLocation(TARGET_LOCATION_2, 1.0)) {
                    setTimeout(() => {
                        logPhase(4, "Returning to Starting Location");
                        
                        // Phase 4: Return to starting location
                        if (moveToLocation(STARTING_LOCATION, 1.0)) {
                            setTimeout(() => {
                                logCompletion();
                                // Script completed successfully
                            }, 2000);
                        }
                    }, 3000);
                }
            }, 3000);
        }
    }, CIRCLE_DURATION + 1000);
}

// =============================================================================
// ERROR HANDLING AND SAFETY
// =============================================================================

function handleError(error) {
    logError(`Script error: ${error.message}`);
    stopSmoothMovement();
    
    // Emergency return to starting location
    setTimeout(() => {
        logProgress("Emergency return to starting location");
        teleportToLocation(STARTING_LOCATION);
    }, 1000);
}

// =============================================================================
// SCRIPT INITIALIZATION
// =============================================================================

// Add error handling
window.addEventListener('error', handleError);

// Start the script when ready
if (typeof bot !== 'undefined' && bot.isReady) {
    executeScript();
} else {
    // Wait for bot to be ready
    const checkReady = setInterval(() => {
        if (typeof bot !== 'undefined' && bot.isReady) {
            clearInterval(checkReady);
            executeScript();
        }
    }, 1000);
}

// Export for external use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        executeScript,
        startCircleWalking,
        moveToLocation,
        teleportToLocation,
        handleError
    };
}