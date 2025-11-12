// IMPORTANT: LSL doesn't support ternary operators, break statements or continue statements, 
// so don't use them in this script! We also can't use "key" or "event" as variable names


// Advanced Keyword-Based Inventory Sorter - Silent Version
// Sorts items by keywords and auto-deletes them after processing


// Configuration constants
float TRANSFER_DELAY = 0.5;    // Delay between folder transfers
integer BOX_CHANNEL = -987654321;  // Channel for box communication
integer DEBUG_MODE = FALSE;     // Silent mode - no debug messages
integer AUTO_DELETE = TRUE;     // Auto-delete items after processing


// Keyword and folder management
list SEARCH_TERMS = [];
list FOLDER_NAMES = [];
integer DEFAULT_KEYWORDS_ADDED = FALSE;


// Mode settings
integer SORT_MODE = 0;  // 0=regular, 1=shirt, 2=pants


// Dialog control variables
integer MENU_CHANNEL;
integer LISTEN_HANDLE = -1;
integer DIALOG_STATE = 0;  // 0=main menu, 1=keyword menu, 2=add keyword, 3=add folder, 4=remove, 5=add batch


// Item tracking
list ITEMS_TO_SORT = [];
integer PROCESSED_ITEMS = 0;
integer SORTED_ITEMS = 0;
string SORTED_ITEMS_DATA = "";  // Data structure workaround for LSL list limits


// Delivery variables
integer DELIVERY_MODE = 0;  // 0=folder mode, 1=box mode, 2=individual keyword folders mode
key CURRENT_BOX_ID = NULL_KEY;
string CURRENT_BOX_NAME = "";
list PENDING_BOX_ITEMS = [];
integer BOX_LISTEN_HANDLE = -1;
string TEMP_SEARCH_TERM = "";  // For two-step keyword addition


// Function to clean strings for better matching
string stripSpecialChars(string input) 
{
    // Convert to uppercase for case insensitivity
    input = llToUpper(input);
    
    // Define characters that should remain attached
    string alphanumeric = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    string cleaned = "";
    integer lastWasSpace = FALSE;
    
    // Process each character
    integer length = llStringLength(input);
    integer i;
    for (i = 0; i < length; i++) 
    {
        string char = llGetSubString(input, i, i);
        if (llSubStringIndex(alphanumeric, char) != -1)
        {
            cleaned += char;
            lastWasSpace = FALSE;
        }
        else
        {
            if (!lastWasSpace)
            {
                cleaned += " ";
                lastWasSpace = TRUE;
            }
        }
    }
    
    return llStringTrim(cleaned, STRING_TRIM);
}


// Update delivery mode in object name
updateModeName() 
{
    string objName = llGetObjectName();
    
    // Remove existing mode suffixes if present
    if (llGetSubString(objName, -11, -1) == "[Box Mode]") 
    {
        objName = llGetSubString(objName, 0, -13); // Remove suffix and space
    } 
    else if (llGetSubString(objName, -14, -1) == "[Folder Mode]") 
    {
        objName = llGetSubString(objName, 0, -16); // Remove suffix and space
    }
    else if (llGetSubString(objName, -28, -1) == "[Individual Keyword Folders]") 
    {
        objName = llGetSubString(objName, 0, -30); // Remove suffix and space
    }
    else if (llGetSubString(objName, -13, -1) == "[Shirt Mode]") 
    {
        objName = llGetSubString(objName, 0, -15); // Remove suffix and space
    }
    else if (llGetSubString(objName, -13, -1) == "[Pants Mode]") 
    {
        objName = llGetSubString(objName, 0, -15); // Remove suffix and space
    }
    
    // Add current mode suffix - first the sort mode
    string sortModeSuffix = "";
    if (SORT_MODE == 1) 
    {
        sortModeSuffix = "Shirt Mode";
    }
    else if (SORT_MODE == 2) 
    {
        sortModeSuffix = "Pants Mode";
    }
    
    // Then the delivery mode
    string deliveryModeSuffix = "";
    if (DELIVERY_MODE == 1) 
    {
        deliveryModeSuffix = "Box Mode";
    } 
    else if (DELIVERY_MODE == 2) 
    {
        deliveryModeSuffix = "Individual Keyword Folders";
    }
    else 
    {
        deliveryModeSuffix = "Folder Mode";
    }
    
    // Build the final name
    if (sortModeSuffix != "") 
    {
        objName += " [" + sortModeSuffix + " - " + deliveryModeSuffix + "]";
    } 
    else 
    {
        objName += " [" + deliveryModeSuffix + "]";
    }
    
    llSetObjectName(objName);
}


