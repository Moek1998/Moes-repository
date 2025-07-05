#!/usr/bin/env python3
"""
Flickr Auto-Like Program
========================

This program automatically likes photos on Flickr that contain the word "Muneca"
in their title, description, or tags.

Features:
- OAuth authentication with Flickr
- Search for photos with specific keywords
- Automatic liking of photos
- Rate limiting to respect API limits
- Configuration file support
- Progress tracking
- Error handling and logging

Author: Auto-generated for Flickr automation
"""

import os
import sys
import time
import json
import logging
from datetime import datetime, timedelta
from configparser import ConfigParser
from typing import List, Dict, Optional, Set
import flickrapi
import requests
from dateutil.parser import parse as parse_date


class FlickrAutoLiker:
    """Main class for automatically liking photos on Flickr"""
    
    def __init__(self, config_file: str = 'config.ini'):
        """
        Initialize the FlickrAutoLiker
        
        Args:
            config_file (str): Path to configuration file
        """
        self.config_file = config_file
        self.config = ConfigParser()
        self.flickr = None
        self.setup_logging()
        self.load_config()
        self.liked_photos = set()
        self.load_liked_photos()
        
    def setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('flickr_auto_like.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def load_config(self):
        """Load configuration from file"""
        if os.path.exists(self.config_file):
            self.config.read(self.config_file)
        else:
            self.create_default_config()
            
    def create_default_config(self):
        """Create default configuration file"""
        self.config['FLICKR'] = {
            'api_key': '',
            'api_secret': '',
            'oauth_token': '',
            'oauth_token_secret': ''
        }
        
        self.config['SEARCH'] = {
            'keywords': 'Muneca',
            'search_in': 'title,description,tags',
            'per_page': '100',
            'max_pages': '10',
            'sort': 'date-posted-desc',
            'privacy_filter': '1',  # Public photos only
            'content_type': '1',    # Photos only
            'media': 'photos'
        }
        
        self.config['BEHAVIOR'] = {
            'max_likes_per_run': '50',
            'delay_between_likes': '2',
            'skip_own_photos': 'true',
            'skip_already_liked': 'true',
            'dry_run': 'false'
        }
        
        self.config['FILTERS'] = {
            'min_upload_date': '',  # YYYY-MM-DD format
            'max_upload_date': '',  # YYYY-MM-DD format
            'exclude_users': '',    # Comma-separated user IDs
            'required_tags': '',    # Comma-separated tags
            'exclude_tags': ''      # Comma-separated tags
        }
        
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)
            
        self.logger.info(f"Created default configuration file: {self.config_file}")
        self.logger.info("Please edit the configuration file with your Flickr API credentials")
        
    def authenticate(self):
        """Authenticate with Flickr API"""
        api_key = self.config.get('FLICKR', 'api_key')
        api_secret = self.config.get('FLICKR', 'api_secret')
        
        if not api_key or not api_secret:
            self.logger.error("API key and secret are required. Please update config.ini")
            return False
            
        self.flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
        
        # Check if we have stored tokens
        oauth_token = self.config.get('FLICKR', 'oauth_token', fallback='')
        oauth_token_secret = self.config.get('FLICKR', 'oauth_token_secret', fallback='')
        
        if oauth_token and oauth_token_secret:
            self.flickr.token_cache.token = oauth_token
            self.flickr.token_cache.token_secret = oauth_token_secret
            try:
                # Test the authentication
                self.flickr.test.login()
                self.logger.info("Authentication successful using stored tokens")
                return True
            except Exception as e:
                self.logger.warning(f"Stored tokens invalid: {e}")
                
        # Need to authenticate
        self.logger.info("Starting OAuth authentication...")
        self.logger.info("Please visit the following URL to authorize the application:")
        
        # Get authorization URL
        self.flickr.get_request_token(oauth_callback='oob')
        authorize_url = self.flickr.auth_url(perms='write')
        print(f"\nAuthorization URL: {authorize_url}")
        
        # Get verifier from user
        verifier = input("\nEnter the verification code: ").strip()
        
        try:
            self.flickr.get_access_token(verifier)
            
            # Save tokens to config
            self.config.set('FLICKR', 'oauth_token', self.flickr.token_cache.token)
            self.config.set('FLICKR', 'oauth_token_secret', self.flickr.token_cache.token_secret)
            
            with open(self.config_file, 'w') as configfile:
                self.config.write(configfile)
                
            self.logger.info("Authentication successful and tokens saved")
            return True
            
        except Exception as e:
            self.logger.error(f"Authentication failed: {e}")
            return False
            
    def load_liked_photos(self):
        """Load previously liked photos from file"""
        liked_file = 'liked_photos.json'
        if os.path.exists(liked_file):
            try:
                with open(liked_file, 'r') as f:
                    self.liked_photos = set(json.load(f))
                self.logger.info(f"Loaded {len(self.liked_photos)} previously liked photos")
            except Exception as e:
                self.logger.warning(f"Error loading liked photos: {e}")
                self.liked_photos = set()
                
    def save_liked_photos(self):
        """Save liked photos to file"""
        liked_file = 'liked_photos.json'
        try:
            with open(liked_file, 'w') as f:
                json.dump(list(self.liked_photos), f)
        except Exception as e:
            self.logger.error(f"Error saving liked photos: {e}")
            
    def search_photos(self) -> List[Dict]:
        """
        Search for photos containing the specified keywords
        
        Returns:
            List[Dict]: List of photo dictionaries
        """
        keywords = self.config.get('SEARCH', 'keywords', fallback='Muneca')
        per_page = int(self.config.get('SEARCH', 'per_page', fallback='100'))
        max_pages = int(self.config.get('SEARCH', 'max_pages', fallback='10'))
        sort = self.config.get('SEARCH', 'sort', fallback='date-posted-desc')
        privacy_filter = self.config.get('SEARCH', 'privacy_filter', fallback='1')
        content_type = self.config.get('SEARCH', 'content_type', fallback='1')
        
        all_photos = []
        
        self.logger.info(f"Searching for photos with keywords: {keywords}")
        
        for page in range(1, max_pages + 1):
            try:
                response = self.flickr.photos.search(
                    text=keywords,
                    per_page=per_page,
                    page=page,
                    sort=sort,
                    privacy_filter=privacy_filter,
                    content_type=content_type,
                    extras='owner_name,date_upload,description,tags,url_s,url_m'
                )
                
                if 'photos' in response and 'photo' in response['photos']:
                    photos = response['photos']['photo']
                    all_photos.extend(photos)
                    
                    self.logger.info(f"Found {len(photos)} photos on page {page}")
                    
                    # Check if we've reached the last page
                    if page >= response['photos']['pages']:
                        break
                        
                else:
                    self.logger.warning(f"No photos found on page {page}")
                    break
                    
            except Exception as e:
                self.logger.error(f"Error searching photos on page {page}: {e}")
                break
                
        self.logger.info(f"Total photos found: {len(all_photos)}")
        return all_photos
        
    def filter_photos(self, photos: List[Dict]) -> List[Dict]:
        """
        Filter photos based on configuration criteria
        
        Args:
            photos (List[Dict]): List of photo dictionaries
            
        Returns:
            List[Dict]: Filtered list of photos
        """
        filtered_photos = []
        skip_own_photos = self.config.getboolean('BEHAVIOR', 'skip_own_photos', fallback=True)
        skip_already_liked = self.config.getboolean('BEHAVIOR', 'skip_already_liked', fallback=True)
        
        # Get user info to filter own photos
        user_info = None
        if skip_own_photos:
            try:
                user_info = self.flickr.test.login()
                own_user_id = user_info['user']['id']
            except Exception as e:
                self.logger.warning(f"Could not get user info: {e}")
                own_user_id = None
        
        # Get filter criteria
        exclude_users = self.config.get('FILTERS', 'exclude_users', fallback='').split(',')
        exclude_users = [u.strip() for u in exclude_users if u.strip()]
        
        required_tags = self.config.get('FILTERS', 'required_tags', fallback='').split(',')
        required_tags = [t.strip().lower() for t in required_tags if t.strip()]
        
        exclude_tags = self.config.get('FILTERS', 'exclude_tags', fallback='').split(',')
        exclude_tags = [t.strip().lower() for t in exclude_tags if t.strip()]
        
        min_date = self.config.get('FILTERS', 'min_upload_date', fallback='')
        max_date = self.config.get('FILTERS', 'max_upload_date', fallback='')
        
        for photo in photos:
            photo_id = photo['id']
            
            # Skip already liked photos
            if skip_already_liked and photo_id in self.liked_photos:
                continue
                
            # Skip own photos
            if skip_own_photos and own_user_id and photo.get('owner') == own_user_id:
                continue
                
            # Skip excluded users
            if photo.get('owner') in exclude_users:
                continue
                
            # Check date filters
            if min_date or max_date:
                try:
                    upload_date = datetime.fromtimestamp(int(photo.get('dateupload', 0)))
                    if min_date and upload_date < parse_date(min_date):
                        continue
                    if max_date and upload_date > parse_date(max_date):
                        continue
                except (ValueError, TypeError):
                    continue
                    
            # Check tag filters
            photo_tags = photo.get('tags', '').lower().split()
            
            if required_tags:
                if not any(tag in photo_tags for tag in required_tags):
                    continue
                    
            if exclude_tags:
                if any(tag in photo_tags for tag in exclude_tags):
                    continue
                    
            filtered_photos.append(photo)
            
        self.logger.info(f"Filtered to {len(filtered_photos)} photos")
        return filtered_photos
        
    def like_photo(self, photo_id: str) -> bool:
        """
        Like a photo
        
        Args:
            photo_id (str): Photo ID to like
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.flickr.favorites.add(photo_id=photo_id)
            self.liked_photos.add(photo_id)
            return True
        except Exception as e:
            # Check if already liked
            if "already in favorites" in str(e).lower():
                self.liked_photos.add(photo_id)
                return True
            self.logger.error(f"Error liking photo {photo_id}: {e}")
            return False
            
    def run(self):
        """Main execution function"""
        self.logger.info("Starting Flickr Auto-Like Program")
        
        # Authenticate
        if not self.authenticate():
            self.logger.error("Authentication failed. Exiting.")
            return
            
        # Search for photos
        photos = self.search_photos()
        if not photos:
            self.logger.info("No photos found. Exiting.")
            return
            
        # Filter photos
        filtered_photos = self.filter_photos(photos)
        if not filtered_photos:
            self.logger.info("No photos match the filter criteria. Exiting.")
            return
            
        # Like photos
        max_likes = int(self.config.get('BEHAVIOR', 'max_likes_per_run', fallback='50'))
        delay = float(self.config.get('BEHAVIOR', 'delay_between_likes', fallback='2'))
        dry_run = self.config.getboolean('BEHAVIOR', 'dry_run', fallback=False)
        
        liked_count = 0
        
        for photo in filtered_photos[:max_likes]:
            if liked_count >= max_likes:
                break
                
            photo_id = photo['id']
            photo_title = photo.get('title', 'Untitled')
            photo_owner = photo.get('ownername', 'Unknown')
            
            self.logger.info(f"Processing photo: '{photo_title}' by {photo_owner} (ID: {photo_id})")
            
            if dry_run:
                self.logger.info("DRY RUN: Would like this photo")
                liked_count += 1
            else:
                if self.like_photo(photo_id):
                    self.logger.info("✓ Successfully liked photo")
                    liked_count += 1
                else:
                    self.logger.warning("✗ Failed to like photo")
                    
            # Add delay between likes
            if delay > 0:
                time.sleep(delay)
                
        self.logger.info(f"Liked {liked_count} photos")
        
        # Save liked photos
        if not dry_run:
            self.save_liked_photos()
            
        self.logger.info("Flickr Auto-Like Program completed")


def main():
    """Main entry point"""
    auto_liker = FlickrAutoLiker()
    
    try:
        auto_liker.run()
    except KeyboardInterrupt:
        auto_liker.logger.info("Program interrupted by user")
    except Exception as e:
        auto_liker.logger.error(f"Unexpected error: {e}")
        raise


if __name__ == "__main__":
    main()