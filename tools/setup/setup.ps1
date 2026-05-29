# Antigravity Toolkit Setup Script for Windows

Write-Host "Checking Python installation..."
if (Get-Command python -ErrorAction SilentlyContinue) {
    $PYTHON_CMD = "python"
} elseif (Get-Command python3 -ErrorAction SilentlyContinue) {
    $PYTHON_CMD = "python3"
} else {
    Write-Host "Error: Python 3 is required but not installed." -ForegroundColor Red
    exit 1
}

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$SetupPy = Join-Path $ScriptDir "setup.py"

& $PYTHON_CMD $SetupPy $args
