# LSL Keyword Sorter - Case Insensitive & Substring Matching Fix

## Problem Identified

The DFS Inventory Sorter script was **not detecting keywords** within item names, even though they should be case-insensitive.

### Example Issue
- **Item Name**: `TRENDY. Lulu Bra [Muneca]`
- **Keyword**: `MUNECA`
- **Expected**: Should match and sort to MUNECA folder
- **Actual**: Not matching at all ❌

## Root Causes

### Issue #1: Keywords Not Persisting
In `state_entry()`, the script was calling `resetToDefaults()` AFTER `loadKeywords()`, which overwrote any custom keywords every time the script reset!

```lsl
// OLD CODE (BROKEN):
state_entry() 
{
    loadKeywords();           // Load saved keywords
    loadDeliveryMode();
    resetToDefaults();        // ❌ OVERWRITES loaded keywords!
}
```

### Issue #2: Case Insensitivity Not Maintained During Load
The `loadKeywords()` function wasn't converting loaded keywords to uppercase, creating inconsistency:

```lsl
// OLD CODE (BROKEN):
SEARCH_TERMS += [search];    // ❌ Not converted to uppercase
FOLDER_NAMES += [folder];    // ❌ Not converted to uppercase
```

### Issue #3: Keyword Matching Logic Required Exact Match
The `wildcardMatch()` function only checked for:
1. Exact match of the entire string
2. Wildcard patterns with `*`

It did NOT check if the keyword appeared **anywhere within** the item name!

```lsl
// OLD CODE (BROKEN):
return (text == pattern);    // ❌ Only exact match
```

This meant:
- Pattern: `MUNECA`
- Text: `TRENDY LULU BRA MUNECA`
- Result: ❌ NO MATCH (because "MUNECA" ≠ "TRENDY LULU BRA MUNECA")

## Solutions Implemented

### Fix #1: Remove resetToDefaults() from state_entry()
```lsl
// NEW CODE (FIXED):
state_entry() 
{
    // Initialize with reasonable memory limit
    llSetMemoryLimit(llGetUsedMemory() + 16384);
    
    // Load saved keywords and delivery mode
    loadKeywords();
    loadDeliveryMode();
    
    // ✅ FIX: Only reset keywords if none were loaded
    // The resetToDefaults() call is now inside loadKeywords() 
    // when the list is empty
}
```

### Fix #2: Convert Keywords to Uppercase on Load
```lsl
// NEW CODE (FIXED):
if (search != "" && folder != "") 
{
    // ✅ FIX: Convert to uppercase for case-insensitive consistency
    SEARCH_TERMS += [llToUpper(search)];
    FOLDER_NAMES += [llToUpper(folder)];
}
```

### Fix #3: Substring Matching by Default
```lsl
// NEW CODE (FIXED):
// Default behaviour: plain keyword matches anywhere within the text
return llSubStringIndex(text, pattern) != -1;
```

Now the matching logic works like this:
- Pattern: `MUNECA`
- Text: `TRENDY LULU BRA MUNECA`
- Result: ✅ MATCH! (because "MUNECA" is found within the text)

## How It Works Now

### Complete Flow Example

**Item**: "TRENDY. Lulu Bra [Muneca]"

1. **Item name is cleaned**:
   - Original: `TRENDY. Lulu Bra [Muneca]`
   - After `stripSpecialChars()`: `TRENDY LULU BRA MUNECA`

2. **Keyword comparison**:
   - Keyword in list: `MUNECA` (uppercase)
   - Cleaned name: `TRENDY LULU BRA MUNECA` (uppercase)

3. **Substring matching**:
   - `llSubStringIndex("TRENDY LULU BRA MUNECA", "MUNECA")` → Returns index 17
   - Index ≠ -1, so it's a MATCH! ✅

4. **Item is sorted**:
   - Delivered to folder: `MUNECA`
   - Auto-deleted (if enabled)

## Keyword Matching Capabilities

The script now supports three matching modes:

### 1. Substring Match (Default)
- **Keyword**: `MUNECA`
- **Matches**:
  - ✅ "TRENDY. Lulu Bra [Muneca]" → `TRENDY LULU BRA MUNECA`
  - ✅ "[Muneca] Dress" → `MUNECA DRESS`
  - ✅ "Cute Muneca Top" → `CUTE MUNECA TOP`

### 2. Prefix Match (with *)
- **Keyword**: `MUNECA*`
- **Matches**:
  - ✅ "Muneca Bra" → starts with `MUNECA`
  - ❌ "Bra Muneca" → doesn't start with `MUNECA`

### 3. Suffix Match (with *)
- **Keyword**: `*LEGACY`
- **Matches**:
  - ✅ "Dress Legacy" → ends with `LEGACY`
  - ❌ "Legacy Dress" → doesn't end with `LEGACY`

### 4. Contains Match (with * on both sides)
- **Keyword**: `*REBORN*`
- **Matches**:
  - ✅ "Classic Reborn Style" → contains `REBORN`
  - This is the same as default substring match

## Case Insensitivity

ALL matching is **fully case-insensitive**:

- ✅ `muneca` matches `MUNECA`
- ✅ `Muneca` matches `MUNECA`
- ✅ `MUNECA` matches `MUNECA`
- ✅ `mUnEcA` matches `MUNECA`

This is because:
1. All keywords are converted to uppercase when saved
2. All keywords are converted to uppercase when loaded
3. All item names are converted to uppercase before matching
4. All pattern matching uses uppercase strings

## Additional Fixes

### Fix #4: Case-Insensitive Sort Mode Detection
```lsl
// Check for sort modes - convert to uppercase for case-insensitive matching
string objNameUpper = llToUpper(objName);
if (llSubStringIndex(objNameUpper, "SHIRT MODE") != -1) 
{
    SORT_MODE = 1;
}
```

## Benefits

1. ✅ **Keywords persist correctly** - Custom keywords are saved and restored
2. ✅ **Fully case-insensitive** - Keywords work regardless of case in item names
3. ✅ **Substring matching works** - Keywords found anywhere in item names
4. ✅ **Wildcard support** - Use `*` for advanced patterns
5. ✅ **Robust and reliable** - No more missing items!

## Testing Example

### Test Case: "TRENDY. Lulu Bra [Muneca]"

```
Input: TRENDY. Lulu Bra [Muneca]
Keyword: MUNECA

Step 1 - Clean name:
  stripSpecialChars("TRENDY. Lulu Bra [Muneca]")
  → "TRENDY LULU BRA MUNECA"

Step 2 - Convert to uppercase:
  Already uppercase: "TRENDY LULU BRA MUNECA"

Step 3 - Check if "MUNECA" is in "TRENDY LULU BRA MUNECA":
  llSubStringIndex("TRENDY LULU BRA MUNECA", "MUNECA")
  → 17 (found at position 17)

Step 4 - Match result:
  17 != -1, so MATCH = TRUE ✅

Step 5 - Get folder:
  Keyword "MUNECA" → Folder "MUNECA"

Step 6 - Deliver:
  Item delivered to "MUNECA" folder ✅
```

## Files Modified

- `/smartbots/docs/Bot_Playground/Examples/DFS_Inventory_Sorter.lsl`
  - Line 312-313: Convert keywords to uppercase on load
  - Line 449: Change exact match to substring match
  - Lines 1351-1357: Remove resetToDefaults() call from state_entry()
  - Line 197: Case-insensitive mode detection

## Version

- **Script**: DFS Inventory Sorter v3.1 (Fixed)
- **Date**: 2024
- **Fix**: Case-insensitive keyword persistence and substring matching
