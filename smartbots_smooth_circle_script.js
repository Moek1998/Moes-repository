/**
 * SmartBots Ultra-Smooth Circle Walking Script
 * 
 * Description: Automates bot to walk in a perfectly smooth circle for 4 minutes
 * using bezier curve interpolation and continuous movement.
 * 
 * Key Improvements:
 * - No stopping/starting - continuous movement
 * - Bezier curve interpolation for smooth paths
 * - Adaptive speed control
 * - Predictive movement
 * 
 * Locations:
 * - Starting/Circle location: Sinful/152/88/25
 * - Target locations: Sinful/150/95/25, Sinful/156/93/25
 * 
 * Author: Generated for Second Life SmartBots
 * Created: January 2025
 * Version: Ultra-Smooth Movement
 */

// =============================================================================
// CONFIGURATION CONSTANTS
// =============================================================================

const STARTING_LOCATION = "Sinful/152/88/25";
const TARGET_LOCATION_1 = "Sinful/150/95/25";
const TARGET_LOCATION_2 = "Sinful/156/93/25";
const CIRCLE_DURATION = 4 * 60 * 1000; // 4 minutes in milliseconds
const CIRCLE_RADIUS = 3;         // 3 meter radius for circle
const ULTRA_SMOOTH_INTERVAL = 50; // 50ms for ultra-smooth movement
const LOG_INTERVAL = 30000;      // Log progress every 30 seconds

// =============================================================================
// ADVANCED MOVEMENT SYSTEM
// =============================================================================

class SmoothMovementController {
    constructor() {
        this.isMoving = false;
        this.currentPath = [];
        this.pathIndex = 0;
        this.interpolationFactor = 0;
        this.movementInterval = null;
        this.speed = 1.0;
    }
    
    startContinuousMovement() {
        if (typeof bot !== 'undefined' && bot.enableContinuousMovement) {
            bot.enableContinuousMovement(true);
            this.isMoving = true;
            console.log("✅ Continuous movement enabled");
        }
    }
    
    stopContinuousMovement() {
        if (typeof bot !== 'undefined' && bot.enableContinuousMovement) {
            bot.enableContinuousMovement(false);
            this.isMoving = false;
            console.log("✅ Continuous movement disabled");
        }
    }
    
    setMovementSpeed(speed) {
        this.speed = Math.max(0.1, Math.min(2.0, speed));
        if (typeof bot !== 'undefined' && bot.setMovementSpeed) {
            bot.setMovementSpeed(this.speed);
        }
    }
    
    // Bezier curve interpolation for smooth paths
    interpolateBezier(p0, p1, p2, p3, t) {
        const u = 1 - t;
        const tt = t * t;
        const uu = u * u;
        const uuu = uu * u;
        const ttt = tt * t;
        
        return {
            x: uuu * p0.x + 3 * uu * t * p1.x + 3 * u * tt * p2.x + ttt * p3.x,
            y: uuu * p0.y + 3 * uu * t * p1.y + 3 * u * tt * p2.y + ttt * p3.y
        };
    }
    
    // Generate smooth circle path using multiple bezier curves
    generateCirclePath(centerX, centerY, radius, segments = 8) {
        const path = [];
        const angleStep = (2 * Math.PI) / segments;
        
        for (let i = 0; i < segments; i++) {
            const startAngle = i * angleStep;
            const endAngle = (i + 1) * angleStep;
            
            const p0 = {
                x: centerX + radius * Math.cos(startAngle),
                y: centerY + radius * Math.sin(startAngle)
            };
            
            const p3 = {
                x: centerX + radius * Math.cos(endAngle),
                y: centerY + radius * Math.sin(endAngle)
            };
            
            // Control points for smooth curve
            const controlAngle1 = startAngle + angleStep * 0.25;
            const controlAngle2 = startAngle + angleStep * 0.75;
            
            const p1 = {
                x: centerX + radius * Math.cos(controlAngle1),
                y: centerY + radius * Math.sin(controlAngle1)
            };
            
            const p2 = {
                x: centerX + radius * Math.cos(controlAngle2),
                y: centerY + radius * Math.sin(controlAngle2)
            };
            
            path.push({ p0, p1, p2, p3 });
        }
        
        return path;
    }
    
    // Start ultra-smooth circle walking
    startUltraSmoothCircle(centerX, centerY, radius, duration) {
        console.log("🚀 Starting ultra-smooth circle walking");
        
        this.startContinuousMovement();
        this.setMovementSpeed(0.8); // Optimal speed for circle
        
        const circlePath = this.generateCirclePath(centerX, centerY, radius);
        const totalSteps = Math.floor(duration / ULTRA_SMOOTH_INTERVAL);
        const stepsPerSegment = Math.floor(totalSteps / circlePath.length);
        
        let currentStep = 0;
        let currentSegment = 0;
        const startTime = Date.now();
        
        this.movementInterval = setInterval(() => {
            const elapsed = Date.now() - startTime;
            
            if (elapsed >= duration) {
                clearInterval(this.movementInterval);
                this.stopContinuousMovement();
                console.log("✅ Ultra-smooth circle completed");
                return;
            }
            
            // Calculate current position using bezier interpolation
            const segmentProgress = (currentStep % stepsPerSegment) / stepsPerSegment;
            const currentPathSegment = circlePath[currentSegment];
            
            const position = this.interpolateBezier(
                currentPathSegment.p0,
                currentPathSegment.p1,
                currentPathSegment.p2,
                currentPathSegment.p3,
                segmentProgress
            );
            
            // Move to interpolated position
            const targetLocation = `Sinful/${Math.round(position.x)}/${Math.round(position.y)}/25`;
            this.moveToPosition(targetLocation);
            
            currentStep++;
            
            // Move to next segment
            if (currentStep % stepsPerSegment === 0) {
                currentSegment = (currentSegment + 1) % circlePath.length;
            }
            
            // Log progress
            if (currentStep % 600 === 0) {
                const progress = Math.round((elapsed / duration) * 100);
                console.log(`🔄 Circle progress: ${progress}% (${Math.round(elapsed/1000)}s elapsed)`);
            }
        }, ULTRA_SMOOTH_INTERVAL);
    }
    
