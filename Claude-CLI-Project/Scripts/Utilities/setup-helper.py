#!/usr/bin/env python3
"""
Claude CLI Setup Helper
Utility script for setting up and configuring the Claude CLI
"""

import os
import sys
import configparser
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Error: Python 3.7 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python {sys.version.split()[0]} detected")
    return True

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import requests
        print("✅ requests library found")
    except ImportError:
        print("❌ requests library not found")
        print("Install with: pip install requests")
        return False
    
    try:
        import configparser
        print("✅ configparser library found")
    except ImportError:
        print("❌ configparser library not found")
        print("Install with: pip install configparser")
        return False
    
    return True

def setup_config_directory():
    """Create configuration directory and files"""
    config_dir = Path.home() / '.claude'
    config_file = config_dir / 'config.ini'
    
    # Create directory if it doesn't exist
    config_dir.mkdir(exist_ok=True)
    print(f"✅ Configuration directory: {config_dir}")
    
    # Create default config if it doesn't exist
    if not config_file.exists():
        config = configparser.ConfigParser()
        config['DEFAULT'] = {
            'api_key': '',
            'model': 'claude-3-5-sonnet-20241022',
            'max_tokens': '1000',
            'temperature': '0.7',
            'subscription_type': 'api'
        }
        
        config['PRO_FEATURES'] = {
            'priority_bandwidth': 'false',
            'early_access': 'false',
            'usage_5x_limit': 'false'
        }
        
        with open(config_file, 'w') as f:
            config.write(f)
        print(f"✅ Created default config: {config_file}")
    else:
        print(f"✅ Config file exists: {config_file}")
    
    return config_file

def check_api_key():
    """Check if API key is configured"""
    config_dir = Path.home() / '.claude'
    config_file = config_dir / 'config.ini'
    
    if not config_file.exists():
        print("❌ Config file not found")
        return False
    
    config = configparser.ConfigParser()
    config.read(config_file)
    
    api_key = config.get('DEFAULT', 'api_key', fallback='')
    env_key = os.getenv('ANTHROPIC_API_KEY', '')
    
    if api_key or env_key:
        print("✅ API key configured")
        return True
    else:
        print("❌ No API key found")
        print("Set up with: claude --setup-key YOUR_API_KEY")
        print("Or set environment variable: export ANTHROPIC_API_KEY=your_key")
        return False

def main():
    """Main setup function"""
    print("🔧 Claude CLI Setup Helper")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Setup config directory
    config_file = setup_config_directory()
    
    # Check API key
    check_api_key()
    
    print("\n🎯 Next Steps:")
    print("1. Get API key: https://console.anthropic.com/")
    print("2. Set up key: claude --setup-key YOUR_API_KEY")
    print("3. Test: claude 'Hello Claude!'")
    print("4. Interactive: claude -i")

if __name__ == "__main__":
    main()