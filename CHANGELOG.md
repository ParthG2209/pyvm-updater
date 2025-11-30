# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.1] - 2025-11-30 🚨 CRITICAL SECURITY FIX

### 🚨 BREAKING CHANGES
- **REMOVED**: `pyvm set-default` command (was causing system crashes)
- **REMOVED**: `--set-default` flag from `pyvm update` command
- **CHANGED**: Tool now ONLY installs Python side-by-side, never modifies system defaults

### Fixed (Critical)
- **System freeze issue**: Removed all code that modified `/usr/bin/python3` symlink via `update-alternatives`
- **Terminal crashes**: Eliminated dangerous system Python default modification that broke package managers
- **System GUI failures**: Removed code that could prevent system settings from opening
- **Package manager corruption**: No longer touches system Python configuration

### Removed
- `_set_python_default_linux()` function (~150 lines of dangerous code)
- `prompt_set_as_default()` function
- `_show_access_instructions()` function (replaced with safe version)
- `pyvm set-default` CLI command
- `--set-default` flag from update command

### Added
- `show_python_usage_instructions()` - Safe, read-only instruction display
- Comprehensive safety documentation (`CRITICAL_SECURITY_FIX_v1.2.1.md`)
- Clear warnings in README about safe behavior
- Instructions for using Python via virtual environments (recommended approach)

### Changed
- `update_python_linux()` now only installs Python, never modifies system defaults
- All docstrings updated to clarify safe, non-invasive behavior
- CLI help text updated to emphasize safety
- Tool version bumped to 1.2.1

### Documentation
- Added `CRITICAL_SECURITY_FIX_v1.2.1.md` with recovery instructions
- Updated README with prominent safety warning
- Added `QUICK_REFERENCE.md` for quick command comparison
- Updated all examples to show safe usage patterns

**Migration Guide**: If you were using `pyvm set-default`, switch to virtual environments:
```bash
python3.12 -m venv myproject
source myproject/bin/activate
```

**For Affected Users**: See `CRITICAL_SECURITY_FIX_v1.2.1.md` for system recovery instructions.

---

## [1.2.0] - 2024-11-09 ⚠️ DEPRECATED - Contains System-Breaking Code

### Added
- **`--set-default` flag**: New option for `pyvm update --set-default` to automatically set the newly installed Python as system default (Linux only)
- **`pyvm set-default` command**: Standalone command to manage Python versions
  - `pyvm set-default` - Lists all available Python versions on the system
  - `pyvm set-default 3.12` - Sets a specific version as system default
- **Automatic version detection**: Automatically finds and registers existing Python installations
- **Installation verification**: Verifies Python installation after update and shows the path
- **Additional packages**: Now installs `python3.x-venv` and `python3.x-distutils` for complete setup on Ubuntu/Debian

### Changed
- **Improved `update-alternatives` setup**: Now automatically configures both old and new Python versions with proper priorities
- **Better default setting**: Uses `update-alternatives --set` for immediate effect without user interaction
- **Enhanced verification**: After setting default, automatically verifies with `python3 --version`
- **More robust path detection**: Checks both `/usr/bin` and `/usr/local/bin` for Python installations
- **Improved error messages**: Clearer feedback when Python version not found or commands fail

### Fixed
- **Linux default Python issue**: Fixed the core issue where installed Python wasn't being set as system default
- **Hardcoded version bug**: Removed hardcoded Python 3.12 reference in `_set_python_default_linux()`
- **PATH issues for non-Anaconda users**: Now properly sets up system-wide Python access for users without Anaconda
- **Better handling of existing alternatives**: Intelligently detects and manages existing Python alternatives

### Documentation
- Updated README with new commands and flags
- Added examples for `--set-default` flag usage
- Enhanced "Making Updated Python the Default" section
- Updated commands reference table with new options
- Added feature list highlighting new capabilities

## [1.1.0] - 2024-11-09

### Added
- **Interactive prompt after update**: Users are now asked if they want to set the new Python as their system default
- **Automatic setup instructions**: If users decline to set as default, they get clear instructions on how to access the new Python version
- **Platform-specific guidance**: Different instructions for Linux, macOS, and Windows
- **Linux default setter**: On Linux, provides commands to set Python as default using `update-alternatives`
- Enhanced documentation for multiple Python versions and PATH setup
- Added pipx installation method to README
- Comprehensive troubleshooting for PEP 668 "externally-managed-environment" errors

### Changed
- Update process now provides better user experience with clear next steps
- Improved documentation structure with Quick Start section
- Updated installation instructions for modern Python environments
- Enhanced README with Anaconda user guidance

### Fixed
- Better handling of multiple Python versions on the same system
- Clearer communication about why default Python might not change after update

## [1.0.2] - 2024-11-08

### Fixed
- Fixed type checking issue with `ctypes.windll` on Windows platform (added type ignore comment)
- Fixed BeautifulSoup attribute type handling for download URL extraction
- Improved type safety by properly casting BeautifulSoup `.get()` return values to strings
- Enhanced error handling for download URL processing

### Changed
- Updated author information in setup.py
- Added .gitignore file for better repository management

## [1.0.1] - Previous Release

### Added
- Cross-platform Python version checking
- Automatic Python updates for Windows, Linux, and macOS
- CLI interface with click
- System information display
- Comprehensive documentation

## [1.0.0] - Initial Release

### Added
- Initial release of Python Version Manager
- Support for Windows, Linux, and macOS
- Version checking against python.org
- Automated installation features
