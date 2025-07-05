#!/usr/bin/env python3
"""
Command-line interface for Flickr Auto-Like Program
"""

import argparse
import sys
import os
from pathlib import Path
import subprocess

def run_setup():
    """Run the setup script"""
    print("🚀 Running setup...")
    try:
        subprocess.run([sys.executable, "setup.py"], check=True)
    except subprocess.CalledProcessError:
        print("❌ Setup failed")
        sys.exit(1)

def run_program(args):
    """Run the main program with optional arguments"""
    cmd = [sys.executable, "flickr_auto_like.py"]
    
    # Pass through any additional arguments
    if hasattr(args, 'extra_args') and args.extra_args:
        cmd.extend(args.extra_args)
    
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        print("❌ Program execution failed")
        sys.exit(1)

def check_config():
    """Check if config.ini exists and has API keys"""
    config_file = Path("config.ini")
    
    if not config_file.exists():
        print("❌ config.ini not found")
        print("Run: python run_flickr_auto_like.py --setup")
        return False
    
    try:
        with open(config_file, 'r') as f:
            content = f.read()
            
        if "your_flickr_api_key_here" in content or "your_flickr_api_secret_here" in content:
            print("⚠️  config.ini needs to be configured with your API keys")
            print("Edit config.ini and add your Flickr API credentials")
            return False
        
        print("✅ config.ini looks good")
        return True
        
    except Exception as e:
        print(f"❌ Error reading config.ini: {e}")
        return False

def show_status():
    """Show current status of the program"""
    print("📊 Flickr Auto-Like Program Status")
    print("=" * 40)
    
    # Check if files exist
    files_to_check = [
        "flickr_auto_like.py",
        "requirements.txt",
        "config.ini"
    ]
    
    for file in files_to_check:
        if Path(file).exists():
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} missing")
    
    # Check config
    print("\n📋 Configuration:")
    check_config()
    
    # Check log file
    log_file = Path("flickr_auto_like.log")
    if log_file.exists():
        print(f"📝 Log file: {log_file} ({log_file.stat().st_size} bytes)")
    else:
        print("📝 No log file found")
    
    # Check liked photos
    liked_file = Path("liked_photos.json")
    if liked_file.exists():
        print(f"❤️  Liked photos file: {liked_file} ({liked_file.stat().st_size} bytes)")
    else:
        print("❤️  No liked photos file found")

def dry_run():
    """Run in dry-run mode"""
    print("🧪 Running in dry-run mode (no photos will be liked)")
    
    # Temporarily modify config to enable dry run
    config_file = Path("config.ini")
    if not config_file.exists():
        print("❌ config.ini not found. Run --setup first.")
        return
    
    # Read current config
    with open(config_file, 'r') as f:
        config_content = f.read()
    
    # Backup original config
    backup_file = Path("config.ini.backup")
    with open(backup_file, 'w') as f:
        f.write(config_content)
    
    # Enable dry run
    config_content = config_content.replace("dry_run = false", "dry_run = true")
    
    with open(config_file, 'w') as f:
        f.write(config_content)
    
    try:
        # Run the program
        run_program(argparse.Namespace())
    finally:
        # Restore original config
        with open(backup_file, 'r') as f:
            original_content = f.read()
        
        with open(config_file, 'w') as f:
            f.write(original_content)
        
        backup_file.unlink()
        print("✅ Original configuration restored")

def main():
    """Main CLI function"""
    parser = argparse.ArgumentParser(
        description="Flickr Auto-Like Program CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_flickr_auto_like.py --setup           # Run setup
  python run_flickr_auto_like.py --run             # Run the program
  python run_flickr_auto_like.py --dry-run         # Test run without liking
  python run_flickr_auto_like.py --status          # Show status
  python run_flickr_auto_like.py --check-config    # Check configuration
        """
    )
    
    parser.add_argument(
        "--setup", 
        action="store_true",
        help="Run the setup script"
    )
    
    parser.add_argument(
        "--run", 
        action="store_true",
        help="Run the main program"
    )
    
    parser.add_argument(
        "--dry-run", 
        action="store_true",
        help="Run in dry-run mode (no photos will be liked)"
    )
    
    parser.add_argument(
        "--status", 
        action="store_true",
        help="Show program status"
    )
    
    parser.add_argument(
        "--check-config", 
        action="store_true",
        help="Check configuration file"
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # If no arguments provided, show help
    if not any(vars(args).values()):
        parser.print_help()
        return
    
    # Handle arguments
    if args.setup:
        run_setup()
    
    elif args.run:
        if not check_config():
            print("❌ Configuration issues found. Please fix them first.")
            return
        run_program(args)
    
    elif args.dry_run:
        if not check_config():
            print("❌ Configuration issues found. Please fix them first.")
            return
        dry_run()
    
    elif args.status:
        show_status()
    
    elif args.check_config:
        check_config()

if __name__ == "__main__":
    main()