// Cycle through delivery modes
toggleDeliveryMode() 
{
    // Cycle through modes: 0 -> 1 -> 2 -> 0
    DELIVERY_MODE++;
    if (DELIVERY_MODE > 2) 
    {
        DELIVERY_MODE = 0;
    }
    
    updateModeName();
}


// Toggle between sort modes (regular, shirt, pants)
toggleSortMode() 
{
    // Cycle through modes: 0 -> 1 -> 2 -> 0
    SORT_MODE++;
    if (SORT_MODE > 2) 
    {
        SORT_MODE = 0;
    }
    
    // Reset keywords to match the new mode
    resetToDefaults();
    
    // Update object name to reflect mode
    updateModeName();
}


// Load delivery mode and sort mode from object name
loadDeliveryMode() 
{
    string objName = llGetObjectName();
    
    // Reset modes to defaults first
    DELIVERY_MODE = 0;
    SORT_MODE = 0;
    
    // Check for delivery modes
    if (llSubStringIndex(objName, "Box Mode") != -1) 
    {
        DELIVERY_MODE = 1;
    } 
    else if (llSubStringIndex(objName, "Individual Keyword Folders") != -1) 
    {
        DELIVERY_MODE = 2;
    }
    else 
    {
        DELIVERY_MODE = 0; // Folder mode
    }
    
    // Check for sort modes - convert to uppercase for case-insensitive matching
    string objNameUpper = llToUpper(objName);
    if (llSubStringIndex(objNameUpper, "SHIRT MODE") != -1) 
    {
        SORT_MODE = 1;
    }
    else if (llSubStringIndex(objNameUpper, "PANTS MODE") != -1) 
    {
        SORT_MODE = 2;
    }
    else 
    {
        SORT_MODE = 0; // Regular mode
    }
    
    // Update the object name to ensure consistency
    updateModeName();
}


// Reset to default keywords based on mode
resetToDefaults() 
{
    if (SORT_MODE == 1) 
    {
        // Shirt mode keywords
        SEARCH_TERMS = ["INTHIUM", "MUNEC", "PEACH"];
        FOLDER_NAMES = ["INTHIUM", "MUNEC", "PEACH"];
    }
    else if (SORT_MODE == 2) 
    {
        // Pants mode keywords
        SEARCH_TERMS = ["KUPRA", "MUNECA", "PEACH"];
        FOLDER_NAMES = ["KUPRA", "MUNECA", "PEACH"];
    }
    else 
    {
        // Regular mode - default keywords
        SEARCH_TERMS = ["KUPRA", "LEGACY", "REBORN", "PEACH", "MUNECA", "LARAX"];
        FOLDER_NAMES = ["KUPRA", "LEGACY", "REBORN", "PEACH", "MUNECA", "LARAX"];
    }
    saveKeywords();
}


// Save keywords to object description
saveKeywords()
{
    // Build data string for saving
    string data = "";
    integer i;
    for (i = 0; i < llGetListLength(SEARCH_TERMS); i++)
    {
        if (i > 0)
        {
            data += "|";
        }
        data += llList2String(SEARCH_TERMS, i) + "," + llList2String(FOLDER_NAMES, i);
    }


    // Preserve box queue information if present
    string desc = llGetObjectDesc();
    integer queueStart = llSubStringIndex(desc, "#BOX_QUEUE#");
    if (queueStart != -1)
    {
        string queueData = llGetSubString(desc, queueStart, -1);
        data += "|" + queueData;
    }


    // Check description length (LSL limit is 127-255 chars depending on version)
    integer dataLen = llStringLength(data);
    if (dataLen > 200)
    {
        llOwnerSay("WARNING: Description is " + (string)dataLen + " chars. May be truncated!");
        llOwnerSay("Consider using fewer or shorter keywords.");
    }


    llSetObjectDesc(data);
}


// Load keywords from object description
loadKeywords() 
{
    SEARCH_TERMS = [];
    FOLDER_NAMES = [];
    
    string desc = llGetObjectDesc();
    if (desc != "") 
    {
        list pairs = llParseString2List(desc, ["|"], []);
        
        integer i;
        for (i = 0; i < llGetListLength(pairs); i++) 
        {
            string pair = llList2String(pairs, i);
            
            // Skip box queue data and settings
            if (llSubStringIndex(pair, "#BOX_QUEUE#") != -1) 
            {
                /* Skip this pair */
            } 
            else 
            {
                list parts = llParseString2List(pair, [","], []);
                if (llGetListLength(parts) >= 2) 
                {
                    string search = llList2String(parts, 0);
                    string folder = llList2String(parts, 1);
                    
                    if (search != "" && folder != "") 
                    {
                        // FIX: Convert to uppercase for case-insensitive consistency
                        SEARCH_TERMS += [llToUpper(search)];
                        FOLDER_NAMES += [llToUpper(folder)];
                    }
                }
            }
        }
    }
    
    // Add defaults if empty
    if (llGetListLength(SEARCH_TERMS) == 0) 
    {
        resetToDefaults();
    }
}


