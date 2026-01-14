# Python Version Manager (pyvm)

A cross-platform CLI tool with an interactive TUI to check and install Python versions side-by-side with your existing installation.

## What's New in v2.1.0

**Security & Reliability Improvements!**

* **SHA256 Checksum Verification**: All Python downloads are now verified against official checksums from python.org for enhanced security
* **Rollback Command**: Undo your last Python installation with `pyvm rollback` - easily remove versions you no longer need
* **Auto pyenv Installation**: On RHEL/CentOS/Fedora systems, pyenv is automatically installed if not present
* **Type Safety**: Improved type hints throughout the codebase for better reliability

**TUI Enhancements:**
* **Rollback Button**: Press `B` to rollback your last installation directly from the TUI
* **Remove Versions**: Press `X` to remove installed Python versions

Try it: `pyvm tui` or `pyvm rollback`

## CRITICAL UPDATE (v1.2.1)

**If you are using v1.2.0 or earlier:** Please update immediately.

Previous versions contained system-breaking code that could freeze Linux systems. **v1.2.1+ is completely safe** and only installs Python without modifying system defaults.

```bash
# Update to the safe version
cd pyvm-updater
git pull
pip install --user -e .
```

See [docs/CRITICAL_SECURITY_FIX_v1.2.1.md](docs/CRITICAL_SECURITY_FIX_v1.2.1.md) for details and recovery instructions.

**Documentation**: [Installation Guide](docs/INSTALL.md) | [Quick Start](docs/QUICKSTART.md) | [Quick Reference](docs/QUICK_REFERENCE.md)

## Quick Start

```bash
# Install the package
pip install --user pyvm-updater

# Use it
pyvm check      # Check your Python version
pyvm update     # Update to latest Python
pyvm tui        # Launch interactive TUI (NEW!)
```

## Features

### Interactive TUI (New in v2.0!)
* Beautiful Terminal Interface: Navigate with keyboard or mouse
* Three-Panel Layout: See installed versions, available releases, and status at a glance
* Keyboard Navigation: Tab between panels, arrows to navigate, Enter to install
* Click to Install: Mouse support for all actions
* Live Updates: See installation progress in real-time
* Theme Support: Switch between dark and light themes (press T)

### CLI Features
* Check your current Python version against the latest stable release
* Install the latest Python or specific versions side-by-side
* List all available Python versions with support status
* Cross-platform support (Windows, Linux, macOS)
* Detailed system information display
* Simple and intuitive CLI interface

### Safety & Intelligence
* Safe: Never modifies your system Python defaults
* SHA256 Verified: All downloads verified against official checksums (NEW in v2.1.0!)
* Smart Installation: Auto-detects and uses mise, pyenv, or system package managers
* Auto pyenv Setup: Automatically installs pyenv on RHEL/CentOS/Fedora if needed
* Rollback Support: Undo installations with `pyvm rollback`
* Multiple Versions: All Python versions coexist peacefully
* Clear Instructions: Shows exactly how to use newly installed versions

## Installation

### Method 1: From GitHub (For New Users)

```bash
# Clone the repository
git clone https://github.com/shreyasmene06/pyvm-updater.git
cd pyvm-updater

# Install
pip install --user .
```

### Method 2: Install via pip (Published on PyPI)

```bash
pip install --user pyvm-updater
```

