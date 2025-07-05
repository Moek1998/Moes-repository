# Flickr Auto-Like Program

A Python program that automatically likes photos on Flickr containing the word "Muneca" (or any other specified keywords).

## Features

- 🔍 **Smart Search**: Search for photos by keywords in titles, descriptions, and tags
- ❤️ **Auto-Like**: Automatically like photos matching your criteria
- 🔐 **OAuth Authentication**: Secure authentication with Flickr API
- ⚙️ **Configurable**: Extensive configuration options for search and behavior
- � **Progress Tracking**: Keeps track of liked photos to avoid duplicates
- �️ **Rate Limiting**: Respects API limits with configurable delays
- � **Logging**: Comprehensive logging for monitoring and debugging
- � **Filtering**: Advanced filtering options (date range, users, tags, etc.)
- 🧪 **Dry Run Mode**: Test the program without actually liking photos

## Installation

1. **Clone or download this repository**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Setup

### 1. Get Flickr API Credentials

1. Go to [Flickr App Garden](https://www.flickr.com/services/api/keys/)
2. Click "Request an API Key"
3. Choose "Apply for a Non-Commercial Key"
4. Fill out the form with your application details
5. You'll receive an API Key and API Secret

### 2. Configure the Program

Run the program once to generate a default configuration file:

```bash
python flickr_auto_like.py
```

This will create a `config.ini` file. Edit it with your API credentials:

```ini
[FLICKR]
api_key = your_api_key_here
api_secret = your_api_secret_here
oauth_token = 
oauth_token_secret = 

[SEARCH]
keywords = Muneca
search_in = title,description,tags
per_page = 100
max_pages = 10
sort = date-posted-desc
privacy_filter = 1
content_type = 1
media = photos

[BEHAVIOR]
max_likes_per_run = 50
delay_between_likes = 2
skip_own_photos = true
skip_already_liked = true
dry_run = false

[FILTERS]
min_upload_date = 
max_upload_date = 
exclude_users = 
required_tags = 
exclude_tags = 
```

### 3. First Run and Authentication

Run the program again after adding your API credentials:

```bash
python flickr_auto_like.py
```

The program will:
1. Open a browser window for OAuth authorization
2. Ask you to authorize the application
3. Request you to enter the verification code
4. Save the authentication tokens for future use

## Configuration Options

### FLICKR Section
- `api_key`: Your Flickr API key
- `api_secret`: Your Flickr API secret
- `oauth_token`: OAuth token (auto-generated during first run)
- `oauth_token_secret`: OAuth token secret (auto-generated during first run)

### SEARCH Section
- `keywords`: Keywords to search for (default: "Muneca")
- `search_in`: Where to search (title, description, tags)
- `per_page`: Number of photos per page (max 100)
- `max_pages`: Maximum pages to search through
- `sort`: Sort order (date-posted-desc, date-posted-asc, date-taken-desc, etc.)
- `privacy_filter`: 1 for public photos, 0 for all
- `content_type`: 1 for photos only, 2 for screenshots, 3 for other
- `media`: Type of media (photos, videos, all)

### BEHAVIOR Section
- `max_likes_per_run`: Maximum number of photos to like per run
- `delay_between_likes`: Delay in seconds between likes (to respect API limits)
- `skip_own_photos`: Whether to skip your own photos
- `skip_already_liked`: Whether to skip previously liked photos
- `dry_run`: Test mode - doesn't actually like photos

### FILTERS Section
- `min_upload_date`: Minimum upload date (YYYY-MM-DD format)
- `max_upload_date`: Maximum upload date (YYYY-MM-DD format)
- `exclude_users`: Comma-separated list of user IDs to exclude
- `required_tags`: Comma-separated list of tags that must be present
- `exclude_tags`: Comma-separated list of tags to exclude

## Usage Examples

### Basic Usage
```bash
python flickr_auto_like.py
```

### Test Mode (Dry Run)
Set `dry_run = true` in config.ini to test without actually liking photos.

### Search for Different Keywords
Change the `keywords` in the SEARCH section:
```ini
keywords = cat cute kitten
```

### Limit by Date Range
Filter photos by upload date:
```ini
min_upload_date = 2023-01-01
max_upload_date = 2023-12-31
```

### Exclude Specific Users
```ini
exclude_users = 12345678@N00,87654321@N00
```

### Require Specific Tags
```ini
required_tags = photography,nature
```

## Files Created

The program creates several files:

- `config.ini`: Configuration file
- `flickr_auto_like.log`: Log file with program output
- `liked_photos.json`: List of previously liked photo IDs

## Logging

The program logs all activities to both the console and `flickr_auto_like.log`. Log levels include:

- **INFO**: General program flow and successful operations
- **WARNING**: Non-critical issues
- **ERROR**: Critical errors that prevent operation

## Rate Limiting

The program includes built-in rate limiting to respect Flickr's API limits:

- Default 2-second delay between likes
- Configurable delay in the `delay_between_likes` setting
- Maximum likes per run to prevent overwhelming the API

## Troubleshooting

### Authentication Issues
- Make sure your API key and secret are correct
- Delete the oauth_token and oauth_token_secret from config.ini to re-authenticate
- Check that your app has the correct permissions

### No Photos Found
- Verify your search keywords
- Check the privacy_filter setting
- Ensure you're searching in the right time range

### API Errors
- Increase the delay_between_likes value
- Reduce max_likes_per_run
- Check your API rate limits on Flickr

## Ethical Usage

Please use this program responsibly:

- Don't spam likes on photos
- Respect other users and their content
- Follow Flickr's Terms of Service
- Use reasonable delays between actions
- Consider the impact on other users

## Legal Disclaimer

This program is provided for educational and automation purposes. Users are responsible for complying with Flickr's Terms of Service and API usage policies. The authors are not responsible for any misuse of this program.

## Support

If you encounter issues:

1. Check the log file for error messages
2. Verify your configuration settings
3. Ensure your API credentials are valid
4. Check Flickr's API status

## License

This program is provided as-is for educational purposes. Use at your own risk.