/**
 * Simple SmartBots Circle Walking Script
 * 
 * This script should work in the SmartBots JavaScript playground.
 * It uses basic movement functions and simple timing.
 */

// Configuration
const STARTING_LOCATION = "Sinful/152/88/25";
const TARGET_LOCATION_1 = "Sinful/150/95/25";
const TARGET_LOCATION_2 = "Sinful/156/93/25";
const CIRCLE_DURATION = 4 * 60 * 1000; // 4 minutes
const MOVEMENT_INTERVAL = 3000; // 3 seconds

// Logging functions
function log(message) {
    console.log(`[${new Date().toLocaleTimeString()}] ${message}`);
}

// Main script
function main() {
    log("🚀 Starting SmartBots Circle Walking Script");
    log(`📍 Starting location: ${STARTING_LOCATION}`);
    log(`📍 Target 1: ${TARGET_LOCATION_1}`);
    log(`📍 Target 2: ${TARGET_LOCATION_2}`);
    
    // Phase 1: Circle walking
    log("🔄 Phase 1: Starting circle walking");
    startCircleWalking();
    
    // Phase 2: Move to targets after circle completes
    setTimeout(() => {
        log("🔄 Phase 2: Moving to first target");
        moveToLocation(TARGET_LOCATION_1);
        
        setTimeout(() => {
            log("🔄 Phase 3: Moving to second target");
            moveToLocation(TARGET_LOCATION_2);
            
            setTimeout(() => {
                log("🔄 Phase 4: Returning to start");
                moveToLocation(STARTING_LOCATION);
                
                setTimeout(() => {
                    log("✅ Script completed successfully!");
                }, 2000);
            }, 3000);
        }, 3000);
    }, CIRCLE_DURATION + 1000);
}

// Circle walking function
function startCircleWalking() {
    const centerX = 152;
    const centerY = 88;
    const radius = 3;
    const totalSteps = Math.floor(CIRCLE_DURATION / MOVEMENT_INTERVAL);
    const angleStep = (2 * Math.PI) / totalSteps;
    
    let currentStep = 0;
    const startTime = Date.now();
    
    log(`🔄 Starting circle: ${totalSteps} steps over ${CIRCLE_DURATION/1000} seconds`);
    
    const interval = setInterval(() => {
        const elapsed = Date.now() - startTime;
        
        if (elapsed >= CIRCLE_DURATION) {
            clearInterval(interval);
            log("✅ Circle walking completed");
            return;
        }
        
        // Calculate circle position
        const angle = currentStep * angleStep;
        const x = centerX + radius * Math.cos(angle);
        const y = centerY + radius * Math.sin(angle);
        const location = `Sinful/${Math.round(x)}/${Math.round(y)}/25`;
        
        // Move to position
        moveToLocation(location);
        
        currentStep++;
        
        // Log progress
        if (currentStep % 20 === 0) {
            const progress = Math.round((elapsed / CIRCLE_DURATION) * 100);
            log(`🔄 Circle progress: ${progress}%`);
        }
    }, MOVEMENT_INTERVAL);
}

// Movement function
function moveToLocation(location) {
    try {
        // Try different SmartBots API methods
        if (typeof walkTo === 'function') {
            walkTo(location);
            log(`🚶 Walking to ${location}`);
        } else if (typeof bot !== 'undefined' && bot.walkTo) {
            bot.walkTo(location);
            log(`🚶 Walking to ${location}`);
        } else if (typeof teleportTo === 'function') {
            teleportTo(location);
            log(`⚡ Teleported to ${location}`);
        } else if (typeof bot !== 'undefined' && bot.teleport) {
            bot.teleport(location);
            log(`⚡ Teleported to ${location}`);
        } else {
            log(`❌ No movement function available for ${location}`);
        }
    } catch (error) {
        log(`❌ Error moving to ${location}: ${error.message}`);
    }
}

// Start the script
log("🚀 Initializing script...");
main();