**Note for Linux users:** On newer systems (Ubuntu 23.04+, Debian 12+), use the `--user` flag or see [troubleshooting](#troubleshooting) if you encounter an "externally-managed-environment" error.

### Method 3: Install via pipx (Recommended for CLI tools)

```bash
# Install pipx if you don't have it
sudo apt install pipx   # Ubuntu/Debian
# or: brew install pipx  # macOS

# Install pyvm-updater
pipx install pyvm-updater

# If pyvm command not found, add to PATH:
pipx ensurepath

# Then restart your terminal or run:
source ~/.bashrc   # or source ~/.zshrc
```

**Why use `--user` or pipx?** On newer Linux systems, using `pip install` without these options may fail with an "externally-managed-environment" error. Use the `--user` flag or see [troubleshooting](#troubleshooting) if you encounter this error.

### Verify Installation

```bash
# Verify installation
pyvm --version
pyvm check
```
**For TUI mode (optional but recommended):**
```bash
pip install --user "pyvm-updater[tui]"
```

Or install textual separately:
```bash
pip install --user textual
```


All dependencies are automatically installed.

### Dependencies

If you encounter permission errors, use `pip install --user .` instead of `pip install .`

This will automatically install all required dependencies:

* requests
* beautifulsoup4
* packaging
* click

The `pyvm` command will be available globally after installation.

### Special Note for Anaconda Users

If you are using Anaconda or Miniconda, the `pyvm update` command will install the latest Python to your system, but your Anaconda environment will continue using its own Python version. This is expected behavior.

**How to check:**
```bash
# Your Anaconda Python (unchanged)
python --version

# The newly installed system Python
python3.14 --version
```

**To use the updated Python:**

1. Use it directly: `python3.14 your_script.py`
2. Create a new environment: `python3.14 -m venv myenv`
3. Continue using Anaconda (recommended for data science work)

**Why does this happen?**

Anaconda manages its own Python installation separately from system Python. This prevents conflicts between your Anaconda packages and system packages.

---

**For detailed installation instructions, see [INSTALL.md](docs/INSTALL.md)**

## Usage

### Interactive TUI Mode (Recommended)

Launch the terminal interface:

```bash
pyvm tui
```

**Navigation:**
* **Tab / Shift+Tab**: Switch between panels (Installed, Available, Status)
* **Arrow Keys**: Navigate within a panel
* **Enter**: Install the selected version from the Available panel
* **1 / 2**: Quick jump to Installed or Available panel
* **U**: Update to the latest Python version
* **R**: Refresh data
* **T**: Toggle theme (dark/light)
* **?**: Show help
* **Q**: Quit

**Panels:**
1. **INSTALLED**: Shows all Python versions detected on your system (current version is marked, shows installation paths)
2. **AVAILABLE**: Lists all active Python releases from python.org (latest version shown first, status indicators, press Enter to install)
3. **STATUS**: Shows current Python, latest available, and update status

### List Available Versions

See all Python versions you can install:

```bash
# Show active release series (3.9+, security updates, etc.)
pyvm list

# Show all versions including patch releases
pyvm list --all
```

Output example:
```
Available Python Versions:
==========================
3.15.x   * pre-release
3.14.0   * bugfix (active development)
3.13.1   * bugfix (active development)
3.12.8   * security (supported until 2028)
3.11.11  * security (supported until 2027)
3.10.16  * security (supported until 2026)
3.9.21   * end of life
```

### Install Specific Version

Install any Python version:

```bash
pyvm install 3.12.8
pyvm install 3.11.5
pyvm install 3.13.1

# Auto-confirm installation
pyvm install 3.12.8 *y
```

The installer will:
* On Linux/macOS: Try mise to pyenv to system package manager
* On Windows: Download official installer from python.org
* Install side-by-side without touching your system Python

### Check Python version

Simply run the tool to check your Python version:

```bash
pyvm
# or
pyvm check
```

Output example:
```
Checking Python version... (Current: 3.12.3)

========================================
A new version (3.14.0) is available!

Current version:   3.12.3
Latest version:    3.14.0
========================================

Tip: Run 'pyvm update' to upgrade Python
```

### Update Python

Update to the latest version:

```bash
pyvm update
```

Update to a specific version:

```bash
pyvm update --version 3.11.5
```

For automatic installation without confirmation:

```bash
pyvm update --auto
pyvm update --version 3.11.5 --auto
```

**IMPORTANT:** This command installs Python side-by-side. Your system Python remains unchanged.

### After Installing - How to Use the New Python

Once installation completes, the new Python is available side-by-side with your existing version:

**Linux/macOS:**
```bash
# Your old Python (unchanged)
python3 --version          # Shows: Python 3.10.x (or whatever you had)

# Your new Python (side-by-side)
python3.12 --version       # Shows: Python 3.12.x

# Use the new Python for a script
python3.12 your_script.py

# Create a virtual environment with the new Python
python3.12 -m venv myproject
source myproject/bin/activate
python --version           # Now shows 3.12.x in this venv
```

**Windows:**
```bash
# List all Python versions
py --list

# Use specific version
py -3.12 your_script.py

# Create virtual environment
py -3.12 -m venv myproject
myproject\Scripts\activate
```

**Why doesn't `python3` automatically use the new version?**

This is intentional and safe! Your system tools (package managers, system utilities) depend on the Python version they were built with. Changing the default could break them. The tool gives you the new Python to use when YOU choose, without risking your system.

### Show system information

```bash
pyvm info
```

Output example:
```
==================================================
           System Information
==================================================
Operating System: Linux
Architecture:     amd64
Python Version:   3.12.3
Python Path:      /usr/bin/python3
Platform:         Linux-5.15.0-generic-x86_64
# How It Works

### Smart Installation Strategy

pyvm uses an intelligent fallback chain to install Python:

**Linux:**
1. **mise** (if available) * Modern, user-friendly version manager
2. **pyenv** (if available) * Popular Python version manager
3. **apt** with deadsnakes PPA (Ubuntu/Debian)
4. **dnf/yum** (Fedora/RHEL)

**macOS:**
1. **mise** (if available) * Modern, user-friendly version manager
2. **pyenv** (if available) * Popular Python version manager
3. **Homebrew** (most common)
4. Official installer link (fallback)

### Windows

* Downloads the official Python installer (.exe)
* Runs the installer interactively
* Recommendation: Check "Add Python to PATH" during installation

### Linux

* Auto-detects and uses mise or pyenv if available
* Falls back to system package managers (apt, yum, dnf)
* May require `sudo` privileges for apt/yum/dnf
* For Ubuntu/Debian: Uses deadsnakes PPA for latest versions
* Recommendation: Install mise or pyenv for easier version management

### macOS

* Auto-detects and uses mise or pyenv if available
### Check Your Setup

```bash9 or higher
* Internet connection
* Admin/sudo privileges (for some system package manager operations)
* Optional: textual package for TUI mode (`pip install textual`)

## Dependencies

### Core Dependencies (automatically installed)
* `requests` * HTTP library
* `beautifulsoup4` * HTML parsing
* `packaging` * Version comparison
* `click` * CLI framework

### Optional Dependencies
* `textual` * Terminal UI framework (for `pyvm tui` command)

## Command Reference

| Command | Description |
|---------|-------------|
| `pyvm` | Check Python version (default) |
| `pyvm check` | Check Python version |
| `pyvm tui` | Launch interactive TUI (NEW) |
| `pyvm list` | List available Python versions (NEW) |
| `pyvm list --all` | Show all versions including patches (NEW) |
| `pyvm install <version>` | Install specific Python version |
| `pyvm install <version> -y` | Install without confirmation |
| `pyvm rollback` | Rollback to previous Python state (NEW) |
| `pyvm rollback -y` | Rollback without confirmation (NEW) |
| `pyvm update` | Update Python to latest version |
| `pyvm update --version 3.11.5` | Update to a specific Python version |
| `pyvm update --auto` | Update without confirmation |
| `pyvm info` | Show system information |
| `pyvm --version` | Show tool version |
| `pyvm --help` | Show help message |

### TUI Keyboard Shortcuts

| Key | Action |
|-----|--------|
| **Tab** / **Shift+Tab** | Switch between panels |
| **Arrow Keys** | Navigate within panel |
| **Enter** | Install selected version |
| **1** / **2** | Jump to Installed / Available panel |
| **U** | Update to latest Python |
| **B** | Rollback last installation (NEW) |
| **X** | Remove selected version (NEW) |
| **R** | Refresh data |
| **T** | Toggle theme (dark/light) |
| **?** | Show help |
| **Q** | Quit

# Now you're using the new Python in this project
python --version           # Shows: Python 3.12.x
pip install -r requirements.txt

# Deactivate when done
deactivate
```

**Benefits:**
* Isolated dependencies per project
* No system modifications
* Easy to switch between Python versions
* No risk of breaking system tools

### Alternative: Direct Invocation

Always specify which version you want:

```bash
# Run scripts with new Python
python3.12 your_script.py

# Install packages for new Python
python3.12 -m pip install requests
```

### Option for Advanced Users: Change System Default

**Warning:** Only do this if you understand the risks!

Changing your system's default Python can break system tools. If you still want to proceed:

```bash
# Manually configure (at your own risk)
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 1
sudo update-alternatives --config python3
```

**We do NOT recommend this approach.** Virtual environments are much safer as they do not modify system defaults and prevent dependency conflicts.

### Windows: Using Multiple Python Versions

Windows Python Launcher (`py`) handles multiple versions automatically:

```bash
# Use specific version
py -3.14 your_script.py

# List all versions
py --list

# Set default in py.ini (optional)
# Create or edit: C:\Windows\py.ini
# Add: [defaults]
#      python=3.14
```

## Exit Codes

* `0` * Success or up-to-date
* `1` * Update available or error occurred
* `130` * Operation cancelled by user (Ctrl+C)

## Troubleshooting

### "externally-managed-environment" Error

**Error message:**
```
error: externally-managed-environment
× This environment is externally managed
```

This is a security feature on newer Linux systems (Ubuntu 23.04+, Debian 12+) that prevents breaking system Python packages.

**Solutions:**

**Option 1: Use `--user` flag (Recommended)**
```bash
pip install --user pyvm-updater
```

**Option 2: Use `pipx` (Best for CLI tools)**
```bash
# Install pipx first
sudo apt install pipx

# Install pyvm-updater with pipx
pipx install pyvm-updater
```

**Option 3: Use a virtual environment**
```bash
python3 -m venv myenv
source myenv/bin/activate
pip install pyvm-updater
```

**Option 4: Override (NOT recommended)**
```bash
pip install --break-system-packages pyvm-updater  # Not recommended
```

### "pyvm: command not found"

The installation directory is not in your PATH.

**If you installed with `pip install --user`:**
```bash
# Add to your ~/.bashrc or ~/.zshrc
export PATH="$HOME/.local/bin:$PATH"

# Then reload your shell
source ~/.bashrc  # or source ~/.zshrc
```

**If you installed with `pipx`:**
```bash
# Add pipx bin directory to PATH
pipx ensurepath

# Then restart your terminal OR reload:
source ~/.bashrc  # for bash
source ~/.zshrc   # for zsh
```

After running `pipx ensurepath`, you should see a message that PATH was updated. Restart your terminal to apply changes.

**Windows:**
* Add `C:\Users\YourName\AppData\Local\Programs\Python\Python3xx\Scripts` to PATH
* Or restart your terminal/command prompt

### "Already installed but still shows old version"

If you're using **Anaconda**, see the [Special Note for Anaconda Users](#️-special-note-for-anaconda-users) section above.

For regular users, check which Python is being used:
```bash
which python3      # Linux/macOS
where python       # Windows
```

### Installation fails with "File exists" error

This happens with Anaconda. Use this instead:
```bash
pip install --user .    # Instead of: pip install --user -e .
```

The difference:
* `pip install .` - Regular installation (recommended)
* `pip install -e .` - Editable/development mode (may conflict with Anaconda)

### Import errors

If you get import errors, install dependencies manually:
```bash
pip install requests beautifulsoup4 packaging click
```

### Permission errors (Linux/macOS)

Some operations require elevated privileges:
```bash
sudo pyvm update
```

### Windows installer issues

* Make sure you have administrator privileges
* Temporarily disable antivirus if installer is blocked
* Download manually from https://www.python.org/downloads/

### "Python updated but I still see the old version"

This is **normal**! The new Python is installed alongside your old version:

```bash
# Check all installed Python versions
ls /usr/bin/python*           # Linux/macOS
py --list                     # Windows

# Use the new version specifically
python3.14 --version          # Linux/macOS
py -3.14 --version           # Windows
```

**Want to make the new Python your default?** See the [Option for Advanced Users: Change System Default](#option-for-advanced-users-change-system-default) section.

## Development

```bash
# Clone the repository
git clone https://github.com/shreyasmene06/pyvm-updater.git
cd pyvm-updater

# Install in editable mode
pip install -e .

# Run tests (if available)
python -m pytest
```

### Running Tests

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=pyvm_updater

# Run specific test file
python -m pytest tests/test_specific.py
```

## Contributing

Contributions are welcome and appreciated. To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature-name`)
3. Make your changes and commit them with clear, descriptive messages
4. Write or update tests as needed
5. Ensure all tests pass
6. Push to your fork (`git push origin feature/your-feature-name`)
7. Open a Pull Request with a clear description of your changes

### Contribution Guidelines

* Follow PEP 8 style guidelines for Python code
* Add tests for new features
* Update documentation as needed
* Keep commits focused and atomic
* Write clear commit messages

For more details, see [CONTRIBUTING.md](CONTRIBUTING.md)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Shreyas Mene

## Disclaimer

This tool downloads and installs software from python.org. Always verify the authenticity of downloaded files. The authors are not responsible for any issues arising from Python installations.
