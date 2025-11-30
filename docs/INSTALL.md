# Installation Guide - Python Version Manager

## 🚀 Quick Install (For New Users)

### Step 1: Get the Code from GitHub

```bash
# Clone the repository
git clone https://github.com/shreyasmene06/pyvm-updater.git

# Navigate to the project
cd pyvm-updater
```

### Step 2: Pre-Installation Check (Optional but Recommended)
```bash
python3 check_requirements.py
```

This will verify:
- ✓ Python version (3.7+ required)
- ✓ pip is installed
- ✓ Internet connectivity
- ✓ Operating system support
- ✓ Installation permissions
- ✓ Existing dependencies

### Step 3: Install the Tool

**Option A: User Install (Recommended - No sudo required)**
```bash
pip install --user .
```

**Option B: System-wide Install**
```bash
sudo pip install .
```

**Option C: Development Install (For contributors only)**
```bash
pip install --user -e .
```

**⚠️ Note for Anaconda Users:** If you get a "File exists" error with option C, use option A instead.

### Step 4: Verify Installation
```bash
pyvm --version
pyvm check
```

If you see "command not found", add `~/.local/bin` to your PATH:
```bash
export PATH="$HOME/.local/bin:$PATH"
```

---

## 📦 Dependencies

All dependencies are automatically installed via `setup.py`:

- `requests>=2.25.0` - HTTP requests for downloading Python info
- `beautifulsoup4>=4.9.0` - HTML parsing for Python.org
- `packaging>=20.0` - Version comparison
- `click>=8.0.0` - CLI framework

---

## 🔧 Manual Dependency Installation (If Needed)

If automatic installation fails:

```bash
pip install requests beautifulsoup4 packaging click
```

Or use the included install scripts:

**Linux/macOS:**
```bash
bash install.sh
```

**Windows:**
```cmd
install.bat
```

---

## � Special Instructions for Anaconda/Miniconda Users

If you're using Anaconda or Miniconda, follow these special instructions:

### Installation
```bash
# Use regular install (NOT editable mode)
pip install --user .
```

**Do NOT use:**
```bash
pip install --user -e .  # ❌ This may cause "File exists" errors with Anaconda
```

### After Installation

The `pyvm` tool will work, but keep in mind:
- ✅ `pyvm check` - Will show your Anaconda Python version
- ✅ `pyvm update` - Will install the latest Python to your system
- ⚠️ Your Anaconda Python version won't change (this is expected!)

### Understanding the Results

```bash
# Your Anaconda Python (unchanged)
python --version
# Output: Python 3.13.5 (or whatever Anaconda version you have)

# The newly installed system Python
python3.14 --version
# Output: Python 3.14.0
```

### How to Use the Updated Python

**Option 1: Use it directly**
```bash
python3.14 your_script.py
```

**Option 2: Create a virtual environment**
```bash
python3.14 -m venv myproject
source myproject/bin/activate
python --version  # Now shows 3.14.0
```

**Option 3: Continue using Anaconda (Recommended for data science)**
```bash
# Your Anaconda environment works normally
conda activate myenv
python your_script.py
```

### Why This Happens

Anaconda maintains its own Python installation separate from system Python. When you update Python with `pyvm`, it updates the system Python, not your Anaconda installation. This is actually beneficial because:
- ✅ Prevents conflicts between Anaconda and system packages
- ✅ Keeps your Anaconda environment stable
- ✅ Gives you both options available

---

## �🖥️ Platform-Specific Notes

### Windows
- No additional requirements
- Installer will be downloaded and launched
- **Tip**: Run as Administrator for system-wide installation

### Linux (Ubuntu/Debian)
- Uses `apt` package manager
- Adds `deadsnakes/ppa` for latest Python versions
- **Requires**: `sudo` privileges for installation
- **Alternative**: Use `pyenv` for user-level installations

### Linux (Fedora/RHEL/CentOS)
- Uses `dnf` or `yum` package manager
- May not have latest Python versions
- **Recommended**: Use `pyenv` for version-specific installs

### macOS
- **With Homebrew** (Recommended):
  - Automatic updates via `brew upgrade python3`
- **Without Homebrew**:
  - Downloads official installer from Python.org
  - Manual installation required

---

## 🧪 Testing Your Installation

```bash
# Check current Python version
pyvm check

# Show system information
pyvm info

# Check for updates (safe, won't install)
pyvm update

# Update Python (with confirmation prompt)
pyvm update

# Update Python (automatic, no prompt)
pyvm update --auto
```

---

## 🔍 Troubleshooting

### "Command not found: pyvm"

**Fix 1**: Ensure pip install location is in PATH
```bash
# Check where pyvm is installed
pip show -f pyvm-updater

# Add to PATH (Linux/macOS - add to ~/.bashrc or ~/.zshrc)
export PATH="$HOME/.local/bin:$PATH"

# Add to PATH (Windows)
# Control Panel → System → Advanced → Environment Variables
# Add: C:\Users\YourName\AppData\Local\Programs\Python\Python3X\Scripts
```

**Fix 2**: Use Python module syntax
```bash
python -m python_version check
```

### "ImportError: No module named 'click'"

Dependencies weren't installed. Run:
```bash
pip install -e .
```

Or manually:
```bash
pip install requests beautifulsoup4 packaging click
```

### "Permission denied" errors on Linux

Use user install instead:
```bash
pip install --user -e .
```

### Network/SSL errors

Update pip and certificates:
```bash
pip install --upgrade pip certifi
```

### Version mismatch after update

The tool updates Python system-wide, but your current terminal may still use the old version.

**Solution**: Restart your terminal/IDE or run:
```bash
hash -r  # Bash/Zsh
rehash   # Tcsh
```

---

## 🔄 Updating the Tool Itself

```bash
cd /home/shreyasmene06/coding/sideProjects
git pull  # If using git
pip install --upgrade -e .
```

---

## 🗑️ Uninstallation

```bash
pip uninstall pyvm-updater
```

---

## 📚 Usage Examples

### Check version only
```bash
pyvm check
# Exit code 0 = up-to-date
# Exit code 1 = update available
```

### Automated update in scripts
```bash
#!/bin/bash
if ! pyvm check; then
    echo "Update available!"
    pyvm update --auto
fi
```

### Show detailed system info
```bash
pyvm info
```

---

## 🛡️ Security Notes

1. **Always verify**: This tool downloads from python.org (official source)
2. **Admin required**: Updates require sudo/admin on most systems
3. **Manual verification**: Review installer prompts before proceeding
4. **PPA trust**: Linux users should trust the deadsnakes PPA

---

## 🆘 Getting Help

1. Check `SECURITY_FIXES.md` for known issues and fixes
2. Run pre-installation checker: `python3 check_requirements.py`
3. Enable verbose mode (if available): `pyvm --verbose check`
4. Check logs in terminal output

---

## ✅ Post-Installation Checklist

- [ ] `pyvm --version` works
- [ ] `pyvm check` shows current version
- [ ] Internet connectivity confirmed
- [ ] Admin/sudo available (if needed)
- [ ] PATH configured correctly
- [ ] All dependencies installed

---

## 🎯 Next Steps

After successful installation:

1. **Check your version**: `pyvm check`
2. **Update if needed**: `pyvm update`
3. **Restart terminal/IDE** to use new Python version
4. **Verify update**: `python --version`

**Enjoy your updated Python! 🐍**
