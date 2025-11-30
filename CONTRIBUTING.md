# Contributing to pyvm

Thanks for wanting to contribute! Here are some guidelines.

## Safety First

### Never add code that:

- Modifies `/usr/bin/python3` or system Python symlinks
- Uses `update-alternatives` to change system defaults
- Alters system PATH or shell configuration files
- Modifies conda/virtualenv environments
- Deletes or replaces existing Python installations
- Changes system-wide Python settings

### Always make sure your code:

- Only installs Python side-by-side with existing versions
- Respects the user's system configuration
- Provides clear instructions instead of automatic modifications
- Works well with virtual environments
- Has proper error handling and validation

## 📋 Development Setup

```bash
# Clone the repository
git clone https://github.com/shreyasmene06/pyvm-updater.git
cd pyvm-updater

# Install in development mode
pip install --user -e .

# Install development dependencies
pip install --user pytest pytest-cov black flake8 mypy
```

## 🧪 Testing

Before submitting a pull request:

```bash
# Check syntax
python3 -m py_compile python_version.py

# Run the tool locally
pyvm check
pyvm info

# Test that dangerous commands don't exist
pyvm set-default 2>&1 | grep -q "No such command" && echo "✓ Dangerous command properly removed"
```

## 📝 Code Style

- Follow PEP 8 guidelines
- Use type hints for function parameters and return values
- Add docstrings to all functions
- Keep functions focused and single-purpose
- Add comments for complex logic

```python
def example_function(param: str) -> bool:
    """
    Brief description of what the function does.
    
    Args:
        param: Description of parameter
        
    Returns:
        Description of return value
    """
    # Implementation
    pass
```

## Pull Request Process

1. Fork the repo and create your branch from `main`
2. Make your changes following the guidelines above
3. Test thoroughly on your platform
4. Update docs if needed
5. Commit with clear messages:
   ```
   fix: brief description of fix
   feat: brief description of new feature
   docs: brief description of documentation change
   ```
6. Submit PR with:
   - Clear description of what changed
   - Why you made the change
   - How you tested it
   - Screenshots if relevant

## Bug Reports

When reporting bugs, please include:

- OS and version: `uname -a` (Linux/macOS) or Windows version
- Python version: `python3 --version`
- pyvm version: `pyvm --version`
- Command used: Exact command that caused the issue
- Error output: Full error message and traceback
- Expected behavior: What should have happened

## Feature Requests

Before requesting features:

1. Make sure it fits with the tool's purpose (safe Python installation)
2. Check it doesn't violate safety guidelines
3. Describe your use case clearly
4. Explain why existing solutions don't work

## What We Won't Accept

- Features that modify system defaults automatically
- Code that requires root/admin for basic operations
- Platform-specific hacks that break other platforms
- Features that duplicate existing tools (like pyenv, conda)
- Code without proper error handling

## What We're Looking For

- Better error messages and user guidance
- Improved cross-platform compatibility
- Better detection of Python installations
- Documentation improvements
- Bug fixes with test cases
- Performance improvements

## 📚 Documentation

When updating documentation:

- Keep language clear and beginner-friendly
- Include code examples
- Add warnings for potentially dangerous operations
- Update all relevant docs (README, INSTALL, QUICKSTART, etc.)

## Security Issues

If you find a security vulnerability:

1. Don't open a public issue
2. Email the maintainer directly (check setup.py for email)
3. Describe the vulnerability and its impact
4. Give us time to fix it before public disclosure

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Thanks!

Thanks for helping make pyvm better and safer for everyone!

---

Remember: This tool's main goal is to safely install Python versions side-by-side. When in doubt, pick the safer option.