// Add a keyword mapping
addKeywordMapping(string search_term, string folder_name) 
{
    search_term = llStringTrim(llToUpper(search_term), STRING_TRIM);
    folder_name = llStringTrim(llToUpper(folder_name), STRING_TRIM);
    
    // Check if search term already exists
    integer index = llListFindList(SEARCH_TERMS, [search_term]);
    if (index != -1) 
    {
        // Update existing mapping
        FOLDER_NAMES = llListReplaceList(FOLDER_NAMES, [folder_name], index, index);
    } 
    else 
    {
        // Add new mapping
        SEARCH_TERMS += [search_term];
        FOLDER_NAMES += [folder_name];
    }
    
    saveKeywords();
}


// Process batch keyword additions
addKeywordBatch(string input)
{
    list mappings = llParseString2List(input, [";"], []);
    integer i;
    integer added = 0;


    for (i = 0; i < llGetListLength(mappings); i++)
    {
        string mapping = llStringTrim(llList2String(mappings, i), STRING_TRIM);
        list parts = llParseString2List(mapping, [","], []);


        if (llGetListLength(parts) >= 2)
        {
            string search = llStringTrim(llList2String(parts, 0), STRING_TRIM);
            string folder = llStringTrim(llList2String(parts, 1), STRING_TRIM);


            if (search != "" && folder != "")
            {
                // Convert to uppercase for consistency
                search = llToUpper(search);
                folder = llToUpper(folder);


                // Check if search term already exists
                integer index = llListFindList(SEARCH_TERMS, [search]);
                if (index != -1)
                {
                    // Update existing mapping
                    FOLDER_NAMES = llListReplaceList(FOLDER_NAMES, [folder], index, index);
                }
                else
                {
                    // Add new mapping
                    SEARCH_TERMS += [search];
                    FOLDER_NAMES += [folder];
                }
                added++;
            }
        }
    }


    // Save once at the end instead of for each keyword
    if (added > 0)
    {
        saveKeywords();
        llOwnerSay("Added " + (string)added + " keyword mappings.");
    }
    else
    {
        llOwnerSay("No valid keyword mappings found.");
    }
}


// Delete a keyword mapping
deleteKeywordMapping(string keyword) 
{
    keyword = llStringTrim(llToUpper(keyword), STRING_TRIM);
    integer index = llListFindList(SEARCH_TERMS, [keyword]);
    
    if (index != -1) 
    {
        SEARCH_TERMS = llDeleteSubList(SEARCH_TERMS, index, index);
        FOLDER_NAMES = llDeleteSubList(FOLDER_NAMES, index, index);
        saveKeywords();
    }
}


// Wildcard matching function - supports *, *pattern, pattern*, and *pattern*
integer wildcardMatch(string pattern, string text) {
    pattern = llToUpper(pattern);
    text = llToUpper(text);
    if(pattern == "*" || pattern == "**") return TRUE;
    integer patlen = llStringLength(pattern);
    integer textlen = llStringLength(text);
    if(llGetSubString(pattern, 0, 0) == "*" && llGetSubString(pattern, -1, -1) == "*") {
        if (patlen <= 2) return TRUE;
        string val = llGetSubString(pattern, 1, -2);
        return llSubStringIndex(text, val) != -1;
    }
    if(llGetSubString(pattern, 0, 0) == "*") {
        string val = llGetSubString(pattern, 1, -1);
        integer vlen = llStringLength(val);
        return (vlen <= textlen) && (llGetSubString(text, textlen-vlen, -1) == val);
    }
    if(llGetSubString(pattern, -1, -1) == "*") {
        string val = llGetSubString(pattern, 0, -2);
        integer vlen = llStringLength(val);
        return (vlen <= textlen) && (llGetSubString(text, 0, vlen-1) == val);
    }
    // Default behaviour: plain keyword matches anywhere within the text
    return llSubStringIndex(text, pattern) != -1;
}

// Check if an item matches any search term and return the matching term
string matchesSearchTerm(string item_name) 
{
    string clean_name = stripSpecialChars(item_name);
    integer i;
    for (i = 0; i < llGetListLength(SEARCH_TERMS); i++) 
    {
        string pattern = llList2String(SEARCH_TERMS, i);
        if (wildcardMatch(pattern, clean_name)) 
        {
            return pattern;
        }
    }
    return "";  // No match found
}

// Get folder name for a matching search term
string getFolderName(string search_term) 
{
    integer index = llListFindList(SEARCH_TERMS, [search_term]);
    if (index != -1) 
    {
        return llList2String(FOLDER_NAMES, index);
    }
    
    // If not found, use the search term itself
    return search_term;
}


