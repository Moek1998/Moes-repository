# PowerShell setup script for Claude CLI

Write-Host "Setting up Claude CLI for PowerShell..." -ForegroundColor Green

# Get the directory where this script is located
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Create a batch file wrapper for Windows
$batchContent = @"
@echo off
python "%~dp0claude.py" %*
"@

$batchFile = Join-Path $scriptDir "claude.bat"
Set-Content -Path $batchFile -Value $batchContent

# Create a PowerShell wrapper function
$psWrapperContent = @"
function claude {
    python "$scriptDir\claude.py" `$args
}
"@

# Check if the PowerShell profile exists
$profileDir = Split-Path -Parent $PROFILE
if (!(Test-Path $profileDir)) {
    New-Item -ItemType Directory -Path $profileDir -Force | Out-Null
}

if (!(Test-Path $PROFILE)) {
    New-Item -ItemType File -Path $PROFILE -Force | Out-Null
}

# Check if the function is already in the profile
$profileContent = Get-Content $PROFILE -Raw -ErrorAction SilentlyContinue
if ($profileContent -notmatch "function claude") {
    Add-Content -Path $PROFILE -Value "`n# Claude CLI function`n$psWrapperContent"
    Write-Host "Added claude function to PowerShell profile" -ForegroundColor Yellow
}

# Add script directory to PATH for current session
$env:Path = "$scriptDir;$env:Path"

# Try to add to system PATH (requires admin rights)
try {
    $currentPath = [Environment]::GetEnvironmentVariable("Path", [EnvironmentVariableTarget]::User)
    if ($currentPath -notlike "*$scriptDir*") {
        [Environment]::SetEnvironmentVariable("Path", "$scriptDir;$currentPath", [EnvironmentVariableTarget]::User)
        Write-Host "Added $scriptDir to user PATH" -ForegroundColor Green
    }
} catch {
    Write-Host "Could not add to PATH automatically. You may need to run as administrator." -ForegroundColor Yellow
}

# Install Python dependencies
Write-Host "`nInstalling Python dependencies..." -ForegroundColor Yellow
& python -m pip install --user requests

Write-Host "`nClaude CLI setup complete!" -ForegroundColor Green
Write-Host "`nNext steps:" -ForegroundColor Cyan
Write-Host "1. Set your Claude API key:" -ForegroundColor White
Write-Host "   `$env:CLAUDE_API_KEY = 'your-api-key-here'" -ForegroundColor Gray
Write-Host "   To make it permanent, add to your PowerShell profile or set as system environment variable" -ForegroundColor Gray
Write-Host ""
Write-Host "2. Reload your PowerShell profile:" -ForegroundColor White
Write-Host "   . `$PROFILE" -ForegroundColor Gray
Write-Host "   Or restart PowerShell" -ForegroundColor Gray
Write-Host ""
Write-Host "3. Test the installation:" -ForegroundColor White
Write-Host "   claude --help" -ForegroundColor Gray
Write-Host ""
Write-Host "Get your API key from: https://console.anthropic.com/" -ForegroundColor Yellow