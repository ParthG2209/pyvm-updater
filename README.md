# Python Version Manager (pyvm)

A cross-platform CLI tool to check and install the latest Python version **side-by-side** with your existing Python.

## 🚨 CRITICAL UPDATE (v1.2.1)

**If you're using v1.2.0 or earlier:** Please update immediately!

Previous versions contained system-breaking code that could freeze Linux systems. **v1.2.1 is completely safe** - it only installs Python, never modifies system defaults.

```bash
# Update to the safe version
cd pyvm-updater
git pull
pip install --user -e .
```

See [docs/CRITICAL_SECURITY_FIX_v1.2.1.md](docs/CRITICAL_SECURITY_FIX_v1.2.1.md) for details and recovery instructions.

📚 **Documentation**: [Installation Guide](docs/INSTALL.md) | [Quick Start](docs/QUICKSTART.md) | [Quick Reference](docs/QUICK_REFERENCE.md)

---

## ⚡ Quick Start (3 Steps)

```bash
# 1. Install the package
pip install --user pyvm-updater

# 2. Use it!
pyvm check      # Check your Python version
pyvm update     # Update to latest Python
```

That's it! 🎉

---

## Features

- ✅ Check your current Python version against the latest stable release
- 🔄 Install the latest Python side-by-side with your existing version
- 🖥️ Cross-platform support (Windows, Linux, macOS)
- 📊 Detailed system information display
- 🚀 Simple and intuitive CLI interface
- 🛡️ **SAFE:** Never modifies your system Python defaults
- 🔧 Multiple Python versions coexist peacefully
- 📚 Clear instructions on how to use the new version

## 🚀 Quick Start for New Users

### Step 1: Get the Code

```bash
# Clone from GitHub
git clone https://github.com/shreyasmene06/pyvm-updater.git
cd pyvm-updater
```

### Step 2: Install

```bash
# Install with pip (recommended)
pip install --user .
```

That's it! All dependencies are automatically installed. 🎉

### Step 3: Verify Installation

```bash
# Check if it works
pyvm --version
pyvm check
```

---

## Installation Methods

### Method 1: Install from GitHub (For New Users)

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