// Add an item to a folder in our data structure
addItemToFolder(string folder_name, string item_name) 
{
    // Store as a pair in the data string: folder_name|item_name|
    SORTED_ITEMS_DATA += folder_name + "|" + item_name + "|";
}


// Get all items for a specific folder
list getItemsForFolder(string folder_name) 
{
    list items = [];
    
    // Parse the data string
    list data_parts = llParseString2List(SORTED_ITEMS_DATA, ["|"], []);
    
    // In this format, each odd-indexed item is a folder name and each even-indexed item is an item name
    integer i;
    for (i = 0; i < llGetListLength(data_parts) - 1; i += 2) 
    {
        if (llList2String(data_parts, i) == folder_name) 
        {
            string item = llList2String(data_parts, i + 1);
            
            // Verify item still exists
            if (llGetInventoryType(item) != INVENTORY_NONE) 
            {
                items += [item];
            }
        }
    }
    
    return items;
}


// Setup box listener for box delivery mode
setupBoxListener() 
{
    // Remove existing listener if any
    if (BOX_LISTEN_HANDLE != -1) 
    {
        llListenRemove(BOX_LISTEN_HANDLE);
    }
    
    // Create new listener
    BOX_LISTEN_HANDLE = llListen(BOX_CHANNEL, "", NULL_KEY, "");
}


// Create a box for delivery
createDeliveryBox(string boxName, list items) 
{
    if (llGetListLength(items) == 0) 
    {
        return;
    }
    
    // Check for Storage Box object
    if (llGetInventoryType("Storage Box") == INVENTORY_OBJECT) 
    {
        // Store information for when box responds
        CURRENT_BOX_NAME = boxName;
        PENDING_BOX_ITEMS = items;
        
        // Setup listener if not already set
        setupBoxListener();
        
        // Rez the box object
        vector pos = llGetPos();
        vector offset = <1.0, 0.0, 0.5> * llGetRot();  // In front and slightly above
        
        llRezObject("Storage Box", pos + offset, ZERO_VECTOR, ZERO_ROTATION, BOX_CHANNEL);
        
        // Set timeout in case box doesn't respond
        llSetTimerEvent(5.0);
    } 
    else 
    {
        // Fall back to folder delivery
        llGiveInventoryList(llGetOwner(), boxName, items);
        
        // Delete items if auto-delete is enabled
        if (AUTO_DELETE) 
        {
            deleteProcessedItems(items);
        }
    }
}


// Transfer items to the rezzed box
transferItemsToBox(key boxID) 
{
    // Send items to box
    integer i;
    for (i = 0; i < llGetListLength(PENDING_BOX_ITEMS); i++) 
    {
        string item = llList2String(PENDING_BOX_ITEMS, i);
        llGiveInventory(boxID, item);
        llSleep(0.1);  // Small delay between transfers
    }
    
    // Tell box to deliver itself to owner and delete
    llWhisper(BOX_CHANNEL, "DELIVER_AND_DELETE|" + (string)boxID + "|" + (string)llGetOwner());
    
    // Delete items if auto-delete is enabled
    if (AUTO_DELETE) 
    {
        deleteProcessedItems(PENDING_BOX_ITEMS);
    }
    
    // Clear pending items
    PENDING_BOX_ITEMS = [];
    CURRENT_BOX_NAME = "";
    CURRENT_BOX_ID = NULL_KEY;
}


// Delete items after they've been processed
deleteProcessedItems(list items) 
{
    integer i;
    for (i = 0; i < llGetListLength(items); i++) 
    {
        string item = llList2String(items, i);
        
        // Check if item exists and has proper permissions
        if (llGetInventoryType(item) != INVENTORY_NONE) 
        {
            // Delete the item
            llRemoveInventory(item);
        }
    }
}


// Continue processing box queue
continueBoxQueue() 
{
    string desc = llGetObjectDesc();
    integer queueStart = llSubStringIndex(desc, "#BOX_QUEUE#");
    
    if (queueStart != -1) 
    {
        // Extract queue data
        string queueData = llGetSubString(desc, queueStart + 11, -1);
        list queueParts = llParseString2List(queueData, ["|"], []);
        
        if (llGetListLength(queueParts) >= 2) 
        {
            // Get next box data
            list folders = llParseString2List(llList2String(queueParts, 0), ["^"], []);
            list items = llParseString2List(llList2String(queueParts, 1), ["^"], []);
            
            if (llGetListLength(folders) > 0 && llGetListLength(items) > 0) 
            {
                string folder = llList2String(folders, 0);
                list boxItems = llParseString2List(llList2String(items, 0), [","], []);
                
                // Remove this entry from queue
                string baseDesc = llGetSubString(desc, 0, queueStart - 1);
                
                if (llGetListLength(folders) > 1) 
                {
                    // Update queue with remaining items
                    folders = llDeleteSubList(folders, 0, 0);
                    items = llDeleteSubList(items, 0, 0);
                    
                    llSetObjectDesc(baseDesc + "#BOX_QUEUE#" + 
                                   llDumpList2String(folders, "^") + "|" + 
                                   llDumpList2String(items, "^"));
                } 
                else 
                {
                    // No more items, remove queue
                    llSetObjectDesc(baseDesc);
                }
                
                // Process this box
                createDeliveryBox(folder, boxItems);
                return;
            }
        }
        
        // Invalid data, clear queue
        llSetObjectDesc(llGetSubString(desc, 0, queueStart - 1));
    }
}


