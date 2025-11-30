# Quick Reference - v1.2.1 Changes

## TL;DR

v1.2.0 was breaking Linux systems. v1.2.1 is safe.

All system-modifying code removed. The tool now only installs Python, never changes defaults.

---

## What Was Removed

| Feature | Why It Was Dangerous | Status |
|---------|---------------------|--------|
| `pyvm set-default` command | Modified `/usr/bin/python3`, broke system tools | ❌ REMOVED |
| `--set-default` flag | Automatically changed system Python | ❌ REMOVED |
| `_set_python_default_linux()` | Used `update-alternatives`, froze terminals | ❌ REMOVED |
| `prompt_set_as_default()` | Asked user to break their system | ❌ REMOVED |

---

## What Changed

### Before (v1.2.0 - DANGEROUS)

```bash
pyvm update --set-default
# Would install Python AND change system default
# Result: System freeze, broken package manager, unusable GUI
```

### After (v1.2.1 - SAFE)

```bash
pyvm update
# Installs Python side-by-side, system unchanged
# Result: New Python available as python3.12, old Python still works
```

---

## How to Use Now

### ✅ Recommended: Virtual Environments

```bash
python3.12 -m venv myproject
source myproject/bin/activate
# Now using Python 3.12 in this project only
```

### ✅ Alternative: Direct Commands

```bash
python3.12 your_script.py
python3.12 -m pip install requests
```

### ⚠️ Not Recommended: Manual System Change

```bash
# If you REALLY want to (at your own risk):
sudo update-alternatives --config python3
```

---

## File Changes

| File | Changes |
|------|---------|
| `python_version.py` | Removed 400+ lines of dangerous code |
| `setup.py` | Version 1.2.0 → 1.2.1 |
| `README.md` | Added warning, updated examples |
| `CRITICAL_SECURITY_FIX_v1.2.1.md` | NEW - Full fix documentation |
| `CHANGELOG_v1.2.1.md` | NEW - Detailed changelog |
| `FIXES_SUMMARY.md` | NEW - Summary of fixes |

---

## Commands Comparison

| Command | v1.2.0 | v1.2.1 |
|---------|--------|--------|
| `pyvm check` | ✅ Safe | ✅ Safe |
| `pyvm update` | ⚠️ Could break system with `--set-default` | ✅ Safe, installs side-by-side only |
| `pyvm set-default` | ❌ DANGEROUS | ❌ Removed |
| `pyvm info` | ✅ Safe | ✅ Safe |
| `pyvm --version` | Shows 1.2.0 | Shows 1.2.1 |

---

## Quick Install

```bash
cd /home/shreyas/pyvm-updater
git pull
pip install --user -e .
pyvm --version  # Should show 1.2.1
```

---

## Quick Test

```bash
# This should fail (command removed):
pyvm set-default
# Expected: "Error: No such command 'set-default'"

# This should work:
pyvm check
# Expected: Shows Python version comparison

# This should work:
pyvm update --help
# Expected: Only shows --auto flag, NOT --set-default
```

---

## Check Your System

Make sure everything is working correctly:

```bash
# Your system Python should be unchanged:
python3 --version
# Should show your original version (e.g., 3.10.12)

# New Python should be available separately:
python3.12 --version  # or whatever version you installed
# Should show new version (e.g., 3.12.x)

# Both should exist if you installed 3.12:
which python3       # /usr/bin/python3
which python3.12    # /usr/bin/python3.12

# Check they're different:
ls -la /usr/bin/python3*
```

---

## What the Tool Does Now

1. ✅ Check version (read-only)
2. ✅ Download Python installer
3. ✅ Install Python side-by-side
4. ✅ Show usage instructions
5. ❌ ~~Change system defaults~~ (REMOVED)
6. ❌ ~~Modify symlinks~~ (REMOVED)
7. ❌ ~~Run update-alternatives~~ (REMOVED)

---

## Need Help?

- Full docs: `CRITICAL_SECURITY_FIX_v1.2.1.md`
- Changelog: Main `CHANGELOG.md`
- Summary: `FIXES_SUMMARY.md`
- Issues: Open an issue on GitHub

---

Updated: 2025-11-30
Version: 1.2.1
Status: Safe to use
