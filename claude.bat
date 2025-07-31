@echo off
REM Claude CLI wrapper for Windows

REM Get the directory where this batch file is located
set SCRIPT_DIR=%~dp0

REM Execute the Python script
python "%SCRIPT_DIR%claude.py" %*