// Scan inventory for items to sort
scanInventory() 
{
    // Reset tracking variables
    ITEMS_TO_SORT = [];
    PROCESSED_ITEMS = 0;
    SORTED_ITEMS = 0;
    SORTED_ITEMS_DATA = "";
    
    // Check all inventory types
    integer count = llGetInventoryNumber(INVENTORY_ALL);
    
    integer i;
    for (i = 0; i < count; i++) 
    {
        string item_name = llGetInventoryName(INVENTORY_ALL, i);
        integer item_type = llGetInventoryType(item_name);
        
        // Skip this script and the storage box
        if (item_name != llGetScriptName() && 
            item_name != "Storage Box" && 
            item_type != INVENTORY_SCRIPT && 
            item_type != INVENTORY_NOTECARD) 
        {
            
            ITEMS_TO_SORT += [item_name];
        }
    }
    
    if (llGetListLength(ITEMS_TO_SORT) > 0) 
    {
        processItems();
    }
}


// Process and categorize items
processItems() 
{
    // Create mapping between items and destination folders
    list destinations = [];
    list destination_items = [];
    list processed_items = []; // Track all items processed for deletion
    
    integer i;
    for (i = 0; i < llGetListLength(ITEMS_TO_SORT); i++) 
    {
        string item_name = llList2String(ITEMS_TO_SORT, i);
        
        // Check if item matches any search term
        string matching_term = matchesSearchTerm(item_name);
        
        if (matching_term != "") 
        {
            // Get folder name for this search term
            string folder_name = getFolderName(matching_term);
            
            // Check permissions
            integer perms = llGetInventoryPermMask(item_name, MASK_OWNER);
            if (perms & PERM_COPY) 
            {
                // Add to our data structure
                addItemToFolder(folder_name, item_name);
                
                // Add to processed items list for deletion
                processed_items += [item_name];
                
                // Track for proper delivery
                integer folder_index = llListFindList(destinations, [folder_name]);
                
                if (folder_index == -1) 
                {
                    // New folder destination
                    destinations += [folder_name];
                    destination_items += [item_name];
                } 
                else 
                {
                    // Add to existing folder contents
                    string existing_items = llList2String(destination_items, folder_index);
                    existing_items += "," + item_name;
                    destination_items = llListReplaceList(destination_items, [existing_items], folder_index, folder_index);
                }
                
                SORTED_ITEMS++;
            }
        }
        
        PROCESSED_ITEMS++;
    }
    
    // Deliver based on mode
    if (SORTED_ITEMS > 0) 
    {
        if (DELIVERY_MODE == 0) 
        {
            // Folder mode - create folders and deliver immediately
            deliverFolders(destinations, destination_items);
            
            // Delete items if auto-delete is enabled
            if (AUTO_DELETE) 
            {
                deleteProcessedItems(processed_items);
            }
        } 
        else if (DELIVERY_MODE == 1) 
        {
            // Box mode - queue and process one by one
            queueBoxes(destinations, destination_items);
            // Items will be deleted after box transfer
        }
        else if (DELIVERY_MODE == 2) 
        {
            // Individual keyword folders mode - deliver each folder separately
            deliverIndividualKeywordFolders();
            
            // Delete items if auto-delete is enabled
            if (AUTO_DELETE) 
            {
                deleteProcessedItems(processed_items);
            }
        }
    }
}


