# Ultraloq Lock Control Scripts

This repository contains scripts to monitor and control Ultraloq smart locks via two methods:

## Scripts Overview

### 1. `api_status.py` - Cloud API Status Check
**What it does:** Checks lock status via Utec cloud API (internet required)
**Advantages:** Always works, no proximity needed, no BLE connection required
**Usage:**
```bash
python api_status.py
```
**Output:** Lock status, battery level, WiFi/BLE strength, firmware version

### 2. `ble_control.py` - Direct Bluetooth Control
**What it does:** Controls lock directly via Bluetooth Low Energy
**Advantages:** Local control, faster response, works offline
**Requirements:** Within BLE range (~10m), lock must be awake
**Usage:**
```bash
python ble_control.py status  # Check status via BLE
python ble_control.py unlock  # Unlock via BLE
python ble_control.py lock    # Lock via BLE
```

### 3. `check_lock_status.py` - Combined API + BLE Status
**What it does:** Gets lock info from API, then attempts BLE status update
**Note:** Currently attempts BLE connection which may time out

## Configuration

Edit `config.py` with your credentials:
```python
EMAIL = "your@email.com"
PASSWORD = "your_password"
LOCK_NAME = "Your Lock Name"
```

## BLE Connection Notes

- Ultraloq locks enter power-save mode and may not accept BLE connections immediately
- If you have a Utec bridge, it may hold the BLE connection
- Touch the lock keypad to wake it before BLE commands
- BLE works best when lock is actively being used

## Recommended Usage

- **Daily monitoring:** Use `api_status.py` (reliable, always works)
- **Direct control:** Use `ble_control.py` when near the lock
- **Testing BLE:** Wake lock first (touch keypad) then run ble_control.py

