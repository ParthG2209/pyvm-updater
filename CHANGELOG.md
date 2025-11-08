# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