// Deliver matched items in individual folders by their keywords
deliverIndividualKeywordFolders() 
{
    // Process each unique folder in our data
    list processed_folders = [];
    list data_parts = llParseString2List(SORTED_ITEMS_DATA, ["|"], []);
    
    // First, collect all unique folder names
    integer i;
    for (i = 0; i < llGetListLength(data_parts) - 1; i += 2) 
    {
        string folder_name = llList2String(data_parts, i);
        
        if (llListFindList(processed_folders, [folder_name]) == -1) 
        {
            processed_folders += [folder_name];
        }
    }
    
    // Now deliver each folder individually
    integer folder_count = llGetListLength(processed_folders);
    
    for (i = 0; i < folder_count; i++) 
    {
        string folder_name = llList2String(processed_folders, i);
        
        // Direct inventory check - try to find the actual item in inventory
        list direct_items = [];
        integer inv_count = llGetInventoryNumber(INVENTORY_ALL);
        integer j;
        
        for (j = 0; j < inv_count; j++) 
        {
            string item_name = llGetInventoryName(INVENTORY_ALL, j);
            
            // Skip scripts and Storage Box
            if (item_name != llGetScriptName() && 
                item_name != "Storage Box" && 
                llGetInventoryType(item_name) != INVENTORY_SCRIPT && 
                llGetInventoryType(item_name) != INVENTORY_NOTECARD) 
            {
                
                // Check if this item matched this keyword/folder
                string matching_term = matchesSearchTerm(item_name);
                if (matching_term != "" && getFolderName(matching_term) == folder_name) 
                {
                    direct_items += [item_name];
                }
            }
        }
        
        // Try to deliver using direct matching
        if (llGetListLength(direct_items) > 0) 
        {
            // Deliver items to this folder
            llGiveInventoryList(llGetOwner(), folder_name, direct_items);
            llSleep(TRANSFER_DELAY);
        } 
        else 
        {
            // Fall back to the original method
            list folder_items = getItemsForFolder(folder_name);
            
            if (llGetListLength(folder_items) > 0) 
            {
                // Deliver items to this folder
                llGiveInventoryList(llGetOwner(), folder_name, folder_items);
                llSleep(TRANSFER_DELAY);
            }
        }
    }
}


// Deliver items in separate folders
deliverFolders(list destinations, list destination_items) 
{
    integer count = llGetListLength(destinations);
    integer i;
    
    for (i = 0; i < count; i++) 
    {
        string folder = llList2String(destinations, i);
        string items_str = llList2String(destination_items, i);
        list items = llParseString2List(items_str, [","], []);
        
        if (llGetListLength(items) > 0) 
        {
            llGiveInventoryList(llGetOwner(), folder, items);
            llSleep(TRANSFER_DELAY);
        }
    }
}


// Queue boxes for delivery
queueBoxes(list destinations, list destination_items) 
{
    if (llGetListLength(destinations) == 0) 
    {
        return;
    }
    
    // Create the first box
    string first_folder = llList2String(destinations, 0);
    string first_items_str = llList2String(destination_items, 0);
    list first_items = llParseString2List(first_items_str, [","], []);
    
    // If more than one box, save the queue
    if (llGetListLength(destinations) > 1) 
    {
        list remaining_folders = llDeleteSubList(destinations, 0, 0);
        list remaining_items = llDeleteSubList(destination_items, 0, 0);
        
        // Save to object description
        string queue_data = "#BOX_QUEUE#" + 
                           llDumpList2String(remaining_folders, "^") + "|" + 
                           llDumpList2String(remaining_items, "^");
        
        // Get existing keyword data
        string desc = llGetObjectDesc();
        integer queue_pos = llSubStringIndex(desc, "#BOX_QUEUE#");
        
        if (queue_pos != -1) 
        {
            // Replace existing queue
            desc = llGetSubString(desc, 0, queue_pos - 1);
        }
        
        // Add new queue
        llSetObjectDesc(desc + queue_data);
    }
    
    // Create the first box
    createDeliveryBox(first_folder, first_items);
}


// Toggle auto-delete functionality
toggleAutoDelete() 
{
    AUTO_DELETE = !AUTO_DELETE;
}


// Show main dialog menu
showMainMenu()
{
    // Explicitly set dialog state to main menu
    DIALOG_STATE = 0;


    // Generate a unique listen channel
    MENU_CHANNEL = (integer)(llFrand(1000000) + 1000000) * -1;


    // Remove any existing listener
    if (LISTEN_HANDLE != -1)
    {
        llListenRemove(LISTEN_HANDLE);
    }


    // Create new listener
    LISTEN_HANDLE = llListen(MENU_CHANNEL, "", llGetOwner(), "");


    // Format the auto-delete status without ternary operator
    string auto_delete_text;
    if (AUTO_DELETE)
    {
        auto_delete_text = "Auto-Delete ON";
    }
    else
    {
        auto_delete_text = "Auto-Delete OFF";
    }


    // Create menu buttons
    list buttons = ["Sort Items", "Toggle Delivery", "Toggle Mode", "Show Keywords",
                    "Add Keyword", "Add Batch", "Remove Keyword", "Reset Keywords",
                    auto_delete_text];


    // Show dialog with appropriate mode text
    string mode_text;
    if (DELIVERY_MODE == 0)
    {
        mode_text = "FOLDER";
    }
    else if (DELIVERY_MODE == 1)
    {
        mode_text = "BOX";
    }
    else
    {
        mode_text = "INDIVIDUAL KEYWORD FOLDERS";
    }


    string sort_mode_text;
    if (SORT_MODE == 0)
    {
        sort_mode_text = "REGULAR";
    }
    else if (SORT_MODE == 1)
    {
        sort_mode_text = "SHIRT";
    }
    else
    {
        sort_mode_text = "PANTS";
    }


    llDialog(llGetOwner(), "Inventory Sorter\n\nDelivery Mode: " + mode_text +
             "\nSort Mode: " + sort_mode_text +
             "\nAuto-Delete: " + auto_delete_text +
             "\n\nSelect an option:", buttons, MENU_CHANNEL);
}


