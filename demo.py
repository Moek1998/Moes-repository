#!/usr/bin/env python3
"""
Flickr Auto-Like Program Demo
============================

This demo script shows how the Flickr Auto-Like program works
without requiring actual API credentials or dependencies.
"""

import time
import random
from datetime import datetime

# Simulate Flickr search results
SAMPLE_PHOTOS = [
    {
        'id': '53456789012',
        'title': 'Beautiful Muneca doll collection',
        'ownername': 'DollCollector123',
        'owner': '12345678@N01',
        'tags': 'muneca doll vintage collection',
        'dateupload': '1703764800'  # 2023-12-28
    },
    {
        'id': '53456789013',
        'title': 'Handmade Mexican Muneca',
        'ownername': 'CraftArtist',
        'owner': '23456789@N02',
        'tags': 'muneca mexican handmade traditional',
        'dateupload': '1703851200'  # 2023-12-29
    },
    {
        'id': '53456789014',
        'title': 'Vintage Muneca from grandmother',
        'ownername': 'VintageFinds',
        'owner': '34567890@N03',
        'tags': 'vintage muneca grandmother family',
        'dateupload': '1703937600'  # 2023-12-30
    },
    {
        'id': '53456789015',
        'title': 'Muneca repair workshop',
        'ownername': 'DollRepairShop',
        'owner': '45678901@N04',
        'tags': 'muneca repair workshop restoration',
        'dateupload': '1704024000'  # 2023-12-31
    },
    {
        'id': '53456789016',
        'title': 'Antique Muneca showcase',
        'ownername': 'AntiqueDealer',
        'owner': '56789012@N05',
        'tags': 'antique muneca showcase museum',
        'dateupload': '1704110400'  # 2024-01-01
    }
]

def print_header():
    """Print demo header"""
    print("🎭 Flickr Auto-Like Program Demo")
    print("=" * 50)
    print("This demo simulates the auto-like functionality")
    print("without connecting to actual Flickr API.\n")

def simulate_authentication():
    """Simulate OAuth authentication"""
    print("🔐 Authenticating with Flickr...")
    time.sleep(1)
    print("✅ Authentication successful!")
    print("📱 OAuth tokens saved for future use\n")

def simulate_search():
    """Simulate photo search"""
    print("🔍 Searching for photos with keyword: 'Muneca'")
    time.sleep(1)
    
    print(f"📸 Found {len(SAMPLE_PHOTOS)} photos:")
    for i, photo in enumerate(SAMPLE_PHOTOS, 1):
        print(f"  {i}. '{photo['title']}' by {photo['ownername']}")
    
    print()

def simulate_filtering():
    """Simulate photo filtering"""
    print("🔍 Filtering photos based on criteria...")
    time.sleep(0.5)
    
    # Simulate filtering
    filtered_photos = SAMPLE_PHOTOS[:]  # Keep all for demo
    
    print("✅ Applied filters:")
    print("  ▸ Skip own photos: enabled")
    print("  ▸ Skip already liked: enabled") 
    print("  ▸ Date range: all dates")
    print("  ▸ Required tags: none")
    print("  ▸ Excluded users: none")
    
    print(f"📊 {len(filtered_photos)} photos match filters\n")
    return filtered_photos

def simulate_liking(photos, dry_run=True):
    """Simulate liking photos"""
    max_likes = 3  # Limit for demo
    delay = 1  # Faster for demo
    
    mode = "DRY RUN" if dry_run else "LIVE"
    print(f"❤️  Starting auto-like process ({mode} mode)")
    print(f"⚙️  Max likes: {max_likes}, Delay: {delay}s between likes\n")
    
    liked_count = 0
    
    for photo in photos[:max_likes]:
        photo_id = photo['id']
        photo_title = photo['title']
        photo_owner = photo['ownername']
        
        print(f"📸 Processing: '{photo_title}' by {photo_owner}")
        print(f"   Photo ID: {photo_id}")
        
        # Simulate API call delay
        time.sleep(delay)
        
        # Simulate random success/failure for realism
        success = random.choice([True, True, True, False])  # 75% success rate
        
        if dry_run:
            print("   🧪 DRY RUN: Would like this photo")
            liked_count += 1
        elif success:
            print("   ✅ Successfully liked photo")
            liked_count += 1
        else:
            print("   ❌ Failed to like photo (already liked or API error)")
        
        print()
    
    return liked_count

def simulate_progress_tracking():
    """Simulate progress tracking"""
    print("📊 Progress tracking:")
    print("  ▸ Total photos found: 5")
    print("  ▸ Photos after filtering: 5")
    print("  ▸ Photos processed: 3")
    print("  ▸ Photos successfully liked: 3")
    print("  ▸ Skipped (already liked): 0")
    print("  ▸ API errors: 0\n")

def show_configuration():
    """Show sample configuration"""
    print("⚙️  Sample Configuration:")
    print("-" * 30)
    print("""[SEARCH]
keywords = Muneca
per_page = 100
max_pages = 10
sort = date-posted-desc

[BEHAVIOR]
max_likes_per_run = 50
delay_between_likes = 2
skip_own_photos = true
dry_run = true

[FILTERS]
min_upload_date = 
exclude_users = 
required_tags = """)
    print()

def show_log_sample():
    """Show sample log output"""
    print("📝 Sample Log Output:")
    print("-" * 30)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"""{current_time} - INFO - Starting Flickr Auto-Like Program
{current_time} - INFO - Authentication successful using stored tokens
{current_time} - INFO - Searching for photos with keywords: Muneca
{current_time} - INFO - Found 100 photos on page 1
{current_time} - INFO - Total photos found: 500
{current_time} - INFO - Filtered to 450 photos
{current_time} - INFO - Processing photo: 'Beautiful Muneca' by DollCollector
{current_time} - INFO - ✓ Successfully liked photo
{current_time} - INFO - Liked 50 photos
{current_time} - INFO - Flickr Auto-Like Program completed""")
    print()

def main():
    """Main demo function"""
    print_header()
    
    # Show configuration
    show_configuration()
    
    # Simulate the full workflow
    simulate_authentication()
    simulate_search()
    filtered_photos = simulate_filtering()
    liked_count = simulate_liking(filtered_photos, dry_run=True)
    
    # Show results
    print(f"🎉 Demo completed!")
    print(f"   Photos liked: {liked_count}")
    print(f"   Mode: DRY RUN (no actual API calls made)\n")
    
    # Show progress tracking
    simulate_progress_tracking()
    
    # Show log sample
    show_log_sample()
    
    print("🚀 To use the real program:")
    print("1. Get Flickr API credentials")
    print("2. Run: python setup.py")
    print("3. Edit config.ini with your credentials")
    print("4. Run: python flickr_auto_like.py")
    print("\n⚠️  Remember to test with dry_run=true first!")

if __name__ == "__main__":
    main()