import argparse
from .main import ClaudeCLI

def main():
    try:
        parser = argparse.ArgumentParser(
            description='Claude CLI - Interact with Claude AI from the command line',
            epilog="""
Examples:
  claude "Hello Claude!"                    # Quick question
  claude -i                                # Interactive mode
  claude --squad                           # Squad simulation mode
  claude --code                            # Code assistant mode
  claude -m claude-3-opus-20240229 "Help"  # Use specific model
  claude --info                            # Show subscription info
            """,
            formatter_class=argparse.RawDescriptionHelpFormatter
        )

        parser.add_argument('message', nargs='*', help='Message to send to Claude')
        parser.add_argument('-i', '--interactive', action='store_true', help='Start interactive mode')
        parser.add_argument('-s', '--system', help='System prompt for the conversation')
        parser.add_argument('-m', '--model', help='Claude model to use')
        parser.add_argument('--setup-key', help='Setup API key')
        parser.add_argument('--config', action='store_true', help='Show config file location')
        parser.add_argument('--models', action='store_true', help='Show available models')
        parser.add_argument('--info', action='store_true', help='Show Claude subscription information')
        parser.add_argument('--squad', action='store_true', help='Start Claude Squad simulation mode')
        parser.add_argument('--code', action='store_true', help='Start Claude Code simulation mode')

        args = parser.parse_args()

        claude = ClaudeCLI()

        if args.setup_key:
            claude.setup_api_key(args.setup_key)
            return

        if args.config:
            print(f"📂 Config file location: {claude.config_file}")
            print(f"📊 Current model: {claude.model}")
            print(f"🔑 API key configured: {'Yes' if claude.api_key else 'No'}")
            return

        if args.models:
            claude.show_models()
            return

        if args.info:
            claude.show_subscription_info()
            return

        if args.squad:
            claude.simulate_squad_features()
            return

        if args.code:
            claude.simulate_code_features()
            return

        if args.interactive:
            claude.interactive_mode()
            return

        if args.message:
            message = ' '.join(args.message)
            response = claude.chat(message, args.system, args.model)
            if response:
                print(response)
        else:
            # If no message provided, show help and start interactive mode
            print("🤖 Claude CLI - AI Assistant")
            print("=" * 30)
            print("💡 Tip: Run 'claude --info' to learn about Claude Pro features")
            print("🔧 Tip: Run 'claude --models' to see available models")
            print("👥 Tip: Run 'claude --squad' for team collaboration features")
            print("💻 Tip: Run 'claude --code' for coding assistance")
            print("\nStarting interactive mode...\n")
            claude.interactive_mode()
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return

if __name__ == '__main__':
    main()