// Show keywords menu
showKeywordMenu() 
{
    DIALOG_STATE = 1;
    
    list buttons = [];
    integer i;
    integer count = llGetListLength(SEARCH_TERMS);
    
    if (count == 0) 
    {
        showMainMenu();
        return;
    }
    
    // Add keywords as buttons (limit to 12)
    for (i = 0; i < count && i < 12; i++) 
    {
        buttons += [llList2String(SEARCH_TERMS, i)];
    }
    
    // Add navigation buttons if needed
    if (count > 12) 
    {
        buttons += ["Next Page", "Main Menu"];
    } 
    else 
    {
        buttons += ["Main Menu"];
    }
    
    // Show dialog
    llDialog(llGetOwner(), "Select a keyword to view its folder mapping:", buttons, MENU_CHANNEL);
}


// Show remove keyword menu
showRemoveKeywordMenu() 
{
    DIALOG_STATE = 4;
    
    list buttons = [];
    integer i;
    integer count = llGetListLength(SEARCH_TERMS);
    
    if (count == 0) 
    {
        showMainMenu();
        return;
    }
    
    // Add keywords as buttons (limit to 12)
    for (i = 0; i < count && i < 12; i++) 
    {
        buttons += [llList2String(SEARCH_TERMS, i)];
    }
    
    // Add navigation buttons if needed
    if (count > 12) 
    {
        buttons += ["Next Page", "Cancel"];
    } 
    else 
    {
        buttons += ["Cancel"];
    }
    
    // Show dialog
    llDialog(llGetOwner(), "Select a keyword to REMOVE:", buttons, MENU_CHANNEL);
}


// Handle dialog menu selections for main menu
handleMainMenu(string message)
{
    if (message == "Sort Items")
    {
        scanInventory();
        return;
    }


    if (message == "Toggle Delivery")
    {
        toggleDeliveryMode();
        showMainMenu();
        return;
    }


    if (message == "Toggle Mode")
    {
        toggleSortMode();
        showMainMenu();
        return;
    }


    if (message == "Show Keywords")
    {
        showKeywordMenu();
        return;
    }


    if (message == "Add Keyword")
    {
        DIALOG_STATE = 2;
        llTextBox(llGetOwner(), "Enter the keyword to search for:", MENU_CHANNEL);
        return;
    }


    if (message == "Add Batch")
    {
        DIALOG_STATE = 5;
        llTextBox(llGetOwner(), "Enter batch keyword mappings in format:\nkeyword1,folder1;keyword2,folder2;...", MENU_CHANNEL);
        return;
    }


    if (message == "Remove Keyword")
    {
        showRemoveKeywordMenu();
        return;
    }


    if (message == "Reset Keywords")
    {
        resetToDefaults();
        showMainMenu();
        return;
    }


    if (llSubStringIndex(message, "Auto-Delete") != -1)
    {
        toggleAutoDelete();
        showMainMenu();
        return;
    }


    // If no match found, show main menu again (defensive)
    showMainMenu();
}


// Handle dialog menu selections for keyword menu
handleKeywordMenu(string message)
{
    if (message == "Main Menu")
    {
        DIALOG_STATE = 0;
        showMainMenu();
        return;
    }
    
    if (message == "Next Page")
    {
        showKeywordMenu();
        return;
    }
    
    // Show mapping for selected keyword
    integer index = llListFindList(SEARCH_TERMS, [message]);
    if (index != -1)
    {
        llInstantMessage(llGetOwner(), "Keyword '" + message + "' maps to folder '" + 
                    llList2String(FOLDER_NAMES, index) + "'");
    }
    showKeywordMenu();
}


// Handle dialog menu selections for add keyword step 1
handleAddKeyword1(string message)
{
    if (message != "")
    {
        TEMP_SEARCH_TERM = llStringTrim(message, STRING_TRIM);
        DIALOG_STATE = 3;
        llTextBox(llGetOwner(), "Enter the folder name for keyword '" + TEMP_SEARCH_TERM + "':", MENU_CHANNEL);
        return;
    }
    
    DIALOG_STATE = 0;
    showMainMenu();
}


