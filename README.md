# UtecIO Python Library

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-0.1.2-green.svg)](https://github.com/maeneak/utecio)

Python library for interacting with Utec devices and Ultraloq smart locks using both Cloud API and Bluetooth Low Energy (BLE).

> ⚠️ **Status:** This library is in active development and the API may change rapidly. Contributions and feedback are welcome!

## Features

- 🔐 **Dual Control Methods**: Cloud API and direct BLE connectivity
- 🔄 **Lock Control**: Lock, unlock, and status monitoring
- 📊 **Device Information**: Battery level, WiFi/BLE strength, firmware version
- 🏠 **Multi-Device Support**: Manage multiple locks and locations
- 🔌 **Offline Capable**: BLE works without internet connection
- 📦 **Easy Integration**: Simple async Python API

## Supported Devices

The library supports a wide range of Ultraloq lock models:

- **Latch 5** (Fingerprint & NFC variants)
- **UL1** Smart Lock
- **Bolt** Series (NFC, WiFi, Z-Wave variants)
- **UBolt** Series
- **Lever** Smart Lock
- **UL3** Smart Lock (including 2nd generation)
- **UL300** Smart Lock
- And more...

## Installation

### From PyPI (recommended)
```bash
pip install utecio
```

### From Source
```bash
git clone https://github.com/maeneak/utecio.git
cd utecio
pip install -r requirements.txt
```

### Development Installation
```bash
git clone https://github.com/maeneak/utecio.git
cd utecio
pip install -e .
```

## Quick Start

### Using Cloud API

```python
import asyncio
from utecio.api import UtecClient

async def main():
    # Initialize client
    client = UtecClient(email="your@email.com", password="your_password")
    
    # Connect and sync devices
    await client.connect()
    locks = await client.get_ble_devices()
    
    # Access lock information
    for lock in locks:
        print(f"Lock: {lock.name}")
        print(f"Status: {lock.lock_status}")
        print(f"Battery: {lock.battery_level}")

asyncio.run(main())
```

### Using BLE Direct Control

```python
import asyncio
from utecio.ble.lock import UtecBleLock

async def main():
    # Create lock instance
    lock = UtecBleLock(
        name="Front Door",
        mac_address="AA:BB:CC:DD:EE:FF",
        api_key="your_api_key"
    )
    
    # Connect and control
    await lock.connect()
    await lock.unlock()
    await lock.disconnect()

asyncio.run(main())
```

## Configuration

Create a `config.py` file in your project:

```python
EMAIL = "your@email.com"
PASSWORD = "your_password"
LOCK_NAME = "Your Lock Name"  # Optional: specific lock to control
```

## Usage Examples

The repository includes ready-to-use scripts:

### 1. Check Lock Status via API
```bash
python api_status.py
```
- Always works remotely
- No proximity required
- Shows battery, WiFi/BLE strength, firmware

### 2. Direct BLE Control
```bash
python ble_control.py status   # Check status via BLE
python ble_control.py unlock   # Unlock via BLE
python ble_control.py lock     # Lock via BLE
```
- Local control (no internet needed)
- Faster response time
- Requires proximity (~10m)

### 3. Combined Status Check
```bash
python check_lock_status.py
```
- API status + BLE connection test

## BLE Connection Tips

Ultraloq locks use power-saving mode which can affect BLE connectivity:

- 🔋 **Wake the lock**: Touch the keypad before BLE commands
- 📱 **Bridge interference**: Utec bridges may hold BLE connections
- 📏 **Range**: Stay within ~10 meters of the lock
- ⚡ **Active mode**: BLE works best when lock is recently used

## Documentation

- [Usage Guide](USAGE.md) - Detailed script usage and examples
- [Deployment Guide](DEPLOYMENT.md) - Remote deployment instructions
- [API Documentation](https://github.com/maeneak/utecio/wiki) - Full API reference

## Requirements

- Python 3.7+
- Dependencies:
  - `bleak` - BLE communication
  - `aiohttp` - Async HTTP client
  - `pycryptodome` - Encryption
  - `ecdsa` - Cryptographic signatures
  - `bleak_retry_connector` - BLE reliability

## Contributing

Contributions are welcome! Whether it's:

- 🐛 Bug reports
- 💡 Feature requests
- 📝 Documentation improvements
- 🔧 Code contributions

Please open an issue or submit a pull request.

### Testing New Lock Models

If you have a specific Ultraloq lock model that needs testing or support, you can help accelerate development:

- [Buy Me a Coffee](https://www.buymeacoffee.com/maeneak)
- [Coindrop](https://coindrop.to/maeneak)

Contributions help with purchasing new locks for testing and development.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This is an unofficial library and is not affiliated with or endorsed by Ultraloq or U-tec. Use at your own risk.

## Support

- 🐛 [Report Issues](https://github.com/maeneak/utecio/issues)
- 💬 [Discussions](https://github.com/maeneak/utecio/discussions)
- 📧 Check repository for contact information

## Acknowledgments

Built with love for the smart home community. Special thanks to all contributors and testers who help make this library better!

---

**Happy Locking! 🔐**
