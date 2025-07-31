# Claude CLI Installation Script for Windows PowerShell

Write-Host "Installing Claude CLI..." -ForegroundColor Green

# Check if Python is installed
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Error: Python is required but not installed." -ForegroundColor Red
    Write-Host "Please install Python from https://python.org and try again."
    exit 1
}

# Check if pip is installed
if (-not (Get-Command pip -ErrorAction SilentlyContinue)) {
    Write-Host "Error: pip is required but not installed." -ForegroundColor Red
    Write-Host "Please install pip and try again."
    exit 1
}

# Install Python dependencies
Write-Host "Installing Python dependencies..."
pip install -r requirements.txt --user

# Create installation directory
$InstallDir = "$env:USERPROFILE\.local\bin"
if (-not (Test-Path $InstallDir)) {
    New-Item -ItemType Directory -Path $InstallDir -Force | Out-Null
}

# Copy files to installation directory
Write-Host "Installing Claude CLI to $InstallDir..."
Copy-Item "claude.py" "$InstallDir\"
Copy-Item "claude.bat" "$InstallDir\"

# Check if the install directory is in PATH
$CurrentPath = [Environment]::GetEnvironmentVariable("PATH", "User")
if ($CurrentPath -notlike "*$InstallDir*") {
    Write-Host "Warning: $InstallDir is not in your PATH." -ForegroundColor Yellow
    Write-Host "To make the 'claude' command available globally, add $InstallDir to your PATH."
    Write-Host "You can do this through System Properties > Environment Variables"
    Write-Host "Or run this command as Administrator:"
    Write-Host "[Environment]::SetEnvironmentVariable('PATH', `$env:PATH + ';$InstallDir', 'User')" -ForegroundColor Cyan
    Write-Host ""
}

Write-Host "Installation completed successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "🚀 CLAUDE CLI READY!" -ForegroundColor Cyan
Write-Host "==============================="
Write-Host ""
Write-Host "📋 GETTING STARTED:" -ForegroundColor Yellow
Write-Host "1. Learn about Claude access types:"
Write-Host "   claude --info" -ForegroundColor Cyan
Write-Host ""
Write-Host "2. Set up your Anthropic API key:"
Write-Host "   claude --setup-key YOUR_API_KEY" -ForegroundColor Cyan
Write-Host "   OR"
Write-Host "   Set environment variable ANTHROPIC_API_KEY" -ForegroundColor Cyan
Write-Host "   Get key: https://console.anthropic.com/" -ForegroundColor Blue
Write-Host ""
Write-Host "3. Try the new features:" -ForegroundColor Yellow
Write-Host "   claude 'Hello Claude!'                    # Quick question" -ForegroundColor Cyan
Write-Host "   claude -i                                # Interactive mode" -ForegroundColor Cyan
Write-Host "   claude --squad                           # Team collaboration" -ForegroundColor Cyan
Write-Host "   claude --code                            # Coding assistant" -ForegroundColor Cyan
Write-Host "   claude --models                          # Show available models" -ForegroundColor Cyan
Write-Host ""
Write-Host "💡 PRO TIP: This CLI uses API access (pay-per-use)" -ForegroundColor Yellow
Write-Host "   For Claude Pro features like real Squad & Code,"
Write-Host "   visit: https://claude.ai/ (`$20/month)" -ForegroundColor Blue
Write-Host ""
Write-Host "📚 For help: claude --help" -ForegroundColor Green