# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### 1. See the Demo
```bash
python3 demo.py
```
This shows you exactly how the program works without needing any setup.

### 2. Get Flickr API Keys
1. Go to https://www.flickr.com/services/api/keys/
2. Click "Request an API Key" → "Apply for a Non-Commercial Key"
3. Save your API Key and API Secret

### 3. Setup
```bash
python3 setup.py
```
This installs dependencies and creates a config file.

### 4. Configure
Edit `config.ini` and add your API credentials:
```ini
[FLICKR]
api_key = your_api_key_here
api_secret = your_api_secret_here
```

### 5. First Run (Test Mode)
```bash
python3 flickr_auto_like.py
```
- Follow the OAuth authentication prompts
- Program runs in dry-run mode by default (safe!)

### 6. Go Live
Edit `config.ini` and change:
```ini
dry_run = false
```

## 🛠️ Quick Commands

```bash
# Run the demo
python3 demo.py

# Setup everything
python3 setup.py

# Run the program
python3 flickr_auto_like.py

# CLI helper (optional)
python3 run_flickr_auto_like.py --help
```

## ⚙️ Quick Configuration

The most important settings in `config.ini`:

```ini
[SEARCH]
keywords = Muneca              # What to search for

[BEHAVIOR]
max_likes_per_run = 50         # How many to like per run
delay_between_likes = 2        # Seconds between likes
dry_run = true                 # Set to false when ready!

[FILTERS]
exclude_users = user1,user2    # Skip these users
min_upload_date = 2023-01-01   # Only newer photos
```

## 🔄 Automation

To run automatically (Linux/Mac):
```bash
# Add to crontab for daily runs at 2 PM
0 14 * * * cd /path/to/flickr-program && python3 flickr_auto_like.py
```

## ⚠️ Important Notes

- **Always test with `dry_run = true` first!**
- The program tracks liked photos to avoid duplicates
- Rate limiting is built-in (2-second delays by default)
- Check `flickr_auto_like.log` for detailed information
- Be respectful - don't spam likes!

## 🆘 Quick Troubleshooting

**"No photos found"**: Check your keywords and privacy_filter settings
**"Authentication failed"**: Verify your API keys are correct
**"API errors"**: Increase the delay_between_likes setting

## 📁 Files Created

- `config.ini` - Your settings
- `flickr_auto_like.log` - Program log
- `liked_photos.json` - Tracks liked photos

That's it! You're ready to automatically like photos with "Muneca" (or any keyword you choose).