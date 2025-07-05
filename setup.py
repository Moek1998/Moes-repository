#!/usr/bin/env python3
"""
Setup script for Flickr Auto-Like Program
"""

import os
import sys
import subprocess
import pkg_resources
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    
    requirements_file = Path("requirements.txt")
    if not requirements_file.exists():
        print("❌ requirements.txt not found")
        return False
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def check_dependencies():
    """Check if all required dependencies are installed"""
    print("🔍 Checking dependencies...")
    
    required_packages = [
        "flickrapi",
        "requests",
        "python-dateutil",
        "configparser"
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            pkg_resources.get_distribution(package)
            print(f"✅ {package} is installed")
        except pkg_resources.DistributionNotFound:
            print(f"❌ {package} is missing")
            missing_packages.append(package)
    
    return len(missing_packages) == 0

def create_sample_config():
    """Create a sample configuration file"""
    config_file = Path("config.ini")
    
    if config_file.exists():
        print("⚠️  config.ini already exists, skipping creation")
        return True
    
    print("📝 Creating sample configuration file...")
    
    config_content = """[FLICKR]
api_key = your_flickr_api_key_here
api_secret = your_flickr_api_secret_here
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
dry_run = true

[FILTERS]
min_upload_date = 
max_upload_date = 
exclude_users = 
required_tags = 
exclude_tags = 
"""
    
    try:
        with open(config_file, 'w') as f:
            f.write(config_content)
        print("✅ Sample config.ini created")
        return True
    except Exception as e:
        print(f"❌ Error creating config.ini: {e}")
        return False

def make_executable():
    """Make the main script executable on Unix systems"""
    if os.name == 'posix':  # Unix/Linux/Mac
        try:
            os.chmod('flickr_auto_like.py', 0o755)
            print("✅ Made flickr_auto_like.py executable")
        except Exception as e:
            print(f"⚠️  Could not make script executable: {e}")

def print_next_steps():
    """Print next steps for the user"""
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Get your Flickr API credentials from: https://www.flickr.com/services/api/keys/")
    print("2. Edit config.ini and add your API key and secret")
    print("3. Run the program: python flickr_auto_like.py")
    print("4. The program will guide you through OAuth authentication")
    print("\n⚠️  Note: dry_run is enabled by default. Change it to 'false' in config.ini when ready!")

def main():
    """Main setup function"""
    print("🚀 Flickr Auto-Like Program Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Setup failed during dependency installation")
        sys.exit(1)
    
    # Check dependencies
    if not check_dependencies():
        print("❌ Some dependencies are still missing")
        sys.exit(1)
    
    # Create sample config
    if not create_sample_config():
        print("❌ Setup failed during config creation")
        sys.exit(1)
    
    # Make executable
    make_executable()
    
    # Print next steps
    print_next_steps()

if __name__ == "__main__":
    main()