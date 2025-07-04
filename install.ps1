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
Write-Host "To get started:"
Write-Host "1. Set up your Anthropic API key:"
Write-Host "   claude --setup-key YOUR_API_KEY"
Write-Host "   OR"
Write-Host "   Set environment variable ANTHROPIC_API_KEY"
Write-Host ""
Write-Host "2. Test the installation:"
Write-Host "   claude Hello Claude!"
Write-Host "   OR"
Write-Host "   claude -i    # for interactive mode"
Write-Host ""
Write-Host "For help, run: claude --help"