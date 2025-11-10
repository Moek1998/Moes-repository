# Mr Clicky UUID Mismatch Issue - RESOLVED in v1.6

## Problem (Historical)
The DFS Plants B bot was failing all Mr Clicky touch operations with the error:
```
[MR_CLICKY] Touch X reported failure: impossible to locate object by UUID
```

## Root Cause
There was a **version mismatch** between the script deployed on SmartBots and the script in this repository.

### UUIDs in Currently Deployed Script (Legacy Set)
The bot logs showed it was attempting to touch these UUIDs:
- `7a0a683d-0aa6-65ed-2ae5-08b7313e6893`
- `d73d9a20-16e0-4122-3c35-7591ccadead2`
- `172769ad-d243-004a-13aa-49256799eaac`
- `2690ae28-187a-5fdb-9a59-72d365f50dc1` (appears in both sets)

### UUIDs in Repository v1.5 (Updated Set)
The v1.5 version contained:
- `3491d5a7-1933-ea06-8d59-ba5788ef63b2`
- `b57c3091-3e9c-2351-0042-ae8feeaa2bb6`
- `715f2238-b3a3-bf04-60a8-fdc94838beec`
- `2690ae28-187a-5fdb-9a59-72d365f50dc1`

### UUIDs in Repository v1.6 (Merged Set - CURRENT)
The v1.6 version now contains ALL 7 UUIDs:
- `3491d5a7-1933-ea06-8d59-ba5788ef63b2` (updated set)
- `b57c3091-3e9c-2351-0042-ae8feeaa2bb6` (updated set)
- `715f2238-b3a3-bf04-60a8-fdc94838beec` (updated set)
- `2690ae28-187a-5fdb-9a59-72d365f50dc1` (both sets)
- `7a0a683d-0aa6-65ed-2ae5-08b7313e6893` (legacy set)
- `d73d9a20-16e0-4122-3c35-7591ccadead2` (legacy set)
- `172769ad-d243-004a-13aa-49256799eaac` (legacy set)

## Why "impossible to locate object by UUID"?
This error means the Mr Clicky objects with these UUIDs either:
1. Don't exist in Second Life at the specified location
2. Have been removed or moved to a different region
3. Are too far from the bot's location
4. The bot doesn't have permission to interact with them

## Solutions

### Option 0: Deploy DFS Plants B v1.6 (Recommended)
1. Copy the entire contents of `smartbots/docs/Bot_Playground/DFS Plants B` (v1.6)
2. Go to SmartBots Bot Playground for "DFS_Bot_B"
3. Replace the script with the updated version
4. Save and restart the bot
5. Monitor the logs to confirm touches succeed with the merged UUID pool

### Option 1: Redeploy the Latest Script (v1.6)
If you were running an older version locally, simply redeploying the v1.6 script resolves the mismatch automatically.

### Option 2: Verify Mr Clicky Objects In-World
If v1.6 still reports "impossible to locate" errors for all 7 UUIDs, verify the actual UUIDs in Second Life:

1. Teleport to one of the plant locations (e.g., `Sugarland/221/85/3080`)
2. Look for Mr Clicky objects near the plants
3. Right-click each Mr Clicky object → Edit → Object tab
4. Copy the UUID from the object properties
5. Update the `MR_CLICKY_UUIDS` array with the correct UUIDs

### Option 3: Obtain Mr Clicky Objects
If there are NO Mr Clicky objects in-world at all:
- Contact the DFS system provider to obtain and rez Mr Clicky objects
- Get the proper UUIDs once rezzed
- Update the script with those UUIDs

## How the Mr Clicky System Works
The Mr Clicky sequence requires the bot to:
1. Sit on the plant
2. Touch 3 different Mr Clicky objects in sequence (cycling through the UUID array)
3. Reply to dialog boxes from each Mr Clicky object
4. Stand up to complete the operation

The script cycles through available Mr Clicky UUIDs using a rotating index:
```javascript
var mrClickyIndex = farmSession.mrClickyUuidIndex % MR_CLICKY_UUIDS.length;
var mrClickyUuid = MR_CLICKY_UUIDS[mrClickyIndex];
farmSession.mrClickyUuidIndex = (farmSession.mrClickyUuidIndex + 1) % MR_CLICKY_UUIDS.length;
```

This means each touch advances the pointer so the bot methodically cycles through the entire UUID pool, even during rescue attempts. Over multiple plants the bot will touch every known Mr Clicky object.

## Next Steps
1. **Immediate**: Confirm whether Mr Clicky objects exist at the plant locations
2. **If they exist**: Get their correct UUIDs and update the script
3. **If they don't exist**: Obtain and rez Mr Clicky objects, then get their UUIDs
4. **After fixing**: Redeploy the script to SmartBots

## Technical Details
- **Git Commit**: `3e20354` shows when UUIDs were last updated
- **Commit Message**: "Replace the MR_CLICKY_UUIDS array in DFS Plants B script with the correct four UUIDs currently in use in-world"
- **Date**: The UUIDs were updated but the deployed script was never updated

## Testing After Fix
Once UUIDs are corrected and script is redeployed, you should see:
```
[MR_CLICKY] ========== Touch 1 of 3 ==========
[MR_CLICKY] Full UUID: [correct-uuid]
[MR_CLICKY] ✓ Touch command sent for step 1 (total touches: 1)
[MR_CLICKY] Touch 1 promise resolved successfully
```

Instead of:
```
[MR_CLICKY] Touch 1 reported failure: impossible to locate object by UUID
```
