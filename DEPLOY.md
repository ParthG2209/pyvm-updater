# Deployment Guide - Publishing to PyPI

## Prerequisites

1. Create accounts:
   - PyPI: https://pypi.org/account/register/
   - TestPyPI (for testing): https://test.pypi.org/account/register/

2. Install publishing tools:
```bash
pip install build twine
```

## Step 1: Prepare Your Package

Ensure all files are ready:
- [x] `setup.py` - Package configuration
- [x] `README.md` - Documentation
- [x] `LICENSE` - MIT License
- [x] `python_version.py` - Main code
- [x] Version number in `setup.py`

## Step 2: Build Distribution Files

```bash
cd /home/shreyasmene06/coding/sideProjects

# Clean previous builds
rm -rf build/ dist/ *.egg-info

# Build the package (use the venv python if needed)
python -m build
# OR if that fails:
# /home/shreyasmene06/coding/.venv/bin/python -m build
```

This creates:
- `dist/pyvm-updater-1.0.2.tar.gz` (source distribution)
- `dist/pyvm_updater-1.0.2-py3-none-any.whl` (wheel)

✅ **Build completed successfully!** Your packages are ready in the `dist/` folder.

## Step 3: Test on TestPyPI (Optional but Recommended)

```bash
# Upload to TestPyPI
python -m twine upload --repository testpypi dist/*

# Install from TestPyPI to test
pip install --index-url https://test.pypi.org/simple/ pyvm-updater
```

## Step 4: Upload to PyPI

```bash
# Upload to real PyPI
python -m twine upload dist/*
```

You'll be prompted for:
- Username: Your PyPI username
- Password: Your PyPI password or API token

## Step 5: Verify Installation

```bash
# Install from PyPI
pip install pyvm-updater

# Test it works
pyvm --version
pyvm check
```

## Using API Tokens (Recommended)

1. Go to PyPI Account Settings → API tokens
2. Create a new token with "Entire account" or project scope
3. Create `~/.pypirc`:

```ini
[pypi]
username = __token__
password = pypi-YOUR_API_TOKEN_HERE

[testpypi]
username = __token__
password = pypi-YOUR_TEST_API_TOKEN_HERE
```

Then upload with:
```bash
python -m twine upload dist/*
```

## Updating Your Package

1. Update version in `setup.py`:
```python
version="1.0.1",  # Increment version
```

2. Rebuild and upload:
```bash
rm -rf dist/ build/ *.egg-info
python -m build
python -m twine upload dist/*
```

## GitHub Release (Optional)

1. Create a new repository on GitHub
2. Push your code:
```bash
cd /home/shreyasmene06/coding/sideProjects
git init
git add .
git commit -m "Initial commit - Python Version Manager"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/pyvm-updater.git
git push -u origin main
```

3. Create a release tag:
```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

## Post-Publication

After publishing, users can install with:
```bash
pip install pyvm-updater
```

And use:
```bash
pyvm check
pyvm update
pyvm info
```

## Checklist Before Publishing

- [ ] All tests pass
- [ ] README is complete and accurate
- [ ] Version number is correct
- [ ] LICENSE file is included
- [ ] Dependencies are listed in `setup.py`
- [ ] Tested on multiple platforms (if possible)
- [ ] Documentation is clear
- [ ] Code is clean and commented

## Marketing Your Package

1. Add to README:
   - Badges (downloads, version, license)
   - Screenshots/GIFs
   - Clear installation instructions

2. Share on:
   - Reddit: r/Python
   - Twitter/X with #Python
   - Dev.to
   - Your blog

3. Update PyPI classifiers for better discoverability

## Common Issues

### "File already exists" error
You tried to upload the same version twice. Increment the version number.

### Import errors after installation
Check that entry points in `setup.py` are correct.

### "Invalid package" error
Ensure `setup.py` is properly formatted and all required fields are present.

## Useful Commands

```bash
# Check package metadata
python setup.py check

# View package info
pip show pyvm-updater

# Uninstall
pip uninstall pyvm-updater

# Install in development mode
pip install -e .
```

## Resources

- PyPI Documentation: https://packaging.python.org/
- Twine Docs: https://twine.readthedocs.io/
- Python Packaging Guide: https://packaging.python.org/tutorials/packaging-projects/
- Semantic Versioning: https://semver.org/

---

Good luck with your package! 🚀