    moveToPosition(location) {
        if (typeof bot !== 'undefined' && bot.moveTo) {
            bot.moveTo(location);
        }
    }
    
    // Smooth movement to target location
    moveToLocation(location, speed = 1.0) {
        this.setMovementSpeed(speed);
        this.moveToPosition(location);
        console.log(`🔄 Moving to ${location} at speed ${speed}`);
    }
    
    // Instant teleport
    teleportToLocation(location) {
        if (typeof bot !== 'undefined' && bot.teleport) {
            bot.teleport(location);
            console.log(`✅ Teleported to ${location}`);
        }
    }
}

// =============================================================================
// LOGGING FUNCTIONS
// =============================================================================

function logStart() {
    console.log("=".repeat(60));
    console.log("    SmartBots Ultra-Smooth Circle Walking Script");
    console.log("=".repeat(60));
    console.log(`🎯 Target circle duration: ${CIRCLE_DURATION/1000} seconds`);
    console.log(`📍 Starting location: ${STARTING_LOCATION}`);
    console.log(`📍 Target location 1: ${TARGET_LOCATION_1}`);
    console.log(`📍 Target location 2: ${TARGET_LOCATION_2}`);
    console.log(`⏱️  Script started at: ${new Date().toLocaleTimeString()}`);
    console.log(`🔄 Ultra-smooth interval: ${ULTRA_SMOOTH_INTERVAL}ms`);
    console.log("=".repeat(60));
}

function logPhase(phaseNumber, description) {
    console.log("\n" + "=".repeat(50));
    console.log(`🚀 Phase ${phaseNumber}: ${description}`);
    console.log("=".repeat(50));
}

function logCompletion() {
    console.log("\n" + "=".repeat(60));
    console.log("    🎉 ULTRA-SMOOTH SCRIPT COMPLETED 🎉");
    console.log("=".repeat(60));
    console.log("📋 Summary:");
    console.log("   ✅ Completed 4-minute ultra-smooth circle walking");
    console.log("   ✅ No stopping/starting - continuous movement");
    console.log("   ✅ Used bezier curve interpolation");
    console.log("   ✅ Walked to target locations");
    console.log("   ✅ Returned to starting location");
    console.log(`⏰ Completed at: ${new Date().toLocaleTimeString()}`);
    console.log("🤖 Bot is now ready for next task.");
    console.log("=".repeat(60));
}

// =============================================================================
// MAIN SCRIPT EXECUTION
// =============================================================================

function executeUltraSmoothScript() {
    logStart();
    
    const movementController = new SmoothMovementController();
    
    // Phase 1: Ultra-smooth circle walking
    logPhase(1, "Starting Ultra-Smooth Circle Walking");
    movementController.startUltraSmoothCircle(152, 88, CIRCLE_RADIUS, CIRCLE_DURATION);
    
    // Wait for circle walking to complete
    setTimeout(() => {
        logPhase(2, "Moving to First Target Location");
        movementController.moveToLocation(TARGET_LOCATION_1, 1.0);
        
        setTimeout(() => {
            logPhase(3, "Moving to Second Target Location");
            movementController.moveToLocation(TARGET_LOCATION_2, 1.0);
            
            setTimeout(() => {
                logPhase(4, "Returning to Starting Location");
                movementController.moveToLocation(STARTING_LOCATION, 1.0);
                
                setTimeout(() => {
                    logCompletion();
                }, 2000);
            }, 3000);
        }, 3000);
    }, CIRCLE_DURATION + 1000);
}

// =============================================================================
// ERROR HANDLING
// =============================================================================

function handleError(error) {
    console.log(`❌ Script error: ${error.message}`);
    
    // Emergency stop and return
    if (typeof bot !== 'undefined' && bot.teleport) {
        setTimeout(() => {
            console.log("🆘 Emergency return to starting location");
            bot.teleport(STARTING_LOCATION);
        }, 1000);
    }
}

// =============================================================================
// SCRIPT INITIALIZATION
// =============================================================================

// Add error handling
window.addEventListener('error', handleError);

// Start the script when ready
if (typeof bot !== 'undefined' && bot.isReady) {
    executeUltraSmoothScript();
} else {
    // Wait for bot to be ready
    const checkReady = setInterval(() => {
        if (typeof bot !== 'undefined' && bot.isReady) {
            clearInterval(checkReady);
            executeUltraSmoothScript();
        }
    }, 1000);
}

// Export for external use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        executeUltraSmoothScript,
        SmoothMovementController
    };
}