// Handle dialog menu selections for add keyword step 2
handleAddKeyword2(string message)
{
    if (message != "")
    {
        addKeywordMapping(TEMP_SEARCH_TERM, llStringTrim(message, STRING_TRIM));
        TEMP_SEARCH_TERM = "";
    }
    DIALOG_STATE = 0;
    showMainMenu();
}


// Handle dialog menu selections for remove keyword
handleRemoveKeyword(string message)
{
    if (message == "Cancel")
    {
        DIALOG_STATE = 0;
        showMainMenu();
        return;
    }
    
    if (message == "Next Page")
    {
        showRemoveKeywordMenu();
        return;
    }
    
    // Delete the selected keyword
    deleteKeywordMapping(message);
    DIALOG_STATE = 0;
    showMainMenu();
}


// Handle dialog menu selections for add batch
handleAddBatch(string message)
{
    if (message != "")
    {
        addKeywordBatch(message);
    }
    DIALOG_STATE = 0;
    showMainMenu();
}


default 
{
    state_entry() 
    {
        // Initialize with reasonable memory limit
        llSetMemoryLimit(llGetUsedMemory() + 16384);  // 16KB extra for operations
        
        // Load saved keywords and delivery mode
        loadKeywords();
        loadDeliveryMode();
        
        // FIX: Only reset keywords if none were loaded (prevents overwriting saved keywords)
        // The resetToDefaults() call was moved into loadKeywords() when the list is empty
    }
    
    on_rez(integer param) 
    {
        llResetScript();
    }
    
    touch_start(integer total_number) 
    {
        key toucher = llDetectedKey(0);
        
        if (toucher == llGetOwner()) 
        {
            showMainMenu();
        }
    }
    
    listen(integer channel, string name, key id, string message)
    {
        if (id != llGetOwner())
        {
            return;
        }


        // Check if it's the box response channel
        if (channel == BOX_CHANNEL)
        {
            // Format: BOX_READY|box_id|box_name
            list parts = llParseString2List(message, ["|"], []);


            if (llList2String(parts, 0) == "BOX_READY")
            {
                key boxID = (key)llList2String(parts, 1);


                // Verify box name matches expected
                string boxName = llList2String(parts, 2);
                if (boxName == CURRENT_BOX_NAME)
                {
                    CURRENT_BOX_ID = boxID;


                    // Cancel timeout
                    llSetTimerEvent(0.0);


                    // Transfer items to box
                    transferItemsToBox(boxID);
                }
            }
            return;
        }


        // Handle menu interactions based on current dialog state
        if (DIALOG_STATE == 0)        // Main menu
        {
            handleMainMenu(message);
        }
        else if (DIALOG_STATE == 1)   // Keyword menu
        {
            handleKeywordMenu(message);
        }
        else if (DIALOG_STATE == 2)   // Add keyword step 1
        {
            handleAddKeyword1(message);
        }
        else if (DIALOG_STATE == 3)   // Add keyword step 2
        {
            handleAddKeyword2(message);
        }
        else if (DIALOG_STATE == 4)   // Remove keyword
        {
            handleRemoveKeyword(message);
        }
        else if (DIALOG_STATE == 5)   // Add batch
        {
            handleAddBatch(message);
        }
        else
        {
            // Unknown state - reset to main menu
            llOwnerSay("Error: Unknown dialog state " + (string)DIALOG_STATE + ". Resetting to main menu.");
            showMainMenu();
        }
    }
    
    timer() 
    {
        // Stop timer
        llSetTimerEvent(0.0);
        
        // Check if we're waiting for box response
        if (CURRENT_BOX_NAME != "" && CURRENT_BOX_ID == NULL_KEY) 
        {
            // Deliver folder instead
            llGiveInventoryList(llGetOwner(), CURRENT_BOX_NAME, PENDING_BOX_ITEMS);
            
            // Delete items if auto-delete is enabled
            if (AUTO_DELETE) 
            {
                deleteProcessedItems(PENDING_BOX_ITEMS);
            }
            
            // Clear pending items
            PENDING_BOX_ITEMS = [];
            CURRENT_BOX_NAME = "";
            
            // Continue processing queue after a short delay
            llSetTimerEvent(2.0);
        } 
        else 
        {
            // Continue processing the box queue
            continueBoxQueue();
        }
    }
    
    changed(integer change) 
    {
        if (change & CHANGED_INVENTORY) 
        {
            // Auto-sort on inventory change if not in menu
            if (DIALOG_STATE == 0 && LISTEN_HANDLE == -1) 
            {
                // Wait a moment for inventory changes to complete
                llSleep(0.5);
                scanInventory();
            }
        }
    }
}
