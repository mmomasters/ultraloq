# Ultraloq Project - Deployment Guide

This guide explains how to set up and deploy the Ultraloq lock status checker to run remotely via SSH.

## Project Overview

This project uses the UtecIO library to interact with Ultraloq BLE locks. It allows you to check lock status, battery level, and other lock information remotely.

Based on the original project: https://github.com/mmomasters/ultraloq

## Prerequisites

### Local Machine
- Git
- SSH client
- Bash shell (Git Bash on Windows, native on Linux/Mac)

### Remote Machine (e.g., Raspberry Pi)
- Python 3.7 or higher
- pip (Python package manager)
- Bluetooth support (for BLE communication)
- SSH access enabled

## Project Structure

```
ultraloq/
├── utecio/              # Core library for Ultraloq communication
│   ├── api.py          # API client for Utec cloud
│   ├── const.py        # Constants
│   ├── enums.py        # Enumerations
│   ├── util.py         # Utilities
│   ├── ble/            # Bluetooth Low Energy modules
│   │   ├── device.py   # BLE device handling
│   │   └── lock.py     # Lock-specific BLE operations
├── check_lock_status.py # Main script to check lock status
├── config.py           # Configuration file (credentials)
├── requirements.txt    # Python dependencies
├── deploy_ssh.sh       # Script to deploy to remote host
├── run_remote.sh       # Script to run remotely
└── DEPLOYMENT.md       # This file
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/mmomasters/ultraloq.git
cd ultraloq
```

### 2. Configure Credentials

Edit `config.py` with your Utec app credentials:

```python
EMAIL = "your@email.com"      # Your Utec app username/email
PASSWORD = "your_password"     # Your Utec App password
LOCK_NAME = "UL3-2ND"         # Your lock's name from the app
```

**⚠️ IMPORTANT: Never commit config.py with real credentials to version control!**

### 3. Deploy to Remote Host

Use the deployment script to copy files and install dependencies on your remote host:

```bash
chmod +x deploy_ssh.sh
./deploy_ssh.sh user@hostname /path/to/remote/directory
```

Example for Raspberry Pi:
```bash
./deploy_ssh.sh pi@192.168.1.100 /home/pi/ultraloq
```

The script will:
- Create the remote directory
- Copy all necessary files (utecio library, check script, config, requirements)
- Install Python dependencies
- Display instructions for final configuration

### 4. Update Remote Configuration

SSH into your remote host and edit the config file:

```bash
ssh user@hostname
nano /path/to/remote/directory/config.py
```

Update with your actual credentials and lock name.

### 5. Run the Lock Status Check

#### Option A: Run Locally (if on remote host)
```bash
ssh user@hostname
cd /path/to/remote/directory
python3 check_lock_status.py
```

#### Option B: Run Remotely from Your Local Machine
```bash
chmod +x run_remote.sh
./run_remote.sh user@hostname /path/to/remote/directory
```

Example:
```bash
./run_remote.sh pi@192.168.1.100 /home/pi/ultraloq
```

## Expected Output

When the script runs successfully, you should see output like:

```
Lock Status: locked
Bolt Status: engaged
Battery: 85
Lock Mode: normal
Mute: False
Autolock Time: 30
```

## Troubleshooting

### Bluetooth Issues
- Ensure your remote device has Bluetooth enabled
- The device must be within BLE range of the lock
- On Linux, you may need to run with sudo or add user to bluetooth group

### Connection Issues
- Verify your Utec app credentials are correct
- Check internet connection on remote host (needed for API access)
- Ensure the lock name matches exactly as shown in the Utec app

### Dependencies
If installation fails, manually install on remote host:
```bash
pip3 install ecdsa bleak pycryptodome aiohttp bleak_retry_connector
```

### SSH Issues
- Verify SSH access: `ssh user@hostname`
- Check SSH key authentication or use password
- Ensure remote path exists and user has write permissions

## Security Notes

1. **Credentials**: Never commit `config.py` with real credentials
2. **SSH Keys**: Use SSH key authentication instead of passwords
3. **File Permissions**: Restrict access to config.py on remote host:
   ```bash
   chmod 600 config.py
   ```

## Automation

To run checks automatically, set up a cron job on the remote host:

```bash
# Edit crontab
crontab -e

# Add line to check every hour
0 * * * * cd /path/to/ultraloq && python3 check_lock_status.py >> /var/log/ultraloq.log 2>&1
```

## Development

### Local Testing
To test locally before deployment:

```bash
cd ultraloq
pip install -r requirements.txt
python check_lock_status.py
```

### Dependencies
See `requirements.txt` for the full list of Python packages.

## License

See LICENSE file for details.

## Credits

- Original project: https://github.com/mmomasters/ultraloq
- UtecIO library by maeneak

## Support

For issues with:
- The library: https://github.com/maeneak/utecio/issues
- This deployment: Create an issue in the project repository