**Note for Linux users:** On newer systems (Ubuntu 23.04+, Debian 12+), use `--user` flag or see [troubleshooting](#-troubleshooting) if you get "externally-managed-environment" error.

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

**Why pipx?** It automatically manages virtual environments for CLI tools, preventing conflicts.

### Method 3: Install from source (For Developers)

```bash
# Clone the repository
git clone https://github.com/shreyasmene06/pyvm-updater.git
cd pyvm-updater

# Optional: Check system requirements first
python3 check_requirements.py

# Install in editable mode
pip install --user .
```

**Note:** If you get permission errors, use `pip install --user .` instead of `pip install .`

This will automatically install all required dependencies:
- requests
- beautifulsoup4
- packaging
- click

The `pyvm` command will be available globally after installation.

---

## ⚠️ Special Note for Anaconda Users

If you're using **Anaconda/Miniconda**, the `pyvm update` command will install the latest Python to your system, but your Anaconda environment will continue using its own Python version. This is expected behavior!

**How to check:**
```bash
# Your Anaconda Python (won't change)
python --version

# The newly installed system Python
python3.14 --version  # (or whatever the latest version is)
```

**To use the updated Python:**
1. Use it directly: `python3.14 your_script.py`
2. Create a new environment: `python3.14 -m venv myenv`
3. Or continue using Anaconda (recommended for data science work)

**Why does this happen?**
Anaconda manages its own Python installation separately from system Python. This is actually good because it prevents conflicts between your Anaconda packages and system packages.

---

**For detailed installation instructions, see [INSTALL.md](INSTALL.md)**

## 📖 Usage

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
     Python Version Check Report
========================================
Your version:   3.12.3
Latest version: 3.14.0
========================================
⚠ A new version (3.14.0) is available!

💡 Tip: Run 'pyvm update' to upgrade Python
```

### Update Python

Update to the latest version:

```bash
pyvm update
```

For automatic installation without confirmation:

```bash
pyvm update --auto
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

Admin/Sudo:       No
==================================================
```

### Show tool version

```bash
pyvm --version
```

---

## 🔄 Using Your New Python Version

After installation, you have **multiple Python versions** side-by-side. Here's how to use them effectively:

### Check Your Setup

```bash
# Your system Python (unchanged)
python3 --version          # Shows: Python 3.10.x

# Your new Python (side-by-side)
python3.12 --version       # Shows: Python 3.12.x

# See all installed versions
ls /usr/bin/python* | grep -E 'python[0-9]'
```

### Best Practice: Use Virtual Environments (Recommended)

This is the safest and most flexible approach:

```bash
# Create project with new Python
python3.12 -m venv myproject
source myproject/bin/activate

# Now you're using the new Python in this project
python --version           # Shows: Python 3.12.x
pip install -r requirements.txt

# Deactivate when done
deactivate
```

**Benefits:**
- ✅ Isolated dependencies per project
- ✅ No system modifications
- ✅ Easy to switch between Python versions
- ✅ No risk of breaking system tools

### Alternative: Direct Invocation

Always specify which version you want:

```bash
# Run scripts with new Python
python3.12 your_script.py

# Install packages for new Python
python3.12 -m pip install requests
```

### Option for Advanced Users: Change System Default

⚠️ **Warning:** Only do this if you understand the risks!

Changing your system's default Python can break system tools. If you still want to:

```bash
# Manually configure (at your own risk)
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 1
sudo update-alternatives --config python3
```

**We do NOT recommend this approach.** Virtual environments are much safer.

This is the **safest approach** as it doesn't change system behavior.

### For Windows Users

Windows Python Launcher (`py`) handles multiple versions automatically:

```bash
# Use specific version
py -3.14 your_script.py

# List all versions
py --list

# Set default in py.ini (optional)
# Create/edit: C:\Windows\py.ini
# Add: [defaults]
#      python=3.14
```

---

## Platform-Specific Notes

### Windows
- Downloads the official Python installer (.exe)
- Runs the installer interactively
- **Recommendation**: Check "Add Python to PATH" during installation

### Linux
- Uses system package managers (apt, yum, dnf)
- May require `sudo` privileges
- For Ubuntu/Debian: Uses deadsnakes PPA for latest versions
- **Alternative**: Install pyenv for easier version management

### macOS
- Uses Homebrew if available
- Falls back to official installer download link
- Run `brew install python@3.x` for Homebrew installation

## Requirements

- Python 3.7 or higher
- Internet connection
- Admin/sudo privileges (for updates on some systems)

## Dependencies

- `requests` - HTTP library
- `beautifulsoup4` - HTML parsing
- `packaging` - Version comparison
- `click` - CLI framework

## Commands Reference

| Command | Description |
|---------|-------------|
| `pyvm` | Check Python version (default) |
| `pyvm check` | Check Python version |
| `pyvm update` | Update Python to latest version |
| `pyvm update --auto` | Update without confirmation |
| `pyvm update --set-default` | Update and set as system default (Linux) |
| `pyvm update --auto --set-default` | Fully automated update and setup (Linux) |
| `pyvm set-default` | List available Python versions (Linux) |
| `pyvm set-default 3.12` | Set Python 3.12 as system default (Linux) |
| `pyvm info` | Show system information |
| `pyvm --version` | Show tool version |
| `pyvm --help` | Show help message |

## Exit Codes

- `0` - Success or up-to-date
- `1` - Update available or error occurred
- `130` - Operation cancelled by user (Ctrl+C)

## 🔧 Troubleshooting

### "externally-managed-environment" error

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
pip install --break-system-packages pyvm-updater  # ⚠️ Not recommended
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
- Add `C:\Users\YourName\AppData\Local\Programs\Python\Python3xx\Scripts` to PATH
- Or restart your terminal/command prompt

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
- `pip install .` - Regular installation (recommended)
- `pip install -e .` - Editable/development mode (may conflict with Anaconda)

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
- Make sure you have administrator privileges
- Temporarily disable antivirus if installer is blocked
- Download manually from https://www.python.org/downloads/

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

**Want to make the new Python your default?** See the detailed guide: [Making Updated Python the Default](#-making-updated-python-the-default)

## Development

To set up for development:

```bash
# Clone or navigate to the project
cd /home/shreyasmene06/coding/sideProjects

# Install in editable mode
pip install -e .

# Run tests (if available)
python -m pytest
```

## License

MIT License - Feel free to use and modify

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Created with ❤️ for the Python community

## Disclaimer

This tool downloads and installs software from python.org. Always verify the authenticity of downloaded files. The authors are not responsible for any issues arising from Python installations.
